To run through terminal:
source venv/bin/activate
pip3 install -r requirements.txt
python3 cli.py


 
When waiting for deposit coins appears, copy the address posted in terminal and deposit coins to it
When prompt appears again, refresh the page and see the coins have been deposited(should add a done print line to notify the user)


Code is commented explaining everything. Heavy lifting is in jobcoin.py. cli.py just calls the functions and gets input

Primarily works by dividing the balance of coins into blocks through a list of random percentages(as long as the number of deposit addresses entered) adding up to 100% and dispersing over time

One major change I would make in an actual mixer is the way I did time. It is the simplest way to do it by sleeping(used seconds for testing purposes but a real mixer should use a longer amount of time), but i would most likely use a sort of time/date array of the same length as the amount of addresses and when the systems time/date is equal to n index in the array I'd deposit.