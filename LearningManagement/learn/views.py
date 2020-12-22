from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
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
        technologyName = request.POST['techName']
        sentenceNumber = request.POST['sentenceNumber']
        language = request.POST['language']
        wikipedia.set_lang(language.lower()[:2])
        response = wikipedia.page(technologyName).url
        
        string = 'http://api.meaningcloud.com/summarization-1.0?key=7341fb6a1d0dbba65050847d3b9054b1&sentences='
        string = string +sentenceNumber
        string = string + "&url="
        string = string + response
        information = requests.get(string)
        movieInfo = information.json()
        string = 'https://www.googleapis.com/books/v1/volumes?q=' # api endpoint url
        # string = 'https://youtube.googleapis.com/youtube/v3/captions/f2Y1U8UhWog9F3-CWmWX_4Arl0HehWEiVewOopK_I38%3D?key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0'
        string = string + technologyName # modifying api endpoint url to include the name of the chosen movie in the html form
        
        # string = string +  "&key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0"
        movieInfo2 = requests.get(string) # getting data from api
        movieInfo2 = movieInfo2.json()
        

        return render(request, 'learn/home.html', {
        
            'title': movieInfo['summary'],
            'movieInfo': movieInfo2['items']
            #'info':movieInfo['Plot']
        })
    else:
        return render(request, 'learn/home.html', {
            
           # 'title': movieInfo['summary'],
            #'info':movieInfo['Plot']
        })
