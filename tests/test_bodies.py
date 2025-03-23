import pytest
from nbody.bodies import CelestialBody

def test_celestial_body_creation():
    body = CelestialBody("Test", 1.0, [1,2,3], [0.1, 0.2, 0.3])
    assert body.name == "Test"
    assert body.mass == 1.0
    assert len(body.position) == 3
    assert len(body.velocity) == 3
