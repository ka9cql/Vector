#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Vector_volts.py

Make Vector speak his battery voltage
"""

import anki_vector
import sys
#import asyncio
#import time

# 100% full -   Battery voltage: (4.079956 - 4.032776)
# 75% full -    Battery voltage: ??
# 50% full -    Battery voltage: ??
# 25% full -    Battery voltage: ??
# ALMOST DEAD - Battery voltage: (3.602064609527588 - 3.6050970554351807)
# DEAD -        Battery voltage: 

# Presumed "linear" region -
FULL_BATT = 4.079956
AD_BATT   = 3.602065

pct_full_only=False


def calcBatteryPercent(bv):

    available_region=(FULL_BATT-AD_BATT)
    range_pos=(bv-AD_BATT)
    truncVal = float('%.f' % float(range_pos/available_region*100.0))

    # show the battery voltage
    print("Current battery voltage: %s" % bv)
    if bv > FULL_BATT:
        print("Probably on charger")
    elif bv > AD_BATT:
        print("Estimated: {0}% full".format(truncVal))
    else:
        print("**** Need to recharge! ****   ALMOST DEAD!   (Only a few minutes left!)")

    return truncVal



def main():

    with anki_vector.Robot() as robot:

        battery_state = robot.get_battery_state()
        if battery_state:
            # print("Vector's Battery Voltage: {0}".format(battery_state.battery_volts))

            pct = calcBatteryPercent(battery_state.battery_volts)

            sayThis = "My battery is "
            sayThis += "{0}".format(pct)
            sayThis += " percent full"

            print("\n\n\tSaying '%s'\n\n" % sayThis)
            robot.say_text(sayThis)


if __name__ == "__main__":
    main()
