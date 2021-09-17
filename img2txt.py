"""
original author: Viet Nguyen <nhviet1009@gmail.com>
Modified/adapted: Bradley Yoder
"""
import cv2
import numpy as np

def try_img_to_text(img_path):
    try:
        mode = "simple"
        CHAR_LIST = '@%#*+=-:. '
        num_chars = len(CHAR_LIST)
        num_cols = 80
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        height, width = image.shape
        cell_width = width / num_cols
        cell_height = 2 * cell_width
        num_rows = int(height / cell_height)
        if num_cols > width or num_rows > height:
            print("Too many columns or rows. Use default setting")
            cell_width = 6
            cell_height = 12
            num_cols = int(width / cell_width)
            num_rows = int(height / cell_height)

        for i in range(num_rows):
            for j in range(num_cols):
                print(
                    CHAR_LIST[min(int(np.mean(image[int(i * cell_height):min(int((i + 1) * cell_height), height),
                                              int(j * cell_width):min(int((j + 1) * cell_width),
                                                                      width)]) * num_chars / 255), num_chars - 1)], end="")
            print("")

        return True
    except:
        return False

def img2txt(excercise):
    extensions = ["jpeg", "jpg", "png"]
    excercise = excercise.replace(" ", "-")
    for ext in extensions:
        # print("Trying {}.{}".format(excercise, ext))
        if try_img_to_text("images/{}.{}".format(excercise, ext)):
            break

if __name__ == '__main__':
    # img2txt("push-ups")
    # img2txt("pullup")
    img2txt("exercise")
