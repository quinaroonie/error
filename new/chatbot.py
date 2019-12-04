import os
import random
import flask
import flask_socketio
import models



class Chatbot():
    def __init__(self):
        return 

    
    def get_chatbot_response(self, message):
        if message[:2] != "!!":
            return ''
        
        kquotes = ["'Although the butterfly and the caterpillar are completely different, they are one and the same.' - TPAB", 
        "Don't you know your imperfections is a wonderful blessing? - ", 
        "I'd rather not live like there isn't a God, then die and find out there really is. Think about it. - Faith",
        "Build your own pyramids, write your own hieroglyphs. - GKMC",
        "Hip-hop is not the problem. Our reality is the problem of the situation. This is our music. This is us expressing ourselves."]
        
        anquotes = ["'Could be an organ donor the way I give up my heart. - Happy Valentine's Day",
        "'Real guys go for a real down to Mars girls.' - Roses",
        "... We on our back staring at the stars above/Talking bout what we gonna be when we grow up/I said what you wanna be, she said, Alive' — Da art of storytellin'",
        "I hope we feel like this forever/Forever, forever ever, forever ever?/Forever never seems that long until you’re grown - Ms. Jackson"
        "When I shoot the moon, high jump the broom - International Player’s Anthem (I Choose You)" ]
        
        alquotes = ["Smoking on this dro, you don’t care/ You don’t judge me, you love me/ That’s why I keep you near - Pop",
        "I might just read a book don’t need no cable/ And everything stays where I leave it/ Every damn rule I created - New Apartment",
        "I said you hell of a drug/ Been gone long/ I’m gonna give you my love - Facetime",
        "I wanna kiss you again/ (?) thirsty for shady men - Speak to me",]
        
        
        points, command, args = message.split(' ', 2)
        if command == "Hey":
            return "wazzzup"
        elif command == "How are you?":
            return "just coolin"
        elif command == "what’s 's your favorite song?":
            return "right now it is Cash Race by Tinashe"
        elif command == "how old are you?":
            return "old enough."
        elif command == "who are you?":
            return "I am a the music_bot_3000"
        elif command == "Give me a musical suggestion":
            return "Listen to some more Ari Lennox"
        elif command == "Whats your favorite genre?":
            return "r&b"
            
        elif command == "Kendrick lamar quotes":
            return random.choice(kquotes)
            
        elif command == "Andre 3000 quotes":
            return random.choice(anquotes)
        
        elif command == "Ari Lennox quotes":
            return random.choice(alquotes)
            
            
            
        else:
            return "Oops! I didn't recognize your command :("