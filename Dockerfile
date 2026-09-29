# Use official lightweight Python runtime
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency specifications first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose port 5000 for web traffic
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]
