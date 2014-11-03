import urllib2
from com.utils.GeneralUtils import Utils

__author__ = 'baruchih'


class PhotoScraper:

    def __init__(self):
        print 'photo_scraper init'

    # gets an image out of the url, saves it into save_folder
    # status = 1 success
    # status = -1 failure
    # save_folder is the folder which the image will be saved
    @staticmethod
    def scrap_photo(url, save_folder):
        if isinstance(url, unicode):
            url = unicode(url)
        pic_name = ''
        try:
            pic_name = Utils.get_image_name(url)
            pic_path = save_folder + u'\\' + pic_name
            # retrieve picture
            f = urllib2.urlopen(url)
            data = f.read()
            with open(pic_path, "wb") as pic:
                pic.write(data)
            res = {u'url': url, u'name': pic_name, u'saved_at': pic_path, u'status': 1}
        except:
            print 'PhotoScraper.scrap_photo error'
            res = {u'url': url, u'name': pic_name, u'saved_at': '', u'status': -1}
        return res