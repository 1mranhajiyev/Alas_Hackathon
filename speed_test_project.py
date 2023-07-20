#pip install speedtest-cli
from tkinter import * 
from speedtest import Speedtest

# Creation OF Function
def update_text(): 
    speed_test = Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)
    down_label.config(text= "Download Speed - " + str(download_speed) + "Mbps") 
    up_label.config(text= "Upload Speed - " + str(upload_speed) + "Mbps") 


# Creation OF GUI
window = Tk()
window.title("Internet Speed Testing")
window.geometry('420x250')
button = Button(window, text="Press Here to Check Speed", width=50, command=update_text,background = 'green', foreground = 'white', font = ('calibri', 12, 'bold'), borderwidth=3)
button.pack(pady=20)
down_label = Label(window, text="", font = ('calibri', 16, 'bold'))
down_label.pack(pady=20)
up_label = Label(window, text="", font = ('calibri', 16, 'bold'))
up_label.pack(pady=20)
window.mainloop()

# End of Code

