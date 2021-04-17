my_list = [("cazzi","mazzi","belli"),("cazzi2","mazzi2","belli2"),("cazzi","mazzi3","belli3")]

done = False

while not done: #SALTO QUI SE SONO CONTINUE
    farmaco = input("Che farmaco vuoi?")
    i = 0
    for t in my_list:
        temp = []
        if farmaco == t[0]:
            print(i,". ",t[1])
            temp.append(t)
        i += 1
    
    if len(temp) == 0:
        print("Hai sbagliato a inserire il farmaco")
        continue

    selezione = int(input("Cosa selezioni"))
    print(my_list[selezione][2])

    scelta = input("Vuoi uscire (s/n): ")
    if scelta.lower() == "s":
        done = True
        print("Sto uscendo...")

#SALTO QUI SE SONO BREAK


exit()







