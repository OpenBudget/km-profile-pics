from com.utils.GeneralUtils import Utils

__author__ = 'baruchih'


base_path = 'D:/Python/Images_New/'
image_file = ['netanyahu_bibi_rect.png', 'Lapid_Yair_rect.png', 'deri_aryeh_rect.png']
save_path = 'D:/Python/Resized'
width = 240
height = 240

for img in image_file:
    try:
        f = base_path + img
        Utils.resize_image(f, width, height, save_path)
    except:
        print 'Error'







