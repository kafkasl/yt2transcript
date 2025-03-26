from fasthtml.common import *
from monsterui.all import *
from yt_transcript import get_formatted_transcript


# Add markdown support for copy functionality
hdrs = (Theme.blue.headers(), MarkdownJS(), HighlightJS())

# Create your app with the theme
app, rt = fast_app(hdrs=hdrs)

@app.post('/get_transcript')
def process_transcript(video_url: str, format: str = 'txt'):
    if not video_url:
        return P("Please enter a YouTube URL or video ID")
    
    try:
        transcript = get_formatted_transcript(video_url, format=format)
        # Wrap transcript in a markdown-enabled div
        return Div(f"```\n{transcript}\n```", cls='marked')
    except Exception as e:
        return P(f"Error retrieving transcript: {str(e)}")

@rt
def index():
    return Titled("YouTube Transcript Extractor",
        Card(
            P("Enter a YouTube URL or video ID below"),
            Form(
                Input(
                    type="text", 
                    name="video_url", 
                    placeholder="https://www.youtube.com/watch?v=...",
                    required=True
                ),
                Select(
                    Option("Text", value="txt", selected=True),
                    Option("JSON", value="json"),
                    name="format"
                ),
                Button("Get Transcript", type="submit"),
                hx_post="/get_transcript",
                hx_target="#transcript-result",
                hx_indicator="#spinner"
            ),
            Div(id="spinner"),
            Div(id="transcript-result")
        )
    )

serve()
