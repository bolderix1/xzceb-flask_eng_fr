import unittest

import french_to_english, english_to_french

class testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(""), "") 
        self.assertNotEqual(french_to_english("Merci"), "Arrigato") 


class testenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertEqual(english_to_french(""), "") 
        self.assertEqual(english_to_french("three"), "cinq") 

unittest.main()