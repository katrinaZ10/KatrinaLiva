#for cikls
'''for i in range(1,10):
    print(str(i)* i )
print()

#suņa vecums
jauns = float(10.5)
vecs = 4
vecums = int(input("Cik jūsus sunim ir gadi?"))
if vecums <3:
    print("Jūsus suņa vecums: ",vecums*jauns)
elif vecums>2:
    print("Jūsus suņa vecums: " ,2*jauns+vecums*vecs)

for i in range(1,21):
    print(str(i), ". autobusa pietura",)'''

'''lines = int(13)
for i in range(lines):
    i = "*"
    while i<7:
        print(str(i)+str(i))
    if i>7:
            print(str(i) - 1)'''

rinda = 7
for i in range(0,rinda):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")
 
for i in range(rinda, 0, -1):
    for j in range(0,i-1):
        print("*",end=" ")
    print("\r")
