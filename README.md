# ECE2524_Project3
This repository is for ECE 2524 Project 3 and Homework Assignment.

Ideas for Project3:

# Twitter
- Data Scrapper for Twitter
- Mastermind
  - Ask any question on Twitter using a specific hashtag (Ex: "#ECE2524 What is the color of the sky")
    - Question will be captured and the payload will be sent to wolfram
  - Question will be answered and the answer will be sent to a text file
  
Edit Date: 5/1/2020

- New project idea I will pursue
  - Enter any twitter user, mine/collect all of their tweets [TWITTER API]
  - Parse through tweets, and detect if there if any of their tweets contain profanity
    - This idea seemed interesting to me since I have my twitter currently set to Private, but if I have a lot of tweets so it would take me a while to look through all my tweets since 2011. If there is a bad tweet sometime a long the way, I can see what it is and it's time stamp so I can delete it
  - The tweets that have been flagged will then be outputted to a textfile
  
Edit date: 5/6/2020

- Twitter has a lot of influence on what happens in today's society, from celebrities to politics. A problem that arises from this is    bots, what I want to achieve in this project is be able to detect if a specific twitter account is a bot or not. 
  - Enter a specific twitter account to review
  - Will get the following information regarding the account: name, followers/friends count, number of statuses, account age, average tweets per day, most mentioned twitter users, and most used hashtags.
    - The data will be printed out to an output text file
  - Data will be analyzed and outputed out to the terminal
  - Following blog written by Mozilla (https://blog.mozilla.org/internetcitizen/2018/01/08/irl-how-to-spot-a-bot/), I will see how to detect a bot.
    - Bots post, a bot account tweets up to around 2,000 times a day
    - If an account has around 2,000 average tweets per day, then we can assume that the account is a bot. A print statement will be sent to the command line stating that the bot has been detected as a bot.
 
 # HOW TO RUN
 
 Libraries used: tweepy, time, sys, datetime, collections, keys
 
 Make sure to have the keys.py, as it contains the keys to access the Twitter API.
  
 run -> sudo pip3 install tweepy
 
 run command -> python3 project3.py [@TWIITERUSER] 
 
 replace [@TWIITERUSER] with any user, for this example we will run the following command.
 
 run command -> python3 project3.py tsheetiz
 
 What to expect:
  - If it is a bot, then a text message in the command line
  - If it is not a bot, then a text message in the command line
  - A text file named "twitter_data.txt" containing data from twitter account
 
 # Conclusion
 
 As you can see I used my Twitter account as an example, and the output that you would get in the terminal is that "The account has not been flagged as a bot". If you were to suspect an account of being bot, you can input their username and wait for it to analyze. It will take a lot longer if an account is detected as a bot, as it will analyze all of their hashtags and mentions in the past 30 days. Then if they are suspected of a bot, then you will get the following error "This account has been flagged as a bot account! Requires further review!". 
 
 Thank you for a great semester! This was a fun project to work on.
