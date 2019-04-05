from rasa_nlu.model import Interpreter

model_directory = "../models/nlu/default/stable"
interpreter = Interpreter.load(model_directory)

while(True):
	raw = input("YOU --> ")
	print("BOT --> " , interpreter.parse(raw))