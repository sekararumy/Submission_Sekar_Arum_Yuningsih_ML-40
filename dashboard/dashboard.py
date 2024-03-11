
## IMPORT LIBRARY YANG DIGUNAKAN ##
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

## DATAFRAME ##
all_df = pd.read_csv("dashboard\main_data.csv")

#QUESTION 1#
def create_stations_df(df) :
    stations_df = all_df.groupby(by='station').agg({
        "PM2.5": ["mean"],
        "PM10" : ["mean"],
        "SO2"  : ["mean"],
        "NO2"  : ["mean"],
        "CO"   : ["mean"],
        "O3"   : ["mean"]
        }).mean(axis=1).round(2)
    return stations_df

#QUESTION 2#
def create_pollutants_df(df) :
    pollutants_df = all_df.groupby(by= 'station').agg({
        "PM10" : ["mean"],
        "SO2"  : ["mean"],
        "NO2"  : ["mean"],
        "CO"   : ["mean"],
        "O3"   : ["mean"]
        }).mean().round(2)
    return pollutants_df

## DASHBOARD VIEW ##
st.header(":sparkles: Beijing's Air Quality Dashboard :sparkles:")

#ADD TAB#
tab1, tab2 = st.tabs(["Diagram", "Data"])

#TAB 1#
with tab1:
    st.header('Average Pollutants by Station')

    st.metric(label="WANSHOUXIGONG (Biggest)", value="283.33 µm/m3")
    #Show the figure and its size
    fig, ax = plt.subplots(figsize=(12, 7))
    #Bar Chart
    create_stations_df(all_df).plot(kind='barh',
                                    color='#ad074a',
                                    label='Mean')
    ax.set_title('Tingkat Polutan di Beijing Tahun 2013-2017',
                fontsize=14, fontweight='bold')
    ax.set_xlabel('Rata-Rata Polutan',
                fontsize=12, fontweight='bold')
    ax.set_ylabel('Kota',
                fontsize=12, fontweight='bold')
    ax.grid(axis='x', linestyle='--', alpha=1)
    ax.legend()
    plt.tight_layout()
    #Show the Plot
    st.pyplot(fig)

    st.header('Overall Average Pollutants')

    st.metric(label="CARBON MONOXIDE (Biggest)", value="1235.68 µm/m3")
    #Show the figure and its size
    fig, ax = plt.subplots(figsize=(12, 7))
    #Bar Chart
    create_pollutants_df(all_df).plot(kind='bar',
                                    color='#ad074a',
                                    label='Mean')
    ax.set_title('Mayoritas Polutan di Beijing Tahun 2013-2017',
                fontsize=14, fontweight='bold')
    ax.set_xlabel('Jenis Polutan',
                fontsize=12, fontweight='bold')
    ax.set_ylabel('Rata-Rata Polutan',
                fontsize=12, fontweight='bold')
    ax.grid(axis='y', linestyle='--', alpha=1)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.legend()
    plt.tight_layout()
    #Show the Plot
    st.pyplot(fig)

#TAB 2#
with tab2:
    st.header("Beijing's Air Quality Data")
    st.table(data=create_stations_df(all_df))
    st.table(data=create_pollutants_df(all_df))

## ADD CAPTION ##
st.caption('Submission Dicoding © Sekar Arum Yuningsih 2024')