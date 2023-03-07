from libs import logger, config
from libs.cron import feed_wdt
import urequests as requests

def send_data(d):
    feed_wdt()
    try:
        resp = requests.post(config.datalogger['URL'], json=d, timeout=config.board['WDT_seconds']-0.2)
        logger.info(resp.content)
    except OSError:
        feed_wdt()
        logger.warning("Couldn't reach datalogging URL")
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
    return result
