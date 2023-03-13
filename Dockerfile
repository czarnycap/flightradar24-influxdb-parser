# Use the official Python image as the base image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY app.py .

# Start the Python script when the container starts
CMD ["python3", "app.py"]

