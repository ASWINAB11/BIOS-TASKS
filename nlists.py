marks=[]
scoreboard=[]
for _ in range(int(input())):
    studname = input()
    studscore = float(input())
    marks+=[[studname,studscore]]
    scoreboard+=[studscore]
y=sorted(list(set(scoreboard)))[1]
for x,z in sorted(marks):
    if z==y :
        print(x)
