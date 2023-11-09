#maquina de refrigerante
mDados = [[1, "Coca", 3.75, 2],[2, "Pepsi", 3.67, 5],[3, "Monster", 9.96, 1],[4, "Café", 1.25, 100],[5, "Redbull", 13.99, 2]]

class Product:
    # cada produto tem um id, nome, custo e estoque
    def __init__(self, id, name, cost, stock):
        self.id = id
        self.name = name
        self.cost = cost
        self.stock = stock

def calc_troco(custo, pago):
    #funcao para calcular o troco, retorna uma tupla com a quantidade de notas e moedas
        troco = pago - custo
        notaCinco = troco // 5
        troco %= 5
        moedaUmR = troco // 1
        troco %= 1
        moedaVinte = troco // 0.2
        troco %= 0.2
        moedaDez = troco // 0.1
        troco %= 0.1
        moedaUmC = round(troco / 0.01)
        return (notaCinco, moedaUmR, moedaVinte, moedaDez, moedaUmC)

class SodaMachine:
    def __init__(self):
        # cria uma lista de produtos
        self.products = [
            Product(mDados[0][0], mDados[0][1], mDados[0][2], mDados[0][3]),
            Product(mDados[1][0], mDados[1][1], mDados[1][2], mDados[1][3]),
            Product(mDados[2][0], mDados[2][1], mDados[2][2], mDados[2][3]),
            Product(mDados[3][0], mDados[3][1], mDados[3][2], mDados[3][3]),
            Product(mDados[4][0], mDados[4][1], mDados[4][2], mDados[4][3]),
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
                        troco = calc_troco(product.cost, payment)
                        print(f"Vendido {product.name} por ${product.cost}")
                        print("troco: ")
                        print(f"notas de 5 reais: {int(troco[0])}")
                        print(f"moedas de 1 real: {int(troco[1])}")
                        print(f"moedas de 20 centavos: {int(troco[2])}")
                        print(f"moedas de 10 centavos: {int(troco[3])}")
                        print(f"moedas 1 centavo: {int(troco[4])}")
                        id = int(input("Entre com ID do produto desejado: "))
                        print(f"preço: {machine.products[id-1].cost}")
                        pago = float(input("Entre com o valor pago: "))
                        machine.sell_product(id, pago)
                else:
                    print(f"{product.name} fora de estoque")
                    id = int(input("Entre com ID do produto desejado: "))
                    print(f"preço: {machine.products[id-1].cost}")
                    pago = float(input("Entre com o valor pago: "))
                    machine.sell_product(id, pago)
                return
        print("Invalid product ID")
        id = int(input("Entre com ID do produto desejado: "))
        print(f"preço: {machine.products[id-1].cost}")
        pago = float(input("Entre com o valor pago: "))
        machine.sell_product(id, pago)
        


#chamadas
machine = SodaMachine()
machine.display_products()

id = int(input("Entre com ID do produto desejado: "))
print(f"preço: {machine.products[id-1].cost}")
pago = float(input("Entre com o valor pago: "))
machine.sell_product(id, pago)
