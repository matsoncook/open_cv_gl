import math

def generate_circle_segments(center_x, center_y, radius, num_segments):
    segments = []
    angle_step = 2 * math.pi / num_segments

    for i in range(num_segments):
        # Start and end angles of each segment
        start_angle = i * angle_step
        end_angle = (i + 1) * angle_step

        # Calculate coordinates
        start_x = center_x + radius * math.cos(start_angle)
        start_y = center_y + radius * math.sin(start_angle)
        end_x = center_x + radius * math.cos(end_angle)
        end_y = center_y + radius * math.sin(end_angle)

        # Store segment coordinates
        segments.append(((start_x, start_y), (end_x, end_y)))

    return segments

# Example parameters
center_x = 0
center_y = 0
radius = 10
num_segments = 12

# Generate the segments
circle_segments = generate_circle_segments(center_x, center_y, radius, num_segments)

# Print the segments
for i, segment in enumerate(circle_segments):
    print(f"Segment {i + 1}: Start {segment[0]}, End {segment[1]}")