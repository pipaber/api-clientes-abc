# Dockerfile
FROM python:3.9-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

COPY ./src /app/src

# Use uvicorn to run the ASGI app
EXPOSE 8000
CMD ["uvicorn", "src.api_clientes.main:app", "--host", "0.0.0.0", "--port", "8000"]

