import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

lunar_phase_dict = {
    0: '1st Quarter',
    1: 'New Moon',
    2: '3rd Quarter',
    3: 'Full Moon'
}

corr_dict = {
    'hashtag': [],
    'corr_1st_quarter': [],
    'corr_3rd_quarter': [],
    'corr_new_moon': [],
    'corr_full_moon': []
}

def make_lunar_categorical(row):
    row['lunar_phase'] = lunar_phase_dict[row['lunar_phase']]
    return row

for file in os.listdir("./processed_errors"):
    error_counts_by_date_df = pd.read_csv("./processed_errors/" + file);
    error_counts_by_date_df['total_error_count'] = error_counts_by_date_df['total_error_count'].astype('int')
    error_counts_by_date_df['total_tweets'] = error_counts_by_date_df['total_tweets'].astype('int')
    error_counts_by_date_df['error_rate'] = error_counts_by_date_df['error_rate'].astype('float64')
    error_counts_by_date_df['lunar_phase'] = error_counts_by_date_df['lunar_phase'].astype('int')
    error_counts_by_date_df['date'] = error_counts_by_date_df['date'].astype('datetime64')


    error_counts_by_date_df = error_counts_by_date_df.apply (lambda row: make_lunar_categorical(row), axis=1)

    error_counts_by_date_df = pd.get_dummies(error_counts_by_date_df, columns=['lunar_phase'])

    hashtag = file.replace(".csv", "")


    correlation = error_counts_by_date_df.corr()['error_rate']
    corr_dict['hashtag'].append(hashtag)
    corr_dict['corr_1st_quarter'].append(abs(correlation['lunar_phase_1st Quarter']))
    corr_dict['corr_3rd_quarter'].append(abs(correlation['lunar_phase_3rd Quarter']))
    corr_dict['corr_new_moon'].append(abs(correlation['lunar_phase_Full Moon']))
    corr_dict['corr_full_moon'].append(abs(correlation['lunar_phase_New Moon']))

corr_df = pd.DataFrame.from_dict(corr_dict)
corr_df.to_csv('./reports/correlation_moon_phase.csv', index=False)
