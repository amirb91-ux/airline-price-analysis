# Airline Ticket Price Analysis
# EDA - looking at price patterns across airlines, routes and booking behavior

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/airline_ticket_prices.csv")

print("Shape:", df.shape)
print(df.head())
print(df.dtypes)
print(df.isnull().sum())
print(df.describe().round(2))

# adding price per km to compare routes more fairly
df["price_per_km"] = (df["Price_USD"] / df["Distance_km"]).round(4)

# grouping by how early the ticket was booked
df["booking_window"] = pd.cut(
    df["Days_Before_Departure"],
    bins=[0, 30, 60, 90, 120],
    labels=["0-30 days", "31-60 days", "61-90 days", "91+ days"]
)

# price distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Price_USD"], bins=20, kde=True, color="steelblue")
plt.title("Price Distribution")
plt.xlabel("Price (USD)")
plt.tight_layout()
plt.savefig("reports/price_distribution.png", dpi=150)
plt.show()

# economy vs business vs first
plt.figure(figsize=(7, 5))
class_avg = df.groupby("Class")["Price_USD"].mean().reindex(["Economy", "Business", "First"])
bars = plt.bar(class_avg.index, class_avg.values, color=["#55A868", "#C44E52", "#8172B2"])
plt.bar_label(bars, fmt="$%.0f", padding=4)
plt.title("Average Price by Class")
plt.ylabel("Price (USD)")
plt.tight_layout()
plt.savefig("reports/price_by_class.png", dpi=150)
plt.show()

# which airline charges more on average
plt.figure(figsize=(9, 5))
airline_avg = df.groupby("Airline")["Price_USD"].mean().sort_values()
airline_avg.plot(kind="barh", color="steelblue")
plt.title("Average Price by Airline")
plt.xlabel("Price (USD)")
plt.tight_layout()
plt.savefig("reports/price_by_airline.png", dpi=150)
plt.show()

# does longer distance mean higher price?
plt.figure(figsize=(8, 5))
class_colors = {"Economy": "#55A868", "Business": "#C44E52", "First": "#8172B2"}
for cls, group in df.groupby("Class"):
    plt.scatter(group["Distance_km"], group["Price_USD"],
                label=cls, alpha=0.6, s=50, color=class_colors[cls])
plt.title("Price vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Price (USD)")
plt.legend(title="Class")
plt.tight_layout()
plt.savefig("reports/price_vs_distance.png", dpi=150)
plt.show()

# does booking earlier save money?
plt.figure(figsize=(7, 5))
bw_avg = df.groupby("booking_window", observed=True)["Price_USD"].mean()
bw_avg.plot(kind="bar", color=sns.color_palette("Set2", 4), rot=0)
plt.title("Average Price by Booking Window")
plt.xlabel("Days Before Departure")
plt.ylabel("Price (USD)")
plt.tight_layout()
plt.savefig("reports/price_by_booking_window.png", dpi=150)
plt.show()

# correlation between numerical features
# wanted to check if distance and days before departure
# actually affect the price or if it's mostly driven by the class
corr = df[["Distance_km", "Days_Before_Departure", "Price_USD", "price_per_km"]].corr()
plt.figure(figsize=(6, 5))
corr = df[["Distance_km", "Days_Before_Departure", "Price_USD", "price_per_km"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0, square=True)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("reports/correlation_heatmap.png", dpi=150)
plt.show()

print("\n--- Key Findings ---")
print("Most expensive airline:", df.groupby("Airline")["Price_USD"].mean().idxmax())
print("Cheapest airline:", df.groupby("Airline")["Price_USD"].mean().idxmin())
print("Avg price by class:")
print(df.groupby("Class")["Price_USD"].mean().round(2))
print("Correlation distance/price:", df["Distance_km"].corr(df["Price_USD"]).round(3))
print("Correlation days ahead/price:", df["Days_Before_Departure"].corr(df["Price_USD"]).round(3))