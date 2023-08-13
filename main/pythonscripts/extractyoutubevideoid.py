def extract_video_id(url):
    video_id = None

    if "youtube.com" in url or "youtu.be" in url:
        if "youtube.com/watch?v=" in url:
            video_id = url.split("youtube.com/watch?v=")[1]
            if "&" in video_id:
                video_id = video_id.split("&")[0]
        if "youtu.be/" in url:
            video_id = url.split("youtu.be/")[1]
            if "&" in video_id:
                video_id = video_id.split("&")[0]
    return video_id

def main():
    urls = [
        "https://www.youtube.com/watch?v=-EW-Jdwk_UY&list=PLchdDss3xGtiKnGnOQQ2BaukmTYVdtG57",
        "https://youtu.be/-EW-Jdwk_UY&list=PLchdDss3xGtiKnGnOQQ2BaukmTYVdtG57",
        "https://www.youtube.com/watch?v=-EW-Jdwk_UY",
        "https://www.youtube.com/watch?v=-EW-Jdwk_UY&feature=related"
    ]

    for url in urls:
        video_id = extract_video_id(url)
        if video_id:
            print(video_id)
        else:
            print("Посилання YouTube недійсне")

if __name__ == "__main__":
    main()