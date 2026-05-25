# Hexaphotone — Baustein 3: Der Operator T_M (Wechselwirkung mit Materie)

> **Status:** Arbeitsdokument (work in progress) — Revision 2
> **Baut auf:** Baustein 1 (Definitionen), Baustein 2 (Mapping F).
> **Zweck:** Definiert den Operator T_M, der beschreibt, wie Materie eine
> Lichtwelle verändert, sowie die Emission neuer Hexaphotonen durch Materie.
> Der überprüfte Teil ist die Hexaphotone-Schreibweise etablierter
> klassischer Optik. Spekulative Annahmen sind in Abschnitt 9 **getrennt**
> und als solche gekennzeichnet.

---

## 1. Was T_M ist und was es leistet

Baustein 2 hat aus einem Hexafeld eine konkrete Lichtwelle gemacht
(`F_feld`). Baustein 3 beschreibt, was passiert, wenn diese Welle auf ein
**Objekt** trifft — einen Spiegel, einen Spalt, eine Kugel.

**T_M ist eine Vorschrift, die eine Welle verändert.** Wie F ist es eine
Funktion. Der Unterschied:

| | Eingabe | Ausgabe | Was es tut |
|---|---------|---------|------------|
| `F` | Hexaphoton / Hexafeld | Welle | übersetzt Beschreibung → Welle |
| `T_M` | Welle | veränderte Welle | verändert eine Welle an der Materie |

```
Welle_aus  =  T_M ( Welle_ein )
```

Eingabe und Ausgabe sind **dieselbe Art von Ding** — beides eine Lichtwelle.

**Das „M" ist ein Platzhalter für das Objekt.** Jedes Objekt hat sein eigenes
T_M: ein Spiegel `T_Spiegel`, ein Spalt `T_Spalt`, eine Glaskugel `T_Kugel`.
T_M ist der eine Ort, an dem die gesamte Materialphysik sitzt.

> **Designentscheidung (Variante A):** T_M wirkt auf die **Welle** — das
> Ergebnis von F —, nicht direkt auf das Hexafeld. Vollständige Kette:
>
> ```
> Hexafeld {Hᵢ}  →  F_feld  →  Welle_ein  →  T_M  →  Welle_aus
> ```

> **Einordnung — ehrlich:** Der überprüfte Teil von T_M (Abschnitte 2–6) ist
> kein neues Konzept. Es ist die etablierte **Transferfunktion** bzw.
> **Streumatrix** der klassischen Optik in Hexaphotone-Schreibweise.

---

## 2. Was T_M NICHT ist: kein Speicher

Ein verbreitetes Missverständnis: dass ein Spiegel die Welle „speichert" oder
ihr Bild aufbewahrt. **Das tut er nicht.**

T_M ist eine reine **Durchgangs-Vorschrift**: Welle rein, veränderte Welle
sofort raus. Es gibt **kein Gedächtnis**. Die „Form des Spiegels", die im
reflektierten Licht erscheint, steckt nicht in einem gespeicherten Bild — sie
steckt darin, *wie* `T_Spiegel` die Richtungen der vielen Einzelwellen
umlenkt. Die Form ist eine Eigenschaft der *Vorschrift*, kein abgelegter Inhalt.

---

## 3. Die drei Wirkungen von T_M auf einfallendes Licht

Wenn eine Welle auf Materie trifft, kann mit den Hexaphotonen, aus denen sie
besteht, dreierlei geschehen. Jedes reale T_M ist eine Mischung dieser drei.

### 3.1 Umlenken — das Hexaphoton existiert weiter

**Reflexion und Brechung.** Das Hexaphoton wird abgelenkt: seine Richtung `d⃗`
ändert sich. Aber es **existiert weiter** — Frequenz, Polarisation und
Phaseninformation bleiben erhalten (ggf. geordnet transformiert).

