# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install dependencies with increased timeout and retries
RUN pip install --no-cache-dir -r requirements.txt --default-timeout=1000 --retries=3

# Copy the entire project directory to the container
COPY . .

# Command to run the pipeline script
CMD ["python", "pipeline.py"]