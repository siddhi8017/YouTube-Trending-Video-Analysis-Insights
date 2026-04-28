# ==============================
# 1. IMPORT LIBRARIES
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: make plots look better
sns.set_style("whitegrid")


# ==============================
# 2. LOAD DATASET
# ==============================
df = pd.read_csv("youtube.csv")

print("First 5 rows:")
print(df.head())


# ==============================
# 3. BASIC INFORMATION
# ==============================
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# ==============================
# 4. DATA CLEANING
# ==============================
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing description
df['description'].fillna("No Description", inplace=True)


# ==============================
# 5. CONVERT DATE COLUMN
# ==============================
df['trending_date'] = pd.to_datetime(df['trending_date'], format='%y.%d.%m')


# ==============================
# 6. TOP 10 MOST VIEWED VIDEOS
# ==============================
top_views = df.sort_values(by='views', ascending=False).head(10)

plt.figure()
plt.barh(top_views['title'], top_views['views'])
plt.title("Top 10 Most Viewed Videos")
plt.xlabel("Views")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()


# ==============================
# 7. CATEGORY-WISE AVERAGE VIEWS
# ==============================
category_views = df.groupby('category_id')['views'].mean()

plt.figure()
category_views.plot(kind='bar')
plt.title("Average Views per Category")
plt.xlabel("Category ID")
plt.ylabel("Average Views")
plt.show()


# ==============================
# 8. LIKES VS DISLIKES
# ==============================
plt.figure()
sns.scatterplot(x='likes', y='dislikes', data=df)
plt.title("Likes vs Dislikes")
plt.xlabel("Likes")
plt.ylabel("Dislikes")
plt.show()


# ==============================
# 9. CORRELATION HEATMAP
# ==============================
plt.figure()
sns.heatmap(df[['views', 'likes', 'dislikes', 'comment_count']].corr(), annot=True)
plt.title("Correlation Matrix")
plt.show()


# ==============================
# 10. EXTRA ANALYSIS (OPTIONAL BUT GOOD)
# ==============================
# Top 10 channels by total views
top_channels = df.groupby('channel_title')['views'].sum().sort_values(ascending=False).head(10)

plt.figure()
top_channels.plot(kind='bar')
plt.title("Top 10 Channels by Total Views")
plt.ylabel("Views")
plt.show()


# ==============================
# 11. INSIGHTS (PRINT OUTPUT)
# ==============================
print("\n🔍 Insights:")
print("1. Videos with higher views tend to receive more likes.")
print("2. Some categories consistently attract more viewers.")
print("3. Popular videos generate higher audience engagement (comments).")
print("4. Top channels dominate trending videos repeatedly.")