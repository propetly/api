FROM python:3.12-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

WORKDIR /api

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY . .

RUN poetry run python manage.py migrate
RUN poetry run python manage.py collectstatic --noinput

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
