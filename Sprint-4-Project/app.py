# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.title('US Vehicle Advertisement Listings')

df = pd.read_csv('./vehicles_us_cleaned.csv')

st.write(df)

st.subheader('Histogram of the types of vehicles by manufacturer')
fig = px.histogram(df, x='manufacturer', color='type')

st.plotly_chart(fig)

st.subheader('Histogram of price distribution between manufacturers')

manufacturer1 = st.selectbox('Manufacturer 1', df['manufacturer'].unique(), index=1)
manufacturer2 = st.selectbox('Manufacturer 2', df['manufacturer'].unique(), index=2)

normalized = st.checkbox('Normalized')

fig = px.histogram()
fig.add_trace(go.Histogram(x=df[df['manufacturer'] == manufacturer1]['price'], name=manufacturer1, opacity=0.75, histnorm='percent'))
fig.add_trace(go.Histogram(x=df[df['manufacturer'] == manufacturer2]['price'], name=manufacturer2, opacity=0.75, histnorm='percent'))

if normalized:
    fig.update_layout(barmode='overlay')
    fig.update_traces(opacity=0.75)

fig.update_xaxes(title_text='Price')

fig.update_yaxes(title_text='Percentage')

st.plotly_chart(fig)




st.subheader('Scatter plot matrix')

x_axis = st.selectbox('X axis', df.columns, index=1)
y_axis = st.selectbox('Y axis', df.columns, index=2)

color = st.selectbox('Color', df.columns, index=3)

st.subheader(f'Scatter plot matrix of {x_axis} and {y_axis} by {color}')

fig = px.scatter_matrix(df, dimensions=[x_axis, y_axis], color=color)

st.plotly_chart(fig)
