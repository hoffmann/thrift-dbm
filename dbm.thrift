namespace py thrift_dbm_gen

exception Exception
{
  1:string msg,
}

service Dbm {

    void setitem(1:string dbname, 2:string key, 3:string value),

    string getitem(1:string dbname, 2:string key) throws (1:Exception e),
	
    void delitem(1:string dbname, 2:string key) throws (1:Exception e),
    
    bool contains(1:string dbname, 2:string key),

    list<string> keys(1:string dbname)

}



