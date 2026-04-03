# Multi-stage Dockerfile for Educational Game Suite
# Optimized for cross-platform desktop deployment

# Stage 1: Builder
FROM python:3.12-slim as builder

WORKDIR /app

# Install system dependencies for build
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# Stage 2: Runtime
FROM python:3.12-slim

WORKDIR /app

# Install runtime dependencies for Pygame/graphics
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    libportmidi0 \
    libsndio7 \
    libegl1-mesa \
    libgl1-mesa-glx \
    libxcb1 \
    libxkbcommon0 \
    xauth \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy Python packages from builder
COPY --from=builder /root/.local /root/.local

# Set PATH to use local Python packages
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd -m -u 1000 gameuser && \
    chown -R gameuser:gameuser /app

USER gameuser

# Allow X11 display forwarding
ENV SDL_VIDEODRIVER=x11
ENV DISPLAY=:0

# Expose any ports if needed (none for desktop app)
EXPOSE 5900

# Run the game
CMD ["python", "main.py"]
