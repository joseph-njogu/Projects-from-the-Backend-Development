# Get the properties of a Redis Hash

import redis

redisClient = redis.StrictRedis(host="localhost", port=6379, db=0)

hashName = "Authors"
redisClient.hmset(hashName, {1: "The C Programming Language", 2: "THe UNIX Programming Environment"})

# CHecking if the key exists
key = 1
print("Does the key {}, exists:".format(key))
# 'hexists' checks and return an integer whether a specified key exists on a Redis hash. Returns TRUE or FALSE
print(redisClient.hexists(hashName, key))

# Print the key value pairs of the Redis hash
print("Before deletion of a key:")
print(redisClient.hgetall(hashName))
print()

# Removing a key
redisClient.hdel(hashName, key)

# Printing the value of the key-value has been removed
print("After deletion of the key:")
# Returning all key values present in hash
print(redisClient.hgetall(hashName))
