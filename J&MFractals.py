import tkinter as tk
from tkinter import ttk
import numpy as np
from PIL import Image


"""
:author : ollprogram
"""

class Complex:
    """
    Representing a complex number.
    """
    real: float
    img: float

    def __init__(self, real: float, img: float):
        """

        :param real: The real part.
        :param img: The imaginary part.
        """
        self.real = real
        self.img = img

    def square(self):
        """

        :return: The square of this complex number.
        """
        return Complex(self.real * self.real - self.img * self.img, 2 * self.real * self.img)

    def square_mod(self):
        """

        :return: The module of this complex number but squared (|c|*|c| = a*a+b*b).
        """
        return self.real * self.real + self.img * self.img


def add_complex(zn: Complex, c: Complex):
    """

    :param zn: A Complex number.
    :param c: Another complex number.
    :return: zn + c.
    """
    zn.real += c.real
    zn.img += c.img
    return zn


def julia_live(z: Complex, c: Complex, precision: int):
    """

    :param z: The z Complex number.
    :param c: The c Complex number (parameter of a julia's fractal).
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The life time of the sequence in the algorithm (numbers of iterations).
    """
    for i in range(precision):
        if z.square_mod() > 4:
            return i
        else:
            z = add_complex(z.square(), c)
    return precision


def mandelbrot_live(c: Complex, precision: int):
    """

    :param c: The c Complex number.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The life time of the sequence in the algorithm (numbers of iterations).
    """
    z = Complex(0, 0)
    for i in range(precision):
        if z.square_mod() > 4:
            return i
        else:
            z = add_complex(z.square(), c)
    return precision


def x_pos_to_jm(x: float, width: int):
    """

    :param x: The x position in the data array.
    :param width: The width of the image.
    :return: The x position converted to the fractal's coordinate system.
    """
    return (4 * x / width) - 2


def y_pos_to_jm(y: float, height: int):
    """

    :param y: The y position in the data array.
    :param height: The height of the image.
    :return: The y position converted to the fractal's coordinate system.
    """
    return (4 * y / height) - 2


def colorize1(n: int, precision: int):
    """
    :param n: Life time (number of iterations) of the sequence in the julia or mandelbrot's algorithm.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The color of the pixel calculated, with the specified life time and precision, using gradiant colorization.
    """
    live_color = n * 255 * 6 / precision
    if live_color <= 255:
        return [live_color, 0, 0]
    elif live_color <= 255 * 2:
        return [255, 0, live_color - 255 * 2]
    elif live_color <= 255 * 3:
        return [255 - (live_color - 255 * 3), 0, 255]
    elif live_color <= 255 * 4:
        return [0, live_color - 255 * 4, 255]
    elif live_color <= 255 * 5:
        return [0, 255, 255 - (live_color - 255 * 5)]
    elif live_color < 255 * 6:
        return [live_color - 255 * 6, 255, 0]
    else:
        return [180, 0, 0]


def colorize2(n: int, precision: int):
    """
    :param n: Life time (number of iterations) of the sequence in the julia or mandelbrot's algorithm.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The color of the pixel calculated, with the specified life time and precision, using bitwise.
    """
    live_color: int = int(n * 255 * 255 * 255 / precision)
    r = live_color >> 16
    g = live_color >> 8 & 0x0000FF
    b = live_color & 0x0000FF
    return [r, g, b]


def colorize3(n: int, precision: int):
    """
    :param n: Life time (number of iterations) of the sequence in the julia or mandelbrot's algorithm.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The color of the pixel calculated, with the specified life time and precision, using bitwise.
    """
    live_color: int = int(n * 255 * 255 * 255 / precision)
    r = live_color >> 16
    b = live_color >> 8 & 0x0000FF
    g = live_color & 0x0000FF
    return [r, g, b]


def colorize4(n: int, precision: int):
    """
    :param n: Life time (number of iterations) of the sequence in the julia or mandelbrot's algorithm.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The color of the pixel calculated, with the specified life time and precision, using bitwise.
    """
    live_color: int = int(n * 255 * 255 * 255 / precision)
    b = live_color >> 16
    r = live_color >> 8 & 0x0000FF
    g = live_color & 0x0000FF
    return [r, g, b]


def colorize5(n: int, precision: int):
    """
    :param n: Life time (number of iterations) of the sequence in the julia or mandelbrot's algorithm.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The color of the pixel calculated, with the specified life time and precision, using bitwise.
    """
    live_color: int = int(n * 255 * 255 * 255 / precision)
    b = live_color >> 16
    g = live_color >> 8 & 0x0000FF
    r = live_color & 0x0000FF
    return [r, g, b]


def colorize6(n: int, precision: int):
    """
    :param n: Life time (number of iterations) of the sequence in the julia or mandelbrot's algorithm.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The color of the pixel calculated, with the specified life time and precision, using bitwise.
    """
    live_color: int = int(n * 255 * 255 * 255 / precision)
    g = live_color >> 16
    b = live_color >> 8 & 0x0000FF
    r = live_color & 0x0000FF
    return [r, g, b]


def colorize7(n: int, precision: int):
    """
    :param n: Life time (number of iterations) of the sequence in the julia or mandelbrot's algorithm.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The color of the pixel calculated, with the specified life time and precision, using bitwise.
    """
    live_color: int = int(n * 255 * 255 * 255 / precision)
    g = live_color >> 16
    r = live_color >> 8 & 0x0000FF
    b = live_color & 0x0000FF
    return [r, g, b]


