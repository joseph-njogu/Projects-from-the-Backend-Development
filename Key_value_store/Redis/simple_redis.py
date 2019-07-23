# THis is a simple Redis-Py that creates a key called 'language'
# and connects to a Redis Server

import redis

# Creating a redis client
redisClient = redis.StrictRedis(host="localhost", port="6379", db=0)

# Setting string value for the key by the name 'language'
redisClient.set("Language", "Python 2.x")

# Getting the value for the key and print it
print(redisClient.get("Language"))

# Changing the value of the key
redisClient.set("Language", "Python 3.x")
print(redisClient.get("Language"))
