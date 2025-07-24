from tkinter import *
import requests

WINDOW_COLOR = "#799EFF"

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.minsize(width=400, height=600)
window.title('Kanye quotes')
window.configure(background=WINDOW_COLOR, padx=10, pady=10)

kanye_img = PhotoImage(file='kanye.png')
bg_img = PhotoImage(file='background.png')

canvas = Canvas(width=300, height=414, bg=WINDOW_COLOR, highlightthickness=0)
canvas.create_image(150, 207, image=bg_img)
quote_text = canvas.create_text(150, 200, text="QUOTE GOES HERE", font=("Arial", 20, "normal"), fill="white", width=210)
canvas.pack()

kanye_button = Button(image=kanye_img, bg=WINDOW_COLOR, borderwidth=0, command=get_quote)
kanye_button.pack()
get_quote()

window.mainloop()