# TODO réarranger tout ça :/
def colorize(option: str, n: int, precision: int):
    """

    :param option: The colorization algorithm's name chosen.
    :param n: Life time (number of iterations) of the sequence in the julia or mandelbrot's algorithm.
    :param precision: Maximum number of iterations in the julia or mandelbrot's algorithm.
    :return: The color of the pixel with the specified life time and option chosen.
    """
    return {"Color 1": colorize1(n, precision), "Color 2": colorize2(n, precision),
            "Color 3": colorize3(n, precision), "Color 4": colorize4(n, precision),
            "Color 5": colorize5(n, precision), "Color 6": colorize6(n, precision),
            "Color 7": colorize7(n, precision)}.get(option, colorize1(n, precision))


def draw_julia(width: int, height: int, c: Complex, color_option: str):
    """

    :param width: Width of the fractal.
    :param height: Height of the fractal.
    :param c: The c complex number (parameter for julia's fractals).
    :param color_option: The algorithm chosen to colorize the fractal.
    :return: Create, save and show a julia's fractal with the specified, c number, size and colorization algorithm.
    """
    julia = tk.Toplevel()
    julia.title("Loading Julia...")
    pb = ttk.Progressbar(julia, length=500, maximum=height)
    pb.pack()
    print("Calculating...")
    data = np.zeros((height, width, 3), dtype=np.uint8)
    for yp in range(height):
        for xp in range(width):
            data[yp][xp] = colorize(color_option, julia_live(Complex(x_pos_to_jm(xp, width),
                                                                     y_pos_to_jm(yp, height)), c, 100), 100)
        pb.step()
        julia.update()
    julia.destroy()
    print("I finished my calculation.")
    im = Image.fromarray(data, 'RGB')
    im.show("Julia_Fractal")
    print("saving...")
    im.save("julia_fractal.png")
    print("saved.")


def draw_mandelbrot(width: int, height: int, color_option: str):
    """

    :param width: Width of the fractal.
    :param height: Height of the fractal.
    :param color_option: The algorithm chosen to colorize the fractal.
    :return: Create, save and show a mandelbrot's fractal with the specified colorization algorithm and size.
    """
    mandel = tk.Toplevel()
    mandel.title("Loading Mandelbrot...")
    pb = ttk.Progressbar(mandel, length=500, maximum=height)
    pb.pack()
    print("Calculating...")
    data = np.zeros((height, width, 3), dtype=np.uint8)
    for yp in range(height):
        for xp in range(width):
            data[yp][xp] = colorize(color_option, mandelbrot_live(Complex(x_pos_to_jm(xp, width),
                                                                          y_pos_to_jm(yp, height)), 100), 100)
        pb.step()
        mandel.update()
    mandel.destroy()
    print("I finished my calculation.")
    im = Image.fromarray(data, 'RGB')
    im.show("Mandelbrot_Fractal")
    print("saving...")
    im.save("mandelbrot_fractal.png")
    print("saved.")


def convert_str_to_complex(number: str):
    """
    :param number: The string representing the complex (ex: -0,285+0,013i).
    :return: The converted Complex number from a String.
    """
    rfind_less = number.rfind('-')
    if rfind_less != 0 and rfind_less != -1:
        real_sign = 1
        if number[0] == '-':
            number = number.replace('-', "", 1)
            real_sign = -1
        parts = number.split("-")
        parts[0] = parts[0].replace(",", ".")
        parts[1] = parts[1].replace(",", ".").replace("i", "")
        return Complex(real_sign * float(parts[0]), -float(parts[1]))
    else:
        parts = number.split("+")
        parts[0] = parts[0].replace(",", ".")
        parts[1] = parts[1].replace(",", ".").replace("i", "")
        return Complex(float(parts[0]), float(parts[1]))


def draw_menu(width: int, height: int):
    """

    :param width: Window width.
    :param height: Window height.
    :return: Displays a menu window where we can choose some options to build fractals with the specified size.
    """
    root = tk.Tk()
    root.title("Mandelbrot & Julia's Fractals")
    menu = tk.Frame(root, width=width, height=height).grid()
    width_entry = tk.Entry(menu)
    width_entry.grid(row=0, column=1)
    width_l = tk.Label(menu, text="width").grid(row=0, column=0)
    height_entry = tk.Entry(menu)
    height_entry.grid(row=1, column=1)
    height_l = tk.Label(menu, text="height").grid(row=1, column=0)
    c_entry = tk.Entry(menu)
    c_entry.grid(row=2, column=1)
    c_label = tk.Label(menu, text="'c' complex number (julia only) \n"
                                  "example 1: 0,285-0,013i\n"
                                  "example 2: -0,285+0,013i").grid(row=2, column=0)
    choices = ["Color 1", "Color 2", "Color 3", "Color 4", "Color 5", "Color 6", "Color 7"]
    variable = tk.StringVar(menu)
    variable.set("Color 1")
    choice_box = tk.OptionMenu(menu, variable, *choices)
    choice_box.grid(row=3, column=2)
    julia_button = tk.Button(menu,
                             text="Julia",
                             font=10,
                             command=lambda: draw_julia(int(width_entry.get()), int(height_entry.get()),
                                                        convert_str_to_complex(c_entry.get()), variable.get()),
                             bg="orange").grid(row=3, column=0)
    mandelbrot_button = tk.Button(menu,
                                  text="Mandelbrot",
                                  font=10,
                                  command=lambda: draw_mandelbrot(int(width_entry.get()),
                                                                  int(height_entry.get()),
                                                                  variable.get()),
                                  bg="blue").grid(row=3, column=1)
    root.mainloop()


if __name__ == "__main__":
    draw_menu(200, 0)
