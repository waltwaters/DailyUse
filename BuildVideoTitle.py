import os
import subprocess
from tkinter import Tk, filedialog


# Function to call a file dialog to select videos
def select_videos():
    root = Tk()
    root.withdraw()  # Hide the main tkinter window
    root.attributes('-topmost', True)  # Bring the dialog to the front

    # Open file dialog and allow selection of multiple files
    video_files = filedialog.askopenfilenames(
        title="Select Videos",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv")],
    )

    return list(video_files)


# Function to update the media title using ffmpeg
def update_media_title(video_files):
    for video_path in video_files:
        # Extract filename without the extension
        filename = os.path.basename(video_path)
        file_name, file_extension = os.path.splitext(filename)

        # Prepare ffmpeg command to change the metadata title
        command = [
            'ffmpeg',
            '-i', video_path,  # input file
            '-metadata', f"title={file_name}",  # update title to match filename
            '-codec', 'copy',  # copy the rest of the codecs to avoid re-encoding
            f"{os.path.splitext(video_path)[0]}_updated{file_extension}"  # output new file
        ]

        # Execute the ffmpeg command
        try:
            subprocess.run(command, check=True)
            print(f"Updated title for: {filename}")
        except subprocess.CalledProcessError as e:
            print(f"Error updating {filename}: {e}")


# Main program logic
if __name__ == "__main__":
    # Call the file dialog to let user select video files
    selected_videos = select_videos()

    if selected_videos:
        # Update the media title to match the filename
        update_media_title(selected_videos)
    else:
        print("No videos selected.")

