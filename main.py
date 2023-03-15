from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3

AUDIO_RATE = 16000

def start():
    # Speech Model
    model = Model('vosk-model-small-en-us-0.15')
    recognizer = KaldiRecognizer(model, AUDIO_RATE)

    # Microphone Setup
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=AUDIO_RATE, input=True, frames_per_buffer=1000)
    stream.start_stream()

    # TTS
    voice = pyttsx3.init()
    voice.say('Now listening.')
    voice.runAndWait()
 

    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()[14:-3]
            if text == 'stop listening':  # Phrase to close the program
                voice.say('Exiting')
                voice.runAndWait()
                break
            
            for word in text.split()[::-1]:  # use last word that ends in er because its fresher in memory
                if (word.endswith('er') or word.endswith('ers')) and word != 'her':
                    word = word[:len(word)-1] if word.endswith('s') else word
                    voice.say(f'{word}? I hardly know her!')
                    voice.runAndWait()
                    break

    stream.stop_stream()

if __name__ == "__main__":
    start()