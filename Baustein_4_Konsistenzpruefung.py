#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hexaphotone - Baustein 4: Konsistenz-Pruefung
==============================================

Zweck
-----
Dieses Skript prueft, ob die Hexaphotone-Notation (Bausteine 1-3)
widerspruchsfrei an die etablierte Mie-Streutheorie ANDOCKT.

Dafuer wird EIN konkretes Streuproblem - Streuung einer Lichtwelle an
einer homogenen Kugel - auf zwei Weisen beschrieben:

  Weg A  -  klassische Mie-Theorie (etablierte Referenz)
  Weg B  -  Hexaphotone-Notation (Bausteine 1-3)

============================================================
WICHTIG - WAS DIESES SKRIPT IST, UND WAS NICHT
============================================================
Dies ist eine KONSISTENZ-PRUEFUNG, KEINE unabhaengige Validierung.

Gemaess Baustein 3, Abschnitt 6 ist der Operator T_Kugel DEFINIERT
als die Mie-Loesung, nur in Hexaphotone-Schreibweise gelesen. Weg B
ruft daher denselben Mie-Kern auf wie Weg A. Dass beide Wege exakt
uebereinstimmen, ist deshalb ERWARTET - es bestaetigt, dass die
Hexaphotone-Groessen (Frequenz -> Wellenlaenge -> Groessenparameter x)
korrekt und widerspruchsfrei mit der Mie-Theorie verknuepft sind.

Was dieses Skript NICHT leistet:
  - Es ist KEIN unabhaengiger Rechenweg. Weg B leitet die Streuung
    nicht aus F_einzeln + Superposition selbst her, sondern nutzt
    den Mie-Kern.
  - Es ist daher KEIN Beweis, dass Hexaphotone "richtig rechnet" -
    es zeigt nur, dass die Notation sauber an bekannte Physik anschliesst.

Eine echte, unabhaengige Validierung muss Weg B vollstaendig aus den
Bausteinen aufbauen. Das verlangt, zuvor die offenen Punkte K5, K6, K7
(Polarisationsvektor, Einheiten, Modalbasis) zu schliessen. Sie ist
Gegenstand eines spaeteren Bausteins 5.
============================================================

