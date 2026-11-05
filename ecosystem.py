print("Hello ecosystem!")

import time

from apex import Apex
from primary import Primary
from secondary import Secondary


Apex = Apex()
Primary = Primary()
Secondary = Secondary()


def reproduce(Primary, Secondary):
    Primary.amount += Primary.amount * Primary.reproduction
    Secondary.amount += Secondary.amount * Secondary.reproduction

def eat():
    pass


def death():
    pass

def adjust():
    pass

def readout(tier):
    print(f"\t{tier.amount} primaries")
    print(f"\t{tier.reproduction * 100}% reproduction rate")
    print(f"\t{tier.death_rate * 100}% death rate")

def ecosystem(Apex, Primary, Secondary):
    
    while True:
        reproduce(Primary, Secondary)
        eat()
        death()
        adjust()
        print("Primary")
        readout(Primary)
        print("Secondary")
        readout(Secondary)
        time.sleep(2)

ecosystem(Apex, Primary, Secondary)
