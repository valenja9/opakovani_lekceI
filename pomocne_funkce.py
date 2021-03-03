def vytvor_soubor(jmeno_souboru):
    with open(f"{jmeno_souboru}.csv", mode="w") as file:
        jmeno, prijmeni, vek = ["Jmeno", "Prijmeni", "vek"]
        text = f"{jmeno},{prijmeni},{vek}" + "\n"
        file.writelines(text)
        print(f"Vytvoril jsem soubor: {jmeno_souboru}")


# manualni zadavani uzivatelu
def zadavani_uzivatelu(jmeno_souboru):
    while True:
        volba = input("Zadej volbu. (Pro ukonceni zmacni q)").lower()
        if volba == "q":
            break
        else:
            zadej_data = input("Zadej vzdy Jmeno, prijmeni a vek(Vse rozdel carkou)").split(",")
            pridani_do_souboru(jmeno_souboru, zadej_data)


# pridani do souboru
def pridani_do_souboru(jmeno_souboru, zadej_data):
    with open(f"{jmeno_souboru}.csv", mode="a") as file:  # Jeste pridat volbu na txt, nebo csv
        jmeno, prijmeni, vek = zadej_data
        text = f"{jmeno},{prijmeni},{vek}" + "\n"
        print(text)
        file.writelines(text)


# Zadej z dat
def zadej_z_dat(jmeno_souboru, data):
    for radek in data:
        pridani_do_souboru(jmeno_souboru, radek)