import requests
import datetime
import time

# URL do Webhook.site
WEBHOOK_URL = "	https://webhook.site/204c9451-da59-4019-9b17-782f26ae20d0"

def send_webhook():
    print("Enviando webhook...")

    params = {
        "status": "deploy_successful",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "message": "Deploy concluído com sucesso!"
    }

    response = requests.get(WEBHOOK_URL, params=params)

    if response.status_code == 200:
        print(f"Webhook enviado com sucesso! {datetime.datetime.now()}")
    else:
        print(f"Erro ao enviar webhook: {response.status_code} - {response.text}")

# Loop infinito para rodar de 2 em 2 minutos
while True:
    send_webhook()
    time.sleep(120)  # Espera 2 minutos (120 segundos)
