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
CMD ["flask", "run", "--host=0.0.0.0:443"]