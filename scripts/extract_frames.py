#!/usr/bin/env python3
"""
Extrae fotogramas de los vídeos en momentos donde el hablante señala algo
en pantalla (lenguaje deíctico), usando los .json de transcribe.py.

Uso:
    python extract_frames.py /ruta/a/videos [--transcripts ../10_transcripciones] [--out ../20_frames]

Por cada pasaje detectado guarda un frame en:
    20_frames/<video>/<HHMMSS>_<palabra_clave>.jpg
y un índice 20_frames/<video>/_index.md con timestamp + frase para que
Claude Code pueda revisar frame + contexto juntos.

Requiere ffmpeg en el PATH.
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".avi", ".webm"}

# Patrones de lenguaje deíctico / momentos visuales en formación de trading
PATTERNS = [
    r"\blook (at|here|how)\b", r"\bright here\b", r"\bover here\b",
    r"\bthis (candle|level|area|zone|gap|leg|move|run|swing|fractal|shelf|low|high|wick)\b",
    r"\bthese (candles|levels|areas|gaps|pockets|fractals)\b",
    r"\byou can see\b", r"\bas you see\b", r"\bnotice\b", r"\bsee how\b",
    r"\bright there\b", r"\bthat's (the|a) (gap|void|inefficienc|shelf|apex|base)\b",
    r"\bfor example\b", r"\bin this example\b", r"\bon the chart\b",
    r"\bI('m| am) (marking|drawing|highlighting)\b", r"\blet me (show|mark|draw)\b",
]
RX = re.compile("|".join(PATTERNS), re.IGNORECASE)

MIN_GAP_SECONDS = 20  # no extraer dos frames a menos de 20s (evita ráfagas)


def keyword_slug(text: str) -> str:
    m = RX.search(text)
    raw = m.group(0) if m else "visual"
    return re.sub(r"[^a-z0-9]+", "_", raw.lower()).strip("_")[:30]


def extract(video: Path, ts: float, out_jpg: Path):
    # +1.5s: el gesto/marca suele llegar justo después de la frase
    cmd = [
        "ffmpeg", "-loglevel", "error", "-ss", f"{ts + 1.5:.2f}",
        "-i", str(video), "-frames:v", "1", "-q:v", "3", "-y", str(out_jpg),
    ]
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("videos_dir", type=Path)
    ap.add_argument("--transcripts", type=Path,
                    default=Path(__file__).parent.parent / "10_transcripciones")
    ap.add_argument("--out", type=Path,
                    default=Path(__file__).parent.parent / "20_frames")
    args = ap.parse_args()

    videos = {p.stem: p for p in args.videos_dir.rglob("*")
              if p.suffix.lower() in VIDEO_EXTS}

    for jf in sorted(args.transcripts.glob("*.json")):
        data = json.loads(jf.read_text(encoding="utf-8"))
        stem = jf.stem
        video = videos.get(stem)
        if not video:
            print(f"[salto] no encuentro el vídeo de {stem}")
            continue

        vout = args.out / stem
        vout.mkdir(parents=True, exist_ok=True)
        index_lines = [f"# Frames: {stem}\n"]
        last_ts = -1e9
        count = 0

        for seg in data["segments"]:
            if not RX.search(seg["text"]):
                continue
            if seg["start"] - last_ts < MIN_GAP_SECONDS:
                continue
            ts = seg["start"]
            hhmmss = f"{int(ts//3600):02d}{int(ts%3600//60):02d}{int(ts%60):02d}"
            jpg = vout / f"{hhmmss}_{keyword_slug(seg['text'])}.jpg"
            if not jpg.exists():
                try:
                    extract(video, ts, jpg)
                except subprocess.CalledProcessError as e:
                    print(f"  error extrayendo {jpg.name}: {e}")
                    continue
            index_lines.append(f"- **{hhmmss[:2]}:{hhmmss[2:4]}:{hhmmss[4:]}** "
                               f"`{jpg.name}` — \"{seg['text'].strip()}\"")
            last_ts = ts
            count += 1

        (vout / "_index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")
        print(f"{stem}: {count} frames")


if __name__ == "__main__":
    main()
