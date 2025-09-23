FROM python:3.11-slim

# Install deps
RUN apt-get update && apt-get install -y portaudio19-dev python3-dev build-essential ffmpeg && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.enableCORS=false"]