import pyperclip

def search(my_list, farmaco):
    for i in range(len(my_list)):
        if my_list[i] == farmaco:
            return True
    return False

my_list=["kesium", "250MG 8CPR APP.",104319076,
             "kesium", "250MG 96CPR APP.",104319088,
             "kesium", "62,5MG 10 CPR APP.",104319013,
             "kesium", "62,5MG 100CPR APP.",104319025,
             "kesium", "625MG 12CPR APP.",104319140,
             "kesium", "625MG 96CPR APP.",104319153,
             "cefaseptin", "300MG - 10CPR CANE",104819040,
             "cefaseptin", "750MG - 12CPR CANE",104819077,
             "cefaseptin", "75MG - 10CPR CANE&GATTO",104819014,
             "meloxoral", "0,5MG 10ML - GATTO",104391065,
             "meloxoral", "1,5MG 10ML - CANE",104391053,
             "meloxoral", "1,5MG 25ML - CANE",104391014,
             "meloxoral", "1,5MG 50ML - CANE",104391026]

farmaco=input("Perfavore scrivi il nome del farmaco da ricercare tutto minuscolo: ")

if search(my_list, farmaco):
    print("il farmaco è presente nella lista, ecco le tipologie: ")
    i=0
    num=1
    while i<len(my_list):
        if my_list [i]==farmaco:
            print(i,my_list[i+1])
            i=i+1
        else:
            i=i+1
else:
    print("farmaco non trovato, controlla di averlo scritto correttamente e tutto..")

codice=int(input("scegli l'opzione di cui vuoi sapere il codice: "))
num_codice=my_list[codice+2]
print("il codice è:", num_codice)

pyperclip.copy(num_codice)
print("il tuo codice è stato copiato negli appunti")





