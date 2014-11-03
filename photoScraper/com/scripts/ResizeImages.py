from com.utils.GeneralUtils import Utils
import os

__author__ = 'baruchih'

'''
    Script to resize all files
    input: base_path
    file_ending: filter for images to resize
    save path: output folder
    width and height are the desired size
'''

base_path = 'D:/Python/Images_New/'
file_ending = '_rect.png'
save_path = 'D:/Python/ResizedImages'
width = 32
height = 32

counter = 0
for file in os.listdir(base_path):
    if file.endswith(file_ending):
        try:
            image_file = base_path + "/" + file
            Utils.resize_image(image_file, width, height, save_path)
            print '(' + str(counter) + ') Resizing ' + file
        except:
            print '(' + str(counter) + ')Error in file - ' + file
        counter += 1


