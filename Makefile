build:
	thrift --gen py dbm.thrift

clean:
	rm -rf gen-py 
