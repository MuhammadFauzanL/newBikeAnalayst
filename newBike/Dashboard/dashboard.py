import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

all_df = pd.read_csv("Finish_data.csv")


all_df['dteday'] = pd.to_datetime(all_df['dteday'])


st.title("Analisis Penyewaan Sepeda")

if st.checkbox("Tampilkan Data Mentah"):
    st.subheader("Data Mentah")
    st.write(all_df)

st.subheader("Jumlah Penyewaan Sepeda per Jam")
total_by_hour = all_df.groupby('hour')['count'].sum().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(total_by_hour['hour'], total_by_hour['count'], color='skyblue')
ax.set_title('Jumlah Penyewaan Sepeda per Jam', fontsize=14)
ax.set_xlabel('Jam', fontsize=12)
ax.set_ylabel('Jumlah Penyewaan', fontsize=12)
ax.set_xticks(total_by_hour['hour'])
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
plt.tight_layout()
st.pyplot(fig)

st.subheader("Total Jumlah Pendaftar pada Hari Kerja berdasarkan Situasi Cuaca")
df_workingday = all_df[all_df['workingday'] == 1]
result = df_workingday.groupby(['weather_situation'])['registered'].sum()

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(result.index, result.values, color='skyblue')
ax.set_title('Total Jumlah Pendaftar pada Hari Kerja\nBerdasarkan Situasi Cuaca', fontsize=14)
ax.set_xlabel('Situasi Cuaca', fontsize=12)
ax.set_ylabel('Jumlah Pendaftar', fontsize=12)

weather_labels = {1: 'Cerah', 2: 'Berawan', 3: 'Hujan ringan', 4: 'Hujan lebat'}
ax.set_xticks(result.index)
ax.set_xticklabels([weather_labels.get(i, i) for i in result.index])

ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
plt.tight_layout()
st.pyplot(fig)

st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari")
weekday_counts = all_df.groupby('weekday')['count'].sum()

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(weekday_counts.index, weekday_counts.values)
ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Hari')
ax.set_xlabel('Hari dalam Seminggu (0=Minggu, 1=Senin, dst.)')
ax.set_ylabel('Jumlah Penyewaan')
ax.set_xticks(weekday_counts.index)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
plt.tight_layout()
st.pyplot(fig)