import random, string

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEAD)" % self.name

    def fire_at(self, enemy):
        
        if self.ammo >= 1:
            self.ammo -= 1
            print("[" + self.name + "] fires on [" + enemy.name + "]")
            enemy.hit()
        else:
            print("[" + self.name + "] is out of ammo!")

    def hit(self):
        if self.alive == False:
            print("Don't waste your ammo. [" + self.name + "] is already dead!")
        else:
            self.armor -= 20
            print("[" + self.name + "] is hit")
            if self.armor <= 0:
                self.explode()

    def explode(self):
        self.alive = False
        print("[" + self.name + "] was destroyed!")

## Lógica do jogo

# Seleciona o número de jogadores
while True:
    tanksQty = int(input("Insert the number of players, from 2 to 10\n"))
    if tanksQty <= 10 and tanksQty >= 2:
        break
    print("Invalid number, try again!\n")

alphabet = list(string.ascii_lowercase)
tanksList = {}

# Cria os tanques
i = 0
while i < tanksQty:
    while True:
        tankName = input("Insert your tank's name\n")
        if tankName != "":
            break
        else:
            print("Your tank's name can't be empty. Please try again.")
    tanksList.update({alphabet[i]:Tank(tankName)})
    i += 1

# Guarda as keys de tanksList
keys = []
for k in tanksList.keys():
    keys.append(k)

# Inicia a partida e executa cada rodada
i = 1
while len(tanksList) > 1:
    print("\n==========\nRound ", i)

    # Exibe Lista de Jogadores Vivos
    j = 0
    print("\n+++ Players Alive +++")
    while j < len(tanksList):
        playerName = tanksList.get(keys[j]).name
        playerArmor = tanksList.get(keys[j]).armor
        print(keys[j], " -> ", playerName, " --- Armor: ", playerArmor)
        j += 1

    # Sorteia o jogador da rodada
    randomNum = random.randint(0, len(tanksList)-1)
    roundTank = tanksList.get(keys[randomNum])

    # Recebe a escolha do alvo
    print("\nNext shooter is: ", roundTank.name)
    while True:
        targetName = input("Choose your target by typing its letter!\n")
        target = tanksList.get(targetName)
        # Checa se o alvo é o jogador da rodada
        if target != roundTank:
            break
        else:
            print("You can't target yourself! Choose another target.")

    # Efetua o disparo
    
    print("\n> Attack >")
    roundTank.fire_at(target)

    # Verifica se o tanque atingido foi destruído
    if target.alive == False:
        tanksList.pop(targetName)
        keys.remove(targetName)

    i += 1

# Identifica vencedor
for value in tanksList.values():
    winner = value
print("Game over! The winner is: ", winner.name)
