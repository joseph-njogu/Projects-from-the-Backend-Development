# Sample Python program to demonstrate List operations of Redis

import redis

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

# Add values to the Redis list through the HEAD position of the list
redisClient.lpush("LanguageList", "Kotlin")
redisClient.lpush("LanguageList", "Python")

# Push multiple values through the HEAD of the list
redisClient.lpush("LanguageList", "Java", "C++")

# Printing the content pf the Redis list
while (redisClient.llen("LanguageList") != 0):
    print(redisClient.lpop("LanguageList"))
