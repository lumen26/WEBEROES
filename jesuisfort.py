class JeSuisFort:

    def __init__(self):
        self.money = 100000

    def process_candle(self, candle_msg:str):
        """This function is called when a new candle_msg is received.
            Candle message is a string of the form:
            'symbol_key' : {'c': [174.3], 'h': [174.3], 'l': [174.19], 'o': [174.19], 's': 'ok', 't': [1643670000], 'v': [1888]}

            Note that there are list, so you can have multiple candles in one message.
        """

    def gains(self):
        return self.money