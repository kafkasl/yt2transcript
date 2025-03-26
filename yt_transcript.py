#!/usr/bin/env python3

import argparse
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter, JSONFormatter

def extract_video_id(url_or_id):
    """Extract video ID from URL or return the ID if already in correct format."""
    if len(url_or_id) == 11: return url_or_id
    
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/v\/|youtube\.com\/watch\?.*v=)([^&\n?#]+)',
        r'youtube\.com\/shorts\/([^&\n?#]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match: return match.group(1)
    
    return url_or_id

def get_formatted_transcript(url_or_id, format='txt', languages=['en']):
    """Get transcript formatted as text or JSON."""
    video_id = extract_video_id(url_or_id)
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id, languages=languages)
    
    if format == 'json':
        formatter = JSONFormatter()
        return formatter.format_transcript(transcript, indent=2)
    else:
        formatter = TextFormatter()
        return formatter.format_transcript(transcript)

def main():
    parser = argparse.ArgumentParser(description='YouTube transcript extractor')
    parser.add_argument('video', help='YouTube video URL or ID')
    parser.add_argument('-o', '--output', help='Output file (default: video_id.txt)')
    parser.add_argument('-f', '--format', choices=['txt', 'json'], default='txt', 
                       help='Output format (txt or json, default: txt)')
    parser.add_argument('-l', '--languages', nargs='+', default=['en'], 
                       help='Preferred languages (default: en)')
    
    args = parser.parse_args()
    
    video_id = extract_video_id(args.video)
    output_file = args.output if args.output else f"{video_id}.{args.format}"
    
    print(f"Extracting transcript for video ID: {video_id}")
    
    try:
        # Get formatted transcript
        formatted_transcript = get_formatted_transcript(
            video_id, 
            format=args.format, 
            languages=args.languages
        )
        
        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_transcript)
        
        print(f"Transcript saved to {output_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 