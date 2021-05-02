import pytube


def main():
    url = input("Insira a url do Vídeo: ")
    yt = pytube.YouTube(url)
    print(f"Titulo do Vídeo: {yt.title}")
    stream = yt.streams.get_highest_resolution()
    print("BAIXANDO VIDEO...")
    stream.download()
    print("Vídeo baixado, confira na sua pasta.")

if __name__ == "__main__":
    main()
