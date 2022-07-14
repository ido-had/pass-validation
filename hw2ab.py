s="asdasdkj23kjh56kjh67kjh2134kjh7kjh345kjh234"
dic={}
for c in s:
    dic[c]=dic.get(c,0) +1
print(sorted(dic.items()))

reversed_dic={}
temp_list=[]
for k,v in dic.items():
    temp_list=reversed_dic.get(v,[]) #getting the current list of the current value
    temp_list.append(k)   #adding the char to the list
    reversed_dic[v]=temp_list #placing the updated list for the matched key


print(reversed_dic.items())





