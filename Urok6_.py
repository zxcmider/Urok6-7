nimed=["Anna","Inna"]
for i in range(3): #сколько раз можно ввести свое имя в список
    nimi=input("Sisesta nimi: ")
    nimed.append(nimi) #добавляет вписанное тобою имя в список nimed
print(nimed)
nimed.sort(reverse=True) #сортирует имена по алфавиту а reverse отражает написанное
print(nimed)
nimed.insert(1,input("Sisesta veel nimi")) #куда именно поставить вписанное имя вписанное  имя поставится на 2 место
print(nimed)
nimed.remove("Anna") #кого удалить из списка
print(nimed)
nimed.pop(2)
print(nimed)
print(len(nimed)) #считает сколько осталось имен в списке
nimed.count(nimed[0]) #какое имя первое в списке


uezdi=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while 1:
    try:
        index=int(input("Введите адресс: "))
        if 10000<=index<=99999:
            break
    except ValueError:
                print("Vale index!")
index_1=index//10000
print(uezdi[index_1-1])
if index[1,2,3]:
    print("Оставайтесь дома!")
else:
    print("Носите Маски!")



from random import *
spisok=[]
N=randint(2,20)
for i in range(N):
    spisok.append(randint(-50,50))
print(spisok)
while 1:
    try:

        k=int(input("Mis positsioonist alustada vahetust"))
        if k<=N//2:
            break
    except ValueError:
        print("Arv Peab olema vaiksem kui",N//2)
k-=1
for i in range(k,-1,-1):
    print(spisok[i],end="<+>")
    print(spisok[N-i-1])
    a=spisok.pop(i)
    spisok.insert(N-i-1-1,a)
    a=spisok.pop(N-i-1)
    spisok.instert(i,a)
print(spisok)
max=-50
for element in spisok:
    if element>max: max=element
new_max=max/N #len(spisok)
spisok.index(max)
spisok.remove(max)
spisok.insert(int,new_max)
print(spisok)
spisok2=[]
for e in spisok:
    spisok2.append(abs(e))
print(spisok2.sort())
print(spisok2.sort(reverse=True))
