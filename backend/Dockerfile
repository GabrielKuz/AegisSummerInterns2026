FROM python:3.14.0-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

RUN groupadd --system app \
    && useradd --system --gid app --home /app app \
    && pip install --no-cache-dir uv \
    && chown app:app /app

COPY --chown=app:app pyproject.toml uv.lock ./

USER app
RUN uv sync --frozen --no-dev

COPY --chown=app:app . .

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers"]