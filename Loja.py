# Separador de linhas
def sep():
    print("-" * 72)

# Nome completo, nome da loja e análise de crédito
def obter_limite():
    sep()
    print("========== Bem-vindo à Loja Virtual do Rodrigo Yuji Kawakani! ==========")
    sep()
    print("Com base nos seus dados faremos uma breve análise de crédito!")

# Dados do usuário
    cargo = input("Digite o seu cargo atual: ")
    salario = float(input("Digite o seu salário: "))
    anonascimento = int(input("Digite o ano de seu nascimento: "))

# Variáveis ano, idade, crédito e cálculo da idade
    from datetime import date
    ano = int(date.today().year)
    idade = ano - anonascimento
    limite = (salario * (idade/1000)) + 100
    limiteinicial = limite

# Mostre ao usuário os seus dados e idade aproximada
    sep()
    print("O seu cargo atual é {}.\nSeu salário é R$ {:.2f}.\nVocê nasceu no ano de {}.\nSua idade aproximada é {} anos.".format(cargo, salario, anonascimento, idade))

# Mostre quanto o cliente poderá gastar
    sep()
    print("=== Parabéns você poderá gastar o valor de R$ {:.2f} em nossa Loja! ===".format(limite))
    sep()

# Valor a ser retornado
    return limite, idade, limiteinicial

# Chamada a função obter limite
limite, idade, limiteinicial = obter_limite()

# Nome do produto e valor com ou sem desconto
def verificar_produto(limite, idade):
    nomeproduto = input("Digite o nome de um produto: ")
    valorproduto = float(input("Digite o preço do produto: "))
    sep()

# Cálculo de desconto - Nome completo: 21 caracteres - Primeiro nome: 7 caracteres
    primeironome = len("Rodrigo")
    nomecompleto = len("Rodrigo Yuji Kawakani")
    valorcomdesconto = valorproduto - (valorproduto * (primeironome/100))

    if valorproduto >= nomecompleto and valorproduto <= idade:
        print("Parabéns você terá um desconto de 7% na sua compra!\nO valor atual do produto {} é R$ {:.2f}!".format(nomeproduto, valorcomdesconto))
        limite = limite - valorcomdesconto        
        sep()
        return limite
    else:
        limite = limite - valorproduto
        return limite

# Quantidade de produtos que deseja cadastrar
n = int(input("Quantos produtos deseja cadastrar: "))

# Repetição para cadastro de produtos e o valor do saldo após cada operação
while n>0:
    limite = verificar_produto(limite, idade)
    n -= 1
    
    if limite > 0:
        print("Seu saldo atual é R${:.2f}.\nVocê pode continuar comprando!".format(limite))
        sep()
    elif limite == 0:
        print("Seus créditos se esgotaram, você não pode comprar mais produtos.\nObrigado pela preferência!")
        sep()
        break
    else:
        print("Você ultrapassou o limite do seu crédito!\nPor favor, realize o processo novamente!")
        sep()
        break

# Forma de pagamento de todos os produtos
def parcelas(limite, limiteinicial):
    valortotal = limiteinicial - limite
    
    if valortotal <= limiteinicial * 0.6:
        print("============================== Liberado! ==============================")
    elif valortotal > limiteinicial * 0.6 and valortotal <= limiteinicial * 0.9:
        print("================= Liberado ao parcelar em até 2 vezes! =================")
    elif valortotal > limiteinicial * 0.9 and valortotal <= limiteinicial:
        print("=============== Liberado ao parcelar em 3 ou mais vezes! ===============")
    else:
        print("============================== Bloqueado! ==============================")

# Chamada a função parcelas
parcelas(limite, limiteinicial)
sep()
