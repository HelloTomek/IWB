# Ciągi znaków w Pythonie otoczone są pojedynczymi lub podwójnymi cudzysłowami.
# Notacja: (''), (""), (''' '''), (""" """").
# String jest to typ sekwencyjny - w jednej zmiennej możemy przechować wiele wartości.

tagi = '#string#napisy#tekst#ciagi_znakow#apostrofy#cudzyslowy \
str'
print(tagi) # multiline albo \

"""USER INPUT"""

a = input('input a: ') 
b = input('input b: ')

c = a+b
print(c)

# Dane typu String w Pythonie są niezmienne (ang. immutable - niemutowalne).

t1 = "iwB" 
t2 = t1.replace("i", input()) 

print(t1) #iwB
print(t2) #IwB

# Spójrzmy zatem blizej na formatowanie ciągów i niektóre metody stosowane na danych typu String. 

                                           
hello, world, hw = 'hello', "world", """Hello World"""
#tag = '#string#napisy#tekst#ciagi_znakow/n#apostrofy#cudzyslowy'
#print(hello); print(world)
#print(hello, world)

# Konkatencja - w programowaniu oznacza łączenie dwóch wyrażeń.
hello_world = hello + ' ' + world
print(hello_world)


# Argumenty pozycyjne
print("{h}{w}".format(h=hello, w=world))

# Padding 
print('{:>10}'.format(hello))
print('{:^10}'.format(world))

# F-Strings (w Python pow. 3.6)
print(hello_world)
print(f'przykladowy tekst: {hello}\n{world}, w nowej linii!')

## Formatowanie ciągów znaków
# Zmieniamy format (castowanie), aby wymusic format danych typu String, mozemy skorzystac z wbudowanej funkcji str().
# str() - tworzy string ze zroznicowanego typu danych, tj. strings, integer literals oraz float literals.

# W ponizszym przypadku z liczby na tekst 

print(type(str(1)))

# Print zakończony jest „niewidzialnym” znakiem nowej linii (\n), mozemy sie od tego uwolnić

print(hello, end='')
print(world) # Output: helloworld

## Metody ciągów znaków
## Lista wszystkich metod w dokumentacji
# https://docs.python.org/3.8/library/stdtypes.html#string-methods

# Python zapewnia zwięzłą składnię dla danych typu String 

# np. do tworzenia podlisty ze str (sublist), 
# aby uzyskać dostęp do podzbiorow ciagow znakow, mozemy skorzystac z metody znanej jako 
# Python String Slicing, wg. zasady: s[:i] + s[i:] == s, dla dla kazdego index'u i 

# String slicing - ciecie napisow 

print(hello_world[4:-4]) # o w

print(hw[1:6])          # tniemy napis od index'u 1 do 6 (exclusive) 
print(hw[3:])           # tniemy napis od index'u 3 do konca
print(hw[:3])           # tniemy od poczatku napisu do index'u 3 (exclusive)
print(hello[:-1])       # ciecie negatywne, liczone od konca - index 
print(hello[::-1])      # ciecie odwrotne, step -1
print(hello[:])         # zwraca nam caly napis w niezmienionej formie


print(hw.index('H')) # test 'h' - err
print(hw.index('o')) # pierwsze indeks o, ktory zostal napotkany.



## Edytowanie wyswietlania napisow
# Prawostronnie wyjustowany napis, padding spacjami
print(hello.rjust(10)) #      hello

# Centrujemy napis, padding spacjami
print(world.center(10)) #   world    



# Rozszczepiamy napis - dzielimy napis według separatora(spacja jeśli nie podano).
# Zwracane sa podciągi w formie listy.

print(hw.split()) # hw.split(' ') 
print(tagi.split('#'))

sub = 'o'
print(tagi.split(sub))

#print(hw.split(str="", num=string.count(str)))
print("\nSplit ---->") # """ multiline na pocz dla roznicy
print(tagi.splitlines()) # tagi.count('\n')
print("<----\n")


# Zamieniamy znak/znaki
print(hw.replace('Hello', 'Bye'))

# Wszystkie jako uppercase 
print(hello.upper()) # HELLO

# Wszystkie jako lowercase 
print(world.lower()) # world

# Napis jako tytuł
print(hw.title()) # Hello World

# Zmienia pierwszą literę w ciągu na dużą
print(hw.capitalize()) # Hello world

# Odwraca rodzaj każdej litery – małe na duże, duże na małe
print(hello_world.swapcase()) # HELLO WORLD


# Output typ int - zmierz dlugość napisu
print(len(hello))

# Output typ int - zlicz ile razy wystepuje nasz substring w napisie
print(f'ile razy pojawia sie litera "{sub}" w napisie: "{hw}"? \
Tyle razy: ', hw.count(sub))


# Znajdz pozycje
print(hello.find('e'))


# Output typ boolean - poczatek sekwencji znakow
print(hw.startswith('Hello'))

# Output typ boolean - koniec sekwencji znakow
print(world.endswith('d'))

# Output typ boolean  - Wszystkie jako alphanumeric
print(world.isalnum())

# Output typ boolean - Wszystkie jako alphabetic
print(hello.isalpha())

# Output typ boolean - Wszystkie jako numeric
print(hw.isnumeric())         # False


## Znaki specjalne notacja backslesh'owa oraz hex, wyjasnienie: 
# \a	  0x07	Alert
# \b	  0x08	Backspace
# \cx	 	Control-x
# \C-x	 	Control-x
# \e	  0x1b	Escape
# \f	  0x0c	Formfeed
# \M-\C-x	 Meta-Control-x
# \n	  0x0a	Nowa linia
# \nnn	  Osemkowa Notacja, gdzie n is in the range 0.7
# \r	  0x0d	return
# \s	  0x20	Spacja
# \t	  0x09	Tab
# \v	  0x0b	Vertical tab
# \x	  Character x
