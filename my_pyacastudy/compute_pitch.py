import my_pyacastudy.audio_math_lib as AudioMath
import tkinter as tk
from tkinter import filedialog, messagebox
from waapi import WaapiClient
import my_pyacastudy.audio_func_lib as AudioFunc

#parser = argparse.ArgumentParser(description="File Path.")
#parser.add_argument("file_path", help= "The path to the file.")

#args= parser.parse_args()
#file_path = args.file_path

#audio_pitch = AudioMath.GetSoundPitch(file_path)


def send_pitch_to_wwise(pitch_value):
    try:

        with WaapiClient() as client:
            client.call("ak.wwise.core.object.setProperty", {
                "object": "Object_ID",
                "property": "property name",
                "value": pitch_value
            })
            print(f"Pitch value {pitch_value} sent to Wwise!")
    except Exception as e:
        print (f"Failed to send pitch to WWise: {e}")

def browse_file():
    file_path = filedialog.askopenfile(
        title="Select Audio File",
        filetypes=(("Audio Files", "*.wav *.mp3"), ("All Files", "*.*"))
    )
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)


def submit():
    file_path = file_entry.get()
    if file_path:
      pitch = AudioFunc.GetAudioFilePitch(file_path)
      send_pitch_to_wwise(pitch)
    else:
        messagebox.showwarning("Input Needed", "Please provide a file path.")
    

root = tk.Tk()
root.title("Pitch Value")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

file_label = tk.Label(frame, text="File Path:")
file_label.grid(row =0, column=0, sticky="w")

file_entry = tk.Entry(frame, width=50)
file_entry.grid(row=0, column=1, padx=5)

browse_button = tk.Button(frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2)

submit_button = tk.Button(frame, text="Analyze", command=submit)
submit_button.grid(row=1, column=1, pady=10)

root.mainloop()

