import multiprocessing

def start(Queue :multiprocessing.Queue, sensitivity):
    while True:
        print(Queue.get())