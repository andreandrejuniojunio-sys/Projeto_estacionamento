# SISTEMA DE ESTACIONAMENTO
# Constantes do estacionamento
CAPACIDADE = 20
VALOR_HORA = 8.00
# Variaveis do sistema
veiculos_estacionados = 0
faturamento = 0.0

# Funcao para registrar entrada
def registrar_entrada(veiculos):
   placa = input("Digite a placa do veiculo: ")
   if veiculos < CAPACIDADE:
       veiculos = veiculos + 1
       print("Entrada registrada com sucesso!")
       print("Placa:", placa)
   else:
       print("Estacionamento lotado!")
   return veiculos

# Funcao para registrar saida
def registrar_saida(veiculos, faturamento):
   if veiculos == 0:
       print("Nao existem veiculos estacionados.")
   else:
       placa = input("Digite a placa do veiculo: ")
       horas = float(input("Quantas horas ficou estacionado? "))
       if horas <= 0:
           print("Quantidade de horas invalida.")
       else:
           valor = horas * VALOR_HORA
           print("Placa:", placa)
           print("Valor a pagar: R$ {:.2f}".format(valor))
           faturamento = faturamento + valor
           veiculos = veiculos - 1
           print("Saida registrada com sucesso!")
   return veiculos, faturamento

# Funcao para consultar vagas
def consultar_vagas(veiculos):
   vagas_disponiveis = CAPACIDADE - veiculos
   print("Capacidade total:", CAPACIDADE)
   print("Veiculos estacionados:", veiculos)
   print("Vagas disponiveis:", vagas_disponiveis)

# Funcao para consultar faturamento
def consultar_faturamento(faturamento):
   print("Faturamento total: R$ {:.2f}".format(faturamento))

# Menu principal
while True:
   print("\n===== SISTEMA DE ESTACIONAMENTO =====")
   print("1 - Registrar entrada de veiculo")
   print("2 - Registrar saida de veiculo")
   print("3 - Consultar vagas disponiveis")
   print("4 - Consultar faturamento")
   print("0 - Sair")
   opcao = input("Escolha uma opcao: ")
   if opcao == "1":
       veiculos_estacionados = registrar_entrada(
           veiculos_estacionados
       )
   elif opcao == "2":
       veiculos_estacionados, faturamento = registrar_saida(
           veiculos_estacionados, faturamento
       )
   elif opcao == "3":
       consultar_vagas(veiculos_estacionados)
   elif opcao == "4":
       consultar_faturamento(faturamento)
   elif opcao == "0":
       print("Sistema encerrado.")
       break
   else:
       print("Opcao invalida! Tente novamente.")