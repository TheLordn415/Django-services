from pytube import YouTube
import os

def download_video(url, csrf_token, resolution):
    try:
        path = os.path.join("./main/static/users_files/", str(csrf_token))
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            print("А ви хто такі?")
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution).first().download(path)
        os.rename(video, path + "/" + "video.mp4")
        return 1, f"Відео {video.split('/')[-1]} завантажено успішно!", 0
    except Exception as e:
        return 0, "Сталася помилка при завантаженні відео:", str(e)

def download_video_and_convert_to_mp3(url, csrf_token):
    try:
        path = os.path.join("./main/static/users_files/", str(csrf_token))
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            print("А ви хто такі?")
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first().download(path)
        os.rename(audio, path + "/" + "audio.mp3")
        return 1, f"Відео {audio.split('/')[-1]} завантажено успішно!", 0
    except Exception as e:
        return 0, "Сталася помилка при завантаженні відео:", str(e)

def test(url, output_path, resolution):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution).first().download(output_path)
        os.rename(video, output_path + "/" + "video.mp4")
        return 1, f"Відео {video.split('/')[-1]} завантажено успішно!", 0
    except Exception as e:
        return 0, "Сталася помилка при завантаженні відео:", str(e)
def main():
    videoList = ["https://www.youtube.com/watch?v=ojyHBbNCZtg",
                 ]
    output_path = "D:/PythonTestScripts/tempfiles/"

    print(test(videoList[0], output_path, '480p'))

    #list = ["2","3","4"]
    #print(list[-4])

if __name__ == "__main__":
    main()