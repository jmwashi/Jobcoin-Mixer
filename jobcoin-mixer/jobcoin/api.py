import requests
from config import API_ADDRESS_URL,API_ADDRESS_URL,API_TRANSACTIONS_URL

class API_Call:
    def checkTransactions(self,address):
        thisAddress = API_ADDRESS_URL+'/'+address
        callback = requests.get(thisAddress)
        addressInfo = callback.json()
        #while loop to continuously scan for an update to the deposit address
        print('Waiting for coins to deposit...')
        while addressInfo.get('balance') == '0':
            r = requests.get(thisAddress)
            addressInfo = r.json()
        return addressInfo.get('balance')

    #function for making a POST request to deposit coins
    def deposit(self,withdrawl_address,amount,deposit_address):
        r = requests.post(API_TRANSACTIONS_URL, data = {'fromAddress':withdrawl_address,'toAddress':deposit_address,'amount':amount})
        print(r.json)
        return 0