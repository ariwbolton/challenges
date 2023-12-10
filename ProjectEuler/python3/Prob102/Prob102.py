import sympy

def triangle_containment():
    triangles = []

    with open('./0102_triangles.txt', 'r') as f:
        for line in f.readlines():
            nums = [int(num_str) for num_str in line.strip().split(',')]
            points = [
                sympy.Point(nums[0], nums[1]),
                sympy.Point(nums[2], nums[3]),
                sympy.Point(nums[4], nums[5]),
            ]

            triangles.append(sympy.Polygon(*points))

    origin = sympy.Point(0, 0)

    # Leverages Sympy; I had drawn up a solution and was looking for helpers to implement... lookslike Sympy did it the same way I did!
    # 1. Imagine walking around the triangle
    # 2. For each segment, the origin should either always be on the right, or the left
        # Use "2-dim cross product" to determine which "side" the origin is on
        # Let A be current vertex, A' be next vertex around the triangle, and O be origin
        # 2a. Consider vectors B = (A' - A) and C = (O - A), but add in a 3rd dimension, set to zero
        # 2b. Do B x C
        # 2c. Check that the resulting sign on the cross product is the same for all A in the triangle
            # If so, the origin is either "on the right/left" for each vertex, and therefore is in the triangle
    return sum(triangle.encloses_point(origin) for triangle in triangles)

print((triangle_containment()))