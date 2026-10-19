import os

ruta = "Gano-Cat-Breeds-V1_1"

print("Ruta que estoy buscando:", os.path.abspath(ruta))
print("¿Existe?:", os.path.exists(ruta))

extensiones = (".jpg", ".jpeg", ".png")

for carpeta, subcarpetas, archivos in os.walk(ruta):
    imagenes = [
        archivo
        for archivo in archivos
        if archivo.lower().endswith(extensiones)
    ]

    if imagenes:
        print(os.path.basename(carpeta), ":", len(imagenes))