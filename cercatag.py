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
            primoelem = attrs[0]
            if debug:
                print primoelem[0], ' ', primoelem[1]
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

filehandle = urllib.urlopen('http://www.di.unito.it/~giovanna/')#
#filehandle = urllib.urlopen('http://www.gulliver.it/home/index.html')


contenuto = filehandle.read()
print 'input length = ', len(contenuto)
parser.feed(contenuto)
print 'lista documenti collegati a:' +'http://www.di.unito.it/~giovanna/'
for elem in    listadocumenti:
    print elem

filehandle.close()

