import requests
from bs4 import BeautifulSoup

##Commit 1

results = []
commitVariable = 0

def extractUrl(text):
    html = str(text)
    startIndex = str(text).find("http")

    endIndex = 0
    i = 0

    while(endIndex == 0):
        if (html[startIndex + i] == "\"") or (html[startIndex + i] == "&"):
            endIndex = startIndex + i
        else:
            i = i + 1


    return (html[startIndex:endIndex])


def getTitle(url):
    request = requests.get(url)
    parser = BeautifulSoup(request.text, 'html.parser')
    return parser.title.text

def traverse(index):
    query = input("Is this what you're looking for? [y/n] \n" + getTitle(results[index]) + "\n" + "Response: ")

    if query == "y":
        return (results[index])
    elif query == "n":
        if(index + 1 < len(results)):
            traverse(index + 1)
    elif query == "exit":
        return("bet")

def start(name):
    #Command Line Input
    #name = input("Query: ")

    fill = name.replace(" ", "+")

    page = requests.get('https://www.google.com/search?q=' + fill)

    try:
        soup = BeautifulSoup(page.text, 'html.parser')
        for link in soup.find_all(class_='g'):
            results.append(extractUrl(str(link)))

        return results
        #Uncoment for command line input
        #print(traverse(0))
    except:
        print("Done")
