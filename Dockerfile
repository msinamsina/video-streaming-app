# Use the official Python 3.12 image as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
COPY ./src /app/

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Install ffmpeg for video processing
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "-m", "manage.py", "runserver"]
