# mp3-to-wav-convertor
Personal project that converts downloaded .mp3 audio file formats to .wav audio file formats

As a house and techno music enthusiast, I enjoy mixing tracks in my free time. High-quality, uncompressed audio is essential for achieving the best mixing experience. While there are online tools for converting .mp3 to .wav, they often come with limitations, such as restricted free usage. This project addresses that need by providing a simple and efficient way to convert audio formats locally.

How to Use (Tested on macOS):
1. Download the script.
2. Prepare your files: Create a directory containing the .mp3 audio files you want to convert to .wav.
3. Open a terminal: Navigate to the directory where you downloaded the script.
4. Run the script: Type python3 mp3_to_wav.py and press Enter.
5. Select the file: Finder will open—navigate to the directory containing your .mp3 files, select one file, and confirm. The script will convert it to .wav.

Current Limitations:
- Only one file can be converted per execution of the script.
- The original .mp3 file remains in the directory and must be deleted manually.

Future Plans:
- Add support for batch file selection.
- Implement automatic deletion of the original .mp3 files after conversion.
