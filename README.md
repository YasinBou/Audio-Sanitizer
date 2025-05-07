# Audio Sanitizer

**Audio Sanitizer** is a simple tool designed to clean up audio files by removing silent sections, making sure the final output maintains smooth transitions between non-silent sections. The tool intelligently handles fade-ins and fade-outs, preventing the audio from sounding too choppy when silence is removed. Whether you're working with podcasts, lectures, or regular audio files, this tool helps optimize your audio content for a more polished listening experience.

> **Note**: This tool is currently in the early stages of development. It is optimized for **.mp3** files and is only supported on **Windows** at this time.

---

## Features

- **Silence Removal**: Detects and removes silent sections from your audio file.
- **Smooth Transitions**: Ensures that the removal of silent sections doesn’t create jarring or abrupt cuts. Crossfades and fades are applied to maintain smooth audio flow.
- **Customization Options**: Adjust the silence detection threshold, minimum silence length, and fade durations to suit your needs.
- **File Management**: Automatically generates unique filenames to avoid overwriting existing files and allows you to save the processed audio in a designated output folder.

---

## Requirements

This project includes a `requirements.txt` file, which contains all necessary dependencies. To install the required libraries, simply run:

```bash
pip install -r requirements.txt
