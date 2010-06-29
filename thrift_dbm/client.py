#!/usr/bin/env python

# based on the 'calculator' demo in the Thrift source

import simplejson
import thrift_dbm_gen
from thrift_dbm_gen import Dbm
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def connect():
  transport = TSocket.TSocket('localhost', 9090)
  transport = TTransport.TBufferedTransport(transport)
  protocol = TBinaryProtocol.TBinaryProtocol(transport)
  client = thrift_dbm_gen.Dbm.Client(protocol)
  transport.open()
  return (transport, client)


class ThriftDbm(object):
    def __init__(self, name):
        self.name = name
        self.transport, self.client = connect()

    def __getitem__(self, key):
        self.client.getitem(self.name, key)

    def __setitem__(self, key, value):
        return self.client.setitem(self.name, key, value)

    def __delitem__(self, key):
        return self.client.delitem(self.name, key)

    def keys(self):
        return self.client.keys(self.name)

    def __contains__(self, key):
        return self.client.contains(self.name, key)

    def close(self):
        self.transport.close()

class JsonDbm(ThriftDbm):
    def __getitem__(self, key):
        return simplejson.loads(self.client.getitem(self.name, key))

    def __setitem__(self, key, value):
        return self.client.setitem(self.name, key, simplejson.dumps(value))


