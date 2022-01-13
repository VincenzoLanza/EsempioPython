# chiedere all'utente input : 1 per cercare (usare output come input per secondo input che chiede chi cercare(se trovo stampo numero sennò stampare "numero inesistente")), 
# 2 per aggiungere numero di telefono alla rubrica (usare output come input per secondo input chiedendo prima il nome e poi il numero e lo salvo nel dizionario(rubrica)), 3 esci
# rubrica={
#     "Luca":3397628321,
#     "Bernardo":234234234234
# }

# print(rubrica)

# print(rubrica["Luca"])

# rubrica["Vincenzo"] = 123123123123

# print(rubrica["Vincenzo"])

# print(rubrica)

# print("Vincenzo" in rubrica)

# name = "Vincenzo"

# print(f"{name} : {rubrica[name]}")
rubrica={
    "Mario":3338383838,
}
while (True):
    menu=int(input("Scegli 1 per cercare una persona \n 2 per aggiungere una persona \n 3 per uscire : "))  
    # while (menu == 1 or menu == 2 or menu == 3):
    if menu == 1:
        cerca_persona=input("Chi stai cercando? ")
        print()
        if  cerca_persona in rubrica:      
            print(rubrica[cerca_persona])
        else: 
            print("persona non registrata alla rubrica \n")
    elif menu == 2:
        nome_input=input("Inserisci il nome della persona ")
        numero_input=int(input("Inserisci il numero della persona "))
        print()
        rubrica[nome_input]=numero_input
        print(rubrica)
    elif menu == 3:
        exit()
    else: 
        print("opzione sbagliata riscegli")
