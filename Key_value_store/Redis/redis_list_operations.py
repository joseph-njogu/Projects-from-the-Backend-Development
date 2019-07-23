import redis

redisClient = redis.StrictRedis(host="localhost", port=6379, db=0)

# Add values to the Redis list through the tail position of the list
noSQLList = "noSQLStores"

redisClient.rpush(noSQLList, "Redis")
redisClient.rpush(noSQLList, "MongoDB")
redisClient.rpush(noSQLList, "Neo4J")
redisClient.rpush(noSQLList, "HBase")
redisClient.rpush(noSQLList, "Cassandra")

# Add more than one value through the tail of the Redis list
redisClient.rpush(noSQLList, "Riak", "CouchDB")

# Printing the content of the redis list
while(redisClient.llen(noSQLList) != 0):
    print(redisClient.rpop(noSQLList))
