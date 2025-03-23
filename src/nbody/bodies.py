import numpy as np

class CelestialBody:
    """
    Represents a celestial body with a position, velocity, mass, and name.
    """
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

    def __repr__(self):
        return f"CelestialBody({self.name}, mass={self.mass}, pos={self.position}, vel={self.velocity})"