```
T_umlenk:   d⃗_ein  →  d⃗_aus        (Richtung geändert)
            f, Pᵢ           bleiben erhalten
```

Beispiele: Spiegel (`T_Spiegel` kehrt die Richtungskomponente senkrecht zur
Oberfläche um), Glasoberfläche (Brechung nach Snellius). **Information bleibt
erhalten** — sie wird nur geordnet umgeformt.

### 3.2 Auswählen — ein Teil kommt durch, ein Teil nicht

**Blenden, Spalte, Aperturen.** Das Objekt lässt nur einen *Teil* der
einfallenden Hexaphotonen passieren; der Rest wird geblockt.

```
T_auswahl:  Hexaphoton im Durchlassbereich  →  kommt durch
            Hexaphoton außerhalb            →  geblockt
```

Dies ist eine **Auswahl** des Hexafelds. Es ist der Mechanismus hinter Beugung
am Spalt und hinter der Lochkamera.

> **Hinweis (korrigiert eine frühere Notiz):** Der Spalt-Effekt ist
> **klassische Wellenoptik** — er funktioniert auch mit Schallwellen. Er ist
> **nicht** dasselbe wie der quantenmechanische Messprozess. Zwei verschiedene
> Phänomene, hier nicht vermischt.

### 3.3 Absorbieren — Energie geht über, Lichtordnung löst sich auf

**Absorption.** Das Hexaphoton wird vom Material aufgenommen. Seine Energie
geht über in die ungeordnete Wärmebewegung der Atome.

```
T_absorb:   Hexaphoton-Energie E  →  Wärme (ungeordnete Schwingung der Materie)
```

**Energie bleibt erhalten.** Kein Joule geht verloren — die Energie ist als
Wärme im Material. Das ist der Energieerhaltungssatz, und das System
respektiert ihn vollständig.

**Was mit der geordneten Lichtstruktur geschieht.** Das einfallende Licht hatte
eine *geordnete* Struktur: eine Richtung `d⃗`, eine Polarisation `Pᵢ`, scharfe
Frequenzen `f`, definierte relative Phasen. Wärme dagegen ist *ungeordnete*
Schwingung — in alle Richtungen, ohne Vorzugspolarisation, phasen-chaotisch,
über einen breiten Frequenzbereich verschmiert. Beim Übergang Licht → Wärme
ist diese geordnete Struktur im Material **nicht mehr auffindbar**.

> **Energiebeitrag hängt von der Frequenz ab.** Nach Baustein 1 (C1) gilt
> `E = h·f`. Ein blaues Hexaphoton (hohe Frequenz) trägt **mehr Energie** als
> ein rotes (niedrige Frequenz) — und gibt bei Absorption entsprechend **mehr
> Wärme** ab. Der Wärmebeitrag pro Hexaphoton ist also farbabhängig, nicht
> für alle Hexaphotonen gleich.

> **Materialspezifisches Absorptionsmuster.** *Welche* Frequenzen ein Material
> absorbiert, ist für jede Atomart charakteristisch und stabil — ein festes
> *Muster* von Frequenzen, für jedes Element verschieden. Diese
> Materialabhängigkeit ist die Grundlage der Spektroskopie und der Grund,
> warum Materialien Farben haben. (Siehe auch Abschnitt 5.2 — dasselbe Muster
> tritt bei der Emission wieder auf.)

---

## 4. Die zwei Arten der Emission: Materie sendet Licht aus

Materie nimmt nicht nur Licht auf — sie kann auch welches **aussenden**, also
**neue Hexaphotonen erzeugen**. Das ist der vierte Vorgang neben den drei
Wirkungen aus Abschnitt 3.

Es gibt **zwei physikalisch verschiedene** Arten der Emission. Sie zu trennen
ist wichtig, weil sie unterschiedlichen Regeln folgen.

### 4.1 Wärmestrahlung (Glühen) — temperaturbestimmt

