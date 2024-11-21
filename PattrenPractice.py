#Pattrren print Practice
#******
#******
#******
n=int(input("Enter the number of rows: "))   
for i in range(1,n+1):   
    print("* "*n) 

# print Number pattern
#11111
#22222
#33333
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()


#print Numnbers incremental

#12345
#12345
#12345

n=int(input("Enter the number of rows to print:"))
for i in range(1,n+1):
      for j in range(1,n+1):
          print(j,end=" ")
      print()


#Pattern-4:  
 
#A A A A A A A A A A 
#B B B B B B B B B B 
#C C C C C C C C C C 
#D D D D D D D D D D


n=int(input("Enter the number of rows to print:"))

for i in range(1,n+1):
    for j in range(1,j+1):
        print(chr(64+i),end=" ")
    print()
    
#Pattern-5:  
 
#A B C D E F G H I J 
#A B C D E F G H I J 
#A B C D E F G H I J 
#A B C D E F G H I J 


n=int(input("Enter the number of rows to print:"))

for i in range(1,n+1):
    for j in range(1,j+1):
        print(chr(64+j),end=" ")
    print()
    


