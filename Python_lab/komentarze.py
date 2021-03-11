## 0. Komentarze 

# W programowaniu komentarze są klarownym wyjaśnieniem w kodzie.
# Komentarze znajdują się w kodzie źródłowym do czytania przez ludzi, 
# przeważnie są pomijane przez kompilatory i tłumacze, mają ułatwić zrozumienie kodu źródłowego. 


# Pierwszy przykład --> 

# Komentarze w Pythonie zaczynają się od znaku krzyżyka (ang. hash mark),
# czyli znak # oraz białego znaku i kończą się na końcu linii.
# Python tak naprawdę nie ma składni dla komentarzy wieloliniowych.
# Aby dodać komentarz wielowierszowy, możesz wstawić # dla każdej linii, lecz ...


# Drugi przyklad -->

"""
W Pythonie zobaczymy wielowierszowe komentarze (komentarze typu multiline).
Używany jest w tym celu trzykrotny cudzyslów.
Nie jest to optymalny sposób. Poniżej cytat Guido van Rossum, twórca Pythona: 
>> Python does not support multi-line comments like C/C++ or Java. 
>> However there is nothing to stop you to use multi-line docstrings as multi-line comments."

Natomiast aby napisać komentarz w Pythonie pot. "wykomentować skrypt",
polecam stosować skróty klawiszowe. 

Przykładowo w IDLE:
- Multiline comment, zaznacz kod który chcesz skomentować i wciśnij pryzciski Alt + 3.
- By odblokować istniejący komentarz, zaznacz kod i wciśnij pryzciski Alt + 4.

"""

# Drugi przyklad cd -->

''' 
Spotkamy się także z powyżej stosowaną notacją do wielowierszowych komentarzy, używając "pojedynczego cudzysłowu". 
czesto aby dokumentować specyficzny segment kodu, który używany jest jak komentarz. 
Ciągi dokumentacyjne, znane rownież jako docstring. Więcej, URL: https://www.python.org/dev/peps/pep-0257/
Przykładowo: liczby zespolone - def complex(real=0.0, imag=0.0).

'''
