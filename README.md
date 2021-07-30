# Genshin-Fanart-Bot

## Tired of looking for good fanart/fanartist in your own? This bot is here to help!

Sometimes it's pretty annoying to have to manually look through social media for good fanart of my favorite shows/videogames. To solve that issue I decided to make a twitter bot that searches for fanart for me. Genshin-Fanart-Bot only searches for Genshin Impact fanart, but the source code can be easily changed if I ever want it to look for something else.

## How does it work?

Genshin-Fanart-Bot searches on twitter for tweets with #genshinfanart, it then can like an retweet those tweets.

The bot likes/retweets one tweet every hour.

Only 'normal' tweets will be noticed by the bot, replies will be ignored.

The bot only notices tweets with at least 20 likes. This is because, generally speaking, art with very few likes might not have the best quality. This condition works as 'quality control'.

Too see the fanart the bot retweeted simply go to https://twitter.com/FanartGenshin

## How was it made?

This bot was made with python, using the tweepy library.
