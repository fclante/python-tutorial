# Introduktion Til Python Programmering

## Indholdsfortegnelse

- [Installation af Python](#installation)
- [Installation af Thonny](#installation-af-thonny)
- [Hello World](#hello-world)
- [Variables](#variabler)
- [Datatypes/DataTyper](#data-types--datatyper)
  - [Integer](#integer)
  - [Float](#float)
  - [String](#string)
  - [List](#list)
- [Operators/Operatorer](#operators--operatorer)
  - [Math](#math--matematik)
  - [Comparison](#comparison--sammenligning)
  - [Logical](#logical--logiske)
- [Conditionals/Betingelser](#conditionals--betingelser)
- [Loops/Løkker](#loops--løkker)
- [Functions/Funktioner](#functions--funktioner)
- [MicroPython](#micropython)

## Installation

Download filen via linket herunder og kør den (Dobbeltklik på filen) og følg instruktionerne på skærmen.

[Download Python](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)

## Installation af Thonny

Thonny er et IDE (Integrated Development Environment) til Python. Det er et program, der gør det nemmere at skrive Python kode.

> Download til Windows, Linux eller Mac OS X

[Thonny](https://thonny.org/)

## Hello World

Et 'Hello World' Er et lille program, der skriver 'Hello World' til skærmen.
Det er et program, der bruges til at teste, om programmeringssproget er installeret korrekt.

[Se eksempel](https://crumb.sh/6FPiVq8p6J2)

## Variabler

Variabler er en måde at gemme data på. Det kan f.eks. være et tal eller en tekst.

[se eksempel](https://crumb.sh/bQJUKXz9cK5)

## Data types / DataTyper

Datatyper er f.eks. tal, tekst, sandt/falsk, lister og meget mere.

[overblik over datatyper](https://python.land/python-data-types#Basic_and_advanced_Python_data_types)

### Integer

Heltal er tal uden decimaler. F.eks. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

```python
age = 10
```

### Float

Float er tal med decimaler. F.eks. 1.5, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0

```python
pi = 3.14
```

### String

String er tekst. F.eks. "Hej", "Dette er en tekst", "Dette er en anden tekst"

```python
name = "Mikkel"
```

### List

List er en samling af data. F.eks. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Operators / Operatorer

Operators er en måde at lave beregninger på. F.eks. plus, minus, gange, dividere, sammenligne og meget mere.

### Math / Matematik

De matematiske operatorer er:

- `+` plus
- `-` minus
- `*` gange
- `/` dividere
- `**` opløftet i
- `%` modulo (resten af en division)

```python
# plus
1 + 1 = 2

# minus
1 - 1 = 0

# gange

1 * 1 = 1

# dividere

1 / 1 = 1

# opløftet i også kaldet eksponent. Oftest noteret med ^. F.eks. 2^2 = 4

2 ** 2 = 4

# modulo (resten af en division), f.eks. 10 / 2 = 5 med resten 0

10 % 2 = 0 # Da 10 kan deles med 2 uden rest
```

### Comparison / Sammenligning

De sammenlignende operatorer er:

- `==` er lig med
- `!=` er ikke lig med
- `>` større end
- `<` mindre end
- `>=` større end eller lig med
- `<=` mindre end eller lig med

```python

# is equal to / er lig med
1 == 1 # True

# is not equal to / er ikke lig med
1 != 1 # False

# greater than / større end
1 > 1 # False

# lesser than / mindre end
1 < 1 # False

# greater than or equal to / større end eller lig med
1 >= 1 # True

# lesser than or equal to / mindre end eller lig med
1 <= 1 # True
```

### Logical / Logiske

De logiske operatorer er:

- `and` og
- `or` eller
- `not` ikke

```python
# and
1 == 1 and 2 == 2 # True

# or
1 == 1 or 2 == 2 # True

# not
not 1 == 1 # False
```

## Conditionals / Betingelser

Conditionals er en måde at lave betingelser på. F.eks. hvis noget er sandt, så gør noget andet.

> Hvis 1 er lig med 1, så skriv "1 er lig med 1"

```python
if 1 == 1:
    print("1 er lig med 1")
```

> Hvis 1 er lig med 1, så skriv "1 er lig med 1", ellers skriv "1 er ikke lig med 1"

```python
if 1 == 1:
    print("1 er lig med 1")
else:
    print("1 er ikke lig med 1")
```

> Hvis 1 _ikke_ er lig med 2 så skriv "1 er ikke lig med 2"

```python
if not 1 == 2:
    print("1 er ikke lig med 2")
```

> Hvis 10 er større end 5, så skriv "10 er større end 5", ellers skriv "10 er ikke større end 5"

```python
if 10 > 5:
    print("10 er større end 5")
else:
    print("10 er ikke større end 5")
```

> Hvis 10 mindre end eller lig med 5, så skriv "10 er mindre end eller lig med 5", ellers skriv "10 er ikke mindre end eller lig med 5"

```python
if 10 <= 5:
    print("10 er mindre end eller lig med 5")
else:
    print("10 er ikke mindre end eller lig med 5")
```

## Loops / Løkker

Loops eller Løkker er en måde hvorpå man kan gennemløbe en liste eller en anden samling af data, og gøre noget med hvert element i listen.

> Gør noget med hvert element i listen

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)
```

output er:
  
  ```text
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  ```

> Gør noget med hvert element i listen, hvis det er et lige tal

```python
for number in numbers:
  if number % 2==0:
    print(f'{number} er et lige tal')
```

output er:

```text
2  er et lige tal
4  er et lige tal
6  er et lige tal
8  er et lige tal
10 er et lige tal
```

> Uendeligt loop

```python
while True:
    print("Hello World")

# output er "Hello World" i uendelighed
```

## Functions / Funktioner

Funktioner er en måde hvorpå vi kan genbruge kode. F.eks. hvis vi skal gøre det samme flere gange.

```python
# definer en funktion
def hello_world():
    print("Hello World")

# kald funktionen
hello_world()

# output er "Hello World"
```

En funktion kan også tage imod parametre.

```python
# definer en funktion, der tager imod en parameter
def hello(name):
    print(f"Hello {name}")

# kalder funktionen med en parameter, her en String med værdien "Mikkel".
hello("Mikkel")

# output er "Hello Mikkel"
```

## MicroPython

MicroPython er en version af Python, der er optimeret til at køre på små computere, som f.eks. en micro:bit.

[MicroPython](https://micropython.org/)
