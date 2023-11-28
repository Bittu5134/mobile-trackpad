import qrcode
from customtkinter import CTk, CTkImage, CTkLabel, CTkSlider, CTkFrame
import random
import socket
import multiprocessing
import flask
import flask_socketio
import queue

def GUI(serverUrl, OAuthCode):

    gui = CTk()
    gui.resizable(False, False)
    gui.title("Remote Trackpad")
    gui.geometry("500x250")

    qrCode = CTkImage(light_image=qrcode.make(f"http://{serverUrl}:4155/?code={OAuthCode}").get_image(), size=(200, 200))
    qrLabel = CTkLabel(gui, text="", image=qrCode)
    qrLabel.grid(row=0, column=0, padx=20, pady=20)

    ctrlFrame = CTkFrame(gui, fg_color="transparent")
    ctrlFrame.grid(row=0, column=1, padx=20, pady=20)

    def slider_event(value): senseLabel.configure(text=f"Sensitivity: {int(value)}%")
    senseSlider = CTkSlider(ctrlFrame, from_=0, to=300, number_of_steps=300, command=slider_event)
    senseSlider.grid(row=0, column=0, padx=20, pady=0)
    senseLabel = CTkLabel(ctrlFrame, text="Sensitivity: 150%")
    senseLabel.grid(row=1, column=0, padx=20, pady=0)

    gui.mainloop()


if __name__ == "__main__":

    OAuthCode = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*") for _ in range(20))
    serverUrl = socket.gethostbyname(socket.gethostname())
    mousePos = queue.Queue()

    serverProcess = multiprocessing.Process(target=SERVER , args=(OAuthCode, mousePos))
    guiProcess = multiprocessing.Process(target=GUI, args=(serverUrl, OAuthCode))

    serverProcess.start()
    guiProcess.start()

    while guiProcess.is_alive(): pass
    serverProcess.terminate()