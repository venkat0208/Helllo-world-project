#Whether Sting is polindrom or not

str=input("enter sttring to check:")
if str == str[::-1]:
    print("Given string is polindrome")
else:
    print("Given string is not a pplindrome")



#2nd method
n = len(str)
x = 0


#while loop
def Polindrome(S):
    l=len(S)
    first = 0
    last = l-1
    while (first<last):
        if S[first] == S[last]:
            print(S[first],S[last])
            first += 1
            last -= 1
        else:
            return False
    return True


print(Polindrome(""))