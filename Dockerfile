FROM alpine:latest

RUN apk --no-cache add \
    python3 \
    py3-pip \
    python3-dev \
    build-base \
    git \
    curl

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY . /app

RUN poetry install

CMD ["poetry", "run", "python", "app.py"]
