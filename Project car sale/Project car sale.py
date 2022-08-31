import pandas as pd



df = pd.read_csv('Car_Purchasing_Data.csv', index_col=[0,1])

print(df)



df.head(500)



import matplotlib.pyplot as plt

plt.plot([18, 36, 54, 72, 90], [10000, 50000, 100000, 500000, 1000000], 'ro')

plt.ylabel('Annual Salary')

plt.xlabel('Age')

df.sort_values('Car Purchase Amount')

plt.show()
