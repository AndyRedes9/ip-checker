import requests
import json

resultados = []

print("Escribe una IP pública o 'exit' para salir.\n")

while True:
    ip = input(" Ingresa una IP: ").strip()
    if ip.lower() == "exit":
        break

    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            info = {
                "ip": ip,
                "pais": data.get("country"),
                "region": data.get("regionName"),
                "isp": data.get("isp"),
                "coordenadas": {
                    "latitud": data.get("lat"),
                    "longitud": data.get("lon")
                }
            }
            resultados.append(info)
            print(json.dumps(info, indent=2, ensure_ascii=False))
        else:
            print(f"IP inválida o no encontrada: {ip}")
    except Exception as e:
        print("Error al consultar la IP:", e)

with open("ip_results.json", "w", encoding="utf-8") as archivo:
    json.dump(resultados, archivo, indent=2, ensure_ascii=False)

print("\n Resultados guardados en 'ip_results.json'")
