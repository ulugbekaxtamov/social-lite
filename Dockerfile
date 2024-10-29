FROM python:3.10-buster

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# Collect static files, apply migrations, and start server
CMD python manage.py collectstatic --noinput && \
    python manage.py migrate && \
    gunicorn --bind 0.0.0.0:8000 --workers 2 config.wsgi
