FROM python:3.12-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml /app/

RUN pip install --no-cache-dir -r pyproject.toml

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]