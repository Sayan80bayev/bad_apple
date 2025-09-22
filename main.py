import cv2
import os
import time
import shutil
import sys

# ASCII brightness ramp
ASCII_CHARS = "%#*+=-:. "


def get_char_from_brightness(pixel_brightness):
    """Maps a pixel's brightness value (0-255) to an ASCII character."""
    char_count = len(ASCII_CHARS)
    step = 256 / char_count
    index = int(pixel_brightness / step)
    return ASCII_CHARS[min(index, char_count - 1)]


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller bundle.
    """
    if hasattr(sys, "_MEIPASS"):  # Running from a PyInstaller bundle
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def play_bad_apple(video_path, target_width=None, target_height=None):
    """Plays a video as ASCII art in the terminal, centered responsively, infinitely."""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file '{video_path}'.")
        return

    # Frame timing
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    delay_between_frames = 1 / frame_rate if frame_rate > 0 else 0.033

    # Get terminal size
    term_cols, term_rows = shutil.get_terminal_size(fallback=(120, 40))

    if target_width is not None:
        term_cols = target_width
    if target_height is not None:
        term_rows = target_height

    prev_gray = None

    try:
        while True:
            start_time = time.time()
            ret, frame = cap.read()

            if not ret:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                prev_gray = None
                continue

            h, w, _ = frame.shape
            aspect_ratio = w / h
            char_aspect_ratio = 2

            max_width, max_height = term_cols, term_rows
            scaled_height = int(max_width / (aspect_ratio * char_aspect_ratio))
            scaled_width = max_width

            if scaled_height > max_height:
                scaled_height = max_height
                scaled_width = int(scaled_height * aspect_ratio * char_aspect_ratio)

            resized_frame = cv2.resize(frame, (scaled_width, scaled_height))
            gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

            if prev_gray is not None:
                gray_frame = cv2.addWeighted(gray_frame, 0.7, prev_gray, 0.3, 0)
            prev_gray = gray_frame

            ascii_rows = [
                "".join(get_char_from_brightness(pixel) for pixel in row)
                for row in gray_frame
            ]

            pad_left = (term_cols - scaled_width) // 2
            ascii_rows = [(" " * pad_left) + line for line in ascii_rows]

            pad_top = (term_rows - scaled_height) // 2
            ascii_frame = ("\n" * pad_top) + "\n".join(ascii_rows)

            sys.stdout.write("\033[H" + ascii_frame)
            sys.stdout.flush()

            elapsed_time = time.time() - start_time
            if elapsed_time < delay_between_frames:
                time.sleep(delay_between_frames - elapsed_time)

    except KeyboardInterrupt:
        print("\nPlayback stopped by user.")
    finally:
        cap.release()


if __name__ == "__main__":
    # Use resource_path to work with PyInstaller bundle
    video_filename = resource_path("Touhou - Bad Apple.flv")
    play_bad_apple(video_filename)
