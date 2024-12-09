from my_pyacastudy.audio_func_lib import GetAudioFilePitch
from my_pyacastudy.compute_pitch import file_entry
import argparse

def test_is_pure_sinewave():
    assert GetAudioFilePitch == 441

def test_is_not_pure_sinewave():
    assert GetAudioFilePitch != 441

def test_pitch():

    parser = argparse.ArgumentParser(description="File path")
    parser.add_argument("file_path", help="The path to the file")

    args = parser.parse_args()
    file_path = args.file_path

    pitch = GetAudioFilePitch(file_path)
    assert pitch == 441
    

