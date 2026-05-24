# Mathematische Ergänzungen zur Hexaphoton‑Theorie

## 1 Übersicht
Dieses Dokument liefert die **formalen Definitionen**, eine **präzisierte Abbildung** des Hexaphoton‑Vektors auf elektromagnetische Feldgrößen, den **Operator‑/Übertragungsformalismus** und eine **konkrete Verbindung zur Mie/T‑Matrix‑Theorie**. Ziel ist, die Theorie prüfbar zu machen und ein reproduzierbares Notebook‑Skelett für numerische Vergleiche bereitzustellen.

---

## 2 Formale Definitionen und Notation

**Hexaphoton (Informationsvektor)**  
\[
\mathbf{H} = \bigl(E,\; f,\; \Pi,\; \phi,\; \vec{p},\; \vec{d}\bigr)
\]
wobei \(E\) Energie, \(f\) Frequenz, \(\Pi\) Polarisation, \(\phi\) Phase, \(\vec p\) Impuls und \(\vec d\) Richtung sind.

**Lichtfeld als Modenüberlagerung**  
In einer geeigneten orthonormalen Modenbasis \(\{u_k(\mathbf r)\}\):
\[
L(\mathbf r,t)=\sum_{k} a_k(t)\,u_k(\mathbf r)
\]
Die komplexen Koeffizienten \(a_k(t)\) kodieren Amplitude, Phase und Polarisationsinformation.

**Fourier‑Darstellung**  
Für räumliche Frequenzen \(\mathbf k\):
\[
\tilde L(\mathbf k,t)=\mathcal{F}\{L(\mathbf r,t)\}(\mathbf k)
\]

---

## 3 Operatorformalismus und Materialantwort

**Allgemeiner Wechselwirkungsoperator**  
Materielle Wechselwirkung wird als linearer Operator \(T_M\) auf dem Modenraum modelliert:
\[
L_{\text{out}} = T_M\bigl[L_{\text{in}}\bigr]
\]
In Fourierraumdarstellung:
\[
\tilde L_{\text{out}}(\mathbf k) = H_M(\mathbf k)\,\tilde L_{\text{in}}(\mathbf k)
\]
wobei \(H_M(\mathbf k)\) die Übertragungsfunktion des Materials/Objekts ist.

**Messung als Projektion**  
Messwerte \(I_j\) sind Projektionen auf Messmoden \(\{m_j\}\):
\[
I_j = \langle m_j,\, L_{\text{out}}\rangle = \int m_j^*(\mathbf r)\,L_{\text{out}}(\mathbf r)\,\mathrm d^3r
\]

**Reflexion / Transmission**  
Für undurchsichtige Objekte modelliert man primär Reflexionsoperatoren \(T_{\text{refl}}\); für transparente Kugeln Transmission + Streuung \(T_{\text{trans}}\).

---

## 4 Verbindung zur Mie / T‑Matrix Theorie

**Mie‑Koeffizienten**  
Für eine homogene Kugel liefert die Mie‑Theorie Streu‑ und Transmissionskoeffizienten \(a_n(f), b_n(f)\) (abhängig von Größe und Brechungsindex). Das gestreute Feld lässt sich als Summe sphärischer Harmonischer schreiben; im Fernfeld ergibt sich eine Winkelverteilung \(S(\theta,\phi;f)\).

**Übertragungsfunktion \(H_M(\mathbf k)\) aus Mie**  
Für eine planare Abbildung in Winkelraum (Paraxialapproximation) kann man die Mie‑Antwort auf eine effektive Übertragungsfunktion \(H_{\text{mie}}(\mathbf k;f)\) mappen. Formal:
\[
H_{\text{mie}}(\mathbf k;f)\approx \sum_{n} \alpha_n(f)\,Y_n(\hat{\mathbf k})
\]
wobei \(\alpha_n\) aus \(a_n,b_n\) konstruiert werden und \(Y_n\) geeignete Winkelmoden sind. Für numerische Vergleiche genügt es, die Winkelabhängigkeit des gestreuten Feldes aus Mie zu berechnen und als diskrete Samples von \(H_M(\mathbf k)\) zu verwenden.

**Praktische Vorgehensweise**
- Berechne mit einer Mie‑Bibliothek die gestreute Feldverteilung für gegebene Frequenzen \(f\) und Kugelparameter.  
- Transformiere die Winkelverteilung in räumliche Frequenzen \(\mathbf k\) (Paraxial‑Mapping).  
- Verwende diese diskrete \(H_M(\mathbf k)\) als Referenz‑Operator für Vergleiche mit dem Hexaphoton‑Modell.

---

## 5 Mapping Hexaphoton → Moden (Vorschlag)

**Allgemeine Abbildung**  
Definiere für jede Mode \(k\) eine Abbildungsfunktion \(\mathcal{F}_k\):
\[
a_k(\mathbf H)=\mathcal{F}_k\bigl(E,f,\Pi,\phi,\vec p,\vec d\bigr)
\]
**Konstruktionsprinzipien für \(\mathcal{F}_k\)**  
- **Energie / Amplitude:** \(E\) skaliert die Gesamtenergie: \(\sum_k |a_k|^2 \propto E\).  
- **Frequenz:** \(f\) wählt die spektrale Gewichtung \(S(f)\) der Moden.  
- **Polarisation:** \(\Pi\) bestimmt die Polarisationskomponenten in den Vektor‑Moden.  
- **Phase:** \(\phi\) setzt globale/relative Phasen der \(a_k\).  
- **Impuls / Richtung:** \(\vec p,\vec d\) verschieben die Modenverteilung im \(\mathbf k\)‑Raum (Doppler/Steering).

**Beispiel‑Ansatz (praktisch)**  
Wähle eine Gauß‑ähnliche Verteilung im \(\mathbf k\)‑Raum zentriert bei \(\vec k_0\) (aus \(\vec d\) und \(\vec p\)):
\[
a(\mathbf k;\mathbf H) = A(E,f)\;P(\Pi)\;\exp\!\bigl(-\tfrac{|\mathbf k-\mathbf k_0(\vec p,\vec d)|^2}{2\sigma(f)^2}\bigr)\;e^{i\phi}
\]
Diskretisiere \(a(\mathbf k)\) auf die Modenbasis \(u_k\) durch Projektion:
\[
a_k(\mathbf H)=\int u_k^*(\mathbf k)\,a(\mathbf k;\mathbf H)\,\mathrm d^2k
\]

---

## 6 Numerische Implementierung — Notebook Skeleton & Anforderungen

**Ziel:** reproduzierbarer Vergleich
