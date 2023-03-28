import sys
import random

class Wordle:
    def __init__(self, index = 0) -> None:
        self.nattempts = 6
        self.dict = self.get_dict(index)
        self.key = self.get_key()
        self.current_state = "_____"
        self.current = None

    def get_dict(self, index):
        dict_list = ["/dict/common-words",
                     "/dict/gre-words"]
        with open(dict_list[index], "r") as file:
            word_list = [word for word in file]
        word_list = [word.replace("\n", "") for word in word_list]
        return word_list
    
    def get_key(self):
        key = self.dict[random.randint(0,len(self.dict)-1)]
        while(len(key) != 5):
            key = self.get_key()
    
        return key
    
    def print_title(self):
        print("""\nWordle (Difficulty: easy)
You have 6 attempts to guess a 5-letter word.
(Enter lowercase letters only.)\n""")
    
    def update_current_state(self, input_string):
        for i in range(len(input_string)):
            if(input_string[i] in self.key):
                j = self.key.index(input_string[i])
                new_character = input_string[i]
                self.current_state = self.current_state[:j] + new_character + self.current_state[j+1:]

    def play_game(self):
        self.print_title()
        while (self.nattempts > 0):
            curr_word = input(self.current_state + "\r")
            self.update_current_state(curr_word)
            if (self.current_state == self.key):
                print("Success! You guessed the word in", 7 - self.nattempts, " attempt(s)!" )
                break
            self.nattempts -= 1
        else:
            print("\nBetter luck next time! The word was", self.key, "\n")

if(len(sys.argv) == 1):
    dict_index = 0
else:
    dict_index = int(sys.argv[1])

new_game = Wordle(dict_index)
        

