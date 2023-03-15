import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
df = pd.read_csv('scientist.csv')


print(df)
plt.switch_backend('TkAgg')
df.hist(column='0 Man')
plt.show()
df.hist(column='1 Man')
plt.show()
df.hist(column='2 Man')
plt.show()
df.hist(column='0 Woman')
plt.show()
df.hist(column='1 Woman')
plt.show()
df.hist(column='2 Woman')
plt.show()

print('first face')
for i in [80, 85, 90, 95, 97.5, 98, 99]:
    print('Man', i, df.loc[df['0 Man'] > i].shape[0])
    print('Woman', i, df.loc[df['0 Woman'] > i].shape[0])

print('second face')
for i in [0, 80, 85, 90, 95, 97.5, 98, 99]:
    print('Man', i, df.loc[df['1 Man'] > i].shape[0])
    print('Woman', i, df.loc[df['1 Woman'] > i].shape[0])


print('third face')
for i in [0, 80, 85, 90, 95, 97.5, 98, 99]:
    print('Man', i, df.loc[df['2 Man'] > i].shape[0])
    print('Woman', i, df.loc[df['2 Woman'] > i].shape[0])

