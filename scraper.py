import datetime
import os
from datetime import timedelta
from pathlib import Path

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
    hashtag = "#Dublin"
    location = "Dublin"

    # Make results directory
    execution_path = Path(__file__).parent.absolute()
    result_path = execution_path / "results"
    result_path.mkdir(exist_ok=True)
    hashtag_result_path = result_path / hashtag.replace("#", '')
    hashtag_result_path.mkdir(exist_ok=False)

    print("Outputting to " + str(result_path))

    date = start_date
    while (date <= end_date):
        query = generate_query(hashtag=hashtag, location=location)

        list_of_tweets = query_tweets(
            query,
            begindate=date,
            enddate=date + timedelta(days=1),
            limit=query_limit,
            lang="en"
        )

        t_iterator = 0
        date_path = hashtag_result_path / date.strftime("%Y-%m-%d")
        date_path.mkdir(exist_ok=False)

        for tweet in list_of_tweets:
            file_path =  date_path / "{}.txt".format(t_iterator)

            file = open(file_path, "w")
            file.write(tweet.text)
            file.close()

            t_iterator += 1

        date = date + timedelta(days=1)

    print("Execution complete!")
