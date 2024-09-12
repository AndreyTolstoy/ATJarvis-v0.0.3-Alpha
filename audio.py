import speech_recognition
from colorama import Fore, Style

def listen():
 with speech_recognition.Microphone() as mic:    
        
        try:
         print("Слушаю...")
         sr = speech_recognition.Recognizer()
         sr.pause_threshold = 0.5
         sr.adjust_for_ambient_noise(source=mic, duration=0.5)
         audio = sr.listen(source=mic)
         query = sr.recognize_google(audio_data=audio, language='ru-RU,eng-Eng').lower()
         print(f"Вы сказали: {query}")
         
         return query
        
        except Exception:
           print(Fore.RED, Style.BRIGHT + f"Jarvis: Не понимаю, что вы говорите?" + Style.RESET_ALL)
         


