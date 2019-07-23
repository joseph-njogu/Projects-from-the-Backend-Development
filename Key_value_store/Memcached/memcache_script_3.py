import memcache

# connecting to the memcached server(s) using the Client constructor
client = memcache.Client([('127.0.0.1', 11211)])

# You can also pass a list of servers. This allows you to connect to a cluster of memcached servers by adding more servers to this list.
#client = memcache.Client([('127.0.0.1', 1121), ('127.0.0.1', 1121), ('127.0.0.1', 1122)])

data = {
    "some_key1": "Key value 1",
    "some_key2": "Key value 2"
}

# 'get/set_multi' that allows us to set or get multiple key/values at a single request. 
#  Also it allows us to add a certain prefix to all the keys during the set or get operations.
client.set_multi(data, time=15, key_prefix="pfx_")
print("Saved the dictionary with prefix pfx_")

print("Getting one key: %s" % client.get("pfx_some_key1"))
print ("Getting all values: %s" % client.get_multi(["some_key1", "some_key2"], key_prefix="pfx_"))
