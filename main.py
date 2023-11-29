import random
import socket
import multiprocessing

import logic
import server
import gui 

if __name__ == "__main__":

    OAuthCode = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(20))
    serverUrl = socket.gethostbyname(socket.gethostname())
    mousePos = multiprocessing.Queue(maxsize=2)

    guiProcess = multiprocessing.Process(target=gui.start, args=(serverUrl, OAuthCode))
    serverProcess = multiprocessing.Process(target=server.start, args=(OAuthCode, mousePos))
    logicProcess =multiprocessing.Process(target=logic.start, args=(mousePos,0))

    guiProcess.start()
    serverProcess.start()
    logicProcess.start()


    while guiProcess.is_alive():pass
    serverProcess.terminate()
    logicProcess.terminate()
