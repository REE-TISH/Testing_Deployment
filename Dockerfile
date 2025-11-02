# Use an official lightweight Python image
FROM python:3.12-slim

# Set environment variables to prevent Python from writing .pyc files and buffering output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app


# Copy dependency files first (for caching)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose port 8000 for Django
EXPOSE 8000

# Command to run the Django server
CMD ["gunicorn", "comicBackend.wsgi:application", "--bind", "0.0.0.0:8000"]
