import pandas as pd

df = pd.read_csv ("nbaplayerstats2425.csv")

#These are the columns we are working with.
df = df[['Player','Team','PTS','FG%','3PA','3P%']]

#Remove missing data.
df = df.dropna()

#View players with at least 300 points
df_filtered = df[df['PTS'] >= 300]

#Reset index
df_filtered = df_filtered.reset_index(drop=True)

#Convert 3PA and PTS to integers.
df_filtered['3PA'] = df_filtered['3PA'].astype(int)
df_filtered['PTS'] = df_filtered['PTS'].astype(int)


#Top 10 Field Goal %
topfg = df_filtered.sort_values(by='FG%', ascending=False).head(10)
print("Top 10 FG% Scorers:")
print(topfg[['Player','Team','PTS','FG%','3PA','3P%']].to_string(index=False))

#Average FG% by Team
df_team = df_filtered[~df_filtered['Team'].isin(['2TM', '3TM'])]
teamfg = df_team.groupby('Team')['FG%'].mean().sort_values(ascending=False)
print("Average Team FG%:")
print(teamfg)

#Top 10 Most Efficient 3-Point Shooters
threept_filtered = df_filtered[df_filtered['3PA'] >= 150]
threept_filtered = threept_filtered.drop_duplicates(subset='Player', keep='first')
topthreept = threept_filtered.sort_values(by = '3P%', ascending=False).head(10)
print("Top 10 3PT Shooters (Min 150 Attempts):")
print(topthreept[['Player','Team','3PA','3P%', 'PTS']].to_string(index=False))

import matplotlib.pyplot as plt

#3PA vs Total Points Figure1
plt.figure(figsize=(10,6))
plt.scatter(df_filtered['3PA'], df_filtered['PTS'], alpha=0.6)
plt.title("3-Point Attempts vs Total Points (2024-2025 NBA Season)")
plt.xlabel("3-Point Attempts")
plt.ylabel("Total Points")
plt.grid(True)

#FG Distribution Figure2
#Convert FG to numeric and drop rows.
df_filtered['FG%'] = pd.to_numeric(df_filtered['FG%'], errors = 'coerce')
df_filtered = df_filtered.dropna(subset=['FG%'])

plt.figure(figsize=(10,6))
plt.hist(df_filtered['FG%'], bins=15, color='red', edgecolor = 'black')
plt.title("Distribution of Field Goal % (2024-2025 NBA Season)")
plt.xlabel("FG%")
plt.ylabel("Number of Players")

#Average Team FG% Figure3
plt.figure(figsize=(12,6))
teamfg.plot(kind = 'bar', color = 'skyblue', edgecolor = 'black')
plt.title("Average Team FG% (2024-2025 NBA Season)")
plt.ylabel("Average FG%")
plt.xlabel("Team")
plt.xticks(rotation = 45)
plt.show()

