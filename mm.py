import tkinter as tk
from gtts import gTTS
import playsound
import os


def text_to_speech():
    text = entry.get()
    if text.strip():  
        tts = gTTS(text=text, lang='en')
        audio_file = "speech.mp3"
        try:
            tts.save(audio_file)
            playsound.playsound(audio_file)
        finally:
            if os.path.exists(audio_file):
                os.remove(audio_file)


def clear_text():
    entry.delete(0, tk.END)


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Text to Speech")
root.geometry("600x600")
root.configure(bg="#f0f0f0") 


label = tk.Label(root, text="Text to Speech", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
label.pack(pady=20)


entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=20)


button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)


play_button = tk.Button(
    button_frame, text="Play", command=text_to_speech, 
    bg="red", fg="white", font=("Arial", 12), width=12, height=2
)
play_button.grid(row=0, column=0, padx=15, pady=10)


clear_button = tk.Button(
    button_frame, text="Clear", command=clear_text, 
    bg="green", fg="white", font=("Arial", 12), width=12, height=2
)
clear_button.grid(row=0, column=1, padx=15, pady=10)


exit_button = tk.Button(button_frame, text="Exit", command=exit_app, bg="black",font=("Arial", 12), fg="white", width=12, height=2)
exit_button.grid(row=0, column=2, padx=15,pady=10)

root.mainloop()