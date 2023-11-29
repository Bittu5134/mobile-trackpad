import random
import socket
import threading
import queue

import logic
import server
import gui 

if __name__ == "__main__":

    OAuthCode = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(20))
    serverUrl = socket.gethostbyname(socket.gethostname())
    mousePos = queue.Queue(maxsize=2)

    guiProcess = threading.Thread(target=gui.start, args=(serverUrl, OAuthCode))
    serverProcess = threading.Thread(target=server.start, args=(OAuthCode, mousePos))
    logicProcess = threading.Thread(target=logic.start, args=(mousePos,0))

    guiProcess.start()
    serverProcess.start()
    logicProcess.start()


    guiProcess.join()
    serverProcess.join()
    logicProcess.join()

    # while guiProcess.is_alive():pass
    # serverProcess.terminate()
    # logicProcess.terminate()
