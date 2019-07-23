# Removing elements of A, which are also present in the other sets, provides the subtraction of multiple sets from a set A.

# Program to demonstrate set difference operation in Redis
import redis

redisClient = redis.StrictRedis(host='localhost',

                                port=6379,

                                db=0)

# Define multiple sets of numbers
redisClient.sadd("NumberSet1", 1, 2, 3, 4)
redisClient.sadd("NumberSet2", 2)
redisClient.sadd("NumberSet3", 3)

# Find the set difference between set 1 and all other sets
print(redisClient.sdiff("NumberSet1", "NumberSet2", "NumberSet3"))

# Define multiple sets of credit ratings
redisClient.sadd("CreditRatings1", "AAA", "AA", "BB")
redisClient.sadd("CreditRatings2", "BB")
redisClient.sadd("CreditRatings3", "AA")

# Find the set difference between CreditRatings set 1 and all other sets
# and tore the results in CreditRatings4

redisClient.sdiffstore("CreditRatings4", "CreditRatings1",
                       "CreditRatings2", "CreditRatings3")
print(redisClient.smembers("CreditRatings4"))
