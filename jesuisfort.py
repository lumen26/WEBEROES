import json
class JeSuisFort:
    def __init__(self, client):
        """
        client is used to issue orders
        """
        self.client = client
        self.total_aapl = 0
        self.count_aapl = 0
        self.previous_price = 0

    def process_candle(self, candle_msg:str):
        """This function is called when a new candle_msg is received.
            Candle message is a string of the form:
            'symbol_key' : {'c': [174.3], 'h': [174.3], 'l': [174.19], 'o': [174.19], 's': 'ok', 't': [1643670000], 'v': [1888]}

            Note that there are list, so you can have multiple candles in one message.
        """
        candle_dict = json.loads(candle_msg)
        for k, v in candle_dict.items():
            if v['c'] <100 and self.client.money>v['c']:
                self.client.buy(k,1)
                self.stock= v['c']
            if v['c'] >250  and self.client.actions[k]>1 and v['c']>self.stock:
                self.client.sell(k,1) 
         
            

               