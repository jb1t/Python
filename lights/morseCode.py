import time
import consoleLightsDAO

__author__ = 'jeffgarrison'

lights = consoleLightsDAO.ConsoleLightsDAO()


class MorseCode:

    def __init__(self):
        self.unit = 0.5
        self.dot = '.'
        self.dash = '-'
        self.time_btw_part_of_letters = self.unit
        self.time_btw_letters = 3 * self.unit
        self.time_btw_words = 7 * self.unit
        self.dash_time = 3 * self.unit
        self.dot_time = self.unit

        self.alphabet = {
            'A': [self.dot, self.dash],
            'B': [self.dash, self.dot, self.dot, self.dot],
            'C': [self.dash, self.dot, self.dash, self.dot],
            'D': [self.dash, self.dot, self.dot],
            'E': [self.dot],
            'F': [self.dot, self.dot, self.dash, self.dot],
            'G': [self.dash, self.dash, self.dot],
            'H': [self.dot, self.dot, self.dot, self.dot],
            'I': [self.dot, self.dot],
            'J': [self.dot, self.dash, self.dash, self.dash],
            'K': [self.dash, self.dot, self.dash],
            'L': [self.dot, self.dash, self.dot, self.dot],
            'M': [self.dash, self.dash],
            'N': [self.dash, self.dot],
            'O': [self.dash, self.dash, self.dash],
            'P': [self.dot, self.dash, self.dash, self.dot],
            'Q': [self.dash, self.dash, self.dot, self.dash],
            'R': [self.dot, self.dash, self.dot],
            'S': [self.dot, self.dot, self.dot],
            'T': [self.dash],
            'U': [self.dot, self.dot, self.dash],
            'V': [self.dot, self.dot, self.dot, self.dash],
            'W': [self.dot, self.dash, self.dash],
            'X': [self.dash, self.dot, self.dot, self.dash],
            'Y': [self.dash, self.dot, self.dash, self.dash],
            'Z': [self.dash, self.dash, self.dot, self.dot],
            '0': [self.dash, self.dash, self.dash, self.dash, self.dash],
            '1': [self.dot, self.dash, self.dash, self.dash, self.dash],
            '2': [self.dot, self.dot, self.dash, self.dash, self.dash],
            '3': [self.dot, self.dot, self.dot, self.dash, self.dash],
            '4': [self.dot, self.dot, self.dot, self.dot, self.dash],
            '5': [self.dot, self.dot, self.dot, self.dot, self.dot],
            '6': [self.dash, self.dot, self.dot, self.dot, self.dot],
            '7': [self.dash, self.dash, self.dot, self.dot, self.dot],
            '8': [self.dash, self.dash, self.dash, self.dot, self.dot],
            '9': [self.dash, self.dash, self.dash, self.dash, self.dot]
        }

    def encode(self, text):
        upper_text = text.upper()
        encoded_string = ""
        for letter in upper_text:
            if letter == ' ':
                encoded_string += '    '
            else:
                for code in self.alphabet[letter]:
                    encoded_string += code + " "
                encoded_string += "  "
        return encoded_string.strip()

    def blinkLEDs(self, encode_string):
        for code in encode_string:
            if code == '.':
                lights.turn_all_on()
                time.sleep(self.dot_time)
                lights.turn_all_off()
            elif code == '-':
                lights.turn_all_on()
                time.sleep(self.dash_time)
                lights.turn_all_off()
            elif code == ' ':
                time.sleep(self.unit)