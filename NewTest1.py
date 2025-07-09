from PIL import Image, ImageEnhance
from PIL import ImageFilter

with Image.open('Placeholder.png') as pic_original:
    print('Image is open\nSize:', pic_original.size)
    print('Format:', pic_original.format)
    print('Type:', pic_original.mode) #цветное
    pic_original.show()
 
    pic_gray = pic_original.convert('L')    
    pic_gray.save('gray.jpg')
    print('Image is created\nSize:', pic_gray.size)
    print('Format:', pic_gray.format)
    print('Type:', pic_gray.mode) #чб
    pic_gray.show()
 
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.show()
 
    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.show()
#bonus 1. Mirror reflection
    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.show()
 
    #bonus 2. Contrast enhancing
    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.show()