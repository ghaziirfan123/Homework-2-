#my name is Mohammad Ghazi Irfan and my ID is 1626488

passwd=input() # taking the simple password as input

passwd=list(passwd) # converting string to list

for i in range(0,len(passwd)): # iterating for changing characters
    if(passwd[i]=='i'):
        passwd[i]='!'
    elif(passwd[i]=='a'):
        passwd[i]='@'
    elif(passwd[i]=='m'):
        passwd[i]='M'
    elif(passwd[i]=='B'):
        passwd[i]='8'
    elif(passwd[i]=='o'):
        passwd[i]='.'

strong_password=""
strong_password=strong_password.join(passwd) # converting list to string

strong_password=strong_password+"q*s" # appending "q*s" at end

print(strong_password) # printing new password