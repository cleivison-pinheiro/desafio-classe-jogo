class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "usou magia"
        elif self.tipo == "guerreiro":
            ataque = "usou espada"
        elif self.tipo == "monge":
            ataque = "usou artes marciais"
        elif self.tipo == "ninja":
            ataque = "usou shuriken"
        else:
            ataque = "usou um ataque desconhecido"

        mensagem = f"O {self.tipo} atacou usando: {ataque}"
        print(mensagem)



heroi_mago = Heroi("Potter", 150, "mago")
heroi_mago.atacar()

heroi_guerreiro = Heroi("Naruto", 35, "guerreiro")
heroi_guerreiro.atacar()

heroi_monge = Heroi("Buda", 40, "monge")
heroi_monge.atacar()

heroi_ninja = Heroi("Hatzu", 28, "ninja")
heroi_ninja.atacar()
