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

# histogram of price depending on transmission, cylinders, type, condition
st.title('Histogram of Price Depending on Transmission, Cylinders, Type, and Condition')
# creating list of parameters
list_of_param=['Transmission','Cylinders','Type', 'Condition']
# creatins selectbox to choose the parameter for histogram
choice_of_param = st.selectbox('Split for price distribution', list_of_param)
# creating histogram 
fig = px.histogram(df, x="Price", color=choice_of_param)
# setting title and axis labels
fig.update_layout(title="<b> Split of price by {}</b>".format(choice_of_param), xaxis_title='Price', yaxis_title='Number of listings')
# setting the range of the x-axis to be between 1000 and 50000 to make visualization more clear
fig.update_xaxes(range=[1000, 50000])
fig.update_yaxes(range=[1000, 2500])
# displaing the histogram
st.plotly_chart(fig)



#Scatter Plot
st.subheader('Scatter Plot')
fig1 = px.scatter(df, x='Model year', y='Price')
st.subheader("Scatter Plot: Price vs. Model Year")

fig1.update_yaxes(range=[10000, 400000])
fig1.update_xaxes(range=[1960, 2020])

st.plotly_chart(fig1)