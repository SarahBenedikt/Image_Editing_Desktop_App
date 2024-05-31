from tkinter import *
from PIL import Image, ImageTk, ImageFont, ImageDraw, ImageFilter

# ---------------------------- Variables ------------------------------- #
WHITE = '#FFF5E0'
BLUE = '#141E46'
PINK = '#FF6969'
RED = '#C70039'
FONT_NAME = 'Comic Sans MS'

im = Image.open("TestPicture.jpeg").resize((700, 700))
raw_im = Image.open("TestPicture.jpeg").resize((700, 700))


# ---------------------------- Image Edit ------------------------------- #
def rotate_image(angle):
    rotated_im = im.rotate(angle)
    return rotated_im


def flip_image():
    flipped_im = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    return flipped_im


def blur_image():
    blurry_im = im.filter(ImageFilter.BLUR)
    return blurry_im

def emboss_image():
    emboss_im = im.filter(ImageFilter.EMBOSS)
    return emboss_im

def contour_image():
    contour_im = im.filter(ImageFilter.CONTOUR)
    return contour_im

def detail_image():
    detail_im = im.filter(ImageFilter.DETAIL)
    return detail_im

def black_white_image():
    bw_image = im.convert("L")
    bw_rgb_image = bw_image.convert("RGB")
    return bw_rgb_image


def create_thumbnail():
    thumbnail_im = im.resize((150,150))
    return thumbnail_im



def add_watermark(text):
    """Add a text watermark to the image."""
    watermark_font = ImageFont.truetype(FONT_NAME, 40)
    watermark_text = text
    watermark_color = (200, 200, 200, 0)
    watermark_positions = ((10, 10), (10, 300), (10, 600), (450, 150), (450, 450))
    watermarked_im = im.copy()
    draw = ImageDraw.Draw(watermarked_im)
    for watermark_position in watermark_positions:
        draw.text(watermark_position, watermark_text, font=watermark_font, fill=watermark_color)
    return watermarked_im


def update_image(new_im):
    global canvas
    canvas.image = ImageTk.PhotoImage(new_im)
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')


# ---------------------------- Button functions ------------------------------- #
def rotate():
    global im
    rotated_im = rotate_image(90)  # Specify the rotation angle here
    im = rotated_im
    update_image(rotated_im)


def watermark():
    global im
    for watermark in range(10):
        watermarked_im = add_watermark("Watermark")  # Specify the watermark text here
    im = watermarked_im  # Update the global image variable
    update_image(watermarked_im)


def flip():
    global im
    flipped_im = flip_image()
    im = flipped_im
    update_image(flipped_im)


def blur():
    global im
    blurry_im = blur_image()
    im = blurry_im
    update_image(blurry_im)

def contour():
    global im
    contour_im = contour_image()
    im = contour_im
    update_image(contour_im)

def emboss():
    global im
    emboss_im = emboss_image()
    im = emboss_im
    update_image(emboss_im)

def detail():
    global im
    detail_im = detail_image()
    im = detail_im
    update_image(detail_im)

def black_white():
    global im
    bw_im = black_white_image()
    im = bw_im
    update_image(bw_im)

def thumbnail():
    global im
    thumbnail_im = create_thumbnail()
    im = thumbnail_im
    update_image(thumbnail_im)

def original():
    global raw_im, im
    im = raw_im
    update_image(raw_im)


def save():
    im.save('new_file.jpeg')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Editor")
window.config(padx=30, pady=30, bg=WHITE)

header_label = Label(text="Image Editor", bg=WHITE, fg=PINK, font=(FONT_NAME, 50, "normal"))
header_label.grid(row=0, column=1,columnspan=2, padx=10, pady=(0, 20))

canvas = Canvas(width=700, height=700, bg=WHITE, highlightthickness=0)
canvas.image = ImageTk.PhotoImage(im)
canvas.create_image(0, 0, image=canvas.image, anchor='nw')
canvas.grid(row=1, column=1)

button_frame = Frame(bg=BLUE, width=200, height=700)
button_frame.grid(row=1, column=2, rowspan=3, padx=(10, 0), sticky="nsew")

original_button = Button(button_frame, text="Back to Original Img", font=(FONT_NAME, 15, "normal"), command=original,
                         highlightbackground=BLUE, fg=PINK, width=15, height=2)
original_button.pack(pady=10, padx=10)

watermark_button = Button(button_frame, text="Watermark", command=watermark, highlightbackground=BLUE, width=15)
watermark_button.pack(pady=10, padx=10)

rotate_button = Button(button_frame, text="Rotate", command=rotate, highlightbackground=BLUE, width=15)
rotate_button.pack(pady=10, padx=10)

rotate_button = Button(button_frame, text="Flip", command=flip, highlightbackground=BLUE, width=15)
rotate_button.pack(pady=10, padx=10)

blur_button = Button(button_frame, text="Filter: Blurry", command=blur, highlightbackground=BLUE, width=15)
blur_button.pack(pady=10, padx=10)

detail_button = Button(button_frame, text="Filter: Detail", command=detail, highlightbackground=BLUE, width=15)
detail_button.pack(pady=10, padx=10)

contour_button = Button(button_frame, text="Filter: Contour", command=contour, highlightbackground=BLUE, width=15)
contour_button.pack(pady=10, padx=10)

emboss_button = Button(button_frame, text="Filter: Emboss", command=emboss, highlightbackground=BLUE, width=15)
emboss_button.pack(pady=10, padx=10)

bw_button = Button(button_frame, text="Filter: Black / White", command=black_white, highlightbackground=BLUE, width=15)
bw_button.pack(pady=10, padx=10)

thumbnail_button = Button(button_frame, text="Thumbnail", command=thumbnail, highlightbackground=BLUE, width=15)
thumbnail_button.pack(pady=10, padx=10)

save_button = Button(button_frame, text="Save", font=(FONT_NAME, 15, "normal"), command=save, highlightbackground=BLUE,
                     fg=RED, width=15, height=2)
save_button.pack(pady=10, padx=10)

window.mainloop()
