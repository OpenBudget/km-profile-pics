from __builtin__ import staticmethod
import cv2
import os
import urllib

__author__ = 'baruchih'


class Utils:

    # gets json as dict and return a csv by keys
    @staticmethod
    def json_to_csv(json_data, return_keys=False):
        keys = json_data.keys()
        line = ''
        key_line = ''
        for i in range(0, len(keys)-1):
            if isinstance(json_data[keys[i]], dict):
                temp = Utils.json_to_csv(json_data[keys[i]], return_keys)
                if return_keys:
                    line += temp[u'line'] + ','
                    key_line += temp[u'keys'] + ','
                else:
                    line += temp
            else:
                line += unicode(json_data[keys[i]]).encode('utf8') + ','
                key_line += keys[i].encode('utf8') + ','

        if isinstance(json_data[keys[len(keys)-1]], dict):
            temp = Utils.json_to_csv(json_data[keys[len(keys)-1]], return_keys)
            if return_keys:
                line += temp[u'line']
                key_line += temp[u'keys']
            else:
                line += temp
        else:
            line += unicode(json_data[keys[len(keys)-1]]).encode('utf8') + '\n'
            key_line += keys[len(keys)-1].encode('utf8') + '\n'

        if return_keys:
            res = dict()
            res[u'line'] = line
            res[u'keys'] = key_line
            return res
        else:
            return line

    # resizes image by width/height and saves it in path_folder
    @staticmethod
    def resize_image(image_file, width, height, path_folder):

        # get pic_name and path
        pic_name = os.path.basename(image_file)
        extension = pic_name[pic_name.find('.'): len(pic_name)]
        output_file = path_folder + u'\\' + pic_name.replace(extension, '') + '_w' + str(width) + '_h' + str(height) + extension

        # Read the image
        image = cv2.imread(image_file)

        resized_image = cv2.resize(image, (width, height))
        cv2.imwrite(output_file, resized_image)

    # receives an image file and returns it as data uri
    @staticmethod
    def image_to_data_uri(image_file):
        encoded = urllib.quote(open(image_file, "rb").read().encode("base64"))
        return encoded

    # retrieve an image name out of a url
    @staticmethod
    def get_image_name(url):
        index = url.find('/')
        while index != -1:
            url = url[index + 1:len(url)]
            index = url.find('/')
        return url