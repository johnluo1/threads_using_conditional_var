from threading import Thread
import logging, random, time

import settings
from settings import resource_lock, shared_resource, max_resource_size

class Producer(Thread):

    def __init__(self, thread_id=None):
        logging.info("producer thread starting")
        Thread.__init__(self)
        self.name = "Producer" + (str(thread_id) if thread_id!=None else "")
    def cleanup(self):
        try: 
            pass
            # resource_lock.release()   # just in case 
        finally:
            pass
    def run(self):
        logging.info("running producer thread...")
        try:
            while True:
                resource_lock.acquire()
                if len(shared_resource) < max_resource_size:
                    shared_resource.append("some junk message " + str(random.randrange(10)))
                    logging.info("producing some random junk....")
                else: 
                    resource_lock.wait()
                    logging.info("resource is full. waiting")
                resource_lock.notify_all()
                resource_lock.release()
                logging.info("producer sleeping...")
                time.sleep(3 + random.random()*3)
        except Exception as e:
            logging.info("producer caught exception: " + str(e))
        finally: 
            self.cleanup()
