from PIL import Image, ImageTk


class ImageLoader:
    @staticmethod
    def load(image_name, colorIndex, index, res):
        im = Image.open(image_name)

        img_left_area = (index*res, colorIndex*res, index*res+res, (colorIndex*res)+res)
        img = im.crop(img_left_area)

        img = img.resize((int(res*1.4), int(res*1.4)), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(img)

        return img