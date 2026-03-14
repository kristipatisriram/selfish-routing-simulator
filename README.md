# Selfish Routing Simulator

This project implements a simple simulation of selfish routing in congestion games, a core topic in Algorithmic Game Theory.

Drivers choose routes selfishly to minimize their own travel time. The simulator computes:

• Nash equilibrium via best-response dynamics  
• Socially optimal routing  
• Price of Anarchy (PoA)

The system supports different latency functions such as:

L(x) = x  
L(x) = x^2  
L(x) = x^3  

These experiments illustrate how selfish behavior affects overall system efficiency.

## Example Output

Drivers: 1000

Equilibrium:
Route0 drivers: 990  
Route1 drivers: 10  

Optimal:
Route1 drivers: 5  

Price of Anarchy ≈ 1.0025

## Concepts Demonstrated

- Nash Equilibrium
- Congestion Games
- Price of Anarchy
- Best Response Dynamics
- Social Cost Minimization

## Run the Simulation




## Future Work

- Network routing games on graphs
- Visualization of congestion dynamics
- Braess’s paradox simulation
