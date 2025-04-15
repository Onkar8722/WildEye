import sounddevice as sd
import numpy as np
import pickle
import librosa

model = pickle.load(open("models/model.pkl", "rb"))

DURATION = 2
SAMPLE_RATE = 22050


def run_gunshot_detection():
    try:
        audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
        sd.wait()

        mfccs = librosa.feature.mfcc(y=audio.flatten(), sr=SAMPLE_RATE, n_mfcc=40)
        mfccs = np.mean(mfccs.T, axis=0).reshape(1, -1)

        prediction = model.predict(mfccs)
        return "Gunshot" if prediction[0] == 1 else "No Gunshot"
    except Exception as e:
        return f"Error: {str(e)}"
