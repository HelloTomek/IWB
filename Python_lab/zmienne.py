## 1. Zmienne i ich typy

# Zmienne w Pythonie stosuje się do przechowywania wartości dowolnego typu.
# Utworzenie zmiennej wiąże się z nadaniem jej wartości bazowej (initial value).

## ZMIENNE - ZASADY:
#  - W nazwach zmiennych rozróżniana jest wielkość liter (np. zmienna: nazwa i NAZWA, to dwie różne zmienne).
#  - Muszą one zaczynać się od litery lub znaku podkreślenia.
#  - Nazawa zmiennej może mieć liczby, ale nie może zaczynać się od cyfry.
#  - Zmienne nie mogą nosić takiej samej nazwy jak słowa kluczowe w Pythonie.

c = 'case sensitive' 
print(type(c))

# Listę słów kluczowych w aktualnej wersji można zawsze uzyskać, wpisując następujące polecenia:

import keyword
print(keyword.kwlist) # Słowa kluczowe Pythona w formie listy, output:
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'

# Trzy zmienne przypisane są do jednej wartości 2 (Przypisane do jednego miejsca w pamięci):
a = b = c = 2  # Właśnie nadpisaliśmy wartość zmiennej c.
print(c)

# Wiele wartości przypisano do różnych zmiennych:
a, b, c = 1, '2', "Witaj w Pythonie"     # Zauważmy, właśnie nadpisaliśmy wartośći zmiennych.
print(a)
print(type(a))

print(b)
print(type(b))

b = input()  # Oczekiwanie na wprowadzenie ciągu znaków. 
b = b*2      # Nowa wartość zmiennej może być wyliczona o dotychczasową wartość tej zmiennej.
# b*=2
print(b)


## Utarte normy

# W celu poprawienia czytelności, zrozumiałości kodu programu - nadawanie nazw definiowane jest
# zgodnie z PEP czyli Python Enhancement Proposal, 
# oficjalny dokument informacyjny dla społeczności programistów Pythona (URL: https://www.python.org/dev/peps/pep-0008/).

# Co trzeba zrobić, aby poprawnie wyświetlać polskie znaki diakrytyczne?

NieZacyNAćZwielkich_liter = "To jest niepoprawnie nazwana zmienna" # Zła praktyka na nazywanie zmeinnej, źle jest np. zmienna ZacyNAćZwielkich_liter.
nazwazmienna = "To jest poprawnie nazwana zmienna" # Poprawnie: nazwazmienna, ale i nazwa_zmienna, nazwazmienna1, czy nazwa_zmienna_1 jest również dobrze wg. ustalonych norm.

NieZacyNAćZwielkich_liter; nazwazmienna # Wykonujemy dwa polecenia Pythona w jednym wierszu. 

# Usuwamy zmienną poleceniem: del nazwa_zmiennej, np.: 
del NieZacyNAćZwielkich_liter

# Exception has occurred: NameError name 'ZacyNAćZwielkich_liter' is not defined
print(NieZacyNAćZwielkich_liter) 
