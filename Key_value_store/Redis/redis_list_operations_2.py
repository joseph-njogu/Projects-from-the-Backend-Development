import redis

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

# Create a Redis list with all zeros
numberList = "numbers"
redisClient.lpush(numberList, 0, 0, 0, 0, 0)

# Print the Redis list before modification
for i in range(0, redisClient.llen(numberList)):
    # 'lindex' returns a value of an element from a Redis list as defined by the index.
    print(redisClient.lindex(numberList, i))

# Modify Redis list contents
for i in range(0, redisClient.llen(numberList)):
    redisClient.lset(numberList, i, i * 2)

print("Contents of the list after modification:")

# Print the Redis list after modification
for i in range(0, redisClient.llen(numberList)):
    print(redisClient.lindex(numberList, i))

# Emptying the Redis list
for i in range(0, redisClient.llen(numberList)):
    redisClient.lpop(numberList)

# Print the length of the list after removing all its elements
print("Length of the Redis list after removing all elements:")
print(redisClient.llen(numberList))
