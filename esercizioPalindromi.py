import json
file_json=open("names.json")
json_file=json.load(file_json)
names={}
for row in json_file:
    dictionary_nome=row["nome"]
    if dictionary_nome==dictionary_nome[::-1]:
        names[dictionary_nome]=row
with open("nomiPalindromi.json","w") as outfile:
    json.dump(names,outfile)
