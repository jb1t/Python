import unittest
import morseCode

morse_code = morseCode.MorseCode()

class MorseCodeTests(unittest.TestCase):
    def testDecodeA_HandlesASingleLetter(self):
        code = morse_code.encode('a')
        self.assertEquals('. -', code)

    def testDecodeSOS_AddsThreeSpacesBetweenLetters(self):
        code = morse_code.encode('SOS')
        self.assertEquals('. . .   - - -   . . .', code)

    def testDecode_WhenThereAreTwoWords_HandlesSpace(self):
        code = morse_code.encode('Hello World')
        self.assertEquals('. . . .   .   . - . .   . - . .   - - -       . - -   - - -   . - .   . - . .   - . .', code)

    def testDecode_EveryLetterAndNumber(self):
        code = morse_code.encode('abcdefghijkl')
        self.assertEquals('. -   - . . .   - . - .   - . .   .   . . - .   - - .   . . . .   . .   . - - -   - . -   . - . .', code)
        code = morse_code.encode('mnopqrstuvwxyz')
        self.assertEquals('- -   - .   - - -   . - - .   - - . -   . - .   . . .   -   . . -   . . . -   . - -   - . . -   - . - -   - - . .', code)
        code = morse_code.encode('0123456789')
        self.assertEquals('- - - - -   . - - - -   . . - - -   . . . - -   . . . . -   . . . . .   - . . . .   - - . . .   - - - . .   - - - - .', code)

    def testDecode_TrailingSpacesAreIgnored(self):
        code = morse_code.encode('a ')
        self.assertEquals('. -', code)

    def testDecode_PreceedingSpacesAreIgnored(self):
        code = morse_code.encode(' a')
        self.assertEquals('. -', code)

    def testDecode_LettersAreNotCaseSensitive(self):
        code = morse_code.encode('Aa')
        self.assertEquals('. -   . -', code)

def main():
    unittest.main()


if __name__ == '__main__':
    main()