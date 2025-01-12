# Use the official Python image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file into container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Set environment variables (optional)
ENV FLASK_APP=app.py

# Run Flask app when the container starts
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

