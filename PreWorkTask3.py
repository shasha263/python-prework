#Question1

def hello_name(user_name="USERNAME"):
    user_name=input("WHAt is your User NAme?:")
    if user_name== "USERNAME":
        print("hello_" + user_name +"!")
    else:
        print("Enter the correct Username")
  
hello_name()

#Question 2:

def first_odds():
   for number in range(1,101,2):
        print(number)
                        
first_odds()


#Question 3:
def max_num_in_list(a_list):
    max_number= max(a_list)
    print(max_number) 
 
my4_list=[23,54,55,4,34,66]
max_num_in_list(my4_list)

#Question 4:

def is_leap_year(a_year="2020"):
    a_year=input("Enter the year:")
    if int(a_year)%4==0 and int(a_year)%100!=0:
        print("True")
    else:
        print("False")     
    
is_leap_year()

#Question 5:

my5_list=[7,2,3,4,5]
def is_consecutive(a_list):
    min_number=min(a_list)    
    max_number=max(a_list)
   
    new_list = [*range(min_number, max_number+1, 1)]
 
    if a_list == new_list:
       print("True")
    else:
       print("False") 
        
is_consecutive(my5_list)


        
     
        


        

