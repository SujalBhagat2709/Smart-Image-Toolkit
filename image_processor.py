from PIL import Image

def grayscale_image(image_path):

    image = Image.open(image_path)

    gray_image = image.convert("L")

    output_file = (
        image_path.rsplit(".", 1)[0]
        + "_grayscale.jpg"
    )

    gray_image.save(output_file)

    return output_file


if __name__ == "__main__":

    image_path = input(
        "Enter Image Path: "
    )

    output = grayscale_image(
        image_path
    )

    print(
        f"\nOutput Generated:\n{output}"
    )