
class Client:
    def __init__(self, emitent, destin, note_ident, email):
        self.emitent = emitent
        self.destin = destin
        if note_ident != 10:
            raise ValueError("O número da nota informada está errado")
        else:
            self.__note_ident = note_ident
        if "@" not in email:
            raise ValueError("O número da nota informada está errado")
        else:
            self.__email= email
    def get_info(self):
        return f"Emitente --> {self.emitent}\nDestinatário --> {self.destin}\nE-mail --> {self.__email}"
    def set_info(self):
        while(True):
            menu = int(input("O que você deseja alterar?\n1 - Alterar emitente\n2 - Alterar destinatário\n3 - Alterar email\n4 - Sair\n--> "))
            if menu == 1:
                new_emitent = input("informe o nome do novo emitente:\n--> ")
                self.emitent = new_emitent
                print("Emitente alterado com sucesso!")
            elif menu == 2:
                new_destin = input("Informe o novo destinatário:\n--> ")
                self.destin = new_destin
                print("Destinatário alterado com sucesso")
            elif menu == 3:
                new_email = input("Informe o novo e-mail:\n--> ")
                if "@" not in new_email:

                    print("Informe um e-mail válido")
                    continue
                else:
                    self.__email = new_email
                    print("E-mail atlerado com sucesso")
            elif menu == 4:
                return "saindo..."
            else:
                continue
class Product:
    def __init__(id, name, price, stock)
    
# cliente1 = Shop("Galdino", "Adiel", 10, "isac.galdino@gmail.com")
# print(cliente1.get_info())
# cliente1.set_info()
# print(cliente1.get_info())


