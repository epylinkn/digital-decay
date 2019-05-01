import os

from PIL import Image
from utils import next_filename


def jpeg_resave(fh):
    img = Image.open(fh)
    new_fh = next_filename()

    img.save(new_fh, optimize=True, quality=1)

def jpeg_resize(fh):
    img = Image.open(fh)
    new_fh = next_filename()
    tmp_fh = 'images/temp.jpg'

    img.resize((1730/4, 1228/4))
    img.save(tmp_fh, quality=50)

    down_image = Image.open(tmp_fh)
    down_image.resize((1730, 1228))

    down_image.save(new_fh, optimize=True, quality=50)
    os.remove(tmp_fh)
