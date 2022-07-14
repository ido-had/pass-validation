#this function gets a list and returns true if it has duplicated content. also prints every duplicated member
def check_list (lists):
    has_duplicates=False
    set1=set() #stores the list as a set
    duplicated=set() # stores duplicated content for ordered printing
    for i in lists:
        tmp_len=len(set1)
        set1.add(i)
        if len(set1)==tmp_len: #the set didnt change its length so the current item is already in the set
            duplicated.add(i) #adding current duplicated member to the duplicated set
            has_duplicates=True
    if has_duplicates:
        print("List "+str(lists)+ " has the following duplication:"+str(duplicated))
    return has_duplicates


lst1=[1,2,3,4]
lst2=[6,7,8,4]
lst3=[1,2,3,4]
raw_list=[lst1,lst2,lst3]    #list of lists that for future check
non_dup_lst=[]
for lst in raw_list:
    if not check_list(lst):
        non_dup_lst.append(lst)

output_set=set()
for i in range(len(non_dup_lst)):
    if i==0: #output set must have at least one list or else the intersction will result empty in any case
        output_set=set(non_dup_lst[i])
    output_set=output_set.intersection(set(non_dup_lst[i]))
print("intersction of non duplicated lists is:"+str(output_set))









