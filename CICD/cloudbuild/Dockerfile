FROM ubuntu:latest

# Install dependencies
RUN apt update && apt install -y curl

# Copy application code
COPY . /app

# Run command when container launches
CMD ["bash", "-c", "echo 'Hello from Ubuntu!'"]
