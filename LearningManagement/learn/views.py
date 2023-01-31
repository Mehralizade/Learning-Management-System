from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .client_api import *
import requests
import wikipedia
import string
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json
import time
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView
from .forms import UserCreateForm
from django.contrib.auth.forms import AuthenticationForm
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
# Create your views here.

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "learn/register.html"
    
@login_required  
def home(request):
    if request.method == 'POST':
        technology_name = request.POST['techName']
        sentence_number = request.POST['sentenceNumber']
        language = request.POST['language']
        url = wikipedia_info(technology_name, language)
        summary_text = summarize_text(url,sentence_number)
        ebook_list = get_ebooks(technology_name)

        return render(request, 'learn/home.html', {
        
            'title': summary_text,
            'ebook_list': ebook_list
           
        })
    else:
        return render(request, 'learn/home.html', {
            
          
        })
def search_video(request):
     if request.method == 'POST':
        video_url = request.POST['videoUrl']
        video_id = video_url.split('?')[1][2:]
        sentence_number = request.POST['sentenceNumber']
        language = request.POST['language']
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = get_text(transcript)
        
        translated_text = translate_text(text,language)
        summary_text = summarize_text(text,sentence_number)

        
        return render(request, 'learn/search_video.html', {
        
          
            'text': summary_text,
            'translation':translated_text, 
           
        })
     else:
        return render(request, 'learn/search_video.html', {
            
           
        })

@login_required
def trendy_skills(request):
    if request.method == 'POST':
        language = request.POST['language']
        sentence_number = request.POST['sentenceNumber']
        search_word = get_trendy_skills()
        video_list = get_video_list(search_word,language,sentence_number)
        
            
        return render(request, 'learn/trends.html', {
            
       
        'info':video_list,
        
       })
    return render(request, 'learn/trends.html', {
            
           
        
       })