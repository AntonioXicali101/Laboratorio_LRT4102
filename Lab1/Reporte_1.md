# Report_1_174527

## Introduction

Python is an interpreted, high-level, and easy-to-read programming language, used both for application development and for data analysis. Its straightforward syntax allows beginners to quickly grasp the fundamentals, and it has a large community that contributes libraries and solutions for a wide range of needs.

### Variable types

Variable types in Python:

    •int: Represents integer numbers (e.g., 5, -3).
    •float: Stores decimal or floating-point numbers (e.g., 3.14, -2.7).
    •str (string): Contains text strings (e.g., "Hello world").
    •bool (boolean): Can only take the values True or False.
    •list: An ordered, mutable collection of elements (e.g., [1, 2, 3]).
    •dict (dictionary): A key-value mapping structure (e.g., {"name": "Ana", "age": 25}).

### Control structures

In Python, there are several control structures that allow you to direct the flow of a program’s execution. One of them is the **while** loop, which repeats as long as the specified condition remains true and stops when it no longer holds. The **for** loop, on the other hand, iterates over each element of a sequence (such as a list or tuple), executing the same block of code for each element. For decision-making, the **if** conditional structure is used, complemented by **else if** and **else**, which evaluate sequential conditions and execute the corresponding block of code depending on whether they are true or false. Finally, there are keywords like **break**, which completely interrupts a loop; **continue**, which skips to the next iteration; and **pass**, which acts as a placeholder without performing any concrete action.


# Object-Oriented Programming in Python

**Object-Oriented Programming (OOP)** in Python organizes code around entities called **classes**, which act as templates for creating objects with attributes and methods. This approach allows for a clear and modular structure by grouping related data and behaviors in one place.

Its main components are classes, objects, attributes, and methods. A class is defined using the reserved word `class`, and when it is instantiated, it generates objects with their own characteristics and behaviors. Additionally, OOP utilizes concepts such as **encapsulation**, which protects data, and **inheritance**, which facilitates code reuse and extension by sharing properties among classes.

To use OOP in Python, you first define the class (for example, `Persona`) with an `__init__` constructor method that initializes the attributes, along with methods that describe its actions. Then, you create objects from the class, each with its own set of attribute values but sharing the same functions and behaviors.

# Problems

## Problem 1

Write a program that reads a positive integer "n" entered by the user and then displays on the screen the sum of all integers from 1 to 
n.

```python
def main():

    n = int(input("Introduce un entero positivo: "))

    suma = n * (n + 1) // 2 

    print(f"La suma de los primeros {n} enteros positivos es: {suma}")

if __name__ == "__main__":
    main()
```

The program asks the user for a positive integer \(n\) and then uses the mathematical formula for the sum of the first \(n\) positive integers, which is:

Sum = (n(n+1))/2

Finally, it displays the calculated result. This way, it does not need to perform iterative additions, but instead takes advantage of the closed-form formula.

## Problem 2

Write a program that asks the user for the number of hours worked and the hourly rate. Then, it should display the corresponding pay on 
the screen.

```python
# Solicita al usuario el número de horas trabajadas
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))

# Solicita la tarifa por hora
tarifa_por_hora = float(input("Introduce la tarifa por hora: "))

# Calcula el pago total
pago_total = horas_trabajadas * tarifa_por_hora

# Muestra el resultado
print(f"El pago correspondiente es: {pago_total}")
```

This code prompts the user to input two values: the number of hours worked and the hourly rate. It then calculates the total payment by multiplying these two values, and finally prints out the resulting amount.

## Problem 3

Create a list with the name, hourly wage, and hours worked for at least six operators.  
Print the name and the total pay for each operator.

```python
def main():
    """
    Calcula el pago total de cada operador en una lista.
    (nombre, sueldo_hora, horas_trabajadas).
    """
    
    # Lista de operadores
    personal = [
        ("Antonio", 10, 40),
        ("José", 8, 40),
        ("Ariadna", 8.5, 45),
        ("Bryan", 12, 30),
        ("Andrea", 13.5, 38),
        ("Alexa", 10.5, 44)
    ]

    # Recorremos la lista y calculamos la paga de cada operador
    for nombre_operador, tarifa_hora, horas_totales in personal:
        pago_total = tarifa_hora * horas_totales
        print(f"{nombre_operador} recibirá un pago de: {pago_total}")

if __name__ == "__main__":
    main()

```

This program defines a list of workers, each containing a name, hourly wage, and total hours worked. It then iterates over the list to calculate each worker’s total payment (wage per hour multiplied by hours worked) and prints out the result for each.

## Problem 4

* Create a list called **numeros** that contains at least 10 numbers.  
* Calculate the average of the even numbers and the product of the odd numbers.  
* Print the results.

```python
def main():
    # Create a list of at least 10 numbers
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Filter even numbers and calculate their average
    pares = [num for num in numeros if num % 2 == 0]
    promedio_pares = sum(pares) / len(pares) if pares else 0
    
    # Filter odd numbers and calculate their product
    impares = [num for num in numeros if num % 2 != 0]
    producto_impares = 1
    for num in impares:
        producto_impares *= num
    
    # Print the results
    print(f"Average of even numbers: {promedio_pares}")
    print(f"Product of odd numbers: {producto_impares}")

if __name__ == "__main__":
    main()
```

This program creates a list of integers, then separates them into two lists: even and odd numbers. It calculates the average of the even numbers (using the sum of even values divided by their count) and computes the product of all odd numbers (by multiplying them in a loop). Finally, it prints both the average of evens and the product of odds.

## Problem 5

Create a program that asks the user to guess a secret number. The program should generate a random number between 1 and 10, and the user must try to guess it. The program should provide hints if the user's guess is too high or too low. The **while** loop should continue until the user guesses correctly. In the end, the program should print how many attempts it took for the user to guess the number.

