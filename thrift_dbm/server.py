#!/usr/bin/env python

# see http://github.com/myelin/simple-thrift-queue
# based on the 'calculator' demo in the Thrift source

import thrift_dbm_gen
from thrift_dbm_gen import Dbm
from thrift_dbm_gen.ttypes import *
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import gdbm
import os.path

class DbmHandler(object):
    __BASE__="/srv/thrift_dbm"
    def __init__(self):
        self.dbms = {}

    def db(self, dbname):
        if not dbname in self.dbms:
            self.dbms[dbname] = gdbm.open(os.path.join(DbmHandler.__BASE__, dbname), "c")
        return self.dbms[dbname]


    def setitem(self, dbname, key, value):
        self.db(dbname)[key] = value

    def getitem(self, dbname, key):
        try:
            return self.db(dbname)[key]
        except KeyError, ke:
            raise Exception("KeyError: "+str(ke))

    def delitem(self, dbname, key):
        try:
            del self.db(dbname)[key]
        except KeyError, ke:
            raise Exception("KeyError: "+str(ke))

       

    def contains(self, dbname, key):
        return key in self.db(dbname)
    
    
    def keys(self, dbname):
        return self.db(dbname).keys()



def run_server():
    handler = DbmHandler()
    processor = thrift_dbm_gen.Dbm.Processor(handler)
    transport = TSocket.TServerSocket(9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    #server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    #server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    print 'Starting the server...'
    server.serve()
    print 'done.'
