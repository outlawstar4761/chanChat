from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from ChanParser.ChanParser import ChanParser
from chatterbot.trainers import ChatterBotCorpusTrainer

def _readFile(path):
    f = open(path)
    html = f.read()
    f.close()
    return html

chatbot = ChatBot("ChanChatter")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

threads = [
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293176174/293176174.html',
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293192259/293192259.html',
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293199125/293199125.html',
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293206224/293206224.html',
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293213332/293213332.html',
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293213534/293213534.html',
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293214560/293214560.html',
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293215202/293215202.html',
    '/media/outlaw/BlackBox1/archive.4plebs.org/pol/293215692/293215692.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79653672/79653672.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79676249/79676249.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79679605/79679605.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79682719/79682719.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79686390/79686390.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79687668/79687668.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79688031/79688031.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79693414/79693414.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79694546/79694546.html',
    '/media/outlaw/BlackBox1/boards.4channel.org/g/79695091/79695091.html'
]


for thread in threads:
    html = _readFile(thread)
    parser = ChanParser(html)
    trainer = ListTrainer(chatbot)
    trainer.train(parser.posts)

while True:
   data = input("Say: ")
   print(chatbot.get_response(data))
