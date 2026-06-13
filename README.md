# PROGRAMMING-EMILIO-CASTILLO-Q2-2026
# Numerical Integration Calculator

**Repository:** UPY-PROGRAMMING-EMILIO-CASTILLO-Q2-2026
**Course:** Programming – Unit 2 (Q2-2026)
**Language:** Python 3.x
**Version Control:** Git | **Hosting:** GitHub

---

## Project Description

This script (`cw06.py`) implements **numerical integration** using four classical Riemann sum methods. Given a mathematical function `f(x)` and an interval `[a, b]`, it approximates the definite integral by dividing the area under the curve into `n = 1000` subintervals and summing their areas.

The program supports the following integration methods:

| Method | Code | Description |
|--------|------|-------------|
| Left Riemann Method | `LRM` | Evaluates f(x) at the **left** edge of each subinterval |
| Right Riemann Method | `RRM` | Evaluates f(x) at the **right** edge of each subinterval |
| Midpoint Riemann Method | `MRM` | Evaluates f(x) at the **center** of each subinterval |
| Trapezoidal Rule | `TRAP` | Averages f(x) at both edges, forming trapezoids |

---

## How It Works

### 1. Input
The user provides four values interactively:
- `a` — left endpoint of the interval (supports `pi`, e.g. `2*pi`)
- `b` — right endpoint of the interval
- `f_x` — the function to integrate, written as a Python expression using `x` (e.g. `x**2 + 3*x`)
- `method` — one of `LRM`, `RRM`, `MRM`, or `TRAP`

### 2. Pi Handling
If `a` or `b` contains the string `"pi"`, it is evaluated using `math.pi`; otherwise it is converted directly to a `float`. This allows inputs like `2*pi` or `pi/2`.

### 3. Initialization
```
n       = 1000          # number of subintervals
h       = (b - a) / n   # width of each subinterval
area    = 0.0           # accumulator for the total area
shift   = 0             # index offset (used by RRM)
constant = 0            # horizontal offset (used by MRM)
```

### 4. Integration Methods

#### LRM — Left Riemann Method (default)
Evaluates `f(x)` at the left edge of each subinterval (`xi = a + i*h`) for `i` from `0` to `n-1`.

#### RRM — Right Riemann Method
Sets `shift = 1` so the loop runs from `i = 1` to `n`, evaluating `f(x)` at the right edge of each subinterval.

#### MRM — Midpoint Riemann Method
Sets `constant = h/2` so each evaluation point is shifted to the center of its subinterval (`xi + h/2`).

#### TRAP — Trapezoidal Rule
Uses a different formula: it averages the function values at both edges of each subinterval. The total area is calculated as:

```
area = (h/2) * [f(a) + 2·f(x₁) + 2·f(x₂) + ... + 2·f(xₙ₋₁) + f(b)]
```

The first and last terms (`f(a)` and `f(b)`) are added only once; all interior points are multiplied by 2.

### 5. Output
```
the integration of <f_x> is <area>
```

---

## Flowchart

The diagram below summarizes the full program logic:

![Flowchart](FlowChart.png)

---

## Environment & Tools

- **Language:** Python 3.x
- **Standard library used:** `math` (for `math.pi`)
- **Version Control:** Git
- **Hosting Platform:** GitHub

---

## How to Run

1. Make sure Python 3 is installed on your system.
2. Clone this repository:
   ```bash
   git clone https://github.com/3milioCM/UPY-PROGRAMMING-EMILIO-CASTILLO-Q2-2026.git
   ```
3. Navigate to the project directory:
   ```bash
   cd UPY-PROGRAMMING-EMILIO-CASTILLO-Q2-2026
   ```
4. Run the script:
   ```bash
   python cw06.py
   ```
5. Follow the prompts:
   ```
   write the left endpoint of the interval: 0
   write the right endpoint of the interval: pi
   write the function to integrate: x**2
   Write the integration method (LRM/RRM/MRM/TRAP): TRAP
   ```

---

## Example

**Input:**
- `a = 0`, `b = pi`
- `f(x) = x**2`
- Method: `MRM`

**Output:**
```
the integration of x**2 is 10.335...
```

---

## Notes

- The function `f_x` is evaluated using Python's built-in `eval()`. Write it using standard Python math syntax:
  - Powers: `x**2` (not `x^2`)
  - Multiplication: `3*x` (not `3x`)
  - Trig functions require `math.` prefix: `math.sin(x)`, `math.cos(x)`
- Accuracy improves with larger `n`; the current default of `1000` provides a good balance between speed and precision.

---

*Developed for the Programming course, Unit 2 – Universidad Politécnica de Yucatán, Q2-2026.*
Yo, Emilio Eduardo Castillo Manzano, declaro que NO he utilizado herramientas de Inteligencia Artificial para la elaboración de este trabajo académico. Afirmo que cuento con evidencias físicas y/o digitales que demuestran mi autoría, incluyendo pero no limitándose a: documentos manuscritos, materiales impresos con anotaciones o subrayado, historial de versiones de documentos electrónicos, o commits en repositorios de código.

Reconozco y acepto que el profesor se reserva el derecho de solicitar dichas evidencias en cualquier momento, especialmente cuando existan sospechas o se detecten conductas que atenten contra la integridad académica, tales como plagio o uso no reportado de herramientas de IA.
