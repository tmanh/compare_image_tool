import os
import cv2


def produce_crop_images(data_folder, list_files, loc_x, loc_y, height, width):
    for f in list_files:
        path = os.path.join(data_folder, f)
        image = cv2.imread(path)
        crop = image[loc_y:loc_y + height, loc_x:loc_x + width, :]
        cv2.imwrite(os.path.join(data_folder, 'crop_' + f), crop)
