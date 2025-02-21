import requests
import json
import datetime

# URL do Webhook.site
WEBHOOK_URL = "https://webhook.site/204c9451-da59-4019-9b17-782f26ae20d0"

# Simula um deploy
def deploy():
    print("Realizando deploy...")
    
    # Aqui você colocaria os comandos reais de deploy
    success = True  # Simulando sucesso no deploy

    # Dados a serem enviados no webhook
    payload = {
        "status": "deploy_successful" if success else "deploy_failed",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "message": "Deploy concluído com sucesso!"
    }

    # Enviar requisição POST para Webhook.site
    response = requests.post(WEBHOOK_URL, json=payload, headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        print("Webhook enviado com sucesso!")
    else:
        print(f"Erro ao enviar webhook: {response.status_code} - {response.text}")

# Executar deploy e enviar webhook
deploy()
