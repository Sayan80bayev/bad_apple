import os
import sys
import time
import shutil

def scale_frame(frame_lines, max_cols, max_rows):
    """Rescale ASCII frame to fit inside terminal (max_cols × max_rows)."""
    from math import floor

    frame_height = len(frame_lines)
    frame_width = max(len(line) for line in frame_lines) if frame_lines else 1

    # scale ratios
    scale_x = frame_width / max_cols if frame_width > max_cols else 1
    scale_y = frame_height / max_rows if frame_height > max_rows else 1
    scale = max(scale_x, scale_y)

    if scale <= 1:
        return frame_lines  # fits already

    new_width = floor(frame_width / scale)
    new_height = floor(frame_height / scale)

    # resample using nearest-neighbor
    scaled = []
    for y in range(new_height):
        src_y = int(y * scale)
        row = frame_lines[src_y]
        new_row = "".join(row[int(x * scale)] for x in range(new_width))
        scaled.append(new_row)
    return scaled


def play_ascii_frames(frame_dir="frames", fps=30):
    """Play pre-generated ASCII frames from text files, scaled & centered in the terminal."""
    frame_files = sorted(f for f in os.listdir(frame_dir) if f.endswith(".txt"))
    if not frame_files:
        print("No ASCII frames found in", frame_dir)
        return

    delay = 1 / fps

    try:
        while True:  # loop infinitely
            term_cols, term_rows = shutil.get_terminal_size(fallback=(120, 40))

            for frame_file in frame_files:
                with open(os.path.join(frame_dir, frame_file), "r", encoding="utf-8") as f:
                    ascii_frame = f.read()

                frame_lines = ascii_frame.split("\n")

                # scale frame to fit terminal
                frame_lines = scale_frame(frame_lines, term_cols, term_rows)

                frame_height = len(frame_lines)
                frame_width = max(len(line) for line in frame_lines) if frame_lines else 0

                # center horizontally
                pad_left = max((term_cols - frame_width) // 2, 0)
                centered_lines = [(" " * pad_left) + line for line in frame_lines]

                # center vertically
                pad_top = max((term_rows - frame_height) // 2, 0)
                centered_frame = ("\n" * pad_top) + "\n".join(centered_lines)

                sys.stdout.write("\033[H" + centered_frame)
                sys.stdout.flush()

                time.sleep(delay)
    except KeyboardInterrupt:
        print("\nPlayback stopped by user.")


if __name__ == "__main__":
    play_ascii_frames("frames", fps=30)