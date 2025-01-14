FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY server.crt /app/server.crt
COPY server.key /app/server.key


ENV FLASK_APP=src.server:app
ENV FLASK_ENV=production

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]