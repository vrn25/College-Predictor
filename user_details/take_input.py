preference_list_of_user=[]
profile_list_of_user=[]



def give_profile(prof_list):
    global profile_list_of_user
    profile_list_of_user.append(prof_list)
    return profile_list_of_user

def give_prefer(pref_list):
    global preference_list_of_user
    preference_list_of_user.append(pref_list)
    return preference_list_of_user

