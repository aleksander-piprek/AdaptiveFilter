import src.analogSignal as analogSignal 
import src.photoSignal as photoSignal
import src.audioSignal as audioSignal

def test():
    analogSignal.test_LMS_Using_Sine_Signal()
    audioSignal.test_LMS_Using_Audio_Signal()
    photoSignal.test_LMS_Using_Photo()

def main():
    test()

if __name__ == "__main__":
    main()