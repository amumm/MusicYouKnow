import urllib.request
from html.parser import HTMLParser
from random import randint

def getYear(year):
    urlText = []


    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag =='a':
                urlText.append(attrs)



    thisurl = "http://top40charts.net/"

    with urllib.request.urlopen(thisurl) as url:
        s=url.read()


    parser=MyHTMLParser()
    parser.feed(s.decode("utf-8"))
    for i in urlText:
        if str(year)+"-m" in i[0][1]:
            return str(i[0][1])

def getTop40(thisurl):
    urlText = []
    result=[]

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag =='a':
                urlText.append(attrs)


    with urllib.request.urlopen(thisurl) as url:
        s=url.read()

    parser=MyHTMLParser()
    parser.feed(s.decode("utf-8"))
    for i in urlText:
        if "youtube.com" in i[0][1]:
            result.append(i[0][1])
    #return result[6]
    return result[randint(0,39)]

def getVideo(topVid):
    urlText = []
    result=[]

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag =='a':
                urlText.append(attrs)



    thisurl = topVid

    with urllib.request.urlopen(thisurl) as url:
        s=url.read()


    parser=MyHTMLParser()
    parser.feed(s.decode("utf-8"))

    for i in urlText:
        if "watch?" in i[0][1]:
           result.append(i[0][1])

    return "http://www.youtube.com"+ result[0]

def getEmbedCode(url):
    urlText = []
    result = []

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "link":
                urlText.append(attrs)



    thisurl = url

    with urllib.request.urlopen(thisurl) as url:
        s=url.read()


    parser=MyHTMLParser()
    parser.feed(s.decode("utf-8"))

    for i in urlText:
        for j in i:
            for k in j:
                if "youtube.com/embed" in k:
                    result.append(k)

    return(result[0])

def crawl(input):

    year = getYear(input).strip()

    top40 = getTop40(year).strip()
    top40 = "".join(top40.split()) #remove whitespace

    video = getVideo(top40).strip()
    embedCode = (getEmbedCode(video)).strip()
    return embedCode

#crawl(2014)
