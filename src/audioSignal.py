import pydub 
import simpleaudio as sa

def test_LMS_Using_Audio_Signal():
    file = 'audio_desiredSignal.mp3'
    sr, x = read(file)
    print(x)

def read(f, normalized=False):
    """MP3 to numpy array"""
    a = pydub.AudioSegment.from_mp3(f)
    y = np.array(a.get_array_of_samples())
    if a.channels == 2:
        y = y.reshape((-1, 2))
    if normalized:
        return a.frame_rate, np.float32(y) / 2**15
    else:
        return a.frame_rate, y