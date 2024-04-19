import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



# Read data from csv file vehicled_us_clean.csv
df = pd.read_csv('./vehicles_us_cleaned.csv')

# Title of the app centered
st.title('US Vehicle Advertisement Listings')

# Show data in the app
st.write(df)

# histogram of the types of vehicles by manufacturer
st.subheader('Histogram of the types of vehicles by manufacturer')
vehicle_sales = df.groupby(['Manufacturer', 'Type']).size().reset_index(name='Vehicles Sold')

# Plot histogram with Manufacturer on the x-axis, Vehicles Sold on the y-axis, and Type as color
fig = px.histogram(vehicle_sales, x='Manufacturer', y='Vehicles Sold', color='Type',
                   title='Number of Vehicles Sold by Manufacturer and Type')
# Set the y-axis limit to
fig.update_yaxes(range=[100,13000])
# plot the histogram
st.plotly_chart(fig)


# histogram of price distribution of Manufacturer between manufacturers
st.subheader('Histogram of price distribution between manufacturers')
# Multiselect widget for selecting manufacturers
selected_condition = st.multiselect('Select Condition', df['Condition'].unique())

# Filter the DataFrame based on selected manufacturers
filtered_df = df[df['Condition'].isin(selected_condition)]
# create a normalized histogram checkbox
normalized = st.checkbox('Normalized', key='normalized_checkbox')

# create a histogram with manufacturer1 and manufacturer2 input
fig = px.histogram(df, x='Condition', y='Price', color='Manufacturer', 
                   hover_data=df.columns)



# Check if normalization checkbox is checked
if normalized:
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)

# x-axis title
fig.update_xaxes(title_text='Manufacturer')
# y-axis title
fig.update_yaxes(title_text='Price')
# Set the y-axis limit
fig.update_yaxes(range=[100000, 160000000])

# plot the histogram
st.plotly_chart(fig)



#Scatter Plot
st.subheader('Scatter Plot')
fig1 = px.scatter(df, x='Model year', y='Price')
st.subheader("Scatter Plot: Price vs. Model Year")

fig1.update_yaxes(range=[10000, 400000])
fig1.update_xaxes(range=[1960, 2020])

st.plotly_chart(fig1)