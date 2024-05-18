## Aplicacion en Python con GUI
### para descargar usar la aplicacion necesitas la libreria pyinstaller y ffmpeg
### accede primero al siguiente enlace para poder descargar la libreria de ffmpeg
https://github.com/BtbN/FFmpeg-Builds/releases
### luego te rediriges a ffmpeg-master-latest-win64-gpl.zip y lo extraes
### dentro de la carpeta /bin encontraras un archivo llamado ffmpeg
### lo copias o cortas y creas una nueva carpeta en tu disco local (C:) y lo pegas dentro
### luego la ruta del archivo lo copias a las variables de entorno
------------------------------------------------
### para instalar pypyinstaller
```bash
pip3 install pyinstaller
```

### usa el siguiente comando con pyinstaller para crear el exe
```bash
pyinstaller --onefile --windowed --add-data "<ruta_de_ffmpeg>;" descargarYT.py
```
