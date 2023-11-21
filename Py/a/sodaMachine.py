mDados = [[1, "Coca", 3.75, 2],[2, "Pepsi", 3.67, 5],[3, "Monster", 9.96, 1],[4, "Café", 1.25, 100],[5, "Redbull", 13.99, 2]]

class Product:
    # cada produto tem um id, nome, custo e estoque
    def __init__(self, id, name, cost, stock):
        self.id = id
        self.name = name
        self.cost = cost
        self.stock = stock



class SodaMachine:
    def __init__(self):
        # cria uma lista de produtos
        self.products = [
            Product(mDados[0][0], mDados[0][1], mDados[0][2], mDados[0][3]),
            Product(mDados[1][0], mDados[1][1], mDados[1][2], mDados[1][3]),
            Product(mDados[2][0], mDados[2][1], mDados[2][2], mDados[2][3]),
            Product(mDados[3][0], mDados[3][1], mDados[3][2], mDados[3][3]),
            Product(mDados[4][0], mDados[4][1], mDados[4][2], mDados[4][3])
        ]
        
        self.troco = [
            Product(0, "10 real", 10, 5),
            Product(1, "5 real", 5, 10),
            Product(2, "1 real", 1, 10),
            Product(3, "50 cent", 0.5, 30),
            Product(4, "20 cent", 0.2, 20),
            Product(5, "10 cent", 0.1, 25),
            Product(6, "1 cent", 0.01, 100)
        ]
        
    # mostra os produtos disponiveis
    def display_products(self):
        print("ID\tName\tCost\tStock")
        for product in self.products:
            print(f"{product.id}\t{product.name}\t${product.cost}\t{product.stock}")
    
    
    # funcao para quando um produto é vendido, analisa o ID do produto, verifica disponibilidade e retorna seu preço, e pede o pagamento
    def sell_product(self, product_id, payment):
        for product in self.products:
            if product.id == product_id:
                if product.stock > 0:
                    product.stock -= 1
                    if product.cost > payment:
                        print("Pagamento insuficiente.")
                    else:
                        troco = calc_troco(product.cost, payment, product_id)
                        print(f"Vendido {product.name} por ${product.cost}")
                        print("troco: ")
                        print(f"notas de 10 reais: {int(troco[0])}")
                        print(f"notas de 5 reais: {int(troco[1])}")
                        print(f"moedas de 1 real: {int(troco[2])}")
                        print(f"moedas de 50 centavos: {int(troco[3])}")
                        print(f"moedas de 20 centavos: {int(troco[4])}")
                        print(f"moedas de 10 centavos: {int(troco[5])}")
                        print(f"moedas 1 centavo: {int(troco[6])}")
                        pedir()
                else:
                    print(f"{product.name} fora de estoque")
                    pedir()
                return
        print("Invalid product ID")
        pedir()
        
#chamadas
machine = SodaMachine()


def pedir():
    machine.display_products()
    id = input("Entre com ID do produto desejado: ")
    if id != "admin":
        id = int(id)
        print(f"preço: {machine.products[id-1].cost}")
        pago = float(input("Entre com o valor pago: "))
        machine.sell_product(id, pago)
    else:
        oq = input("Deseja: \n*A*dicionar um novo produto\n*R*emover um produto\n*E*ditar um produto\n")
        if oq == "A" or oq == "a":
            idnova = int(input("Entre com o ID do novo produto: "))
            nome = input("Entre com o nome do novo produto: ")
            preco = float(input("Entre com o preço do novo produto: "))
            estoque = int(input("Entre com o estoque do novo produto: "))
            machine.products.append(Product(idnova, nome, preco, estoque))
        elif oq == "R" or oq == "r":
            idrem = int(input("Entre com o ID do produto a ser removido: "))
            machine.products.pop(idrem-1)
        elif oq == "E" or oq == "e":
            idedit = int(input("Entre com o ID do produto a ser editado: "))
            oq = input("Deseja editar: \n*N*ome\n*P*reço\n*E*stoque\n")
            if oq == "N" or oq == "n":
                nome = input("Entre com o novo nome: ")
                machine.products[idedit-1].name = nome
            elif oq == "P" or oq == "p":
                preco = float(input("Entre com o novo preço: "))
                machine.products[idedit-1].cost = preco
            elif oq == "E" or oq == "e":
                estoque = int(input("Entre com o novo estoque: "))
                machine.products[idedit-1].stock = estoque
        pedir()
        
def calc_troco(custo, pago, id):
    #funcao para calcular o troco, retorna uma tupla com a quantidade de notas e moedas
        troco = pago - custo
        trocototal = []        
       
        for x in range(len(machine.troco)):
            y = machine.troco[x].cost
            cedula = troco // y
            if machine.troco[x].stock > cedula:
                trocototal.append(cedula)
                machine.troco[x].stock -= cedula
                troco %= y
                
            else:
                trocototal.append(machine.troco[x].stock)
                troco -= machine.troco[x].stock * y
                machine.troco[x].stock = 0
                        
        if troco > 0 and troco < 0.01:
            troco = 0
            trocototal[-1] += 1
            machine.troco[-1].stock -= 1
            
        if troco > 0:
            print("Não temos troco para essa quantia, compra cancelada.")
            for x in range(len(trocototal)):
                machine.troco[x].stock += trocototal[x]
            machine.products[id-1].stock = machine.products[id-1].stock + 1
            pedir()
        
        return (trocototal)
        
pedir()
