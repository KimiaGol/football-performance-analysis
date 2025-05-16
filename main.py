import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("data/players.csv")

# Show first 5 rows
print(df.head())

# General info about the dataset
print(df.info())

# 1. Calculate averages
print("Average goals:", df["Goals"].mean())
print("Average assists:", df["Assists"].mean())
print("Average minutes played:", df["Minutes"].mean())

# 2. Top goal scorers
top_scorers = df.sort_values(by="Goals", ascending=False).head(5)
print("\nTop 5 goal scorers:")
print(top_scorers[["Player", "Goals"]])

# 3. Top assist providers
top_assists = df.sort_values(by="Assists", ascending=False).head(5)
print("\nTop 5 assist providers:")
print(top_assists[["Player", "Assists"]])

# 4. Total goal contributions (goals + assists)
df["Total_Contributions"] = df["Goals"] + df["Assists"]
top_total = df.sort_values(by="Total_Contributions", ascending=False).head(5)
print("\nTop 5 players by total contributions (goals + assists):")
print(top_total[["Player", "Goals", "Assists", "Total_Contributions"]])

# Plot: Top 5 Goal Scorers - Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(data=top_scorers, x="Player", y="Goals", palette="viridis")
plt.title("Top 5 Goal Scorers")
plt.ylabel("Goals Scored")
plt.xlabel("Player")
plt.show()

# Plot: Top 5 Assist Providers - Bar Chart
plt.figure(figsize=(10,6))
sns.barplot(data=top_assists, x="Player", y="Assists", palette="magma")
plt.title("Top 5 Assist Providers")
plt.ylabel("Assists")
plt.xlabel("Player")
plt.show()

# Plot: Total Contributions (Goals + Assists) for Top 5 Players
plt.figure(figsize=(10,6))
sns.barplot(data=top_total, x="Player", y="Total_Contributions", palette="coolwarm")
plt.title("Top 5 Players by Total Contributions")
plt.ylabel("Total Goals + Assists")
plt.xlabel("Player")
plt.show()