Jeder warme Körper sendet Licht aus, **weil** er warm ist: heißes Eisen, eine
Glühlampe, die Sonne. Die entscheidende Eigenschaft:

> **Die Farbverteilung der Wärmestrahlung hängt allein von der Temperatur ab —
> nicht vom Material.** Eisen, Kohle, Wolfram, Keramik: auf dieselbe Temperatur
> gebracht, glühen sie in derselben Farbe.

- ~800 °C → Rotglut
- ~1200 °C → Gelborange
- ~1500 °C und mehr → fast weiß

Heißer bedeutet **zugleich heller und farblich verschoben** (von rot Richtung
weiß). Temperatur steuert also *beides* — Helligkeit und Farbverteilung.

Das Material beeinflusst nur, *wie effizient* abgestrahlt wird (die
sogenannte Emissivität), **nicht** die Farbverteilung selbst.

> **Praktischer Prüfstein:** Schmiede lesen seit Jahrhunderten die Temperatur
> ihres Werkstücks an der Glühfarbe ab. Das funktioniert nur, weil die
> Glühfarbe materialunabhängig allein von der Temperatur abhängt.

In Hexaphotone-Sprache: Ein heißes Material ist ein **Hexafeld-Erzeuger**. Es
produziert neue Hexaphotonen, deren Frequenzverteilung die Temperatur
bestimmt. Es ist ein *breites, kontinuierliches* Spektrum — keine scharfe
Frequenz. (Die exakte Form beschreibt das Plancksche Strahlungsgesetz.)

### 4.2 Spektrallinien — materialbestimmt

Daneben gibt es Emission bei **materialspezifischen, scharfen Frequenzen**:
Natrium leuchtet gelb, Neon rotorange, Kupfer grünlich. Sichtbar bei
Gasentladungslampen, Feuerwerk, Flammenfärbung.

Dies ist **nicht** Wärmestrahlung. Es ist ein eigener Vorgang: angeregte
Elektronen fallen auf bestimmte Energieniveaus zurück und senden dabei
Hexaphotonen genau festgelegter Frequenzen aus.

> **Verbindung zu Abschnitt 3.3:** Die Frequenzen der Spektrallinien-Emission
> eines Elements sind **dieselben** wie sein Absorptionsmuster. Das
> materialspezifische Frequenzmuster ist zwei Seiten einer Medaille — einmal
> beim Aufnehmen (Absorption), einmal beim Aussenden (Emission).

### 4.3 Wichtig: emittierte Hexaphotonen sind neue Hexaphotonen

Bei beiden Emissionsarten gilt für den **überprüften** Teil des Systems:

> Die emittierten Hexaphotonen sind **neu**. Ihre Eigenschaften werden bei der
> Wärmestrahlung durch die *Temperatur*, bei den Spektrallinien durch die
> *Atomart* bestimmt — **nicht** durch die Eigenschaften zuvor absorbierter
> Hexaphotonen. Beleg: Mit blauem Licht aufgeheiztes Eisen glüht bei gegebener
> Temperatur **gleich** wie mit rotem Licht aufgeheiztes. Die Glühfarbe verrät
> die Temperatur, nicht die Vorgeschichte.

> Die *weitergehende* Frage, ob Emission stattdessen eine Umordnung zuvor
> absorbierter Hexaphotonen sein könnte, ist damit **nicht** beantwortet. Eine
> alternative, spekulative Deutung dieses Vorgangs findet sich in Abschnitt 9
> (Hypothese H3); die verwandten Fragen nach Fortbestand und Identität in
> H1 und H2. Der überprüfte Teil des Systems hängt von diesen Hypothesen
> nicht ab.

---

## 5. Zusammensetzung und Energiebilanz

Ein reales Objekt wirkt nie nur auf eine Weise. Ein realer Spiegel reflektiert
das meiste Licht, schluckt aber einen Teil — deshalb wird er warm. Formal:

