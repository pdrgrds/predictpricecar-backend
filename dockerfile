FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libpq-dev \
    git \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=2.1.2
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false && \
    poetry install --no-root

RUN poetry add gunicorn

COPY . /app/

EXPOSE 8000

# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
CMD ["poetry", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]
