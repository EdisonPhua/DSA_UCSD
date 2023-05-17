from sys import stdin


def points_cover(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    # Combine start and end points into a single list with their type
    events = [(start, 'start') for start in starts] + [(end, 'end') for end in ends]

    # Sort the combined list
    events.sort()

    # Counter to track the number of active segments
    active_segments = 0

    # Iterate over the sorted list
    for event, event_type in events:
        if event_type == 'start':
            active_segments += 1
        else:  # event_type == 'end'
            active_segments -= 1

        # Find the index of the point in the original points list
        point_index = points.index(event)

        # Update the count for the point
        count[point_index] = active_segments

    return count




if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
