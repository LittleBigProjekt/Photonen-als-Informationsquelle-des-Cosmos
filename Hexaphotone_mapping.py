"""
Hexaphotone Mapping: Canonical Gaussian Modal Amplitudes
========================================================

This script computes the modal amplitudes a(k; H) for a given Hexaphoton vector H
using the canonical Gaussian parameterization defined in Hexaphotone v3.1.

Dependencies:
-------------
- numpy
- scipy
"""

import numpy as np
from scipy.constants import c, pi

def compute_k0(f, d_vec):
    """
    Compute the central wavevector k0 from frequency f and propagation direction d_vec.

    Parameters:
    -----------
    f : float
        Central frequency (Hz).
    d_vec : array-like, shape (3,)
        Unit propagation direction vector.

    Returns:
    --------
    k0 : ndarray, shape (3,)
        Central wavevector.
    """
    k0_magnitude = 2 * pi * f / c
    return k0_magnitude * np.array(d_vec)

def compute_sigma(f, alpha):
    """
    Compute the frequency-dependent spectral spread sigma(f).

    Parameters:
    -----------
    f : float
        Central frequency (Hz).
    alpha : float
        Calibration parameter for spectral spread.

    Returns:
    --------
    sigma : float
        Spectral spread.
    """
    return alpha * f / c

def compute_A(E, C, sigma):
    """
    Compute the normalization amplitude A(E, f) to enforce the energy constraint.

    Parameters:
    -----------
    E : float
        Energy scale (proportional to total modal energy).
    C : float
        Calibration constant for energy normalization.
    sigma : float
        Spectral spread (from compute_sigma).

    Returns:
    --------
    A : float
        Normalization amplitude.
    """
    denominator = pi * sigma**2
    return np.sqrt(C * E / denominator)

def compute_modal_amplitudes(k_grid, H, alpha, C):
    """
    Compute the modal amplitudes a(k; H) for a given Hexaphoton vector H.

    Parameters:
    -----------
    k_grid : ndarray, shape (N, 3)
        Grid of wavevectors k at which to compute the amplitudes.
    H : dict
        Hexaphoton vector with keys:
        - 'E': Energy scale (float)
        - 'f': Central frequency (float)
        - 'P_i': Polarization (array-like, shape (3,) for Jones vector)
        - 'phi': Global phase (float, radians)
        - 'p_vec': Modal momentum vector (array-like, shape (3,))
        - 'd_vec': Unit propagation direction (array-like, shape (3,))
    alpha : float
        Calibration parameter for spectral spread.
    C : float
        Calibration constant for energy normalization.

    Returns:
    --------
    a_k : ndarray, shape (N,)
        Modal amplitudes at each point in k_grid.
    """
    E, f, P_i, phi, p_vec, d_vec = H['E'], H['f'], H['P_i'], H['phi'], H['p_vec'], H['d_vec']

    # Compute k0 and sigma
    k0 = compute_k0(f, d_vec)
    sigma = compute_sigma(f, alpha)

    # Compute normalization amplitude A
    A = compute_A(E, C, sigma)

    # Compute the Gaussian envelope
    k_diff = k_grid - k0
    k_diff_magnitude_sq = np.sum(k_diff**2, axis=1)
    gaussian_envelope = np.exp(-k_diff_magnitude_sq / (2 * sigma**2))

    # Compute polarization weight (simplified for scalar polarization)
    # For full Jones vector treatment, this would need to be extended
    P_weight = np.ones_like(gaussian_envelope)  # Placeholder for P(P_i)

    # Combine all terms
    a_k = A * P_weight * gaussian_envelope * np.exp(1j * phi)

    return a_k

# Example usage
if __name__ == "__main__":
    # Define a Hexaphoton vector
    H_example = {
        'E': 1.0,               # Energy scale
        'f': 5e14,             # Frequency (500 THz, ~green light)
        'P_i': [1, 0, 0],      # Polarization (x-direction)
        'phi': pi / 4,         # Global phase (45 degrees)
        'p_vec': [0, 0, 1e7],  # Momentum vector (z-direction, magnitude ~2pi f / c)
        'd_vec': [0, 0, 1]     # Propagation direction (z-axis)
    }

    # Define k-grid (example: 10x10x10 grid around k0)
    kx = np.linspace(-1e7, 1e7, 10)
    ky = np.linspace(-1e7, 1e7, 10)
    kz = np.linspace(0, 2e7, 10)
    kx_grid, ky_grid, kz_grid = np.meshgrid(kx, ky, kz)
    k_grid = np.column_stack((kx_grid.ravel(), ky_grid.ravel(), kz_grid.ravel()))

    # Calibration parameters
    alpha = 0.1  # Example value
    C = 1.0      # Example value

    # Compute modal amplitudes
    a_k = compute_modal_amplitudes(k_grid, H_example, alpha, C)

    print("Modal amplitudes computed for example Hexaphoton vector.")
