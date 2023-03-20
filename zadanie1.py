liczby=input("Podaj liczby rozdzielone przecinikiem")

for i in range(0, len(liczby)):
    lista=liczby.split(",")

min=lista[0]
max=lista[0]
for i in range(0,len(lista)):
    if lista[i]<min:
        min=lista[i]
    elif lista[i]>max:
        max=lista[i]

print("Max= "+max+" Min= "+min)