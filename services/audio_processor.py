from pydub import AudioSegment
from pydub.silence import detect_nonsilent


def remove_silence(
    input_file,
    output_file,
    silence_thresh=-40,
    min_silence_len=700,
    padding=300,
    crossfade_duration=100,
    fade_duration=50,
):
    try:
        audio = AudioSegment.from_file(input_file, format="mp3")

        # Detect non-silent parts of the audo.
        # Returns a list of [start, end] pairs ofr each detected non-silent part.
        nonsilent_ranges = detect_nonsilent(
            audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh
        )

        # Return false if no meaningful audio is found.
        if not nonsilent_ranges:
            return False, "No audio content found."

        processed_audio = AudioSegment.empty()

        for i, (start, end) in enumerate(nonsilent_ranges):
            # Add padding before and after the chunk for smoothness.
            chunk = audio[max(0, start - padding) : min(len(audio), end + padding)]
            # Apply fade-in and fade-out to soften the chunk.
            chunk = chunk.fade_in(fade_duration).fade_out(fade_duration)

            if i == 0:
                processed_audio = chunk
            else:
                processed_audio = processed_audio.append(
                    chunk, crossfade=crossfade_duration
                )

        processed_audio.export(output_file, format="mp3")
        return True, "Audio processed successfully."

    except Exception as e:
        return False, f"Processing error: {str(e)}"
