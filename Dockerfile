# Dockerfile that creates an image for a Python application:
# Start with a base image
FROM python:3.8-slim-buster

## Set the working directory
RUN apt update -y && apt install awscli -y
WORKDIR /app

# Copy the application code
COPY . /app

# Install application dependencies
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# Specify the default command to run the application
CMD ["python3", "app.py"]