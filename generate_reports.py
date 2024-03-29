import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

corr_dict = {
    'hashtag': [],
    'correlation': []
}

for file in os.listdir("./processed_errors"):
    error_counts_by_date_df = pd.read_csv("./processed_errors/" + file);
    error_counts_by_date_df['total_error_count'] = error_counts_by_date_df['total_error_count'].astype('int')
    error_counts_by_date_df['total_tweets'] = error_counts_by_date_df['total_tweets'].astype('int')
    error_counts_by_date_df['error_rate'] = error_counts_by_date_df['error_rate'].astype('float64')
    error_counts_by_date_df['lunar_phase'] = error_counts_by_date_df['lunar_phase'].astype('int')
    error_counts_by_date_df['date'] = error_counts_by_date_df['date'].astype('datetime64')

    hashtag = file.replace(".csv", "")

    fig, ax = plt.subplots(figsize=(10,8))
    ax.plot(error_counts_by_date_df["date"], error_counts_by_date_df['error_rate'])

    plt.xticks(rotation=45)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
    ax.xaxis.set_minor_locator(mdates.DayLocator())

    ax.set_xlabel('Date (YY-MM-DD)')
    ax.set_ylabel('Error Rate')
    ax.set_title('Total Error Counts over time for #{}'.format(hashtag))

    fig.savefig("./reports/{}.png".format(hashtag))

    correlation = abs(error_counts_by_date_df.corr()['error_rate']['lunar_phase'])
    corr_dict['hashtag'].append(hashtag)
    corr_dict['correlation'].append(correlation)

corr_df = pd.DataFrame.from_dict(corr_dict)
corr_df.to_csv('./reports/correlation.csv', index=False)
