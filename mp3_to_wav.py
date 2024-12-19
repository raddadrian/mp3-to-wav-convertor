from pydub import AudioSegment
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def convert_mp3_to_wav(input_mp3, output_wav):
    try:
        # Load the .mp3 file
        audio = AudioSegment.from_mp3(input_mp3)
        # Export the audio to .wav format
        audio.export(output_wav, format="wav")
        print(f"Converted {input_mp3} to {output_wav}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    Tk().withdraw()  # Prevents an empty tkinter window from appearing
    input_mp3 = askopenfilename(title="Select the .mp3 file", filetypes=[("MP3 files", "*.mp3")])
    
    if not input_mp3:
        print("No file selected. Please try again.")
    elif not os.path.isfile(input_mp3):
        print("The specified .mp3 file does not exist. Please try again.")
    else:
        output_wav = os.path.splitext(input_mp3)[0] + '.wav'
        convert_mp3_to_wav(input_mp3, output_wav)