FROM python:3.7-alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir pipenv

COPY . .

RUN pipenv sync --dev

CMD [ "pipenv", "run", "gunicorn", "--bind=0.0.0.0", "run:quote" ]
