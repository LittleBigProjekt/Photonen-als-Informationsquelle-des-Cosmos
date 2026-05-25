# Baustein 3 — Der Materie-Operator T_M (Version 4.0)

## 3.1 Zweck des Operators

Der Operator **T_M** beschreibt, wie Materie die Eigenschaften eines
Hexaphotons verändert.  
Er ist die kompakte Darstellung der klassischen Wechselwirkungen:

- Absorption  
- Reflexion  
- Brechung  
- Streuung  
- Polarisationsänderung  

T_M ist **kein neuer physikalischer Mechanismus**, sondern eine
Notation der etablierten linearen Optik.

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

Dabei gilt:

- \( f' = f \) in linearer Optik  
- \( P' = M_P \, P \) (Jones- oder Mueller-Matrix)  
- \( d' = M_d \, d \) (Richtungsänderung durch Brechung/Streuung)

---

## 3.3 Lineare Optik (Standardfall)

### Frequenz
\[
f' = f
\]
Die Frequenz bleibt bei allen linearen optischen Prozessen erhalten.

### Polarisation
\[
P' = M_P \, P
\]
mit \( M_P \) als Jones- oder Mueller-Matrix des Materials.

### Richtung
\[
d' = M_d \, d
\]
z. B. durch:

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
T_M(H) = \alpha \cdot H'
\]

mit \( H' = (f, P', d') \).

- \( \alpha = 1 \): keine Absorption  
- \( \alpha = 0 \): vollständige Absorption  

---

## 3.5 Emission

Emission wird **nicht** durch T_M beschrieben, da sie ein separater Prozess ist
(Spontan- oder stimulierte Emission).  
Ein emittiertes Hexaphoton wird als neues Objekt erzeugt:

\[
H_{\text{emit}} = (f_{\text{emit}}, P_{\text{emit}}, d_{\text{emit}})
\]

---

## 3.6 Nichtlineare Erweiterungen (optional)

Für spätere Arbeiten kann ein erweiterter Operator **T\*_M** definiert werden,
der nichtlineare Effekte beschreibt:

- Frequenzverschiebung (Raman, Brillouin)
- Erzeugung neuer Frequenzen (SHG, THG)
- Intensitätsabhängige Brechung (Kerr-Effekt)
- Polarisationseffekte jenseits linearer Optik

Beispiel:

\[
T^*_M(H) = (f + \Delta f, \; P', \; d')
\]

Diese Erweiterung ist **nicht Bestandteil** des Kernsystems.

---

## 3.7 Beziehung zu den Hypothesen (Interpretation)

Die Hypothesen H1 und H2 aus der separaten Sammlung können als
**Interpretationsrahmen** dienen, sind aber **nicht Teil des Operators**:

- **H1** (Fortbestand absorbierter Photonen):  
  → keine Integration in T_M, da Absorption vollständig durch \( \alpha \) beschrieben wird.

- **H2** (Identität absorbierter/emittierter Photonen):  
  → Emission erzeugt neue Hexaphotonen; Identität ist nicht definiert.

Diese Hypothesen bleiben bewusst **außerhalb** des Notationssystems.

---

## 3.8 Zusammenfassung

Der Operator T_M:

- beschreibt alle klassischen linearen Wechselwirkungen  
- ist vollständig kompatibel mit Maxwell-Optik  
- verändert Polarisation und Richtung  
- erhält die Frequenz  
- beschreibt Absorption über einen Dämpfungsfaktor  
- erzeugt **keine** neuen Photonen  
- bleibt frei von spekulativen Annahmen  

Optionale Erweiterungen (T\*_M) ermöglichen später die Beschreibung
nichtlinearer Effekte, ohne den Kern der Theorie zu verändern.
