from my_pyacastudy.audio_func_lib import GetAudioFilePitch

def test_is_pure_sinewave():
    assert GetAudioFilePitch == 441

def test_is_not_pure_sinewave():
    assert GetAudioFilePitch != 441

