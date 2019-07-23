import redis


# Create a redis client

redisClient = redis.StrictRedis(host='localhost',

                                port=6379,

                                db=0)

# Defining a set of prime numbers
redisClient.sadd("primes", 2, 3, 5, 7)

# 'SISMEMBER' checks whether an element is a member of a set.

# Checking if 6 is a prime number
print("Is 6 a prime number? {}".format(redisClient.sismember("primes", 6)))

# Checking if 7 is a prime number
print("Is 7 a prime number? {}".format(redisClient.sismember("primes", 7)))
