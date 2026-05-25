# Baustein 3 — Der Materie-Operator T_M (Version 4.2)

## 3.1 Zweck des Operators

Der Operator **T_M** beschreibt, wie Materie die Eigenschaften eines
Hexaphotons verändert. Er ist **keine neue Physik**, sondern eine
**kompakte Notation** für etablierte klassische Transformationen:
Brechung, Reflexion, Streuung, Polarisationsänderung, Absorption.

T_M fasst Jones-, Mueller-, Fresnel- und Snellius-Formalismen in einer
einheitlichen Schreibweise zusammen.

> **T_M ist kein Speicher.** Es ist eine reine Durchgangs-Vorschrift —
> Welle rein, veränderte Welle raus. Die „Form" eines streuenden Objekts
> steckt darin, *wie* T_M die Richtungen umlenkt, nicht in einem
> gespeicherten Bild.

---

## 3.2 Definition des Operators

Ein Hexaphoton ist \( H = (f, P, d) \). Der Materie-Operator wirkt:

\[
T_M(H) = (f', P', d')
\]

mit \( f' = f \) (lineare Optik), \( P' = M_P\,P \) (Polarisationsmatrix),
\( d' = M_d\,d \) (Richtungsänderung).

---

## 3.3 Die drei Wirkungen auf einfallendes Licht

Jedes reale T_M ist eine Mischung dreier Grundwirkungen.

### Umlenken — das Hexaphoton existiert weiter
Reflexion und Brechung ändern die Richtung \( d \); Frequenz und
Polarisation bleiben erhalten (ggf. geordnet transformiert).
Information bleibt erhalten.
Beispiele: Snellius-Brechung, Fresnel-Reflexion, Mie-/Rayleigh-Streuung.

### Auswählen — ein Teil kommt durch, ein Teil nicht
Blenden, Spalte und Aperturen lassen nur einen Teil der einfallenden
Hexaphotonen passieren; der Rest wird geblockt. Dies ist eine **Auswahl**
des Hexafelds — der Mechanismus hinter Beugung am Spalt und der Lochkamera.

> Der Spalt-Effekt ist klassische Wellenoptik (funktioniert auch mit
> Schallwellen). Er ist **nicht** der quantenmechanische Messprozess.

### Absorbieren — Energie geht über, Lichtordnung löst sich auf
Das Hexaphoton wird vom Material aufgenommen; seine Energie geht in die
ungeordnete Wärmebewegung der Atome über. Die Energie bleibt erhalten —
die geordnete Lichtstruktur (Richtung, Polarisation, Phase, scharfe
Frequenz) ist danach im Material nicht mehr auffindbar.

---

## 3.4 Absorption — formale Beschreibung

Absorption wird durch einen Dämpfungsfaktor \( \alpha \in [0,1] \)
beschrieben:

\[
T_M(H) = \alpha \cdot (f, P', d')
\]

- \( \alpha = 1 \): keine Absorption
- \( \alpha = 0 \): vollständige Absorption
- \( 0 < \alpha < 1 \): partielle Absorption

Der Dämpfungsfaktor \( \alpha \) hängt vom Material und von der Frequenz
ab — ein Objekt kann für eine Farbe durchsichtig, für eine andere
undurchsichtig sein. Diese Frequenzabhängigkeit ist der Grund, warum
Materialien Farben haben.

---

## 3.5 Emission — zwei Arten

Emission ist **nicht** durch T_M beschrieben; sie erzeugt ein neues
Hexaphoton:

\[
\emptyset \;\longrightarrow\; H_{\text{emit}} = (f_{\text{emit}}, P_{\text{emit}}, d_{\text{emit}})
\]

Es gibt **zwei physikalisch verschiedene** Emissionsarten:

**Wärmestrahlung (Glühen) — temperaturbestimmt.** Jeder warme Körper
sendet Licht aus, weil er warm ist. Die Farbverteilung hängt **allein von
der Temperatur** ab, nicht vom Material (Plancksches Strahlungsgesetz):
~800 °C rot, ~1200 °C gelborange, ~1500 °C fast weiß. Ein breites,
kontinuierliches Spektrum.

**Spektrallinien — materialbestimmt.** Emission bei scharfen,
materialspezifischen Frequenzen (Natrium gelb, Neon rotorange). Die
Frequenzen entsprechen dem Absorptionsmuster desselben Materials — zwei
Seiten desselben charakteristischen Frequenzmusters.

> Emittierte Hexaphotonen sind **neue** Hexaphotonen. Ihre Eigenschaften
> bestimmt die Temperatur bzw. die Atomart — nicht zuvor absorbierte
> Hexaphotonen. Die spekulative Gegenposition ist in der
> Hypothesen-Sammlung (H2, H3) getrennt dokumentiert.

---

## 3.6 Energiebilanz

\[
E_{\text{ein}} = E_{\text{umgelenkt}} + E_{\text{durchgelassen}} + E_{\text{absorbiert}}
\]

Die absorbierte Energie ist als Wärme im Material — nicht verschwunden.
Verschwunden (aufgelöst) ist nur die *geordnete Information* des
absorbierten Anteils.

---

## 3.7 Nichtlineare Erweiterungen (optional)

Für spätere Arbeiten kann ein erweiterter Operator **T\*_M** definiert
werden:

\[
T^*_M(H) = (f + \Delta f,\; P',\; d')
\]

Er beschreibt Raman- und Brillouin-Streuung, Erzeugung neuer Frequenzen
(SHG, THG), Kerr-Effekt, intensitätsabhängige Brechung. T\*_M ist
**nicht Bestandteil** des Kernsystems.

---

## 3.8 Systemgrenze

Was die Materie nach der Absorption mit der Wärme tut — sich ausdehnen,
durch geringere Dichte aufsteigen (Konvektion), schmelzen — liegt
**außerhalb** von Hexaphotone. Das ist Thermodynamik und
Strömungsmechanik. Hexaphotone endet bei „Energie ist als Wärme im
Material angekommen".

---

## 3.9 Entkopplung von spekulativen Hypothesen

Spekulative Ideen aus der Hypothesen-Sammlung (H1–H7, z. B. Fortbestand
absorbierter Photonen, innere Rotation, Wärme als gespeicherte Photonen)
werden **nicht** durch T_M beschrieben. Der Operator bildet ausschließlich
klassische, experimentell bestätigte Transformationen ab.

---

## 3.10 Zusammenfassung

Der Operator T_M:

- ist eine kompakte Notation klassischer Optik
- erhält die Frequenz (lineare Optik)
- verändert Polarisation und Richtung
- wirkt dreifach: umlenken, auswählen, absorbieren
- beschreibt Absorption über einen Dämpfungsfaktor
- erzeugt **keine** neuen Photonen (Emission ist ein separater Vorgang)
- ist vollständig kompatibel mit Maxwell-Optik
- bleibt frei von spekulativen Annahmen

Optionale Erweiterungen (T\*_M) ermöglichen nichtlineare Effekte, ohne
den Kern zu verändern.
