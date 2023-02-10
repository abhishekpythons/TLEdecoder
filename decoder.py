import requests
import pandas as pd

class Decoder:
    """decoder for satellites tle by norad id"""
    def __init__(self, norad_id):
        self.norad_id = norad_id
        self.df = pd.DataFrame()
        response = requests.get("https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle")
        content = str(response.content).split('\\r\\n')
        self.df

    def decode(self):
        print(self.data)

if __name__ == '__main__':
    d = Decoder(51589)
    d.decode()

        
