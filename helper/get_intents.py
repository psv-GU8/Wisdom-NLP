data = ''
with open('../data/nlu_train.md', 'r') as f: data = f.readlines()

intents = ''
for i in data: 
	if('##' in i): intents += "- " + str(i.split(":")[1])

print(intents)