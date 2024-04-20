import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



# Read data from csv file vehicled_us_clean.csv
df = pd.read_csv('./vehicles_us_cleaned.csv')

# Title of the app centered
st.title('US Vehicle Advertisement Listings')





# histogram of the types of vehicles by manufacturer
st.header('Histogram of the types of vehicles by manufacturer')
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
fig.update_xaxes(range=[1000, 30000])
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




st.write("""
##### Filter the data below:
""")

# if checkbox marked, only listings that are 10 days old or less will be shown
new_listings = st.checkbox('Include only young listings (only 10 days old or less)')
if new_listings is True:
     df = df[df['Days listed'] <= 10]

# creating filtered data by model and year
# creating a list of unique car models
model_condition = df['Condition'].unique()

# creating slider
made_choice = st.selectbox('Select model:', model_condition)


# year range for slider
min_year = 1960
max_year = int(df['Model year'].max())
year_range = st.slider(
     "Choose year",
     value = (min_year,max_year), min_value=min_year, max_value=max_year )

# creating list of years
actual_range=list(range(year_range[0], year_range[1]+1))

# filtering data with picked parameters and showing 5 first rows of filtered table 
filtered_df = df[(df.Condition == made_choice) & (df['Model year'].isin(list(actual_range)))]
st.table(filtered_df.head(5))



# histogram of price depending on transmission, cylinders, type, condition
st.title('Histogram of Price Depending on Transmission, Cylinders, Type, and Condition')

# Create a checkbox for normalization
normalized_checkbox = st.checkbox('Normalize')

# Creating list of parameters
list_of_param = ['Transmission', 'Cylinders', 'Type', 'Condition']

# Creating selectbox to choose the parameter for histogram
choice_of_param = st.selectbox('Split for price distribution', list_of_param)

# Check if list_of_param is not empty before using it
if list_of_param:
    # Creating selectbox to choose the parameter for histogram
    choice_of_param = st.selectbox('Split for price distribution', list_of_param)

    # Creating histogram 
    fig = px.histogram(df, x="Price", color=choice_of_param)

    # Adjust histogram based on checkbox state
    if normalized_checkbox:
        fig.update_layout(barmode='overlay')
        fig.update_traces(opacity=0.75)

    # Setting title and axis labels
    fig.update_layout(title="<b> Split of price by {}</b>".format(choice_of_param), xaxis_title='Price', yaxis_title='Number of listings')

    # Setting the range of the x-axis to be between 1000 and 50000 to make visualization more clear
    fig.update_xaxes(range=[1000, 30000])
    fig.update_yaxes(range=[1000, 2500])

    # Displaying the histogram
    st.plotly_chart(fig)
else:
    st.warning("No parameters available for histogram selection.")