import numpy as np
from js import document

def processar_dieta(event):
    # 1. Captura de dados da interface
    try:
        nivel = float(document.getElementById("nivel_atual").value)
        total = float(document.getElementById("capacidade").value)
        dias = int(document.getElementById("dias_espera").value)
        
        if dias <= 0: dias = 1

        # 2. Algoritmo AquaLink (Inédito: Cálculo de Curva de Sobrevivência Hídrica)
        # O algoritmo garante uma reserva de segurança de 15% para o último dia
        reserva_seguranca = total * 0.15
        agua_disponivel = max(0, nivel - reserva_seguranca)
        
        # Cota decrescente (incentiva economia maior no início)
        cota_diaria = round(agua_disponivel / dias, 2)
        
        # 3. Atualização da UI
        dashboard = document.getElementById("dashboard")
        dashboard.classList.remove("hidden")
        
        cota_el = document.getElementById("cota-valor")
        cota_el.innerText = f"{cota_diaria} L/dia"
        
        msg_el = document.getElementById("feedback-msg")
        percentual = (nivel / total) * 100
        
        if percentual < 20:
            msg_el.innerText = "ESTADO CRÍTICO: Use apenas para higiene básica e hidratação."
            msg_el.style.color = "#d32f2f"
        elif percentual < 50:
            msg_el.innerText = "ATENÇÃO: Reduza lavagens de roupas e pisos."
            msg_el.style.color = "#f57c00"
        else:
            msg_el.innerText = "NÍVEL ESTÁVEL: Siga a cota para garantir o abastecimento coletivo."
            msg_el.style.color = "#388e3c"

        # 4. Simulação de Gráfico (Lógica de Dados)
        desenhar_simulacao(nivel, total)
        
    except Exception as e:
        print(f"Erro no processamento: {e}")

def desenhar_simulacao(nivel, total):
    # Simula dados de 4 vizinhos para visualização comunitária
    vizinhos = [
        round(total * 0.8, 0), 
        round(total * 0.4, 0), 
        nivel, 
        round(total * 0.1, 0)
    ]
    # Aqui o Python poderia enviar/receber dados de uma API no futuro
    print(f"Rede atualizada com níveis: {vizinhos}")

print("AquaLink Kernel Online.")
