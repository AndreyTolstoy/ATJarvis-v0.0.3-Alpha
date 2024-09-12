#Библиотеки
from datetime import datetime


#Мои модули
from commands import *
from jsons import json_load
from audio import listen
from write import writing



    

class Receive_and_process:
   def main():
       time_now= float(datetime.now().strftime("%H:%M").replace(":","."))
       if int(str(time_now).split(".")[0]) < 10:
           Commands.sound("Jarvis Sound Pack от Jarvis Desktop/Доброе утро.wav")
         
       
       data = json_load("path.json")
       #print(data)
       while True:
         rec_commands = listen()
         
         commands = [greeting, google, music,  open_youtube, open_discord, open_telegram,  close_activ_window, pause, write]  


         for command in commands:    
                 if rec_commands in command.activation_phrases:
                    print("Распознана команда: ", command.command_name)

                    if command.open_prg == "None":
                        #print(command.command_name)
                        open_prog_list = {command.command_name : data[command.command_name]}
                        print(open_prog_list[command.command_name])
                        command.open_prg = open_prog_list[command.command_name]
                        
                    #elif command.command_name == "search_in_youtube":
                        #youtube()

   
                    
                    elif command.command_name == "write":
                       writing()
                       
                    command.opening_prg(),
                    command.opening_site(),
                    command.hotkey_release(),
                    command.answer_choice()
                 
                    






           

