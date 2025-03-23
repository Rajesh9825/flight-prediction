# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /application

# Copy project files
COPY . /application

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 7860

# Run the application
CMD ["python", "application.py"]
