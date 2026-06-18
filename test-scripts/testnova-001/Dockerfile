FROM mcr.microsoft.com/playwright/python:v1.60.0-jammy

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p screenshots

ENV SCREENSHOT_DIR=screenshots

# Provide BASE_URL, TEST_USERNAME, and TEST_PASSWORD at runtime:
#   docker run --rm --env-file .env <image>
CMD ["pytest", "-v"]
