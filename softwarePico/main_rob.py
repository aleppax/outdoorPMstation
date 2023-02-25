from libs import config, cron, logger, sensors, wlan, output_mqtt, output_db
from libs import leadacid, sps30, picosngcja5, ahtx0, bmp280
from time import ticks_diff, ticks_ms, sleep_ms
from secrets import secrets
from libs.mqtt_as import MQTTClient
from libs.mqtt_local import config_mqtt
from machine import Pin, I2C

client_mqtt = MQTTClient(config_mqtt)
#client_mqtt.connect()

#from machine import WDT
# init logger
logger.info('booting')
logger.check_fs_free_space()
#init I2C and GPIO. access a port with gpio['GP2']
#i2c, gpio = config.initialize_board()
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq =100000)
print (i2c)
th_s = ahtx0.AHT10(i2c) # AHT20 temperature humidity sensor
bm_b = bmp280.BMP280(i2c, addr=0x77, use_case = bmp280.BMP280_CASE_WEATHER) # Bosh BMP280 pressure temperature sensor
bm_b.oversample(bmp280.BMP280_OS_HIGH)
logger.info('I2C active, now sensor init')
#sensors.init(i2c, gpio)
logger.info('sensor init done')
#sensor_preheating = config.cron['sensor_preheating_s']*1000
connection_max_time = config.wlan['connection_timeout']*1000
wlan.initialize()
print(config.wlan['SSID_0'])
print(connection_max_time)
print(wlan)
#print(wlan.isconnected())
print('IP: ', wlan.ifconfig()[0])
logger.info('activate output')
if (config.scheduler['mqtt'] == 1):
    logger.info('mqtt enabled')
    client_mqtt = output_mqtt.init(i2c)
    logger.info('init mqtt done')
    print(client_mqtt)
    output_mqtt.mqttpub_test(client_mqtt,'proviamo') #rr fake write
    logger.info('mqtt sending')

output_db.db_measure('proviamo db') #rr fake write
logger.info('db sending')
exit()
while True:
    if cron.do_measure:
        sensors.wakeup()
        short_sleep = sensor_preheating - connection_max_time
#        cron.lightsleep_wrapper(short_sleep)
        logger.info('waking up')
        # init network
        start_extra_time = ticks_ms()
        extra_time_ms = ticks_diff(ticks_ms(),start_extra_time)
        still_to_wait = connection_max_time - extra_time_ms
        if still_to_wait > 0:
            sleep_ms(still_to_wait)
        #sensors measurements, they have been pre-heated for 30s
        sensors.measure(logger.now_DTF())
        sensors.shutdown()
        # if online, save data online, otherwise to file
        if wlan.initialize():
            #data submission to servers
            # load from file
            # send data
            output_mqtt.mqttpub('proviamo') #rr fake write
            logger.info("sending")
            #if submission is successful, reset file, otherwise write to file
        else:
            #store data to file
            logger.info("saving")
    # if online check if it's time to look for NTP and software updates
    if wlan.online():
        # a software upgrade starts only if an update is available
        print('non controllo update')
#        cron.updates()
#    wlan.turn_off()
    print('disabilito lightsleep')
    #cron.lightsleep_until_next_cycle()
    sleep_ms(30000)