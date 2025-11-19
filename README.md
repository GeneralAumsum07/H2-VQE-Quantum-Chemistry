# H2-VQE-Quantum-Chemistry

Quantum chemistry VQE pipeline for **H₂**, developed for the Qubit Advance Level Hackathon themed:

Healthcare & Life Sciences – Small Molecular Drug Discovery using Quantum Computing

This repository contains a complete, reproducible implementation of the Variational Quantum Eigensolver (VQE) applied to the hydrogen molecule (H₂). Although H₂ is simple, the workflow demonstrated here directly scales to small drug-relevant molecules and forms a foundation for quantum-aided drug discovery.

-------------------------------------------------------------------------------

## Project Summary

This project uses Qiskit and Qiskit Nature to:

- Build the molecular Hamiltonian of H₂ (via PySCF)
- Encode the fermionic Hamiltonian onto qubits (Jordan–Wigner)
- Solve the ground state using VQE with multiple optimizers and restarts
- Compare to exact diagonalization
- Generate plots, CSV tables, and markdown summaries of accuracy

The notebook in this repository provides a full demonstration pipeline.

-------------------------------------------------------------------------------

## Repository Structure

```
H2-VQE-Quantum-Chemistry/
├── notebooks/
│   └── H2_VQE_Notebook.ipynb
├── src/
│   └── (optional helper scripts)
├── results/
│   ├── plots/
│   └── tables/
│   └── report/
├── requirements.txt
├── README.md
```

-------------------------------------------------------------------------------

## Quickstart Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd H2-VQE-Quantum-Chemistry
```

### 2. Create and activate a Conda environment (recommended)

```bash
conda create -n ga07-vqe python=3.10 -y
conda activate ga07-vqe
```

### 3. Install dependencies

Option A — install via pip:

```bash
pip install -r requirements.txt
```

Option B — more stable for PySCF (recommended):

```bash
conda install -c conda-forge pyscf
pip install -r requirements.txt
```

### 4. Open the notebook

Launch Jupyter from within the activated environment:

```bash
jupyter lab
```

Then open:
```
notebooks/H2_VQE_Notebook.ipynb
```

Select the kernel:
```
Python 3.10 (ga07-vqe)
```

-------------------------------------------------------------------------------

## Running the Notebook

The notebook is organized into cells:

1. Environment setup and imports  
2. Build Hamiltonian and qubit mapping  
3. Single VQE computation  
4. Exact diagonalization  
5. Robust VQE sweep over H–H distances  
6. Build and save error tables (CSV + Markdown)  
7. Generate final results report section  

### Outputs

- Plot images → `results/plots/`
- Tables (CSV, sorted CSV) → `results/tables/`
- Markdown summaries → `results/tables/`
- Additional reports → `results/report/`

Each file is timestamped for reproducibility.

-------------------------------------------------------------------------------

## Notes and Troubleshooting

- If Qiskit packages are not detected, ensure the correct env is activated in VS Code's Jupyter kernel selector.
- On Windows, always prefer running under **WSL** when using PySCF.
- If VQE raises Estimator or TwoLocal errors, ensure that:
  - qiskit-terra
  - qiskit-aer
  - qiskit-algorithms
  - qiskit-nature  
  are installed and compatible.

-------------------------------------------------------------------------------

## Relevance to Drug Discovery

The pipeline demonstrated here is directly applicable to:

- Binding energy computation  
- Reaction pathway modeling  
- Pharmacophore energy landscape exploration  
- Fragment-based drug design  

Techniques used: (tapering, optimizer fallback, random restarts) scale to larger systems and more expressive ansätze like UCCSD.

-------------------------------------------------------------------------------

## Future Improvements

- Implement UCCSD and ADAPT-VQE
- Test alternative encodings (Parity, Bravyi–Kitaev)
- Apply workflow to molecules beyond H₂ (e.g., LiH, CH₄ fragments)
- Run experiments on real IBM Quantum hardware
- Add parallelized sweeps for multiple molecules

-------------------------------------------------------------------------------

## License

This project is provided for educational and hackathon use.  
Cite Qiskit, PySCF, and related libraries where appropriate.

-------------------------------------------------------------------------------

## Author

Rachit Samal (GeneralAumsum07) 
Hackathon Participant / Developer
