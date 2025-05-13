from api import get_bus_arrivals
from database import registrar_chegada_onibus

def main():
    try:

        print("Consultando a API do CTA...")
        chegadas = get_bus_arrivals()
        print(f"Chegadas de ônibus obtidas com sucesso: {len(chegadas)} ônibus encontrados.")

   
        for onibus in chegadas:
            if onibus["eta_minutes"] == 2:
                print(f"Ônibus chegando em 2 minutos: {onibus}")
                registrar_chegada_onibus(onibus)
                print(f"Feedback do ônibus {onibus['vehicle_id']} registrado no banco de dados.")

    except Exception as e:
        print(f"Erro ao executar o programa: {e}")

if __name__ == "__main__":
    main()
