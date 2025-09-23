print("Hello, ESP32!")
from machine import Pin, ADC
from time import sleep
ldr = ADC(Pin(34))          
ldr.atten(ADC.ATTN_11DB)   
ldr.width(ADC.WIDTH_12BIT) 
led_principal = Pin(25, Pin.OUT)  
led_apoio = Pin(26, Pin.OUT)     
limiar1 = 1500  
limiar2 = 1100  
while True:
    valor = ldr.read() 
print("Valor LDR:", valor)
    if valor < limiar2:
        led_principal.on()
        led_apoio.on()
        estado = "LED Principal + LED Apoio ON"
    elif valor < limiar1:
        led_principal.on()
        led_apoio.off()
        estado = "LED Principal ON"
    else:
        led_principal.off()
        led_apoio.off()
        estado = "LEDs OFF"
    print("Luminosidade:", valor, "-", estado)
    sleep(0.5)