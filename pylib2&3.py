#Python Libary #2 & 3: Pandas & MatPlotLib


import pandas as pd
import matplotlib.pyplot as plt


#A simple program that displays the Lifeline of the Tesla Motors stock using data from a spreadsheet using the MatPlotLib libary to display it on a graph, and the Pandas libary to fetch the data and organize it. 

df = pd.read_csv("tesla_stock_1y_data.csv")

start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2021-03-30')

df['Date'] = pd.to_datetime(df['Date']) 
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1.set_index('Date')
plt.figure(figsize=(5,5))
plt.suptitle('Stock prices of Tesla Motors.,\n01-04-2020 to 30-03-2021', \
                 fontsize=18, color='black')
plt.xlabel("Date",fontsize=16, color='black')
plt.ylabel("$ price", fontsize=16, color='black')
 
df2.plot(color='green');
plt.show()
