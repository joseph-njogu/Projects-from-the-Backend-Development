
# Adding values to a Redis Hash and retrieving them using Python and Redis-Py

import redis

# Creating a redis client
redisClient = redis.StrictRedis(host="localhost", port=6379, db=0)

# Adding key value pair to the hashes
redisClient.hset("NumberVsString", "1", "One")
redisClient.hset("NumberVsString", "2", "Two")
redisClient.hset("NumberVsString", "3", "Three")

# Retrieve the value for a specific key
print("The value for the key 3 is")
print(redisClient.hget("NumberVsString", "3"))
print()

# Printing the keys present in the Redis hash
print("The key present in the hash:")
print(redisClient.hkeys("NumberVsString"))
print()

# printing all the keys and values present in a hash
print("The keys and values present in the Redis hash are:")
print(redisClient.hgetall("NumberVsString"))
