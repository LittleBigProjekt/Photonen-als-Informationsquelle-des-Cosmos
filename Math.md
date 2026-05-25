Mathematische Grundlagen der Hexaphotonischen Notation (Version 4.1)

Dieses Dokument fasst alle mathematischen Definitionen des Hexaphoton‑Notation‑Systems zusammen.  
Es bildet die formale Grundlage der Bausteine 1–4.

---

1. Das Hexaphoton

1.1 Definition

Ein Hexaphoton ist ein Tripel:

H = (f, P, d)

mit:

- f : Frequenz (positiv)  
- P : Polarisationsvektor (komplex 2D)  
- d : Richtungsvektor (Norm = 1)

---

1.2 Abgeleitete Größen

Energie:  
E = h * f

Impuls:  
p = (h  f / c)  d

Phase:  
Die Phase ist keine Eigenschaft eines einzelnen Hexaphotons.  
Sie entsteht erst im Ensemble:

phiij = phii - phi_j

---

2. Das Hexafeld

Ein Hexafeld ist eine Menge von Hexaphotonen:

H_set = { H1, H2, ..., Hn }

---

3. Das Mapping F

3.1 Definition

F ordnet jedem Hexaphoton einen Wellenbeitrag zu:

F(H) = A  P  exp(i  (kx - omega*t))

mit:

omega = 2pif  
k = (2pif/c) * d  
A = komplexe Amplitude

Linearität:

F(aH1 + bH2) = aF(H1) + bF(H2)

---

3.2 Superposition

Die resultierende Welle eines Hexafeldes:

E(x,t) = Summe ueber i von F(Hi)

---

4. Der Materie-Operator T_M

4.1 Definition

Materie wirkt auf ein Hexaphoton durch:

T_M(H) = (f', P', d')

In linearer Optik:

f' = f  
P' = M_P * P  
d' = M_d * d

M_P = Jones- oder Mueller-Matrix  
M_d = Richtungsoperator (Brechung, Reflexion, Streuung)

---

4.2 Absorption

Absorption wird durch einen Faktor alpha in [0,1] beschrieben:

T_M(H) = alpha * (f, P', d')

---

4.3 Emission

Emission ist ein separater Prozess:

(empty) -> H_emit

---

5. Nichtlineare Erweiterung T_M* (optional)

TM*(H) = (f + Deltaf, P', d')

Beispiele:

- Raman-Streuung  
- SHG / THG  
- Kerr-Effekt  

T_M* ist nicht Teil des Kernsystems.

---

6. Konsistenzbedingungen

Das System ist konsistent, wenn:

1. Frequenz erhalten bleibt: f' = f  
2. Polarisation korrekt transformiert wird: P' = M_P * P  
3. Richtung korrekt transformiert wird: d' = M_d * d  
4. Superposition gilt: E = Summe F(Hi)  
5. Keine neue Physik eingefuehrt wird

---

7. Zusammenfassung

Dieses Dokument definiert:

- das Hexaphoton  
- das Hexafeld  
- das Mapping F  
- den Materie-Operator T_M  
- die optionale Erweiterung T_M*  
- die Konsistenzbedingungen  

Es bildet die mathematische Grundlage der Bausteine 1–4.
