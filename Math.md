# Mathematische Grundlagen der Hexaphotonischen Notation (Version 4.1)

Dieses Dokument fasst alle mathematischen Definitionen des
Hexaphoton‑Notation‑Systems zusammen.  
Es bildet die formale Grundlage der Bausteine 1–4.

---

# 1. Das Hexaphoton

## 1.1 Definition

Ein Hexaphoton ist ein Tripel aus drei unabhängigen Freiheitsgraden:

\[
H = (f, P, d)
\]

mit:

- \( f \in \mathbb{R}^+ \): Frequenz  
- \( P \in \mathbb{C}^2 \): Polarisationsvektor (Jones‑Formalismus)  
- \( d \in S^2 \): Richtungsvektor auf der Einheitssphäre  

Alle weiteren Größen sind abgeleitet.

---

## 1.2 Abgeleitete Größen

### Energie
\[
E(H) = h f
\]

### Impuls
\[
p(H) = \frac{h f}{c} \, d
\]

### Phase  
Die Phase ist **keine Eigenschaft eines einzelnen Hexaphotons**.  
Sie entsteht erst im Ensemble:

\[
\phi_{ij} = \phi_i - \phi_j
\]

---

# 2. Das Hexafeld

Ein Hexafeld ist eine endliche oder abzählbare Menge von Hexaphotonen:

\[
\mathcal{H} = \{ H_1, H_2, \dots, H_n \}
\]

---

# 3. Das Mapping F

## 3.1 Definition

Das Mapping F ordnet jedem Hexaphoton einen Beitrag zur klassischen
elektromagnetischen Welle zu:

\[
F(H) = A \, P \, e^{i(k \cdot x - \omega t)}
\]

mit:

- \( \omega = 2\pi f \)  
- \( k = \frac{2\pi f}{c} d \)  
- \( A \in \mathbb{C} \): skalierbare Amplitude  

F ist **linear**:

\[
F(aH_1 + bH_2) = aF(H_1) + bF(H_2)
\]

---

## 3.2 Superposition

Die resultierende Welle eines Hexafeldes ist:

\[
E(x,t) = \sum_{i=1}^{n} F(H_i)
\]

Dies entspricht exakt der klassischen Wellenoptik.

---

# 4. Der Materie‑Operator T_M

## 4.1 Definition

Materie wirkt auf ein Hexaphoton durch:

\[
T_M(H) = (f', P', d')
\]

In linearer Optik gilt:

\[
f' = f
\]
\[
P' = M_P \, P
\]
\[
d' = M_d \, d
\]

mit:

- \( M_P \): Jones‑ oder Mueller‑Matrix  
- \( M_d \): Richtungsoperator (Brechung, Reflexion, Streuung)  

---

## 4.2 Absorption

Absorption wird durch einen Faktor \( \alpha \in [0,1] \) beschrieben:

\[
T_M(H) = \alpha \cdot (f, P', d')
\]

---

## 4.3 Emission

Emission ist ein separater Prozess:

\[
\emptyset \longrightarrow H_{\text{emit}}
\]

---

# 5. Nichtlineare Erweiterung T\*_M (optional)

Für nichtlineare Effekte:

\[
T^*_M(H) = (f + \Delta f, \; P', \; d')
\]

Beispiele:

- Raman‑Streuung  
- SHG / THG  
- Kerr‑Effekt  

T\*_M ist **nicht Teil des Kernsystems**.

---

# 6. Konsistenzbedingungen

Das System ist konsistent, wenn:

1. Frequenz in linearer Optik erhalten bleibt  
   \[
   f' = f
   \]

2. Polarisation korrekt transformiert wird  
   \[
   P' = M_P P
   \]

3. Richtung korrekt transformiert wird  
   \[
   d' = M_d d
   \]

4. Superposition identisch zur klassischen Optik ist  
   \[
   E = \sum_i F(H_i)
   \]

5. Keine neue Physik eingeführt wird  
   (Notation ≠ Theorie)

---

# 7. Zusammenfassung

Dieses Dokument definiert:

- das Hexaphoton  
- das Hexafeld  
- das Mapping F  
- den Materie‑Operator T_M  
- die optionale Erweiterung T\*_M  
- die Konsistenzbedingungen  

Es bildet die mathematische Grundlage der Bausteine 1–4.
