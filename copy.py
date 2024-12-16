'''
Данный код осуществляет добавление шума к изображениям, находящимся в заданной директории, 
и сохраняет их в указанном месте. 
Кроме того, он выполняет поворот изображений на 15 градусов по часовой стрелке 
и сохраняет обработанные изображения в определённую папку
'''

import os
import numpy as np
from PIL import Image


def add_noise(image):
    """Добавляет шум к изображению."""
    # Преобразуем изображение в массив numpy
    image_array = np.array(image)

    # Генерируем шум
    noise = np.random.normal(0, 25, image_array.shape)  # Среднее 0, стандартное отклонение 25
    noisy_image_array = np.clip(image_array + noise, 0, 255).astype(np.uint8)

    return Image.fromarray(noisy_image_array)


def process_images(input_folder, output_folder):
    """Обрабатывает изображения в указанной папке."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # форматы изображений
            # Открываем изображение
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)

            # Копируем изображение и добавляем шум
            noisy_image = add_noise(image)
            noisy_image = noisy_image.convert("RGB")  # Преобразуем в RGB перед сохранением
            noisy_image.save(os.path.join(output_folder, f'noisy_{filename}'))

            # Копируем исходное изображение и поворачиваем на 15 градусов
            rotated_right_60 = image.rotate(-15, expand=True)
            rotated_right_60 = rotated_right_60.convert("RGB")  # Преобразуем в RGB перед сохранением
            rotated_right_60.save(os.path.join(output_folder, f'rotated_right_60_{filename}'))


# Укажите путь к папке с изображениями и папке для сохранения результатов
input_folder = 'D:\\Буткмекер\\1xБет\\'  # Папка с изображениями
output_folder = 'D:\\Буткмекер\\1xБет\\output4'  # Папка для сохранения результатов

process_images(input_folder, output_folder)
