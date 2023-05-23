from pickletools import optimize
from PIL import Image
import os

path = 'C:/Users/yera2/VScodePython/NuevaCarpeta/'

if __name__ == '__main__':
    count = 1
    for filename in os.listdir(path):
        name, extension = os.path.splitext(path + filename)
        if extension == '.jpg':
            picture = Image.open(path + filename)
            os.rename(path + filename, path + 'image - No ' + str(count) + '.jpg')
            count =+ 1
    
            