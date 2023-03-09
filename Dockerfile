FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

WORKDIR /app

RUN apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

COPY ./ ./

RUN pip install -r ./requirements/requirementsdev.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=core.settings.dev"]