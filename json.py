book = {}

book['Ankush'] = {
    'name': 'Ankush',
    'Address': 'Dattanagar',
    'Phone': 8378807384
    }
book['Muskan'] = {
    'name': 'Muskan',
    'Address': 'Dattanagar',
    'Phone': 8956687568
    }
import json
s = json.dumps(book)
print(s)

with open("C:\Users\Ankush\Documents\JUPYTER NOTEBOOKS","w") as f:
    f.write(s)