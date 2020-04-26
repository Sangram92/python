
import pandas as pd
import numpy as np


data_file = "data.csv"
id_name_file = "queryfinal.csv"
data = pd.read_csv(data_file)
id_names = pd.read_csv(id_name_file)

id_name_dict = { id_names['ADJUSTERUSERID'][i] :  id_names['ADJUSTERNAME'][i] \
	for i in range(len(list(id_names['ADJUSTERUSERID'])))}

adj_names = []
for id_ in data['ADJUSTERUSERID']:
	adj_names.append(id_name_dict.get(id_, "NOT FOUND"))

data['ADJUSTERNAME'] = adj_names

data.to_csv('output.csv', index=False)