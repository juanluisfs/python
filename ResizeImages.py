import cv2
import os

def redimensionar_imagenes(carpetas, nuevo_tamano=(64, 64), carpeta_destino="imagenes_redimensionadas"):
    for carpeta in carpetas:
        if not os.path.exists(carpeta):
            print(f"La carpeta '{carpeta}' no existe.")
            continue

        carpeta_destino_actual = os.path.join(carpeta_destino, os.path.basename(carpeta))
        os.makedirs(carpeta_destino_actual, exist_ok=True)

        for archivo in os.listdir(carpeta):
            ruta_completa = os.path.join(carpeta, archivo)

            if os.path.isfile(ruta_completa):
                try:
                    imagen = cv2.imread(ruta_completa)
                    imagen_redimensionada = cv2.resize(imagen, nuevo_tamano)
                    
                    ruta_destino = os.path.join(carpeta_destino_actual, archivo)
                    cv2.imwrite(ruta_destino, imagen_redimensionada)
                    
                    print(f"Imagen redimensionada: {ruta_destino}")
                except Exception as e:
                    print(f"Error al procesar la imagen {ruta_completa}: {e}")

# Rutas de las carpetas que contienen las imágenes
carpetas_imagenes = ["/Users/juanluis/Downloads/K"]

# Redimensionar las imágenes en las carpetas especificadas y guardarlas en una nueva carpeta
redimensionar_imagenes(carpetas_imagenes)
