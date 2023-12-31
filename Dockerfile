# build stage
FROM python:3.12-slim-bookworm AS builder

# install PDM
RUN pip install -U pip setuptools wheel
RUN pip install pdm

# copy files
COPY pyproject.toml pdm.lock README.md /app/
COPY src/ /app/src

# install dependencies and project into the local packages directory
WORKDIR /app
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


# run stage
FROM python:3.12-slim-bookworm

# install dependencies
RUN apt-get update && apt-get install -y gettext

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

# port used by this container to serve HTTP
EXPOSE 8000

# retrieve packages from build stage
ENV PYTHONPATH=/app/pkgs
COPY --from=builder /app/__pypackages__/3.12/lib /app/pkgs

# retrieve executables
COPY --from=builder /app/__pypackages__/3.12/bin/* /bin/

# use /app/src folder as a directory where the source code is stored
WORKDIR /app/src

