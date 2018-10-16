import Adafruit_CharLCD as LCD

from mqqtclient import MqqtClient
from settings import Settings

lcd = LCD.Adafruit_CharLCD(27, 22, 25, 24, 23, 18, 16, 2, 4,False)


def callback(client, userdata, message):
    print(message.payload)
    lcd.clear()
    lcd.set_backlight(1)
    lcd.message(message.payload)


class HackIot(object):

    def __init__(self):
        pass

    def start(self):

        s = Settings('config/settings.json')

        client = MqqtClient(s.device_id, s.device_endpoint, s.device_port, 'config/root-ca.pem',
                            'config/private.pem.key', 'config/certificate.pem.crt')
        client.start_callback_loop(callback)


if __name__ == "__main__":
    h = HackIot()
    h.start()
