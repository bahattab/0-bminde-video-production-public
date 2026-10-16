# BMinde production and verification

## Portable workflow

1. Read the current channel profile and the user's requested topic, duration, deliverables and audience. Discover the actual workspace, editor and available runtime; do not assume paths from an earlier machine.
2. Create or recover a task-specific production register. For a batch, track every required episode independently and preserve the full requested count through interruptions.
3. Research the episode's material claims, write original narration, an original example/application, an evidence note and a scene plan. Mark incomplete verification honestly.
4. Establish the broadcast-style voice through an actual accepted audition. Keep paid spending within the user's stated authorization; work on other production tasks if the voice decision is pending.
5. Generate the complete narration, verify it decodes, and measure its duration. Use phrase/paragraph timing or alignment for the storyboard. Avoid recycling one scene or one script across a large batch.
6. Author the visual story. Each scene should demonstrate the mechanism or worked example, rather than display a wall of narration. Keep diagrams readable, Arabic direction correct, labels within the frame, and scientific comparisons faithful to their evidence.
7. Inspect representative frames, transitions and narrative synchronization; check the whole final file for decode errors and duration. For speech quality, listen to actual audio, especially beginnings, endings, technical terms and joins.
8. Deliver actual files with a clear episode index and scientific references. State completion per episode; do not mark a batch complete while any required video remains missing or unverified.

## Remotion route

Use the relevant installed Remotion skill/docs for the project's actual version. Keep Remotion packages on one compatible version. Open Studio before composition edits where supported. If the in-app browser is unavailable, keep Studio running and provide the real preview URL; do not claim the browser preview was inspected.

Keep each independently editable composition/scene/sequence as its own authored JSX node and reusable named scene component. Register scene components as connected compositions where useful. Use frame-driven animation, `useVideoConfig().fps` for seconds-to-frames conversions and supported premount props. Use complete, explicitly typed props with safe missing-data behavior. Do not render a caption as precisely synchronized unless actual timings support it.

Do not automatically render 100 videos concurrently on a shared workstation. Use a measured pilot and bounded queues. If cold browser rendering fails on a constrained Windows host, `--gl=swangle --concurrency=1` was a previously verified fallback, but re-check the current runtime rather than assuming it is always necessary. A slow live job is a wait, not proof of failure; inspect the same process/job before deciding to restart it. Temporary pre-encode files are not deliverable MP4s.

Typical installed-tool checks:

```text
ffprobe -v error -show_streams -show_format -of json episode.mp4
ffmpeg -v error -i episode.mp4 -f null -
```

Confirm expected dimensions, audio/video streams, actual requested duration, and full decode. For the current 3–5 minute series, check 180–300 seconds individually for every final file. Do not use estimated script length or a build-success message to pass this gate.

## Publishing when requested

The distributed profile retains only the channel name. Obtain and verify the intended channel identity from the owner before any publishing action. Explicitly verify the selected account/channel before uploads; multiple connected accounts may exist. Publication defaults from an earlier task do not authorize a new external action by themselves. Preserve existing videos unless the user requests a change.

After upload, record the video ID immediately so an uncertain follow-up cannot cause duplicate uploads. Independently verify the destination channel, requested visibility, processed upload and successful media processing. A generated watch URL does not establish publication. Retain an accurate status record and useful visual proof. Do not report the batch as published until every requested episode passes that check.
