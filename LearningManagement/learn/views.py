from django.shortcuts import render
import requests
import wikipedia
import string
from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json
import time
# Create your views here.
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
        
        return render(request, 'learn/home.html', {
        
            'title': movieInfo['summary'],
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
 
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ''
        for i in range(len(transcript)//6):

            text= text + transcript[i]['text']
         
            text = text +  ' '
        
        string = 'http://api.meaningcloud.com/summarization-1.0?key=7341fb6a1d0dbba65050847d3b9054b1&sentences='
        string = string +'2'
        string = string + "&txt="
        string = string + text
        information = requests.get(string)
        movieInfo = information.json()
        return render(request, 'learn/home2.html', {
        
            'title': string,
            'text': movieInfo['summary']
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
def youtubeplay(request):
    
    
    return render(request, 'learn/youtubeplay.html', {
            
           # 'title': movieInfo['summary'],
            #'info':movieInfo['Plot']
       })
