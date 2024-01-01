FROM python:3.11-slim
# set work directory
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

WORKDIR /usr/src/app

# copy project
COPY . .

COPY Pipfile.lock Pipfile ./
RUN pip install -U pip setuptools pipenv && pipenv install

# run app
CMD ["python", "server.py"]