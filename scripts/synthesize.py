"""Generate a single free neural narration with an installed edge-tts client."""
import argparse
import asyncio
import hashlib
import json
import logging
import os
from pathlib import Path
import shutil
import sys
import tempfile


async def synthesize() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--voice", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--rate", default="-5%")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    temporary: Path | None = None
    created_output = False
    try:
        text = args.input.read_text(encoding="utf-8-sig").strip()
        if not text:
            raise ValueError("Narration text is empty")
        if args.output.exists() and not args.overwrite:
            print(json.dumps({"success": False, "error": "Output already exists; choose a new path or explicitly allow replacement."}))
            return 2
        import edge_tts
        args.output.parent.mkdir(parents=True, exist_ok=True)
        handle, filename = tempfile.mkstemp(prefix="bminde-", suffix=".mp3", dir=args.output.parent)
        os.close(handle)
        temporary = Path(filename)
        await edge_tts.Communicate(text, args.voice, rate=args.rate).save(str(temporary))
        if temporary.stat().st_size < 1000:
            raise ValueError("No usable audio was returned")
        if args.overwrite:
            os.replace(temporary, args.output)
        else:
            # Exclusive creation also works on drives without hard-link support.
            with args.output.open("xb") as destination:
                created_output = True
                with temporary.open("rb") as source:
                    shutil.copyfileobj(source, destination)
            temporary.unlink()
            created_output = False
        temporary = None
        print(json.dumps({"success": True, "file": str(args.output.resolve()), "voice": args.voice, "rate": args.rate, "script_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(), "duration_verified": False}, ensure_ascii=False))
        return 0
    except Exception:
        logging.exception("BMinde speech synthesis failed")
        if created_output:
            args.output.unlink(missing_ok=True)
        print(json.dumps({"success": False, "error": "Speech generation failed. Check the installed dependency, service availability and output location before retrying."}))
        return 1
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    sys.exit(asyncio.run(synthesize()))
