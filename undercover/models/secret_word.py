import json
import random

wordSets = json.load(open("secretWords.json", "r", encoding='utf-8'))

class SecretWord():
    def __init__(self):
        self.related_words = random.choice(json.load(open("secretWords.json", "r", encoding='utf-8')))
    @classmethod
    def get_random(cls): 
        return cls()
