from functools import reduce
import random
import time
from api import API_Call

class Mixer:
    def __init__(self):
        self.api_client = API_Call()

    def transactionCheck(self,address):
        balance = self.api_client.checkTransactions(address)

    def deposit(self,withdrawl_address,amount,deposit_address):
        confirmation = self.api_client.deposit(withdrawl_address,amount,deposit_address)

    #function that calculates a list of n nums within the range of 1-total by
    def randomNums(self,n, total):
        #generate list of n-1 random numbers between 0-100 to divide by
        nums = sorted(random.sample(range(1, total), n - 1))
        return [a - b for a, b in zip(nums + [total], [0] + nums)]

    def mixer(self,balance,addressList):
        #take 3% fee for mixing
        fee = str(float(balance)*.03)
        self.api_client.deposit('House',fee,'Fee')
        balance = float(balance)-float(fee)
        balance = str(balance)
        #generates a list of percentages to divide the balance into a number of portions equal to
        #the number of addresses the user enters 
        numsList = self.randomNums(len(addressList),100)
        print('Depositing coins...')
        #runs a for loop that iterates through the address_list and deposits coins in random time increments
        for nums,addresses in zip(numsList,addressList):
            #calculates how much of the balance to deposit this time
            depositAmount = str(((float(balance)*nums)/100))
            #time to wait before depositing. room for improvement.
            time.sleep(random.randint(1,6))
            self.api_client.deposit('House',depositAmount,addresses)
    
        return
