# Call-Analysis-AI
# Setting up Faster Whisper for Speech-to-Text

## 1. Update and Install Dependencies
Run the following command to update your system and install the required dependencies:
```bash
apt update && apt upgrade -y
apt install -y python3 python3-pip ffmpeg wget git
```

## 2. Create a Virtual Environment (Optional but Recommended)
To maintain a clean working environment, use `venv` to create a virtual environment:
```bash
python3 -m venv whisper_env
source whisper_env/bin/activate
```

## 3. Install Faster Whisper
Install the `faster-whisper` package:
```bash
pip install faster-whisper
```

## 4. Download the Whisper Model
The model is downloaded automatically when first used, but you can preload it:
```bash
python3 -c "from faster_whisper import WhisperModel; model = WhisperModel('small')"
```

## 6. Run Whisper to Transcribe Audio to Text
Use the following Python script to transcribe the audio file and save the extracted text:

```python
from faster_whisper import WhisperModel

# Load the model
model = WhisperModel("small")

# Define the audio file path
audio_file = "/home/recordings/test.wav"

# Perform transcription (en -ar .............
segments, _ = model.transcribe(audio_file, language="en")

# Save the text output
output_file = "/home/recordings/transcribed_test.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for segment in segments:
        line = f"{segment.start:.2f}s - {segment.end:.2f}s: {segment.text}\n"
        f.write(line)

print(f"Transcription saved to: {output_file}")
```

## 7. Verify the Transcription Output
To check the transcribed text, run:
```bash
cat /home/recordings/transcribed_test.txt
or
tail -f /home/recordings/transcribed_test.txt
```


