# iniciante 03.
if __name__ == "__mainb__":
    # iniciante.
    for i in range(25):
        hour = f"{i}"
        if i < 10:
            print(f"0{i}:00 - 0{i}:30")
            if i + 1 < 10:
                print(f"0{i}:30 - 0{i + 1}:00")
            else:
                print(f"0{i}:30 - {i + 1}:00")
        else:
            print(f"{i}:00 - {i}:30")
            print(f"{i}:30 - {i + 1}:00")

# iniciante 02.
for i in range(25):
    hour = "{0:02d}:00 - {0:02d}:30"
    print(hour.format(i))

    hour = "{0:02d}:30 - {0:02d}:00"
    print(hour.format(i, i + 1))
