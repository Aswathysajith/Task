# import pandas as pd
# import  datetime as dt
# df=pd.read_csv('NIFTY_BANK.csv')
# # print(df.head(5))
# start_date=dt.datetime(2022,1,3,9,30)
# end_date=dt.datetime(2022,1,31,3,00)
#
# # resDate=pd.date_range(start_date,end_date,freq=dt.timedelta(days=1,minutes=1)).tolist()
# for ts in pd.date_range(start_date,end_date,freq=dt.timedelta(days=0,minutes=1)):
#     print(ts)


# Import reader module from csv Library
from csv import reader

# read the CSV file
def load_csv(filename):
    # Open file in read mode
    file = open(filename, "r")
    # Reading file
    lines = reader(file)
    # Converting into a list
    data = list(lines)
    return data
if __name__ == "__main__":
    # Path of the dataset
    file_path = "NIFTY_BANK.csv"
    data = load_csv(file_path)
 # Let's print the first 5 datapoints
    for row in data[:6]:
        print(row, end="\n")

import datetime
from datetimerange import DateTimeRange

time_range = DateTimeRange("2022-01-03 09:30:0+3:00", "2023-02-24T09:30:3+0300")
for value in time_range.range(datetime.timedelta(days=1,minutes=1 )):

    print(value)




