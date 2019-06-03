preference_list_of_user=[]
def give(def_list):
	Def=def_list
	global preference_list_of_user
	preference_list_of_user=Def
	return Def

def give_to_model():
	return preference_list_of_user