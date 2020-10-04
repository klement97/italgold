import os

from kral_kutu_backend.settings import BASE_DIR

folder_dir = os.path.join(BASE_DIR, 'KRAL_KUTU/TABLALAR')
media_folder = os.path.join(BASE_DIR, 'media/products')
image_paths = os.listdir(folder_dir)
image_paths = [image.replace(' ', '') for image in image_paths]

for image_path in image_paths:
    with open(folder_dir + image_path) as img:

