import pyACA
import statistics
import argparse
import os
import sys

parser = argparse.ArgumentParser(description="File Path.")
parser.add_argument("file_path", help= "The path to the file.")

args= parser.parse_args()
file_path = args.file_path


if not os.path.exists(file_path):
    print(f"Error: The file Path '{file_path}' does not exist", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(file_path):
    print(f"Error: '{file_path}' is not a file.", file=sys.stderr)
    sys.exit(1)

print(f"The file '{file_path}' exists and is valid.")


#Reading passed file
[f_s,afAudioData] = pyACA.ToolReadAudio(file_path)

#computing
[vsf,t] = pyACA.computePitch("SpectralAcf", afAudioData, f_s)

print(statistics.mean(vsf))

