__author__ = 'marino'
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib
import httplib2

#usare mechanize o selenium ??
#http://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet/
#
listadocumenti = []
debug = False
document = 'http://www.di.unito.it/~goy/'

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'link':
            if attrs[0][0] != "STYLESHEET":
                if debug:
                    print 'trovata tag link'
                for att in attrs:
                    if att[0] == 'href':
                        listadocumenti.append(att[1])
          #  exit()
        if tag == 'a':
            if debug:
                print 'trovata tag  a'
            for att in attrs:
                if att[0] == 'href':
                    listadocumenti.append(att[1])
            if debug:
                print attrs[0]
          #  exit()
        if tag == 'img':
            if debug:
                print 'trovata tag  img'
            for att in attrs:
                if att[0] == 'src':
                    listadocumenti.append(att[1])
#        print "Start tag:", tag
#        for attr in attrs:
 #           print "     attr:", attr
    def handle_endtag(self, tag):
        if debug:
            print "End tag  :", tag
    def handle_data(self, data):
        if debug:
            print "Data     :", data
    def handle_comment(self, data):
        if debug:
            print "Comment  :", data
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])
        if debug:
            print "Named ent:", c
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        if debug:
            print "Num ent  :", c
    def handle_decl(self, data):
        if debug:
            print "Decl     :", data

parser = MyHTMLParser()

#parser.feed('<img src="python-logo.png" alt="The Python logo">')

filehandle = urllib.urlopen(document)
contenuto = filehandle.read()
print 'input length = ', len(contenuto)
parser.feed(contenuto)
print 'lista documenti collegati a:' +document +'\n\n'
for elem in    listadocumenti:
    print elem
#DDDDDDDDDDDDDDDDDDDDDDDD
filehandle.close()

print '\n\ndocumenti da file pdf convertito a html\n'
listadocumenti = []
with open ("/home/marino/PycharmProjects/sem/samples/provahtml.html", "r") as myfile:
    data=myfile.read()
    parser.feed(data)
for elem in    listadocumenti:
    print elem