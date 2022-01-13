#contare per ogni parola quante volte appare e stamparle dalle più alla meno frequente 
from collections import OrderedDict
import requests

risultato=requests.get(url="https://jsonplaceholder.typicode.com/todos")
todos=risultato.json()
parole_diz = {}
for n in todos:
    titolo=n["title"]
    parole=titolo.split(" ")
    for parola in parole:
        if parola in parole_diz:
            parole_diz[parola] +=1
        else:
            parole_diz[parola]=1
item_dizionario=parole_diz.items()
lista_valori_dizionario =list(item_dizionario)
def get_valore (elem):
    return elem[1]
    # return elem.get()
lista_valori_dizionario.sort(key=get_valore,reverse=True)
print(lista_valori_dizionario)
# parole_diz=OrderedDict(sorted(parole_diz.items(), reverse=True, key=lambda t: t[1]))
# for key,value in parole_diz.items():
#     print(key,value)
