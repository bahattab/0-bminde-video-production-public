# Narration: audition, generation, acceptance

## Acceptance criteria

Listen to an actual generated excerpt containing a question, a longer explanatory sentence, and a transition. Check Arabic articulation and vowel reading, names and technical terms, pacing, sentence emphasis, pauses, and distracting synthesis artifacts. Ask for the user's choice when the sound they want is not yet established. A healthy MP3 or successful transcription does not prove professional delivery. Do not call a voice accepted merely because the user agreed to the general broadcast-style requirement.

Prepare spoken text separately from citations, scene directions and notes. The channel requirement is a fully vocalized Arabic narration script with a grammar and sentence-flow review, including correct tanween where required. Never sprinkle arbitrary vowels onto text or present unchecked automatic diacritization as a linguistic review. Check agreement, case endings, active/passive readings, word segmentation, pronunciation of names and intended sentence stops. Use punctuation to control natural phrasing. Spell numbers for speech when that avoids a misreading. The brand's trial spoken rendering is «بِي مَايْنْد» while its displayed name remains «بمايند | BMinde»; confirm the actual audio rather than claiming this spelling guarantees the intended reading. Correct the text or model settings before relying on audio effects to mask a poor voice. Re-audition materially changed settings or a replacement voice.

## Free neural route

`edge-tts` uses Microsoft's online Edge speech service; it is not local/offline synthesis. The script text is sent to that service. Do not send confidential scripts without appropriate authorization. Its availability and terms are separate from the open-source package license; package licensing alone does not prove output/publication rights. Do not promise unlimited availability or commercial permission based solely on a successful request.

Verified on 2026-10-15: the installed 7.2.7 client could list voices but synthesis returned HTTP 403; the official PyPI 7.3.1 package in an isolated `uv` environment produced valid Arabic neural samples. This is a dated compatibility observation, not a permanent version requirement. Use the current supported release and service documentation when rechecking failures. Do not forge credentials, disable TLS verification, or bypass a service restriction. Bound retries: inspect one failure, verify whether a supported client update addresses it, then retry once; if it still fails, report the restriction and use another legitimately available route.

Sources: [project](https://github.com/rany2/edge-tts), [official package](https://pypi.org/project/edge-tts/). Discover current voice IDs using the client's voice list; do not assume an old catalog remains available.

When the dependency is installed, run the portable helper:

```text
python scripts/synthesize.py --input script.txt --voice ar-SA-HamedNeural --output episode.mp3 --rate=-5%
```

For an isolated dependency environment where `uv` is already available:

```text
uv run --no-project --with edge-tts==7.3.1 python scripts/synthesize.py --input script.txt --voice ar-SA-HamedNeural --output episode.mp3 --rate=-5%
```

The example voice matches this profile's configured default; another channel may select a different voice. The helper never installs dependencies itself, never makes a paid request, never silently overwrites an existing file, and does not retry failed service calls. Use `--overwrite` only for an intended replacement. It writes a new MP3 through a temporary sibling file. Verify the final audio with an installed media tool.

## Post-production

Keep processing restrained. Match audition loudness for a fair comparison; the bundled samples were normalized toward -16 LUFS with -1.5 dBTP ceiling and 44.1 kHz output for online-video auditions. Those values are not a claim of compliance with any television station's delivery specification. Obtain a station's actual audio spec if that is the destination. Do not pitch-shift a weak robotic voice and describe the result as a broadcast narrator.

Record engine/version, voice ID, settings, script hash, generated-file path and actual duration. Keep a successful result rather than rerunning generation when a later status check fails. Full-series duration must be measured after the final accepted narration, not inferred from an audition or word count.

## Context-sensitive Arabic pronunciation

Resolve ambiguous Arabic words from the sentence's meaning before synthesis, rather than applying a fixed vowel pattern to an unvocalized spelling. For example, جُمَل means sentences and جَمَل means a camel; inflect endings for grammar and intended pauses. Do not confuse the singular جُمْلَة or the verb تُجَمِّل with either noun.

A synthesis engine can misread a word even when the written text contains الْجُمَلُ. Written diacritics are therefore insufficient evidence of correct output. For text-related contexts, compare a complete phrase such as جُمَلُ النَّصِّ with a meaning-preserving spoken rephrase such as عِبَارَاتُ النَّصِّ if necessary. Do not replace every occurrence globally or change an animal meaning into a text meaning. Preserve display wording separately when only spoken wording changes, and document the reason.

Audition the ambiguous word in its full intended sentence and verify the actual audio before accepting it or scaling narration. Rephrasing is a candidate remedy, not a guarantee. Apply the same contextual review to other homographs, active/passive forms, technical terms, and proper names. A clean decode, correct spelling, or transcription does not certify pronunciation. The contextual sample is the configured reference; use the current profile for that setting and keep per-episode pronunciation checks separate.


For the semantic review procedure and the current accepted-sample distinction, read [Arabic contextual narration review](arabic-context-review.md).
