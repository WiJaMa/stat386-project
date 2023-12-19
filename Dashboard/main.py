import pandas as pd
import numpy as np
import math as math

import streamlit as st
import plotly.express as px

df = pd.read_csv('keqiang.csv')

df.rename(columns = {'energy_cons': 'Energy Consumption',
                    'rail_cargo': 'Railway Cargo',
                    'urban_per': 'Percent Urban',
                    'service_per': 'Percent Services'},inplace = True)

st.title("Li Keqiang Index Project---Data Exploration")

st.header('Explore Quantitative Variables')

st.subheader('Univariate Exploration')
st.markdown('Examine the univariate distribution of each quantitative variable. [See examples from EDA.](https://wijama.org/2023/12/15/Li-Keqiang-Index-Introduction-and-EDA.html#:~:text=Exploratory%20Data%20Analysis)')
selected_var = st.selectbox('Select a Variable', ['Year','Democracy Index','Energy Consumption','Railway Cargo','Percent Urban','Percent Services','GDP'])
hist_series = df[selected_var]

if st.checkbox('Log variable'):
    fig = px.histogram(x= [math.log(item) for item in hist_series])
    st.plotly_chart(fig)
else:
    fig = px.histogram(df, x= hist_series)
    st.plotly_chart(fig)

st.subheader("Bivariate Exploration")
st.markdown('Examine quantitative variables in relation to each other. [For examples, see pair plot from EDA](https://wijama.org/2023/12/15/Li-Keqiang-Index-Introduction-and-EDA.html#:~:text=pair%20plot)')
scatter_var1, scatter_var2 = st.multiselect('Select Two Variables', ['Year','Democracy Index','Energy Consumption','Railway Cargo','Percent Urban','Percent Services','GDP'], ['Railway Cargo', 'GDP'], max_selections = 2)
if st.checkbox(f'Log {scatter_var1}'):
    scatter_series1 = [math.log(item) for item in df[scatter_var1]]
else: 
    scatter_series1 = df[scatter_var1]
if st.checkbox(f'Log {scatter_var2}'):
    scatter_series2 = [math.log(item) for item in df[scatter_var2]]
else: 
    scatter_series2 = df[scatter_var2]

if st.checkbox('Trendline'):
    scatter_trendline="ols"
else:
    scatter_trendline=None
if st.checkbox('Color Region'):
    color_region = "Region"
else:
    color_region = None

scatter_fig = px.scatter(df, x=scatter_series1, y=scatter_series2, color = color_region, trendline = scatter_trendline,
                         labels={
                        "x": scatter_var1,
                        "y": scatter_var2})
st.plotly_chart(scatter_fig)

st.subheader('Count of Data Points by Region')
st.markdown('Examine the number of data points from each region. [See comments on this in EDA.](https://wijama.org/2023/12/15/Li-Keqiang-Index-Introduction-and-EDA.html#:~:text=A%20countplot%20of%20data)')
reg_count = px.histogram(df, y= 'Region', barmode='group')
st.plotly_chart(reg_count)

st.subheader('Missing Values')
st.markdown('Examine the number of missing values by region. [See EDA for example.](https://wijama.org/2023/12/15/Li-Keqiang-Index-Introduction-and-EDA.html#:~:text=missing%20at%20least%20one%20value)')
num_missing = st.slider('Number of Missing Values', min_value = 0, max_value = 11, step = 1)

vc = df['Country'].value_counts() < 13 - num_missing
vc = vc[vc]

dropped_countries = df.loc[df['Country'].isin(vc.index)][['Country','Region']].drop_duplicates()
dropped_countries['Region'].value_counts()
missing_count = px.histogram(dropped_countries, y = 'Region', barmode='group',
                             title = f'Countries missing at least {num_missing} values by region').update_yaxes(categoryorder= 'total ascending')
st.plotly_chart(missing_count)