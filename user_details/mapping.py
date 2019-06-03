from .models import FillProfile

profile_list=[]
prefer_list=[]
def profile_receive(final_profile_list):
	global profile_list
	profile_list=final_profile_list

def prefer_receive(final_prefer_list):
	global prefer_list
	prefer_list=final_prefer_list

#profile_list contains all user profiles and prefer_list contains all user preferences
#first element of prefer_list is the prefernces of first user and so on.

d={}

d={
	'Indian Institute of Technology Bombay, Aerospace Engineering':[0,0] ,
	 
	'Indian Institute of Technology Bombay, Chemical Engineering':[0,1] ,
	 
	'Indian Institute of Technology Bombay, Civil Engineering':[0,2] ,
	 
	'Indian Institute of Technology Bombay, Computer Science and Engineering':[0,3] ,
	 
	'Indian Institute of Technology Bombay, Electrical Engineering':[0,4] ,
	 
	'Indian Institute of Technology Bombay, Electronics and Communication':[0,5] ,
	 
	'Indian Institute of Technology Bombay, Mechanical Engineering':[0,6] ,
	 
	'Indian Institute of Technology Delhi, Aerospace Engineering':[1,0] ,
	 
	'Indian Institute of Technology Delhi, Chemical Engineering':[1,1] ,
	 
	'Indian Institute of Technology Delhi, Civil Engineering':[1,2] ,
	 
	'Indian Institute of Technology Delhi, Computer Science and Engineering':[1,3] ,
	 
	'Indian Institute of Technology Delhi, Electrical Engineering':[1,4] ,
	 
	'Indian Institute of Technology Delhi, Electronics and Communication':[1,5] ,
	 
	'Indian Institute of Technology Delhi, Mechanical Engineering':[1,6] ,
	 
	'National Institute of Technology Surathkal, Chemical Engineering':[2,0] ,
	 
	'National Institute of Technology Surathkal, Civil Engineering':[2,1] ,
	 
	'National Institute of Technology Surathkal, Computer Science and Engineering':[2,2] ,
	 
	'National Institute of Technology Surathkal, Electrical Engineering':[2,3] ,
	 
	'National Institute of Technology Surathkal, Electronics and Communication':[2,4] ,
	 
	'National Institute of Technology Surathkal, Information Technology':[2,5] ,
	 
	'National Institute of Technology Surathkal, Mechanical Engineering':[2,6] ,
	 
	'National Institute of Technology Trichy, Chemical Engineering':[3,0],
	 
	'National Institute of Technology Trichy, Civil Engineering':[3,1],
	 
	'National Institute of Technology Trichy, Computer Science and Engineering':[3,2],
	 
	'National Institute of Technology Trichy, Electrical Engineering':[3,3],
	 
	'National Institute of Technology Trichy, Electronics and Communication':[3,4],
	 
	'National Institute of Technology Trichy, Information Technology':[3,5],
	 
	'National Institute of Technology Trichy, Mechanical Engineering':[3,6],
	 
	'Indian Institute of Information Technology Allahabad, Computer Science and Engineering':[4,0],
	 
	'Indian Institute of Information Technology Allahabad, Electrical Engineering':[4,1],
	 
	'Indian Institute of Information Technology Allahabad, Electronics and Communication':[4,2],
	 
	'Indian Institute of Information Technology Allahabad, Information Technology':[4,3],
	 
	'Indian Institute of Information Technology Delhi, Computer Science and Engineering':[5,0],
	 
	'Indian Institute of Information Technology Delhi, Electrical Engineering':[5,1],
	 
	'Indian Institute of Information Technology Delhi, Electronics and Communication':[5,2],
	 
	'Indian Institute of Information Technology Delhi, Information Technology':[5,3],
		 
}

def send_to_algo():
	lf=[]
	d1={}
	if len(profile_list)==FillProfile.objects.all().count() and len(prefer_list)==FillProfile.objects.all().count():
		for each_user in prefer_list:
			l=[]
			for prefs_of_given_user in each_user:
				l.append(d.get(prefs_of_given_user))
			lf.append(l)

		for i in range(len(profile_list)):
			d1.update({tuple(profile_list[i]):lf[i]})

		'''l1=[]
		#d_adv={}
		d2={}
		for each in profile_list:
			l1.append(tuple(each))
		#l2=l1
		#l1.sort(key=lambda x:x[1]) #sorts wrt adv rank
		#l2.sort(key=lambda x:x[2]) #sorts wrt mains rank
		for each in l1:
			d2.update({each:d1[each]})
		'''	

		return d1	
		#send d1 to algo file		



# HAVE if CONDITION OF SENDING profile_list to algo only when count is 4	