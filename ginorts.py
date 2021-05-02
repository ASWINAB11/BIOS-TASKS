a=str(input())
L=list()
U=list()
od=list()
even=list()
for i in a:
    if(i.islower()):
      L.append(ord(i))
    elif(i.isupper()):
      U.append(ord(i))
    else:
        if(int(i)%2==0):
          even.append(ord(i))
        else:
          od.append(ord(i))
L.sort()
U.sort()
od.sort()
even.sort()
merge=L+U+od+even
for i in merge:
    print(chr(i),end='')
