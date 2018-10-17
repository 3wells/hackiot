from raspberry import Raspberry
from mqqtclient import MqqtClient
from settings import Settings


class HackIot(object):

    def __init__(self):
        pass

    def start(self):

        s = Settings('config/settings.json')

        client = MqqtClient(s.device_id, s.device_endpoint, s.device_port, 'config/root-ca.pem',
                            'config/private.pem.key', 'config/certificate.pem.crt')

        client.start_callback_loop(Raspberry().callback)


if __name__ == "__main__":
    h = HackIot()
    h.start()
