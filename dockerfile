# Use a specific version of Python
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app

# Install dependencies
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/ || exit 1

# Command to run the application
CMD ["flask", "run"]
