# Intersection of multiple sets is provided by a set whose elements are present in all of those sets for which the Intersection is taken.

import redis

redisClient = redis.StrictRedis(host='localhost',

                                port=6379,

                                db=0)


# Define multiple sets of fruits in Redis

redisClient.sadd("FruitBasket1", "Pear", "Peach", "Guava", "Melon")
redisClient.sadd("FruitBasket2", "Apple", "Melon", "Berry", "Mango")
redisClient.sadd("FruitBasket3", "Grapes", "Banana", "Melon", "Berry")

# Finding the set Intersection of the multiple fruits
newBasket = redisClient.sinter("FruitBasket1", "FruitBasket2", "FruitBasket3")
print("Intersection of fruit basket")
print(newBasket)

# Define multiple sets of games in Redis
redisClient.sadd("GameSet1", "Cricket", "Hockey", "Base Ball")
redisClient.sadd("GameSet2", "Foot Ball", "Badminton", "Hockey")
redisClient.sadd("GameSet3", "Tennis", "Hockey", "Polo")

# Find the intersection of multiple sets of games
redisClient.sinterstore("GameSetCommon", "GameSet1", "GameSet2", "GameSet3")
# 'SINTERSTORE' is similar to 'SINTER', but Instead of returning the intersection of multiple sets, SINTERSTORE stores it in the destination set provided.
print("Intersection of game sets:")
print(redisClient.smembers("GameSetCommon"))
