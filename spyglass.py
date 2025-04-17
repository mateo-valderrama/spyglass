from googlesearch import search
import requests
from bs4 import BeautifulSoup
import spacy
#from linkedin_scraper import Person, actions
from selenium import webdriver

nlp = spacy.load('en_core_web_sm')

def search_links(query):
    return [url for url in search(query, num_results=10)]

def get_page_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except:
        return ""
    
def extract_keywords(text):
    doc = nlp(text)
    return [chunk.text for chunk in doc.noun_chunks if len(chunk.text) > 3]