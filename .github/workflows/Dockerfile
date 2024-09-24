# Use a base image with Python 3.10
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /app

# Copy the Poetry files
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install --upgrade pip && \
    pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the project files
COPY . .

# Set the command to run your application
CMD ["poetry", "run", "python", "main.py"]