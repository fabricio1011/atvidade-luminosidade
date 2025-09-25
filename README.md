# atvidade-luminosidade

Claro! Aqui está uma versão do README com um espaço reservado para a **foto do circuito** ou **print da simulação no Wokwi**:

---

# 🌞 Projeto: Sensor de Luminosidade com ESP32 e LEDs

Este projeto simula um sistema de automação de iluminação usando um sensor de luz (LDR) e dois LEDs controlados por um ESP32. Ideal para iniciantes em eletrônica e MicroPython.

---

## 🖼️ Visão Geral do Circuito

**📷 Insira aqui uma imagem do circuito montado ou da simulação no Wokwi:**

<img width="![5BB7377D-D675-4A19-8BCC-E2762E7D49EA](https://github.com/user-attachments/assets/ec505744-06ed-42ed-8c25-e0fae8cbd2fc)
1917" height="897" alt="Captura de tela 2025-09-23 171037" src="https://github.com/user-attachments/assets/ec2e2fb0-e926-488d-a9be-b42ef16903e6" />
![61D9081D-EDB4-432C-9619-F2A0CF6B006C](https://github.com/user-attachments/assets/39584a04-6324-478c-8484-5d33a27bf7ea)


---

## 📦 Componentes Utilizados

| Componente                 | Quantidade | Descrição                      |
| -------------------------- | ---------- | ------------------------------ |
| ESP32 DevKit-C             | 1          | Microcontrolador principal     |
| Sensor LDR (fotorresistor) | 1          | Sensor de intensidade luminosa |
| LED vermelho               | 1          | Indica pouca luz               |
| LED amarelo                | 1          | Indica luminosidade média/alta |
| Resistores 1kΩ             | 3          | Limitadores de corrente        |
| Protoboard                 | 1          | Montagem do circuito           |

---

## 🔌 Esquema de Ligação

* **LDR** conectado ao pino 34 (entrada analógica) do ESP32.
* **LED vermelho** no pino 15 (saída digital).
* **LED amarelo** no pino 2 (saída digital).
* Resistores de 1kΩ para proteger os LEDs e o sensor.

---

## 🧠 Lógica de Funcionamento

1. O ESP32 lê o valor analógico vindo do LDR.
2. Com base na intensidade de luz:

   * 💡 **Baixa luz** → Acende o LED vermelho.
   * 🌤️ **Luz suficiente** → Acende o LED amarelo.
3. A troca de LEDs é feita automaticamente de acordo com o ambiente.

---

## 💻 Código (MicroPython)

```python
from machine import Pin, ADC
from time import sleep

# Configuração dos pinos
ldr = ADC(Pin(34))  # Entrada analógica
led_vermelho = Pin(15, Pin.OUT)
led_amarelo = Pin(2, Pin.OUT)

while True:
    valor = ldr.read()
    print("Luminosidade:", valor)

    if valor < 1500:
        led_vermelho.on()
        led_amarelo.off()
    else:
        led_vermelho.off()
        led_amarelo.on()
    
    sleep(0.5)
```

---

## ▶️ Como Simular no Wokwi

1. Acesse [https://wokwi.com](https://wokwi.com)
2. Crie um novo projeto com ESP32 e selecione MicroPython
3. Copie e cole o código acima no arquivo `main.py`
4. Importe o arquivo `diagram.json` (do Wokwi)
5. Clique em ▶️ **"Simular"**

---

## 🚀 Ideias de Expansão

* Adicionar um buzzer que toca em baixa luminosidade
* Enviar os dados via Wi-Fi (MQTT ou HTTP)
* Mostrar os dados num display OLED

---

Se quiser, posso transformar isso em um projeto pronto para subir no GitHub com todos os arquivos. Deseja isso também?

