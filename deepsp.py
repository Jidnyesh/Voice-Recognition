from deepspeech import Model
import scipy.io.wavfile as wav
import os
import pyaudio

path=os.path.abspath(".")
BEAM_WIDTH = 500
LM_WEIGHT = 1.50
VALID_WORD_COUNT_WEIGHT = 2.10
N_FEATURES = 26
N_CONTEXT = 9

deep= Model(path+"/models/output_graph.pb",
N_FEATURES,
N_CONTEXT,
path+"/models/alphabet.txt",
BEAM_WIDTH)

fs,audio=wav.read(path+"/male.wav")
deep.stt(audio, fs)