from InternetSpeedTwitterBot import InternetSpeedTwitterBot as bot

def main():
    twitter_bot = bot()
    twitter_bot.get_internet_speed()
    twitter_bot.tweet_at_provider()

if __name__ == '__main__':
    main()