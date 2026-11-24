# FoF 26: TSE Stand, Crew-Visualisierung

Eine einzige Datei (`index.html`), keine Abhängigkeiten, läuft offline und auf GitHub Pages.

## Auf GitHub Pages stellen

1. Auf github.com ein neues Repository anlegen (Add file, Upload files) und `index.html` und `.nojekyll` hochladen.
2. Settings, Pages, Source: "Deploy from a branch", Branch `main`, Folder `/ (root)`, Save.
3. Nach ein bis zwei Minuten steht die Seite unter `https://<benutzer>.github.io/<repo>/`.

Hinweis: Im kostenlosen GitHub-Tarif muss das Repository für Pages öffentlich sein. Die Seite ist dann für jeden mit dem Link erreichbar.

## Aktualisieren

Neue `index.html` über die alte hochladen (gleicher Dateiname). Pages baut automatisch neu.

## Stand

Visualisierung zur Orientierung, keine Werkplanung. Verbindlich sind die Pläne aus dem Briefing.

## Pausenslide Green Stage (`/pause/`)

Animierter Loop für die Regie der Green Stage: https://7deeda.github.io/fof26-stand/pause/

- Im Browser (Chrome/Edge) öffnen, **F** für Vollbild.
- Leertaste: Pause/weiter. Pfeil rechts/links (auch Bild auf/ab, Clicker): nächste/vorherige Folie.
- **Auto-Update:** Die Seite prüft alle 20 s, ob eine neue Fassung auf GitHub liegt, und lädt sie am Ende des laufenden Durchgangs neu. Nach einem Commit dauert es ca. 1 bis 2 Minuten (GitHub-Pages-Deploy), dann ist die Änderung in der Regie. Im Pause-Modus wird nicht neu geladen.
- Texte ändern: `pause/index.html` auf github.com mit dem Stift bearbeiten und committen (z. B. nach `Aus Berlin.` suchen).
- Foto tauschen: Datei in `pause/assets/` mit **gleichem Namen** hochladen und danach in `pause/index.html` die Zahl hinter `?v=` überall ändern (sonst kann der Browser bis zu 10 Minuten das alte Bild zeigen).
