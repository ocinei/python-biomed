class Suncas:
    
    def __init__(self, cute = False, sound_volume = 30):
        self.cute = cute
        self.sound_volume = sound_volume
        if self.sound_volume > 100:
            raise ValueError("Sound volume cannot be greater than 100")
    
    def speak(self):
        speech = ["Suncas suncas! \n"] * self.sound_volume
        speech = ''.join(speech)
        print(speech)
        return None
    
    def is_cute(self):
        if self.cute:
            print("Cuteness overload for this Suncas")
        else:
            print("Suncas is not cute!")
        return None
    
    def mea(self):
        print("Suncas hates MEA")
        return None

