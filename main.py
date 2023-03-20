import random
import getpass

print(random.randint(0, 10))

choice = getpass.getpass("wybor: ")
print(choice)
'''

temperature = float(input("pomiar temperatury"))
if temperature < 28 or temperature > 41:
    print("uwaga! zagrozenie "+str(temperature))
else:
    print("temp "+str(temperature))

pressure="180/110"
symptom="bol w klatce piersiowej"


my_pressure=input("pomiar cisnienia")
my_sympton=input("objawy")

if my_pressure==pressure and my_sympton==symptom:
    print("Trzeba wezwac karetke")
else:
    print("niebezpieczenstwo")



#petla

while True:
    dane=input("podaj dane / end-konczy")
    if dane=="end":
        break
        print(dane)


i=0
while i< 10:
    i += 1
    if i==5:

        continue
    print(i)
    #i+=1


for i in range(0,10):
    print(i)

for i in range(0, 10):
    if i== 5:
        continue
        print(i)
'''

moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
print(len(moja_lista))

print(moja_lista[len(moja_lista)-1])

for indexx in range(0, len(moja_lista)):
    print(moja_lista[indexx])

moja_lista[indexx]= "Plock"
print(moja_lista)

moja_lista.append("Sopot")
print(moja_lista)
moja_lista.insert(0,"Katowice")
print(moja_lista)

moja_lista.extend(["nowe","nowe"])
print(moja_lista)


#usuwa ostatni elemnet
del moja_lista[-1]
del moja_lista[len(moja_lista)-1]
print(moja_lista)

misato=moja_lista.pop()
print(misato)
print(moja_lista)

indexx = moja_lista.index("Łódź")
misato = moja_lista.pop(indexx)
print(misato)
print(moja_lista)


miasto = "Warszawa"
if miasto in moja_lista:
    moja_lista.remove(miasto)
else:
    print("nie ma w liscie takiego miasta")

print(moja_lista)


moja_lista.append("Warszawa")
moja_lista.insert(0,"Warszawa")

if miasto in moja_lista:
    moja_lista.remove(miasto)
    print(moja_lista)

print(max(moja_lista))
print(min(moja_lista))

liczby = list(range(0,10,1))

for element in liczby:
    print(element)
print(max(liczby))
print(min(liczby))


cities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok"
#moja_lista = cities.split(",")