import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


df = pd.read_csv('dashboard/exported_data.csv')
    
df['datetime'] = pd.to_datetime(df['datetime'])

st.header('Air Quality Index (AQI) Dashboard :sparkles:')

st.subheader("PM2.5 Polution")
annual_df = df.resample(rule='Y', on='datetime').agg({
  "PM2.5": "mean",
  "PM10": "mean",
  "SO2": "mean",
  "NO2": "mean",
  "CO": "mean",
  "O3": "mean",
  "TEMP": "mean"
})

annual_df.index = annual_df.index.strftime('%Y')

fig = plt.figure(figsize=(10,5))
plt.plot(annual_df.index, annual_df['PM2.5'], label='PM2.5')
plt.xlabel("Year")
plt.ylabel("Concentration (μg/m3)")
plt.title("Air Pollutants over the Year")
plt.legend()
st.pyplot(fig)


st.subheader("PM10 Polution")

fig = plt.figure(figsize=(10,6))
plt.plot(annual_df.index, annual_df["PM10"], label="PM10")
plt.xlabel("Year")
plt.ylabel("Concentration (μg/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("SO2 Polution")

fig = plt.figure(figsize=(10,6))
plt.plot(annual_df.index, annual_df["SO2"], label="SO2")
plt.xlabel("Year")
plt.ylabel("Concentration (μg/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("NO2 Polution")

fig = plt.figure(figsize=(10,6))
plt.plot(annual_df.index, annual_df["NO2"], label="NO2")
plt.xlabel("Year")
plt.ylabel("Concentration (μg/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("CO Polution")

fig = plt.figure(figsize=(10,6))
plt.plot(annual_df.index, annual_df["CO"], label="CO")
plt.xlabel("Year")
plt.ylabel("Concentration (μg/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("O3 Polution")

fig = plt.figure(figsize=(10,6))
plt.plot(annual_df.index, annual_df["O3"], label="O3")
plt.xlabel("Year")
plt.ylabel("Concentration (μg/m3)")
plt.legend()
st.pyplot(fig)


st.subheader("CO Polution")

fig = plt.figure(figsize=(10,6))
plt.plot(annual_df.index, annual_df["CO"], label="CO")
plt.xlabel("Year")
plt.ylabel("Concentration (μg/m3)")
plt.legend()
st.pyplot(fig)


st.subheader("Temperature")
fig = plt.figure(figsize=(10,6))
plt.plot(annual_df.index, annual_df["TEMP"], label="TEMP")
plt.xlabel("Year")
plt.ylabel("°C")
plt.legend()
st.pyplot(fig)