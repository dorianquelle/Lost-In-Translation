from googletrans import Translator
from langdetect import detect, DetectorFactory
import os

translator = Translator()
def safe_detect_google(x):
    try:
        return translator.detect(x).lang
    except:
        return "NO LANUAGE DETECTED"
    
def safe_translate(t):
    # Check whether t is None or empty. 
    if not t or t == " " or not isinstance(t,str):
        return ""
    try: # Very rarely the translate fails. 
        if len(t) > 4999:
            split,splits = 0,[]
            while len(t) - split > 4999:
                split = split + np.where(np.array(list(t[split:split+5000])) == " ")[0][-1]
                splits.append(split)
        else:
            # If smaller than 5000 => just translate
            return translator.translate(text=t).text
        
        # Append 0 and end to splits to have first and last break
        splits = [0] + splits + [len(t)]
        
        # Depending on if we were able to detect the language 
        # List comprehension of translations; Then joined into one string. 
        return " ".join([translator.translate(text=t[splits[i]:splits[i+1]]).text for i in range(len(splits)-1)])
    except:
        return "" # If all fails.