try:
	from tkinter import *
	from tkinter import filedialog,messagebox
	import tkinter as tk
except:
	from Tkinter import *
	from Tkinter import filedialog,messagebox
	import Tkinter as tk
try:
	from pytube import *
	import webbrowser
except:
	messagebox.showinfo("Error","Requirements unsatisfied. See the requirements.txt file to install the Requirements")



root=tk.Tk()
root.geometry("500x600")
root.config(bg="#2D2926")
root.title("Youtube Video Downloader | Manjunathan C")
root.iconphoto(True,tk.PhotoImage(file="icon.png"))

def mp4():
	try:
		val=YouTube(entry.get())
		vid=val.streams.get_highest_resolution()
		path=filedialog.askdirectory()
		vid.download(path)
		messagebox.showinfo("Success","Done.\nFile saved in "+path)
	except:
		messagebox.showerror("Error Occured","1.URL Error\nOR\n2.Network Issue")
def mp3():
	try:
		val=YouTube(entry.get())
		vid=val.streams.filter(only_audio=True)#.all()
		path=filedialog.askdirectory()
		vid[0].download(path)
		messagebox.showinfo("Success","Done.\nFile saved in "+path+"\nYou can manually change the file extension to Mp3")
		
	except:
		messagebox.showerror("Error Occured","1.URL Error\nOR\n2.Network Issue")	

label1=Label(root,text="Youtube Video Downloader",bg="#2D2926",fg="#E94B3C",font=("font awesome",15,"bold italic"))
label1.place(x=110,y=10)

label2=Label(root,text="Paste Your URL here ",bg="#2D2926",fg="#E94B3C",font=("font awesome",10,"bold italic"))
label2.place(x=180,y=80)

entry=Entry(root,font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#2D2926",width=35,borderwidth=5)
entry.place(x=55,y=120)

label2=Label(root,text="Download",bg="#2D2926",fg="#E94B3C",font=("font awesome",12,"bold italic"))
label2.place(x=210,y=170)



button1=Button(root,font=("fontawesome",12,"bold italic"),text="Video",bg="#E94B3C",fg="#2D2926",borderwidth=5,width=10,activebackground="#181818",command=mp4)
button1.place(x=180,y=200)

button2=Button(root,font=("fontawesome",12,"bold italic"),text="Audio",bg="#E94B3C",fg="#2D2926",borderwidth=5,width=10,activebackground="#181818",command=mp3)
button2.place(x=180,y=260)

buttonclear=Button(root,text="Clear",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#2D2926",borderwidth=5,width=10,activebackground="#181818",command=lambda: entry.delete(0,END))
buttonclear.place(x=180,y=320)

buttexit=Button(root,text="Exit",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#2D2926",borderwidth=5,width=10,activebackground="#181818",command=root.quit)
buttexit.place(x=180,y=380)

buttoncontact=Button(root,text="Contact",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#2D2926",borderwidth=5,width=10,activebackground="#181818",command=lambda: webbrowser.open("https://github.com/cmanjunathan45/"))
buttoncontact.place(x=180,y=440)

buttonPlaylist=Button(root,text="Playlist Downloader",font=("fontawesome",12,"bold italic"),bg="#E94B3C",fg="#2D2926",borderwidth=5,width=15,activebackground="#181818",command=lambda: webbrowser.open("https://github.com/cmanjunathan45/youtube-playlist-downloader"))
buttonPlaylist.place(x=150,y=500)

root.mainloop()
