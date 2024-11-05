from Smart_IM2pdf import convert_images_to_pdf,compress_image,rename_images_to_sequential_numbers,resize_image
from tkinter import *
from tkinter import filedialog
import os

class SmartPDF(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Smart_IM2PDF")
        self.master.rowconfigure(500, weight=500)
        self.master.columnconfigure(5, weight=5)
        self.grid(sticky=W+E+N+S)
        self.count = 0
        self.text = Label(text='Каталог файлов:', height=2, width=122, background="silver",foreground='blue')
        self.text.grid(row=1,column=0)
        self.text2 = Label(text='Каталог Преобразованных файлов:', height=2, width=122, background="silver",foreground='blue')
        self.text2.grid(row=3,column=0)
        self.button = Button(self, text="Выбрать каталог файлов",
                             command=self.select_file_directory, width=60)
        self.button.grid(row=1, column=0)
        self.button2 = Button(self, text="Преобразовать файлы В PDF",width=60,
                              command=lambda:(convert_images_to_pdf(self.image_paths,self.pdf),self.result_name_pdf()))
        self.button2.grid(row=3, column=1)
        self.button3 = Button(self, text="Выбрать каталог преобразованных",
                              command=self.select_file_directory_resize,width=60)
        self.button3.grid(row=2, column=0)
        self.button5 = Button(self, text="Сжать Изображения на quality 85",
                              command=lambda : (compress_image(self.images,self.directory_path, self.directory_resize),
                                                self.result_name_compres()),width=60)
        self.button5.grid(row=2, column=1)
        self.text_list = Label(text='Готовые файлы:', height=2, width=122, background="silver",foreground='blue')
        self.text_list.grid(row=8, column=0)
        self.button8 = Button(self, text="Переименовать файлы по номерам(Если наименования русские)",
                              command=lambda: rename_images_to_sequential_numbers(self.directory_path),width=60)
        self.button8.grid(row=3, column=0)
        self.button6 = Button(self, text="Resize_image alpha 0.85",
                              command=lambda : resize_image(self.images,self.directory_path, self.directory_resize,0.85),
                                                width=60)
        self.button6.grid(row=1, column=1)
        # self.text_box = Text(width=30, height=2, bg='darkgreen', fg='white', wrap=WORD)
        # self.text_box.grid(row=5, column=3)

    def select_file_directory(self):
        self.directory_path = filedialog.askdirectory(initialdir='/', title='Выбрать каталог')
        self.text_dir_f = Label(text=str(self.directory_path), height=2, width=122, background="silver",
                                foreground='blue')
        self.text_dir_f.grid(row=2, column=0)
        self.images = os.listdir(self.directory_path)
        self.image_paths = [os.path.join(self.directory_path, image) for image in self.images if
                       image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        self.last_folder = os.path.basename(os.path.normpath(self.directory_path))
        print(self.last_folder)  # Вывод: latest_project
        self.name_pdf = f'NEWapplication'+ f'_{self.last_folder}' + '.pdf'


    def select_file_directory_resize(self):
        self.directory_resize = filedialog.askdirectory(initialdir='\\', title='Выбрать каталог для преобразованных')
        self.text_dir_r = Label(text=str(self.directory_resize), height=2, width=122, background="silver",
                               foreground='blue')
        self.text_dir_r.grid(row=5, column=0)
        self.pdf = os.path.join(self.directory_resize, self.name_pdf)


    def select_list_image(self):
        print(type(self.text_list))
        self.images_list = filedialog.askopenfilenames(initialdir='\\', title='Выбрать порядок списка')
        #self.text_list['text'] = self.text_list['text'] + ' ' +
        print(self.images_list)
        self.text_list = Label(text=str(self.images_list),height=2, width=122, background="silver",
                           foreground='blue')
        self.text_list.grid(row=9, column=0)

    def result_name_pdf(self):
        self.text_list = Label(text=str(self.name_pdf), height=2, width=122, background="silver",
                               foreground='blue')
        self.text_list.grid(row=9, column=0)
    def result_name_compres(self):
        self.text_list = Label(text=str(self.image_paths), height=2, width=122, background="silver",
                               foreground='blue')
        self.text_list.grid(row=9, column=0)
    def result_name_resize(self):
        self.image_paths = [os.path.join(self.directory_resize, image) for image in self.images if
                            image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
        self.text_list = Label(text=str(self.image_paths), height=2, width=122, background="silver",
                               foreground='blue')
        self.text_list.grid(row=9, column=0)

    # def select_name_file(self):
    # Не получается нормально склеить строку + имя
    #     self.name_pdf = self.text_box.get("1.0",END) + '.pdf'
    #     try:
    #         self.pdf = os.path.join(self.directory_resize,self.name_pdf)
    #         print(self.pdf)
    #     except:
    #         print('Введите имя файла и Каталог для его создания')


if __name__ == "__main__":
    SmartPDF().mainloop()




