# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
# COPY requirements.txt .

# Install the project dependencies
RUN pip install opencv-python face_recognition

# Copy the entire project to the container
COPY . .

# Set the command to run your Python script
CMD ["python", "play.py"]