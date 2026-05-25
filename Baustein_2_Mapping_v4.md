# Baustein 2 — Das Mapping F (Version 4.1)

## 2.1 Zweck des Mappings

Das Mapping **F** beschreibt, wie aus einem einzelnen Hexaphoton
\[
H = (f, P, d)
\]
ein Beitrag zur klassischen elektromagnetischen Welle entsteht.

F ist **kein physikalischer Prozess**, sondern eine **Notation**, die die
klassische Wellenoptik kompakt beschreibt.

---

## 2.2 Das Mapping F für ein einzelnes Hexaphoton

F bildet ein Hexaphoton auf einen komplexen Wellenbeitrag — eine ebene
Welle — ab:

\[
F(H) = A \; \vec{\varepsilon}\; e^{\,i(\vec{k}\cdot\vec{x} - \omega t)}
\]

mit:

- \( \omega = 2\pi f \) — Kreisfrequenz, aus der Frequenz
- \( \vec{k} = \dfrac{2\pi f}{c}\,\vec{d} \) — Wellenvektor, aus Frequenz und Richtung
- \( \vec{\varepsilon} \) — Polarisationsvektor, aus \( P \) (siehe 2.3)
- \( A \) — Amplitude (Skalierungsfaktor, nicht Teil des Hexaphotons; siehe K6)

> **Konsistenz mit Baustein 1.** Der Wellenvektor \( \vec{k} \) ist der
> Impuls \( \vec{p} \) in Wellen-Schreibweise (\( \vec{p} = \hbar\vec{k} \));
> Constraint C2 ist damit automatisch erfüllt.

**Wichtig:** Die Phase entsteht **erst im Hexafeld**, nicht im einzelnen
Hexaphoton. Für ein isoliertes \( H \) wird sie per Konvention auf null
gesetzt. Damit ist F vollständig kompatibel mit Baustein 1.

---

## 2.3 Der Polarisationsvektor (Lösung von K5)

Die Polarisation \( P \) ist ein **Jones-Vektor** — zwei komplexe Zahlen
\( (J_1, J_2) \). Damit daraus ein **realer** Schwingungsvektor
\( \vec{\varepsilon} \) im 3D-Raum wird, braucht es zwei Bezugsrichtungen
in der Ebene senkrecht zu \( \vec{d} \).

**Konvention B — mitgeführtes Bezugspaar.** Das Paar \( \hat{e}_1,
\hat{e}_2 \) wird aus der Richtung \( \vec{d} \) selbst konstruiert; es
hängt nur von einer Hexaphoton-Größe ab. Mit einem festen Hilfsvektor
\( \hat{z} \):

\[
\hat{e}_1 = \frac{\hat{z}\times\vec{d}}{\lVert\hat{z}\times\vec{d}\rVert},
\qquad
\hat{e}_2 = \vec{d}\times\hat{e}_1
\]

\( \hat{e}_1, \hat{e}_2, \vec{d} \) bilden ein rechtwinkliges Dreibein.
Der Polarisationsvektor ist:

\[
\vec{\varepsilon} = J_1\,\hat{e}_1 + J_2\,\hat{e}_2
\]

> **Sonderfall.** Zeigt \( \vec{d} \) parallel zu \( \hat{z} \), versagt die
> Regel (\( \hat{z}\times\vec{d}=0 \)); dann wird ein Ausweich-Hilfsvektor
> verwendet. Dies ist eine bekannte, unvermeidbare Eigenheit jeder
> Bezugspaar-Konstruktion (vgl. Längengrade am Nordpol), kein Mangel.

Reelle \( J_1, J_2 \) ergeben **lineare**, eine 90°-Phasendifferenz
**zirkulare**, andere Werte **elliptische** Polarisation. \( \vec{\varepsilon} \)
steht nach Konstruktion stets senkrecht auf \( \vec{d} \) — die
Querwellen-Bedingung ist automatisch erfüllt.

---

## 2.4 Das Hexafeld als Summe der Beiträge

Ein Hexafeld ist eine Menge von Hexaphotonen:
\[
\mathcal{H} = \{ H_1, H_2, \dots, H_N \}
\]

Die resultierende Welle ergibt sich durch lineare Superposition der
Wellenbeiträge:

\[
E(\vec{x},t) = \sum_{i=1}^{N} F(H_i)
\]

wobei jedem \( H_i \) seine relative Phase \( \Delta\phi_i \) zugewiesen
wird (Baustein 1). Erst dadurch entstehen:

- Interferenz
- Kohärenz
- Phasenbeziehungen
- Wellencharakter

Diese Eigenschaften sind **nicht** im einzelnen Hexaphoton enthalten,
sondern entstehen erst durch die Summe.

---

## 2.5 Linearität des Mappings

Das Mapping ist **linear in den Wellenbeiträgen**: Die Welle eines
Hexafelds ist die Summe der Einzelwellen, und Skalierung eines
Wellenbeitrags überträgt sich direkt:

\[
F\!\left(\textstyle\sum_i H_i\right) = \sum_i F(H_i),
\qquad
A\cdot F(H) = F(H)\big|_{\text{Amplitude } A}
\]

> **Präzisierung.** Linear ist die **Superposition der Wellen**, nicht eine
> Rechenoperation „Zahl mal Hexaphoton". Ein Ausdruck wie \( aH \) ist nicht
> definiert — ein Hexaphoton ist das Tripel \( (f,P,d) \), kein Vektorraum-
> Element. Die Linearität betrifft ausschließlich die Wellenbeiträge
> \( F(H_i) \). Dies entspricht exakt der klassischen Wellenoptik.

---

## 2.6 Keine neue Physik

F ist eine **Reformulierung** der bekannten Maxwell-Lösung für ebene
Wellen und ihrer Superposition. Es werden **keine** neuen Annahmen
eingeführt.

---

## 2.7 Erweiterung F\* (optional)

Für spätere Arbeiten kann eine erweiterte Abbildung **F\*** definiert
werden, die nichtlineare Effekte beschreibt (Frequenzverschiebung wie
Raman, Erzeugung neuer Frequenzen wie SHG, Polarisationsänderungen
jenseits linearer Optik).

F\* ist **nicht Bestandteil** des Hexaphoton-Kernsystems, sondern eine
optionale Ergänzung.

---

## 2.8 Offene Punkte

- **K5 — Polarisationsvektor.** ✓ Gelöst (Abschnitt 2.3, Konvention B).
- **K6 — Amplituden-Konstante \( A \).** Offen. Der genaue Zusammenhang
  zwischen \( A \) und der Energie \( E \) (Einheiten, Proportionalitäts-
  faktor) ist noch festzulegen.
- **K7 — Übergang zur Modalbasis.** Offen. Für die Anbindung an die
  Mie-Streutheorie muss der Wechsel von der ebenen Welle zu sphärischen
  Streumoden ausgearbeitet werden.

---

## 2.9 Kommentar zur Interpretation

- Das Hexaphoton beschreibt **diskrete Freiheitsgrade**.
- F beschreibt, wie diese Freiheitsgrade zur **klassischen Welle** beitragen.
- Das Hexafeld ist die **Brücke** zwischen Einzelelement und Wellenbild.

Spekulative Hypothesen (H1–H7) werden **nicht** in F integriert.
