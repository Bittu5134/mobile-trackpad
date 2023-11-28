import queue

def parallel(q :queue.Queue):
    while True:
        print(q.get())
