FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


ENV FLASK_APP=src.server:app
ENV FLASK_ENV=production

# Expose port 433
EXPOSE 443

# Run the Flask app
CMD ["gunicorn", "src.server:app", "--bind", "0.0.0.0:443", "--certfile=ssl.crt", "--keyfile=ssl.key"]
