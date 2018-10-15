import json


class Settings(object):

    device_id = None
    device_endpoint = None
    device_port = None

    def __init__(self, settings_file):
        try:
            f = open(settings_file, 'r')
            self.__dict__ = json.loads(f.read())
            f.close()
        except IOError:
            print('Settings file not found.')
            raise
