import requests
import streamlit as st

url="https://newsdata.io/api/1/news?apikey=pub_29126c9014eabeea4cc21d9c04c0bfa1a2fe5&q=pegasus&language=en"
response_data=requests.get(url)
data=response_data.json()


st.title('News')

# Create a button to iterate through the loop
if st.button('Next Article'):
    for i in range(len(data['results'])):
        article = data['results'][i]
        st.subheader(article['title'])
        st.write(article['description'])