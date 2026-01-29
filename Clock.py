import tkinter as tk
import time
import colorsys

hue = 0.0
HUE_SPEED = 0.0010
REFRESH_RATE = 20


def get_rainbow_color():

    global hue

    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

    r = int(rgb[0] * 255)
    g = int(rgb[1] * 255)
    b = int(rgb[2] * 255)

    color_hex = f"#{r:02x}{g:02x}{b:02x}"

    hue += HUE_SPEED
    if hue > 1.0:
        hue = 0.0

    return color_hex


def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)

    new_color = get_rainbow_color()
    clock_label.config(fg=new_color)

    root.after(REFRESH_RATE, update_clock)


root = tk.Tk()
root.title("RGB Clock")
root.geometry("400x150")
root.configure(bg='#101010')


clock_label = tk.Label(root, font=('Verdana', 50, 'bold'), bg='#101010')
clock_label.pack(expand=True)


update_clock()


root.mainloop()
