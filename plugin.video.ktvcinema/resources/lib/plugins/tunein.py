import requests
from bs4 import BeautifulSoup as BS
import json



class TuneIn():
    domain = ['tunein.com']

    def __init__(self):
        self.streams=[]
    

    def getStream(self, stationId):
        '''Get stream URL '''
        if stationId.startswith('s'): stationId = stationId[1:]
        u= "https://tunein.com/tuner/tune/?tuneType=Station&preventNextTune=true&waitForAds=false&audioPrerollEnabled=false&partnerId=&stationId=%s"%stationId
        streamInfo = requests.get(u).json()
        streamUrl='http:'+streamInfo['StreamUrl']
        streamData = requests.get(streamUrl).json() # there is usually a lot more data here 
        
        
        mpStream=streamData['Streams'][0]['Url'] # we get the first URL 

        return mpStream

    def getCategory(self, category):
        ''' Returns Category info'''

        u="https://api.tunein.com/categories/%s?formats=mp3,aac,ogg,flash,html"%category
        categoryData = requests.get(u).json()

        allCategories = categoryData and categoryData['Items'] and categoryData['Items'][0] and categoryData['Items'][0]['Children']
        y = [{'Title':i['Title'], 'GuideId': i['GuideId'] } for i in allCategories if 'GuideId' in i]

        return y

    def getCatStations(self, category):
        '''Get Stations from a sub Category'''

        baseUrl = 'https://api.tunein.com/categories/%s?filter=s:free&limit=%d&formats=mp3,aac,ogg,flash,html'
        firstUrl = baseUrl %(category, 1)
        firstData = requests.get(firstUrl).json()
        print "Determining Total Station Count"
        totalCount = firstData and firstData['Paging'] and firstData['Paging']['TotalItemCount'] or None

        if totalCount is None:
            print "No Streams Found"
            return []

        print "Trying to get %d Stations"%totalCount
        allStationUrl = baseUrl % (category, totalCount)
        allStationsData = requests.get(allStationUrl)
        test = allStationsData.text
        allStationsData = allStationsData.json()
        allStationsData = allStationsData if 'Items' in allStationsData else {}

        AllStationsList = [ {'Title': i['Title'], 'GuideId': i['GuideId'] } for i in allStationsData['Items'] if 'GuideId' in i]
        return AllStationsList

    def getStationStreams(self, Stations):
        '''Get Stream URLs for all Stations'''

        streamLinks=[]
        for station in Stations:
            print "Getting stream for :",station['Title']
            stream = self.getStream(station['GuideId'])
            streamLinks.append({'stream':stream, 'title':station['Title']})

        return streamLinks

    def grabStreamsForCategory(self, category):
        '''Main Method to populate the links list'''

        x= self.getCategory(category)
        for each in x:
            print "Getting Stations for Category:",each['Title']
            stations=self.getCatStations(each['GuideId'])
            streams = self.getStationStreams(stations)
            # categorizedStreams = [  for i in streams]


            for s in streams:
                s.update({'category': category})
                # print s
                self.streams.append(s)
        
        print "finished"

    

test =TuneIn().grabStreamsForCategory('sports')

