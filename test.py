from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from ChanParser.ChanParser import ChanParser
from chatterbot.trainers import ChatterBotCorpusTrainer
from multiprocessing import Pool
import os
import random

def _readFile(path):
    f = open(path)
    html = f.read()
    f.close()
    return html
def _train(thread):
    html = _readFile(thread)
    parser = ChanParser(html)
    trainer = ListTrainer(chatbot)
    trainer.train(parser.posts)
def _findFiles(input):
    rootDir = input[0]
    extension = input[1]
    results = []
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            if file.endswith(extension):
                #print(os.path.join(root,file))
                results.append(os.path.join(root,file))
    return results

chatbot = ChatBot("ChanChatter")
trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train('chatterbot.corpus.english')

limit = 500
path = '/media/outlaw/BlackBox1/archive.4plebs.org/pol/'
targetData = [path,".html"]
p = Pool(os.cpu_count())
threads = p.apply(_findFiles,(targetData,))
print("Found: %s" % len(threads))
threads = random.sample(threads, limit)
p.map(_train, threads)

while True:
   data = input("Say: ")
   if(data == "stop"):
       exit()
   print(chatbot.get_response(data))
