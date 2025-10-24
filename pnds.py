import pandas as pd

datum = pd.DataFrame({
    "Currencies": ["USD", "EUR", "JPY", "GBP", "AUD", "ZAR"],
    "Amounts": [780, 760, 740, 720, 700, 680]
})

print(datum.sort_values(by="Amounts"))

print(datum.sort_values(by="Currencies"))

print(datum.describe())

print(datum)

more = datum.assign(extras = datum["Amounts"] * 1.5)
print(more)

print(more.sort_values(by="extras"))

