
from lib.network import get_ip, get_tor_address
from lib.qr_generator import generate_qr_code
from lib.lnd import LndGRPC
from lib.btc import BtcRPC
import lib.rpc_pb2 as ln
import lib.rpc_pb2_grpc as lnrpc
from lib.network import get_tor_address
from consts import bold_font

import pygame

class InfoSectionsList():

    def __init__(self):
        # Init RPC connections
        self.btc_grpc = BtcRPC()
        self.lnd_grpc = LndGRPC()
    class torURL():
        def __init__(self, parent):
            self.title = "Tor URL"
            self.data = "Loading..."
            self.parent = parent
        def updateData(self):
            self.data = get_tor_address()
        def getData(self):
            self.updateData()
            return (self.title, self.data, True, pygame.freetype.Font(bold_font, 20))
    class maxSend():
        def __init__(self, parent):
            self.title = "Max Send"
            self.data = "Loading..."
            self.parent = parent
        def updateData(self):
            self.data = self.parent.lnd_grpc.get_max_send()
        def getData(self):
            self.updateData()
            return (self.title, self.data, False, False)
    class maxReceive():
        def __init__(self, parent):
            self.title = "Max Recieve"
            self.data = "Loading..."
            self.parent = parent
        def updateData(self):
            self.data = self.parent.lnd_grpc.get_max_receieve()
        def getData(self):
            self.updateData()
            return (self.title, self.data, False, False)
    class activeChannels():
        def __init__(self, parent):
            self.title = "Active Channels"
            self.data = "Loading..."
            self.parent = parent
        def updateData(self):
            self.data = self.parent.lnd_grpc.get_active_channels()
        def getData(self):
            self.updateData()
            return (self.title, self.data, False, False)
    class forward():
        def __init__(self, parent):
            self.title = "24H Forwards"
            self.data = "Loading..."
            self.parent = parent
        def updateData(self):
            self.data = self.parent.lnd_grpc.get_forwarding_events()
        def getData(self):
            self.updateData()
            return (self.title, self.data, False, False)
    class syncProgress():
        def __init__(self, parent):
            self.title = "Sync progress"
            self.data = "Loading..."
            self.parent = parent
        def updateData(self):
            self.data = str(self.parent.btc_grpc.get_sync_progress()) + "%"
        def getData(self):
            self.updateData()
            return (self.title, self.data, False, False)
