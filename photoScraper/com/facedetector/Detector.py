import cv2
import os
import math
import numpy as np

__author__ = 'baruchih'


class Detector:

    # Constructor must accept the face cascade
    def __init__(self, cascade_file):
        self.face_cascade = cv2.CascadeClassifier(cascade_file)

    # will return a json:
    # {
    #   rect: {
    #           rect_x: "x value of the bottom left corner of the face rectangle",
    #           rect_y: "y value of the bottom left corner of the face rectangle",
    #           rect_h: "height of the face rectangle",
    #           rect_w: "width of the face rectangle",
    #           saved_at: "save location of the rectangle face (if save_as_rect=True)"
    #         },
    #   circle: {
    #               circle_radius: "radius of the circular face",
    #               circle_center: {
    #                                   circle_center_x: "x value of the center of the circular face"
    #                                   circle_center_y: "y value of the center of the circular face"
    #                              },
    #               saved_at: "save location of the circular face (if save_as_circle=True)"
    #           },
    # }
    #
    # increase_range will enlarge the detected face area by *increase_range area (should be 0<= increase_range <= 1)
    def get_face(self, image_file, save_as_rect=False, save_as_circle=False, increase_range=0):

        # get pic_name and path
        pic_name = os.path.basename(image_file)
        save_path = os.path.realpath(image_file).replace(pic_name, '')
        extension = pic_name[pic_name.find('.'): len(pic_name)]

        # Read the image
        image = cv2.imread(image_file)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # create output and save pics if save = True
        if len(faces) > 0:

            # choose the last face
            '''
            face = faces[0]
            for k in range(1, len(faces)):
                f = faces[k]
                if f[2] > face[2] and f[3] > face[3]:
                    face = f
            '''
            face = faces[len(faces) - 1]

            x = face[0]
            y = face[1]
            h = face[2]
            w = face[3]

            # increase range if requested
            if increase_range > 0:
                h += int(h*increase_range)
                w += int(w*increase_range)
                x -= int(w*increase_range/2)
                if x < 0:
                    x = 0
                y -= int(h*increase_range/2)
                if y < 0:
                    y = 0

            res = dict()
            res[u'rect'] = {u'rect_x': x, u'rect_y': y, u'rect_h': h, u'rect_w': w}
            res[u'circle'] = {u'circle_radius': int(h/2), u'circle_center': {u'circle_center_x': x + int(w/2), u'circle_center_y': int(h/2)}}

            # save images
            if save_as_rect:
                #rectangle image
                rect_img = image[y:y+h, x:x+w]
                rect_img_file = save_path + u'\\' + pic_name.replace(extension, '') + '_rect.png'
                cv2.imwrite(rect_img_file, rect_img)
                res[u'rect'][u'saved_at'] = rect_img_file

            if save_as_circle:
                #circle image
                circle_img = np.zeros((h, w, 4), dtype=np.uint8)
                for r in range(1, h):
                    for c in range(1, w):
                        rad = math.sqrt((r-h/2)**2 + (c-w/2)**2)
                        if rad <= h/2:
                            circle_img[r, c][0] = rect_img[r, c][0]
                            circle_img[r, c][1] = rect_img[r, c][1]
                            circle_img[r, c][2] = rect_img[r, c][2]
                            circle_img[r, c][3] = 255
                circle_img_file = save_path + u'\\' + pic_name.replace(extension, '') + '_circle.png'
                cv2.imwrite(circle_img_file, circle_img)
                res[u'circle'][u'saved_at'] = circle_img_file
            return res
        else:
            return None


