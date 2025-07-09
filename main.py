import random

print("Welcome to the game Hangman")

print(r"""
    _    _                                             
   | |  | |                                            
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __      
   |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \     
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |    
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|    
                        __/ |                          
                       |___/                           
""")

allowed_tries = random.randint(5, 10)
print(allowed_tries)
