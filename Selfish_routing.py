import random
import matplotlib.pyplot as plt

n=int(input("Enter no of drivers:"))
exponents = []
poa_values = []

def latency_route0(x):
    return 10

def latency_route1(x):
    return x ** d

def count_route_drivers(routes):
    r0=routes.count(0)
    r1=routes.count(1)
    return r0,r1

def get_latencies(routes):
    r0,r1 = count_route_drivers(routes)

    t0 = latency_route0(r0)
    t1 = latency_route1(r1)

    return t0,t1

def update_driver(routes,driver):
    r0,r1 = count_route_drivers(routes)

    t0 = latency_route0(r0)
    t1 = latency_route1(r1)

    current = routes[driver]

    if current == 0 and t1 < t0:
        routes[driver] = 1
    
    elif current == 1 and t0 < t1:
        routes[driver] = 0

def social_cost(routes):
    r0, r1 = count_route_drivers(routes)
    cost = r0 * latency_route0(r0) + r1 * latency_route1(r1)
    return cost

def optimal_distribution(n):
    best_cost = float("inf")
    best_x = None

    for x in range(n+1):
        r1 = x
        r0 = n-x

        cost = r0 * latency_route0(r0) + r1 * latency_route1(r1)

        if cost < best_cost:
            best_cost = cost
            best_x = x
        
    return best_x,best_cost

def runsim(routes, iterations=100):

    for i in range(iterations):
        for j in range(len(routes)):
            update_driver(routes, j)
    
    return routes

for d in range(1,6):
    
    

    routes=[random.randint(0,1) for i in range(n)]
    routes = runsim(routes)

    total_poa = 0

    for trial in range(10):
        routes = [random.randint(0,1)for i in range(n)]
        routes = runsim(routes)
        eq_cost = social_cost(routes)
        opt_x,opt_cost = optimal_distribution(n)
        total_poa += eq_cost/opt_cost

    avg_poa = total_poa/10

    r0,r1 = count_route_drivers(routes)
    
    print("Route 0 drivers:", r0)
    print("Route 1 drivers:", r1)
    
    print("Travel time of Route 0:",latency_route0(r0))
    print("Travel time of Route 1:",latency_route1(r1))
    
    eq_cost = social_cost(routes)
    opt_x, opt_cost = optimal_distribution(n)
    PoA = eq_cost / opt_cost
    
    exponents.append(d)
    poa_values.append(PoA)

    print("Equilibrium cost:", eq_cost)
    print("Optimal distribution route1:", opt_x)
    print("Optimal cost:", opt_cost)
    print("Price of Anarchy:", PoA)

plt.plot(exponents, poa_values, marker='o')

plt.xlabel("Congestion exponent (d)")
plt.ylabel("Price of Anarchy")
plt.title("Effect of congestion severity on system inefficiency")

plt.grid(True)
plt.show()