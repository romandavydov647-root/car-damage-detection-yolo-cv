# 🚗 Car Damage Detection (CV Pet-Project)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-yellow)

## 📌 О проекте
Этот проект решает задачу **автоматической детекции повреждений автомобилей** с помощью компьютерного зрения. Задача максимально приближена к реальным бизнес-процессам в страховании (автоматическая модерация страховых случаев, оценка ущерба).

**Цель:** Разработать end-to-end пайплайн от «сырых» данных (COCO JSON) до готовой модели, способной находить и классифицировать дефекты на фотографиях.

## 🛠 Стек технологий
*   **Язык:** Python
*   **Deep Learning:** PyTorch, YOLOv8 (Ultralytics)
*   **Работа с данными:** JSON, OpenCV, NumPy
*   **Инструменты:** Google Colab, Git

## 📊 Данные и подготовка
В проекте использовался академический датасет **CarDD (Car Damage Detection)**.
*   **Проблема:** Изначально данные были в формате COCO JSON (сложная структура, координаты в пикселях).
*   **Решение:** Был написан **собственный конвертер** (`convert_coco_to_yolo.py`), который:
    *   Читает JSON-файлы.
    *   Пересчитывает координаты `[x_min, y_min, width, height]` в нормализованный формат YOLO `[x_center, y_center, w, h]` (от 0 до 1).
    *   Автоматически сдвигает индексы классов (из COCO 1-6 в YOLO 0-5).
    *   Генерирует `.txt` файлы для каждой картинки.
*   **Классы:** `dent` (вмятина), `scratch` (царапина), `crack` (трещина), `glass_shatter` (разбитое стекло), `lamp_broken` (разбитая фара), `tire_flat` (спущенное колесо).

## 🚀 Как запустить проект

1.  Клонируйте репозиторий:
    ```bash
    git clone https://github.com/romandavydov647-root/car-damage-detection-yolo-cv.git
    cd car-damage-detection-yolo-cv
