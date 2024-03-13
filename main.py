# Fixed variables and imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the datasets
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Set page title
st.title("Bike Share Dashboard Dicoding")

# Sidebar
st.sidebar.title("My Information:")
st.sidebar.markdown("**• Nama: Divania Aulya Dewi**")
st.sidebar.markdown("**• Email: [divaniadewi@gmail.com](mailto:divaniadewi@gmail.com)**")
st.sidebar.markdown("**• Dicoding: [divaniaaulya](https://www.dicoding.com/users/divaniaaulya/)**")

st.sidebar.title("Dataset Bike Share")

# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(day_df) 

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(day_df.describe())  

# Melengkapi Dashboard dengan Berbagai Visualisasi Data
st.header('Bike Sharing :sparkles:')

st.subheader('Daily Sharing')
col1, col2, col3 = st.columns(3)
 
with col1:
    total_orders = day_df['cnt'].sum()
    st.metric("Total Sharing Bike", value=total_orders)

with col2:
    total_sum = day_df['registered'].sum()
    st.metric("Total Registered", value=total_sum)

with col3:
    total_sum = day_df['casual'].sum()
    st.metric("Total Casual", value=total_sum)


#Jam ketika paling banyak dan paling sedikit disewa
st.subheader("Pada jam berapa yang paling banyak dan paling sedikit disewa?")
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))

sns.barplot(x="hr", y="cnt", data=hour_df.head(5), palette=["#D3D3D3", "#D3D3D3", "#90CAF9", "#D3D3D3", "#D3D3D3"], ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Hours (PM)", fontsize=10)
ax[0].set_title("Jam dengan banyak penyewa sepeda", loc="center", fontsize=10)
ax[0].tick_params(axis='y', labelsize=10)
ax[0].tick_params(axis='x', labelsize=10)
 
sns.barplot(x="hr", y="cnt", data=hour_df.sort_values(by="hr", ascending=True).head(5), palette=["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#90CAF9"], ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Hours (AM)",  fontsize=10)
ax[1].set_title("Jam dengan sedikit penyewa sepeda", loc="center", fontsize=10)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].tick_params(axis='y', labelsize=10)
ax[1].tick_params(axis='x', labelsize=10)

st.pyplot(fig)

# Display untuk Perbandingan Customer yang Registered dengan Casual
st.subheader("Perbandingan Customer yang Registered dengan Casual")
labels = 'casual', 'registered'
sizes = [day_df['casual'].sum(), day_df['registered'].sum()]
explode = (0, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=["#D3D3D3", "#90CAF9"],
        shadow=True, startangle=90)
ax1.axis('equal')  
st.pyplot(fig1)

# Filter data based on temperature
temp_slider = st.slider("Filter data berdasarkan Suhu", float(day_df['temp'].min()), float(day_df['temp'].max()))
filtered_data = day_df[day_df['temp'] <= temp_slider]
st.write(filtered_data)

st.caption('Copyright (C) Divania Aulya Dewi 2024')