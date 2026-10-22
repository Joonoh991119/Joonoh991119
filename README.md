<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img alt="Joonoh Park — Integrated M.S./Ph.D. Student, Department of Brain and Cognitive Sciences, Seoul National University. Cognitive and Systems Neuroscience Laboratory, advisor Prof. Sang-Hun Lee." src="assets/header-light.svg" width="100%">
</picture>

<sub>&nbsp;✉&nbsp; <a href="mailto:joonop99@snu.ac.kr">joonop99@snu.ac.kr</a> &nbsp;·&nbsp; <a href="https://snu-csnl.com">snu-csnl.com</a></sub>

---

### Repositories

Repositories are labeled by area — click a label to filter.

| | Label | |
|:-:|---|---|
| 🔬 | [`personal-research`](https://github.com/Joonoh991119?tab=repositories&q=topic%3Apersonal-research) | Experimental design, computational modeling, and analysis methods |
| 💼 | [`lab-management`](https://github.com/Joonoh991119?tab=repositories&q=topic%3Alab-management) | AI-powered lab management system for CSNL (private) |
| 🤖 | [`auto-research`](https://github.com/Joonoh991119?tab=repositories&q=topic%3Aauto-research) | AI-powered research automation system, built in collaboration with [@ysys143](https://github.com/ysys143) |
| 🗂️ | [`personal-apps`](https://github.com/Joonoh991119?tab=repositories&q=topic%3Apersonal-apps) | Apps for productivity and an organized work environment |

---

### Education

**Integrated M.S./Ph.D.**, Brain and Cognitive Sciences, Seoul National University &nbsp;<sub>2024.03 – Present</sub><br>
**B.S.**, Convergent Biotechnology and Advanced Materials Science, Kyung Hee University &nbsp;<sub>2020.03 – 2024.02</sub>

---

### Research Interests

> I study how uncertainty in the representation of absolute magnitude (e.g., size, time, numerosity) is carried into its relative representation within a context. So far, I have used computational models to predict human behavior and tested those predictions by collecting and fitting behavioral data; next, I plan to extend this work to fMRI and neural network models.

**Human behavior**
- Magnitude estimation — size, pitch, time, numerosity, value
- Context-dependent normalization<sup>[[1]](#references)</sup><sup>[[2]](#references)</sup>
- History effects<sup>[[2]](#references)</sup><sup>[[3]](#references)</sup><sup>[[4]](#references)</sup>
- Granularity effect<sup>[[2]](#references)</sup>

**Computational models**
- *Cognitive models*
  - **Bayesian observer models** — humans combine noisy measurements with prior knowledge to produce Bayes-optimal behavior.
  - **Information-theoretic models** — humans produce optimal behavior within the limits of their neural resources (efficient coding).
- *Neural models*
  - **Task-optimized RNNs** — to explain temporal dynamics, such as the accumulation and drift of working memory, and how neural representations align across contexts.<sup>[[1]](#references)</sup><sup>[[5]](#references)</sup><sup>[[3]](#references)</sup>
  - **Generative models (e.g., β-VAE)** — to learn compressed representations under a resource limit, giving resource-optimal Bayesian models a neural substrate.<sup>[[6]](#references)</sup><sup>[[7]](#references)</sup><sup>[[8]](#references)</sup>
  - **CNNs** — to gain insight into the computation from the representations that emerge through learning.

<details>
<summary><b>Projects by dimension</b> &nbsp;<sub>🔒 = private, available on request</sub></summary>

<br>

| Dimension | Projects |
|-----------|----------|
| Size · pitch (granularity effect) | 🔒[gran_cann](https://github.com/Joonoh991119/gran_cann) · 🔒[granularity-effect-sim](https://github.com/Joonoh991119/granularity-effect-sim) |
| Size | 🔒[AR_Estimation_n51](https://github.com/Joonoh991119/AR_Estimation_n51) · 🔒[RingRepSca](https://github.com/Joonoh991119/RingRepSca) · 🔒[RingRepSca-Bayesian](https://github.com/Joonoh991119/RingRepSca-Bayesian) · 🔒[RingRepSca_SEM](https://github.com/Joonoh991119/RingRepSca_SEM) |
| Time | 🔒[Time2Dist](https://github.com/Joonoh991119/Time2Dist) · 🔒[Time2Dist_exante](https://github.com/Joonoh991119/Time2Dist_exante) · 🔒[Time2Dist_Exp1](https://github.com/Joonoh991119/Time2Dist_Exp1) · 🔒[Time2Dist_Exp1_N12](https://github.com/Joonoh991119/Time2Dist_Exp1_N12) · 🔒[Time2Dist_Exp2](https://github.com/Joonoh991119/Time2Dist_Exp2) · 🔒[Time2Dist_Exp2_Scaling_Trajectory](https://github.com/Joonoh991119/Time2Dist_Exp2_Scaling_Trajectory) · 🔒[SD_time2dist_exp2](https://github.com/Joonoh991119/SD_time2dist_exp2) · 🔒[boec_hmc](https://github.com/Joonoh991119/boec_hmc) |
| Numerosity | 🔒[Numerosity](https://github.com/Joonoh991119/Numerosity) · 🔒[Uncertainty](https://github.com/Joonoh991119/Uncertainty) |
| Bayesian observer + efficient coding (BOEC) | 🔒[boec_simulator](https://github.com/Joonoh991119/boec_simulator) · [boec_review](https://github.com/Joonoh991119/boec_review) · 🔒[boec_hmc](https://github.com/Joonoh991119/boec_hmc) |

</details>

<a id="references"></a>
<details>
<summary><b>References</b></summary>

<br>

1. Sheahan, H., Luyckx, F., Nelli, S., Teupe, C., & Summerfield, C. (2021). Neural state space alignment for magnitude generalization in humans and recurrent networks. *Neuron, 109*(7), 1214–1226. [doi](https://doi.org/10.1016/j.neuron.2021.02.004)
2. Lee, H., Lim, J., & Lee, S.-H. (2025). Belief updating in decision-variable space: More fine-grained choices attract future ones more strongly. *iScience, 28*(7), 112844. [doi](https://doi.org/10.1016/j.isci.2025.112844)
3. Gu, H., Lee, J., Kim, S., Lim, J., Lee, H.-J., Lee, H., ... Lee, S.-H. (2025). Attractor dynamics of working memory explain a concurrent evolution of stimulus-specific and decision-consistent biases in visual estimation. *Neuron, 113*(20), 3476–3490. [doi](https://doi.org/10.1016/j.neuron.2025.07.003)
4. Lim, J., & Lee, S.-H. (2023). Spatial correspondence in relative space regulates serial dependence. *Scientific Reports, 13*, 18162. [doi](https://doi.org/10.1038/s41598-023-45505-5)
5. Flesch, T., Juechems, K., Dumbalska, T., Saxe, A., & Summerfield, C. (2022). Orthogonal representations for robust context-dependent task performance in brains and neural networks. *Neuron, 110*(7), 1258–1270. [doi](https://doi.org/10.1016/j.neuron.2022.01.005)
6. D'Amato, L., Lancia, G. L., & Pezzulo, G. (2025). The geometry of efficient codes: How rate-distortion trade-offs distort the latent representations of generative models. *PLOS Computational Biology, 21*(5), e1012952. [doi](https://doi.org/10.1371/journal.pcbi.1012952)
7. Fang, Z., & Sims, C. R. (2025). Humans learn generalizable representations through efficient coding. *Nature Communications, 16*, 3989. [doi](https://doi.org/10.1038/s41467-025-58848-6)
8. D'Amato, L., Nuzzi, D., Testolin, A., Stoianov, I. P., Zorzi, M., & Pezzulo, G. (2025). A rate-distortion perspective on the emergence of number sense in unsupervised generative models. *arXiv:2512.19450*. [arXiv](https://arxiv.org/abs/2512.19450)

</details>

---

### Techniques

![Advanced](https://img.shields.io/badge/Advanced-1D4E89?style=flat-square) ![Basic](https://img.shields.io/badge/Basic-D6DEE8?style=flat-square)

| Category | |
|----------|--------|
| **Languages** | ![MATLAB](https://img.shields.io/badge/MATLAB-1D4E89?style=flat-square) ![Python](https://img.shields.io/badge/Python-D6DEE8?style=flat-square&logo=python&logoColor=1A2433) |
| **Modeling** | ![Bayesian Observer](https://img.shields.io/badge/Bayesian%20Observer-1D4E89?style=flat-square) ![Efficient Coding](https://img.shields.io/badge/Efficient%20Coding-1D4E89?style=flat-square) ![CANN](https://img.shields.io/badge/CANN-D6DEE8?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-D6DEE8?style=flat-square&logo=pytorch&logoColor=1A2433) ![CNN](https://img.shields.io/badge/CNN-D6DEE8?style=flat-square) |
| **Analysis** | ![Dimensionality Reduction](https://img.shields.io/badge/Dimensionality%20Reduction-1D4E89?style=flat-square) ![Structural Equation Modeling](https://img.shields.io/badge/Structural%20Equation%20Modeling-1D4E89?style=flat-square) ![Hierarchical Bayesian Model Fitting](https://img.shields.io/badge/Hierarchical%20Bayesian%20Model%20Fitting-1D4E89?style=flat-square) ![fMRI](https://img.shields.io/badge/fMRI-D6DEE8?style=flat-square) |
| **Experiments** | ![Psychtoolbox](https://img.shields.io/badge/Psychtoolbox-1D4E89?style=flat-square) ![jsPsych](https://img.shields.io/badge/jsPsych-D6DEE8?style=flat-square) ![Eye Tracking](https://img.shields.io/badge/Eye%20Tracking-D6DEE8?style=flat-square) ![tES](https://img.shields.io/badge/tES-D6DEE8?style=flat-square) |
| **Automation** | [![Claude Code](https://img.shields.io/badge/Claude%20Code-D6DEE8?style=flat-square&logo=claude&logoColor=1A2433)](https://github.com/Joonoh991119?tab=repositories&q=topic%3Alab-management) |

<sub>And, lately, a fair amount of vibe coding.</sub>

---

### Teaching

<sub>Teaching assistant · Seoul National University</sub>

<table>
<tr><td><code>2026 · 2</code></td><td><b>Probabilistic Brain</b>&nbsp; <sub>M0000.002100</sub></td></tr>
<tr><td><code>2026 · 1</code></td><td><b>Methods in Brain and Cognitive Sciences</b>&nbsp; <sub>339.502</sub></td></tr>
<tr><td><code>2025 · 2</code></td><td><b>Brain and Cognitive Science of Vision</b>&nbsp; <sub>M1426.004000</sub></td></tr>
<tr><td><code>2024 · 2</code></td><td><b>Data Collection and Statistical Analysis for Functional MRI</b>&nbsp; <sub>M2480.000600</sub></td></tr>
<tr><td><code>2024 · 2</code></td><td><b>Brain and Cognitive Science of Consciousness</b>&nbsp; <sub>M1426.004100</sub></td></tr>
</table>

---

### Publications & Presentations

#### Conference Poster

**Park, J.**, & Lee, S.-H. (2026). The fate of uncertainty in the transformation from absolute to relative magnitude. *CBrain 2026*.<br>
<a href="https://joonoh991119.github.io/csnl-posters-2026/"><img src="assets/btn-poster.svg" alt="Poster" height="22"></a>&nbsp;<a href="https://github.com/Joonoh991119/2026CBrain_TheFateUncertainty"><img src="assets/btn-code.svg" alt="Data and code" height="22"></a>