```
T_M  =  Anteil_Umlenkung  +  Anteil_Auswahl  +  Anteil_Absorption
```

Die Anteile hängen von Material und Frequenz `f` ab.

**Energiebilanz.** Was an Energie hineingeht, kommt entweder umgelenkt heraus,
wird durchgelassen oder absorbiert. Nichts geht verloren:

```
E_ein  =  E_umgelenkt  +  E_durchgelassen  +  E_absorbiert
```

Kommt durch Emission (Abschnitt 4) Energie hinzu, stammt sie aus dem
Wärmevorrat bzw. der Anregungsenergie des Materials — auch hier bleibt die
Gesamtenergie erhalten.

---

## 6. Anbindung an die Mie- / T-Matrix-Streutheorie (konzeptuell)

Damit `T_M` an überprüfbare Physik gebunden ist, wird es an etablierte
Streutheorie angeschlossen. Dieser Abschnitt bleibt **konzeptuell** — die
vollständige Rechnung folgt in Baustein 4.

### 6.1 Die Kugel als Referenzobjekt

Für eine homogene Kugel ist die Wirkung auf eine Lichtwelle **exakt bekannt**:
die **Mie-Theorie** (Gustav Mie, 1908) liefert die vollständige Lösung. Die
Kugel dient als **Eichobjekt**: `T_Kugel` ist nicht geraten, sondern bekannt.
Wenn Hexaphotone korrekt ist, muss `T_Kugel` in Hexaphotone-Schreibweise
dieselben Ergebnisse liefern wie die direkte Mie-Rechnung.

### 6.2 T-Matrix für allgemeine Objekte

Für Objekte, die keine Kugeln sind, leistet die **T-Matrix-Methode** dasselbe
allgemeiner. In Hexaphotone-Sprache: Die T-Matrix **ist** ein konkret
berechenbares `T_M` für allgemeine Objektformen — der Referenzmaßstab, gegen
den jede Hexaphotone-Rechnung geprüft werden kann.

### 6.3 Was Baustein 4 leisten muss

Dort wird mit einer etablierten Mie-Bibliothek die Streuung an einer Kugel
berechnet, dasselbe Problem in Hexaphotone-Notation durchgerechnet und
geprüft, ob beide übereinstimmen. Stimmen sie überein, ist das System als
Notations-System validiert.

---

## 7. Das Ergebnis wieder als Hexafeld lesen

Das Ergebnis `Welle_aus` ist selbst wieder eine Lichtwelle — und damit nach
Baustein 2 wieder als Hexafeld darstellbar:

```
Welle_aus   →   (Umkehrung von F_feld)   →   Hexafeld {Hᵢ'}
```

Das ausgehende Hexafeld `{Hᵢ'}` hat im Allgemeinen andere Richtungen `d⃗ᵢ'`
(Umlenkung), weniger Hexaphotonen (Auswahl, Absorption) — oder zusätzliche
(Emission) — und veränderte relative Phasen `Δφᵢ'`.

---

## 8. Zusammenfassung als Diagramm

```
   HEXAFELD {Hᵢ}
        │  F_feld  (Baustein 2)
        ▼
   WELLE_ein
        │
        │  T_M  =  Umlenkung + Auswahl + Absorption
        │
        ├──[Umlenkung]───▶ Hexaphoton existiert weiter, d⃗ geändert
        ├──[Auswahl]─────▶ Teil kommt durch, Teil geblockt
        └──[Absorption]──▶ Energie → Wärme; Lichtordnung löst sich auf
        │
        │  + EMISSION (Materie erzeugt neue Hexaphotonen)
        ├──[Wärmestrahlung]──▶ neue Hexaphotonen, Spektrum durch TEMPERATUR
        └──[Spektrallinien]──▶ neue Hexaphotonen, Frequenz durch ATOMART
        ▼
   WELLE_aus
        │  (Umkehrung von F_feld)
        ▼
   HEXAFELD {Hᵢ'}

   Referenzmaßstab für T_M:  Mie-Theorie (Kugel) / T-Matrix (allgemein)
                              → konkrete Rechnung in Baustein 4
```

