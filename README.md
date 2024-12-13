# **YouTube Video Downloader & MP3 Extractor**  
A simple Python script to download YouTube videos and automatically convert the audio into MP3 format. Perfect for quickly extracting audio tracks from videos.  
---
#### **Features**:
- Downloads YouTube videos in the highest available quality.  
- Extracts audio and saves it as an MP3 file with customizable quality.  
- Automatically saves audio files to a specified directory.  
- Accepts YouTube URLs via user input.  

#### **Technologies Used**:
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp): For video downloading.  
- [`FFmpeg`](https://ffmpeg.org/): For audio extraction and conversion.  

#### **Requirements**:
- Python 3.7 or higher.  
- `yt-dlp` and `FFmpeg` installed on your system.  

#### **Installation**:
1. Clone this repository:  
   ```bash
   git clone <your-repository-URL>
   ```  
2. Install the required dependencies:  
   ```bash
   pip install yt-dlp
   ```  
3. Ensure FFmpeg is installed ([Guide](https://ffmpeg.org/download.html)).  

#### **Usage**:
Run the script and provide the YouTube video URL and the output directory:  
```bash
python downloader.py
```  

#### **Contributions**:
Feel free to suggest improvements or report issues via pull requests or the issues section.  
