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

def generate_dial_segment_array(center_x=0.0,
                                  center_y=0.0,
                                  radius=1.0, num_segments = 10, arc_angle = 20)
    dial_segments = []
    angle_step = 2 * math.pi / num_segments
    
    for i in range(num_segments):
        start_angle = i * angle_step-(arc_angle/2)
        end_angle =   i * angle_step+(arc_angle/2)
        ds = generate_dial_segment(start_angle,end_angle)
        dial_segments.append(ds)
    return dial_segments

def generate_dial_segment(start_angle,
                          end_angle,
                          center_x=0.0,
                          center_y=0.0,
                          radius=1.0,
                          depth=0.2):


        # Calculate coordinates
    x1 = center_x + radius * math.cos(start_angle)
    y1 = center_y + radius * math.sin(start_angle)
    x2 = center_x + radius * math.cos(end_angle)
    y2 = center_y + radius * math.sin(end_angle)

    x3 = center_x + (radius - depth) * math.cos(end_angle)
    y3 = center_y + (radius - depth) * math.sin(end_angle)
    x4 = center_x + (radius - depth) * math.cos(start_angle)
    y4 = center_y + (radius - depth) * math.sin(start_angle)

        # Store segment coordinates
        

    return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]


# Example parameters
center_x = 0
center_y = 0
radius = 10
num_segments = 12

# Generate the segments
circle_segments = generate_circle_segments(center_x, center_y, radius,
                                           num_segments)

# Print the segments
for i, segment in enumerate(circle_segments):
    print(f"Segment {i + 1}: Start {segment[0]}, End {segment[1]}")
