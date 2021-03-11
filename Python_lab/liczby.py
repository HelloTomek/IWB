#!/usr/bin/python3 
# shebang line - wskazuje jaką wersję Pythona wybrać domyślnie do przetwarzania skryptu.

## 1. Typy liczbowe
# Istnieją cztery różne typy liczbowe: zwykłe liczby całkowite, (długie liczby całkowite),
# liczby zmiennoprzecinkowe i liczby zespolone. 
# Python może być używany rownież jako kalkulator,
# rozpoznaje cztery podstawowe operatory arytmetyczne: + - * /

## Zwykłe liczby całkowite
a = 5  
b = 10
m = -3

# Odstępy przy operatorach są opcjonalne.
c =a+ b  *2

print(a, b, c)

# W Pythonie wyróżniamy dodatkowe dwa operatory arytmetyczne: potęgowanie, oraz reszta z dzielenia
print(3**2)   # Output: 9
print(8%3)    # Output: 2


## Długie liczby całkowite
# W Pythonie 3 'long integer' nie jest osobnym typem 
# Python 2 posiada dwa typy integer'ow - int oraz long.
dlugieliczbycalkowite = c*c**c
print(dlugieliczbycalkowite)
# print(type(c*c**c*100))
# print(type(c))
print(type(dlugieliczbycalkowite))

# W Pythonie liczby całkowite można zapisywać nie tylko w systemie liczbowym dziesiętnym, 
# rownież w dwójkowym (binarnym), ósemkowym (oktalnym) i szesnastkowym (heksadecymalnym).

# konwertujemy liczby na wybrany sytem, korzystjąc z wbudowanych funkcji typu build-in: bin(), dec(), hex()
print(hex(16))
#print(bin(m))


# Natomiast aby interpreter pythona odczytał Liczby podawane w systemie innym niż dziesietnym 
# należy dopisac na początku liczby zero i litere odpowiadajaca systemowi. 
# Binarnym: zero i literę b, ósemkowym: zero i literę o, a w szesnastkowym: zero i literę x, np.
a_hex=0xf
b_bin=0b10

sum = a_hex + b_bin
print(sum, type(sum))

# Jeżeli wyrażenie zawiera więcej operatorów, są one wykonywane w kolejności znanej z algebry
# W przypadku konieczności zmiany kolejności wykonywania operatorów, używamy nawiasów okrągłych
c_mix=a_hex+b_bin/a*b/c
#print(c_mix)

# Zauważmy, że zmienna c_mix posiada wartość zmiennoprzecinkową typu float. 
#print(type(c_mix))


## Float
# zaznaczmy na początek, że i w tym przypadku znajdzie zastosowanie funkcja castowania w pythonie, znamy ten rodzaj konwersji z napisów
# definujemy zmiennoprzecinkowe wartośći zmiennych
f = float(a) # 5.0
#print(f)
l = 10.266666
o = 2.

sum = f+l+o

# wydrukujmy informacje o typie danych poszczególnych zmiennych
print(type(c_mix))
print(type(f),type(l),type(o))
print(sum, type(sum))

# liczby rzeczywiste zapisujemy również w postaci notacji naukowej (mantysa”E”+–wykładnik)
print(1e+6)        # Output: 1000000.0

# Aby odizolować z wyniku dzielenia część ułamkową, użyjemy podwójnego znaku dzielenia
print(3.0 // 2.0)    # Output: 1.0


# Dopuszczalna notacja dla "nie jest liczbą" - Not a number
#print(float("nan"))
print(float("NaN"))

# Dopuszczalna notacja dla nieskonczoności - inf/infinity
print(float("inf"))
#print(float("InF"))
#print(float("InFiNiTy"))


## Liczby zespolone
# w Pythonie zapisywane jako suma części rzeczywistej i części urojonej. 
# Część urojona definiowana jest przez dostawianie na końcu wyrażenia literki "j",
# gdy w wyrażeniu występuje min. jedna liczba urojona, output jest liczbą zespoloną.

print(-2.+2j)      # Output: (-2+2j)
#print(-3j/2)       # Output: (-0-1.5j)

print(type(-2.+2j))

print(complex(a)) # Output: (5+0j)
# W liczbach zespolonych operacje: mod ( % ) oraz floor( // ) są niedostępne.


## Operacje na liczbach
# Python zawiera następujące funkcje, które wykonują obliczenia matematyczne (bez konieczności importowania modułu math)
# Lista wszystkich metod w dokumentacji
# https://docs.python.org/3.8/library/stdtypes.html#numeric-types-int-float-complex

# Dystans między liczbą m a zerem
print(abs(m))  # |m| = 3

# Wyróżnij max spośród podanych liczb
print(max(a, b, c, m))

# Wyróżnij min spośród podanych liczb
print(min(a, b, c, m))

# Zaokrąglij liczbę, round(x [, n] ), gdzie n wskazuje do ilu liczb po przecinku zostanie zokrąglona liczba, 
# jeżeli zostawimy n puste to domyslnie przypisywana jest wartość n = 0.
print(round(sum, 3))
