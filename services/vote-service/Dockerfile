FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gcc \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*


RUN useradd -m -u 1000 appuser

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN chown -R appuser:appuser /app

USER appuser

ENTRYPOINT ["/entrypoint.sh"]
CMD ["uvicorn", "cmd.server.main:app", "--host", "0.0.0.0", "--port", "8000"]
