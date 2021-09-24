import os
import sys
import time

import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET ES DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads/'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = f'{BASE_URL}/{cc.lower()}.gif'
    resp = requests.get(url)
    return resp.content


def show(text: str):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')

    return len(cc_list)


def main(download_many_func):
    t0 = time.time()
    count = download_many_func(POP20_CC)
    elapsed = time.time() - t0
    print(f'\n{count} flags downloaded in {elapsed:.2f}s')


if __name__ == '__main__':
    main(download_many)
