import redis

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

# Create a Redis list with few even numbers
numberList = "numbers"
redisClient.rpush(numberList, 2, 4, 6, 8, 10, 12)

# Trimming the list to have only single digit elements
startIndex = 0
endIndex = 3

# 'ltrim' command keeps only a specified range of indexes of a Redis list and removes other elements
newList = redisClient.ltrim(numberList, startIndex, endIndex)

# Print the Redis list after trimming
for i in range(0, redisClient.llen(numberList)):
    print(redisClient.lindex(numberList, i))

# Clear the Redis list
for i in range(0, redisClient.llen(numberList)):
    print(redisClient.lpop(numberList))
