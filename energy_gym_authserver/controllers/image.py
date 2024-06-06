import os
from PIL import Image
from uuid import uuid4
from pathlib import Path


class ImgController:

    def __init__(self, folder: str = 'media'):
        self.folder = self.ensure_directory(folder)


    @staticmethod
    def ensure_directory(dir: str) -> str:
        Path(dir).mkdir(parents=True, exist_ok=True)
        return dir


    def save(self, image: Image.Image) -> str:
        img_name = str(uuid4()) + '.' + image.format
        self.resize(image, 400).save( os.path.join(self.folder, img_name), image.format, quality=90, optimize=True, progressive=True )
        # image.save( os.path.join(self.folder, img_name), image.format, quality=90, optimize=True, progressive=True )
        return img_name


    def retreive_path(self):
        return self.folder
    
    
    def delete(self, image_name: str):
        path_to_image = os.path.join(self.folder, image_name)
        if os.path.exists( path_to_image ):
            os.remove(path_to_image)


    @staticmethod
    def resize(image: Image.Image, final_width: int) -> Image.Image:
        resize_factor = (final_width / float(image.width))
        final_height = int((float(image.height) * float(resize_factor)))

        return image.resize((final_width, final_height))
