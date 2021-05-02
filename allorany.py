num = list(map(int,input().split()))
c = 0
cp = 0
for element in num:
    if element > 0:
        c += 1
for i in range(len(num)):
    string = str(num[i])
    a = 0
    for j in range(len(string)//2):
        if string[j] == string[-1-j]:
            a += 1
    if a == len(string)//2:
        cp += 1
if cp > 0 and c ==len(num):
    print(True)
else:
    print(False)
