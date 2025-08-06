import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


st.set_page_config(page_title="Website Analytics Dashboard", layout="wide")


df = pd.read_csv("website_analytics.csv")
df["date"] = pd.to_datetime(df["date"])


st.markdown("""
    <h1 style='text-align: center;'>Website Analytics Overview</h1>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Visitors", f"{df['visitors'].sum():,}")
col2.metric("Page Views", f"{df['page_views'].sum():,}")
col3.metric("Bounce Rate", f"{df['bounce_rate'].mean():.2f}%")
col4.metric("Avg. Session Duration", f"{df['avg_session_duration'].mean():.2f} sec")

st.markdown("---")


row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)


with row1_col1:
    st.subheader("Visitors Over Time")
    visitors_line = df[['date', 'visitors']].set_index('date')
    st.line_chart(visitors_line)


with row1_col2:
    st.subheader("Page Views by Country")
    country_views = df.groupby('country')['page_views'].sum().sort_values(ascending=False).reset_index()
    fig_country = px.bar(country_views, x='country', y='page_views', color='country', height=400)
    st.plotly_chart(fig_country, use_container_width=True)


with row2_col1:
    st.subheader("Device Distribution")
    device_counts = df['device'].value_counts().reset_index()
    device_counts.columns = ['device', 'count']
    fig_device = px.pie(device_counts, values='count', names='device', hole=0.4)
    fig_device.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_device, use_container_width=True)


with row2_col2:
    st.subheader("Traffic Source Distribution")
    traffic_counts = df['traffic_source'].value_counts().reset_index()
    traffic_counts.columns = ['source', 'count']
    fig_traffic = px.pie(traffic_counts, values='count', names='source', hole=0.4)
    fig_traffic.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_traffic, use_container_width=True)


st.markdown("---")
st.subheader("Preview of Website Analytics Data")
st.dataframe(df.head(15), use_container_width=True)
