# emtrades-destilado

Repo de destilación del método EMTrades. Leer CLAUDE.md primero.

## Arranque rápido
1. Volcar vídeos a 00_fuentes/videos, PDFs a 00_fuentes/pdfs, capturas a 00_fuentes/capturas
2. pip install faster-whisper (en WSL2 con CUDA) y sudo apt install ffmpeg
3. python scripts/transcribe.py 00_fuentes/videos
4. python scripts/extract_frames.py 00_fuentes/videos
5. Abrir Claude Code en la raiz del repo y pedirle: "procesa la siguiente fuente pendiente segun CLAUDE.md"
