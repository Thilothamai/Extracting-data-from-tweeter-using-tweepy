import LWePY
auth tweepy.oAuthHandler ("mF4tbF'3bj fLIC4SVnbhpZ6eRb" , "HfZaiwEUfeOGdKPFP678 COMAKYQWV6ZhIjGTdAHDywaf 3UWYB7")
auth.set_access_token ("1460637391828385794-N2mHqluRui lpwak2awEd7 z7j Ugjmod", "9fiKEzUyKYEA 5a02IHEKcfsa2UEA8 cSGZ 7 dARmKIWjmRJ")
api = tweepy.API (auth)
public_tweets = api.home_timeline ()
for tweet in pubiic_tweets:
        print (tweet.text) 
