FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install TensorFlow and other dependencies
RUN pip install --no-cache-dir tensorflow
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install tf-keras

# Copy your application files
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Command to run your application
CMD ["python", "main.py"]