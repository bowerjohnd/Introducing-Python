import redis

conn = redis.Redis(host='localhost', port=6379, decode_responses=True)

topics = ['siamese', 'persian']
sub = conn.pubsub()
sub.subscribe('siamese', 'persian')

print('Listening for:', topics)
for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']

        print('Subscribe: %s wears a %s' % (cat, hat))