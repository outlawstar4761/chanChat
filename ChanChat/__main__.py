# __main__.py
from ChanParser.ChanParser import ChanParser
from ChanChat.ChanChat import ChanChat
import os

def _readFile(path):
    f = open(path)
    html = f.read()
    f.close()
    return html
def _findFiles(rootDir,extension):
    results = []
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            if file.endswith(extension):
                #print(os.path.join(root,file))
                results.append(os.path.join(root,file))
    return results

def main():
    """
    Train a chatbot on 4chan data and chat with it.
    """
    #path = input("Path training: ")
    # path = '/media/outlaw/BlackBox1/boards.4channel.org/g/'
    path = '/media/outlaw/BlackBox1/archive.4plebs.org/pol/'
    threads = _findFiles(path,".html")
    chatbot = ChanChat()
    print('Attempting to train on %s threads' % len(threads))
    i = 0
    for thread in threads:
        #print(i)
        i += 1
        html = _readFile(thread)
        parser = ChanParser(html)
        if(len(parser.posts)):
            chatbot.train(parser.posts)
    while True:
        data = input("Say: ")
        print(chatbot.getResponse(data))


if __name__ == "__main__":
    main()
