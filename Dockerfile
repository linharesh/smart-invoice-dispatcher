FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=src.server:app
ENV FLASK_ENV=production
EXPOSE 443
RUN chmod +x /app/start.sh
CMD ["/app/start.sh"]