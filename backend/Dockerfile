# ------------------------- BUILDER ---------------------------------------
FROM python:3.10-slim AS builder

WORKDIR /usr/src/app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# ------------------------- TEST RUNNER ------------------------------------
FROM python:3.10-slim AS test_runner

WORKDIR /tmp

COPY --from=builder /venv /venv
COPY --from=builder /usr/src/app /app

ENV PATH="/venv/bin:$PATH"
ENV PYTHONPATH=/app/src

RUN pip install --no-cache-dir pytest

RUN pytest /app/tests

# ------------------------- SERVICE LAYER ----------------------------------
FROM python:3.10-slim AS service

WORKDIR /app

COPY --from=builder /venv /venv
COPY --from=builder /usr/src/app /app

ENV PATH="/venv/bin:$PATH"
ENV PYTHONPATH=/app/src

CMD ["uvicorn", "openapi_server.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
