import wikipedia
import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

def wikipedia_info(tech_name, language):
    #Returns info from wikipedia related to the given technology concept in given language
    wikipedia.set_lang(language)
    response = wikipedia.page(tech_name).url
    return response

def summarize_text(url,sentence_number):
    #Returns the summary of the given wikipedia url in requested number of sentences
    string = 'http://api.meaningcloud.com/summarization-1.0?key=7341fb6a1d0dbba65050847d3b9054b1&sentences='
    string = string +sentence_number
    string = string + "&url="
    string = string + url
    information = requests.get(string)
    summary_text = information.json()
    return summary_text['summary']
    
def get_ebooks(tech_name):
    #Returns the list of ebooks according to the input
    string = 'https://www.googleapis.com/books/v1/volumes?q='
    string = string + tech_name
    ebook_list = requests.get(string) # getting data from api
    ebook_list = ebook_list.json()
    
    return ebook_list['items'] 
    
def get_text(transcript):
    #Returns the list of videos according to the input
    text = ''
    d=0
    for i in range(len(transcript)//6):
        d = d+1
        
        text= text + transcript[i]['text']
        if d==6:
            d=0
            text = text +  '. '
    return text
        
def translate_text(text,language):
    url_for_translation = 'https://api.deepl.com/v2/translate?auth_key=1169a1dc-f264-c753-0772-f6f97e808be9&text=' + text + '&target_lang='+language
    r = requests.post(url_for_translation)
    translated_text = r.json()
    translated_text = translated_text['translations']
    translated_text = translated_text[0]['text']      
    return translated_text

  
def get_trendy_skills():
    #Scrapes the list of the trendy tech skills from the web
    r = requests.get("https://www.cnbc.com/2019/11/19/these-will-be-the-top-10-most-popular-tech-skills-of-2020.html")
    soup = BeautifulSoup(r.content, 'html.parser')
    
    headings = soup.find_all('h2')
    
    
    search_word = str(headings[0]).split('1.')[1].split('<')[0] + '5 mins explanation'
    
    return search_word

def get_video_list(search_word,language,sentence_number):
    string =  "https://www.googleapis.com/youtube/v3/search?key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0&type=video&part=snippet&maxResults=4&q=" + search_word
        
    information = requests.get(string)

    video_list = information.json()

    for e in video_list['items']:
        
        video_id = e['id']['videoId']
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        text = ''
        d=0
        for i in range(len(transcript)//2):
            d = d+1
            
            text= text + transcript[i]['text']
            if d==3:
                d=0
                text = text +  '. '
        
        string = 'http://api.meaningcloud.com/summarization-1.0?key=7341fb6a1d0dbba65050847d3b9054b1&sentences='+sentence_number
        string = string + "&txt="
        string = string + text
        
        information = requests.get(string)
        
        information = information.json()
        
        text =  information['summary']
        url_for_translation = 'https://api.deepl.com/v2/translate?auth_key=1169a1dc-f264-c753-0772-f6f97e808be9&text=' + text + '&target_lang='+language.lower()[:2]
        r = requests.post(url_for_translation)
        translatedText = r.json()
        translatedText = translatedText['translations']

        translatedText = translatedText[0]['text']
        
        
        e['id2'] = translatedText
        
    return video_list['items']