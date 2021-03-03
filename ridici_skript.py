from data_pro_ucitele import DATA
from pomocne_funkce import *


def main():
   mode = input("Zadej mode ('m' pro manual nebo 'a' pro automatic)").lower()
   jmeno_souboru = input("Zadej jmeno souboru: ")
   if mode == "m":
     vytvor_soubor(jmeno_souboru)
     zadavani_uzivatelu(jmeno_souboru)
   elif mode == "a":
    zadej_z_dat(jmeno_souboru, DATA)
   else:
    print("spatny mod exit!")
    exit()


if __name__ == "__main__":
    main()
