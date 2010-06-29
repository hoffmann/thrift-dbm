import sys, os.path
sys.path.insert(0, os.path.join(os.path.abspath(os.path.split(__file__)[0]), '..', 'gen-py'))

from thrift_dbm.client import connect, ThriftDbm, JsonDbm
from thrift_dbm.server import run_server
