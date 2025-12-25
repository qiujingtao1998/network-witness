import numpy as np
import igraph as ig
from scipy.optimize import root_scalar
import math
from itertools import combinations
import json
import matplotlib.pyplot as plt

print("start")
round = 10  # index for different rounds
d = 2  # local dimension
n_max = 25  # maximum number of parties
n_min = 4  # minimum number of parties
n_set = [i for i in range(n_min, n_max+1)]
data = {"n_set": n_set}

def f_odd(x, g):  # the equation for the SSWs, x denotes gamma_prime=gamma*(d+1)
    equation = -1
    v_number = g.vcount()
    u = set([i for i in range(v_number)])
    for i in range(v_number//2):
        for j in combinations(range(v_number), i+1):
            v_set = set(j)
            cut = g.es.select(_between=(v_set, u - v_set))
            cut_length = len(cut)
            equation += x**cut_length
    return equation


def f_even(x, g):
    equation = -1
    v_number = g.vcount()
    u = set([i for i in range(v_number)])
    for i in range(v_number//2-1):
        for j in combinations(range(v_number), i+1):
            v_set = set(j)
            cut = g.es.select(_between=(v_set, u - v_set))
            cut_length = len(cut)
            equation += x**cut_length
    for j in combinations(range(v_number), v_number//2):
        v_set = set(j)
        cut = g.es.select(_between=(v_set, u - v_set))
        cut_length = len(cut)
        equation += 0.5 * x**cut_length
    return equation

p_sets_SSW = []  # store the visibility thresholds for SSWs
p_sets_fidelity = []  # store the visibility thresholds for fidelity-based witnesses
densities = [i for i in np.arange(0.2, 1.1, 0.2)]  # graph densities
for density in densities:
    p_set_SSW = []
    p_set_fidelity = []
    graphs = []
    for n in range(n_min, n_max+1):
        m = int(math.comb(n, 2) * density)  # number of edges
        if m < n-1:  # not enough edges to form a connected graph
            p_set_SSW.append(None)
            p_set_fidelity.append(None)
        else:
            g = ig.Graph.Erdos_Renyi(n=n, m=m)
            while not g.is_connected():  # ensure the graph is connected
                g = ig.Graph.Erdos_Renyi(n=n, m=m)
            graphs.append(g.get_edgelist())
            if n % 2 == 0:
                gamma_prime = root_scalar(f_even, args=g, bracket=[0, 1]).root
            else:
                gamma_prime = root_scalar(f_odd, args=g, bracket=[0, 1]).root
            p_SSW = d**2/(d-1)/(d+1+(d**2-1)*gamma_prime) - 1/(d**2-1)
            p_set_SSW.append(p_SSW)
            p_fidelity = (np.power(d, 2-g.mincut().value/m)-1)/(d**2-1)
            p_set_fidelity.append(p_fidelity)
    p_sets_SSW.append(p_set_SSW)
    p_sets_fidelity.append(p_set_fidelity)
    # the following three lines are used to save data for each density
    data_density = {"density": density, "n_set": n_set, "p_set_SSW": p_set_SSW, "p_set_fidelity": p_set_fidelity, "graphs": graphs}
    with open(f'densities/density{density}(n={n_max})({round}).json', 'w') as f:
        json.dump(data_density, f)
    print(f"Density={density} done.")


# calculating the complete graph individually to reduce time complexity
# even N=2k; x: gamma*(d+1)
def f_complete_even(x, k):
    equation = -1
    for i in range(1, k):
        equation += math.comb(2*k, i) * x**(i*(2*k-i))
    equation += math.comb(2*k, k)/2 * x**(k**2)
    return equation

# odd N=2k+1
def f_complete_odd(x, k):
    equation = -1
    for i in range(1, k+1):
        equation += math.comb(2*k+1, i) * x**(i*(2*k+1-i))
    return equation

densities.append(1)
p_set_SSW = []
p_set_fidelity = []
for n in range(n_min, n_max+1):
    if n % 2 == 0:
        gamma_prime = root_scalar(f_complete_even, args=n//2, bracket=[0, 1]).root
    else:
        gamma_prime = root_scalar(f_complete_odd, args=n//2, bracket=[0, 1]).root
    v = d**2/(d-1)/(d+1+(d**2-1)*gamma_prime) - 1/(d**2-1)
    p_set_SSW.append(v)
    p_set_fidelity.append((d**2*np.power(1/d, 2/n)-1)/(d**2-1))

p_sets_SSW.append(p_set_SSW)
p_sets_fidelity.append(p_set_fidelity)

data["densities"] = densities
data["p_sets_SSW"] = p_sets_SSW
data["p_sets_fidelity"] = p_sets_fidelity


# the following three lines are used to save data for density=1
data_density = {"density": 1, "n_set": n_set, "p_set_SSW": p_set_SSW, "p_set_fidelity": p_set_fidelity}
with open(f'densities/density1(n={n_max})({round}).json', 'w') as f:
    json.dump(data_density, f)
