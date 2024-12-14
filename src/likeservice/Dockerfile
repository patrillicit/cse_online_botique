# Base image with Python runtime
FROM python:3.12.6-slim@sha256:ad48727987b259854d52241fac3bc633574364867b8e20aec305e6e7f4028b26 AS base

# Builder stage to install dependencies
FROM base AS builder

# Install build dependencies
RUN apt-get -qq update \
    && apt-get install -y --no-install-recommends \
        wget g++ \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Runtime stage
FROM base

# Enable unbuffered logging for better Docker logs
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /likeservice

# Grab packages from builder
COPY --from=builder /usr/local/lib/python3.12/ /usr/local/lib/python3.12/


# Add the application
COPY . .


# Expose the application port
ENV PORT=8080
EXPOSE 8080

# Run the application
CMD ["python", "server.py"]
