from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# https://fonts.google.com/specimen/Roboto

def obtener_imagen(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.mode)
        print(image.format)
        
        # image_blackwhite = image.convert('L')
        # image_blackwhite.show()
        # image_blackwhite.save('linux_bw.jpg')
        
        font = ImageFont.truetype('fonts/Roboto-Bold.ttf',120)
        draw = ImageDraw.Draw(image)
        draw.text(
            (20,0),
            "LINUX TUX",
            255,
            font
        )
        image.show()
        image.save('linux_bw_text.jpg')
        
        # Crear Thumbnail
        image.thumbnail((100,100))
        image.show()
        image.save('linux_bw_thumbnail.jpg')
    except (FileNotFoundError, KeyboardInterrupt):
        print('No se encontro la imagen')

if __name__ == '__main__':
    obtener_imagen('linux_bw.jpg')
