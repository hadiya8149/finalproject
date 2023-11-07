from confluent_kafka import Producer, Consumer
import confluent_kafka
import multiprocessing
import time
producer = Producer(
    {'bootstrap.servers':'localhost:9092'} 
                         )

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition))

def ll():
    for n in range(0,10):
        producer.poll(0)
        
        producer.produce('reddit-events', str(n).encode('utf-8'), callback=delivery_report)
    for n in "hadiyaasif":
        producer.poll(0)
        producer.produce('reddit-events', str(n).encode('utf-8'), callback=delivery_report)
    producer.flush()

consumer = Consumer(
    {
        'bootstrap.servers':'localhost:9092', 
        'group.id':'newGroup', 
        'auto.offset.reset':'earliest'
    })
consumer.subscribe(['reddit-events'])
def ip():
    try:
        while True:
            msg = consumer.poll(0.1) 
            if msg is None:
                continue
            if msg.error():
                print('Consumer error: {}'.format(msg.error()))
                continue
            print("msg.value", msg.value())
            print('Consumed: {}'.format(type(msg.value().decode('utf-8'))))
            print(msg.offset)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
def process_data():
    print("hiya hiya hiya look at me")
    arr = [1,2,3,4]
    return arr
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=ll)
    p2  = multiprocessing.Process(target=ip)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    with multiprocessing.Pool() as pool:
        res = [pool.apply_async(process_data)]
        pool.close()
        pool.join()
    for y in res:
        x  = y.get()
    print(x)

    print("done")
    # so basically i want the consumer to run on a different process and the other processes differently