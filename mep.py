import requests

response = requests.get("https://www.bullmarketbrokers.com/Information/StockPrice/GetStockPrices?term=3&index=usd+soberanos&sortColumn=ticker&isAscending=true")
data = response.json()["result"]

bonds = {
    "AL30" :  None,
    "AL30D":  None,
    "AL29" :  None,
    "AL29D":  None,
    "AE38" :  None,
    "AE38D":  None,
    "AL35" :  None,
    "AL35D":  None,
    "AL41" :  None,
    "AL41D":  None,
    "GD29": None,
    "GD29D": None,
    "GD30": None,
    "GD30D": None,
    "GD35": None,
    "GD35D": None,
    "GD38": None,
    "GD38D": None,
    "GD41": None,
    "GD41D": None,
    "GD46": None,
    "GD46D": None,

}

mep = []

for bond in data:
    if bond["ticker"] in bonds:
        bonds[bond["ticker"]] = bond["stockState"]


for bond in bonds:
    if f"{bond}D" in bonds:
        try:
            cotizacion = float(bonds[bond]["price"])/float(bonds[f"{bond}D"]["price"])
        except Exception:
            continue

        mep.append({
            "ticker": bond,
            "cotizacion": cotizacion,
            "$AR": bonds[bond]['price'],
            "U$D": bonds[f'{bond}D']['price'],
            "volumen": bonds[bond]['operations'],
        })
        #print(f"{bond}: {cotizacion} | $AR {bonds[bond]['price']} | U$D {bonds[f'{bond}D']['price']} | volumen: {bonds[bond]['operations']}")

mep = sorted(mep, key=lambda c: c["cotizacion"])

for i in range(len(mep)):
    cot = mep[i]
    print(f" {cot['ticker']:5}| {cot['cotizacion']:.3f} | $AR {cot['$AR']:.2f} | U$D {cot['U$D']:.2f} | volumen: {cot['volumen']:8}")
