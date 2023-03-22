import random
listaMiast = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
planWycieczki = []
zmniejszanie = 0;
for i in range(0, len(listaMiast)):
    index = random.randint(0, 9-zmniejszanie)
    print(index)
    planWycieczki.append(listaMiast[index])
    del listaMiast[index]
    zmniejszanie += 1


print(planWycieczki)
