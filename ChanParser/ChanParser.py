from bs4 import BeautifulSoup
import re


#I want to be able to use quote tags to build more accurate conversations
#Cleanup post string
#i.e green-text,quote tags, new lines?

class ChanParser:
    def __init__(self,html):
        self.soup = BeautifulSoup(html,features="lxml")
        #self.title = self._title()
        #self.prompt = self._prompt()
        self.posts = self._posts()
    def _title(self):
        return self.soup.find('h2','post_title').get_text()
    def _prompt(self):
        return self.soup.find('div','text').get_text()
    def _cleanPost(self,postStr):
        return re.sub('\n','',re.sub('>>.*','',postStr));
    def _posts(self):
        html = self.soup.findAll('div','post_wrapper')
        posts = []
        for post in html:
            posts.append(self._cleanPost(post.find('div','text').get_text(separator="\n")))
        return posts
    #def _convesate(self,post[?host to be structured, probably not plain text]): return a nested list of conversations
