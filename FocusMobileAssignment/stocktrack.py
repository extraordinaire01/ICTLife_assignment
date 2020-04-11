import bs4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re
import html.parser
import csv
from googletrans import Translator

class StockTrack(object):
    """Provided a stock symbol find its current price."""
    def __init__(self, symbol, preferred_language, preferred_currency):
        super(StockTrack, self).__init__()
        self.symbol = symbol
        self.preferred_language = preferred_language
        self.preferred_currency = preferred_currency
        self.stockprice = {}
        self.languages = {}
        self.supportedCurrency = {}
        self.currencylayer_accesskey = "189de90f4e628614d07092e5467483a2"
        self.fixeraccesskey = "d3024595d962553e437d1c9a6948dc55"

    def readAvailableLanguages(self):
        with open('Cheap.Stocks.Internationalization.Languages.csv', newline='') as csvfile:
           reader = csv.DictReader(csvfile)
           #headers = next(reader) SKIP HEADERS
           for row in reader:
               language = row["Language"]
               iso_code = row["ISO 639-1 code"]
               self.languages[iso_code] = language
        return self.languages

    def readAvailableCurrencies(self):
        with open('Cheap.Stocks.Internationalization.Currencies.csv', newline='') as csvfile:
           reader = csv.DictReader(csvfile)
           #headers = next(reader) SKIP HEADERS
           for row in reader:
               country = row["Country"]
               currency = row["Currency"]
               code = row["ISO 4217 Code"]
               self.supportedCurrency[country] = currency
               self.supportedCurrency[code] = code
        return self.supportedCurrency

    def createGoogleQuery(self):
        #CONSTRUCT THE GOOGLE QUERY AND SUBMIT QUERY
        url = "https://www.google.com/search?tbm=fin&q={}".format(self.symbol)
        #print (url)
        try:
            req = Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0')
            resp = urlopen(req)
            html = resp.read().decode('utf-8')
            return html
        except:
            print("Error Opening the Url")

    def processGoogleQuery(self):
        #PROCESS THE RESULTS OF THE QUERY USING REGEX
        unprocessed_query = self.createGoogleQuery()
        pattern = '><span class="(.*?)" jsdata="(.*?)" jsname="(.*?)">(?:\d+(?:\.\d*)?|\.\d+)'
        list_of_items = re.search(pattern, unprocessed_query)
        if list_of_items:
            span_with_price = list_of_items.group(0)
            price = span_with_price[-6:]
            self.stockprice['name'] = self.symbol
            self.stockprice['current_price'] = '{} USD'.format(price)
            return self.stockprice
        else:
            error = "Invalid stock symbol: {}".format(self.symbol)
            return error

    def getConversationRateLayer(self):
        url = "http://apilayer.net/api/live?access_key={}&currencies={}&source=USD&format=1".format(self.currencylayer_accesskey, self.preferred_currency)
        req = requests.get(url)
        rate_data = req.json()
        if rate_data['success'] == False:
            error = 'Query failed'
            return error
        else:
            rate = rate_data['quotes']['USD{}'.format(self.preferred_currency)]
            return rate





#GOOGLE IMPLEMENTATION
# input = input ("Enter stock symbol (kindly note only USA Stocks eg aapl) :")
# preferred_language = input ("What is your preferred language:")
# preferred_currency = input ("What is your preferred currency:")
# stockprice = StockTrack(input, preferred_language, preferred_currency)
# results = stockprice.getConversationRateLayer()
# print (results)



# #YAHOO IMPLEMENTATION
# input = input ("Enter stock symbol :")
#stockprice = StockTrack(input)
# results = stockprice.processYahooQuery()
# print (results)


def getConversationRateLayer():
    url = "http://apilayer.net/api/live?access_key=189de90f4e628614d07092e5467483a2&currencies=DZD&source=USD&format=1"
    req = requests.get(url)
    rate_data = req.json()
    if rate_data['success'] == False:
        error = 'Query failed'
        return error
    else:
        rate = rate_data['quotes']['USDDZD']
        return rate


def getConversationRateFixer():
    #FOR THE FREE PLAN, BASE USD IS NOT SUPPORTED THUS FOR OUR APP ITS NOT HELPFUL
    url = "http://data.fixer.io/api/latest?access_key=bf1169a26f96a42fa5ac213e45b19196&base=USD&symbols=DZD"
    req = requests.get(url)
    rate_data = req.json()
    if rate_data['success'] == False:
        error = 'Query failed'
        return error
    else:
        rate = rate_data['quotes']['USDDZD']
        return rate

def convertLanguageToPreferred():
    response = "The current price for"
    translator = Translator()
    result = translator.translate(response, dest='fr')
    return result


result = convertLanguageToPreferred()
print(result)