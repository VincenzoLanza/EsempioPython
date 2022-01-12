import requests
import sys

risultato=requests.get(url="https://jsonplaceholder.typicode.com/todos")
todos=risultato.json()
stringhefiltrate=""
query=sys.argv[1:]
for n in todos:
    titolo=n["title"]
   #if titolo.find(query) != -1
    for m in query: 
        if m in titolo:
            stringhefiltrate += titolo + "\n"
            break
print(stringhefiltrate)

