import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calcular_diarias(data_entrada, data_saida):
    try:
        formato_data = "%d/%m/%Y"
        ano_padrao = "2025"  # Adicionando um ano padrão
        data_entrada = datetime.strptime(data_entrada + '/' + ano_padrao, formato_data)
        data_saida = datetime.strptime(data_saida + '/' + ano_padrao, formato_data)
        return (data_saida - data_entrada).days
    except ValueError:
        messagebox.showerror("Erro", "Formato de data inválido! Use dd/mm.")
        return None

def total_diarias_str(totalDiarias):
    if totalDiarias == 1:
        return "uma"
    elif totalDiarias == 2:
        return "duas"
    elif totalDiarias == 3:
        return "três"
    elif totalDiarias == 4:
        return "quatro"
    elif totalDiarias == 5:
        return "cinco"
    elif totalDiarias == 6:
        return "seis"
    elif totalDiarias == 7:
        return "sete"
    elif totalDiarias == 8:
        return "oito"
    elif totalDiarias == 9:
        return "nove"
    elif totalDiarias == 10:
        return "dez"
    else:
        return str(totalDiarias)

def diaria(totalDiarias):
    if totalDiarias == 1:
        return 'diária'
    elif totalDiarias > 1:
        return 'diárias'

def gerar_texto():
    nomeHospede = entry_nome.get()
    checkin = entry_checkin.get()
    checkout = entry_checkout.get()
    valor_diaria = entry_valor_diaria.get()
    
    try:
        valor_diaria = float(valor_diaria.replace(",", "."))
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor de diária válido!")
        return
    
    hospedagem_opcao = hospedagem_var.get()
    hospedagens = {
        1: "Quarto Térreo no Hotel",
        2: "Quarto Superior no Hotel",
        3: "Chalé Belvedere",
        4: "Chalé Temático sem Hidromassagem",
        5: "Chalé Temático com Hidromassagem",
        6: "Chalé Geodo"
    }
    
    hospedagem = hospedagens.get(hospedagem_opcao, "Opção inválida")

    totalDiarias = calcular_diarias(checkin, checkout)
    if totalDiarias is None or totalDiarias <= 0:
        messagebox.showerror("Erro", "Datas inválidas! O check-out deve ser após o check-in.")
        return
    
    valorTotal = totalDiarias * valor_diaria
    vinteCinco = valorTotal * 0.25

    valor_diaria_str = f"{valor_diaria:.2f}".replace('.', ',')
    valorTotal_str = f"{valorTotal:.2f}".replace('.', ',')
    vinteCinco_str = f"{vinteCinco:.2f}".replace('.', ',')

    resultado = (f'Pré-Reserva confirmada em nome de _{nomeHospede}_ '
                 f'em um *{hospedagem}* com entrada dia {checkin} e saída {checkout}, '
                 f'totalizando {total_diarias_str(totalDiarias)} {diaria(totalDiarias)} no valor de R${valor_diaria_str} '
                 f'TOTAL = R${valorTotal_str}, *(25% = R${vinteCinco_str})*')

    texto_resultado.config(state="normal")  
    texto_resultado.delete("1.0", tk.END)  
    texto_resultado.insert(tk.END, resultado)
    texto_resultado.config(state="disabled") 

def copiar_texto():
    root.clipboard_clear()  # Limpa a área de transferência
    root.clipboard_append(texto_resultado.get("1.0", tk.END))  # Copia o conteúdo
    root.update()  # Atualiza o sistema de clipboard
    messagebox.showinfo("Copiado!", "Texto copiado para a área de transferência.")

root = tk.Tk()
root.title("Gerador de Texto de Pré-Reserva")
root.geometry("450x550")

tk.Label(root, text="Nome do Hóspede:").pack()
entry_nome = tk.Entry(root, width=40)
entry_nome.pack()

tk.Label(root, text="Escolha a hospedagem:").pack()
hospedagem_var = tk.IntVar(value=1)
hospedagens = [
    "Quarto Térreo no Hotel",
    "Quarto Superior no Hotel",
    "Chalé Belvedere",
    "Chalé Temático sem Hidromassagem",
    "Chalé Temático com Hidromassagem",
    "Chalé Geodo"
]

for idx, hospedagem in enumerate(hospedagens, start=1):
    tk.Radiobutton(root, text=hospedagem, variable=hospedagem_var, value=idx).pack(anchor="w")

tk.Label(root, text="Data de Check-in (dd/mm):").pack()
entry_checkin = tk.Entry(root, width=20)
entry_checkin.pack()

tk.Label(root, text="Data de Check-out (dd/mm):").pack()
entry_checkout = tk.Entry(root, width=20)
entry_checkout.pack()

tk.Label(root, text="Valor da diária (R$):").pack()
entry_valor_diaria = tk.Entry(root, width=20)
entry_valor_diaria.pack()

btn_gerar = tk.Button(root, text="Gerar Texto", command=gerar_texto)
btn_gerar.pack(pady=10)

texto_resultado = tk.Text(root, height=6, width=50, wrap="word")
texto_resultado.pack()
texto_resultado.config(state="disabled")  # Impede edição manual

btn_copiar = tk.Button(root, text="Copiar Texto", command=copiar_texto)
btn_copiar.pack(pady=5)

root.bind("<Return>", lambda event: gerar_texto())

root.mainloop()
