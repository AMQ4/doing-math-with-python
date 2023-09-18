"""
#4: Drawing the Mandelbrot Set

Your challenge here is to write a program to draw the Mandelbrot set—another
example of the application of simple rules leading to a complicated-looking
shape (see Figure 6-14).
"""

import matplotlib.pyplot as plt
import matplotlib.cm as cm

if __name__ == "__main__":
    width, height = 400, 400
    max_iterations = 1000
    xmin, xmax, ymin, ymax = -2.5, 1, -1, 1

    image = [[0 for _ in range(width)] for _ in range(height)]

    for x in range(width):
        for y in range(height):
            zx, zy = x * (xmax - xmin) / (width - 1) + xmin, y * (ymax - ymin) / (height - 1) + ymin
            c = zx + zy * 1j
            z = c
            for i in range(max_iterations):
                if abs(z) > 2.0:
                    break
                z = z * z + c
            # Set the pixel color based on the number of iterations
            image[y][x] = i

    plt.imshow(image, extent=(xmin, xmax, ymin, ymax), origin="lower", cmap=cm.Greys_r, interpolation="nearest")
    plt.colorbar()
    plt.show()
