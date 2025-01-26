import cv2

def load_image(path):
    """Load an image from the given path."""
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image at path '{path}' could not be loaded. Check the path.")
    return img

def resize_image(img, width, height):
    """Resize the image to the given dimensions."""
    return cv2.resize(img, (width, height))

def crop_image(img, x_start, y_start, x_end, y_end):
    """Crop the image to the given coordinates."""
    return img[y_start:y_end, x_start:x_end]

def main():
    # Path to the input image
    path = "Resources/road.jpg"
    
    # Load the image
    img = load_image(path)
    print(f"Original Image Shape: {img.shape}")
    
    # Resize the image
    width, height = 1000, 1000
    img_resized = resize_image(img, width, height)
    print(f"Resized Image Shape: {img_resized.shape}")
    
    # Crop a region from the image
    x_start, y_start, x_end, y_end = 430, 300, 480, 540
    img_cropped = crop_image(img, x_start, y_start, x_end, y_end)
    
    # Resize the cropped image to match the original size
    img_cropped_resized = resize_image(img_cropped, img.shape[1], img.shape[0])
    
    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Resized Image", img_resized)
    cv2.imshow("Cropped Image", img_cropped)
    cv2.imshow("Cropped and Resized Image", img_cropped_resized)
    
    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the main function
if __name__ == "__main__":
    main()
