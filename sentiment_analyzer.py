# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 22:47:10 2020

Check out the Ends With Benefits podcast to learn about investing 
and techniques to disrupt the wealth inequality gap

This program uses the StockTwits api to fetch tweets from investors
and measure whether the users have a positive or negative sentiment
about a particular company

@author: Marshall Felder
"""

from statistics import mean
import requests
from textblob import TextBlob

def main():
    
    #Hit the stocktwits api. Switch the ticker for the stock you want to analyze
    r = requests.get('https://api.stocktwits.com/api/2/streams/symbol/MSFT.json')
    
    tweets = r.json()
    
    microsoft_sentiments = []
    
    #collect all of the tweets into a list
    for i in range(len(tweets['messages'])):
        n = tweets['messages'][i]['body']
        microsoft_sentiments.append(n)
     
    #Gather the sentiment for each tweet and store it in a list
    microsoft_sentiments2 = [TextBlob(i).sentiment.polarity for i in microsoft_sentiments]
      
    #Get the average of all of the tweets sentiment scores
    average_sentiment_score = round(mean(microsoft_sentiments2),2)
     
    
    if average_sentiment_score > .5:
        print(f"The Microsoft tweets on Stocktwits has an average sentiment score of {average_sentiment_score}. The overall market is feeling positive about Microsoft")
    elif average_sentiment_score < .5:
        print(f"The Microsoft tweets on Stocktwits has an average sentiment score of {average_sentiment_score}. The overall market is feeling pretty crunchy about Microsoft")
    
if __name__ == '__main__':
    main()
