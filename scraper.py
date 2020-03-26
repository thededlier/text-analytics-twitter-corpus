import datetime
from datetime import timedelta
from twitterscraper import query_tweets

query_limit = 10
start_date = datetime.date(2019, 12, 26)
end_date = datetime.date(2020, 2, 23)

def generate_query(hashtag=None, date=None, location=None):
    """
    Generates a query
    Example query: "(#dublin) lang:en until:2019-12-26 since:2019-12-26 -filter:links -filter:replies -place:Dublin"
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

    date = start_date
    while (date <= end_date):
        query = generate_query(hashtag="#Dublin", location="Dublin")

        list_of_tweets = query_tweets(
            query,
            begindate=date,
            enddate=date + timedelta(days=1),
            limit=query_limit,
            lang="en"
        )

        for tweet in list_of_tweets:
            print(tweet.text)
