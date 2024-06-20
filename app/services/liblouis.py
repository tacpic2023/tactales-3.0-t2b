# from config import backTranslateString, translateString
import louis


class LiblouisService:
    def __init__(self):
        pass

    def translate_english_to_braille_g1(self, text):
        return louis.translateString(["braille-patterns.cti", "en-us-g1.ctb"], text)

    def back_translate_english_to_braille_g1(self, text):
        return louis.backTranslateString(["braille-patterns.cti", "en-us-g1.ctb"], text)
    
    def translate_english_to_braille_g2(self, text):
        return louis.translateString(["braille-patterns.cti", "en-us-g2.ctb"], text)

    def back_translate_english_to_braille_g2(self, text):
        return louis.backTranslateString(["braille-patterns.cti", "en-us-g2.ctb"], text)
    
    def translate_zhuyin_tw_to_braille(self, text):
        return louis.translateString(["braille-patterns.cti", "zh-tw.ctb"], text)