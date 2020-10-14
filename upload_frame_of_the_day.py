
# tweepy-bots/bots/config.py
import tweepy
import logging
import os
import math

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    print ("consumer key "+consumer_key)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

twitter_api = create_api()

starting_frame = 1294

index = os.listdir('/root/index/')[0]
next_frame = int(index)+1-starting_frame
# upload next frame
image_folder = "{0:04d}".format(math.floor(next_frame/10000))
image_path = "/root/files/"+image_folder+"/"+"{0:08d}.jpg".format(next_frame)
tweet_text = "Frame number # "+str(next_frame)

status = twitter_api.update_with_media(image_path, tweet_text)


#try:
#  twitter_api.update_status(status=tweet_text)
#except Exception as e:
#  logger.error("Error updating", exc_info=True)
#  raise e
#logger.info("Twitted")



#remove previous index
os.remove('/root/index/'+index)
#add next index
os.mknod("/root/index/{0:08d}".format(next_frame))
