import json
from com.utils.GeneralUtils import Utils
import os

__author__ = 'baruchih'

'''
    General script to retrieve images from url's, detect faces and save it in save_folder
    input json has 2 keys:
    {
        img: "the image url",
        name: "the member name (in unicode)"
    }
    images_folder is the folder that contains all the .png to resize
    outFile is the output json, 2 keys:
    {
        data_uri: "the data uri of the resized image"
        name: "the member name (in unicode)"
    }
'''

inputJson = 'D:/Python/Images_New/pics_new.json'
images_folder = 'D:/Python/ResizedImages'
outFile = 'D:/Python/ResizedImages/dataURI.json'

writer_json = open(outFile, 'w')

images = dict()
counter = 0
for file in os.listdir(images_folder):
    if file.endswith('.png'):
        index = file.index('_rect')
        name = file[0:index]
        images[name] = images_folder + '/' + file

print len(images)

inputFile = open(inputJson)
pics = json.load(inputFile)
pics_data = []
count = 0
for p in pics:
    if isinstance(p, dict):
        if p.has_key(u'name') and p.has_key(u'img'):
            picName = Utils.get_image_name(p[u'img']).replace('.jpg', '')
            if images.has_key(picName):
                res = dict()
                res[u'name'] = p[u'name']
                res[u'data_uri'] = Utils.image_to_data_uri(images[picName])
                pics_data.append(res)

print len(pics_data)
json.dump(pics_data, writer_json)
writer_json.close()