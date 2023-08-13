import instaloader, os

def download_media(post_url, output_path):
    # Створити об'єкт Instaloader
    loader = instaloader.Instaloader()

    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        # Завантажити пост за посиланням
        post = instaloader.Post.from_shortcode(loader.context, post_url.split("/")[-2])

        # Отримати інформацію про автора
        author = post.owner_profile.username
        print("Автор поста:", author)

        # Завантажити зображення автора
        profile_pic = post.owner_profile.profile_pic_url
        loader.download_pic(f"{output_path}post_author_avatar", profile_pic, post.date_utc)
        print("Завантаження зображення автора завершено!")

        # Завантажити зображення або відео поста
        if post.is_video:
            loader.download_post(post, author)
            print("Завантаження відео завершено!")
        else:
            loader.download_pic(f"{output_path}post_picture", post.url, post.date_utc)
            print("Завантаження зображення поста завершено!")

        # Вивести опис до посту
        caption = post.caption
        print("Опис до посту:", caption)

        print("Завантаження завершено!")
    except Exception as e:
        print("Сталася помилка під час завантаження:", str(e))

def main():
    post_url = "https://www.instagram.com/p/CtcRRKirGLC/"
    download_media(post_url, "./main/temp_files/")

if __name__ == "__main__":
    main()