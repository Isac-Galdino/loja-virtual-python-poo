class Loja:
    def __init__(self, emitent, destin, nota_ident, email):
        self.emitent = emitent
        self.destin = destin
        if nota_ident > 44 and nota_ident < 44:
            self.__nota_ident = nota_ident
        else:
            raise ValueError("O número de nota fiscal informada é inválida")

        if "@" not in email:
            raise ValueError("O e-mail informado é inválido")
        else:
            self.__email = email

    def get_info(self):
        return f"Emitente"