import argparse
import json
import numpy as np
from nbody.bodies import CelestialBody
from nbody.integrators import verlet_step, euler_step

def run_simulation(bodies, dt, steps, method='verlet'):
    """
    Run N-body simulation with specified integrator method.
    """
    positions_over_time = []
    integrator = verlet_step if method == 'verlet' else euler_step
    
    for _ in range(steps):
        positions_over_time.append([(body.name, body.position.copy()) for body in bodies])
        integrator(bodies, dt)

    return positions_over_time

def main():
    parser = argparse.ArgumentParser(description="Run N-body simulation.")
    parser.add_argument("--config", type=str, required=True,
                        help="Path to simulation config JSON.")
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = json.load(f)

    dt = config["dt"]
    steps = config["steps"]
    method = config["method"]

    # Create bodies
    bodies = []
    for body_conf in config["bodies"]:
        body = CelestialBody(body_conf["name"],
                             body_conf["mass"],
                             body_conf["position"],
                             body_conf["velocity"])
        bodies.append(body)

    # Run simulation
    results = run_simulation(bodies, dt, steps, method)

    # For demonstration, just print final positions
    print("Final positions:")
    for b in bodies:
        print(b)

if __name__ == "__main__":
    main()
