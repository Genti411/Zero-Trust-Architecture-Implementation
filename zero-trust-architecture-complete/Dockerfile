FROM python:3.10-slim
WORKDIR /app
COPY src/ /app
RUN pip install --no-cache-dir -r compliance-scanner/requirements.txt
CMD ["python", "compliance-scanner/scan.py"]
