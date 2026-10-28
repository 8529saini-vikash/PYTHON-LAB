from PIL import Image, ImageFilter


filename = input("Enter image filename (with extension): ")

try:
    image = Image.open(filename)
except FileNotFoundError:
    print("Error: Image file not found.")
    raise SystemExit
except Exception as error:
    print("Unable to open image:", error)
    raise SystemExit


print("Image loaded successfully.")
print("Image size:", image.size)
print("Available filters: 1. Grayscale  2. Threshold  3. Blur")

choice = input("Choose a filter: ")

if choice == "1":
    result = image.convert("L")
    output_name = "output_grayscale.png"
elif choice == "2":
    grayscale = image.convert("L")
    result = grayscale.point(
        lambda pixel: 255 if pixel >= 128 else 0
    )
    output_name = "output_threshold.png"
elif choice == "3":
    result = image.filter(ImageFilter.BLUR)
    output_name = "output_blur.png"
else:
    print("Invalid choice.")
    raise SystemExit

result.save(output_name)
print("Filter applied successfully.")
print("Saved processed image as:", output_name)
