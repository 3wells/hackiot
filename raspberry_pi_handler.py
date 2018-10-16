import Adafruit_CharLCD as LCD
import time

lcd = LCD.Adafruit_CharLCD(27, 22, 25, 24, 23, 18, 16, 2, 4, False)


def callback(client, userdata, message):
    print(message.payload)
    lcd.clear()
    lcd.set_backlight(1)
    lcd.message(message.payload)

    if len(message.payload) > 16:
        for i in range(len(message.payload) - 16):
            time.sleep(0.5)
            lcd.move_left()
