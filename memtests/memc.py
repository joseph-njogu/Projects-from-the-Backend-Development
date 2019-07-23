# Caching Module For DB Queries
 
# SETTINGS
MEM_SERVER = '127.0.0.1' # Server Address
MEM_PORT = '11211' # Mem Port
MEM_TIMEOUT = 30 # Data TTL (Seconds)
 
 
import memcache, hashlib
 
# Connect To Local Memcache Server
mem = memcache.Client(['%s:%s' % (MEM_SERVER,MEM_PORT)])
 
def get_result(query):
        # Check if query has a value
        if query:
                hash = hashlib.md5(query).hexdigest()       # hash query with md5
 
                # Check Cache
                result = mem.get(hash)
                if result: # Check if query is cached
                        return result
                else:
                        return False # Nothing Cached, Run Query
 
def set_result(query, result):
        # Check if query has a value
        if query:
                hash = hashlib.md5(query).hexdigest()
 
                # Set Key and Value (hash, result)
                mem.set(hash,result, MEM_TIMEOUT)