from utime import sleep
from pluvio import Pluviometro

pluviometro = Pluviometro(5)

while True:
    volume_hoje = pluviometro.volume_chuva()
    print(f"Volume de chuva: {volume_hoje:.2f} mm")
    sleep(3)  # Atualizando a cada 3 segundos para finalidade da demonstração