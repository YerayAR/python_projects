from pytube import YouTube

def descargar_video(url):
    print("Descargando...")
    YouTube(url).streams.first().download()
    print("Descarga completa!!")

def descargar_lista_videos():
    while True:
        url = input("Por favor, introduce la URL del video de YouTube que quieres descargar (o 'salir' para finalizar): ")
        if url.lower() == 'salir':
            print("No hay más descargas")
            break
        else:
            descargar_video(url)

descargar_lista_videos()