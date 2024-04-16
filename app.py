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


# histogram of price distribution of condition between manufacturers
st.subheader('Histogram of price distribution between manufacturers')
# drop down menu for selecting the manufacturer 1 and 2 
# index 1 and 2 are used to set default values for the drop down menu
manufacturer1 = st.selectbox('Manufacturer 1', df['Manufacturer'].unique(), index=1)
manufacturer2 = st.selectbox('Manufacturer 2', df['Manufacturer'].unique(), index=2)

# create a normalized histogram checkbox
normalized = st.checkbox('Normalized')

# create a histogram with manufacturer1 and manufacturer2 input
fig = px.histogram(df, x='Price', y='Condition', color='Manufacturer', 
                   marginal='rug',  # adds marginal rug plots
                   hover_data=df.columns)

# Check if normalization checkbox is checked
if normalized:
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)


# Set the y-axis limit
fig.update_yaxes(range=[100, 13000])

# Set the x-axis limit
fig.update_xaxes(range=[100, 13000])

# plot the histogram
st.plotly_chart(fig)



# scatter plot matrix 
st.subheader('Scatter plot matrix')
# drop down for each dimension 
# index 1, 2, and 3 are used to set default values for the drop down menu
x_axis = st.selectbox('X axis', df.columns, index=1)
y_axis = st.selectbox('Y axis', df.columns, index=2)
# drop down for the color
color = st.selectbox('Color', df.columns, index=3)
# subheader for the scatter plot matrix that automatically updates
st.subheader(f'Scatter plot matrix of {x_axis} and {y_axis} by {color}')
# create the scatter plot matrix
fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)
fig.update_xaxes(range=[1950, 2024])
# plot the scatter plot matrix
st.plotly_chart(fig)