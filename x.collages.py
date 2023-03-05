from PIL import Image
import math

def create_collage(images, collage_width=1000):
    # Calcula el número de filas y columnas necesarias
    num_images = len(images)
    rows = math.ceil(math.sqrt(num_images))
    cols = math.ceil(num_images / rows)
    
    # Calcula el tamaño de cada miniatura
    thumbnail_size = (200, 200)
    
    # Crea un collage en blanco
    collage_height = rows * thumbnail_size[1]
    collage = Image.new('RGB', (collage_width, collage_height))
    
    # Itera sobre las imágenes, redimensiona y pega cada una en el collage
    for i, image in enumerate(images):
        # Abre la imagen y la redimensiona a la miniatura
        img = Image.open(image)
        img.thumbnail(thumbnail_size)
        
        # Calcula la posición de la miniatura en el collage
        row = i // cols
        col = i % cols
        x = col * thumbnail_size[0]
        y = row * thumbnail_size[1]
        
        # Pega la miniatura en el collage
        collage.paste(img, (x, y))
    
    # Guarda el collage
    collage.save('collage.jpg')

import os

# Carpeta donde se encuentran las imágenes
folder_path = r'C:\Users\Mauri\OneDrive\Documentos\ml_proyects'

# Lista de extensiones de archivo de imagen
image_extensions = ('.png', '.jpg', '.jpeg')

# Lee la lista de archivos en la carpeta y filtra solo los archivos de imagen
image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(image_extensions)]

# Imprime la ruta de archivo de cada imagen
for image_file in image_files:
    print(image_file)

create_collage(image_files)
#images = ['imagen1.jpg', 'imagen2.jpg', 'imagen3.jpg', 'imagen4.jpg']
#create_collage(images)