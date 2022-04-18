#!/usr/bin/python3
# Main display
#
# It's 2022, and I seriously don't know what i'm doing.
# good god this will be messy
#

# Import all the things.
# Ok, only the necessary stuff.

import tkinter
# At somepoint, I'll figure how to give this a UI

priorities = {a, b, c, d, e}
sections = {Attributes, Nuyen, Magic, Race, Skills}
charPri = {}

print("""
======================
Choose Priority Values
======================
""")
print("Priorities Available:" + priorities)
charPri.append = input(sections[0] + ": ")
if charPri[0] in priorities:
    print(sections[0] + "is set to Priority" + charPri[0])
    priorities.remove[charPri[0]]