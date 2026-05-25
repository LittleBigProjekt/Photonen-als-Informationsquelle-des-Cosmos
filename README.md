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

Eine Interaktion mit Materie wird als Operator `T_M` beschrieben. Er wirkt
auf die **Lichtwelle** (das Ergebnis des Mappings F) und überführt eine
einfallende in eine ausgehende Welle:

```
Welle_aus = T_M ( Welle_ein )
```

`T_M` kann auf das Licht dreifach wirken — **umlenken** (Reflexion/Brechung),
**auswählen** (Spalt/Blende) oder **absorbieren**. Daneben kann Materie auch
selbst Licht **emittieren** (Wärmestrahlung, Spektrallinien). `T_M` codiert
Geometrie und Materialeigenschaften des Objekts. Dieser Operator-Formalismus
ist die etablierte Transferfunktions- bzw. Streumatrix-Theorie, in
Hexaphotone-Notation geschrieben. Details in Baustein 3.

---

## 📄 Inhalte dieses Repositories

| Datei | Inhalt | Status |
|-------|--------|--------|
| `README.md` | Diese Übersicht. | aktuell |
| `Baustein_1_Definitionen.md` | Definition von Hexaphoton, Hexafeld und der drei Größenklassen. | aktuell |
| `Baustein_2_Mapping.md` | Das Mapping F — Übersetzung von Hexaphoton/Hexafeld in eine Lichtwelle. | aktuell |
| `Baustein_3_Operator.md` | Der Operator T_M — Wechselwirkung mit Materie; Emission; offene Hypothesen H1–H4. | aktuell |
| `Baustein_4_Konsistenzpruefung.md` | Begleitdokument zur Konsistenz-Prüfung. | aktuell |
| `Baustein_4_Konsistenzpruefung.py` | Lauffähiges Prüf-Skript (Mie vs. Hexaphotone). | aktuell |
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
- [x] **Baustein 2 — Das Mapping F.** Vorschrift, wie aus einem Hexaphoton
      bzw. Hexafeld eine konkrete Lichtwelle wird. *(abgeschlossen)*
- [x] **Baustein 3 — Der Operator T_M.** Wechselwirkung mit Materie
      (umlenken / auswählen / absorbieren), Emission, sowie ein eigener
      Abschnitt für offene und spekulative Hypothesen. *(abgeschlossen)*
- [x] **Baustein 4 — Konsistenz-Prüfung.** Lauffähiger Code: die Notation
      dockt widerspruchsfrei an die Mie-Theorie an. *(abgeschlossen —
      Konsistenz-Prüfung, noch keine unabhängige Validierung)*
- [ ] **Offene Punkte K5–K7.** Polarisationsvektor, Einheiten, Modalbasis —
      müssen vor der echten Validierung geschlossen werden. *(in Arbeit)*
- [ ] **Baustein 5 — Unabhängige Validierung.** Die Streuung eigenständig
      aus den Bausteinen herleiten und gegen Mie prüfen.
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
