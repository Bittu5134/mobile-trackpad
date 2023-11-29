import random
import socket
import multiprocessing
import gui 
import server
import queue

if __name__ == "__main__":

    OAuthCode = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(20))
    serverUrl = socket.gethostbyname(socket.gethostname())
    mousePos = queue.Queue()

    guiProcess = multiprocessing.Process(target=gui.start, args=(serverUrl, OAuthCode))
    serverProcess = multiprocessing.Process(target=server.start, args=(OAuthCode, 10))

    guiProcess.start()
    serverProcess.start()

    while guiProcess.is_alive():pass
    serverProcess.terminate()
