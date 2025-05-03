# Use the official Python base image
FROM python:3.13-bullseye

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY *.py /app
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variable to avoid bytecode files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the Flask app environment variable (optional)
ENV FLASK_APP=app.py

# Start the Gunicorn App
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
