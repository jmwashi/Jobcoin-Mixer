#!/usr/bin/env python
import uuid
import sys

import click
import requests
from jobcoin import jobcoin

@click.command()
def main(args=None):
    print('Welcome to the Jobcoin mixer!\n')
    while True:
        addresses = click.prompt(
            'Please enter a comma-separated list of new, unused Jobcoin '
            'addresses where your mixed Jobcoins will be sent.',
            prompt_suffix='\n[blank to quit] > ',
            default='',
            show_default=False)
        if addresses.strip() == '':
            sys.exit(0)
        deposit_address = uuid.uuid4().hex
        click.echo(
            '\nYou may now send Jobcoins to address {deposit_address}. They '
            'will be mixed and sent to your destination addresses.\n'
              .format(deposit_address=deposit_address))
        thisMixer = jobcoin.Mixer()
        balance = thisMixer.transactionCheck(deposit_address)
        deposit = thisMixer.deposit(deposit_address,balance,'House')
        #splits the string into list of addresses for easier parsing
        addresses= addresses.split(",")
        thisMixer.mixer(balance,addresses)


if __name__ == '__main__':
    sys.exit(main())
