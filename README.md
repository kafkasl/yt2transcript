# YouTube Transcript Extractor

A simple tool to extract transcripts from YouTube videos in plain text or JSON format using the [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api).

## Installation

### Using Make

```bash
make install
```

### Using Just (Alternative)

If you prefer to use [Just](https://github.com/casey/just) as a command runner (simpler parameter passing):

```bash
# Install Just if not already installed
# On macOS:
brew install just

# On Linux:
# Follow instructions at https://github.com/casey/just#installation

# Then install dependencies
just install
```

## Usage

### Extract transcript as plain text

```bash
# Using make:
make transcript-txt ID=lRyGIzW9d9k

# Or using just (easier parameter passing):
just transcript-txt lRyGIzW9d9k

# Or directly:
./yt_transcript.py "lRyGIzW9d9k" -f txt -o output.txt
```

### Extract transcript as JSON

```bash
# Using make:
make transcript-json ID=lRyGIzW9d9k

# Or using just:
just transcript-json lRyGIzW9d9k

# Or directly:
./yt_transcript.py "lRyGIzW9d9k" -f json -o output.json
```

### Using custom language preferences

Just makes it easy to pass multiple parameters:

```bash
just transcript lRyGIzW9d9k json "es en"
```

This extracts the transcript in JSON format, preferring Spanish but falling back to English.

### Additional options

```
usage: yt_transcript.py [-h] [-o OUTPUT] [-f {txt,json}] [-l LANGUAGES [LANGUAGES ...]] video

YouTube transcript extractor

positional arguments:
  video                 YouTube video URL or ID

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file (default: video_id.txt)
  -f {txt,json}, --format {txt,json}
                        Output format (txt or json, default: txt)
  -l LANGUAGES [LANGUAGES ...], --languages LANGUAGES [LANGUAGES ...]
                        Preferred languages (default: en)
```

## Examples

Extract transcript in English:
```bash
./yt_transcript.py "https://www.youtube.com/watch?v=lRyGIzW9d9k" -l en
```

Extract transcript in Spanish, falling back to English if Spanish isn't available:
```bash
./yt_transcript.py "lRyGIzW9d9k" -l es en -f json
```

## Web Interface

This project now includes a web interface for extracting transcripts directly in your browser.

### Running the Web Server

```bash
# Using just:
just serve

# Or directly:
python main.py
```

The web server will start on http://localhost:8000. Open this URL in your browser to access the YouTube Transcript Extractor web interface.

### Features

- Simple form interface to enter YouTube URLs or video IDs
- Select output format (Text or JSON)
- Copy button for easy transcript copying
- Responsive design 