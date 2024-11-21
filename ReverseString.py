list1=[4,7,9,2]
list1.reverse()
print(list1)

#Slicing 
list2=list1[::-1]
print(list2)

#Reversed

list3=list(reversed(list1))
print(list3)

#for loop
list4=[]
for i in  range(len(list1)--1,1,-1):
    list4.append(list1[i])
print(list4)

list5=[]
lst="VENKY"
#list1=list(lst)
for i in  range(len(lst)-1,-1,-1):
    list5.append(lst[i])
print(list5)
