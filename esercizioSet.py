#trovare tutte le singole parole usate(non stampare doppioni) e contare quante parole singole ci sono
#contare per ogni parola quante volte appare e stamparle dalle più alla meno frequente 
import requests

risultato=requests.get(url="https://jsonplaceholder.typicode.com/todos")
todos=risultato.json()
parole = set()
ultima_parola= None
for n in todos:
    titolo=n["title"]
    par=titolo.split(" ")
    for m in par:
        if m != ultima_parola:
            parole.add(m)
            ultima_parola=m
print(len(parole))
# print(len(parole))

