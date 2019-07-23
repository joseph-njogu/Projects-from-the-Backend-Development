# Removing values from a Redis Hash using Python and Redis-Py

import redis

redisClient = redis.StrictRedis(host="localhost", port="6379", db=0)

# Add key value pairs to the Redis hash
hashName = "Dessert"
redisClient.hset(hashName, 1, "Cheesecake")
redisClient.hset(hashName, 2, "Apple Pie")

# Printing the hash
print(redisClient.hgetall(hashName))

# Removing a key
redisClient.hdel(hashName, 1)

# Printing the hash after removing a key
print(redisClient.hgetall(hashName))
