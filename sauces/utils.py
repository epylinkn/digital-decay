import os
import re


def latest_filename(path=False):
    latest_fh = sorted(os.listdir('./images'))[-1]
    print(latest_fh)
    return "images/"+latest_fh if path else latest_fh

def next_filename():
    fh = latest_filename()
    regex = re.compile('test-(\d{5}).jpg')
    current_version = int(regex.findall(fh)[0])
    next_version = format(current_version+1, '05')

    return 'images/test-' + next_version + '.jpg'
