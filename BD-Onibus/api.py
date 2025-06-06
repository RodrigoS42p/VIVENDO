from config import API_KEY, STOP_ID

def get_bus_arrivals():
    url = f"http://www.ctabustracker.com/bustime/api/v2/getpredictions?key={API_KEY}&stpid={STOP_ID}&format=json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Erro ao acessar API da CTA")

    data = response.json()
    predictions = data.get("bustime-response", {}).get("prd", [])

    result = []
    for p in predictions:
        eta_minutes = calculate_eta_minutes(p["tmstmp"], p["prdtm"])
        result.append({
            "vehicle_id": p["vid"],
            "route": p["rt"],
            "eta_minutes": eta_minutes,
            "timestamp": p["tmstmp"]
        })
    return result

def calculate_eta_minutes(current_time, predicted_time):
    from datetime import datetime

    fmt = "%Y%m%d %H:%M"
    now = datetime.strptime(current_time[:13], fmt)
    eta = datetime.strptime(predicted_time[:13], fmt)
    return int((eta - now).total_seconds() / 60)