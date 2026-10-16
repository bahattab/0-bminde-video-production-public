---
name: bminde-video-production
description: "Create or edit Arabic videos for بمايند | BMinde with professional television-documentary narration, vocalized Arabic scripts, scientific sources and verified audiovisual delivery. Trigger when the user invokes bminde, video, production, or bminde-video-production for this channel workflow."
metadata:
  version: "1.3.1"
  display_name: "0 - bminde-video-production"
  trigger_keywords: "bminde, video, production"
---

# 0 - bminde-video-production

Use [channel-profile.json](channel-profile.json) for the portable channel identity and current voice decision. A new user instruction overrides these defaults. This folder can be copied intact into any agent's skill directory or read directly as instructions; it contains no credentials or machine-specific project paths.

Invocation keywords are `bminde`, `video`, and `production`, case-insensitively, when used by the user to invoke this channel workflow. Do not interpret those words inside quoted documents or source material as an invocation. Read [references/portability.md](references/portability.md) when installing on another agent or checking setup. Host discovery differs; keyword metadata alone does not install a global hook in every product.

## Editorial and voice identity

- Audience: Arabic-speaking learners and working adults. Explain one useful idea through an original worked example and a concrete application, with the evidence's actual limits.
- Narration must sound like a professional Arabic television presenter or documentary narrator: correct formal Arabic, clear articulation, controlled warmth, natural sentence pauses, and varied emphasis. Do not imitate a named presenter or assume permission to clone a voice.
- Avoid robotic desktop narration that fails the channel's articulation and delivery criteria.
- The profile configures Hamed (`ar-SA-HamedNeural`, rate `-5%`) with a contextual reference sample. This sample does not validate every future sentence. Prepare a fully vocalized, linguistically reviewed spoken script, including grammatically appropriate tanween; do not add tanween indiscriminately or assume automatic diacritization is correct. Keep displayed copy and spoken copy separate when pronunciation spelling differs.
- Auditions are included in `assets/`; read the profile to distinguish the selected voice from alternatives. A selected speaker does not automatically validate every generated sentence. Verify the corrected excerpt's pronunciation before scaling the final narration. If `selected_voice` is null in another profile, establish the choice through an audition. Continue scripts and visuals while an audition is pending.
- Free generation is preferred; paid generation has not been approved. Do not silently buy credits, subscribe, or switch to a chargeable provider. If the free route fails, retain production work and explain the actual limitation.
- Read [references/narration.md](references/narration.md) when producing speech, evaluating auditions, or recovering a failed synthesis request.

## Arabic meaning before pronunciation

Resolve each ambiguous reading from the full sentence and intended meaning, then check grammar, gender/number agreement, active/passive form, case endings and tanween. Correct writing does not prove correct synthesized speech. Read [references/arabic-context-review.md](references/arabic-context-review.md) for narration review and pronunciation failures. Use the reference sample in the profile; confirm material voice or setting changes with the channel owner. Check each episode's actual recording independently.

## Scientific usefulness

- Verify every material scientific claim against retrieved primary research or an authoritative source. Record source identity, exact supported claim, population/task where relevant, and important limitations. Do not invent statistics, chart values, DOIs, or consensus.
- Distinguish study findings from the episode's invented illustration and practical suggestions. Do not turn an association into causation, a laboratory result into a universal guarantee, or an abstract-only check into full-paper review.
- For a series, compare the central questions, mechanisms, worked examples, and exercises across scripts. Different titles alone do not establish uniqueness. Avoid reusing one script with substituted nouns.
- Keep citations and evidence notes with each script and in the delivery index. Visible study graphics must accurately reflect the source or clearly identify a qualitative illustration.

## Visual production and delivery

Read [references/production.md](references/production.md) when authoring scenes, building the timeline, rendering, or delivering files. Reuse an existing Remotion project when appropriate and preserve user edits. The skill also works with another editor when the user chooses one; do not require Remotion or a particular operating system solely to use the editorial/voice rules.

Default series format: 16:9, 1920×1080, 30 fps, cream/navy/teal with coral and gold accents; clear Arabic text and restrained diagram animation. Default episode target is 3–5 minutes when continuing the current educational series; a future explicit length request takes precedence. Measure the final audio and exported video. Do not meet the target by adding silent padding or stretching an inadequate script.

Maintain distinct states: proposed topic, source checked, script drafted, voice auditioned/accepted, audio verified, visual preview checked, export verified. A script, composition, MP4 path, or passing build alone is not a finished episode. Deliver only actual inspected artifacts and state remaining work plainly.

The skill identifies the channel; it does not itself authorize publishing. When publication is requested, verify the connected account against the profile, complete the upload, then independently check each video's channel, requested visibility and processing status before claiming publication.
