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

""" Vector_say.py

Make Vector say whatever you type into the input line.
"""

import anki_vector
import sys
import asyncio
import time


def main():
    # args = anki_vector.util.parse_command_args()
    # with anki_vector.Robot(args.serial) as robot:
    with anki_vector.Robot() as robot:

        foundIt=0
        sayThis = ""

        if len(sys.argv)>1:
            for x in sys.argv:
                if (str.endswith(x,"Vector_say.py")):
                    foundIt = 1
                    continue
                if (foundIt == 1):
                    sayThis += " "
                    sayThis += x
        else:
            print
            sayThis = input("What would you like Vector to say? : ")

        print("Saying '%s'" % sayThis)
        robot.say_text(sayThis)


if __name__ == "__main__":
    main()
