#%%
import pyACA
import matplotlib.pyplot as plt
import numpy as np

#file to analyze
cPath = "test.wav"
[f_s,afAudioData] = pyACA.ToolReadAudio(cPath)

#computing
[vsf,t] = pyACA.computePitch("SpectralAcf", afAudioData, f_s)

plt.plot(t, np.squeeze(vsf))
# %%
