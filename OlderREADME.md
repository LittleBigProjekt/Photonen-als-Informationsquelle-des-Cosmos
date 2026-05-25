# Hexaphotone — Ein Notations-System für Licht als Informationsträger

### Eine kompakte, klassische Beschreibung von Licht über sechs Größen
**Autor:** Manuel Julin
**Lizenz:** CC-BY-SA 4.0
**Status:** Arbeitsdokument / work in progress

---

## 📘 Überblick

Dieses Repository entwickelt **Hexaphotone** — ein *Notations-System*, das
Licht über eine kompakte, modulare Beschreibung erfasst.

Wichtig zur Einordnung: Hexaphotone ist in seiner aktuellen Form **keine neue
physikalische Theorie**. Es ist eine **Umformulierung etablierter klassischer
Wellenoptik** (Maxwell, Fourier-Optik, Mie-/T-Matrix-Streutheorie) in einer
eigenen, intuitiven Notation. Der Erfolgsmaßstab ist daher nicht „ist es
wahr?" — die zugrunde liegende Physik ist bekannt und korrekt — sondern
„ist es konsistent, eindeutig und nützlich?".

Ob daraus später eine echte, über die Standardoptik hinausgehende
*Vorhersage* entstehen kann, ist eine offene Frage für eine spätere Phase.
Bis dahin gilt: ehrliche Positionierung als Notations-System.

---

## 🔭 Kernidee: zwei Ebenen

Das System trennt strikt zwischen zwei Ebenen — die Vermischung beider war
der zentrale Fehler früherer Entwürfe.

| Ebene | Symbol | Bedeutung |
|-------|--------|-----------|
| **Hexaphoton** | `H` | Ein einzelnes Lichtelement — eine idealisierte Mode bzw. ein Strahl. |
| **Hexafeld** | `{Hᵢ}` | Ein Ensemble vieler Hexaphotonen — eine Quelle oder ein Bild. |

Ein einzelnes Hexaphoton ist *positionslos*: Es trägt eine **Richtung**, aber
keinen Herkunftsort. Form, Bild, Projektion, Interferenz und die räumliche
Position einer Quelle sind **ausschließlich Hexafeld-Eigenschaften**.

---

## 🧩 Der Hexaphoton-Vektor

Ein Hexaphoton wird traditionell über sechs Größen benannt:

```
H = ( E , f , Pᵢ , φ , p⃗ , d⃗ )
```

Diese sechs Größen sind **nicht gleichartig**. Sie zerfallen in drei Klassen:

| Klasse | Größen | Charakter |
|--------|--------|-----------|
| **A — Eigenschaften** | `f` (Frequenz), `Pᵢ` (Polarisation), `d⃗` (Richtung) | Echte, unabhängige Freiheitsgrade eines einzelnen Hexaphotons. |
| **B — Abgeleitet** | `E` (Energie), `p⃗` (Impuls) | Folgen über feste Constraints aus Klasse A. Deklarierte Redundanz. |
| **C — Relation** | `φ` (Phase) | Keine Eigenschaft eines einzelnen `H`. Nur als Beziehung *zwischen* Hexaphotonen im Hexafeld definiert. |

Ein einzelnes Hexaphoton hat damit **3 unabhängige Freiheitsgrade**
(`f`, `Pᵢ`, `d⃗`). Die Bezeichnung „Hexa" (sechs) ist eine eingängige
Etikette für die sechs Größenarten — **kein Naturgesetz**.

### Constraint-Gleichungen

```
C1   E  = h · f                    (Energie aus Frequenz)
C2   p⃗  = (h · f / c) · d⃗          (Impuls aus Frequenz und Richtung)
```

`h` = Plancksches Wirkungsquantum, `c` = Lichtgeschwindigkeit.

### Die Phase φ

Eine **absolute** Phase eines einzelnen Hexaphotons ist physikalisch
bedeutungslos. Nur die **relative Phase zwischen** Hexaphotonen ist
beobachtbar (sie steuert Interferenz). Die Phase ist daher eine
Relationsgröße auf Hexafeld-Ebene:

```
Δφᵢ = φᵢ − φ_ref
```

---

## 🔄 Interaktion mit Materie

Eine Interaktion mit Materie wird als linearer Operator `T_M` beschrieben,
der ein eingehendes in ein ausgehendes Hexaphoton (bzw. Hexafeld) überführt:

```
H_aus = T_M ( H_ein )
```

`T_M` codiert Geometrie und Materialeigenschaften des streuenden Objekts.
Dieser Operator-Formalismus ist die etablierte Transferfunktions- bzw.
Streumatrix-Theorie, in Hexaphotone-Notation geschrieben.

---

## 📄 Inhalte dieses Repositories

| Datei | Inhalt | Status |
|-------|--------|--------|
| `README.md` | Diese Übersicht. | aktuell |
| `Baustein_1_Definitionen.md` | Saubere Definition von Hexaphoton, Hexafeld und der drei Größenklassen. | aktuell |
| `LICENSE` | Lizenztext (CC-BY-SA 4.0). | aktuell |

> **Hinweis:** Frühere PDF-Versionen des Dokuments verwenden noch die
> überholte Bezeichnung „PIV — photonischer Informationsvektor" und
> vermischen die Hexaphoton- mit der Hexafeld-Ebene. Sie werden Schritt
> für Schritt durch die neuen Bausteine ersetzt.

---

## 🗺️ Fahrplan

Das Projekt wird in **Bausteinen** entwickelt, die aufeinander aufbauen:

- [x] **Baustein 1 — Definitionen.** Hexaphoton, Hexafeld, drei Größenklassen,
      Constraints. *(abgeschlossen)*
- [ ] **Baustein 2 — Das Mapping F.** Vorschrift, wie aus einem Hexaphoton
      bzw. Hexafeld eine konkrete komplexe Modalamplitude wird. Macht das
      System rechenfähig.
- [ ] **Baustein 3 — Operatoren.** Saubere Definition von `T_M` und der
      Anbindung an Mie-/T-Matrix-Streutheorie.
- [ ] **Baustein 4 — Numerische Validierung.** Ein konkretes Streuproblem
      durchrechnen und gegen eine etablierte Mie-Bibliothek prüfen.
- [ ] **Offene Frage (spätere Phase):** Lässt sich eine eigenständige,
      über die klassische Optik hinausgehende Vorhersage formulieren?

---

## ⚠️ Was Hexaphotone (noch) NICHT ist

Zur Ehrlichkeit gehört, klar zu sagen, was das System aktuell *nicht* leistet:

- Es ist **kein Quantenmodell.** Es quantisiert das Feld nicht und macht
  keine Aussagen über Einzelphotonen-Quanteneffekte.
- Es macht **keine Vorhersage**, die nicht auch direkt aus Maxwell/Mie folgt.
- Es ist **nicht numerisch validiert** — das ist Baustein 4.

---

## 📜 Lizenz

Dieses Projekt steht unter der **Creative Commons CC-BY-SA 4.0** Lizenz:

- Jeder darf die Arbeit nutzen und weiterentwickeln.
- Der Autor muss genannt werden.
- Weiterentwicklungen müssen unter derselben Lizenz frei bleiben.

Vollständiger Lizenztext: https://creativecommons.org/licenses/by-sa/4.0/

---

## 📚 Zitierempfehlung

Manuel Julin (2026). *Hexaphotone — Ein Notations-System für Licht als
Informationsträger.* Arbeitsversion. CC-BY-SA 4.0.

---

## 🤝 Beiträge

Diskussionen, Ideen und Erweiterungen sind willkommen.
Pull Requests und Issues können jederzeit erstellt werden.
