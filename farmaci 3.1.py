#prompt comandi pip install pyperclip
#avviato terminale>tasto destro>proprietà>tipi di carattere
import pyperclip

my_list= [("kesium", "250MG 8CPR APP.",104319076),
         ("kesium", "250MG 96CPR APP.",104319088),
         ("kesium", "62,5MG 10 CPR APP.",104319013),
         ("kesium", "62,5MG 100CPR APP.",104319025),
         ("kesium", "625MG 12CPR APP.",104319140),
         ("kesium", "625MG 96CPR APP.",104319153),
         ("cefaseptin", "300MG - 10CPR CANE",104819040),
         ("cefaseptin", "750MG - 12CPR CANE",104819077),
         ("cefaseptin", "75MG - 10CPR CANE&GATTO",104819014),
         ("meloxoral", "0,5MG 10ML - GATTO",104391065),
         ("meloxoral", "1,5MG 10ML - CANE",104391053),
         ("meloxoral", "1,5MG 25ML - CANE",104391014),
         ("meloxoral", "1,5MG 50ML - CANE",104391026),
         ("decongesta", "1,25MG - 5X10CPR",104984024),
         ("decongesta", "5MG - 5X10CPR",104984051),
         ("fortekor", "FLAVOUR 2,5MG - 28CPR",101962076),
         ("fortekor", "FLAVOUR 20MG - 14CPR",101962126),
         ("fortekor", "FLAVOUR 5MG - 14CPR",101962090),
         ("fortekor", "FLAVOUR 5MG - 56CPR",101962114),
         ("fortekor", "PLUS 1,25/2,5MG 30CPR",104968019),
         ("fortekor", "PLUS 5/10MG 30CPR",104968033),
         ("cardinefril", "20MG 14CPR",104832011),
         ("cardinefril", "5MG 14CPR",104857014),
         ("cardisure", "FLAV. 5MG - 100CPR",104323199),
         ("cardisure", "FLAV. 1,25MG - 100CPR",104323035),
         ("cardisure", "FLAV. 10MG - 100CPR",104323276),
         ("cardisure", "FLAV. 2,5MG - 100CPR",104323112),
         ("cardalis", "10MG-80MG 30CPR",104541053),
         ("cardalis", "2,5MG-20MG 30CPR",104541014),
         ("cardalis", "5MG-40MG 30CPR",104541038),
         ("diuren", "30CPR",102243033),
         ("diuren", "MAXI 30CPR",102243058),
         ("diuren", "SOLUZIONE GOCCE 25ML",102243045),
         ("upcard", "0,75MG 100CPR",104919028),
         ("upcard", "0,75MG 30CPR",104919016),
         ("upcard", "3MG 100CPR",104919042),
         ("upcard", "3MG 30CPR",104919030),
         ("semintra", "SOLUZIONE ORALE 30ML",104608017),
         ("bravecto", "Cane: L 20-40KG 1X1000MG",104715103),
         ("bravecto", "Cane: M 10-20KG 1X500MG",104715077),
         ("bravecto", "Cane: S 4,5-10KG 1X250MG",104715040),
         ("bravecto", "Cane: XL 40-56KG 1X1400MG",104715139),
         ("bravecto", "Cane: XS 2-4,5KG 1X112,5MG",104715014),
         ("bravecto", "Gatto: L 1PipX500MG",104715267),
         ("bravecto", "Gatto: M 1PipX250MG",104715228),
         ("bravecto", "Gatto: S 1PipX112,5MG",104715180),
         ("bravecto", "Gatto: PLUS L 1PipX500MG",105233050),
         ("vectra", "3D CANI 1,5-4KG 3PIP.GIALLO",104687025),
         ("vectra", "3D CANI 10-25KG 3PIP.BLU",104687126),
         ("vectra", "3D CANI 25-40KG 3PIP.VIOLA",104687177),
         ("vectra", "3D CANI 4-10KG 3PIP.VERDE",104687076),
         ("vectra", "3D CANI >40KG 3PIP.ROSSO",104687227),
         ("vectra", "FELIS 3 PIPETTE",104777026),
         ("cardotek", "30 MAST. 6X136 12 KG - 22 KG MCG VERDE",100243118),
         ("cardotek", "30 MAST. 6X272 23 KG - 45 KG MCG MARRONE",100243120),
         ("cardotek", "30 MAST. 6X68 FINO A 11 KG MCG BLU",100243106),
         ("cardotek", "30 PLUS 6X136 12 - 22 KG MCG VERDE",100001027),
         ("cardotek", "30 PLUS 6X272 23 - 45 KG MCG MARRONE",100001039),
         ("cardotek", "30 PLUS 6X68 FINO A 11 KG MCG BLU",100001015),
         ("cardotek", "30 PLUS 9X68 FINO 11 KG MCG BLU",100001041),
         ("cardotek", "30 PLUS 9X272 23 KG - 45 KG MCG MARRONE",100001078),
         ("cardotek", "30 PLUS 9X136 12 KG - 22 KG MCG VERDE",100001066),
         ("afilaria", "136 8CPR ARGENTO 23-45KG",104841059),
         ("afilaria", "30 8CPR FUXIA <10KG",104841010),
         ("afilaria", "68 8CPR ORO 11-22KG",104841034),
         ("prednicortone", "20MG - 30CPR",104808011),
         ("prednicortone", "20MG - 30CPR",104808011)]

done = False

while not done:
    farmaco = input ("Inserire il nome del farmaco da ricercare: ")
    print (" ")
    i=0
    opzioni = []
    for t in my_list:
        if farmaco.lower() == t[0]:
            print (i,": ",t[1])
            opzioni.append(t)
        i += 1
        
    
    if len(opzioni) == 0:
        print (" ")
        print ("Farmaco non presente nella lista")
        continue

    print(" ")        
    scelta = int(input("Inserire il numero del farmaco desiderato: "))
    print(" ")
    num_codice=my_list[scelta][2]
    print ("Il codice è: ",num_codice)
    pyperclip.copy(num_codice)
    print("Il tuo codice è stato copiato negli appunti")             

    print(" ")
    nuovo = input("Desideri ricercare un altro farmaco? (s/n) ")
    if nuovo.lower() == "n" :
        done = True        
        

exit()
        
                









    

print (my_list)
