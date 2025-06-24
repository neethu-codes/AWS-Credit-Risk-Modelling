FROM python:3.9-slim

WORKDIR /app

COPY prediction_helper.py /app/
COPY requirements.txt /app/
COPY artifacts/ /app/artifacts/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "prediction_helper:app", "--host", "0.0.0.0", "--port", "8000"]
