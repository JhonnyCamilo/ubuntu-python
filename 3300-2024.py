import json
import requests
import time
import random

url = "https://api-prod-graphql.delightfulisland-802dbc14.eastus.azurecontainerapps.io/"

def nuevo_variables(temperatura):
    mutation = """
       mutation nuevaVariable($input: VariablesInput){
        nuevaVariable(input:$input){
            nombre
            dato
            creado
            }
        }
    """

    variables = {
         "input": {
            "nombre": "°C",
            "dato": temperatura,
            "sensor":  "65c17946eed3e14354880f70"
        
        }
    }

    payload = {
        "query": mutation,
        "variables": json.dumps(variables)
    }

    response = requests.post(url, json=payload)
    return response.json()


def main():
    while True: # Bucle infinito para ejecutar continuamente
        temperatura = random.randint(1, 100) # Generar un valor aleatorio para la temperatura
        response = nuevo_variables(temperatura)
        print(f"Datos enviados: {response}")
        time.sleep(5) # Esperar 5 segundos antes de enviar el siguiente valor


main()