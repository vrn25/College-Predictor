from .models import FillProfile
final_dict={}
keys_in_dict=[]
cat_list=[]
list_of_username=[]

def input_to_algo(d):
    global final_dict
    final_dict=d

    '''global keys_in_dict

    for key in final_dict:
        keys_in_dict.append(key)'''

    q=[]
    for key in final_dict:
        q.append(key)

    global keys_in_dict
    keys_in_dict.append(q[-1])

    #after input_algo is executed, final_dict will contain all prof+pref
#keys_in_dict[-1][5]
    #creating list of enumerated list of category
    global cat_list
    
    if keys_in_dict[-1][5]=='general':
        cat_list.append(0)
    elif keys_in_dict[-1][5]=='obc':
        cat_list.append(1)
    elif keys_in_dict[-1][5]=='sc':
        cat_list.append(2)
    elif keys_in_dict[-1][5]=='st':
        cat_list.append(3)

def fun_username(l):
    global list_of_usernames
    list_of_usernames=l


def execute_algo():
    class student:
        def __init__(self, rno, name ,main_rank, adv_rank, cat,pref):
    #preferences is a list of numbers corresponding to a course
    #in cat 0-General, 1-OBC, 2-SC, 3- ST 
            self.rno=rno
            self.name=name
            self.main_rank=main_rank
            self.adv_rank=adv_rank
            self.cat=cat           
            self.pref=pref
            self.tba=0
            self.tg=0
            
    class batch:
        def __init__(self, vac_seats, ids):
            self.vac_seats=vac_seats
            self.ids=ids
        
    #add student details to this list
    stl=[]
    #To Add A Student do-

    #FIRST DIGIT
    #IIT Bombay is 0
    #IIT Delhi is 1
    #IIT Madras is 2
    #IIT Kanpur is 3
    #IIT Kharagpur is 4
    #NIT Trichy is 5
    #NIT Warnagal is 6
    #NITK Surathkal is 7

    #SECOND DIGIT
    #Computer Science Engineering is 0
    #Electrical Engineering is 1
    #Mechanical Engineering is 2
    #Civil Engineering is 3
    #Chemical Engineering is 4
    #Aerospace Engineering is 5
    #Engineering Physics is 6
    #Metallurgical Engineering and Materials Science is 7

    #For eg a preference10 can be [2,3] i.e., IIT Madras Civil
    for x in range(FillProfile.objects.all().count()):
        stl.append(student(x, list_of_usernames[x] ,keys_in_dict[x][2] , keys_in_dict[x][1] , cat_list[x] , final_dict[keys_in_dict[x]] )) 
         #rollcall,name,adv,mains,cat,pref
    #[-1,-1] signifies "NO ALLOTMENT" and should always be added at the end
    print(stl)
    print(list(stl))
    nos=[5,3,1,1]
    seats = [[batch([nos[0],nos[1],nos[2],nos[3]],[[],[],[],[]]) for j in range(11)] for i in range(11)]

    #nit_seats = [[nit_batch([25,13,8,4,25,13,8,4],[[],[],[],[],[],[],[],[]]) for j in range(11)] for i in range(11)]

    def allot(i):
        flag=0
        if stl[i].pref[stl[i].tba][0]==-1:
            return
    #trying to get in thru general
        if (not seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0]) or (stl[seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0][-1]].adv_rank<stl[i].adv_rank and seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]>0):
            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0].append(i)
            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]-=1
            flag=1
        else :
            j=0

            if stl[i].pref[stl[i].tba][0]<=4:
                for x in seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0] :
                    if stl[x].adv_rank>stl[i].adv_rank:
                        seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0].insert(j, i)
                        flag=1
                        seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]-=1
                        break
                    j+=1
            else:
                for x in seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0] :
                    if stl[x].main_rank>stl[i].main_rank:
                        seats[stl[i].pref[stl[i].tba][1]][stl[i].pref[stl[i].tba][2]].ids[0].insert(j, i)
                        flag=1
                        seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]-=1
                        break
                    j+=1

        if flag==1: 
            if seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]==-1:
                seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[0]=0

                ko=seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0][-1]
                seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[0].pop()
                allot(ko)
            return


    #trying to get thru category
        if stl[i].cat!=0:
            if (not seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat]) or (stl[seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat][-1]].adv_rank<stl[i].adv_rank and seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]>0):
                seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat].append(i)
                seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]-=1
                flag=1
            else :
                j=0
                flag=0
                if stl[i].pref[stl[i].tba][0]<=4:
                    for x in seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat] :
                        if stl[x].adv_rank>stl[i].adv_rank:
                            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat].insert(j, i)
                            flag=1
                            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]-=1
                            break
                        j+=1
                else:
                    for x in seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat] :
                        if stl[x].main_rank>stl[i].main_rank:
                            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat].insert(j, i)
                            flag=1
                            seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]-=1
                            break
                        j+=1
            if flag==1: 
                if seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]==-1:
                    seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].vac_seats[stl[i].cat]=0

                    ko=seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat][-1]
                    seats[stl[i].pref[stl[i].tba][0]][stl[i].pref[stl[i].tba][1]].ids[stl[i].cat].pop()
                    allot(ko)
                return
        if flag==0:
            stl[i].tba+=1
            allot(i)

    l=len(stl)
    for i in range(l):
        allot(i)
    result_list=[]
    for i in range(l):
        result_list.append(stl[i].pref[stl[i].tba])

    give_back_result_list=[]
    '''for i in range(len(result_list)):
        give_back_list.append(0)'''

    from .mapping import d
    map_list=list(d.items()) # map_list=[('nitk',[1,0]),('iitb',[2,5])] etc. It is the list according to d imported from mapping.py 

    '''for each in map_list:
        if each[1] in result_list:
            i=result_list.index(each[1])
            give_back_list[i]=each[1]'''

    for each in result_list:
        for i in map_list:
            if i[1]==each:
                give_back_result_list.append(i[0])

    return give_back_result_list

