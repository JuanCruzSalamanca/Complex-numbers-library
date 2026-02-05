# Libreria números complejos

La libreria puede realizar siete operaciones de números complejos. Cada número de entrada se debe escribir como un tupla ``(a,b)`` que representara el número complejo $a + bi$. Las operaciones que puede realizar esta calculadora son:

## 1. Suma
Dados dos números complejos $C_1 = (a_1, b_1)$ y $C_2 = (a_2, b_2)$, la calculadora sigue la siguiente fórmula para realizar $C_1 + C_2$:

$$
    C_1 + C_2 = (a_1 + a_2, b_1 + b_2)
$$

## 2. Resta
Dados dos números complejos $C_1 = (a_1, b_1)$ y $C_2 = (a_2, b_2)$, la calculadora sigue la siguiente fórmula para realizar $C_1 - C_2$:

$$
    C_1 - C_2 = (a_1 - a_2, b_1 - b_2)
$$
## 3. Multiplicación
Dados dos números complejos $C_1 = (a_1, b_2)$ y $C_2 = (a_2, b_2)$, la calculadora sigue la siguiente fórmula para realizar $C_1 \times C_2$:

$$
    C_1 \times C_2 = (a_1a_2 - b_1b_2, a_1b_2 + a_2b_1)
$$
## 4. División
Dados dos números complejos $C_1 = (a_1, b_1)$ y $C_2 = (a_2, b_2)$, la calculadora sigue la siguiente fórmula para realizar $\frac{C_1}{C_2}$:

$$
    \frac{C_1}{C_2} = \frac{C_1 \times \overline{C_2}}{|C_2|^2}
$$

## 5. Módulo
Dado un número complejo $C_1 = (a_1, b_1)$, la calculadora sigue la siguiente fórmula para realizar $|C_1|$:

$$
    |C_1| = \sqrt{a_1^2 + b_1^2}
$$

## 6. Conjugado
Dado un número complejo $C_1 = (a_1, b_1)$, la calculadora sigue la siguiente fórmula para realizar $\overline{C_1}$:

$$
    \overline{C_1} = (a_1, -b_1)
$$

## 7. Conversión sistema de coordenadas
### Coordenadas cartesianas a polares
Dado un número complejo $C_1 = (a_1, b_1)$ en coordenadas cartesianas, la calculadora hace la conversión a coordenadas polares con las siguientes fórmulas:

$$
    \rho =  \sqrt{a_1^2 + b_1^2}
$$

$$
    \theta = \arctan{\frac{b_1}{a_1}}
$$

### Coordenadas polares a cartesianas
Dado un número complejo $C_1 = (\rho, \theta)$ en coordenadas polares, la calculadora hace la conversión a coordenadas cartesianas con las siguientes fórmulas:

$$
    a = \rho\cos{\theta}
$$

$$
    b = \rho\sin{\theta}
$$