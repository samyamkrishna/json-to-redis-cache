import json
import redis
redis_connection = redis.StrictRedis(host='localhost', port=6379, db=1)
with open('your_json_file.json') as json_data:
    your_data = json.load(json_data)
r.set('test_json', your_data)
