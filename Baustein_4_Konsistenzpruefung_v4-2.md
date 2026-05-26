# Baustein 4 — Konsistenzprüfung am Beispiel der Mie-Streuung (Version 4.2)

## 4.1 Zweck dieses Bausteins

Baustein 4 zeigt, dass das Hexaphoton-Notations-System **kompatibel mit
der etablierten klassischen Optik** ist. Als Prüfbeispiel dient ein
realer, gut untersuchter Prozess: **Mie-Streuung an kugelförmigen
Partikeln.**

Dieser Baustein postuliert keine neue Physik, sondern prüft, ob die
Notation korrekt, widerspruchsfrei und auf reale optische Phänomene
anwendbar ist.

> **Wichtige Einordnung — was dieser Baustein ist und was nicht.**
> Dies ist eine **Konsistenzprüfung**, keine *unabhängige Validierung*.
> Sie zeigt, dass die Hexaphotone-Notation widerspruchsfrei an die
> Mie-Theorie *andockt*. Sie zeigt **nicht**, dass das System die
> Streuung aus eigener Kraft — allein aus F und Superposition —
> herleitet. Eine echte unabhängige Validierung ist Gegenstand eines
> späteren Bausteins 5; die dafür nötigen Klärungspunkte K5–K7 sind
> inzwischen geschlossen (siehe Abschnitt 4.9).

---

## 4.2 Ausgangspunkt: Das Hexafeld

Ein Hexafeld ist eine Menge von Hexaphotonen:
\[
\mathcal{H} = \{ H_1, H_2, \dots, H_N \}, \qquad H_i = (f_i, P_i, d_i)
\]

Die resultierende Welle ergibt sich durch Superposition:
\[
E(\vec{x},t) = \sum_{i=1}^{N} F(H_i)
\]

Dies ist exakt die klassische Superposition elektromagnetischer Wellen.

---

## 4.3 Wirkung von Materie: Anwendung von T_M

Ein Partikel (z. B. ein Wassertröpfchen) wirkt auf jedes Hexaphoton über
den Materie-Operator:
\[
T_M(H_i) = (f_i', P_i', d_i')
\]

In linearer Optik gilt \( f_i' = f_i \), \( P_i' = M_P P_i \),
\( d_i' = M_d d_i \). Damit ist T_M kompatibel mit der klassischen
Beschreibung der Streuung.

---

## 4.4 Vergleich mit der Mie-Theorie

Die Mie-Theorie beschreibt winkelabhängige Intensität und Polarisation,
Phasenverschiebungen, spektrale Abhängigkeit und Richtungsänderungen.
In Hexaphotone-Notation entstehen diese Größen durch:

1. Transformation der Polarisation: \( P' = M_P(\theta,\phi)\,P \)
2. Transformation der Richtung: \( d' = d'(\theta,\phi) \)
3. Superposition aller gestreuten Beiträge:
   \( E_{\text{scat}} = \sum_i F(T_M(H_i)) \)

Die Notation bildet damit dieselben Größen ab wie die Mie-Theorie.

> **Ehrlichkeitshinweis.** Dass die Notation dieselben Größen abbildet,
> bedeutet: sie ist mit Mie *kompatibel*. Es bedeutet nicht, dass sie
> Mie *ersetzt* oder unabhängig reproduziert. Die konkrete numerische
> Prüfung leistet das Begleit-Skript (siehe 4.7).

---

## 4.5 Konsistenzkriterien

Das Notationssystem ist konsistent, wenn:

1. **Frequenz erhalten bleibt** — ✔ erfüllt (linear-optisch korrekt)
2. **Polarisation korrekt transformiert wird** — ✔ erfüllt (Jones/Mueller)
3. **Richtungsänderungen korrekt abgebildet werden** — ✔ erfüllt
4. **Superposition identisch zur klassischen Wellenoptik ist** — ✔ erfüllt
5. **Keine neue Physik eingeführt wird** — ✔ erfüllt (reine Notation)

Damit ist das Hexaphoton-System **konzeptuell konsistent** mit der
klassischen Mie-Streuung.

---

## 4.6 Was Baustein 4 NICHT tut

- Er führt **keine** neuen Mechanismen ein.
- Er testet **keine** spekulativen Hypothesen (H1–H7).
- Er ersetzt **nicht** die Mie-Theorie.
- Er dient **nicht** der Modellierung von Nichtlinearitäten.
- Er liefert **keine** unabhängige Validierung (siehe 4.1).

---

## 4.7 Numerisches Begleit-Skript

Zur konkreten Prüfung gehört ein lauffähiges Python-Skript
(`Baustein_4_Konsistenzpruefung.py`). Es rechnet die Streuung an einer
Kugel auf zwei Wegen (Mie-Referenz und Hexaphotone-Notation) und
vergleicht sie für mehrere Kugelgrößen.

Das Skript bestätigt die **Konsistenz** (widerspruchsfreies Andocken).
Es ist — wie in 4.1 erläutert — keine unabhängige Validierung, da der
Hexaphotone-Weg denselben Mie-Kern nutzt.

---

## 4.8 Erweiterbarkeit

Das System kann später erweitert werden: nichtlineare Streuung (über
T\*_M), spektrale Verteilungen, kohärente vs. inkohärente Felder,
zeitabhängige Felder. Diese Erweiterungen verändern den Kern nicht.

---

## 4.9 Status und nächster Schritt

- **K6** — Amplituden-Konstante \( A \): ✓ gelöst (Baustein 2, Abschnitt 2.7).
- **K7** — Übergang zur Modalbasis: ✓ gelöst (Baustein 2, Abschnitt 2.8,
  konzeptuell).
- **Baustein 5** — unabhängige Validierung: Mit K5–K7 geschlossen ist nun
  die Grundlage gelegt, den Streuvorgang eigenständig aus den Bausteinen
  herzuleiten und gegen Mie zu prüfen.

---

## 4.10 Zusammenfassung

Baustein 4 zeigt:

- Das Hexaphoton-System ist **konzeptuell konsistent** mit der
  klassischen Optik.
- Die Notation bildet reale physikalische Prozesse widerspruchsfrei ab.
- Es gibt **keine Widersprüche** zu etablierten Messungen.

Damit ist das Hexaphoton-Notations-System (Bausteine 1–4) auf der
Notations-Ebene **in sich stimmig**. Eine unabhängige numerische
Validierung steht noch aus (Baustein 5); die Klärungspunkte K5–K7
sind dafür bereits geschlossen.
