# Hexaphotone — Baustein 4: Konsistenz-Prüfung

> **Status:** Arbeitsdokument (work in progress) — Revision 1
> **Baut auf:** Baustein 1 (Definitionen), Baustein 2 (Mapping F),
> Baustein 3 (Operator T_M).
> **Zugehöriger Code:** `Baustein_4_Konsistenzpruefung.py`
> **Zweck:** Begleitdokument zum Prüf-Skript. Erklärt, was die Prüfung
> zeigt — und, ebenso wichtig, was sie **nicht** zeigt.

---

## 1. Worum es geht

Die Bausteine 1–3 waren Texte: Definitionen und Konzepte. Baustein 4 ist
der erste Baustein, in dem tatsächlich **gerechnet** wird — mit lauffähigem
Programmcode.

Geprüft wird ein konkretes, einfaches Streuproblem: **eine Lichtwelle trifft
auf eine homogene Kugel.** Das Problem wird auf zwei Weisen beschrieben:

| Weg | Beschreibung |
|-----|--------------|
| **Weg A** | Klassische Mie-Theorie (Gustav Mie, 1908) — die etablierte, exakte Referenzlösung. |
| **Weg B** | Dasselbe Problem in Hexaphotone-Notation (Bausteine 1–3). |

Verglichen wird die **Winkelverteilung** des gestreuten Lichts — also: in
welche Richtungen wird wie viel Licht gestreut.

---

## 2. Das Ergebnis

Für drei verschiedene Kugelgrößen (Größenparameter `x ≈ 0,75`, `3` und `8`)
stimmen Weg A und Weg B **exakt überein** — die Abweichung ist null bis auf
Rechengenauigkeit. Die Kurven in der zugehörigen Grafik
(`Baustein_4_Konsistenzpruefung.png`) liegen vollständig deckungsgleich
übereinander.

---

## 3. Was dieses Ergebnis bedeutet — und was nicht

Hier ist **Ehrlichkeit** wichtiger als ein schönes Resultat.

### 3.1 Was die Prüfung zeigt

Sie zeigt, dass die Hexaphotone-Notation **widerspruchsfrei an die
Mie-Theorie andockt**. Konkret: Die Kette aus den Bausteinen —

```
Frequenz f  →  Wellenlänge λ = c/f  →  Größenparameter x = 2πR/λ
```

— verknüpft die Hexaphoton-Größen (Baustein 1/2) korrekt mit der
Objektgröße der Kugel. Die Einheiten passen, die Constraints C1/C2 aus
Baustein 1 sind erfüllt, und der Operator-Begriff `T_Kugel` aus Baustein 3
lässt sich konsistent anwenden. Das ist ein **echter, nützlicher Befund**:
Es bedeutet, dass die Notation sauber gebaut ist und keine inneren
Widersprüche enthält, die beim Rechnen sofort auffallen würden.

### 3.2 Was die Prüfung NICHT zeigt

Die exakte Übereinstimmung ist **erwartet** — und genau deshalb ist sie
**kein Beweis**, dass Hexaphotone „die Physik richtig herleitet".

Der Grund: Baustein 3, Abschnitt 6 hat `T_Kugel` ausdrücklich **definiert**
als die Mie-Lösung, nur in Hexaphotone-Schreibweise gelesen. Im Code ruft
Weg B daher denselben Mie-Rechenkern auf wie Weg A. Zwei Wege, die mit
demselben Kern rechnen, *müssen* dasselbe Ergebnis liefern. Das ist fast
eine Tautologie:

> „Wenn man `T_Kugel` als die Mie-Lösung definiert, dann ist `T_Kugel` die
> Mie-Lösung."

Das ist **Konsistenz**, nicht **Validierung**. Die Prüfung bestätigt, dass
die Notation in sich stimmig ist — sie testet aber nicht, ob Hexaphotone
ein Streuergebnis *aus eigener Kraft* erzeugen kann.

### 3.3 Der Unterschied in einem Satz

- **Konsistenz-Prüfung** (das hier): Passt die Notation widerspruchsfrei zur
  bekannten Physik? → Ja.
- **Echte Validierung** (noch offen): Kann Hexaphotone die Streuung aus
  seinen *eigenen* Bausteinen (F_einzeln + Superposition) unabhängig
  herleiten und trifft damit die Mie-Kurve? → noch nicht geprüft.

---

## 4. Was eine echte Validierung bräuchte

Eine unabhängige Validierung müsste Weg B **vollständig aus den Bausteinen
selbst** aufbauen — ohne den Mie-Kern zu benutzen. Dafür müssten zuerst die
offenen Punkte aus den Bausteinen 2 und 3 geschlossen werden:

- **K5** — der Polarisationsvektor `ε⃗(Pᵢ)` muss konkret definiert werden;
- **K6** — die Amplituden-Konstante / Einheiten müssen festgelegt werden;
- **K7** — der Übergang von der ebenen Welle zur Modalbasis (sphärische
  Harmonische) muss ausgearbeitet werden.

Erst dann kann Weg B die Streuung wirklich eigenständig rechnen. Das ist
Gegenstand eines späteren **Baustein 5**.

---

## 5. Einordnung im Projekt

Baustein 4 ist damit ein **ehrlicher Zwischenstand**, kein Schlusspunkt:

- ✅ Die Notation der Bausteine 1–3 ist in sich stimmig und rechnet
  widerspruchsfrei.
- ✅ Es gibt erstmals lauffähigen, nachvollziehbaren Code.
- ⏳ Die unabhängige Validierung steht noch aus (Baustein 5, nach K5–K7).

Das ist genau der Zustand, den man von einem ehrlichen Arbeits-Repo erwartet:
Ein solider, geprüfter Zwischenschritt — klar benannt als das, was er ist.

---

## 6. Hinweise zum Code

Das Skript `Baustein_4_Konsistenzpruefung.py`:

- benötigt nur `numpy`, `scipy`, `matplotlib` — **keine** externe
  Mie-Bibliothek (die Mie-Berechnung ist im Code selbst implementiert und
  damit vollständig nachvollziehbar);
- gibt die Ergebnisse als Text aus und erzeugt die Vergleichsgrafik
  `Baustein_4_Konsistenzpruefung.png`;
- enthält im Kopf denselben ehrlichen Hinweis wie dieses Dokument:
  Konsistenz-Prüfung, keine Validierung.

Ausführen:

```
python3 Baustein_4_Konsistenzpruefung.py
```

---

*Ende Baustein 4, Revision 1. Nächster Schritt: die offenen Punkte K5–K7
schließen, dann Baustein 5 — die echte, unabhängige Validierung.*
