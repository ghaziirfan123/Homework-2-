#my name is mohammad ghazi irfan and my ID is 1626488

s = input()
low = 0
high = len(s)-1
result = True
while(low<high):
    if(s[low]==' '):
        low+=1
    elif(s[high]==' '):
        high-=1
    elif(s[low]!=s[high]):
        result = False
        break
    else:
        low+=1
        high-=1
if (result):
    print(s,"is a palindrome")
else:
    print(s, "is not a palindrome")