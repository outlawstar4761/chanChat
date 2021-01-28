# __main__.py
from ChanParser.ChanParser import ChanParser

def _readFile(path):
    f = open(path)
    html = f.read()
    f.close()
    return html

def main():
    """
    Parse archived 4Chan HTML into conversations.
    """
    #path = input("Path to HTML: ")
    path = '/media/outlaw/BlackBox1/archive.4plebs.org/pol/302272112/302272112.html'
    html = _readFile(path)
    parser = ChanParser(html)
    print(parser.title)
    print(parser.prompt)
    for post in parser.posts:
        print(post)

if __name__ == "__main__":
    main()
