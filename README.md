# Pitch & Pizza Timer

Countdown für Beamer oder Laptop mit lautem Alarm bei 0:00. Läuft komplett offline und nur auf diesem Rechner.

## Starten

Voraussetzung ist Python 3.

- **macOS/Linux:** `./start.sh`
- **Windows:** `start.bat` doppelklicken

Der Browser öffnet sich auf `http://127.0.0.1:8765/`. Der Server lauscht nur auf 127.0.0.1 und ist im WLAN nicht erreichbar. Beenden mit `Strg+C`.

Ist Port 8765 belegt, weicht der Server auf den nächsten freien Port bis 8775 aus. Einstellungen werden pro Port gespeichert.

## Tastenkürzel

| Taste | Funktion |
| --- | --- |
| Leertaste | Start / Pause / Fortsetzen |
| R | Reset |
| F | Vollbild an/aus |
| P | Pizza-Modus an/aus |
| Beliebige Taste oder Klick | Alarm stoppen, danach steht der Timer wieder auf der Ausgangszeit |

Im Vollbild beendet Escape den Alarm und zusätzlich das Vollbild, das erzwingt der Browser. Mit jeder anderen Taste bleibt das Vollbild an.

## Vor dem Event prüfen

1. Unter „Einstellungen“ den Alarmton wählen und mit „Test“ anhören.
2. Die Lautstärke des Rechners hochdrehen und das richtige Ausgabegerät (HDMI/Beamer) wählen. Der Browser kann beides nicht selbst einstellen.
3. Nicht stummschalten: Der Alarmton läuft über die normale Systemausgabe.

## Hinweise

- Der Alarm flackert rot/weiß mit 2,5 Wechseln pro Sekunde und bleibt damit unter der 3-Hz-Grenze für Fotosensibilität. Trotzdem kurz ansagen, falls jemand empfindlich reagiert.
- Der Bildschirm bleibt über die Wake Lock API wach, mit einem stummen Mini-Video als Fallback. Unter macOS hält `start.sh` ihn zusätzlich mit `caffeinate` wach.
- Der Alarm kommt auch pünktlich, wenn der Tab verdeckt ist. Dafür muss einmal „Start“ gedrückt worden sein, was den Ton freischaltet.
