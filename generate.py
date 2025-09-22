import cv2
import os
import sys
import shutil

# ASCII brightness ramp
ASCII_CHARS = "%#*+=-:. "

def get_char_from_brightness(pixel_brightness):
    """Map a pixel's brightness value (0-255) to an ASCII character."""
    char_count = len(ASCII_CHARS)
    step = 256 / char_count
    index = int(pixel_brightness / step)
    return ASCII_CHARS[min(index, char_count - 1)]

def generate_ascii_frames(video_path, output_dir="frames", target_width=240, target_height=80):
    """
    Convert a video into ASCII frames at higher resolution.
    Frames are saved as .txt files inside output_dir.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video file '{video_path}'.")
        return

    os.makedirs(output_dir, exist_ok=True)

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape
        aspect_ratio = w / h
        char_aspect_ratio = 2  # approximate width:height of monospace characters

        scaled_height = int(target_width / (aspect_ratio * char_aspect_ratio))
        scaled_width = target_width

        if scaled_height > target_height:
            scaled_height = target_height
            scaled_width = int(scaled_height * aspect_ratio * char_aspect_ratio)

        # Resize and convert to grayscale
        resized_frame = cv2.resize(frame, (scaled_width, scaled_height))
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

        # Convert to ASCII
        ascii_rows = [
            "".join(get_char_from_brightness(pixel) for pixel in row)
            for row in gray_frame
        ]
        ascii_frame = "\n".join(ascii_rows)

        # Save each frame
        with open(os.path.join(output_dir, f"frame_{frame_count:05d}.txt"), "w", encoding="utf-8") as f:
            f.write(ascii_frame)

        frame_count += 1
        if frame_count % 100 == 0:
            print(f"Saved {frame_count} frames...")

    cap.release()
    print(f"Done. {frame_count} frames saved to {output_dir}/")

if __name__ == "__main__":
    # Generate ASCII frames at high resolution (safe defaults: 240x80)
    generate_ascii_frames("Touhou - Bad Apple.flv", target_width=240, target_height=80)