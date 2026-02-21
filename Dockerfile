# Use a lightweight Python image
FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 10000


WORKDIR /app

# Install system dependencies for some python packages if needed (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download NLTK data
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"

# Copy project files
COPY . .

# Expose the port Render expects
EXPOSE 10000

# Run the application
CMD uvicorn app.main:app --host 0.0.0.0 --port 10000
