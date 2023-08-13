from django.shortcuts import render
from .pythonscripts import downloadyoutubevideo, extractyoutubevideoid
import re

#from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'General page',
        'values': [],
    }
    return  render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def DownloadYoutubeVideo(request):
    if request.method == "POST":
        data = dict()
        print(request.POST)
        video_url = request.POST.get('video_url')
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        resolution = request.POST.get('resolution')
        if resolution == "mp3":
            response = list(downloadyoutubevideo.download_video_and_convert_to_mp3(video_url, csrf_token))
        else:
            response = list(downloadyoutubevideo.download_video(video_url, csrf_token, resolution))
        print(response[0], response[1], response[2])
        if not response[0]:
            return render(request, 'main/DownloadYoutubeVideo.html', {"error": "Something went wrong. Check correctness your url or choose another resolution."})
        video_id = extractyoutubevideoid.extract_video_id(video_url)
        data["video_url"] = video_url
        data["video_image_url"] = f"https://img.youtube.com/vi/{video_id}/0.jpg"
        if resolution == "mp3":
            data["output_path_file"] = f"{csrf_token}/audio.mp3"
            data["file_format"] = "audio.mp3"
        else:
            data["output_path_file"] = f"{csrf_token}/video.mp4"
            data["file_format"] = "video.mp4"
        return render(request, 'main/DownloadYoutubeVideo.html', data)
    return render(request, 'main/DownloadYoutubeVideo.html')

def downloadmediainstagram(request):
    if request.method == "POST":
        data = {}
        print(request.POST)
    return render(request, 'main/downloadinstagrammedia.html')

def convertfiles(request):
    return render(request, 'main/convertfiles.html')