import pyACA
import statistics

def GetSoundPitch(file_path):

    [f_s,afAudioData] = pyACA.ToolReadAudio(file_path)
    #computing
    [vsf,t] = pyACA.computePitch("SpectralAcf", afAudioData, f_s)

    return statistics.mean(vsf)

