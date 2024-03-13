import os
from PIL import Image, ImageDraw, ImageFont

def get_next_serial_number(output_folder):
    # Get a list of all files in the output folder
    existing_files = os.listdir(output_folder)

    # Extract serial numbers from existing file names
    serial_numbers = []
    for file_name in existing_files:
        try:
            serial_number = int(file_name.split('_')[0])  # Assuming the serial number is at the beginning of the file name before underscore
            serial_numbers.append(serial_number)
        except ValueError:
            pass

    # Find the next available serial number
    if serial_numbers:
        next_serial_number = max(serial_numbers) + 1
    else:
        next_serial_number = 1

    return next_serial_number

def generate_coin_with_details(radius, company_name, coin_value, color='gold', padding=10, stripe_color='black', stripe_width=5, output_folder=r'C:\Users\rithv\OneDrive\Desktop\ccnft', output_file='.jpg'):
    # Get the next serial number
    serial_number = get_next_serial_number(output_folder)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Calculate the dimensions of the image
    diameter = radius * 2
    image_width = diameter + 2 * padding
    image_height = diameter + 2 * padding

    # Create a blank image with a white background
    image = Image.new('RGB', (image_width, image_height), color='white')

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)

    # Load font
    font_path = "arial.ttf"  # Change this to the path of your desired font file
    font_size = 20
    font = ImageFont.truetype(font_path, font_size)

    # Calculate the position to draw the coin with padding
    coin_position = (padding, padding)

    # Draw the stripe border
    for i in range(1, stripe_width + 1):
        draw.ellipse([(coin_position[0] - i, coin_position[1] - i),
                      (coin_position[0] + diameter + i, coin_position[1] + diameter + i)],
                     outline=stripe_color)

    # Draw the coin
    draw.ellipse([coin_position, (coin_position[0] + diameter, coin_position[1] + diameter)], fill=color, outline='black')

    # Draw the company name above the serial number
    company_name_text = f"{company_name}"
    company_name_width, company_name_height = draw.textsize(company_name_text, font=font)
    company_name_position = ((image_width - company_name_width) // 2, (image_height - company_name_height) // 2 - 50)
    draw.text(company_name_position, company_name_text, fill='black', font=font)

    # Draw the serial number above the text
    serial_number_text = f"#{serial_number}"
    serial_number_width, serial_number_height = draw.textsize(serial_number_text, font=font)
    serial_number_position = ((image_width - serial_number_width) // 2, company_name_position[1] - serial_number_height - 10)
    draw.text(serial_number_position, serial_number_text, fill='black', font=font)

    # Draw "Carbon Credit NFT" text inside the coin
    text = "Carbon Credit NFT"
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((image_width - text_width) // 2, (image_height - text_height) // 2)
    draw.text(text_position, text, fill='black', font=font)

    # Increase the font size for the coin value
    value_font_size = 30
    value_font = ImageFont.truetype(font_path, value_font_size)

    # Draw coin value below the text
    coin_value_text = f"{coin_value}"
    coin_value_width, coin_value_height = draw.textsize(coin_value_text, font=value_font)
    coin_value_position = ((image_width - coin_value_width) // 2, text_position[1] + text_height + 10)
    draw.text(coin_value_position, coin_value_text, fill='black', font=value_font)

    # Save the image with a unique serial number in the specified folder
    output_file = f"{serial_number}_{output_file}"
    output_path = os.path.join(output_folder, output_file)
    image.save(output_path)
    print(f"Coin image saved as '{output_path}'")

    # Display the image
    display_image(output_path)

def display_image(file_path):
    image = Image.open(file_path)
    image.show()

# Example usage:
company_name = input("enter company: ")  # Change this to the desired company name
coin_value = int(input("carbon credit value: "))  # Change this to the desired coin value
generate_coin_with_details(radius=100, company_name=company_name, coin_value=coin_value, padding=20, stripe_color='blue', stripe_width=8)  # Generates and displays a coin with serial number, text, value, and company name inside
