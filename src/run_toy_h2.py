import numpy as np
import matplotlib.pyplot as plt

def morse_energy(r, De=0.1745, re=0.741, a=1.02):
    return De * (1 - np.exp(-a * (r - re)))**2 - De

def main():
    r = np.linspace(0.4, 2.0, 25)
    E = [morse_energy(x) for x in r]
    plt.plot(r, E, marker='o')
    plt.xlabel('H-H distance (Å)')
    plt.ylabel('Energy (arb. units)')
    plt.title('Toy H2 Potential Energy Curve')
    plt.grid(True)
    plt.savefig("notebooks/h2_toy_curve.png")
    print("Saved plot to notebooks/h2_toy_curve.png")

if __name__ == "__main__":
    main()
