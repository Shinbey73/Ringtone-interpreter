# Ringtone-interpreterMamba Number Py — RTTTL Ringtone Interpreter 🎵

A Python tool that reads RTTTL ringtone strings, validates and edits them, and exports a browser player to preview the tunes. Includes an interactive CLI and unit tests. 

Features
- RTTTL parsing & validation for title, defaults (d,o,b), and notes with unit tests for note correctness and ringtone assembly. 
- Interactive CLI: choose which songs to keep, adjust speed (note length), and shift octaves before export. 
- Robust input handling across multiple RTTTL files, including malformed lines. 
- HTML player generation powered by WebAudio + WebAudioFont and bundled soundfont assets for playback. 

What is RTTTL?
- RTTTL (Ring Tone Text Transfer Language) is a compact text format (e.g., name:d=4,o=5,b=100:8c,8d,8e,...) used on early phones to represent melodies. This project reads those strings and makes them playable on modern browsers.
