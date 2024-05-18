import sys
import os
from moviepy.editor import *
from pytube import YouTube
import tkinter as tk
from tkinter import messagebox

# Ubicación del directorio de logs en AppData del usuario
appdata_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'MiAplicacion', 'Logs')
os.makedirs(appdata_path, exist_ok=True)  # Crea el directorio si no existe

# Redirección de stdout y stderr a archivos de log en la carpeta creada
sys.stdout = open(os.path.join(appdata_path, 'stdout.txt'), 'w')
sys.stderr = open(os.path.join(appdata_path, 'stderr.txt'), 'w')

def limpiar_titulo(titulo):
    return "".join(c for c in titulo if c.isalnum() or c.isspace())

def descargar_audio():
    url = url_entry.get()
    if not url.strip():
        messagebox.showerror("Error", "Por favor, ingresa una URL válida.")
        return
    try:
        video = YouTube(url).streams.filter(only_audio=True).first()
        if video is None:
            raise Exception("No se encontró una pista de audio en el video.")

        titulo_limpio = limpiar_titulo(video.title)
        ruta_descarga = os.path.join(os.path.expanduser('~'), 'Downloads')
        output_file = video.download(output_path=ruta_descarga, filename=titulo_limpio)
        final_audio = os.path.join(ruta_descarga, f"{titulo_limpio}.mp3")

        audio_clip = AudioFileClip(output_file)
        audio_clip.write_audiofile(final_audio)
        audio_clip.close()

        os.remove(output_file)
        messagebox.showinfo("Éxito", "Descarga y conversión completada")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")
    finally:
        url_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Descargador de YouTube")

url_entry = tk.Entry(root, width=60)
url_entry.pack(padx=10, pady=10)

descargar_btn = tk.Button(root, text="Descargar Audio", command=descargar_audio)
descargar_btn.pack(pady=10)

root.mainloop()

# Asegurarse de cerrar los archivos de log al cerrar la aplicación
sys.stdout.close()
sys.stderr.close()
