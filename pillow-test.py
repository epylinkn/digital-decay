import os
import re
import pdb

from PIL import Image
from time import sleep



def decay(fh):
    img = Image.open(fh)
    new_fh = next_name()

    img.save(new_fh, optimize=True, quality=20)
