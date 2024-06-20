from fastapi import APIRouter
from services.liblouis import LiblouisService

router = APIRouter()
liblouis_service = LiblouisService()

@router.get("/liblouis-translate-eng-braille-g1/")
def get_translate_eng_braille_g1(text: str) -> str:
    translated_text = liblouis_service.translate_english_to_braille_g1(text)
    return translated_text

@router.get("/liblouis-translate-eng-braille-g2/")
def get_translate_eng_braille_g2(text: str) -> str:
    translated_text = liblouis_service.translate_english_to_braille_g2(text)
    return translated_text

@router.get("/liblouis-back-translate-eng-braille-g1/")
def get_back_translate_eng_braille_g1(text: str) -> str:
    back_translated_text = liblouis_service.back_translate_english_to_braille_g1(text)
    return back_translated_text

@router.get("/liblouis-back-translate-eng-braille-g2/")
def get_back_translate_eng_braille_g2(text: str) -> str:
    back_translated_text = liblouis_service.back_translate_english_to_braille_g2(text)
    return back_translated_text

@router.get("/liblouis-translate-zhuyin-tw/")
def get_translate_zhuyin_tw(text: str) -> str:
    translated_text = liblouis_service.translate_zhuyin_tw_to_braille(text)
    return translated_text
