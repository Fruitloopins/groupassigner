import random
import configparser
import os

#Creating config if necessary
config = configparser.ConfigParser()
def write_file():
    config.write(open("config.ini", "w"))

if not os.path.exists("config.ini"):
    config.add_section("Settings")
    config.set("Settings", "names", "Names go here")
    config.set("Settings", "numberofgroups", "4")
    config.set("Settings", "capacities", "0 0 0 0")

    with open("config.ini", "w") as configfile:
        config.write(configfile)

#Reading settings
config.read("config.ini")

#Reading names and shuffling them
namelist = config["Settings"]["names"].split()
random.shuffle(namelist)
print("Names:", namelist)

#Reading quantity of groups
groupnumber = 0
grouplist = []
for i in range (int(config["Settings"]["numberofgroups"])):
    grouplist.append(groupnumber)
    groupnumber = groupnumber + 1
print("Number of groups:", groupnumber)

#Reading current member count of each group
capacitylist = []
capacities = config["Settings"]["capacities"].split()
for i in capacities:
    i = int(i)
    capacitylist.append(i)
print("Capacity of each group:", capacitylist, "\n")

#Goes through all names in namelist until it is empty and tries to add them to a group,
#if the group is too large it will move on to the next name and try that name later to ensure the groups stay balanced
while namelist != []:
    for name in namelist:
        choice = random.choice(grouplist)
        capacity = capacitylist[choice]
        if capacity == min(capacitylist):
            print(name, "has been assigned to group", choice + 1)
            capacitylist[choice] = capacitylist[choice] + 1
            namelist.remove(name)

print("\nFinal capacity of each group:", capacitylist)