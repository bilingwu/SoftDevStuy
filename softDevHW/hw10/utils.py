import urllib2
import json
from bs4 import BeautifulSoup
import time


def wrapper(f):
    def inner(*arg):
        return f.func_name + ":" + str(arg)+ f(*arg)
    return inner

def timer(f):
    def inner(*arg):
        begin = time.time()
        f(*arg)
        end = time.time()
        return f(*arg) + "Execution time: " + str(end - begin)
    return inner

#Gets first paragraph from Wikipedia about the location
@timer
@wrapper
def getWiki(location):
    '''
    This will return the title of an article that mostly closely matches your query.
    location is the place you wish to find information about
    action=query allows you to get information and data
    list=search is a submodule used for searching through titles and text. Data is returned in a list.
    srsearch={} specifies what you are searching for
    format=json will return the data in json format
    '''
    url1 = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&format=json".format(location)
    result1 = json.loads(urllib2.urlopen(url1).read())
    place = ""
    for i in result1['query']['search']:
        if i['wordcount'] > 1000:
            place = i['title'].replace(" ", "%20")
            break
    if len(result1['query']['search']) == 0:
        return None
    '''
    This will return the text in an article.
    action=query allows you to get information and data
    titles={} will look for the wikipedia article with the specified title
    prop=extracts will return plain-text or limited HTML extracts of the page
    format=json will return the data in json format
    '''
    url2 = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&format=json".format(place)
    result2 = json.loads(urllib2.urlopen(url2).read())
    key = result2['query']['pages'].keys()[0]
    info = result2[u'query']['pages'][key]['extract']
    soup = BeautifulSoup(info, 'html.parser')
    paragraphs = []
    for p in soup.find_all('p'):
        paragraphs.append(p.get_text().encode("utf-8"))
        '''
        Sometimes there is no first paragraph and therefore we must go to the second one
        '''
    if(paragraphs[0] == ""):
        return paragraphs[1]
    else:
        return paragraphs[0]
    
def coordinates(query):
    '''
    Gets the longitude and latitude for a location using bing maps
    query is the location you wish to search for
    maxResults sets how many results you wish to get
    key is necessary to use the api
    '''
    key = "Aj1X2oDWw6lKh5Y5Roy_uyou-ySwIiBhRzBVQMKMG9KVYoWXtw7XczdppkOnXe3L"
    url = "http://dev.virtualearth.net/REST/v1/Locations?query=%s&maxResults=1&key=%s"
    url = url%(query,key)
    result = json.loads(urllib2.urlopen(url).read())
    if result['resourceSets'][0]['estimatedTotal'] == 0:
        return None
    coord =  result['resourceSets'][0]['resources'][0]['point']['coordinates']
    coord = {'lat':coord[0], 'lng':coord[1]}
    return coord
    

