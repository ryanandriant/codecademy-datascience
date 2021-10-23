# 1 
# Import necessary libraries
import pandas as pd
from matplotlib import pyplot as plt

# load rankings data
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')

# load rankings data
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# 2
# Create a function to plot rankings over time for 1 roller coaster
def ranking_plot(name, park_name, df):
  df_filter = df[(df.Name == name) & (df.Park == park_name)]
  ranks = df_filter['Rank']
  year = df_filter['Year of Rank']
  plt.plot(year, ranks)
  ax = plt.subplot()
  ax.invert_yaxis()
  plt.xlabel('Year')
  plt.ylabel('Rank')
  plt.title('Rank of {name} - {pn} per year'.format(name=name, pn=park_name))
  plt.show()
  plt.clf()

# 3
# Create a plot of El Toro ranking over time
ranking_plot('El Toro', 'Six Flags Great Adventure', wood)

# Create a plot of El Toro and Boulder dash hurricanes
def two_ranking_plot(name1, park_name1, name2, park_name2, df):
  df_filter1 = df[(df.Name == name1) & (df.Park == park_name1)]
  ranks1 = df_filter1['Rank']
  year1 = df_filter1['Year of Rank']
  df_filter2 = df[(df.Name == name2) & (df.Park == park_name2)]
  ranks2 = df_filter2['Rank']
  year2 = df_filter2['Year of Rank']
    
  plt.plot(year1, ranks1, label=name1)
  plt.plot(year2, ranks2, label=name2)
  ax = plt.subplot()
  ax.invert_yaxis()
  plt.legend()
  plt.xlabel('Year')
  plt.ylabel('Rank')
  plt.title('Rank of {name1}-{pn1} vs {name2}-{pn2}'.format(name1=name1, pn1=park_name1, name2=name2, pn2=park_name2))
  plt.show()
  plt.clf()

two_ranking_plot('El Toro','Six Flags Great Adventure','Boulder Dash','Lake Compounce', wood)

# 4
# Create a function to plot top n rankings over time
def top_n_ranking(n, df):
  top_n_rankings = df[df.Rank <= n]
  for coaster in set(top_n_rankings['Name']):
    coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
    plt.plot(coaster_rankings['Year of Rank'],coaster_rankings['Rank'],label=coaster)
  plt.legend()
  ax = plt.subplot()
  ax.invert_yaxis()
  plt.show()

# Create a plot of top n rankings over time
top_n_ranking(5, wood)

# 5
# load roller coaster data
data = pd.read_csv('roller_coasters.csv')

# 6
# Create a function to plot histogram of column values
def numeric_hist(df, column):
    plt.hist(df[column].dropna())
    plt.xlabel(column.title())
    plt.ylabel('Count')
    plt.title('Roller Coaster\'s {}'.format(column.title()))
    plt.show()
    plt.clf()


# Create histogram of roller coaster speed
numeric_hist(data, 'speed')
# Create histogram of roller coaster length
numeric_hist(data, 'length')
# Create histogram of roller coaster number of inversions
numeric_hist(data, 'num_inversions')

# Create a function to plot histogram of height values
def height_hist(df):
    heights = df[df['height'] <= 140]
    plt.hist(heights.height)
    plt.xlabel('Height')
    plt.ylabel('Count')
    plt.title('Roller Coaster\'s Height')
    plt.show()
    plt.clf()
# Create a histogram of roller coaster height
height_hist(data)

# 7
# Create a function to plot inversions by coaster at park
def plot_inversions(df, park):
  df_filtered = df[df.park == park]
  print(df_filtered)
  x = df_filtered['name']
  y = df_filtered['num_inversions'] 
  plt.bar(range(len(x)), y)
  plt.xlabel("Roller Coaster")
  plt.ylabel('Number of Inversions')
  plt.title('Number of Inversions in {} Park'.format(park))
  ax = plt.subplot()
  ax.set_xticks(range(len(x)))
  ax.set_xticklabels(x, rotation = 30)
  plt.show()
  plt.clf()

# Create barplot of inversions by roller coasters
plot_inversions(data, 'Parc Asterix')

# 8
# Create a function to plot a pie chart of status.operating
def pie_chart(df):
  operating_coasters = df[df['status'] == 'status.operating']
  closed_coasters = df[df['status'] == 'status.closed.definitely']
  operating_count = len(operating_coasters)
  closed_count = len(closed_coasters)
  status_counts = [operating_count, closed_count]
  plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating','Closed'])
  plt.show()
  plt.clf()

# Create pie chart of roller coasters
pie_chart(data)

# 9
# Create a function to plot scatter of any two columns
def scatter(col1, col2, df):
  if col1 != 'height' and col2 != 'height':
    column1data = df[col1]
    column2data = df[col2]
    plt.scatter(column1data, column2data)
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title('{x} vs {y}'.format(x=col1, y=col2))
    plt.show()
    plt.clf()
  else:
    heights = df[df['height'] <= 140]
    column1data = heights[col1]
    column2data = heights[col2]
    plt.scatter(column1data, column2data)
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title('{x} vs {y}'.format(x=col1, y=col2))
    plt.show()
    plt.clf()
    
# Create a function to plot scatter of speed vs height
scatter('speed', 'height', data)

# Create a scatter plot of roller coaster height by speed
scatter('height', 'speed', data)