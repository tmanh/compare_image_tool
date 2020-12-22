from utils import produce_crop_images


loc_x, loc_y, height, width = 300, 300, 300, 300

data_folder = '/Users/anhtruong/Workspace/publication/iet-image-processing-2020/figures'
list_files = ['origin.png', '1.5.png', '2.0.png', '2.5.png', '3.0.png', '3.5.png', '4.0.png']


produce_crop_images(data_folder, list_files, loc_x, loc_y, height, width)