```python
import random

def main():
    # Pick a random number between 1 and 10
    numero_oculto = random.randint(1, 10)
    intentos = 0
    encontrado = False

    # Keep guessing until the user finds the correct number
    while not encontrado:
        intento = int(input("Guess a number between 1 and 10: "))
        intentos += 1

        if intento < numero_oculto:
            print("Too low!")
        elif intento > numero_oculto:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {intentos} attempts.")
            encontrado = True

if __name__ == "__main__":
    main()
```

This program generates a random number between 1 and 10, then repeatedly asks the user for a guess. After each guess, it informs the user if their guess is too high or too low. When the user guesses the correct number, it displays how many attempts were required.

## Problem 6

The program should generate a matrix of at least **5x5**.  
The robot starts its path at position **(0,0)** in the matrix and must exit at position **(4,4)** or the maximum position if the matrix 
size is changed.  

* The number and position of obstacles are random.  
* The robot can only move forward, turn left, or turn right to find a free path.  
* If the robot cannot reach the destination, it should print **"Impossible to reach the destination"** on the screen.  
* If the robot successfully reaches its final destination, it should print the map with free spaces and obstacles displayed as 
follows:  

```
o o o X o  
o o o o o  
o o o o X  
o o o o o  
o X X X o  
```

Additionally, the program should print the **route** the robot followed.  
A second map should be displayed showing the **path** taken by the robot using arrows.

### Solution


**Matrix Generation**  
The program starts by prompting the user for the size of the matrix, ensuring that it is at least 5×5. Once the size is confirmed, the matrix is initialized by randomly placing obstacles (denoted by `X`) throughout the grid, making sure that neither the starting position `(0,0)` nor the destination position `(mSize-1, mSize-1)` contains any obstacle. All remaining free positions are marked with `o`. 

**Starting and Destination Points**  
In this implementation, the robot always begins at the top-left corner `(0,0)` of the matrix. Meanwhile, the bottom-right corner `(4,4)` in a 5×5 matrix— or `(mSize-1, mSize-1)` for a larger one—serves as the robot’s destination. These positions are critical checkpoints that guide both the matrix setup (to keep them obstacle-free) and the pathfinding process.

**Robot Movement**  
The robot is permitted only to move forward, turn left, or turn right in its search for a path. Whenever the robot encounters an obstacle blocking its route, it modifies its direction accordingly and continues to explore any remaining viable paths. This process involves keeping track of each step the robot takes, ensuring that no option is left unexplored unless it is blocked by an obstacle.

**Pathfinding Logic**  
A pathfinding loop orchestrates the robot’s movements until it either successfully reaches the destination or runs out of valid moves. If the robot eventually occupies the final cell `(mSize-1, mSize-1)`, the program concludes that a path exists. Conversely, if the robot cannot find a route after evaluating all possible movements, the program determines that it is “Impossible to reach the destination.”

**Output**  
At the end of the procedure, the program presents two distinct maps. The first map shows the initial layout of the matrix, illustrating all free spaces (marked by `o`) and obstacles (denoted by `X`). The second map depicts the exact path followed by the robot, represented by directional arrows (such as `→` and `↓`). If, however, no valid path is discovered, the program simply displays the message “Impossible to reach the destination,” indicating that the robot was unable to navigate to the final cell.

# Problem 7

This solution employs the Object-Oriented Programming (OOP) paradigm to implement a simple inventory management system. The design is structured around two primary classes: `Producto` and `Inventario`, which encapsulate the behavior and data for individual products and the overall inventory, respectively. A menu-driven interface in the `main()` function allows the user to interact with the system.

## Key Components

### 1. `Producto` Class
* **Propósito:**  
  Represents a single product within the inventory.
  
* **Atributos:**  
  - `nombre`: The name of the product.  
  - `precio`: The price per unit of the product.  
  - `cantidad_en_stock`: The current stock level or quantity available.

* **Métodos:**  
  - `vender(cantidad_vendida)`:  
    Reduces the product’s stock by the specified amount if sufficient stock is available. If not, it prints a message indicating insufficient stock.
  - `mostrar_informacion()`:  
    Returns a formatted string that contains the product’s details (name, price, and stock).

### 2. `Inventario` Class
* **Propósito:**  
  Manages a collection of `Producto` objects and provides functionality to update and retrieve inventory data.
  
* **Atributos:**  
  - `productos`: A list that stores instances of the `Producto` class.
  
* **Métodos:**  
  - `agregar_producto(producto)`:  
    Adds a new `Producto` object to the inventory list.
  - `actualizar_stock(nombre, cantidad_vendida)`:  
    Searches for a product by its name and reduces its stock using the `vender` method if found.
  - `mostrar_informacion_producto(nombre)`:  
    Displays detailed information for a specific product by calling its `mostrar_informacion` method.
  - `calcular_valor_inventario()`:  
    Calculates the total value of the inventory by summing the product of each product’s price and its available stock.
  - `encontrar_producto(nombre)`:  
    A helper method that performs a case-insensitive search for a product in the inventory by its name.

### 3. `main()` Function
* **Propósito:**  
  Serves as the entry point of the program, offering a user interface to interact with the inventory system.
  
* **Flujo:**  
  1. Se crea una instancia de la clase `Inventario`.  
  2. The program enters a loop where it displays a menu with options to:
     - Add a product
     - Sell a product
     - Show product information
     - Calculate and display the total inventory value
     - Exit the program
  3. Based on the user’s choice, the corresponding methods of the `Producto` or `Inventario` classes are invoked to perform the required operations.
  4. The loop continues until the user chooses to exit.
