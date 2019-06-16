import tweepy
import time
import random 
import requests
import json


#login for twitter API and its credencials 
consumer_key = ''
consumer_secret = ''
access_key = ''
access_secret = '' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth) 


#oxford dict credentials
app_id = ""
app_key = ""
language = "en-gb"


#creates list of words from text file with 370,103 words
my_file = open('words_alpha.txt', 'r')
word_list = my_file.read().split()


while len(word_list) > 0:
    
    #picks a random number from the list 
    number = random.randint(0, len(word_list));
    
    #accounts if word not in the oxford dict
    try:
        word_id = word_list[number]
        field = "definitions"
        url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower() + '?fields=' + field
        request = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
    
        definition = request.json()["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"][0]
        grammar = request.json()['results'][0]['lexicalEntries'][0]['lexicalCategory']['text']        
        status = word_id.capitalize() + " (" + grammar + ") " + "\n" + definition
        
        api.update_status(status)
        print("Posted")
        
        #delets word from list after it is used, stops repeat words
        del word_list[number]
        
        
        
    except KeyError:
        #delets word from list after it is used/does not work
        del word_list[number]
        continue;
    
    time.sleep(43200)
    

