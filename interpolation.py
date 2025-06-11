def linear_interpolation(x_vals, y_vals, x):
    if len(x_vals) != len(y_vals):
        raise ValueError("x and y lists must be the same length")
    if len(x_vals) < 2:
        raise ValueError("At least two data points are required for linear interpolation")

    for i in range(len(x_vals) - 1):
        if x_vals[i] <= x <= x_vals[i + 1]:
            x0, x1 = x_vals[i], x_vals[i + 1]
            y0, y1 = y_vals[i], y_vals[i + 1]
            return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

    raise ValueError("The point is outside the range of the table")


def polynomial_interpolation(x_vals, y_vals, x):
    if len(x_vals) != len(y_vals):
        raise ValueError("x and y lists must be the same length")
    if len(x_vals) == 0:
        raise ValueError("At least one data point is required for polynomial interpolation")

    n = len(x_vals)
    result = 0
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
    x_vals = [1, 2, 4, 5]
    y_vals = [1, 4, 2, 5]
    x = 3  # Point to estimate

    try:
        lin_result = linear_interpolation(x_vals, y_vals, x)
        print(f"Linear interpolation result: {lin_result}")
    except ValueError as e:
        print(f"Linear interpolation error: {e}")

    try:
        poly_result = polynomial_interpolation(x_vals, y_vals, x)
        print(f"Polynomial interpolation result: {poly_result}")
    except ValueError as e:
        print(f"Polynomial interpolation error: {e}")


if __name__ == "__main__":
    main()

