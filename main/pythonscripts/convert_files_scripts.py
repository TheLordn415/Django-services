import pdf2docx, docx2pdf, PyPDF2, moviepy.editor
from PIL import Image as ConvertImage
def convert_pdf_to_docx(pdf_path, docx_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)

    docx_converter = pdf2docx.Converter(pdf_path)
    docx_converter.convert(docx_path, start=0, end=len(pdf_reader.pages))
    docx_converter.close()

    print(f'Конвертація завершена. Результат збережено у файлі: {docx_path}.')

def convert_docx_to_pdf(docx_path, pdf_path):
    docx2pdf.convert(docx_path, pdf_path)

    print(f"Файл {docx_path.split('/')[-1]} успішно конвертовано у {pdf_path.split('/')[-1]}.")

def convert_jpg_to_png(jpg_path, png_path):
    image = ConvertImage.open(jpg_path)
    image.save(png_path, "PNG")
    print(f"Файл {jpg_path} успішно конвертовано у {png_path}")

def convert_jpg_to_webp(jpg_path, webp_path):
    image = ConvertImage.open(jpg_path)
    image.save(webp_path, "WEBP")
    print(f"Файл {jpg_path} успішно конвертовано у {webp_path}")

def convert_png_to_jpg(png_path, jpg_path):
    image = ConvertImage.open(png_path)
    image.save(jpg_path, "JPEG")
    print(f"Файл {png_path} успішно конвертовано у {jpg_path}")

def convert_png_to_webp(png_path, webp_path):
    image = ConvertImage.open(png_path)
    image.save(webp_path, "WEBP")
    print(f"Файл {png_path} успішно конвертовано у {webp_path}")

def convert_webp_to_jpg(webp_path, jpg_path):
    image = ConvertImage.open(webp_path)
    image.save(jpg_path, "JPEG")
    print(f"Файл {webp_path} успішно конвертовано у {jpg_path}")

def convert_webp_to_png(webp_path, png_path):
    image = ConvertImage.open(webp_path)
    image.save(png_path, "PNG")
    print(f"Файл {webp_path} успішно конвертовано у {png_path}")

def convert_mp4_to_mp3(mp4_path, mp3_path):
    video = moviepy.editor.VideoFileClip(mp4_path)
    audio = video.audio
    audio.write_audiofile(mp3_path)
    print(f"Файл {mp4_path} успішно конвертовано у {mp3_path}")

def main():
    input_path = "D:/documents/Downloads/video_2023-06-11_21-38-42.mp4"
    output_path = "D:/documents/Downloads/audio.mp3"

    # Конвертуємо
    convert_mp4_to_mp3(input_path, output_path)

if __name__ == "__main__":
    main()