def home2(request):
     if request.method == 'POST':
        videoUrl = request.POST['videoUrl']
        video_id = videoUrl.split('?')[1][2:]
        sentenceNumber = request.POST['sentenceNumber']
        Language = request.POST['language']
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ''
        d=0
        for i in range(len(transcript)//6):
            d = d+1
            
            text= text + transcript[i]['text']
            if d==6:
                d=0
                text = text +  '. '
        
        url_for_translation = 'https://api.deepl.com/v2/translate?auth_key=1169a1dc-f264-c753-0772-f6f97e808be9&text=' + text + '&target_lang='+Language.lower()[:2]
        r = requests.post(url_for_translation)
        translatedText = r.json()
        translatedText = translatedText['translations']
 
        translatedText = translatedText[0]['text']
        #lets find the definition of word incredible
        url_for_words = "https://wordsapiv1.p.rapidapi.com/words/incredible/definitions"

        headers = {
            'x-rapidapi-key': "884e268161msh1031990822f1d26p1373cdjsne6d04f63ae56",
            'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
            }

        response_word = requests.request("GET", url_for_words, headers=headers)

        print(response_word.text)

        string = 'http://api.meaningcloud.com/summarization-1.0?key=7341fb6a1d0dbba65050847d3b9054b1&sentences='
        string = string +sentenceNumber
        string = string + "&txt="
        string = string + text
        information = requests.get(string)
        movieInfo = information.json()
        
        return render(request, 'learn/home2.html', {
        
            #'title': string,
            'text': movieInfo['summary'],
            'translation':translatedText, 
            #'info':movieInfo['Plot']
        })
     else:
        return render(request, 'learn/home2.html', {
            
           # 'title': movieInfo['summary'],
            #'info':movieInfo['Plot']
        })


#imdb requester
def imdb(request):
    if request.method == 'POST': #checking whether something is posted in html template 
        name = request.POST['movieName'] # getting the data from html form -- movieName is the name parameter of the input box where we get the data for the movie name
        string = 'http://www.omdbapi.com/?apikey=4add9297&t=' # api endpoint url
        string = string + name # modifying api endpoint url to include the name of the chosen movie in the html form
        movieInfo = requests.get(string) # getting data from api
        movieInfo = movieInfo.json() 

        # render parameters: request, corresponding html template, values to put in html placeholders in double brackets
        return render(
            request, 'learn/imdb.html', {
                'FilmName':movieInfo['Title'],
                'FilmPlot':movieInfo['Plot']
            }
        )
    
    return render(request, 'learn/imdb.html', {
            
           # 'title': movieInfo['summary'],
            #'info':movieInfo['Plot']
       })

def home3(request):
    if request.method == 'POST': #checking whether something is posted in html template 
        name = request.POST['movieName'] # getting the data from html form -- movieName is the name parameter of the input box where we get the data for the movie name
        string = 'https://youtube.googleapis.com/youtube/v3/search?q=' # api endpoint url
        # string = 'https://youtube.googleapis.com/youtube/v3/captions/f2Y1U8UhWog9F3-CWmWX_4Arl0HehWEiVewOopK_I38%3D?key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0'
        string = string + name # modifying api endpoint url to include the name of the chosen movie in the html form
        
        string = string +  "&key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0"
        movieInfo = requests.get(string) # getting data from api
        movieInfo = movieInfo.json() 
        movieInfo = movieInfo["items"]
        a=[]
        for elem in movieInfo:
            a.append(elem["id"]["videoId"])
        # for elem in a:
        #     elem=elem.strip()
        movieInfo=a

        # render parameters: request, corresponding html template, values to put in html placeholders in double brackets
        return render(
            request, 'learn/home3.html', {
                'FilmName':movieInfo
            }
        )
    
    return render(request, 'learn/home3.html', {
            
           # 'title': movieInfo['summary'],
            #'info':movieInfo['Plot']
       })
def home4(request):
    if request.method == 'POST': #checking whether something is posted in html template 
        name = request.POST['movieName'] # getting the data from html form -- movieName is the name parameter of the input box where we get the data for the movie name
        # string = 'https://youtube.googleapis.com/youtube/v3/search?q=' # api endpoint url
        # string = string + name # modifying api endpoint url to include the name of the chosen movie in the html form
        
        # string = string +  "&key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0"
        string='https://youtube.googleapis.com/youtube/v3/captions/%22f2Y1U8UhWog9F3-CWmWX_4Arl0HehWEiVewOopK_I38%3D%22?key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0'
        movieInfo = requests.get(string) # getting data from api
        movieInfo = movieInfo.json() 

        # render parameters: request, corresponding html template, values to put in html placeholders in double brackets
        return render(
            request, 'learn/home4.html', {
                'FilmName':movieInfo
            }
        )
    
    return render(request, 'learn/home4.html', {
            
           # 'title': movieInfo['summary'],
            #'info':movieInfo['Plot']
       })
def ebooks(request):
    if request.method == 'POST': #checking whether something is posted in html template 
        name = request.POST['movieName'] # getting the data from html form -- movieName is the name parameter of the input box where we get the data for the movie name
        string = 'https://www.googleapis.com/books/v1/volumes?q=' # api endpoint url
        # string = 'https://youtube.googleapis.com/youtube/v3/captions/f2Y1U8UhWog9F3-CWmWX_4Arl0HehWEiVewOopK_I38%3D?key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0'
        string = string + name # modifying api endpoint url to include the name of the chosen movie in the html form
        
        # string = string +  "&key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0"
        movieInfo = requests.get(string) # getting data from api
        movieInfo = movieInfo.json() 
        a=[]
        
        movieInfo = movieInfo['items']
        # [1]['volumeInfo']['averageRating']
        # for elem in movieInfo:
        #     a.append(elem['volumeInfo']['averageRating'])
        # movieInfo=a
        # 3, 4, 3.5, 4.5, 4, 4, 4, 4, 4, 2
        # render parameters: request, corresponding html template, values to put in html placeholders in double brackets
        return render(
            request, 'learn/ebooks.html', {
                'FilmName':movieInfo
            }
        )
    
    return render(request, 'learn/ebooks.html', {
            
           # 'title': movieInfo['summary'],
            #'info':movieInfo['Plot']
       })

@login_required        
def youtubeplay(request):
     if request.method == 'POST':
        search = request.POST['videoSearch']
        
        language = request.POST['language']
        sentenceNumber = request.POST['sentenceNumber']
        print(language, ' ', sentenceNumber)
        string =  "https://www.googleapis.com/youtube/v3/search?key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0&type=video&part=snippet&maxResults=4&q=" + search
        
        information = requests.get(string)

        movieInfo = information.json()
        summaryList = []
        for e in movieInfo['items']:
            
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
            
            string = 'http://api.meaningcloud.com/summarization-1.0?key=7341fb6a1d0dbba65050847d3b9054b1&sentences='+sentenceNumber
            string = string + "&txt="
            string = string + text
            
            information = requests.get(string)
            
            movieInfo2 = information.json()
            
            text =  movieInfo2['summary']
            url_for_translation = 'https://api.deepl.com/v2/translate?auth_key=1169a1dc-f264-c753-0772-f6f97e808be9&text=' + text + '&target_lang='+language.lower()[:2]
            r = requests.post(url_for_translation)
            translatedText = r.json()
            translatedText = translatedText['translations']

            translatedText = translatedText[0]['text']
            #lets find the definition of word incredible
           

            headers = {
                'x-rapidapi-key': "884e268161msh1031990822f1d26p1373cdjsne6d04f63ae56",
                'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
                }

           
            
            e['id2'] = translatedText
            
            
            #print(e)
        return render(request, 'learn/youtubeplay.html', {
            
           # 'title': movieInfo['summary'],
        'info':movieInfo['items'],
        
       })
     return render(request, 'learn/youtubeplay.html', {
            
           
        
       })

@login_required
def trendySkills(request):
    if request.method == 'POST':
        language = request.POST['language']
        sentenceNumber = request.POST['sentenceNumber']
        r = requests.get("https://www.cnbc.com/2019/11/19/these-will-be-the-top-10-most-popular-tech-skills-of-2020.html")
        soup = BeautifulSoup(r.content, 'html.parser')
        
        headings = soup.find_all('h2')
        
        
        searchWord = str(headings[0]).split('1.')[1].split('<')[0] + '5 mins explanation'
        print(searchWord)
        string =  "https://www.googleapis.com/youtube/v3/search?key=AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0&type=video&part=snippet&maxResults=4&q=" + searchWord
        
        information = requests.get(string)

        movieInfo = information.json()
        summaryList = []
        for e in movieInfo['items']:
            
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
            
            string = 'http://api.meaningcloud.com/summarization-1.0?key=7341fb6a1d0dbba65050847d3b9054b1&sentences='+sentenceNumber
            string = string + "&txt="
            string = string + text
            
            information = requests.get(string)
            
            movieInfo2 = information.json()
            
            text =  movieInfo2['summary']
            url_for_translation = 'https://api.deepl.com/v2/translate?auth_key=1169a1dc-f264-c753-0772-f6f97e808be9&text=' + text + '&target_lang='+language.lower()[:2]
            r = requests.post(url_for_translation)
            translatedText = r.json()
            translatedText = translatedText['translations']

            translatedText = translatedText[0]['text']
            #lets find the definition of word incredible
           

            headers = {
                'x-rapidapi-key': "884e268161msh1031990822f1d26p1373cdjsne6d04f63ae56",
                'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
                }

           
            
            e['id2'] = translatedText
            
        return render(request, 'learn/trends.html', {
            
           # 'title': movieInfo['summary'],
        #'info':movieInfo['items'],
        'info':movieInfo['items'],
        
       })
    return render(request, 'learn/trends.html', {
            
           
        
       })