import time, random, sys, os, platform

def LimpaTela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

LimpaTela()
print("Saia do labirinto!!!")
nomeInput = input("Qual o nome do seu personagem? ")

acertos = 0
erros = 0
mochila = {"Pocoes de Vida": 3}
mochila["Pocoes de Forca"] = 0
surpresa = 0


def GameOver():
    print("Fim de Jogo!")
    sys.exit()

def GameWin():
    print("Você conseguiu sair do labirinto!!! \o/")
    sys.exit()


class Personagem:
    def __init__(self):
        self.nome = ""
        self.hp = 0
        self.ataque = 0
        self.defesa = 0

# Colocar random para dano
    def CalculaDano(self,inimigo):
        LimpaTela()
        print("Você encontrou um inimigo!")
        print("O %s parece perigoso! Atributos: \n HP: %d \n Ataque: %d \n Defesa: %d " % (inimigo.nome, inimigo.hp, inimigo.ataque, inimigo.defesa))
        time.sleep(2)
        while(jogador.hp >= 0 != inimigo.hp >=0):
            dano = ((self.ataque * random.uniform(0.6,2)) - (inimigo.defesa * random.uniform(0.7,1.3))) // 1
            danoSofrido = ((inimigo.ataque * random.uniform(0.5,1.8)) - (self.defesa * random.uniform(0.7,1.2))) // 1
            if dano < 0:
                dano = 0
            if danoSofrido < 0:
                danoSofrido = 0
            self.hp = self.hp - danoSofrido
            inimigo.hp = inimigo.hp - dano
            print("%s está lutando com %s!" %(self.nome,inimigo.nome))
            if jogador.hp < 0:
                jogador.hp = 0
            if inimigo.hp <0:
                inimigo.hp = 0
            print("%s hp %d --- %s %d" % (self.nome, self.hp, inimigo.nome, inimigo.hp))
            time.sleep(0.4)

            if jogador.hp == 0:
                print("%s foi morto por %s!" %(self.nome,inimigo.nome))
                GameOver()
            if inimigo.hp == 0:
                print("%s matou %s!" %(self.nome,inimigo.nome))
                time.sleep(0.75)
                LimpaTela()
                Mapa()

class Inimigo(Personagem):
    def __init__(self, jogador):
        Personagem.__init__(self)

class Heroi(Personagem):
    def __init__(self):
        Personagem.__init__(self)
        self.xp = 0
#Carrega Jogador
jogador = Heroi()
jogador.nome = nomeInput
jogador.hp = 30
jogador.ataque = 7
jogador.defesa = 5

inimigo = Inimigo(jogador)
inimigo.nome = "Lobo"
inimigo.hp = 20
inimigo.ataque = 6
inimigo.defesa = 3

def Mapa():

    MovimentoBool = bool(random.getrandbits(1)) #Gera um booleano randomico
    acertos = 0
    erros = 0
    Mcaminho = input("\n Pra qual direção você vai? \n Comandos: \n A = (Esquerda) \n D = (Direita) \n Q = (Atributos) \n V = (Pocoes de Vida) \n F = (Pocoes de Força) \n Sair = Sair \n \n Comando: ")

    if (Mcaminho.lower() == "a"):
        Mcaminho = 0
        LimpaTela()
        print(jogador.nome,"está caminhando para o lado esquerdo...")
        time.sleep(0.75)
        LimpaTela()
    elif (Mcaminho.lower() == "d"):
        Mcaminho = 1
        LimpaTela()
        print(jogador.nome,"está caminhando para o lado direito...")
        time.sleep(0.75)
        LimpaTela()
    elif (Mcaminho.lower() == "q"):
        LimpaTela()
        print("Nome:", jogador.nome)
        print("HP:", jogador.hp)
        print("Ataque:", jogador.ataque)
        print("Defesa:", jogador.defesa)
        print("Mochila:", mochila)
        Mapa()
    elif(Mcaminho.lower() == "v"):
        if (mochila["Pocoes de Vida"] > 0):
            LimpaTela()
            print(jogador.nome,"está tomando uma poção...")
            time.sleep(0.75)
            LimpaTela()
            jogador.hp += 15
            mochila["Pocoes de Vida"] -= 1
        else:
            LimpaTela()
            print(jogador.nome, "não possui mais poções!")
            time.sleep(0.75)
            LimpaTela()
        Mapa()
    elif(Mcaminho.lower() == "f"):
        if (mochila["Pocoes de Forca"] > 0):
            LimpaTela()
            print(jogador.nome,"está tomando uma poção de força...")
            time.sleep(0.75)
            LimpaTela()
            jogador.ataque += 10
            mochila["Pocoes de Forca"] -= 1

        else:
            LimpaTela()
            print(jogador.nome, "não possui poções de força!")
            time.sleep(0.75)
            LimpaTela()
        Mapa()

    elif (Mcaminho.lower() == "sair"):
        print("Você decidiu sair do jogo! :(")
        sys.exit()

    else:
        LimpaTela()
        print("Comando inválido.")
        time.sleep(0.4)
        LimpaTela()
        Mapa()

    if (Mcaminho == MovimentoBool):
        acertos =+ 1
        surpresa = random.randint(1,20)
        if surpresa == 1:
            mochila["Pocoes de Vida"] += 1
            print(jogador.nome, "encontrou uma poção de saúde!")
        elif surpresa == 2:
            mochila["Pocoes de Forca"] +=1
            print(jogador.nome, "encontrou uma poção de Força!")
        elif surpresa == 10:
            mochila["Pocoes de Vida"] +=3
            jogador.hp = 50
            jogador.ataque += 8
            jogador.defesa += 8
            print(jogador.nome, "encontrou um baú misterioso. Dentro dele há 3 Pocoes de vida e uma capa mágica que te deixa mais poderoso!")

        ContadorAcertos()
        Mapa()
    else:
        erros =+ 1
        ContadorErros()
        Mapa()

def ContadorAcertos():
    global acertos
    acertos = acertos = acertos + 1
    if acertos == 1:
        jogador.hp += 10
        print(jogador.nome, "encontrou e comeu uma fruta!")
        print("HP: ", jogador.hp)
    elif acertos == 3:
        jogador.defesa += 5
        print(jogador.nome, "encontrou um escudo mágico!")
        print("Sua defesa aumentou para: ", jogador.defesa)
    elif acertos == 5:
        jogador.ataque += 5
        print(jogador.nome, "encontrou uma espada mágica!")
        print("Seu ataque aumentou para: ", jogador.ataque)
    elif acertos == 15:
        inimigo.nome = "Dragão de 5 cabeças"
        inimigo.hp = 400
        inimigo.ataque = 30
        inimigo.defesa = 20
    elif acertos == 16:
        GameWin()
    else:
        print("Aqui não parece ter nada de importante...")
def ContadorErros():
    global erros
    erros = erros = erros + 1
    if erros == 3:
        inimigo.nome = "Urso"
        inimigo.hp = 40
        inimigo.ataque = 6
        inimigo.defesa = 7
    elif erros == 5:
        inimigo.nome = "Dragão"
        inimigo.hp = 40
        inimigo.ataque = 16
        inimigo.defesa = 12
    elif erros == 8:
        inimigo.hp = 60
    elif erros == 10:
        inimigo.nome = "Dragão de 2 cabeças"
        inimigo.hp = 100
        inimigo.ataque = 16
    else:
        print("Aqui não parece ter nada de importante...")
    if inimigo.hp > 0:
        jogador.CalculaDano(inimigo)

Mapa()
