from weather import get_weather
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = Tk()
root.title("Current Weather forecast App")
root.geometry("900x500+300+200")
root.resizable(False, False)

def show_weather():
    
    city = textfield.get()
    weather_data = get_weather(city)

    if weather_data is not None:
        # Update labels with weather data
        t.config(text=(weather_data["temp"], "°"))
        c.config(text=(weather_data["condition"], "|", "FEELS LIKE", weather_data["feel_like"], "°"))
        w.config(text=(weather_data["wind"], "km/h"))
        h.config(text=(weather_data["humidity"], "%"))
        d.config(text=weather_data["description"])
        p.config(text=(weather_data["pressure"], "hPa"))
        SR.config(text=weather_data["sunrise"])
        SS.config(text=weather_data["sunset"])
        CT.config(text=f"CURRENT TIME: {weather_data['current_time']}")
    else:
        messagebox.showerror("Weather Forecast App", "City not found🚨🚨")
            
#Search box
Search_image = PhotoImage(file="image/Search-Bar.png")
myimage = Label(image=Search_image)
myimage.place(x=33, y=34)

# prompt the user for the input
textfield = tk.Entry(root, justify="center", width=21, font=("poppins", 25, "bold"))
textfield.place(x=45, y=45)
textfield.focus()

#search icon
Search_icon = PhotoImage(file="image/icon-bar.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#FFFFFF", command=show_weather)
myimage_icon.place(x=380, y=50)

#bottom box
frame_image = PhotoImage(file="image/frame01.png")
frame= Label(image=frame_image)
frame.pack(padx=5, pady=5, side = BOTTOM)

#sunset 
Sunset_image = PhotoImage(file="image/sunset.png")
Sunset = Label(image=Sunset_image)
Sunset.place(x=700, y=120)
SS = Label(font=("arial", 18, "bold"))
SS.place(x=720, y =270)

#sunrise
Sunrise_image = PhotoImage(file="image/sunrise.png")
Sunrise = Label(image=Sunrise_image)
Sunrise.place(x=460, y =120)
SR = Label(font=("arial", 18, "bold"))
SR.place(x=470, y =270)

#time
CT = Label(font=("arial", 15))
CT.place(x=50, y=280)

#label
label1 = Label(root, text="WIND SPEED", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=70, y=360)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=260, y=360)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=450, y=360)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=680, y=360)


t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=50, y=130)
c = Label(font=("arial", 15, "bold"))
c.place(x=50, y= 230)

w = Label(font=("arial", 18, "bold"), bg="#5A85B2")
w.place(x=90, y =420)
h = Label(font=("arial", 18, "bold"), bg="#5A85B2")
h.place(x=270, y =420)
d = Label(font=("arial", 18, "bold"), bg="#5A85B2")
d.place(x=440, y =420)
p = Label(font=("arial", 18, "bold"), bg="#5A85B2")
p.place(x=710, y =420)



root.mainloop()