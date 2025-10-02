FROM python:3.9
WORKDIR /app
COPY backend/requirements.txt backend/requirements.txt
RUN pip3 install --no-cache-dir -r backend/requirements.txt
COPY . .
EXPOSE 5000