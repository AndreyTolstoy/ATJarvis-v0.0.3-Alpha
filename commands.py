#импорт библиотек
from pyglet import resource, app
from webbrowser import open as site
from os import system
from random import choice
from keyboard  import press_and_release

class Commands:
    
    bot_name = "джарвис"
    
    def __init__(self, command_name=None, activation_phrases=None, open_prg=None, open_site=None, hotkey = None, answer=None, answer2=None):
        self.command_name = command_name
        self.activation_phrases = activation_phrases
        self.open_prg = open_prg
        self.open_site = open_site
        self.hotkey = hotkey
        self.answer = answer
        self.answer2 = answer2
        
    
    
            


    def sound(name):
        sound = resource.media(name)
        sound.play()
        app.exit()
        

                  

    def opening_prg(self):
        if self.open_prg != "-":
            print(f"Открытие программы по пути {self.open_prg}")
           #subprocess.Popen(self.open_prg, shell=True)
            system(self.open_prg)

        else:
            pass

    def opening_site(self):
        if self.open_site != "-":
            print(f"Открытие сайта по пути {self.open_site}")
            site(self.open_site)
            
        else:
            pass


    def hotkey_release(self):
        if self.hotkey != "-":
           press_and_release(self.hotkey)


    def answer_choice(self):
        answers = self.answer, self.answer2
        if self.answer2 !="-":
         random_answer = choice(answers)
         print(f"Аудио ответ по пути {random_answer}")
         Commands.sound(random_answer)

        else:
         print(f"Аудио ответ по пути {self.answer}")
         Commands.sound(self.answer)
    



   
    




greeting = Commands(
    command_name="greeting",
    activation_phrases=["привет", "приветствую", f"привет {Commands.bot_name}", "здравствуй"],
    open_prg="-",
    open_site="-",
    hotkey="-",
    answer="Jarvis Sound Pack от Jarvis Desktop/Джарвис - приветствие.wav",
    answer2="Jarvis Sound Pack от Jarvis Desktop/Джарвис - приветствие (Песня целиком).wav"
)

google = Commands(
    command_name="google",
    activation_phrases=["открой гугл", "открой браузер", "гугл", "открой пожалуйста браузер", f"{Commands.bot_name} открой гугл"],
    open_prg="-",
    open_site="https://",
    hotkey="-",
    answer="Jarvis Sound Pack от Jarvis Desktop/Загружаю сэр.wav",
    answer2="Jarvis Sound Pack от Jarvis Desktop/Есть.wav"
)

music = Commands(
    command_name="music",
    activation_phrases=["включи плейлист для разработки", "хочу сделать обновление"],
    open_prg="-",
    open_site="https://youtu.be/LVbUNRwpXzw?si=f0V49TK58Lai9t9M",
    hotkey="-",
    answer="Jarvis Sound Pack от Jarvis Desktop/О чем я думал, обычно у нас все веселенькое.wav",
    answer2="Jarvis Sound Pack от Jarvis Desktop/Мы работаем над проектом сэр 2.wav"
)



open_youtube = Commands(
    command_name="open_youtube",
    activation_phrases=["открой ютуб", "ютуб", "youtube", "открой youtube"],
    open_prg="-",
    open_site="https://www.youtube.com/",
    hotkey="-",
    answer="Jarvis Sound Pack от Jarvis Desktop/Да сэр.wav",
    answer2="Jarvis Sound Pack от Jarvis Desktop/О чем я думал, обычно у нас все веселенькое.wav" 
)


open_discord = Commands(
    command_name = "open_discord",
    activation_phrases = ["discord", "открой discord", "дискорд"],
    open_prg = "None",
    open_site = "-",
    hotkey = "-",
    answer = "Jarvis Sound Pack от Jarvis Desktop/Да сэр.wav",
    answer2 = "Jarvis Sound Pack от Jarvis Desktop/О чем я думал, обычно у нас все веселенькое.wav"
)



open_telegram = Commands(
    command_name = "open_telegram",
    activation_phrases = ["telegram", "открой telegram", "открой тг"],
    open_prg = "None",
    open_site = "-",
    hotkey = "-",
    answer = "Jarvis Sound Pack от Jarvis Desktop/Да сэр(второй).wav",
    answer2 = "Jarvis Sound Pack от Jarvis Desktop/Загружаю сэр.wav"
)















#hotkey command
close_activ_window = Commands(
    command_name = "close_activ_window",
    activation_phrases = ["закрой окно", "закрыть окно", "окно закрой"],
    open_prg = "-",
    open_site = "-",
    hotkey = "alt + f4",
    answer = "Jarvis Sound Pack от Jarvis Desktop/Всегда к вашим услугам сэр.wav",
    answer2 = "Jarvis Sound Pack от Jarvis Desktop/Есть.wav")



pause = Commands(
    command_name = "pause",
    activation_phrases = ["пауза", "поставь на паузу"],
    open_prg = "-",
    open_site = "-",
    hotkey= "space",
    answer = "Jarvis Sound Pack от Jarvis Desktop/Всегда к вашим услугам сэр.wav",
    answer2 = "Jarvis Sound Pack от Jarvis Desktop/Есть.wav"

)




#search and write

write = Commands(
    command_name = "write",
    activation_phrases = ["напиши", "напиши текст", "диктую"],
    open_prg = "-",
    open_site = "-",
    hotkey = "-",
    answer="Jarvis Sound Pack от Jarvis Desktop/Есть.wav",
    answer2="Jarvis Sound Pack от Jarvis Desktop/Да сэр.wav"
)


