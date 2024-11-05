from Smart_IM2pdf import compress_image, resize_image,convert_images_to_pdf
import os

tp = 'new'
directory_path = r"D:\\Image2PDF\\NEW\\"
files = os.listdir(directory_path)
#print(files)
directory_save = r"D:\\Image2PDF\\res2\\"

# Создаем директории
os.makedirs(directory_path, exist_ok=True)
os.makedirs(directory_save, exist_ok=True)
#Коэфициент сжатия
alpha = 0.7
#Cжатие картинок
resize_image(files, directory_path, directory_save, alpha)

# directory_path = directory_save
# files = os.listdir(directory_path)

# directory_save = directory_save
# os.makedirs(directory_save, exist_ok=True)

#compress_image(files, directory_path, directory_save, quality=70)

# path = r"D:\\Users\\user\\Pictures\ets\\"
# #path2 = r"D:\\Users\\user\\Pictures\ets\\tst\\"
# output_pdf = "application.pdf"  # Имя PDF-файла, который вы хотите создать
# output_pdf = os.path.join(path, output_pdf)
# #print(output_pdf)
#
# images = os.listdir(path)
# image_paths = [os.path.join(path, image) for image in images if image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
# print(image_paths)
#convert_images_to_pdf(image_paths, output_pdf)

# # #Коэфициент сжатия
# alpha = 0.7
# # # #Cжатие картинок
# # compress_image(files, directory_path, directory_save)


