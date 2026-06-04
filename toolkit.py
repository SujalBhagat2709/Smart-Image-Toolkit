from PIL import Image

from image_processor import grayscale_image

def resize_image(
    image_path,
    width,
    height
):

    image = Image.open(image_path)

    resized = image.resize(
        (width, height)
    )

    output_file = (
        image_path.rsplit(".", 1)[0]
        + "_resized.jpg"
    )

    resized.save(output_file)

    return output_file


print(
    "\n================================="
)

print(
    "SMART IMAGE TOOLKIT"
)

print(
    "================================="
)

image_path = input(
    "\nEnter Image Path:\n"
)

print(
    "\n1. Grayscale"
)

print(
    "2. Resize"
)

choice = input(
    "\nChoose Option: "
)

if choice == "1":

    output = grayscale_image(
        image_path
    )

elif choice == "2":

    width = int(
        input("Width: ")
    )

    height = int(
        input("Height: ")
    )

    output = resize_image(
        image_path,
        width,
        height
    )

else:

    print(
        "Invalid Choice"
    )

    exit()

print(
    f"\nOutput Generated:\n{output}"
)