# Baustein 3 — Der Materie-Operator T_M (Version 4.1)

## 3.1 Zweck des Operators

Der Operator **T_M** beschreibt, wie Materie die Eigenschaften eines
Hexaphotons verändert.  
Er ist **keine neue Physik**, sondern eine **kompakte Notation** für
etablierte klassische Transformationen:

- Brechung  
- Reflexion  
- Streuung  
- Polarisationsänderung  
- Absorption  

T_M fasst Jones-, Mueller-, Fresnel- und Snellius-Formalismen in einer
einheitlichen Schreibweise zusammen.

---

## 3.2 Definition des Operators

Ein Hexaphoton ist definiert als:

\[
H = (f, P, d)
\]

Der Materie-Operator wirkt darauf wie folgt:

\[
T_M(H) = (f', P', d')
\]

mit:

- \( f' = f \) (Frequenz bleibt in linearer Optik erhalten)
- \( P' = M_P \, P \) (Polarisationsmatrix)
- \( d' = M_d \, d \) (Richtungsänderung)

---

## 3.3 Lineare Optik (Standardfall)

### Frequenz (immer erhalten)
\[
f' = f
\]

Dies ist eine zentrale Eigenschaft linearer Optik.  
Jede Frequenzänderung gehört definitionsgemäß **nicht** zu T_M.

### Polarisation
\[
P' = M_P \, P
\]

mit \( M_P \) als Jones- oder Mueller-Matrix des Materials.

### Richtung
\[
d' = M_d \, d
\]

Beispiele:

- Snellius-Brechung  
- Fresnel-Reflexion  
- Mie- oder Rayleigh-Streuung  

### Energie
\[
E' = h f' = h f
\]

---

## 3.4 Absorption

Absorption wird durch einen Dämpfungsfaktor \( \alpha \in [0,1] \) beschrieben:

\[
T_M(H) = \alpha \cdot (f, P', d')
\]

Interpretation:

- \( \alpha = 1 \): keine Absorption  
- \( \alpha = 0 \): vollständige Absorption  
- \( 0 < \alpha < 1 \): partielle Absorption  

Absorption ist eine Abbildung:

\[
H \;\longrightarrow\; \alpha H'
\]

---

## 3.5 Emission (separater Prozess)

Emission ist **nicht** durch T_M beschrieben.  
Sie erzeugt ein neues Hexaphoton:

\[
\emptyset \;\longrightarrow\; H_{\text{emit}}
\]

mit:

\[
H_{\text{emit}} = (f_{\text{emit}}, P_{\text{emit}}, d_{\text{emit}})
\]

Damit sind Absorption und Emission **klar getrennt**:

- Absorption: Transformation eines existierenden Hexaphotons  
- Emission: Erzeugung eines neuen Hexaphotons  

---

## 3.6 Nichtlineare Erweiterungen (optional)

Für spätere Arbeiten kann ein erweiterter Operator **T\*_M** definiert werden:

\[
T^*_M(H) = (f + \Delta f, \; P', \; d')
\]

Er beschreibt Effekte wie:

- Raman- und Brillouin-Streuung  
- Erzeugung neuer Frequenzen (SHG, THG)  
- Kerr-Effekt  
- Intensitätsabhängige Brechung  

**Wichtig:**  
T\*_M ist **nicht Bestandteil** des Kernsystems.

---

## 3.7 Entkopplung von spekulativen Hypothesen

Spekulative Ideen aus der Hypothesen-Sammlung (z. B. Fortbestand absorbierter
Photonen, Identität von Photonen) werden **nicht** durch T_M beschrieben.

Der Operator bildet ausschließlich **klassische, experimentell bestätigte**
Transformationen ab.

---

## 3.8 Zusammenfassung

Der Operator T_M:

- ist eine kompakte Notation klassischer Optik  
- erhält die Frequenz  
- verändert Polarisation und Richtung  
- beschreibt Absorption über einen Dämpfungsfaktor  
- erzeugt **keine** neuen Photonen  
- ist vollständig kompatibel mit Maxwell-Optik  
- bleibt frei von spekulativen Annahmen  

Optionale Erweiterungen (T\*_M) ermöglichen die Beschreibung nichtlinearer
Effekte, ohne den Kern der Theorie zu verändern.
