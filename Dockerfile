FROM python:3.10-slim
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "api.py"]