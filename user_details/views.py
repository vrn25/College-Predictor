from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms
from . models import FillProfile,FillPrefer,GiveResult
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
result_list=[]
l1=[]

@login_required(login_url='ACCOUNTS:login')
def profile_views(request):
    if User.objects.get(username=request.user.username) and FillProfile.objects.filter(Logged_in_user_id=request.user.id):
        return redirect('USER_DETAILS:results')
    
    else:

        if FillProfile.objects.filter(Logged_in_user_id=request.user.id):
            return redirect('USER_DETAILS:userpreferences')
        
        else:

            if request.method=='POST':
                msg1=""
                msg2=""
                form=forms.FillProfileForm(request.POST)
                if form.is_valid():
                    #if FillProfile.objects.filter(adv_air=request.user.adv_air): #TO BE WORKED ON 
                        #return redirect('USER_DETAILS:userprofile')
                    #else:
                    all_fill = FillProfile.objects.all()
                    instance=form.save(commit=False)
                    instance.Logged_in_user=request.user
                    instance.full_clean()
                    for fill in all_fill:
                        if fill.adv_air == form.cleaned_data.get('adv_air'):
                            msg2="Advanced AIR already exists"
                            return render(request,'user_details/Fillprofile.html',{'ProfileForm':form,'msg2':msg2})
                    for fill in all_fill:
                        if fill.mains_air == form.cleaned_data.get('mains_air'):
                            msg1="Mains AIR already exists"
                            return render(request,'user_details/Fillprofile.html',{'ProfileForm':form,'msg1':msg1})
                    instance.save()
                    global l1
                    l1.append(str(request.user.username))
                    profile=list(FillProfile.objects.filter(Logged_in_user_id=request.user.id).values())
                    d=profile[0]
                        #global detail_list_of_user
                        #detail_list_of_user=list(d.values())
                    from .take_input import give_profile
                    final_profile_list=give_profile(list(d.values()))
                #final_profile_list contains the list of the profile of all users with each element itself as a list of username, ranks etc
                        #when 10 users would have entered their details then this final profile list would assign its value to a global
                        #variable which will be sent to the mapping file(mapping dictionary)
                    if FillProfile.objects.all().count()>0:
                        from .mapping import profile_receive
                        profile_receive(final_profile_list)
                        from .track import fun
                        fun(l1) #l1 is a list of usernames in form of a string
                    return redirect('USER_DETAILS:userpreferences')
            else:
                form=forms.FillProfileForm()
    return render(request,'user_details/Fillprofile.html',{'ProfileForm':form})

#not being executed now
@login_required(login_url='ACCOUNTS:login')
def preferences_views(request):
    if request.method=='POST':
        form=forms.FillPreferForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.Logged_in_user=request.user
            instance.save()
            return redirect('HOME:homepage')
    else:
        form=forms.FillPreferForm()
    return render(request,'user_details/Fillpreferences.html',{'PreferForm':form})


def take_json(json_string):
    import json
    x=json_string
    y=json.loads(x)
    l=list(y.values())
    l1=l[0]
    l2=l1.replace('<option>','+')
    l3=l2.replace('</option>','')

    l4=[]
    l5=[]
    for i in range(len(l3)):
        if l3[i]=='+':
            l4.append(i)

    for i in range(len(l4)):
        if i!=(len(l4)-1):
            l5.append(l3[l4[i]+1:l4[i+1]])
        else:
            l5.append(l3[l4[i]+1:])

    l6=[]
    for i in range(len(l5)):
        l6.append([l5[i],l5[i]])

    COLLEGE_SELECTED=l6
    Def=[]
    Def=l5
    return COLLEGE_SELECTED,Def


@login_required(login_url='ACCOUNTS:login')
def intermediate_view(request):
    if request.method=='POST':
        url = request.POST.get('url')
        combined_tuple=take_json(url)
        print(combined_tuple[0])
        print(combined_tuple[1])
        from .take_input import give_prefer
        final_prefer_list=give_prefer(combined_tuple[1])
        print(len(final_prefer_list))
        print(final_prefer_list)
    #final_prefer_list contains list of all users' till now preferences with each element being prefer list of a user
    #when 10 users would have entered their details then this final profile list would assign its value to a global
    #variable which will be sent to the mapping file(mapping dictionary) 
        if len(final_prefer_list)>0:
            from .mapping import prefer_receive,send_to_algo
            prefer_receive(final_prefer_list)
            final_dict=send_to_algo() #final_dict has d1 form mapping file
            from .gale_shapely import input_to_algo,execute_algo,fun_username
            print(final_dict)
            from .track import fun2
            List_of_usernames=fun2() #List_of_usernames contain all usernames in form of strings
            fun_username(List_of_usernames)
            input_to_algo(final_dict)
            global result_list
            result_list=execute_algo()
            print(len(result_list))
            print(result_list)  #result_list has allotments of all students in form of python list of strings
        return HttpResponse('<h1>hello</h1>')
    '''else:
        return render(request,'user_details/result.html')'''

@login_required(login_url='ACCOUNTS:login')
def results_view(request):
    if FillProfile.objects.all().count()>0:
        if request.method=='GET':

            if GiveResult.objects.filter(logged_in_user=request.user.id): #if user already exists(logging in not signing up)
                var=GiveResult.objects.all()
                return render(request,'user_details/result.html',{'var':var})
            
            else:

                l=result_list
                from .track import fun2
                l2=fun2() #l2 contains list of all usernames in form of strings
                print(l)
                print(l2)
                current=User.objects.get(username=request.user.username)
                GiveResult.objects.create(name=l2[-1],allotted_list=l[-1],logged_in_user=current)
                var=GiveResult.objects.all()

                '''for i in l2:
                    me.append(User.objects.get(username=i))
                for i in range(len(l)):
                    GiveResult.objects.create(name=l2[i],allotted_list=l[i],logged_in_user=me[i])
            var=GiveResult.objects.all()'''
            return render(request,'user_details/result.html',{'var':var})
                # take the global result_list and display it on an html page
    else:
        return render(request,'user_details/result_inter.html')