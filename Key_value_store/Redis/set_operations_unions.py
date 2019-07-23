# Demonstrating set union
# Union of 'n' sets is a set, which has elements that are part of either the individual sets or part of many of them.

import redis

redisClient = redis.StrictRedis(host='localhost',

                                port=6379,

                                db=0)
# Define multiple sets of fruits
redisClient.sadd("Fruits1", "Pear", "Peach", "Guava", "Melon")
redisClient.sadd("Fruits2", "Apple", "Melon", "Berry", "Mango")
redisClient.sadd("Fruits3", "Grapes", "Banana", "Melon", "Berry")

# Finding the union of the sets
print(redisClient.sunion("Fruits1", "Fruits2", "Fruits3"))

# Defining multiple set of games
redisClient.sadd("Games1", "Cricket", "Hockey", "BaseBall")
redisClient.sadd("Games2", "FootBall", "Badminton", "Hockey")
redisClient.sadd("Games3", "Tennis", "Hockey", "Polo")

# Find the union of the redis sets and store it in the destination set provided
# 'SUNIONSTORE'is similar to 'SUNION'. However, stores the resultant union of multiple sets in a destination set provided.
redisClient.sunionstore("Games4", "Games1", "Games2", "Games3")

# Print the members of new set
print(redisClient.smembers("Games4"))
