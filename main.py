import os
import subprocess
import pdb

from time import sleep
from sauces.utils import latest_filename
from sauces.ketchup import jpeg_resave, jpeg_resize
from sauces.mustard import vignette


DETACHED_PROCESS = 0x00000008

i = 0
while True:
    i = i + 1
    fh = latest_filename(path=True)

    cmd = 'fbi -a --noverbose %s' % fh
    proc = subprocess.Popen(cmd, shell=True)

    sleep(.5)
    proc.terminate()

    vignette('images/test-00001.jpg', i)

