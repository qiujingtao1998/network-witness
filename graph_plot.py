import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple']
round = 10
densities = [0.2, 0.4, 0.6, 0.8, 1]
n = 25


with open(f'densities/density{densities[0]}(n={n})(1).json', 'r') as f:
    n_set = json.load(f)["n_set"]

p_sets_SSW = []
p_sets_fidelity = []

for density in densities[:2]:
    # since density=0.2 and 0.4 has value "None", we handle them separately
    for i in range(1, round+1):
        if i == 1:
            with open(f'densities/density{density}(n={n})({i}).json', 'r') as f:
                data = json.load(f)
                p_set_SSW = np.array(data["p_set_SSW"])
                p_set_fidelity = np.array(data["p_set_fidelity"])
        else:
            with open(f'densities/density{density}(n={n})({i}).json', 'r') as f:
                data = json.load(f)
            p_set_SSW_prime = np.array(data["p_set_SSW"])
            p_set_fidelity_prime = np.array(data["p_set_fidelity"])
            for j in range(len(n_set)):
                if not (p_set_SSW[j] is None):
                    p_set_SSW[j] += p_set_SSW_prime[j]
                    p_set_fidelity[j] += p_set_fidelity_prime[j]

    for j in range(len(n_set)):
        if not (p_set_SSW[j] is None):
            p_set_SSW[j] /= round
            p_set_fidelity[j] /= round

    p_sets_SSW.append(p_set_SSW)
    p_sets_fidelity.append(p_set_fidelity)


for density in densities[2:]:
    p_set_SSW = 0
    p_set_fidelity = 0
    for i in range(1, round+1): # rounds
        with open(f'densities/density{density}(n={n})({i}).json', 'r') as f:
            data = json.load(f)
            p_set_SSW += np.array(data["p_set_SSW"])
            p_set_fidelity += np.array(data["p_set_fidelity"])
    p_set_SSW /= round
    p_set_fidelity /= round
    p_sets_SSW.append(p_set_SSW)
    p_sets_fidelity.append(p_set_fidelity)

fig = plt.figure(figsize = (14/2.54, 8.6/2.54))
ax = plt.subplot(111)



for i in range(len(densities)):
    p_set_SSW = p_sets_SSW[i]
    p_set_fidelity = p_sets_fidelity[i]
    density = densities[i]
    if i == 0:
        ax.plot(n_set, p_set_SSW, marker='o', markersize=4, color=colors[i], label=f'{density:.1f}')  # , label=f'{density:.1f}')
        ax.plot(n_set, p_set_fidelity, marker='^', markersize=4, linestyle='--', color=colors[i]) 
    else:
        ax.plot(n_set, p_set_SSW, marker='o', markersize=4, color=colors[i], label=f'{density:.1f}')
        ax.plot(n_set, p_set_fidelity, marker='^', markersize=4, linestyle='--', color=colors[i]) 

ax.tick_params(axis='both', which='major', direction='in', labelsize=13)
ax.tick_params(axis='both', which='minor', direction='in', labelsize=13)
ax.set_ylim([0.33, 1])
ax.set_xlabel(r"$|V|$", fontsize=13)
ax.set_ylabel(r"$p$", fontsize=13)


handles = [
    mpatches.Patch(color=colors[0], label='0.2'),
    mpatches.Patch(color=colors[1], label='0.4'),
    mpatches.Patch(color=colors[2], label='0.6'),
    mpatches.Patch(color=colors[3], label='0.8'),
    mpatches.Patch(color=colors[4], label='1.0')
]

leg1 = ax.legend(
    title = r'Density $D$',
    handles=handles,
    loc='center left',
    bbox_to_anchor=(1, 0.5),
    fontsize=13,
    title_fontsize=13,
)


fig.savefig('densities_average.pdf', bbox_inches='tight')