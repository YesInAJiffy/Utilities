from PIL import Image
import os
import sys


def is_within_tolerance(color1, color2, tolerance=5):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def make_transparent_gif(input_gif_path, output_gif_path, transparent_color=(255, 255, 255), tolerance=5):
    # Load the existing GIF
    gif = Image.open(input_gif_path)
    
    # Store the modified frames
    frames = []

    # Iterate through each frame in the GIF
    while True:
        # Convert each frame to RGBA (to include alpha channel for transparency)
        frame = gif.convert("RGBA")
        
        # Create a new transparent frame with the same size as original frame
        new_frame = Image.new("RGBA", frame.size, (0, 0, 0, 0))

        # Get the data of the current frame
        data = frame.getdata()

        # Process each pixel in the frame
        new_data = []
        for pixel in data:
            #print(pixel[:3])
            if is_within_tolerance(pixel[:3], transparent_color, tolerance):  # Check if the pixel is within tolerance
            #if pixel[:3] == transparent_color:  # If the pixel matches the transparent color
                new_data.append((0, 0, 0, 0))  # Fully transparent
            else:
                new_data.append(pixel)  # Keep the original pixel

        # Update the new frame with the processed data
        new_frame.putdata(new_data)
        
        # Append the modified frame to the list
        frames.append(new_frame)

        # Move to the next frame
        try:
            gif.seek(gif.tell() + 1)
        except EOFError:
            break  # End of frames

    # Save the modified frames as a new GIF
    frames[0].save(
        output_gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=gif.info.get('duration', 100),  # Default to 100ms if undefined
        loop=0,
        disposal=2,
        transparency=0  # Set the first color (index 0) as transparent
    )


def main():
    # Check if an argument is provided
    if len(sys.argv) < 2:
        print("Usage: python removetransparency.py sample.gif")
        print("Please provide name of the file.")
        return
    
    # Get the input string
    input_gif_path = sys.argv[1]

    #input_gif_path = 'return1.gif'  # Path to your input GIF
    base_name, _ = os.path.splitext(input_gif_path)
    output_gif_path = f"{base_name}_updated.gif"
    #transparent_color = (255, 255, 255)  # Color to make transparent (this RGB is for white)
    #transparent_color = (160,178,187)  # Superman image, first run
    transparent_color = (114,127,130)  # Superman image, second run

    make_transparent_gif(input_gif_path, output_gif_path, transparent_color, tolerance=30)

    

if __name__ == '__main__':
    main()
