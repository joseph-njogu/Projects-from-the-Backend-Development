import memcache

# connecting to the memcached server(s) using the Client constructor
client = memcache.Client([('127.0.0.1', 11211)])

#This dictionary will act as the value to the key
sample_obj = {
    "name": "Soliman",
    "language": "Python"
}

# set method to store a standard Python dict as the value of the "sample_user" key.
client.set("sample_user", sample_obj, time=15)
print ("Stored to memcache, will auto-expire in 15 seconds")

print(client.get("sample_user"))	#Retrieving data using set
