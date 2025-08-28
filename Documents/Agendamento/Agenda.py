from datetime import datetime

print(f'*****GERADOR DO TEXTO DE PRÉ-RESERVA*****\n'
      f'------------------------------------------\n'
      f'[1] Quarto Térreo no Hotel\n'
      f'[2] Quarto Superior no Hotel\n'
      f'[3] Chalé Belvedere\n'
      f'[4] Chalé Temático sem Hidromassagem\n'
      f'[5] Chalé Temático com Hidromassagem\n'
      f'[6] Chalé Geodo\n'
      f'------------------------------------------\n')

nomeHospede = input("Digite o nome do hóspede: ")
hospedagem_opcao = int(input("Digite o número da opção de hospedagem: "))

if hospedagem_opcao == 1:
    hospedagem = "Quarto Térreo no Hotel"
elif hospedagem_opcao == 2:
    hospedagem = "Quarto Superior no Hotel"
elif hospedagem_opcao == 3:
    hospedagem = "Chalé Belvedere"
elif hospedagem_opcao == 4:
    hospedagem = "Chalé Temático sem Hidromassagem"
elif hospedagem_opcao == 5:
    hospedagem = "Chalé Temático com Hidromassagem"
elif hospedagem_opcao == 6:
    hospedagem = "Chalé Geodo"
else:
    hospedagem = "Opção inválida"

checkin = input("Digite a data de entrada (dd/mm): ")
checkout = input("Digite a data de saída (dd/mm): ")

def calcular_diarias(data_entrada, data_saida):
    formato_data = "%d/%m/%Y"
    ano_padrao = "2025"  # Adicionando um ano padrão
    data_entrada = datetime.strptime(data_entrada + '/' + ano_padrao, formato_data)
    data_saida = datetime.strptime(data_saida + '/' + ano_padrao, formato_data)
    diferenca = (data_saida - data_entrada).days
    return diferenca

totalDiarias = calcular_diarias(checkin, checkout)
valor_diaria = float(input("Digite o valor da diária em R$: "))

valorTotal = totalDiarias * valor_diaria
vinteCinco = valorTotal * 0.25

valor_diaria_str = f"{valor_diaria:.2f}".replace('.', ',')
valorTotal_str = f"{valorTotal:.2f}".replace('.', ',')
vinteCinco_str = f"{vinteCinco:.2f}".replace('.', ',')

if totalDiarias == 1:
    totalDiarias_str = "uma"
elif totalDiarias == 2:
    totalDiarias_str = "duas"
elif totalDiarias == 3:
    totalDiarias_str = "três"
elif totalDiarias == 4:
    totalDiarias_str = "quatro"
elif totalDiarias == 5:
    totalDiarias_str = "cinco"
elif totalDiarias == 6:
    totalDiarias_str = "seis"
elif totalDiarias == 7:
    totalDiarias_str = "sete"
elif totalDiarias == 8:
    totalDiarias_str = "oito"
elif totalDiarias == 9:
    totalDiarias_str = "nove"
elif totalDiarias == 10:
    totalDiarias_str = "dez"
else:
    totalDiarias_str = str(totalDiarias)

def diaria(totalDiarias):
    if totalDiarias == 1:
        return 'diária'
    elif totalDiarias > 1:
        return 'diárias'

diarias_str = diaria(totalDiarias)

print(f'Pré-Reserva confirmada em nome de _{nomeHospede}_'
      f' em um *{hospedagem}* com entrada dia {checkin} e saída {checkout}'
      f', totalizando {totalDiarias_str} {diarias_str} no valor de R${valor_diaria_str}'
      f' TOTAL = R${valorTotal_str}, *(25% = R${vinteCinco_str})*')
