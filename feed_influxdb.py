import socket
from influxdb import InfluxDBClient
from config import INFLUXDB_HOST, INFLUXDB_PORT, INFLUXDB_USERNAME, INFLUXDB_PASSWORD, INFLUXDB_DATABASE
import pyModeS

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((FR24_FEEDER_IP, FR24_FEEDER_PORT))

client = InfluxDBClient(host=INFLUXDB_HOST, port=INFLUXDB_PORT, username=INFLUXDB_USERNAME, password=INFLUXDB_PASSWORD, database=INFLUXDB_DATABASE)

while True:
    data = sock.recv(1024)
    if not data:
        break

    # Parse the ADS-B message using pyModeS
    msg = pyModeS.df(data)

    # Store the data in InfluxDB
    json_body = [
        {
            "measurement": "flightdata",
            "tags": {
                "icao24": msg.get('icao24'),
                "flight": msg.get('flight'),
            },
            "time": int(time.time() * 1000000000),
            "fields": {
                "altitude": msg.get('altitude'),
                "lat": msg.get('lat'),
                "lon": msg.get('lon'),
                "velocity": msg.get('velocity'),
                "vertical_rate": msg.get('vertical_rate'),
                "squawk": msg.get('squawk'),
                "alert": msg.get('alert'),
                "emergency": msg.get('emergency'),
                "spi": msg.get('spi'),
                "on_ground": msg.get('on_ground'),
            }
        }
    ]

    client.write_points(json_body)

