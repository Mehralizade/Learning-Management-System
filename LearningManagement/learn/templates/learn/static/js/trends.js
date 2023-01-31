$(document).ready(function(){

    var API_KEY ="AIzaSyC2i5kzHio67jG0c5hUEEhtco9tkPSXDG0"
    
    var video = ""
    
    
    $("#form").submit(function(event){
        event.preventDefault()
        alert("form is submitted")
    
    
        
        var search = $("#search").val()
    
        videoSearch(API_KEY,search,4)
    
    })
    
    function videoSearch(key,search,maxResults) {
        $("#videos").empty()
    
        $.get("https://www.googleapis.com/youtube/v3/search?key="+ key
         + "&type=video&part=snippet&maxResults=" + maxResults + "&q=" + search,function(data){
             console.log(data)
             data.items.forEach(item => {
                 
                var aga =  $("#search").val()
                
                    video=`
                <iframe width="420" height="315"  
                    src="http://www.youtube.com/embed/${item.id.videoId}" frameborder="0" allowfullscreen></iframe>` 
    
                $("#videos").append(video)
                
             });
               
    
    
         }) 
        
    
        
     
    
    }
    
    })
        