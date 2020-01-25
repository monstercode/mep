import requests

response = requests.get("https://www.bullmarketbrokers.com/Information/StockPrice/GetStockPrices?term=3&index=usd+soberanos&sortColumn=ticker&isAscending=true")
data = response.json()["result"]

bonds = {
    "AA25" :  None,
    "AA25D":  None,
    "AA37" :  None,
    "AA37D":  None,
    "AO20" :  None,
    "AO20D":  None,
    "AY24" :  None,
    "AY24D":  None,
    "DICA" :  None,
    "DICAD":  None,
    "DICY" :  None,
    "DICYD":  None,
    "PARA" :  None,
    "PARAD":  None,
    "PARY" :  None,
    "PARYD":  None,
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
