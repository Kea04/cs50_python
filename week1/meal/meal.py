def main():
    input_time = input("What time is it? ")
    time_in_hours = convert(input_time)
    
    if 7.00 <= time_in_hours <= 8.00:
        return "breakfast time"
    elif 12.00 <= time_in_hours <= 13.00:
        return "lunch time"
    elif 18.00 <= time_in_hours <= 19.00:
        return "dinner time"
    else:
        return "none"


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    print(main())