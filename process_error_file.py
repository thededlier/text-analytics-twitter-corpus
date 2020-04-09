import pandas as pd
import numpy as np

# Change these as needed
hashtag = "beautiful"
base_path = "C:/Users/rohan/Documents/Text-Analytics-Lunar/results/from_la/"
file_name = "./error_files/error_results_beautiful.csv"

lunar_phase_dict = {
    0: '1st Quarter',
    1: 'New Moon',
    2: '3rd Quarter',
    3: 'Full Moon'
}

# For dublin, may need to change for other locations

lunar_phase_date_dict = {
    '2019-12-26': 1, '2019-12-27': 1, '2019-12-28': 1, '2019-12-29': 1,
    '2019-12-30': 1, '2019-12-31': 1, '2020-01-01': 1, '2020-01-02': 1,
    '2020-01-03': 0, '2020-01-04': 0, '2020-01-05': 0, '2020-01-06': 0,
    '2020-01-07': 0, '2020-01-08': 0, '2020-01-09': 0, '2020-01-10': 3,
    '2020-01-11': 3, '2020-01-12': 3, '2020-01-13': 3, '2020-01-14': 3,
    '2020-01-15': 3, '2020-01-16': 3, '2020-01-17': 2, '2020-01-18': 2,
    '2020-01-19': 2, '2020-01-20': 2, '2020-01-21': 2, '2020-01-22': 2,
    '2020-01-23': 2, '2020-01-24': 1, '2020-01-25': 1, '2020-01-26': 1,
    '2020-01-27': 1, '2020-01-28': 1, '2020-01-29': 1, '2020-01-30': 1,
    '2020-01-31': 1, '2020-02-01': 1, '2020-02-02': 0, '2020-02-03': 0,
    '2020-02-04': 0, '2020-02-05': 0, '2020-02-06': 0, '2020-02-07': 0,
    '2020-02-08': 0, '2020-02-09': 3, '2020-02-10': 3, '2020-02-11': 3,
    '2020-02-12': 3, '2020-02-13': 3, '2020-02-14': 3, '2020-02-15': 2,
    '2020-02-16': 2, '2020-02-17': 2, '2020-02-18': 2, '2020-02-19': 2,
    '2020-02-20': 2, '2020-02-21': 2, '2020-02-22': 2, '2020-02-23': 1
}

error_results = pd.read_csv(file_name)

def parse_meta_data_from_filename(row):
    row['hashtag'] = row['filename'].replace(base_path, '').split('\\')[0]
    row['date'] = row['filename'].replace(base_path, '').split('\\')[1]
    row['file'] = row['filename'].split(row['date'] + '\\')[1].split('.')[0]
    row['lunar_phase'] = lunar_phase_date_dict[row['date']]
    return row


error_results = error_results.apply (lambda row: parse_meta_data_from_filename(row), axis=1)

error_counts_by_date_df = pd.DataFrame(columns=['date', 'hashtag', 'total_error_count', 'lunar_phase'])

for (key, value) in lunar_phase_date_dict.items():
    total_tweets = np.size(error_results.loc[error_results['date'] == key]['error_count'])
    total_error_count = np.sum(error_results.loc[error_results['date'] == key]['error_count'])
    row = {
        'date': key,
        'lunar_phase': value,
        'hashtag': hashtag,
        'total_error_count': total_tweets,
        'total_tweets': total_error_count,
        'error_rate': total_error_count / total_tweets
    }

    error_counts_by_date_df = error_counts_by_date_df.append(row, ignore_index=True)

error_counts_by_date_df['total_error_count'] = error_counts_by_date_df['total_error_count'].astype('int')
error_counts_by_date_df['total_tweets'] = error_counts_by_date_df['total_tweets'].astype('int')
error_counts_by_date_df['error_rate'] = error_counts_by_date_df['error_rate'].astype('float64')
error_counts_by_date_df['lunar_phase'] = error_counts_by_date_df['lunar_phase'].astype('int')
error_counts_by_date_df['date'] = error_counts_by_date_df['date'].astype('datetime64')

error_counts_by_date_df.to_csv("./processed_errors/{}.csv".format(hashtag), index=False)
