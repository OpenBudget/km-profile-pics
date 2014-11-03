from com.facedetector import Detector
from com.photoscraper.PhotoScraper import PhotoScraper
from com.utils.GeneralUtils import Utils
import time
import json

__author__ = 'baruchih'

'''
    General script to retrieve images from url's, detect faces and save it in save_folder
    input json has 2 keys:
    {
        img: "the image url",
        name: "the member name (in unicode)"
    }
'''

save_folder = 'D:/Python/Images_New/'
outCSV = 'D:/Python/Images_New/data.csv'
outJSON = 'D:/Python/Images_New/data.json'
inputFileName = 'D:/Python/Images_New/pics_new.json'
face_cascade = 'D:/Python/Scripts/Faces/haarcascade_frontalface_default.xml'

# initiate face detector
face_detector = Detector.Detector(face_cascade)
writer_csv = open(outCSV, 'w')
writer_json = open(outJSON, 'w')
wrote_keys = False


def scrap_and_detect(p, count, wrote_keys):
    # scrap image
    try:
        scrap_result = PhotoScraper.scrap_photo(p['img'], save_folder)
    except:
        print "ERR " + str(count)
        time.sleep(2)
        scrap_and_detect(p, count)

    res = p
    if scrap_result[u'status'] == 1:
        # detect faces
        res[u'face'] = face_detector.get_face(scrap_result[u'saved_at'], True, False, 0.4)
        if res != None:
            res[u'name'] = p[u'name']
            res[u'status'] = 1
        else:
            res[u'status'] = -1
        pics_data.append(res)
        if not wrote_keys:
            temp = Utils.json_to_csv(res, True)
            writer_csv.write(temp[u'keys'])
            writer_csv.write(temp[u'line'])
            wrote_keys = True
        else:
            writer_csv.write(Utils.json_to_csv(res))
    return wrote_keys

inputFile = open(inputFileName)
pics = json.load(inputFile)
pics_data = []
count = 0
for p in pics:
    if isinstance(p, dict):
        if p.has_key(u'name') and p.has_key(u'img'):
            wrote_keys = scrap_and_detect(p, count, wrote_keys)
    count += 1
    #if count == 5:
    #    break
    print count

json.dump(pics_data, writer_json)
writer_json.close()
writer_csv.close()
