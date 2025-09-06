import requests
from cartas.models import Carta

API_URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php?archetype=Blue-Eyes"

def get_cartas_list():
    response = requests.get(API_URL)
    if response.status_code != 200:
        print(f"Error fetching data from API: {response.status_code}")
        return []
    return response.json().get("data", [])

def load_cartas():
    if Carta.objects.exists():
        return "Cartas ya cargadas en la base de datos."

    cartas = get_cartas_list()
    for c in cartas:
        Carta.objects.create(
            id=c["id"],
            name=c.get("name"),
            defense=c.get("def"),
            level=c.get("level"),
            attribute=c.get("attribute"),
            image_url=c.get("card_images", [{}])[0].get("image_url"),
            cardmarket_price=c.get("card_prices", [{}])[0].get("cardmarket_price", 0.0),
        )
    return f"{Carta.objects.count()} cartas cargadas exitosamente."
