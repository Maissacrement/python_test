
import json

r = open('fichier.json').read()
print(r)
data = json.loads(r)
print(data)
print(data['income'])
'#donne = json.load(r)'
'#print(donne)'
