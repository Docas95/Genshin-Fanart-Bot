import tweepy
from time import sleep
from genshinBotConfig import QUERY, SLEEP_TIME
from genshinBotENV import *

# start the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print('Twitter bot which retweets and likes Genshin Impact fanart')

for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    # if a tweet is a reply or made by the bot, ignore it
    if tweet.in_reply_to_status_id is not None or tweet.id == api.me().id:
        print('Tweet is a reply or was made by the bot\nSkipped')
        continue

    # check if the bot has already liked/retweeted the tweet
    status = api.get_status(tweet.id)
    favorited = status.favorited
    retweeted = status.retweeted
    # if the tweet has less than 20 likes or has alredy been liked/retweeted, ignore it
    if tweet.favorite_count > 20 and not retweeted and not favorited:
        try:
            print('\nTweet by: @ ' + tweet.user.screen_name)
            
            # retweet
            try:
                tweet.retweet()
                print('Retweeted the tweet')
            except:
                print('Error on fav')
            # like
            try:
                tweet.favorite()
                print('Retweeted the tweet')
            except:
                print('Error on retweet')

            print('Sleeping...')
            sleep(SLEEP_TIME)
            print('Woke up')

        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
