import pandas as pd

#Open file of interest
csv_file = pd.read_csv('avgsentiment/msft.csv')
#Select columns of interest by their column name
tiker, date, score = csv_file.Tiker, csv_file.Date, csv_file.Score

t_list, d_list, s_list = [], [], []

for t in tiker:
    t_list.append(t)

for d in date:
    d_list.append(d)

for s in score:
    s_list.append(s)

print(len(s_list))
#
# new_data = {'Tiker': t_list,
#             'Date': d_list,
#             'Score': s_list}
#
# df = pd.DataFrame(new_data, columns = ['Tiker', 'Date', 'Score'])
# df.to_csv('avgsentiment/new_data.csv')
# print("New file has been saved")