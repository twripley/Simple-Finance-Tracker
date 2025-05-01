# Use the official Python base image
FROM python:3.13-bullseye

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY ../app.py /app
COPY ../config.py /app
COPY ../models.py /app

# Install dependencies
RUN pip install --no-cache-dir -r ../requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variable to avoid bytecode files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the Flask app environment variable (optional)
ENV FLASK_APP=app.py

# Start the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
