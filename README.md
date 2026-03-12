# Electric Vehicle Market Analysis - India

This project is a **Streamlit dashboard** that visualizes the Indian Electric Vehicle (EV) market using data collected from [CarDekho](https://www.cardekho.com/electric-cars).  
It provides insights into **price, driving range, battery capacity, and brand segmentation** for EVs in India.

---

## Features

- Number of EV models per brand  
- Price vs Driving Range scatter plot  
- Battery Capacity vs Driving Range scatter plot  
- Average Price by Brand bar chart  
- Driving Range Distribution histogram  
- Hover to see detailed model info: battery, power, price  

---

## Dataset

- Collected from CarDekho: [https://www.cardekho.com/electric-cars](https://www.cardekho.com/electric-cars)  
- Cleaned and analyzed using **Python (Pandas, Plotly)**  
- Saved as `EV_cleaned.csv`  

---

## Installation

```bash
# Clone the repo
git clone <your_repo_url>
cd EV_car_Analysis

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit dashboard
streamlit run EV_dashboard.py

st.plotly_chart(fig)

# Insights
st.markdown("""
**Insights:**

- **Most EVs in India fall into the 400–500 km range**, which is currently the mainstream segment.
- Premium EVs extend beyond 500 km, highlighting **high-end market targeting longer range**.
- Histogram helps identify **popular range segments and outliers** in the market.
""")