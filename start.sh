#!/bin/sh

# Start the Gunicorn server in the background
gunicorn src.server:app \
  --bind 0.0.0.0:443 \
  --certfile=ssl.crt \
  --keyfile=ssl.key \
  --access-logfile - \
  --error-logfile - \
  --log-level info \
  --preload &

# Start the Python script in the background
python create_invoice_job.py &

# Wait for both processes to finish
wait