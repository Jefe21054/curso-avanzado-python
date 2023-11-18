from PIL import Image
import os

def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_path_name,file_extension = os.path.splitext(image_folder + file)
            print('comprimiendo archivo ' + file_path_name + file_extension)
            
            if file_extension == '.jpg':
                file_compressed = Image.open(image_folder + file)
                splitted_name_vector = file_path_name.split('/')
                file_name = splitted_name_vector[2]
                file_compressed.save(image_folder + 'COMPRESAS/' + file_name + 
                                    '_compreso.jpg', 
                                    optimize=True,
                                    quality=70)
    except FileNotFoundError:
        print('No se pudo comprimir la imagen')

if __name__ == '__main__':
    compress_images('D:/WALLPAPERS/')
