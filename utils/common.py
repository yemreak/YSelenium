# Yardımcı modül belirteci
if __name__ == "__main__":
    print("Yardımcı modüldür, doğrudan çalıştırılamaz.")
    exit()

import time

from utils import config
from json import dumps

LOG_FILE = f"{config.OUTPUT_PATH}/{time.asctime()}.log"


def log_to_file(index=False, title=False):
    if config.LOGGER:
        with open(LOG_FILE, "a") as file:
            log_line = config.LOG_INFO + "|"

            if index:
                log_line += f"{index}.link işleniyor "

            if title:
                log_line += f"'{title}'"

            file.write(log_line)


def to_json(json_str: str):
    return dumps(json_str)


def download_urls(urls):
    import wget

    os.mkdir(DOWNLOAD_DIR)
    for url in urls:
        wget.download(url, out=DOWNLOAD_DIR)

def write_array_to_file(output_name, array):
    FILE_PATH = "/".join([config.OUTPUT_PATH, config.FILE_OUT])
    print(FILE_PATH)
    with open(FILE_PATH, "w") as file:
        for element in array:
            file.write(element + "\n")
