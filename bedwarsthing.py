import requests
import json
import time

def getData(username):
    uuid = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()["id"]
    data = requests.get(
        url = "https://api.hypixel.net/player",
        params = {
            "key": "PLACE KEY HERE", #API key
            "uuid": uuid
        }
    ).json()
    
    star = data["player"]["achievements"]["bedwars_level"]
    finals = data["player"]["stats"]["Bedwars"]["final_kills_bedwars"]
    deaths = data["player"]["stats"]["Bedwars"]["final_deaths_bedwars"]
    return [username, star, finals/deaths]


def getIgns():
    igns = []
    with open('igns.txt','r') as f:
        igns=[]
        for line in f:
            strip_lines=line.strip()
            igns.append(strip_lines)
    return igns

def format(n, lst):
    print(''.join(x.ljust(n + 2) for x in lst))

    
def maketeam():
    igns = getIgns()
    stats = []
    for ign in igns:
        data = getData(ign)
        print(data)
        stats.append(getData(ign))
        time.sleep(7)

    print("Players from best to worst: ")
    stats.sort(key=lambda x: x[1])

    # Find maximal length of all elements in list
    print(stats)

    
    print("Team A:")
    print(stats[0], "\n", stats[31], "\n", stats[8], "\n", stats[23])
    print("Average Stars: ", ((stats[0][1]+ stats[31][1] + stats[8][1] + stats[23][1])/4))
    print("Average FKDR: ", ((stats[0][2]+ stats[31][2] + stats[8][2] + stats[23][2])/4))


    print("Team B:")
    print(stats[1],"\n", stats[30], "\n",stats[9], "\n",stats[22])
    print("Average Stars: ", ((stats[1][1]+ stats[30][1] + stats[9][1] + stats[22][1])/4))
    print("Average FKDR: ", ((stats[1][2]+ stats[30][2] + stats[9][2] + stats[22][2])/4))

    print("Team C:")
    print(stats[2],"\n", stats[29],"\n", stats[10],"\n", stats[21])
    print("Average Stars: ", ((stats[2][1]+ stats[29][1] + stats[10][1] + stats[21][1])/4))
    print("Average FKDR: ", ((stats[2][2]+ stats[29][2] + stats[10][2] + stats[21][2])/4))



    print("Team D:")
    print(stats[3],"\n", stats[28],"\n", stats[11], "\n",stats[20])
    print("Average Stars: ", ((stats[3][1]+ stats[28][1] + stats[11][1] + stats[20][1])/4))
    print("Average FKDR: ", ((stats[3][2]+ stats[28][2] + stats[11][2] + stats[20][2])/4))

    
    print("Team E:")
    print(stats[4],"\n", stats[27],"\n", stats[12],"\n", stats[19])
    print("Average Stars: ", ((stats[4][1]+ stats[27][1] + stats[12][1] + stats[19][1])/4))
    print("Average FKDR: ", ((stats[4][2]+ stats[27][2] + stats[12][2] + stats[19][2])/4))



    print("Team F:")
    print(stats[5], "\n",stats[26], "\n",stats[13], "\n",stats[18])
    print("Average Stars: ", ((stats[5][1]+ stats[26][1] + stats[13][1] + stats[18][1])/4))
    print("Average FKDR: ", ((stats[5][2]+ stats[26][2] + stats[13][2] + stats[18][2])/4))



    print("Team G:")
    print(stats[6], "\n",stats[25],"\n", stats[14], "\n",stats[17])
    print("Average Stars: ", ((stats[6][1]+ stats[25][1] + stats[14][1] + stats[17][1])/4))
    print("Average FKDR: ", ((stats[6][2]+ stats[25][2] + stats[14][2] + stats[17][2])/4))



    print("Team H:")
    print(stats[7], "\n",stats[24], "\n",stats[15], "\n",stats[16])
    print("Average Stars: ", ((stats[7][1]+ stats[24][1] + stats[15][1] + stats[15][1])/4))
    print("Average FKDR: ",  ((stats[7][2]+ stats[24][2] + stats[15][2] + stats[16][2])/4))




    
    
