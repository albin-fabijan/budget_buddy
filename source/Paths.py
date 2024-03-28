import os


class Paths:
    def __init__(self):
        self.root_path = self.get_root_path()
        self.images_path = self.get_images_path()

    def get_root_path(self):
        root_path = os.path.join(__file__, os.pardir, os.pardir)
        root_path = os.path.abspath(root_path)

        return root_path

    def get_images_path(self):
        images_path = os.path.join(self.root_path, "images")
        images_path = os.path.abspath(images_path)

        return images_path

    def select_image_file(self, image_file_name):
        image_file_path = os.path.join(self.images_path, image_file_name)
        image_file_path = os.path.abspath(image_file_path)

        return image_file_path