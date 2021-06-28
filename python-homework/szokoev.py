# Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e.
# Szökőév minden negyedik, nem szökőév minden századik, mégis az minden 400-adik. # (2000-ben ezért volt szökőév.)
# A függvény visszatérési értéke legyen logikai típusú! Tipp( % maradekos osztas operátor)
# Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja, hogy szökőév-e!
# Használd az előbb megírt függvényt! Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ? 1900 Nem szökőév.

year = int(input("Please, submit a year, to check if it is a leap year?: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
