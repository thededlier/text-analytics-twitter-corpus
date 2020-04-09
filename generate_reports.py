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

    hashtag = file.replace(".csv", "")

    fig, ax = plt.subplots(figsize=(8,6))
    ax.plot(error_counts_by_date_df["date"], error_counts_by_date_df['error_rate'])

    plt.xticks(rotation='vertical')
    ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_minor_locator(mdates.DayLocator())

    ax.set_xlabel('Date')
    ax.set_ylabel('Error Rate')
    ax.set_title('Total Error Counts over time for #{}'.format(hashtag))

    fig.savefig("./reports/{}.png".format(hashtag))

    correlation = abs(error_counts_by_date_df.corr()['error_rate']['lunar_phase'])
    corr_dict['hashtag'].append(hashtag)
    corr_dict['correlation'].append(correlation)

corr_df = pd.DataFrame.from_dict(corr_dict)
corr_df.to_csv('./reports/correlation.csv', index=False)
