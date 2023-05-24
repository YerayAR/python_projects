import os
from moviepy.editor import VideoFileClip

def extraer_audio(ruta_videos, ruta_musica):
    # Verificar si las rutas proporcionadas existen
    if not os.path.exists(ruta_videos):
        print(f"La ruta de los videos proporcionada {ruta_videos} no existe.")
        return
    if not os.path.exists(ruta_musica):
        print(f"La ruta de la carpeta de musica proporcionada {ruta_musica} no existe.")
        return

    # Recorrer todos los archivos en la ruta de videos
    for archivo in os.listdir(ruta_videos):
        if archivo.endswith('.mp4'):  # Asegurate de ajustar esto a los formatos de video que tengas
            ruta_completa = os.path.join(ruta_videos, archivo)
            # Crear un VideoFileClip para cada archivo de video
            clip = VideoFileClip(ruta_completa)
            # Extraer el audio
            audio = clip.audio
            # Crear una ruta para el nuevo archivo de audio
            nombre_audio = os.path.splitext(archivo)[0] + '.mp3'  # cambiar a '.wav' si prefieres ese formato
            ruta_audio = os.path.join(ruta_musica, nombre_audio)
            # Guardar el archivo de audio
            audio.write_audiofile(ruta_audio)

# Usar la función
extraer_audio('path1', 'path2')