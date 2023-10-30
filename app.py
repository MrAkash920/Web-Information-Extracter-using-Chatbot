import openai
import requests
from bs4 import BeautifulSoup
import streamlit as st


openai.api_key = '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'

def scrape_info(url):
    try:
        
        response = requests.get(url)

        
        soup = BeautifulSoup(response.text, 'html.parser')

       
        title = soup.title.text

        return title
    except Exception as e:
        return str(e)

def chat_with_bot(question, website_url):
    context = f"Question: {question}\nWebsite: {scrape_info(website_url)}"

    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=context,
        max_tokens=2000,  
    )

    return response.choices[0].text

st.title("Website Chatbot")

website_url = st.text_input("Enter the URL of the website:")

widget_counter = 0


user_question = st.text_input("Ask a question (or type 'exit' to quit):", key=f"question_{widget_counter}")

if st.button("Ask") and user_question:
    if website_url:
        answer = chat_with_bot(user_question, website_url)
        st.write("Answer:", answer)
    else:
        st.write("Please enter a valid website URL.")
    
    widget_counter += 1
