#!/usr/bin/env python3
"""
Transcripción por lotes de vídeos EMTrades con faster-whisper.
Adaptado a GPU con 4GB VRAM (RTX 2050): distil-large-v3 en int8_float16,
fallback automático a medium.en, y a CPU si no hay CUDA.

Uso:
    python transcribe.py /ruta/a/videos [--model distil-large-v3] [--out ../10_transcripciones]

- Reanudable: si el .json de un vídeo ya existe, lo salta.
- Salidas por vídeo: <nombre>.md (legible, timestamps), <nombre>.srt, <nombre>.json
- Procesa .mp4 y .mov (añade extensiones en VIDEO_EXTS si hace falta).

Instalación (WSL2 con CUDA):
    pip install faster-whisper
    sudo apt install ffmpeg
"""
import argparse
import gc
import json
import sys
from pathlib import Path

VIDEO_EXTS = {".mp4", ".mov", ".mkv", ".avi", ".webm", ".wav", ".m4a", ".mp3"}

# Prompt inicial: sesga el decodificador hacia la jerga del método
INITIAL_PROMPT = (
    "Trading education about GBPUSD price action and liquidity: price inefficiency, "
    "liquidity gap, liquidity void, rebalance, fade, bids, offers, fractal, price run, "
    "price swing, price spike, shelf, apex, midflow, low liquidity state, LLS, CPS, SWE, "
    "cable, pips, order book, liquidity providers, dealers, efficient price delivery."
)


def fmt_ts(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")


def fmt_ts_md(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def load_model(name: str):
    from faster_whisper import WhisperModel

    attempts = [
        (name, "cuda", "int8_float16"),
        ("medium.en", "cuda", "int8_float16"),
        (name, "cpu", "int8"),
    ]
    last_err = None
    for model_name, device, compute in attempts:
        try:
            print(f"[modelo] intentando {model_name} en {device} ({compute})...")
            m = WhisperModel(model_name, device=device, compute_type=compute)
            print(f"[modelo] cargado: {model_name} / {device}")
            return m, model_name
        except Exception as e:  # VRAM insuficiente, sin CUDA, etc.
            print(f"[modelo] fallo con {model_name}/{device}: {e}")
            last_err = e
    raise RuntimeError(f"No se pudo cargar ningún modelo: {last_err}")


def transcribe_one(model, video: Path, outdir: Path):
    md_path = outdir / f"{video.stem}.md"
    srt_path = outdir / f"{video.stem}.srt"
    json_path = outdir / f"{video.stem}.json"

    segments_iter, info = model.transcribe(
        str(video),
        language="en",
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 700},
        initial_prompt=INITIAL_PROMPT,
        beam_size=5,
        condition_on_previous_text=False,  # evita bucles de repetición en vídeos largos
    )

    segments = []
    with open(md_path, "w", encoding="utf-8") as md, open(
        srt_path, "w", encoding="utf-8"
    ) as srt:
        md.write(f"# Transcripción: {video.name}\n\n")
        md.write(f"Duración: {info.duration:.0f}s — idioma detectado: {info.language} "
                 f"(p={info.language_probability:.2f})\n\n")
        for i, seg in enumerate(segments_iter, start=1):
            text = seg.text.strip()
            segments.append({"start": seg.start, "end": seg.end, "text": text})
            md.write(f"**[{fmt_ts_md(seg.start)}]** {text}\n\n")
            srt.write(f"{i}\n{fmt_ts(seg.start)} --> {fmt_ts(seg.end)}\n{text}\n\n")
            # progreso en consola cada ~2 min de vídeo
            if i % 40 == 0:
                print(f"    ... {fmt_ts_md(seg.start)} / {fmt_ts_md(info.duration)}")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(
            {"file": video.name, "duration": info.duration, "segments": segments},
            f, ensure_ascii=False, indent=1,
        )
    return len(segments), info.duration


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("videos_dir", type=Path)
    ap.add_argument("--model", default="distil-large-v3")
    ap.add_argument("--out", type=Path, default=Path(__file__).parent.parent / "10_transcripciones")
    ap.add_argument("--limit", type=int, default=0, help="max videos por tanda (0 = todos)")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    videos = sorted(
        p for p in args.videos_dir.rglob("*") if p.suffix.lower() in VIDEO_EXTS
    )
    if not videos:
        sys.exit(f"No hay vídeos en {args.videos_dir}")

    pending = [v for v in videos if not (args.out / f"{v.stem}.json").exists()]
    if args.limit > 0:
        pending = pending[:args.limit]
    print(f"{len(videos)} vídeos encontrados, {len(pending)} pendientes.")
    if not pending:
        return

    model, model_name = load_model(args.model)
    total_audio = 0.0
    for n, video in enumerate(pending, 1):
        print(f"\n[{n}/{len(pending)}] {video.name}")
        try:
            nseg, dur = transcribe_one(model, video, args.out)
            total_audio += dur
            print(f"    OK — {nseg} segmentos, {dur/60:.1f} min")
        except Exception as e:
            print(f"    ERROR en {video.name}: {e} — continúo con el siguiente")
        gc.collect()

    print(f"\nHecho. {total_audio/3600:.1f}h de audio transcritas con {model_name}.")
    print(f"Salidas en: {args.out}")


if __name__ == "__main__":
    main()
