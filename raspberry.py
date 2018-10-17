import time
import boto3
import subprocess


class Raspberry:

    def __init__(self):

        self.enable_lcd = True
        self.enable_sound = True

        try:
            import Adafruit_CharLCD as LCD
            self.lcd = LCD.Adafruit_CharLCD(27, 22, 25, 24, 23, 18, 16, 2, 4, False)
        except IOError:
            self.enable_lcd = False

        self.polly_client = boto3.Session(region_name='us-west-2').client('polly')

    def callback(self, client, userdata, message):
        print(message.payload)
        self.display_message(message.payload)
        self.say_message(message.payload)

    def display_message(self, message):
        if self.enable_lcd:
            self.lcd.clear()
            self.lcd.set_backlight(1)
            self.lcd.message(message)

            if len(message) > 16:
                for i in range(len(message) - 16):
                    time.sleep(0.5)
                    self.lcd.move_left()

    def say_message(self, message):
        response = self.polly_client.synthesize_speech(VoiceId='Matthew',
                                                       OutputFormat='mp3',
                                                       Text=message)

        if self.enable_sound:
            speech_file = open('speech.mp3', 'w')
            speech_file.write(response['AudioStream'].read())
            speech_file.close()

            try:
                omxprocess = subprocess.Popen(['omxplayer', 'speech.mp3'], stdin=subprocess.PIPE, stdout=None,
                                              stderr=None, bufsize=0)
                time.sleep(2)
                omxprocess.stdin.write(b'q')
            except OSError:
                self.enable_sound = False
