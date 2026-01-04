# The code about the paper "Scalable Certification of Entanglement in Quantum Networks"
+ `graph.py` is used to generate date.
+ `graph_plot.py` is used to plot the figure.
+ The bounds for fidelity-based witnesses are determined by the minimum cut. More specifically, the maximum fidelity of biseparable states and the perfect state $\bigotimes_{e\in E}\Phi_e$ is $\alpha=\min_{K\in\mathcal{B}(G)}\frac{1}{d^{|K|}}$. To see this, note that for any partition $S|S^c$ with cut $K$, the Schmidt coefficients of $\bigotimes_{e\in E}\Phi_e$ with respect to $S|S^c$ are all $\frac{1}{\sqrt{d}^{|K|}}.$