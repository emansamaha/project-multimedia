from tkinter import Label, messagebox, Frame,Tk, Entry, Button
import yt_dlp
import webbrowser
def play_video(resolution):
    url =url_entry.get()
    
    if not url:
        messagebox.showerror("Error", "Please paste a valid YouTube link.")
        return
    
    try:
        ydl_opts = {}
        
        if resolution == "high":
            ydl_opts = {'format': 'bestvideo'}
        elif resolution == "low":
            ydl_opts = {'format': 'worstvideo'}
        elif resolution == "audio":
            ydl_opts = {'format': 'bestaudio'}
        else:
            messagebox.showerror("Error", "Invalid resolution option.")
            return
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url', None)
            
            if not video_url:
                messagebox.showerror("Error", f"No streams available for {resolution} resolution.")
            else:
                webbrowser.open(video_url)
    
    except yt_dlp.utils.DownloadError as e:
        messagebox.showerror("Download Error", f"Could not process the video: {e}")
    
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

root = Tk()
root.title("GUI")
root.geometry("400x300")

Label(root, text="Add Your Link Here",bg="yellow",font= 2).pack(pady=20,ipadx=5,ipady=5)

url_entry = Entry(root, width=40,bg="gray")
url_entry.pack(pady=40)

button = Frame(root)
button.pack(pady=5)

highbutton = Button(button, text="High Resolution", command=lambda: play_video("high"),bg="green",fg="white")
highbutton.pack(side="left", padx=10)

lowbutton = Button(button, text="Low Resolution", command=lambda: play_video("low"),bg="green",fg="white")
lowbutton.pack(side="left", padx=10)

audiobutton = Button(root, text="Audio Only", command=lambda: play_video("audio"),bg="green",fg="white")
audiobutton.pack(pady=15)

root.mainloop()