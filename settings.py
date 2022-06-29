import json

f = open('settings.json')

Settings = json.load(f)

f.close()
