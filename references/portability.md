# Installation and use by any agent

The entrypoint is `SKILL.md`, with standard YAML `name` and `description`. Human-readable Markdown instructions are sufficient for agents without a skills loader. Trigger keywords are **bminde**, **video**, **production** when used to invoke this channel workflow; the unambiguous invocation is `$bminde-video-production`.

## Host setup

- With a skill loader, copy/extract the entire `0 - bminde-video-production` folder into that host's configured skills directory. Keep `SKILL.md`, the profile, references, scripts and audition assets together. Use the host's normal refresh/reload or next-turn discovery; do not claim universal automatic discovery without a host check.
- Without a loader, tell the agent: “Read 0 - bminde-video-production/SKILL.md and use it for this BMinde video.” Supply the whole folder so relative links and assets remain accessible.
- For a searchable shared library, index the name, description and relative `SKILL.md` path. Do not overwrite a shared catalog after a partial inventory.
- `agents/openai.yaml` is optional OpenAI UI metadata. Other agents can ignore it; nothing in the production workflow depends on that file or on a particular MCP tool name.

## Required checks after installation

Read the installed `SKILL.md` and `channel-profile.json`. Resolve the references used for the current task. Confirm that the selected voice is Hamed and that fully vocalized, grammatically reviewed Arabic is required. Read the current profile for audition acceptance: the packaged contextual Hamed sample is the configured reference. Do not infer that every episode is accepted from this sample or a file-format test.

There is no API key, login, paid subscription, scheduled job, global environment change or automatic external publishing setup required by this skill. Do not create those merely because it is installed.

For script/editorial tasks, no additional software is required. For free neural synthesis using the optional helper, use Python 3.10 or later plus a working `edge-tts` dependency and network access to the provider. Follow `narration.md`; an isolated `uv` invocation is shown there when that tool is already available. The helper does not install software. Confirm a real short generated file and decode it before a large batch. For local media checks, use an available `ffprobe`/`ffmpeg` or equivalent media tool. For Remotion work, discover the actual project and installed version rather than hard-coding a workstation path.

Preserve user edits when updating an installed copy. Back up the prior version, validate the new source, compare known file hashes, then read back the installed files and portable archive. Leave unrelated skill folders and host settings intact.

The display and library folder name is `0 - bminde-video-production`. The machine identifier remains `bminde-video-production` for loader-compatible names and the existing `$bminde-video-production` invocation. A host that requires its directory to match the machine identifier may install the folder as `bminde-video-production` while retaining the display name.
