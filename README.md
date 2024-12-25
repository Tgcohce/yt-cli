
# YouTube CLI Tool

This is a Python-based command-line interface (CLI) tool that allows users to **upload** and **download** YouTube videos. The tool uses the YouTube Data API for uploading videos and `yt-dlp` for downloading.

---

## Features
- **Upload Videos**: Upload videos to your YouTube channel with metadata (title, description, privacy status, etc.).
- **Download Videos**: Download YouTube videos in the best possible quality.

---

## Prerequisites
### 1. **Python**
Make sure you have Python 3.7 or later installed. You can download Python [here](https://www.python.org/downloads/).

### 2. **FFmpeg**
FFmpeg is required for downloading videos with the best quality (audio and video merged). Install FFmpeg as follows:

- **Windows**:
  1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).
  2. Extract the archive and copy the path to the `bin` folder (e.g., `C:\ffmpeg-master-latest-win64-gpl\bin`).
  3. Add the path to the system's PATH environment variable.

- **Linux/macOS**:
  ```bash
  sudo apt install ffmpeg      # Linux
  brew install ffmpeg          # macOS
  ```

### 3. **Google API Setup**
To use the upload functionality, you need to set up the **YouTube Data API v3** on Google Cloud Console. Follow these steps:

#### **Step 1: Create a Google Cloud Project**
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Log in with your Google account.
3. Click on **New Project** at the top.
4. Give your project a name (e.g., `YouTube CLI Tool`) and click **Create**.

#### **Step 2: Enable the YouTube Data API v3**
1. In the Google Cloud Console, select your project.
2. Go to **APIs & Services > Library**.
3. Search for **YouTube Data API v3** and click on it.
4. Click **Enable**.

#### **Step 3: Create OAuth 2.0 Credentials**
1. Go to **APIs & Services > Credentials**.
2. Click **Create Credentials** and select **OAuth Client ID**.
3. Configure the consent screen:
   - Click on **Configure Consent Screen**.
   - Choose **External** and click **Create**.
   - Fill in the **App Name** (e.g., `YouTube CLI Tool`) and your email address.
   - Click **Save and Continue**.
4. Create the OAuth Client:
   - Select **Desktop App** as the application type.
   - Click **Create** and download the `secrets.json` file.
   - Place the `secrets.json` file in the same directory as `yt_tool.py`.

#### **Step 4: Test the API**
The tool will prompt you to authenticate during the first upload. Follow the on-screen instructions to complete authentication.

---

## Installation
1. Clone the repository or download the code:
   ```bash
   git clone https://github.com/your-repo/yt-cli-tool.git
   cd yt-cli-tool
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### 1. **Upload Videos**
To upload a video to YouTube, run:
```bash
python yt_tool.py upload "path/to/video.mp4" "Video Title" "Video Description" --category CATEGORY_ID --privacy PRIVACY_STATUS
```

#### Example:
```bash
python yt_tool.py upload "C:/Videos/my_first_video.mp4" "My First Video" "This is a description" --category 22 --privacy public
```

#### Authentication:
The first time you upload a video, you'll be prompted to authenticate:
1. A browser window will open.
2. Log in with your Google account and grant the required permissions.
3. The upload will proceed after successful authentication.

---

### 2. **Download Videos**
To download a YouTube video, run:
```bash
python yt_tool.py download "YOUTUBE_VIDEO_URL" --output "OUTPUT_DIRECTORY"
```

#### Example:
```bash
python yt_tool.py download "https://www.youtube.com/watch?v=example" --output "./downloads"
```

The tool downloads the video in the **best possible quality** (audio and video merged).

---

## File Structure
```plaintext
yt-cli-tool/
├── yt_tool.py            # Main CLI tool
├── secrets.json   # Google API credentials
├── requirements.txt      # Required Python libraries
├── downloads/            # Default folder for downloads (optional)
```

---

## Dependencies
- `google-auth`
- `google-auth-oauthlib`
- `google-auth-httplib2`
- `google-api-python-client`
- `yt-dlp`
- `ffmpeg` (external dependency)

---

## Troubleshooting
1. **Error: `HTTP Error 403: Forbidden` (Downloading)**:
   - Update `yt-dlp`:
     ```bash
     pip install --upgrade yt-dlp
     ```

2. **Error: `HTTP Error 400: Bad Request` (Uploading)**:
   - Ensure your `client_secrets.json` file is correctly set up.
   - Use the latest version of `google-auth-oauthlib`.

3. **FFmpeg Not Found**:
   - Ensure FFmpeg is installed and added to your PATH.

---

## Acknowledgment
This tool was developed for my internship. Feel free to use or contribute to the project to improve its functionality.

