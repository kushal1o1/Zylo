FROM python:3.11-slim

WORKDIR /zylo

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=ZYLO.settings

# collect static files at build time
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "gunicorn ZYLO.wsgi:application --bind 0.0.0.0:$PORT"]
