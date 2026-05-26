# Hexaphotone — Ein Notations-System für Licht als Informationsträger

### Eine kompakte, klassische Beschreibung von Licht über sechs Größen
**Autor:** Manuel Julin
**Lizenz:** CC-BY-SA 4.0
**Status:** Notations-System (Bausteine 1–4) konzeptuell abgeschlossen — work in progress

---

## 📘 Überblick

Dieses Repository entwickelt **Hexaphotone** — ein *Notations-System*, das
Licht über eine kompakte, modulare Beschreibung erfasst.

Wichtig zur Einordnung: Hexaphotone ist **keine neue physikalische Theorie**.
Es ist eine **Umformulierung etablierter klassischer Wellenoptik** (Maxwell,
Fourier-Optik, Mie-/T-Matrix-Streutheorie) in einer eigenen, intuitiven
Notation. Der Erfolgsmaßstab ist nicht „ist es wahr?" — die zugrunde liegende
Physik ist bekannt und korrekt — sondern „ist es konsistent, eindeutig und
nützlich?".

Spekulative Ideen, die über die etablierte Physik hinausgehen, werden
**streng getrennt** in einer eigenen Hypothesen-Sammlung geführt (siehe
Dateiliste). Sie sind **nicht Bestandteil** des Notations-Systems.

---

## 🔭 Kernidee: zwei Ebenen

Das System trennt strikt zwischen zwei Ebenen — die Vermischung beider war
der zentrale Fehler früherer Entwürfe.

| Ebene | Symbol | Bedeutung |
|-------|--------|-----------|
| **Hexaphoton** | `H` | Ein einzelnes Lichtelement — eine idealisierte Mode. |
| **Hexafeld** | `{Hᵢ}` | Ein Ensemble vieler Hexaphotonen — eine Quelle oder ein Bild. |

Ein einzelnes Hexaphoton ist *positionslos*: Es trägt eine **Richtung**, aber
keinen Herkunftsort. Form, Bild, Interferenz, Phase und die räumliche
Position einer Quelle sind **ausschließlich Hexafeld-Eigenschaften**.

---

## 🧩 Der Hexaphoton-Vektor

Ein Hexaphoton wird traditionell über sechs Größen benannt:

```
H = ( E , f , P , φ , p⃗ , d⃗ )
```

Diese sechs Größen sind **nicht gleichartig**. Sie zerfallen in drei Klassen:

| Klasse | Größen | Charakter |
|--------|--------|-----------|
| **Primär** | `f` (Frequenz), `P` (Polarisation), `d⃗` (Richtung) | Die drei unabhängigen Freiheitsgrade eines einzelnen Hexaphotons. |
| **Abgeleitet** | `E` (Energie), `p⃗` (Impuls) | Folgen über feste Constraints aus den Primärgrößen. |
| **Relation** | `φ` (Phase) | Keine Eigenschaft eines einzelnen `H`. Nur als Beziehung *zwischen* Hexaphotonen im Hexafeld definiert. |

Ein einzelnes Hexaphoton hat damit **3 unabhängige Freiheitsgrade**. Die
Bezeichnung „Hexa" (sechs) ist eine eingängige Etikette für die sechs
Größenarten — **kein Naturgesetz**.

### Constraint-Gleichungen

```
C1   E  = h · f                    (Energie aus Frequenz)
C2   p⃗  = (h · f / c) · d⃗          (Impuls aus Frequenz und Richtung)
```

---

## 🗂️ Die vier Bausteine

Das System ist in vier aufeinander aufbauenden **Bausteinen** organisiert:

| Baustein | Inhalt |
|----------|--------|
| **1 — Das Hexaphoton** | Definition von Hexaphoton, Hexafeld, den drei Größenklassen und den Constraints. |
| **2 — Das Mapping F** | Übersetzung eines Hexaphotons/Hexafelds in eine konkrete Lichtwelle. Enthält die Lösungen K5 (Polarisationsvektor), K6 (Amplitude) und K7 (Modalbasis). |
| **3 — Der Operator T_M** | Wechselwirkung mit Materie: umlenken, auswählen, absorbieren; Emission (Wärmestrahlung, Spektrallinien). |
| **4 — Konsistenzprüfung** | Prüfung am Beispiel der Mie-Streuung: die Notation dockt widerspruchsfrei an die etablierte Optik an. |

