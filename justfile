# YouTube Transcript Extractor commands

# Show help
default:
    @just --list

# Install required dependencies
install:
    pip install -r requirements.txt

# Extract transcript as text
transcript-txt VIDEO_ID:
    python yt_transcript.py "{{VIDEO_ID}}" -f txt -o "./transcripts/{{VIDEO_ID}}.txt"

# Extract transcript as JSON
transcript-json VIDEO_ID:
    python yt_transcript.py "{{VIDEO_ID}}" -f json -o "./transcripts/{{VIDEO_ID}}.json"

# Extract transcript with custom language preferences
transcript VIDEO_ID FORMAT="txt" LANGS="en":
    python yt_transcript.py "{{VIDEO_ID}}" -f {{FORMAT}} -l {{LANGS}} -o "{{VIDEO_ID}}.{{FORMAT}}"

# Start the web server
serve:
    python main.py 