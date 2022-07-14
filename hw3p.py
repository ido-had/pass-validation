from statistics import mean,median

def split_male_female(members:dict)->tuple():
     """
     This function gets a nested dictionary and split and returns male and female dictionary
     :param members:nested dictionary contains detailed members for collecting male and female members
     :return: Separated dict by sex
     """
     male={}
     female={}
     for index in members:
         if members[index]["sex"]=="male":
             male[index]=members[index]
         else:
             female[index]=members[index]
     return male,female

# def insert_member(members:dict):
#     """
#     Inserting a new member to the data set
#     :param members: nested dictionary contains detailed members
#     """
#     data=input("Please enter member Id,Name,Sex,age in this order followed by a space between:")
#     lst_data=data.rsplit(" ")
#     try:
#         id_num=lst_data[0]
#         members[id_num]={}
#         members[id_num]['name']=lst_data[1]
#         members[id_num]['sex']=lst_data[2]
#         members[id_num]['age']=int(lst_data[3])
#     except IndexError:
#         print("Wrong input-missing data ")
#     except:
#         print("wrong input ")

def find_median_average(members:dict):
    """
    Calculating and printing median and average age in data members
    :param members: nested dictionary contains detailed members
    """
    if len(members)>0:
        lst_age=[] #this list will store all ages of members
        for index in members:
            lst_age.append(members[index]["age"])
        try:
            print("The average age of members is:"+str(mean(lst_age)))
            print("The median age of members is"+str(median(lst_age)))
        except : #age list contains a non int value
            print("Some data is probably corrupted ")

def print_values_above(members:dict,age:int=-1):
    """
    printing members in members dict above or all certain age
    :param members: members-nested dict contains detailed member data
    :param age: optional integer.default value=-1 the minimum age of a member to
    be printed.if not used prints all members
    """
    if len(members)==0:
        print("There are no members")
    for index,values in members.items():
            if members[index]["age"]>age:
              print(index,values)

def main():
    """
    main function of this model allows user to choose different action such as printing members etc
    """
    members ={3322117:{"name": "Tal", "sex": "male", "age": 12},
              176864301:{"sex": "female", "age": 57, "height": 1.65,"name": "Anat"}}
   # members={}
    male,female=split_male_female(members)
    find_median_average(members)
    print_values_above(members)






main()