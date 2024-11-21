import re

string1="a1b4c7"

chacters1=re.findall(r"[a-zA-Z]",string1)
digits1=re.findall('\d+',string1)

for ch,di in zip(chacters1,digits1):
    print(ch*int(di),end='')

print()
print(''.join([char*num for  char,num in zip('ABC',[2,4,6])]))
