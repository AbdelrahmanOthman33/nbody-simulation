# N-Body Simulation Explanations

## Mathematical Formulation

We use Newton's law of gravitation:

\[
F_{ij} = G \frac{m_i m_j}{r_{ij}^2} \hat{r}_{ij}
\]

where \( \hat{r}_{ij} \) is the unit vector from body \( i \) to body \( j \), and \( G \) is the gravitational constant.

## Numerical Integration

Common integrators:
- **Verlet** (Symplectic, great for orbital problems)
- **Runge-Kutta** (High-accuracy method)

## Visualization

We use Matplotlib or another library to animate the positions of bodies over time.
