import customtkinter
from PIL import Image

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("Remote TrackPad")
app.geometry("500x250")

my_image = customtkinter.CTkImage(light_image=Image.open("./test.png"), size=(200, 200))
button = customtkinter.CTkButton(app, text="", command=button_callback, image=my_image, fg_color="WHITE", hover_color="GREY")
button.grid(row=0, column=0, padx=20, pady=20)

rect = customtkinter.CTkFrame(app, fg_color="transparent", corner_radius=0, width=250, height=250)
rect.grid(row=0, column=1)


def slider_event(value):
    print(value)
    sliderLabel.configure(text=f"Sensitivity: {int(value)}")

slider = customtkinter.CTkSlider(rect, from_=0, to=100, command=slider_event, )
slider.grid(row=0, column=0, padx=20, pady=10)

sliderLabel = customtkinter.CTkLabel(rect, text="Sensitivity: 50")
sliderLabel.grid(row=1, column=0, padx=20, pady=0)


app.mainloop()