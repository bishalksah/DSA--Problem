# Assignment 6: Seconds to H:M:S [Warm-up]
# Convert total seconds to (hours, minutes, seconds).
def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return (hours, minutes, seconds)
print(seconds_to_hms(3661))  # Output: (1, 1, 1)