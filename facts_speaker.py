import pyttsx3
from time import  sleep
import randfacts

engine =pyttsx3.init()
try:
    for i in range(1000):
        x = randfacts.get_fact(True)
        print(x)
        engine.say(x)
        engine.runAndWait()
        sleep(2)
except DeprecationWarning:
    pass
except KeyboardInterrupt:
    pass
