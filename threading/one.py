import threading
import queue
import two
import time

q = queue.Queue(maxsize=2)

def func():
    while True:
        q.put(time.time())

threading.Thread(target=func).start()
two.parallel(q)