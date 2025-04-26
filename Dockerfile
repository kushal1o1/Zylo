FROM python:latest

WORKDIR /zylo

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=Zylo.settings

EXPOSE 8000

CMD ["python", "manage.py","runserver", "0.0.0:8000"]