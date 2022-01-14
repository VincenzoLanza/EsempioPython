#trovare tutte le singole parole usate(non stampare doppioni) e contare quante parole singole ci sono
import requests

risultato=requests.get(url="https://jsonplaceholder.typicode.com/todos")
todos=risultato.json()
parole = set()  
for n in todos:
    titolo=n["title"]
    par=titolo.split(" ")
    for m in par:
            parole.add(m)
print(parole)
print(len(parole))

