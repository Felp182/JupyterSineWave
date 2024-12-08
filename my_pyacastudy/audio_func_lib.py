import pyACA
import statistics
import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox


def normalize_path(file_path):
    return file_path.replace("\\", "/")

def GetAudioFilePitch(file_path):

    path = normalize_path(file_path)
    if not os.path.exists(path):
         messagebox.showerror("Error", "File does not exist")
         return
       
    try:
       [f_s,afAudioData] = pyACA.ToolReadAudio(path)
       [vsf,t] = pyACA.computePitch("SpectralAcf", afAudioData, f_s)
       pitch_mean = statistics.mean(vsf)

       messagebox.showinfo("Audio Pitch value", f"The pitch is: {pitch_mean}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def CheckSoundFilePath(file_path):

    if not os.path.exists(file_path):
        print(f"Error: The file Path '{file_path}' does not exist", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a file.", file=sys.stderr)
        sys.exit(1)

    print(f"The file '{file_path}' exists and is valid.")

    return file_path

    
        