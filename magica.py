import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test",
                    help="Does not output result into file",
                    action="store_true")
args = parser.parse_args()

def getOption(opts, prompt, error_msg):
    got_val = False
    while not got_val:
        val = input(prompt)
        got_val = True
        try:
            opts.index(val)
        except:
            print(error_msg)
            got_val = False
    return val

name = input("Nome: ")
mtype = getOption(["Solar", "Lunar"], "Tipo (Solar/Lunar): ", "Erro: Tipo inválido")

if mtype == "Solar":
    period = getOption(["1H", "3H", "6H", "9H"], "Horário (1H/3H/6H/9H): ", "Erro: Horário inválido")
else:
    period = getOption(["Nova", "Crescente", "Cheia", "Minguante"], "Fase (Nova/Crescente/Cheia/Minguante): ", "Erro: Fase inválida")

if not args.test:
    # mf - Magic File
    with open("./magias/" + name + ".txt", "w") as mf:
        mf.write("Nome: " + name + "\n")
        mf.write("Tipo: " + mtype + "\n")
        mf.write(("Horário: " if mtype == "Solar" else "Fase: ") + period + "\n")
        mf.write("Descrição:")
