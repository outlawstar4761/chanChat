from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("ChanChatter")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]


trainer = ListTrainer(chatbot)
trainer.train(conversation)

while True:
    data = input("Say: ")
    print(chatbot.get_response(data))
