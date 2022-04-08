from scraper import SeleniumClient

bot = SeleniumClient()

bot.twitterLogin()

bot.scrapeTweets()

bot.getTweetData()
