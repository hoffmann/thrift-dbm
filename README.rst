==========
thrift-dbm
==========

Peter Hoffmann
http://peter-hoffmann.com/code/thrift-dbm/

**thrift-dbm** is a thrift rpc server for key/value databases.
It is still alpha software and a toy-project to explore 
thrift. The server is written in Python and uses
gdbm, the GNU implementation of the standard Unix dbm library.

The Python client library provides raw access to the rpc connection
as well as a dict like access. 


Requirements
============

- Apache Thrift <http://incubator.apache.org/thrift/>
- Python  <http://python.org>

Building and running
====================


::

    make
    python runserver.py

Then start a python shell::

    import thrift_dbm
    db = thrift_dbm.ThriftDbm("test.db")
    db['foo'] = 'bar'
    'bar' in db
    print db['foo']


More Information
================
The software was inspired by Phillip Pearsons simple-thrift-queue_.

.. _simple-thrift-queue:  http://github.com/myelin/simple-thrift-queue

