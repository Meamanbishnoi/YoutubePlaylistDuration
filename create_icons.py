from PIL import Image, ImageDraw

def create_icon(size, filename):
    # Create image with red background
    img = Image.new('RGB', (size, size), color='#ef4444')
    draw = ImageDraw.Draw(img)
    
    # Calculate play button triangle
    padding = size * 0.25
    triangle = [
        (padding, padding),
        (size - padding, size / 2),
        (padding, size - padding)
    ]
    
    # Draw white play button
    draw.polygon(triangle, fill='white')
    
    # Save
    img.save(f'static/{filename}')
    print(f'Created {filename}')

# Create both icon sizes
create_icon(192, 'icon-192.png')
create_icon(512, 'icon-512.png')
print('Icons created successfully!')
