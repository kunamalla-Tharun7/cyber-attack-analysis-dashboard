import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Tharun@19",
        database="cyber_attacks_analysis",
        port=3306
    )


# -----------------------------
# LOAD DATA FROM MYSQL
# -----------------------------
@st.cache_data
def load_data():
    conn = get_connection()

    query = "SELECT * FROM cyber_attacks"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


# -----------------------------
# STREAMLIT PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="Cyber Attacks Dashboard",
    layout="wide"
)

st.title("🌍 Global Cyber Attacks Analysis Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
df = load_data()

if df.empty:
    st.warning("No data found in database")
    st.stop()

# -----------------------------
# METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Attacks", len(df))
col2.metric("Countries Affected", df["country"].nunique())
col3.metric("Industries Targeted", df["industry"].nunique())


st.divider()

# -----------------------------
# TOP ATTACKED COUNTRIES
# -----------------------------
st.subheader("Top Attacked Countries")

country_df = (
    df.groupby("country")
    .size()
    .reset_index(name="Attacks")
    .sort_values(by="Attacks", ascending=False)
    .head(10)
)

fig1 = px.bar(
    country_df,
    x="country",
    y="Attacks",
    color="Attacks",
    title="Top 10 Targeted Countries"
)

st.plotly_chart(fig1, use_container_width=True)


# -----------------------------
# MOST TARGETED INDUSTRIES
# -----------------------------
st.subheader("Most Targeted Industries")

industry_df = (
    df.groupby("industry")
    .size()
    .reset_index(name="Attacks")
    .sort_values(by="Attacks", ascending=False)
)

fig2 = px.bar(
    industry_df,
    x="industry",
    y="Attacks",
    color="Attacks",
    title="Industry Attack Distribution"
)

st.plotly_chart(fig2, use_container_width=True)


# -----------------------------
# ATTACK TREND OVER TIME
# -----------------------------
st.subheader("Cyber Attacks Over Years")

year_df = (
    df.groupby("year")
    .size()
    .reset_index(name="Attacks")
)

fig3 = px.line(
    year_df,
    x="year",
    y="Attacks",
    markers=True,
    title="Cyber Attack Trend"
)

st.plotly_chart(fig3, use_container_width=True)


# -----------------------------
# FINANCIAL LOSS BY ATTACK TYPE
# -----------------------------
st.subheader("Financial Loss by Attack Type")

loss_df = (
    df.groupby("attack_type")["financial_loss"]
    .sum()
    .reset_index()
    .sort_values(by="financial_loss", ascending=False)
)

fig4 = px.bar(
    loss_df,
    x="attack_type",
    y="financial_loss",
    color="financial_loss",
    title="Financial Loss by Attack Type"
)

st.plotly_chart(fig4, use_container_width=True)


# -----------------------------
# SEARCH FUNCTION
# -----------------------------
st.subheader("Search Attacks by Country")

country_search = st.text_input("Enter country name")

if country_search:
    filtered = df[df["country"].str.contains(country_search, case=False)]

    st.write(filtered)