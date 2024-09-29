import matplotlib.pyplot as plt


def calculate_rate_of_change(x1, y1, x2, y2):
    """
    Calculate the rate of change (slope) between two points (x1, y1) and (x2, y2).

    :param x1: x-coordinate of the first point
    :param y1: y-coordinate of the first point
    :param x2: x-coordinate of the second point
    :param y2: y-coordinate of the second point
    :return: Rate of change or slope between the two points
    """
    try:
        # Calculate the rate of change
        rate_of_change = (y2 - y1) / (x2 - x1)
        return rate_of_change
    except ZeroDivisionError:
        return "Error: Division by zero. The x-values of the two points cannot be the same."


def plot_rate_of_change(x1, y1, x2, y2, rate_of_change):
    """
    Plot the two points and the line connecting them to visualize the rate of change.

    :param x1: x-coordinate of the first point
    :param y1: y-coordinate of the first point
    :param x2: x-coordinate of the second point
    :param y2: y-coordinate of the second point
    :param rate_of_change: Calculated rate of change
    """
    # Plot the points
    plt.scatter([x1, x2], [y1, y2], color='red', zorder=5, label='Points')

    # Plot the line connecting the points
    plt.plot([x1, x2], [y1, y2], color='blue', linestyle='-', zorder=1, label='Rate of Change Line')

    # Annotate the points
    plt.text(x1, y1, f'({x1}, {y1})', fontsize=9, ha='right')
    plt.text(x2, y2, f'({x2}, {y2})', fontsize=9, ha='right')

    # Display the rate of change as text
    plt.title(f'Rate of Change: {rate_of_change:.2f}')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    print("Rate of Change Calculator with Visualization")
    try:
        # Get input from the user
        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))
        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))

        # Calculate the rate of change
        rate = calculate_rate_of_change(x1, y1, x2, y2)

        # Display the result
        if isinstance(rate, str):
            print(rate)
        else:
            print(f"The rate of change between points ({x1}, {y1}) and ({x2}, {y2}) is: {rate}")
            # Visualize the rate of change
            plot_rate_of_change(x1, y1, x2, y2, rate)
    except ValueError:
        print("Invalid input. Please enter numerical values.")


if __name__ == "__main__":
    main()
