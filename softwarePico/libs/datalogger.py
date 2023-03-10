from libs import logger, config
from libs.cron import feed_wdt
import urequests as requests
from machine import unique_id
import binascii
from time import sleep_ms

iam = unique_id()
UID = str(int(binascii.hexlify(iam).decode('utf-8'),16))

def send_data(d):
    feed_wdt()
    try:
        # if resp takes too long to arrive, 
        resp = requests.post(config.datalogger['URL'], json=d, timeout=config.board['WDT_seconds']-0.5)
        logger.info(resp.content)
    except OSError:
        feed_wdt()
        return False
    feed_wdt()
    isInt = True
    try:
        # converting to integer (we assume that the server replies
        # with the new record ID if the insert succeded. An error message otherwise.
        int(resp.content)
    except ValueError:
        isInt = False
    return isInt

def send_data_list(l):
    result = True
    for d in l:
        result &= send_data(d)
        sleep_ms(100)
    if result == False:
        logger.warning("Couldn't reach datalogging URL")
    return result
