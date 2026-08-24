import matplotlib.pyplot as plt

fig = plt.figure(figsize = (14/2.54, 2*8.6/2.54))
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
fig.subplots_adjust(hspace=0.4)
V_set = [i for i in range(3, 11)]  # number of parties


SSW_bound_white = []
# \mathrm{Tr}(W_E\rho) = -\frac{1}{2} + \left[\frac{1}{2} - \frac{2}{4^{|E|}} + \frac{3}{2^{|E|+1}}\right]\lambda.
for V in range(3, 11):
    n = V - 1  # number of edges
    SSW_bound_white.append(1/(1-1/4**(n-1)+3/2**n))

SSW_bound_dephasing = []
# \mathrm{Tr}(W_E\rho) = -\frac{1}{2} + \left[\frac{1}{2}-\frac{1}{2^{|E|-1}}+\left(\frac{2}{3}\right)^{|E|-1}\right] \lambda.
for V in range(3, 11):
    n = V - 1
    SSW_bound_dephasing.append(1/(1-1/2**(n-2)+2**n/3**(n-1)))

GEN_bound_white = []
# \mathrm{Tr}(W_1\rho) = -1 + \left[1+\left(\frac{3}{4}\right)^{|E|}+\frac{2^{|E|}-3}{4^{|E|}}\right]\lambda.
for V in range(3, 11):
    n = V - 1
    GEN_bound_white.append(1/(1+3**n/4**n+(2**n-3)/4**n))

GEN_bound_dephasing = []
# \mathrm{Tr}(W_1\rho) = -1 + \left[2-\frac{1}{2^{|E|-1}}\right]\lambda.
for V in range(3, 11):
    n = V - 1
    GEN_bound_dephasing.append(1/(2-1/2**(n-1)))


ax1.plot(V_set, SSW_bound_white, label='SSWs', marker='o')
ax1.plot(V_set, GEN_bound_white, label='Ref. [9]', marker='^')

ax1.legend()
ax1.tick_params(axis='both', which='major', direction='in', labelsize=10)
ax1.tick_params(axis='both', which='minor', direction='in', labelsize=10)
ax1.set_title("White noise")
ax1.set_xlabel(r"$|V|$", fontsize=10)
ax1.set_ylabel(r"$\lambda$", fontsize=10)

ax2.plot(V_set, SSW_bound_dephasing, label='SSWs', marker='o')
ax2.plot(V_set, GEN_bound_dephasing, label='Ref. [9]', marker='^')

ax2.legend()
ax2.tick_params(axis='both', which='major', direction='in', labelsize=10)
ax2.tick_params(axis='both', which='minor', direction='in', labelsize=10)
ax2.set_title("Dephasing noise")
ax2.set_xlabel(r"$|V|$", fontsize=10)
ax2.set_ylabel(r"$\lambda$", fontsize=10)

fig.savefig('comparison.pdf', bbox_inches='tight')