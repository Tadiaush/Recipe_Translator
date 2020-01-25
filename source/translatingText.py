from translate import Translator

def translating(textList):
    translator = Translator(to_lang='eng', from_lang='swe')
    translatedText = list()
    for text in textList:
        translatedText.append(translator.translate(text))

    return translatedText

