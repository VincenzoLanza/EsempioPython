import requests
risultato=requests.get(url="https://jsonplaceholder.typicode.com/todos")
print(risultato.json())