from rasa_core.agent import Agent
from rasa_core.utils import EndpointConfig

model_directory = "./models/nlu/default/stable"
agent = Agent.load('./models/dialouge', interpreter=model_directory,action_endpoint=EndpointConfig(url="http://localhost:5055/webhook"))

print("Bot is ready to chat. type ur msg or 'stop' to end the convo")
while True:
	a = input("YOU -> ")
	if a=="stop": break
	responses = agent.handle_message(a)
	for response in responses:
		print("BOT -> " , responses[0]['text'])
