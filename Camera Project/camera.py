import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

class ImageUploader:
    def __init__(self, root):

        # Initialize the ImageUploader class
        self.root = root
        self.root.title("PhotoFilter")

        # Set the window size (width x height)
        self.root.geometry("1000x1000")

        # Create a label to display the image
        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        # Create a button for uploading an image
        upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        upload_button.pack(pady=10)

        # Define filter options for the dropdown menu
        filter_options = ["Original", "Gaussian Blur", "Grayscale", "Sepia", "Edge Enhancement"]

        # Create a variable to store the selected filter
        self.filter_var = tk.StringVar(root)
        self.filter_var.set(filter_options[0])

        # Create a dropdown menu for selecting filters
        filter_dropdown = tk.OptionMenu(root, self.filter_var, *filter_options)
        filter_dropdown.pack(pady=10)

        # Create a button for applying the selected filter
        apply_filter_button = tk.Button(root, text="Apply Filter", command=self.apply_filter)
        apply_filter_button.pack(pady=10)

    def upload_image(self):
        # Open a file dialog to select an image file
        file_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])

        # If a file is selected, display the image
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        # Open the selected image and display it in the GUI
        self.original_image = Image.open(file_path)
        self.displayed_image = ImageTk.PhotoImage(self.original_image.resize((300, 300)))

        self.image_label.config(image=self.displayed_image)
        self.image_label.image = self.displayed_image

    def apply_filter(self):
        # Apply the selected filter to the image
        selected_filter = self.filter_var.get()

        if selected_filter == "Original":
            # Display the original image
            self.display_image(self.original_image.filename)
        elif selected_filter == "Gaussian Blur":
            # Apply Gaussian Blur filter to the image
            filtered_image = self.original_image.filter(ImageFilter.GaussianBlur(radius=2))
            self.update_display(filtered_image)
        elif selected_filter == "Grayscale":
            # Convert the image to grayscale
            filtered_image = self.original_image.convert("L")
            self.update_display(filtered_image)
        elif selected_filter == "Sepia":
            # Apply Sepia filter to the image
            filtered_image = self.apply_sepia(self.original_image)
            self.update_display(filtered_image)
        elif selected_filter == "Edge Enhancement":
            # Apply Edge Enhancement filter to the image
            filtered_image = self.apply_edge_enhancement(self.original_image)
            self.update_display(filtered_image)

    @staticmethod
    def apply_sepia(image):
        # Apply Sepia filter to the image
        width, height = image.size
        sepia_image = Image.new("RGB", (width, height))
        pixels = image.load()

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                sepia_image.putpixel((i, j), (min(tr, 255), min(tg, 255), min(tb, 255)))

        return sepia_image

    @staticmethod
    def apply_edge_enhancement(image):
        # Apply Edge Enhancement filter to the image
        enhanced_image = image.filter(ImageFilter.EDGE_ENHANCE)
        return enhanced_image

    def update_display(self, image):
        # Update the displayed image after applying a filter
        filtered_image = ImageTk.PhotoImage(image.resize((300, 300)))
        self.image_label.config(image=filtered_image)
        self.image_label.image = filtered_image

if __name__ == "__main__":
    # Create a Tkinter window and run the main loop
    root = tk.Tk()
    app = ImageUploader(root)
    root.mainloop()