---

## 📄 Inhalte dieses Repositories

| Datei | Inhalt | Status |
|-------|--------|--------|
| `README.md` | Diese Übersicht. | aktuell |
| `Baustein_1_Hexaphoton_v4.md` | Baustein 1 — Definitionen. | aktuell (v4.1) |
| `Baustein_2_Mapping_v4.md` | Baustein 2 — Mapping F, inkl. K5/K6/K7. | aktuell (v4.1) |
| `Baustein_3_Operator_v4.md` | Baustein 3 — Operator T_M. | aktuell (v4.2) |
| `Baustein_4_Konsistenzpruefung_v4.md` | Baustein 4 — Konsistenzprüfung. | aktuell (v4.2) |
| `Baustein_4_Konsistenzpruefung.py` | Lauffähiges Prüf-Skript (Mie vs. Hexaphotone). | aktuell |
| `Hexaphotone_Hypothesen_Sammlung.md` | **Getrennte** Sammlung spekulativer Hypothesen (H1–H7). Nicht Teil des Notations-Systems. | aktuell |
| `LICENSE` | Lizenztext (CC-BY-SA 4.0). | aktuell |

> **Hinweis:** Frühere PDF-Versionen (PB 1.4, 2.0, 3.0) verwenden noch die
> überholte Bezeichnung „PIV" und vermischen die Hexaphoton- mit der
> Hexafeld-Ebene. Sie sind durch die Bausteine 1–4 (v4.x) abgelöst und
> sollten als veraltet gelten.

---

## 🗺️ Fahrplan

- [x] **Baustein 1 — Definitionen.** *(abgeschlossen, v4.1)*
- [x] **Baustein 2 — Das Mapping F.** Inkl. K5, K6, K7 gelöst. *(abgeschlossen, v4.1)*
- [x] **Baustein 3 — Der Operator T_M.** *(abgeschlossen, v4.2)*
- [x] **Baustein 4 — Konsistenzprüfung.** *(abgeschlossen, v4.2)*
- [ ] **Baustein 5 — Unabhängige Validierung.** Den Streuvorgang
      eigenständig aus den Bausteinen herleiten und numerisch gegen die
      Mie-Theorie prüfen. Setzt auf dem nun vollständigen Fundament auf.
- [ ] **Offene Frage (spätere Phase):** Lässt sich eine eigenständige,
      über die klassische Optik hinausgehende Vorhersage formulieren?

---

## ⚠️ Was Hexaphotone (noch) NICHT ist

Zur Ehrlichkeit gehört, klar zu sagen, was das System aktuell *nicht* leistet:

- Es ist **kein Quantenmodell.** Es quantisiert das Feld nicht und macht
  keine Aussagen über Einzelphotonen-Quanteneffekte.
- Es macht **keine Vorhersage**, die nicht auch direkt aus Maxwell/Mie folgt.
- Es ist **noch nicht unabhängig validiert.** Baustein 4 zeigt bislang nur
  *Konsistenz* (widerspruchsfreies Andocken an Mie), nicht eine eigenständige
  Herleitung. Die echte Validierung ist Baustein 5.
- Die **Hypothesen-Sammlung (H1–H7)** ist ausdrücklich spekulativ und kein
  Bestandteil des geprüften Notations-Systems.

---

## 📜 Lizenz

Dieses Projekt steht unter der **Creative Commons CC-BY-SA 4.0** Lizenz:
Jeder darf die Arbeit nutzen und weiterentwickeln; der Autor muss genannt
werden; Weiterentwicklungen müssen unter derselben Lizenz frei bleiben.

Vollständiger Lizenztext: https://creativecommons.org/licenses/by-sa/4.0/

---

## 📚 Zitierempfehlung

Manuel Julin (2026). *Hexaphotone — Ein Notations-System für Licht als
Informationsträger.* Arbeitsversion, Bausteine 1–4. CC-BY-SA 4.0.

---

## 🤝 Beiträge

Diskussionen, Ideen und Erweiterungen sind willkommen.
Pull Requests und Issues können jederzeit erstellt werden.
