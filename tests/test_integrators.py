import pytest
import numpy as np
from nbody.bodies import CelestialBody
from nbody.integrators import compute_accelerations

def test_accelerations_no_overlapping():
    body1 = CelestialBody("Body1", 1e5, [0,0,0], [0,0,0])
    body2 = CelestialBody("Body2", 1e5, [1,0,0], [0,0,0])
    bodies = [body1, body2]
    accs = compute_accelerations(bodies)
    assert accs.shape == (2,3)
    # Just check it's non-zero or something expected
    assert not np.allclose(accs, 0)
