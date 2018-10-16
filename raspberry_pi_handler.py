import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCD(27, 22, 25, 24, 23, 18, 16, 2, 4, False)


def callback(client, userdata, message):
    print(message.payload)
    lcd.clear()
    lcd.set_backlight(1)
    lcd.message(message.payload)
