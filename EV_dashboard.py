# EV_dashboard.py
# Streamlit Dashboard for Electric Vehicle Market Analysis

import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------
# Page Config
# ----------------------
st.set_page_config(page_title="EV Market Analysis", layout="wide")

# ----------------------
# Title & Description
# ----------------------
st.title("🚗 Electric Vehicle Market Analysis - India")

st.markdown("""
**Author:** Vishnu Kumar  
**Project:** Web Scraping + Data Analysis + Visualization  

This dashboard presents insights on the Indian EV market.
Data is collected from **CarDekho** and includes:
- Brand & Model
- Price (Lakh ₹)
- Driving Range (km)
- Battery Capacity (kWh)
- Power (bhp)

""")

# ----------------------
import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------
# Load Data
# ----------------------
df = pd.read_csv("EV_cleaned.csv")

# Convert price to numeric (if needed)

# Metrics
total_models = df.shape[0]
avg_range = round(df["Range"].mean(),1)
avg_price = round(df["Price"].mean(),2)
avg_battery = round(df["Battery"].mean(),2)

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total EV Models", total_models)
col2.metric("Average Range (km)", avg_range)
col3.metric("Average Price (Lakh ₹)", avg_price)
col4.metric("Average Battery Capacity (kWh)", avg_battery)

brand_count = df.groupby("Brand")["Model"].count().reset_index()
brand_count.rename(columns={"Model": "Count"}, inplace=True)
# Plot
# ----------------------
st.subheader("1️⃣ EV Models by Brand")
fig1 = px.bar(
    brand_count,
    x="Brand",
    y="Count",
    color="Brand",
    hover_data=["Count"],
    title="Number of EV Models per Brand",
    height=500,
    width=900
)

st.plotly_chart(fig1)

st.subheader("Insights: Brand vs Number of EV Models")
st.markdown("""
- **Tata** has the most EV models, focusing on affordable/mid-range segment.  
- **BMW, Kia, BYD** focus on premium EVs with fewer models.  
- **Mahindra, MG, Hyundai** are growing in the mid-range segment.  
- Clear segmentation exists: volume vs premium vs mid-range strategies.
""")

st.subheader("2️⃣ Price vs Driving Range of All EVs in India")

# Scatter plot for all EVs
fig = px.scatter(
    df,
    x="Price",
    y="Range",
    color="Brand",
    hover_data=["Model", "Battery", "Power"],
    title="Price vs Driving Range",
    height=600,
    width=900
)

st.plotly_chart(fig)

# ----------------------
# Insights
# ----------------------
st.markdown("""
**Insights:**

- **Higher-priced EVs generally have longer driving ranges.**
  Premium brands like Kia and BMW dominate the higher price segment.
- **Affordable brands (Tata, Mahindra) cluster in mid-range** (around 400–500 km).
- **Price and range are positively correlated** — bigger batteries typically give longer ranges.
- Hovering over points reveals **model-specific price, battery, and power**.
""")

st.subheader("3️⃣ Battery Capacity vs Driving Range of EVs")

# Scatter plot
fig = px.scatter(
    df,
    x="Battery",
    y="Range",
    color="Brand",
    hover_data=["Model", "Price", "Power"],
    title="Battery Capacity vs Driving Range",
    height=600,
    width=900
)

st.plotly_chart(fig)

# Insights
st.markdown("""
**Insights:**

- **Battery capacity strongly correlates with driving range** — EVs with bigger batteries typically have longer range.
- Premium EVs (Kia, BMW) tend to have **larger battery capacities**, contributing to higher ranges.
- Affordable EVs (Tata, Mahindra) have **moderate battery sizes**, clustering in 400–500 km range.
""")


st.subheader("4️⃣ Average EV Price by Brand")

# Calculate average price per brand
avg_price = df.groupby("Brand")["Price"].mean().reset_index()

# Bar chart
fig = px.bar(
    avg_price,
    x="Brand",
    y="Price",
    color="Brand",
    hover_data=["Price"],
    title="Average EV Price by Brand (Lakh ₹)",
    height=600,
    width=900
)

st.plotly_chart(fig)

# Insights
st.markdown("""
**Insights:**

- **Premium brands (Kia, BMW)** have the highest average prices.
- **Tata and Maruti** have lower average prices, focusing on **affordable EVs**.
- This chart clearly shows the **market segmentation**: premium vs mid-range vs affordable EVs.
""")

st.subheader("5️⃣ Driving Range Distribution of EVs")

# Histogram
fig = px.histogram(
    df,
    x="Range",
    nbins=10,
    color="Brand",
    hover_data=["Model","Price","Battery","Power"],
    title="Distribution of EV Driving Ranges",
    height=600,
    width=900
)

st.plotly_chart(fig)

# Insights
st.markdown("""
**Insights:**

- **Most EVs in India fall into the 400–500 km range**, which is currently the mainstream segment.
- Premium EVs extend beyond 500 km, highlighting **high-end market targeting longer range**.
- Histogram helps identify **popular range segments and outliers** in the market.
""")