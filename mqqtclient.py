import time

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


class MqqtClient(object):

    def __init__(self, device_id, device_endpoint, device_port, root_ca_path, private_key_path, certificate_path):

        self.device_id = device_id

        self.client = AWSIoTMQTTClient(device_id)

        self.client.configureEndpoint(device_endpoint, device_port)
        self.client.configureOfflinePublishQueueing(-1)
        self.client.configureDrainingFrequency(2)
        self.client.configureConnectDisconnectTimeout(10)
        self.client.configureMQTTOperationTimeout(5)

        self.client.configureCredentials(root_ca_path, private_key_path, certificate_path)

        self.client.connect()

    def start_callback_loop(self, callback):

        self.client.subscribe('iot/{}'.format(self.device_id), 1, callback)

        try:
            while True:
                time.sleep(10)
                self.client.publish('iot/{}/heartbeat'.format(self.device_id), 'heartbeat', 0)
        except KeyboardInterrupt:
            pass
