import numpy as np

G = 6.67430e-11  # Gravitational constant (SI units) - or scale as needed

def compute_accelerations(bodies):
    """
    Compute and return an array of accelerations for each body
    due to gravitational attraction from all other bodies.
    """
    n = len(bodies)
    accs = np.zeros((n, 3))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                r_ij = bodies[j].position - bodies[i].position
                dist_sq = np.dot(r_ij, r_ij)
                dist = np.sqrt(dist_sq)
                # Prevent division by zero in any corner case
                if dist_sq == 0:
                    continue
                # Acceleration from j on i
                accs[i] += G * bodies[j].mass / dist_sq * (r_ij / dist)
    return accs

def verlet_step(bodies, dt):
    """
    Symplectic Verlet integrator step.
    """
    # 1. Calculate accelerations at t
    accs = compute_accelerations(bodies)

    # 2. Update positions to t+dt
    for i, body in enumerate(bodies):
        body.position += body.velocity * dt + 0.5 * accs[i] * dt**2

    # 3. Calculate accelerations at t+dt
    new_accs = compute_accelerations(bodies)

    # 4. Update velocities to t+dt
    for i, body in enumerate(bodies):
        body.velocity += 0.5 * (accs[i] + new_accs[i]) * dt

def euler_step(bodies, dt):
    """
    Simple (but less accurate) Euler integrator step.
    """
    accs = compute_accelerations(bodies)
    for i, body in enumerate(bodies):
        body.velocity += accs[i] * dt
        body.position += body.velocity * dt
