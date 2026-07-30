import unicodedata
import re


def normalize_str(string :str) -> str:
    INVALID = r'[<>:"/\\|?*\x00-\x1F]'
    
    string = unicodedata.normalize("NFC", string)
    string = re.sub(INVALID, "", string)
    string = re.sub(r"\s+", " ", string)
    string = string.strip().rstrip(".")

    #print(string)

    return string
    
