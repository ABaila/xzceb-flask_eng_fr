'''
Resolution of the project for the
IBM's Skills Network specialization
"Applied Software Engineering
Fundamentals Specialization"
'''

from deep_translator import MyMemoryTranslator



def english_to_french(english_text):
    '''
    Takes a string with english text, uses
    MyMemory Translator to translate it to
    french and returns the french translation.

            Parameters:
                    english_text (str): Input string with English text

            Returns:
                    french_text (str): String with automated translation to French
    '''
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''
    Takes a string with french text, uses
    MyMemory Translator to translate it to
    english and returns the english translation.

            Parameters:
                    french_text (str): Input string with French text

            Returns:
                    english_text (str): String with automated translation to English
    '''
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
