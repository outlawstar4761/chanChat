from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

class ChanChat:
    def __init__(self):
        self.chatbot = ChatBot("ChanChatter")
        self._baseTrain()
    def _baseTrain(self):
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train('chatterbot.corpus.english')
    def train(self,conversation):
        trainer = ListTrainer(self.chatbot)
        trainer.train(conversation)
    def getResponse(self,input):
        return self.chatbot.get_response(input)
