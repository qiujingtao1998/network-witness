# The codes about the paper "Scalable Certification of Entanglement in Quantum Networks"
+ `graph.py` is used to generate data for Fig. 3.
  - It computes the lower bound of the visibility $p$ above which GME can be certified for the IPEN state $\rho=\bigotimes_{e\in T}(p\Phi_e+(1-p)\mathbb{I}_e/d^2)$ using the corresponding witnesses.
  - The bounds for fidelity-based witnesses are determined by the minimum cut. More specifically, the maximum fidelity of biseparable states and the perfect state $\bigotimes_{e\in E}\Phi_e$ is $\alpha=\min_{K\in\mathcal{B}(G)}\frac{1}{d^{|K|}}$. To see this, note that for any partition $S|S^c$ with cut $K$, the Schmidt coefficients of $\bigotimes_{e\in E}\Phi_e$ with respect to $S|S^c$ are all $\frac{1}{\sqrt{d}^{|K|}}.$
+ `graph_plot.py` is used to plot the figure.
+ `comparison.py` is used to generate Fig. S3 in the Supplementary Information.
  Here, we consider the qubit case, and two different global noises are considered.
  - The white noise $\rho = (1-\lambda)\bigotimes_{e\in E} \Phi_e + \lambda \bigotimes_{e\in E} \frac{\mathbb{I}_e}{4}$.
  - The dephasing noise $\rho = (1-\lambda)\bigotimes_{e\in E} \Phi_e + \lambda \Delta(\bigotimes_{e\in E} \Phi_e)$, where $\Delta$ denotes the operation that retains only the diagonal elements.