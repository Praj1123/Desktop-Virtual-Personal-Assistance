import wikipedia
def searchWekepedia(query):
    if 'wikipedia' in query:
        query = query.replace('wikipedia','').replace('on','').replace('search','').replace('luna','')
        #speak('This is what , I found on wikipedia')
        result = wikipedia.summary(query,sentences=2)
        #speak('According to wikipedia')
        print(result)
        #speak(result)
searchWekepedia('computer')