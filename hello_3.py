aku = {
    "etunimi":"aku",
    "sukunimi":"ankka",
    "laji":"ankka",
    "nukkumapaikka":"riippumatto",
    "ika":61,
    "osoite":"paratiisitie_13",
    "naimisissa":False,
    "perhe":["tupu","hupu","lupu"]
}

#print(aku["ika"])

for ominaisuus in aku:
    #print(ominaisuus)
    #print(aku[ominaisuus])
    print(f"{ominaisuus}:{aku[ominaisuus]}")
    