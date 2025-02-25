from faster_whisper import WhisperModel

# تحميل النموذج
model = WhisperModel("tiny", device="cpu", compute_type="int8", num_workers=4)

# مسار الملف الصوتي
audio_file = "/home/recordings/test.mp3"

# تنفيذ التحويل
segments, _ = model.transcribe(audio_file, language="en")

# حفظ النص في ملف
output_file = "/home/recordings/test.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for segment in segments:
        f.write(f"{segment.start:.2f}s - {segment.end:.2f}s: {segment.text}\n")

print(f"✅ تم حفظ النص في: {output_file}")

