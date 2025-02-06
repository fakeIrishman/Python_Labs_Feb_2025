#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: This is a Game of Tanks
"""
   GOT - Game of tanks
"""
import tank
import sys

def main():
    # Instantiate/Create 3 tank objects

    erik_tank = tank.Tank("german", "tiger")
    zane_tank = tank.Tank("american", "sherman")
    aram_tank = tank.Tank("british","churchill")

    # And the game begins

    erik_tank.accel(61)
    zane_tank.accel(44)

    aram_tank.rotate_left(289)
    aram_tank.accel(31)
    aram_tank.shoot()

    erik_tank.take_damage(37)
    zane_tank.take_damage(49)

    print (f"Health of Erik's tank is {erik_tank._health}")

    print (f"Status of Erik's and Zane's tank is {erik_tank + zane_tank}")

    # Erik gets a health boost
    # erik_tank.set_health (100) #setter
   #  print(f"New health of Erik's Tank is {erik_tank.get_health()}") # getter
    erik_tank.tank_health = 100
    print(f"New health of Erik's Tank is {erik_tank.tank_health}")

    return None




if __name__ == "__main__":
    main()
    sys.exit(0)

