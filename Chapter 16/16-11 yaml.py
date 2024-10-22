import yaml

with open('mcintyre.yaml', 'rt') as fin :
	text = fin.read()
data = yaml.safe_load(text)

print(data['details'])
print(len(data['poems']))
print("")
print("--", data['poems'][1]['title'], "--")
print(data['poems'][1]['text'])