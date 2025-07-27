# Выкачиваем из dockerhub образ с python версии 3.9
FROM python:3.9

# # Устанавливаем рабочую директорию для проекта в контейнере
# WORKDIR /backend

# # Скачиваем/обновляем необходимые библиотеки для проекта 
# COPY requirements.txt /backend
# RUN pip3 install --upgrade pip -r requirements.txt

# # Копируем содержимое папки, где находится Dockerfile, в рабочую директорию контейнера
# COPY . /backend


WORKDIR /workspace
COPY backend/requirements.txt /workspace/backend/
RUN pip3 install --upgrade pip -r backend/requirements.txt
COPY . /workspace

# Устанавливаем порт, который будет использоваться для сервера
EXPOSE 5000