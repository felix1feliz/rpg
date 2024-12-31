import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--points",
                    help="Quantity of stats points",
                    type=int)
parser.add_argument("-H", "--health",
                    help="Quantity of health",
                    type=int)
args = parser.parse_args()

name = input("Nome: ")
valid_races = ["Alto", "Anão", "Elfo", "Goblin"]
got_race = False

while not got_race:
    race = input("Raça (Alto/Anão/Elfo/Goblin): ")
    got_race = True
    try:
        valid_races.index(race)
    except:
        print("Erro: Raça invalida")
        got_race = False

status_points = (args.points or random.randrange(16, 24))
print("Você tem", status_points, "para gastar em status")
print("Os status são:\n - Força\n - Destreza\n - Agilidade\n - Percepção\n - Carisma\n")

def intput(prompt):
    ret = 0
    is_int = False
    while not is_int or ret < 0:
        if ret < 0:
            print("Erro: Valor não pode ser negativo")
        inp = input(prompt)
        is_int = True
        try:
            ret = int(inp)
        except:
            print("Erro: Valor não é númerico")
            ret = 0
            is_int = False
    return ret

def getstat(prompt, status_points):
    print("(", status_points, ")")
    ret = intput(prompt)
    while ret > status_points:
        print("Erro: Valor maior que pontos de status")
        print("(", status_points, ")")
        ret = intput(prompt)
    return ret, status_points - ret

strength, dexterity, agility, perception, rizz = 0, 0, 0, 0, 0
done = False

while status_points != 0:
    if done:
        print("Erro: Todos os pontos de status devem ser utilizados")
    
    status_points += strength
    strength, status_points = getstat("Força: ", status_points)
    status_points += dexterity
    dexterity, status_points = getstat("Destreza: ", status_points)
    status_points += agility
    agility, status_points = getstat("Agilidade: ", status_points)
    status_points += perception
    perception, status_points = getstat("Percepção: ", status_points)
    status_points += rizz
    rizz, status_points = getstat("Carisma: ", status_points)
    done = True

health = (args.health or 20)

with open("./personagens/" + name + ".txt", "w") as character_file:
    character_file.write("Nome: " + name + "\n")
    character_file.write("HP: " + str(health) + "/" + str(health) + "\n")
    character_file.write("Raça: " + race + "\n")
    character_file.write("Força: " + str(strength) + "\n")
    character_file.write("Destreza: " + str(dexterity) + "\n")
    character_file.write("Agilidade: " + str(agility) + "\n")
    character_file.write("Percepção: " + str(perception) + "\n")
    character_file.write("Carisma: " + str(rizz) + "\n")

