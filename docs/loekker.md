# Loops / Løkker

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

---
[tilbage](/README.md)
