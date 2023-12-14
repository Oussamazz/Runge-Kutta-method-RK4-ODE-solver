# Exponential Decay ODE Solver

## Overview

This Python script demonstrates the numerical solution of an exponential decay ordinary differential equation (ODE) using the fourth-order Runge-Kutta method. The ODE describes the decay of a quantity over time, and the script provides a visual representation of the decay process.

## Files

- `exponential_decay_solver.py`: Python script containing the ODE solver function and code to visualize the solution.

## Dependencies

- `numpy`: Used for numerical operations.
- `matplotlib`: Used for plotting the numerical solution.

## Usage

1. Ensure you have the required dependencies installed:

   ```bash
   pip install numpy matplotlib
   ```

2. Run the script:

   ```bash
   python rk4.py
   ```

3. Adjust the parameters in the script, such as the initial conditions, decay rate (`k`), and time interval, to explore different scenarios of exponential decay.

## Example

The default example in the script considers an exponential decay ODE with an initial quantity of 1, a decay rate (`k`) of 0.5, and a time interval from 0 to 5 with a step size of 0.1. The resulting numerical solution is plotted using Matplotlib.

