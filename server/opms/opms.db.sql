BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "measurements" (
	"id"	INTEGER,
	"station"	INTEGER NOT NULL,
	"datetime"	TEXT NOT NULL,
	"humidity"	NUMERIC NOT NULL,
	"temperature"	NUMERIC NOT NULL,
	"pm1.0"	NUMERIC NOT NULL,
	"pm2.5"	NUMERIC NOT NULL,
	"pm4"	NUMERIC,
	"pm10"	NUMERIC,
	"pm1.0_ch2"	NUMERIC,
	"pm2.5_ch2"	NUMERIC,
	"pm4_ch2"	NUMERIC,
	"pm10_ch2"	NUMERIC,
	"sound pressure"	INTEGER,
	"barometric pressure"	INTEGER,
	"battery charge percentage"	NUMERIC,
	"O3"	INTEGER,
	"NO2"	INTEGER,
	"internal temperature"	NUMERIC,
	"wind direction"	INTEGER,
	"wind speed"	INTEGER,
	"battery is charging"	INTEGER,
	"dew point"	NUMERIC,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "stations" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"maintainer"	TEXT NOT NULL,
	"station purpose"	TEXT NOT NULL,
	"latitude"	NUMERIC NOT NULL,
	"longitude"	NUMERIC NOT NULL,
	"altitude msl"	INTEGER,
	"country"	TEXT NOT NULL,
	"city"	TEXT NOT NULL,
	"address"	TEXT NOT NULL,
	"pm capable ch1"	INTEGER NOT NULL,
	"pm capable ch2"	INTEGER,
	"pm units ch1"	TEXT NOT NULL,
	"pm units ch2"	TEXT,
	"pm sensor model ch1"	TEXT NOT NULL,
	"pm sensor model ch2"	TEXT,
	"pm sensor SN ch1"	TEXT,
	"pm sensor SN ch2"	TEXT,
	"pm sensor in situ calibration report ch1"	TEXT,
	"pm sensor in situ calibration report ch2"	TEXT,
	"pm sensor uncertainty percentage ch1"	INTEGER,
	"pm sensor uncertainty percentage ch2"	INTEGER,
	"sound pressure capable"	INTEGER NOT NULL,
	"sound pressure units"	TEXT,
	"sound pressure sensor model"	TEXT,
	"barometric pressure capable"	INTEGER NOT NULL,
	"barometric pressure units"	TEXT,
	"barometric pressure sensor model"	TEXT,
	"temperature capable"	INTEGER,
	"temperature units"	TEXT,
	"temperature sensor model"	TEXT,
	"O3 capable"	INTEGER NOT NULL,
	"O3 units"	TEXT,
	"O3 sensor model"	TEXT,
	"NO3 capable"	INTEGER NOT NULL,
	"NO3 units"	TEXT,
	"NO3 sensor model"	TEXT,
	"wind direction capable"	INTEGER NOT NULL,
	"wind direction units"	TEXT,
	"wind direction sensor model"	TEXT,
	"wind speed capable"	INTEGER NOT NULL,
	"wind speed units"	TEXT,
	"wind speed sensor model"	TEXT,
	"umidity capable"	INTEGER,
	"umidity units"	TEXT,
	"umidity sensor model"	TEXT,
	PRIMARY KEY("id")
);