---

## 9. Offene Hypothesen und spekulative Annahmen

> **Zweck dieses Abschnitts.** Die Abschnitte 1–8 beschreiben ausschließlich
> überprüfte, etablierte Physik in Hexaphotone-Schreibweise. Der vorliegende
> Abschnitt sammelt **spekulative Annahmen** des Autors, die **derzeit nicht
> überprüfbar** sind. Sie werden hier bewusst nicht als Tatsachen, sondern als
> *offene Hypothesen* festgehalten — damit sie dokumentiert sind und später
> mit Fachleuten diskutiert und, falls möglich, geprüft werden können.
> Der überprüfte Teil des Systems hängt **nicht** von diesen Annahmen ab.

Jede Hypothese hat drei Felder: *Annahme* — *Motivation* — *Was prüfbar
werden müsste*.

### H1 — Fortbestand absorbierter Hexaphotonen

- **Annahme:** Ein absorbiertes Hexaphoton hört nicht vollständig auf zu
  existieren, sondern geht in einen derzeit nicht messbaren Zustand über.
- **Motivation:** Der Gedanke, dass in der Natur nichts „aus dem Nichts"
  verschwindet; Analogie zur Energieerhaltung.
- **Status / Gegenargument:** Der überprüfte Teil der Physik benötigt diese
  Annahme nicht — *Energie*-Erhaltung ist auch ohne sie vollständig erfüllt
  (Abschnitt 3.3, 5). Die *geordnete Information* des Lichts ist nach
  Absorption nachweislich nicht mehr auffindbar (zweiter Hauptsatz der
  Thermodynamik). Die Annahme ist daher nicht notwendig und derzeit nicht
  überprüfbar.
- **Was prüfbar werden müsste:** Ein Messverfahren, das einen wie auch immer
  gearteten „verborgenen Zustand" eines absorbierten Hexaphotons nachweisen
  oder ausschließen könnte. Solange ein solches Verfahren nicht existiert,
  bleibt H1 reine Spekulation.

### H2 — Identität emittierter Hexaphotonen

- **Annahme:** Bei der Emission (Abschnitt 4) könnten die ausgesandten
  Hexaphotonen mit zuvor absorbierten in einem tieferen Sinn „dieselben" sein.
- **Motivation:** Die Frage „woher kommen die neuen Hexaphotonen?"; Wunsch
  nach lückenloser Identitäts-Verfolgung.
- **Status / Gegenargument:** Photonen besitzen nach etablierter Physik **keine
  individuelle Identität** — zwei Hexaphotonen gleicher Frequenz, Polarisation
  und Richtung sind prinzipiell ununterscheidbar. Die Frage „dieselben?" ist
  daher nach heutigem Kenntnisstand nicht nur unbeantwortet, sondern
  möglicherweise nicht sinnvoll stellbar. Zudem zeigt das Glüh-Experiment
  (Abschnitt 4.3), dass emittierte Hexaphotonen die Eigenschaften der
  absorbierten **nicht** tragen.
- **Was prüfbar werden müsste:** Ein tragfähiger physikalischer Begriff von
  „Photon-Identität" überhaupt — und ein Experiment, das Identität über einen
  Absorptions-Emissions-Zyklus hinweg verfolgen könnte.

### H3 — Emission als Umordnung statt Neuerzeugung

- **Annahme:** Emission (Abschnitt 4) ist möglicherweise nicht die Erzeugung
  gänzlich neuer Hexaphotonen, sondern eine *Umordnung*: Zuvor absorbierte
  Hexaphotonen gehen durch erneute Energie-Einwirkung wieder in einen
  gerichteten, reisefähigen Zustand über, nehmen dabei neue Information auf
  und bewegen sich erneut mit Lichtgeschwindigkeit als Informationsträger
  durch Raum und Zeit.
