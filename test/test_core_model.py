from rasa_core.agent import Agent

model_directory = "../models/nlu/default/stable"
agent = Agent.load('../models/dialouge', interpreter=model_directory)

print("Bot is ready to chat. type ur msg or 'stop' to end the convo")
while True:
	a = input()
	if a=="stop": break
	responses = agent.handle_message(a)
	print(responses)
	for response in responses:
		print(responses[0]['text'])
