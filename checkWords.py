import urllib.request
import re
import os

print(os.getcwd())
currentPath = os.getcwd()
filePath = currentPath+"\movie_quotes.txt"
print(filePath)

def checkWords(word):
    with urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+word) as url:
        #print(url)
        s = url.read()
        print(s)
        if(s==b'true'):
            print("there is a profanity")
        else:
            print("all it good")

        s = url.close()
def readWords():
    txt = open(filePath)
    content = txt.read()
    contentNoSpace=re.sub(' ','%20',content)
    contentNoEnter=contentNoSpace.replace('\n', ' ').replace('\r', '')
    to_remove = " \n\t\r"
    table = {ord(char): None for char in to_remove}
    contentProcess = contentNoEnter.translate(table)
    txt.close()
    checkWords(contentProcess)
  
readWords()
