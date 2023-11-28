from qrcode import make as qrMake
from customtkinter import CTk, CTkImage, CTkLabel, CTkSlider, CTkFrame
import random
import socket
import server
import threading
import flask
import flask_socketio

OAuthCode = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*") for i in range(20))
serverUrl = socket.gethostbyname(socket.gethostname())

def GUI(OAuthCode, serverUrl):
    gui = CTk()
    gui.title("Remote Trackpad")
    gui.geometry("500x250")

    qrCode = CTkImage(light_image=qrMake(f"http://{serverUrl}:4155/?code={OAuthCode}").get_image(), size=(200, 200))
    qrLabel = CTkLabel(gui, text="", image=qrCode)
    qrLabel.grid(row=0, column=0, padx=20, pady=20)

    ctrlFrame = CTkFrame(gui, fg_color="transparent")
    ctrlFrame.grid(row=0, column=1, padx=20, pady=20)

    def slider_event(value): senseLabel.configure(text=f"Sensitivity: {int(value)}%")
    senseSlider = CTkSlider(ctrlFrame, from_=0, to=100, number_of_steps=100, command=slider_event)
    senseSlider.grid(row=0, column=0, padx=20, pady=0)
    senseLabel = CTkLabel(ctrlFrame, text="Sensitivity: 50%")
    senseLabel.grid(row=1, column=0, padx=20, pady=0)

    gui.mainloop()


threading.Thread(target=GUI, args=(OAuthCode, serverUrl)).start()
server.start(OAuthCode)