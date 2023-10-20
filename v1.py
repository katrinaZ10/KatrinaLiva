#izdrukāt skaitļus 0, 1, 2, 3, 4, 5
'''for i in range(6):#defaultā sāksies ar 0
    print(i)

print("\n...")

#iozdrukāt 3, 5, 7
for i in range(3,8,2):
    print(i)

n = int(input("Ievadīt skaitli:"))
for i in range(1,11):
    print(n,'+',i,'=',n+i)'''

print("\n...")

#atrast skaitļu 2 un 4 dalītājus
#uz eksrāna parādīt to, kas dalās ar 2, tos, kas dalās gan ar 4, gan 2
#range 50

 
for i in range((int(input("Ievadi range:"))+1)):
    if i%2==0 and i%4==0:
       print(i,":dalos ar 2 un ar 4")
    elif i%2==0:
        print(i,":dalos ar 2")
    else:
        print(i)
