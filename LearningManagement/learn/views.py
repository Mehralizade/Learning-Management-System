from django.shortcuts import render
import requests
import wikipedia
import string
from youtube_transcript_api import YouTubeTranscriptApi


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