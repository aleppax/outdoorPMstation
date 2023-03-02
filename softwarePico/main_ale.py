from libs import config, cron, filelogger, logger, sensors, wlan
from time import ticks_diff, ticks_ms

# init logger
logger.info('booting')
logger.check_fs_free_space()
#init I2C and GPIO. access a port with gpio['GP2']
i2c, i2c_1, gpio = config.initialize_board2()
print('ok00')
sensors.init2(i2c,i2c_1, gpio)
print('ok0')
sensor_preheating = config.cron['sensor_preheating_s']*1000
connection_max_time = config.wlan['connection_timeout']*1000

while True:
    if cron.do_measure:
        sensors.wakeup()
        print('ok1')
        short_sleep = sensor_preheating - connection_max_time
        cron.lightsleep_wrapper(short_sleep)
        print('ok2')
        
        logger.info('waking up')
        # init network
        start_extra_time = ticks_ms()
        print('ok3')
        extra_time_ms = ticks_diff(ticks_ms(),start_extra_time)
        still_to_wait = connection_max_time - extra_time_ms
        print('ok4')
        if still_to_wait > 0:
            cron.sleep_ms_feeded(still_to_wait)
        #sensors measurements, they have been pre-heated for 30s
        sensors.measure(logger.now_DTF())
        sensors.shutdown()
        # if online, save data online, otherwise to file
        if wlan.initialize():
            #success = datalogger.send_data_list(filelogger.read())
            # if success:
            #     filelogger.clear_data()
            #data submission to servers
            # load from file
            # datalogger.send_data(sensors.measures)
            logger.info("sending")
            #if submission is successful, reset file, otherwise write to file
        else:
            #store data to file
            logger.info("saving")
            filelogger.write(sensors.measures)
    # if online check if it's time to look for NTP and software updates
    if wlan.online():
        # a software upgrade starts only if an update is available
        cron.updates()
    wlan.turn_off()
    cron.lightsleep_until_next_cycle()

