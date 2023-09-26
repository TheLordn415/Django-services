from django.shortcuts import render
from .models import *
from .pythonscripts import downloadyoutubevideo, extractyoutubevideoid, convert_files_scripts
import re, os

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

def ConvertFiles(request):
    if request.method == "POST":
        print(request.POST)
        file = request.FILES['fileInput']
        csrf_token = request.POST.get('csrfmiddlewaretoken')
        file_extenstion_output = request.POST.get('extenstionOutput')
        if not file_extenstion_output:
            data = {'error': "You did not choose the output extenstion!"}
            return render(request, 'main/convertfiles.html', data)
        str_file = str(file)
        file_input_extension = str_file.split('.')[-1]
        path_from = f"main/temp_files/{str_file}"
        path_to = f"main/static/users_files/{csrf_token}/input.{file_input_extension}"
        doc = InputFile.objects.create(file=file)
        doc.save()
        if not os.path.exists(f"main/static/users_files/{csrf_token}"):
            os.mkdir(f"main/static/users_files/{csrf_token}")
        try:
            os.rename(path_from, path_to)
        except FileNotFoundError:
            data = {'error': "Your file has illegal symbols or else. Please, rename your file. Example: input!"}
            return render(request, 'main/convertfiles.html', data)
        except FileExistsError:
            os.remove(path_to)
            os.rename(path_from, path_to)
            #continue

        #CODE Here
        '''
        elif file_input_extension == '' and file_extenstion_output == '':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
                    }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_<>_to_<>(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        '''
        if file_input_extension == 'pdf' and file_extenstion_output == 'docx':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
                    }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_pdf_to_docx(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        elif file_input_extension == 'docx' and file_extenstion_output == 'pdf':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
                    }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_docx_to_pdf(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        elif file_input_extension == 'jpg' and file_extenstion_output == 'png':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
            }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_jpg_to_png(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        elif file_input_extension == 'jpg' and file_extenstion_output == 'webp':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
            }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_jpg_to_webp(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        elif file_input_extension == 'png' and file_extenstion_output == 'jpg':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
            }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_png_to_jpg(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        elif file_input_extension == 'png' and file_extenstion_output == 'webp':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
            }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_png_to_webp(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        elif file_input_extension == 'webp' and file_extenstion_output == 'png':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
            }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_webp_to_png(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        elif file_input_extension == 'webp' and file_extenstion_output == 'jpg':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}',
                'file_format': f'output.{file_extenstion_output}'
            }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/output.{file_extenstion_output}'
            convert_files_scripts.convert_webp_to_jpg(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)
        elif file_input_extension == 'mp4' and file_extenstion_output == 'mp3':
            data = {
                'output_path_file': f'main/static/users_files/{csrf_token}/audio.{file_extenstion_output}',
                'file_format': f'audio.{file_extenstion_output}'
            }
            path_file_input = path_to
            path_file_output = f'main/static/users_files/{csrf_token}/audio.{file_extenstion_output}'
            convert_files_scripts.convert_mp4_to_mp3(path_file_input, path_file_output)
            return render(request, 'main/convertfiles.html', data)

    return render(request, 'main/convertfiles.html')