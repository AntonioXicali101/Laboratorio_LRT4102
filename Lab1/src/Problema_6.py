import random
import numpy as np

def main():
    # Setting up the minimum size of the matrix
    mSize = 0
    while mSize < 5:
        mSize = int(input("Enter the size (at least 5) for the matrix: "))
        if mSize < 5:
            print("The matrix should be at least 5 x 5.")

    # Create the main matrix (m) and a separate directions matrix (d)
    # to avoid referencing the same array.
    m = np.zeros((mSize, mSize), dtype=str)
    d = np.full((mSize, mSize), ' ', dtype=str)  # fill directions with blank spaces initially

    # Fill the matrix with random choices
    for i in range(mSize):
        for j in range(mSize):
            m[i, j] = random.choice(['x', 'o', 'o'])

    # Set up the starting and finish points
    m[0, 0] = 'R'  # 'R' for Robot
    m[mSize - 1, mSize - 1] = 'D'  # 'D' for Destination

    print("Initial Matrix:")
    print(m)

    # NAVIGATION
    attempts = 0

    # Check if the robot is blocked right from the start
    if m[0, 1] == 'x' and m[1, 0] == 'x':
        print("No valid path exists from the start.")
    else:
        current_row, current_col = 0, 0
        last_origin_row = 0

        # Continue until the robot reaches the destination or there is no path
        while (current_row, current_col) != (mSize - 1, mSize - 1):
            attempts += 1  # increment attempts

            # 1. Attempt to move RIGHT
            if (current_col < mSize - 1 
                and (m[current_row][current_col + 1] in ['o', 'M']) 
                and m[current_row][current_col + 1] != 'x'):
                
                m[current_row][current_col] = 'M'    # Mark path in main matrix
                d[current_row][current_col] = '→'    # Mark direction in directions matrix

                current_col += 1

                print(m)
                print("Moving right...")

            # 2. Attempt to move DOWN
            elif (current_row < mSize - 1 
                  and (m[current_row + 1][current_col] in ['o', 'M']) 
                  and m[current_row + 1][current_col] != 'x'):
                
                m[current_row][current_col] = 'M'
                d[current_row][current_col] = '↓'

                current_row += 1

                print(m)
                print("Moving down...")

            # 3. If at the boundary, check if destination is next
            elif ((current_col == mSize - 1 or current_row == mSize - 1) and
                  ((current_row + 1 < mSize and m[current_row + 1][current_col] == 'D') or
                   (current_col + 1 < mSize and m[current_row][current_col + 1] == 'D'))):

                m[current_row][current_col] = 'M'

                # Destination DOWN
                if current_row + 1 < mSize and m[current_row + 1][current_col] == 'D':
                    d[current_row][current_col] = '↓'
                    current_row += 1
                    print(m)
                    print("Moving down into the destination...")

                # Destination RIGHT
                else:
                    d[current_row][current_col] = '→'
                    current_col += 1
                    print(m)
                    print("Moving right into the destination...")

            # 4. If no moves are possible, backtrack to the next row start
            else:
                last_origin_row += 1
                if last_origin_row < mSize:
                    current_row, current_col = last_origin_row, 0
                    print(m)
                    print("No path forward. Moving to next row start:")
                    print("Current position:", current_row, current_col)
                else:
                    print("No valid path exists.")
                    break

        # Check if destination was reached
        if (current_row, current_col) == (mSize - 1, mSize - 1):
            print(m)
            print("Robot reached the destination!")

    # Final results
    print("Final Matrix (Directions):")
    print(d)
    print(f"The robot performed a total of {attempts} moves.")

if __name__ == "__main__":
    main()
