from moviepy import VideoFileClip
import tkinter as tk
from tkinter import filedialog
import imageio




#----------------- start -------------------

#function ....
def video_to_gif():
    video_path=filedialog.askopenfilename(
        title="select video",
        filetypes=[
            
            ("video files","*mp4 *.mov *.mkv *.avi " ),
            ("All files","*.*")
        ]
    )
    
    if not video_path:
        return
    
    
    
    
    start=float(start_entry.get())
    end=float(end_entry.get())
    
    output_path=filedialog.asksaveasfilename(title="save Gif",
                                             defaultextension=".gif",
                                             filetypes=[("GIF","*.gif")]
                                             )
    
    if not output_path:
        return
    
    
    
    
    
    clip=VideoFileClip(video_path)
    gif_clip=clip.subclipped(start,end)
    frames=[]
    
    for frame in gif_clip.iter_frames( fps=10):
        frames.append(frame)
        
    imageio.mimsave(output_path,frames,duration=0.1)
    
    gif_clip.close()
    clip.close()
    
    status_label.config(text="GIF Created Successfully.")
        








#------------ GUI 

window=tk.Tk()

window.title("Video -> GIF Converter.")

window.geometry("1000x1000")


title=tk.Label(window,text="🎬 Video -> GIF Converter" , font=("Arial", 22))# you can set every font that you wnat .
title.pack(pady=30)



start_label=tk.Label(window,text="Strat Time (Seconds)")
start_label.pack()


start_entry=tk.Entry(window)
start_entry.insert(0, "0")
start_entry.pack(pady=5)


end_label=tk.Label(window,text="End Time ( seconds)")
end_label.pack()
end_entry=tk.Entry(window)


end_entry.insert(0,"5")
end_entry.pack(pady=5)






#------------button
convert_button=tk.Button(window,
                         text="Convert to Gif🚩",
                         command=video_to_gif,
                         font=("Arial",14)
                         )
convert_button.pack(pady=25)


status_label=tk.Label(window,text="")
status_label.pack()

window.mainloop()




