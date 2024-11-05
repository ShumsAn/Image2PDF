from img2pdf import convert
from PIL import Image, ImageFilter
import os
import cv2

def convert_images_to_pdf(image_paths, output_pdf):
    with open(output_pdf, "wb") as f:
        f.write(convert(image_paths))


def resize_image(list_img, input_path, output_path, alpha):
    """ЕСТЬ ПРОБЛЕМЫ С Shape. в cv2.imread выдает NoneType Потому что имена файлов русские.."""
    i = 0
    for img in list_img:
        i += 1
        print(i)
        full_path_source = os.path.join(input_path, img)
        print(full_path_source)
        #Загружаем изображение
        image = cv2.imread(full_path_source)
        # Получаем новые размеры изображения
        print(f'{type(image)}')
        new_width = int(image.shape[1] * alpha)
        new_height = int(image.shape[0] * alpha)
        # Уменьшаем размер изображения
        resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
        # Создаем путь для сохранения уменьшенного изображения
        full_path_save = os.path.join(output_path, img)
        # Сохраняем уменьшенное изображение
        cv2.imwrite(full_path_save, resized_image)

def compress_image(list_img, input_path, output_path, quality=85):
    i = 0
    for img in list_img:
        i += 1
        if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            full_path_source = os.path.join(input_path, img)
            image = Image.open(full_path_source)
            # Удаление альфа-канала (если он есть)
            image = image.convert('RGB')
            # Создаем путь для сохранения изображения стем же именем, но в формате JPEG
            output_img_name = os.path.splitext(img)[0] + ".jpg"
            full_path_save = os.path.join(output_path, output_img_name)
            # Сохраняем изображение в формате JPEG с указанным уровнем качества
            image.save(full_path_save, "JPEG", quality=quality)

def rename_images_to_sequential_numbers(directory):
    # Получаем список файлов в директории
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # Сортируем список файлов
    image_files.sort()

    # Счетчик для порядкового номера
    count = 1
    for image_file in image_files:
        # Получаем полный путь к файлу
        old_path = os.path.join(directory, image_file)
        # Формируем новое имя файла
        new_name = str(count) + ".jpg"  # Можете изменить расширение на нужное
        new_path = os.path.join(directory, new_name)

        # Переименовываем файл
        os.rename(old_path, new_path)
        # Увеличиваем счетчик
        count += 1