- **Motivation:** Die Intuition, dass Absorption und Emission zwei Seiten
  desselben Vorgangs sein könnten; der Wunsch nach lückenloser
  Verfolgbarkeit des Informationsflusses, ohne einen „Bruch" bei der
  Absorption.
- **Status / Gegenargumente:** Diese Annahme steht in Konflikt mit zwei gut
  bestätigten Punkten der etablierten Physik:
  1. *Zweiter Hauptsatz der Thermodynamik.* Die in Abschnitt 3.3 beschriebene
     ungeordnete Wärme ordnet sich nicht von selbst wieder zu gerichtetem
     Licht zurück. Eine Formulierung wie „das Hexaphoton verlässt seine
     Entropie" beschreibt einen Vorgang, der dem zweiten Hauptsatz
     widerspricht — vergleichbar einer zerbrochenen Tasse, die von selbst
     wieder zusammenspringt.
  2. *Glüh-Experiment (Abschnitt 4.3).* Emittierte Hexaphotonen tragen die
     Eigenschaften der absorbierten nachweislich nicht.
  H3 müsste, um haltbar zu sein, beide Punkte auflösen. Solange das nicht
  geschehen ist, bleibt H3 reine Spekulation und **nicht** Bestandteil des
  überprüften Systems.
- **Was prüfbar werden müsste:** (a) Ein Nachweis, dass emittierte
  Hexaphotonen irgendeine messbare Spur zuvor absorbierter tragen. (b) Ein
  physikalischer Mechanismus, der erklärt, wie ein nicht-thermischer,
  geordneter Anteil die Absorption „überdauern" könnte, ohne dem zweiten
  Hauptsatz zu widersprechen — etwa über einen bislang unbekannten,
  nicht-thermischen Freiheitsgrad. Bis dahin ist H3 als offener Denkansatz
  zu verstehen, nicht als Mechanismus.


> **Hinweis des bearbeitenden Reviews:** H1, H2 und H3 sind als Denkanstöße
> dokumentiert, nicht als Bestandteil der Theorie. Sollten sie künftig in eine
> prüfbare Form gebracht werden, gehören sie in einen eigenen, klar von der
> klassischen Notation getrennten Theorie-Zweig.

---

## 10. Systemgrenze

Hexaphotone beschreibt Licht und seine Wechselwirkung mit Materie. **Was die
Materie nach der Absorption mit der aufgenommenen Wärme tut** — sich ausdehnen,
durch geringere Dichte aufsteigen (Auftrieb, Konvektion), schmelzen — liegt
**außerhalb** des Geltungsbereichs von Hexaphotone. Das ist Gegenstand der
Thermodynamik und der Strömungsmechanik. Hexaphotone endet bei „Energie ist
als Wärme im Material angekommen" und übergibt dort an andere Fachgebiete.

---

## 11. Verbleibende offene Punkte (für die nächsten Bausteine)

- **K5 (aus Baustein 2)** — Polarisationsvektor `ε⃗(Pᵢ)` konkret. Wird in
  Baustein 4 gebraucht.
- **K6 (aus Baustein 2)** — Amplituden-Konstante / Einheiten. Wird in
  Baustein 4 festgelegt.
- **K7 (aus Baustein 2)** — Übergang zur Modalbasis (sphärische Harmonische)
  für die Mie-Anbindung. In Baustein 4 zu klären.
- **K8** — Frequenzabhängigkeit von T_M: Parametrisierung über Brechungsindex
  und Absorptionsspektrum eines konkreten Materials. Für Baustein 4.

---

*Ende Baustein 3, Revision 2. Nächster Schritt: Baustein 4 — numerische
Validierung: ein konkretes Streuproblem (Kugel) in Hexaphotone-Notation
durchrechnen und gegen eine etablierte Mie-Bibliothek prüfen.*
