import argparse
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import yt_dlp

# YouTube Upload Function
def upload_video(file_path, title, description, category="22", privacy_status="public"):
    """Uploads a video to YouTube."""
    try:
        # Define the scopes required for uploading
        scopes = ["https://www.googleapis.com/auth/youtube.upload"]

        # Use the OAuth flow to authenticate
        flow = InstalledAppFlow.from_client_secrets_file('secrets.json', scopes)
        credentials = flow.run_local_server(port=0)

        # Build the YouTube API client
        youtube = build('youtube', 'v3', credentials=credentials)

        # Prepare the metadata for the video
        body = {
            "snippet": {
                "title": title,
                "description": description,
                "categoryId": category
            },
            "status": {
                "privacyStatus": privacy_status
            }
        }

        # Upload the video file
        media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
        request = youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media
        )

        # Execute the request and get the response
        response = request.execute()
        print(f"Video uploaded successfully! Video ID: {response['id']}")

    except Exception as e:
        print(f"An error occurred during upload: {e}")


# YouTube Download Function
def download_video(url, output_path="."):
    """Downloads a video from YouTube in the best possible quality."""
    try:
        # Set options for best video and audio
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Best video and audio
            'merge_output_format': 'mp4',         # Output format (merged into MP4)
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save with title as filename
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',         # Ensure final output is MP4
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Video downloaded successfully in the best quality!")
    except Exception as e:
        print(f"An error occurred during download: {e}")

# Command-Line Interface
def main():
    parser = argparse.ArgumentParser(description="YouTube Upload and Download Tool")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    # Upload command
    upload_parser = subparsers.add_parser("upload", help="Upload a video to YouTube")
    upload_parser.add_argument("file", type=str, help="Path to the video file")
    upload_parser.add_argument("title", type=str, help="Title of the video")
    upload_parser.add_argument("description", type=str, help="Description of the video")
    upload_parser.add_argument("--category", type=str, default="22", help="Category ID (default: 22)")
    upload_parser.add_argument("--privacy", type=str, default="public", help="Privacy status (default: public)")

    # Download command
    download_parser = subparsers.add_parser("download", help="Download a video from YouTube")
    download_parser.add_argument("url", type=str, help="YouTube video URL")
    download_parser.add_argument("--output", type=str, default=".",
                                 help="Output directory (default: current directory)")

    args = parser.parse_args()

    if args.command == "upload":
        upload_video(args.file, args.title, args.description, args.category, args.privacy)
    elif args.command == "download":
        download_video(args.url, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
