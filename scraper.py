import datetime
from twitterscraper import query_tweets

limit = 10

def generate_query(hashtag=None, date=None, location=None):
    """
    Generates a query
    Example query: "(#feminism) lang:en until:2019-12-26 since:2019-12-26 -filter:links -filter:replies -place_country:IE"
    """
    query = ""

    if hashtag:
        query += "({}) ".format(hashtag)
    if date:
        query += "since:{} until:{} ".format(date, date)
    if location:
        query += "-place:{} ".format(location)

    query += "-filter:replies -filter:links"

    return query

if __name__ == '__main__':
    query = generate_query(hashtag="#Dublin", location="Dublin")

    list_of_tweets = query_tweets(
        query,
        begindate=datetime.date(2019, 12, 26),
        enddate=datetime.date(2019, 12, 27),
        limit=limit,
    )

    for tweet in list_of_tweets:
        print(tweet)
