import random
lis=[]
lis2=[]
maxn=0
m=0
def generatePassword() :
    for i in range(31) :
        r = random.randint(-100,100)
        if r not in lis :
            lis.append(r)
        i+=1
    return lis
def main() :
    print('Список:',generatePassword())
main()
m=max(lis)
maxn=lis.index(m)
print('\nМаксимальне значення:',m,'\nІндекс:',maxn)
lis2 = [i for i in lis if i % 2 == 1]
if not lis2:
    print("Таких чисел немає!")
else:
    lis2.sort(reverse=True)
    print('\nНепарні числа',lis2)
