from  confluent_kafka import Consumer
import ast
consumer = Consumer(
    {
        'bootstrap.servers':'localhost:9092', 
        'group.id':'newGroup', 
        'auto.offset.reset':'earliest'
    })
consumer.subscribe(['reddit-events'])
try:
    while True:
        msg = consumer.poll(0.1) 
        if msg is None:
            continue
        if msg.error():
            print('Consumer error: {}'.format(msg.error()))
            continue
        print("msg.value", msg.value())
except KeyboardInterrupt:
    pass
finally:
    consumer.close()