Abhaengigkeiten:  numpy, scipy, matplotlib  (keine externe Mie-Bibliothek)
Lizenz:           CC-BY-SA 4.0
"""

import numpy as np
from scipy.special import spherical_jn, spherical_yn
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ===================================================================
# TEIL 1  -  WEG A:  klassische Mie-Theorie (Referenz)
# ===================================================================
#
# Die Mie-Theorie (Gustav Mie, 1908) loest exakt, wie eine homogene
# Kugel eine ebene Lichtwelle streut. Sie ist hier die "Wahrheit",
# gegen die der Hexaphotone-Weg geprueft wird.
#
# Die Streuung wird durch die Mie-Koeffizienten a_n und b_n beschrieben.
# Aus ihnen folgt die Winkelverteilung des gestreuten Lichts.
# ===================================================================

def mie_koeffizienten(m, x, n_max):
    """
    Berechnet die Mie-Koeffizienten a_n und b_n.

    Parameter
    ---------
    m     : relativer Brechungsindex der Kugel (Kugel / Umgebung)
    x     : Groessenparameter  x = 2*pi*R / lambda
            (R = Kugelradius, lambda = Wellenlaenge)
    n_max : hoechste beruecksichtigte Multipol-Ordnung

    Rueckgabe
    ---------
    a, b  : Arrays der Mie-Koeffizienten, Index 1..n_max
    """
    n = np.arange(1, n_max + 1)

    # Riccati-Bessel-Funktionen psi und xi am Argument x bzw. m*x.
    # psi_n(z)  = z * j_n(z)        (j_n = sphaerische Besselfunktion)
    # chi_n(z)  = -z * y_n(z)       (y_n = sphaerische Neumannfunktion)
    # xi_n(z)   = psi_n(z) - i*chi_n(z)
    def psi(nn, z):
        return z * spherical_jn(nn, z)

    def dpsi(nn, z):
        # Ableitung von psi nach z
        return spherical_jn(nn, z) + z * spherical_jn(nn, z, derivative=True)

    def chi(nn, z):
        return -z * spherical_yn(nn, z)

    def dchi(nn, z):
        return -(spherical_yn(nn, z) + z * spherical_yn(nn, z, derivative=True))

    psi_x   = psi(n, x)
    dpsi_x  = dpsi(n, x)
    psi_mx  = psi(n, m * x)
    dpsi_mx = dpsi(n, m * x)
    chi_x   = chi(n, x)
    dchi_x  = dchi(n, x)

    xi_x  = psi_x  - 1j * chi_x
    dxi_x = dpsi_x - 1j * dchi_x

    # Standard-Mie-Formeln fuer a_n und b_n
    a = (m * psi_mx * dpsi_x - psi_x * dpsi_mx) / \
        (m * psi_mx * dxi_x  - xi_x  * dpsi_mx)
    b = (psi_mx * dpsi_x - m * psi_x * dpsi_mx) / \
        (psi_mx * dxi_x  - m * xi_x  * dpsi_mx)

    return a, b


def mie_streufunktion(m, x, theta_grad, n_max=None):
    """
    Berechnet die Streu-Intensitaet als Funktion des Streuwinkels.

    Gibt die (unpolarisiert gemittelte) Streufunktion S(theta) zurueck,
    normiert auf ihren Maximalwert (damit nur die *Form* der Winkel-
    verteilung verglichen wird, unabhaengig von Einheiten).
    """
    if n_max is None:
        # Faustregel nach Wiscombe fuer die noetige Multipol-Anzahl
        n_max = int(x + 4.05 * x ** (1.0 / 3.0) + 2)

    a, b = mie_koeffizienten(m, x, n_max)
    n = np.arange(1, n_max + 1)
    faktor = (2 * n + 1) / (n * (n + 1))

    theta = np.deg2rad(theta_grad)
    cos_t = np.cos(theta)

    S1 = np.zeros(len(theta), dtype=complex)
    S2 = np.zeros(len(theta), dtype=complex)

    # Winkelfunktionen pi_n und tau_n ueber Rekursion aufbauen
    for i, ct in enumerate(cos_t):
        pi_nm1 = 0.0
        pi_n   = 1.0
        for k in range(1, n_max + 1):
            if k == 1:
                pi_curr = 1.0
            else:
                pi_curr = ((2 * k - 1) / (k - 1) * ct * pi_n
                           - k / (k - 1) * pi_nm1)
            tau_curr = k * ct * pi_curr - (k + 1) * pi_nm1

            f = faktor[k - 1]
            S1[i] += f * (a[k - 1] * pi_curr + b[k - 1] * tau_curr)
            S2[i] += f * (a[k - 1] * tau_curr + b[k - 1] * pi_curr)

            pi_nm1 = pi_n if k > 1 else 1.0
            # pi-Werte fuer naechsten Schritt verschieben
            if k == 1:
                pi_nm1 = 1.0
                pi_n = pi_curr
            else:
                pi_nm1 = pi_n
                pi_n = pi_curr

    # unpolarisierte Streuintensitaet
    S = (np.abs(S1) ** 2 + np.abs(S2) ** 2) / 2.0
    return S / np.max(S)


# ===================================================================
# TEIL 2  -  WEG B:  Hexaphotone-Notation
# ===================================================================
#
# Hier wird dasselbe Problem in der Sprache der Bausteine 1-3 gerechnet.
#
#   Baustein 1:  ein Hexaphoton H = (f, Pi, d) + abgeleitet (E, p)
#   Baustein 2:  F_einzeln bildet H auf eine ebene Welle ab
#   Baustein 3:  der Operator T_M (hier: T_Kugel) veraendert die Welle
#
# Kernpunkt von Baustein 3, Abschnitt 6:
#   T_Kugel ist KEIN neuer, geratener Operator. Es IST die Mie-Loesung,
#   nur in Hexaphotone-Schreibweise gelesen. Das einfallende Hexafeld
#   (eine ebene Welle = viele gleichgerichtete Hexaphotonen) wird durch
#   T_Kugel in ein ausgehendes Hexafeld ueberfuehrt, dessen Hexaphotonen
#   in viele Richtungen d' zeigen - die Streurichtungen.
#
# Wenn die Bausteine konsistent sind, muss dieser Weg dieselbe
# Winkelverteilung liefern wie Weg A.
# ===================================================================

class Hexaphoton:
    """Ein einzelnes Hexaphoton gemaess Baustein 1.

    Eigenschaften (Klasse A):  f, Pi, d
    Abgeleitet   (Klasse B):  E, p   - ueber die Constraints C1, C2
    """
    h = 6.62607015e-34          # Plancksches Wirkungsquantum [J*s]
    c = 2.99792458e8            # Lichtgeschwindigkeit [m/s]

    def __init__(self, f, Pi, d):
        self.f  = f                       # Frequenz (Klasse A)
        self.Pi = Pi                      # Polarisation (Klasse A)
        d = np.asarray(d, dtype=float)
        self.d  = d / np.linalg.norm(d)   # Richtung (Klasse A), normiert

    @property
    def E(self):
        # Constraint C1 aus Baustein 1:  E = h * f
        return self.h * self.f

    @property
    def p(self):
        # Constraint C2 aus Baustein 1:  p = (h*f/c) * d
        return (self.h * self.f / self.c) * self.d

    @property
    def wellenlaenge(self):
        return self.c / self.f


def F_einzeln_wellenvektor(H):
    """Baustein 2, F_einzeln (Schritt 2): Wellenvektor aus f und d.

        k = (2*pi*f / c) * d = (2*pi/lambda) * d
    """
    return (2 * np.pi * H.f / Hexaphoton.c) * H.d


def T_kugel_hexaphotone(H_ein, m, R, theta_grad):
    """Der Operator T_Kugel in Hexaphotone-Notation (Baustein 3).

    Eingabe
    -------
    H_ein      : einfallendes Hexaphoton (definiert f, d, Pi)
    m          : relativer Brechungsindex der Kugel
    R          : Kugelradius [m]
    theta_grad : Streuwinkel, fuer die das ausgehende Hexafeld
                 ausgewertet wird

    Vorgehen
    --------
    1. Aus dem einfallenden Hexaphoton den Groessenparameter x bilden.
       x verknuepft die Hexaphoton-Groesse (Frequenz -> Wellenlaenge)
       mit der Objektgroesse (Kugelradius). Das ist die Bruecke
       zwischen Baustein 2 (Welle) und Baustein 3 (Objekt).
    2. T_Kugel anwenden. Gemaess Baustein 3, Abschnitt 6 IST T_Kugel
       die Mie-Loesung - hier also derselbe Kern wie in Weg A, aber
       angesprochen ueber die Hexaphoton-Groessen.
    3. Ergebnis: das ausgehende Hexafeld, beschrieben durch die
       Intensitaet seiner Hexaphotonen je Streurichtung d'(theta).

    Rueckgabe
    ---------
    Winkelverteilung der Intensitaet des ausgehenden Hexafelds,
    normiert auf den Maximalwert.
    """
    # Schritt 1: Hexaphoton-Groessen -> Groessenparameter x
    lam = H_ein.wellenlaenge                 # aus Baustein 1/2
    x   = 2 * np.pi * R / lam                # Bruecke zur Objektgroesse

    # Schritt 2+3: T_Kugel anwenden = Mie-Kern, ueber x angesprochen.
    # Die Streurichtungen d'(theta) des ausgehenden Hexafelds sind
    # genau die Winkel theta. Die Intensitaet je Richtung ist die
    # Streufunktion.
    I_aus = mie_streufunktion(m, x, theta_grad)

    return I_aus


# ===================================================================
# TEIL 3  -  VERGLEICH BEIDER WEGE
# ===================================================================

def vergleich(beschreibung, f, Pi, d, m, R):
    """Rechnet ein Testproblem auf beiden Wegen und vergleicht."""
    theta = np.linspace(0, 180, 361)        # Streuwinkel 0..180 Grad

    # --- Weg B: Hexaphotone ---
    H = Hexaphoton(f=f, Pi=Pi, d=d)
    lam = H.wellenlaenge
    x   = 2 * np.pi * R / lam
    I_hexa = T_kugel_hexaphotone(H, m, R, theta)

    # --- Weg A: direkte Mie-Referenz ---
    I_mie = mie_streufunktion(m, x, theta)

    # --- Abweichung ---
    diff = np.abs(I_hexa - I_mie)
    max_diff = np.max(diff)
    mittel_diff = np.mean(diff)

    print("=" * 64)
    print(f"Testfall: {beschreibung}")
    print("-" * 64)
    print(f"  Frequenz f              : {f:.3e} Hz")
    print(f"  Wellenlaenge lambda     : {lam*1e9:.1f} nm")
    print(f"  Kugelradius R           : {R*1e9:.1f} nm")
    print(f"  Brechungsindex m        : {m}")
    print(f"  Groessenparameter x     : {x:.4f}")
    print("-" * 64)
    print(f"  Groesste Abweichung     : {max_diff:.2e}")
    print(f"  Mittlere Abweichung     : {mittel_diff:.2e}")
    if max_diff < 1e-9:
        print("  ERGEBNIS: Beide Wege identisch (bis Rechengenauigkeit).")
        print("            Konsistenz bestaetigt: die Hexaphotone-Notation")
        print("            dockt fuer diesen Fall widerspruchsfrei an Mie an.")
    else:
        print("  ERGEBNIS: Abweichung gefunden - bitte pruefen.")
    print("=" * 64)
    print()

    return theta, I_mie, I_hexa, x


def main():
    # Drei Testfaelle mit verschiedenen Groessenparametern.
    # Brechungsindex m = 1.33 (Wasser-Troepfchen in Luft) als Beispiel.
    faelle = [
        ("Kleine Kugel  (x klein, Rayleigh-nah)",
         6.0e14, "linear-x", [0, 0, 1], 1.33, 60e-9),
        ("Mittlere Kugel (x ~ 3)",
         6.0e14, "linear-x", [0, 0, 1], 1.33, 240e-9),
        ("Groessere Kugel (x ~ 8, viele Keulen)",
         6.0e14, "linear-x", [0, 0, 1], 1.33, 640e-9),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6),
                             subplot_kw={"projection": "polar"})

    alle_ok = True
    for ax, (beschr, f, Pi, d, m, R) in zip(axes, faelle):
        theta, I_mie, I_hexa, x = vergleich(beschr, f, Pi, d, m, R)
        if np.max(np.abs(I_mie - I_hexa)) >= 1e-9:
            alle_ok = False

        th = np.deg2rad(theta)
        # Mie-Referenz: dicke helle Linie
        ax.plot(th, I_mie, color="#1f77b4", linewidth=5,
                alpha=0.35, label="Weg A: Mie (Referenz)")
        # Hexaphotone: duenne dunkle Linie darueber
        ax.plot(th, I_hexa, color="#d62728", linewidth=1.4,
                label="Weg B: Hexaphotone")
        ax.set_title(f"x = {x:.2f}", fontsize=11, pad=18)
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.set_rlabel_position(135)
        ax.tick_params(labelsize=7)

    axes[1].legend(loc="upper center", bbox_to_anchor=(0.5, -0.12),
                   ncol=2, fontsize=9, frameon=False)
    fig.suptitle("Hexaphotone Baustein 4 - Konsistenz-Pruefung: "
                 "Streuung an einer Kugel\n"
                 "Weg A (Mie) und Weg B (Hexaphotone) - die Notation "
                 "dockt widerspruchsfrei an Mie an (Kurven deckungsgleich)",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0.02, 1, 0.93])
    fig.savefig("/mnt/user-data/outputs/Baustein_4_Konsistenzpruefung.png",
                dpi=150, bbox_inches="tight")
    print("Grafik gespeichert: Baustein_4_Konsistenzpruefung.png")

    print()
    if alle_ok:
        print(">>> GESAMTERGEBNIS: Alle Testfaelle konsistent.")
        print(">>> Die Hexaphotone-Notation dockt widerspruchsfrei an die")
        print(">>> Mie-Theorie an. Dies ist eine Konsistenz-Pruefung,")
        print(">>> KEINE unabhaengige Validierung (siehe Kopf des Skripts).")
        print(">>> Echte Validierung: spaeterer Baustein 5.")
    else:
        print(">>> GESAMTERGEBNIS: Mindestens ein Testfall zeigt")
        print(">>> eine Abweichung. Bitte Bausteine pruefen.")


if __name__ == "__main__":
    main()
