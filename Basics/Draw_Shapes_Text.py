import cv2
import numpy as np

def draw_shapes(img):
    """
    Draws various shapes on the given image.

    Parameters:
        img: The image on which to draw shapes.
    """
    # Draw a green diagonal line
    cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), thickness=2)

    # Draw a filled red rectangle
    cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), thickness=cv2.FILLED)

    # Draw a blue circle with thickness
    cv2.circle(img, (150, 400), 50, (255, 0, 0), thickness=3)

    # Add a label with text
    cv2.putText(img, "Draw Shapes", (75, 50), cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0, 150, 0), thickness=2)

def main():
    # Create a black image (512x512 pixels, 3 color channels)
    img = np.zeros((512, 512, 3), np.uint8)

    # Call the function to draw shapes
    draw_shapes(img)

    # Display the image in a window
    cv2.imshow("Image", img)

    # Save the image to a file
    output_path = "shapes_image.png"
    cv2.imwrite(output_path, img)
    print(f"Image saved to {output_path}")

    # Wait for a key press and close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
