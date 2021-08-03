# Twitter_Sentimental_Analysis
### Description ###
* This repository contains three branches.
* First one is I have performed Twitter Sentiment Analysis in our local sytem.
  * Package Used:-
    * nltk
    * Textblob
* The second one is I have performed Twitter Sentiment Analysis using pyspark.
  * First I have created a streaming connection.
  * Then called the functionalities using pyspark.
* The third one is using Azure Event Hub Streaming.
  * First I have created an Azure Event Hubs account and created a new job inside that.
  * Then, I have created a new cluster in the databricks and installed several packages and those are:-
    * tweepy
    * azure-eventhub
    * azure-eventhub-checkpointstoreblob-aio
    * textblob
    * nltk
  * Then I have implemented it my adding the event hub connection string and the credentials from the twitter development account.
