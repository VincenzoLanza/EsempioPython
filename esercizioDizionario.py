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
import json
file_json=open("Rubrica.json", "r")
loaded_rubrica=json.load(file_json)
exit=False
while (exit==False):
    menu=int(input("Scegli 1 per cercare una persona \n 2 per aggiungere una persona \n 3 per uscire : "))  
    #while (menu == 1 or menu == 2 or menu == 3):
    if menu == 1:
        cerca_persona=input("Chi stai cercando? ")
        if cerca_persona in loaded_rubrica:
            nome=loaded_rubrica[cerca_persona]["nome"]
            cognome=loaded_rubrica[cerca_persona]["cognome"]
            numero_tel=loaded_rubrica[cerca_persona]["num_tel"]
            indirizzo=loaded_rubrica[cerca_persona]["indirizzo"]         
            print()
            print(f"Nome: {nome}, Cognome: {cognome}, Numero: {numero_tel}, Indirizzo: {indirizzo}")
        else:
            print()
            print("persona non registrata alla rubrica \n")
    elif menu == 2:
        diz_interno={}
        diz_interno_2={}
        nome_input=input("Inserisci il nome della persona ")
        cognome_input=input("Inserisci il cognome della persona ")
        numero_input=int(input("Inserisci il numero della persona "))
        
        indirizzo_input=int(input)("Inserisci l'indirizzo della persona ")
        print()
        diz_interno["nome"]=nome_input
        diz_interno["cognome"]=cognome_input
        diz_interno["num_tel"]=numero_input
        diz_interno["indirizzo"]=indirizzo_input
        loaded_rubrica[nome_input]=diz_interno
        print(loaded_rubrica)
    elif menu == 3:
        exit=True
    else: 
        print("opzione sbagliata riscegli")

with open("Rubrica.json", "w") as jsonFile:
    data = json.dump(loaded_rubrica,jsonFile)
