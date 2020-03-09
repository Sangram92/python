# read csv using panda
# date parsing, two date columns difference and validation


import pandas as pd
import numpy as np

parse_dates = ['CLAIMCREATIONDATE', 'CLAIMCLOSEDATE']
file_path = "C:/Users/sangrpatil/Desktop/Minion Training/PaymentUnder6.csv"
data = pd.read_csv(file_path, parse_dates=parse_dates)

correct_entries = 0
for idx, val in data['CLAIMCLOSEDATE'].items():
	if val and data['CLAIMCREATIONDATE'][idx]:
		diff = val - data['CLAIMCREATIONDATE'][idx]
		diff_in_minutes = diff / np.timedelta64(1, 'm')
		if diff_in_minutes < 6:
			correct_entries += 1
			print(idx, "==>", diff_in_minutes)

print("Correct Entries Found ===> ", correct_entries)