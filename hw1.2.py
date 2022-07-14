

lst1=["a","b","c","d"]
lst2=["x","y","z","w"]
lst_res=[]
for i in range(1,len(lst1)+1):
    lst_res.append(lst1[i-1]+lst2[-i])


print(lst_res)