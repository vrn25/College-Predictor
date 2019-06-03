from django.contrib.auth.models import User

final_dict={}

def input_to_algo(d):
    global final_dict
    final_dict=d

def execute_algo():
    pass

#after input_algo is executed, final_dict will contain all prof+pref 

class student:
    allotment="NO ALLOTMENT"
    def __init__(self, username, adv_rank, mains_rank, state, cat, pref):
#preferences is a list of numbers corresponding to a course
#in cat 0-General, 1-OBC, 2-SC, 3- ST
        self.username=username
        self.adv_rank=adv_rank
        self.mains_rank=mains_rank
        self.state=state
        self.cat=cat
        self.pref=pref
        
class iit_batch:
    def __init__(self, vac_seats_with_cat=[50,26,16,8], rnos=[]):
        self.vac_seats_with_cat=vac_seats_with_cat
        self.rnos=rnos
#class nit_batch:
#    vac_seats_with_cat=[25,13,8,4,25,13,8,4]
#    names=[]
    
#add student details
students_list=[]
#To Add A Student do-
#IIT Bombay is 0
#IIT Delhi is 1
#IIT Madras is 2
#IIT Kanpur is 3
#IIT Kharagpur is 4

#Computer Science Engineering is 0
#Computer Electrical Engineering is 1
#Mechanical Engineering is 2
#Civil Engineering is 3
#Chemical Engineering is 4
#Aerospace Engineering is 5
#Engineering Physics is 6
#Metallurgical Engineering and Materials Science is 7

#For eg a preference can be [2,3] i.e., IIT Madras Civil

for i in range(len(final_dict)):
    

for x in range(0, 200):
    students_list.append(student(x, request.user.username, detail_list_of_user[1], detail_list_of_user[5], dprefer[2]))#dprefer should be of form [2,3]
                                                                                            #presently of form just 'c1'

seats = [[iit_batch([50,26,16,8],[]) for j in range(11)] for i in range(11)]

#the student list should be sorted jeeadv rank wise
for x in students_list:
    for y in x.pref:   
# y here is a list of 2 nos eg [2,3]
        if seats[y[0]][y[1]].vac_seats_with_cat[0] != 0:
            #checks if student is getting in thru General
            seats[y[0]][y[1]].vac_seats_with_cat[0]-=1
            seats[y[0]][y[1]].rnos.append(x.rno)
            x.allotment=y
            break
        elif x.cat != 0:
            if seats[y[0]][y[1]].vac_seats_with_cat[x.cat] != 0:
                #checks if student is getting in thru category
                seats[y[0]][y[1]].vac_seats_with_cat[x.cat]-=1
                seats[y[0]][y[1]].rnos.append(x.rno)
                x.allotment=y
                break
                
        
        
    print(x.allotment)
    
    





        
            
            
            
            
                
                
                
        
    
    
  

    
    




    
    

        