def linear_interpolation(x_vals, y_vals, x):
    """
    Performs linear interpolation for a given point x using x_vals and y_vals.

    Args:
        x_vals (list): list of x data points (must be sorted in ascending order)
        y_vals (list): corresponding y values
        x (float): the x value to interpolate

    Returns:
        float: interpolated y value

    Raises:
        ValueError: for invalid input or out-of-bounds x
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("x and y lists must be the same length")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required for linear interpolation")
    if x < x_vals[0] or x > x_vals[-1]:
        raise ValueError("The point is outside the range of the table")

    for i in range(len(x_vals) - 1):
        if x_vals[i] <= x <= x_vals[i + 1]:
            x0, x1 = x_vals[i], x_vals[i + 1]
            y0, y1 = y_vals[i], y_vals[i + 1]
            return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

    raise ValueError("Could not interpolate the given value")


def polynomial_interpolation(x_vals, y_vals, x):
    """
    Performs polynomial interpolation using Lagrange method.

    Args:
        x_vals (list): list of x data points
        y_vals (list): corresponding y values
        x (float): the x value to interpolate

    Returns:
        float: interpolated y value

    Raises:
        ValueError: for invalid input, duplicate x values, or out-of-bounds x
    """
    if len(x_vals) != len(y_vals):
        raise ValueError("x and y lists must be the same length")
    if len(x_vals) == 0:
        raise ValueError("At least one data point is required for polynomial interpolation")
    if x < min(x_vals) or x > max(x_vals):
        raise ValueError("The point is outside the range of the table")

    result = 0
    n = len(x_vals)

    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if j != i:
                if x_vals[i] == x_vals[j]:
                    raise ValueError("Duplicate x values are not allowed")
                term *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        result += term
    return result


def main():
    # Sample data
    x_vals = [1, 2, 4, 6]
    y_vals = [1, 4, 2, 5]
    x = 3  # Point to estimate

    try:
        lin_result = linear_interpolation(x_vals, y_vals, x)
        print(f"Linear interpolation result: {lin_result}")
    except (ValueError, TypeError) as e:
        print(f"Linear interpolation error: {e}")

    try:
        poly_result = polynomial_interpolation(x_vals, y_vals, x)
        print(f"Polynomial interpolation result: {poly_result}")
    except (ValueError, TypeError) as e:
        print(f"Polynomial interpolation error: {e}")


if __name__ == "__main__":
    main()
