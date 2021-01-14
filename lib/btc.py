import os

from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
  
class BtcGRPC:
    def __init__(self):
        btcurl = "http://%s:%s@%s:%s"%(os.getenv('BITCOIN_RPC_USER'), os.getenv('BITCOIN_RPC_PASS'), os.getenv('BITCOIN_IP'), os.getenv('BITCOIN_RPC_PORT'))
        self.connection = AuthServiceProxy(btcurl)

    def connection_locked(self):
        try:
            response = self.connection.get_blockchain_info()
            return True
        except JSONRPCException:
            return False

    def get_blockchain_info(self):
        response = self.connection.getblockchaininfo()
        return response