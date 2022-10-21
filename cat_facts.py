import time
import json
import requests



def requestFact():
    data = requests.get('https://the-cat-fact.herokuapp.com/api/randomfact')
    d = data.json()
    fact = json.dumps(d, sort_keys = 4, indent = 4, ensure_ascii = False)
    x = fact.index("{",2) + 23
    y = fact.index("}",2) - 10
    fact1 = fact[x:y]
    return fact1




