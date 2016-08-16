d = {"Michanel":95,"Bob":75,"Tracy":85}
print(d["Michanel"])
d["Adam"] = 67
d["Jack"] = 90
print(d)
d["Jack"] = 88
print(d)
print("thomas" in d)
print("Bob" in d)
print(d.get("thomas"))
print(d.get("thomas",-1))
print(d.get("Bob"))
d.pop("Tracy")
print(d)
