import memcache

# connecting to the memcached server(s) using the 'Client' constructor,
# and then we using the set method to store a standard Python 'counter'
client = memcache.Client([('127.0.0.1', 11211)])
client.set("counter", "10")

client.incr("counter")
print("The counter was incremented on the server by 1, now the counter is %s" %
      client.get("counter"))

client.incr("counter", 9)
print("The counter was incremented on the server by 9, now its %s" %
      client.get("counter"))

client.decr("counter")
print ("Counter was decremented on the server by 1, now it's %s" %
       client.get("counter"))
