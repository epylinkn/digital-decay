import os
import re
import pdb

from PIL import Image
from time import sleep

from algorithms.geekouts import foo


def latest_filename(path=False):
    latest_fh = sorted(os.listdir('./images'))[-1]
    print(latest_fh)
    return "images/"+latest_fh if path else latest_fh

def next_name():
    fh = latest_filename()
    regex = re.compile('test-(\d{5}).jpg')
    current_version = int(regex.findall(fh)[0])
    next_version = format(current_version+1, '05')

    return 'images/test-' + next_version + '.jpg'

# this doesn't seem to work beyond a certain point
def jpeg_resave(fh):
    img = Image.open(fh)
    new_fh = next_name()

    img.save(new_fh, optimize=True, quality=1)

def jpeg_resize(fh):
    img = Image.open(fh)
    new_fh = next_name()
    tmp_fh = 'images/temp.jpg'

    img.resize((1730/4, 1228/4))
    img.save(tmp_fh, quality=50)

    down_image = Image.open(tmp_fh)
    down_image.resize((1730, 1228))

    down_image.save(new_fh, optimize=True, quality=50)
    os.remove(tmp_fh)

def decay(fh):
    jpeg_resave(fh)
    #jpeg_resize(fh)

foo()
1/0

while True:
    fh = latest_filename(path=True)

    #os.system('fbi -a --noverbose %s' % fh)
    #sleep(.02)

    decay(latest_filename(path=True))
