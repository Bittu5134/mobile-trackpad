import queue

def start(Queue :queue.Queue, sensitivity):
    while True:
        print(Queue.get())