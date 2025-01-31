import os
import logging
from parse_csv import parse_CSV
from parse_manual import parse_manual_input
from find_closest import find_closest_points


#Main function which serves as the hub for the user and functionality with the rest of the code
def main():
    #Prompting the user on what type of input format they want to use
    print("How would you like to input your data?")
    print("1. CSV File")
    print("2. Manual Input - Decimal Degrees")
    print("3. Manual Input - Degrees Minutes Seconds")

    choice = input("Enter the number of your choice: ").strip()

    if choice == "1":
        #Prompt for file inputs
        fileA = input("Enter path for first CSV file: ").strip()
        fileB = input("Enter path for second CSV file: ").strip()

        #Make sure user entered valid files
        if not os.path.exists(fileA) or not os.path.exists(fileB):
            print("ERROR: Could not open one or both of the files")
            return
        
        pointsA = parse_CSV(fileA)
        pointsB = parse_CSV(fileB)

    elif choice == "2":
        #Manual input using Decimal Degrees
        num_points_A = int(input("Enter number of points in A: "))
        pointsA = []
        for _ in range(num_points_A):
            lat = float(input("Enter latitude: ").strip())
            lon = float(input("Enter longitude: ").strip())
            pointsA.append((lat,lon))

        num_points_B = int(input("Enter number of points in B: "))
        pointsB = []
        for _ in range(num_points_B):
            lat = float(input("Enter latitude: ").strip())
            lon = float(input("Enter longitude: ").strip())
            pointsB.append((lat,lon))

    elif choice == "3":
        #Manual input using DMS
        num_points_A = int(input("Enter number of points in A: "))
        pointsA = []
        for _ in range(num_points_A):
            lat = input("Enter latitude (DMS format): ").strip()
            lon = input("Enter latitude (DMS format): ").strip()
            pointsA.append((parse_manual_input(lat),parse_manual_input(lon)))
        
        num_points_B = int(input("Enter number of points in B: "))
        pointsB = []
        for _ in range(num_points_B):
            lat = input("Enter latitude (DMS format): ").strip()
            lon = input("Enter latitude (DMS format): ").strip()
            pointsB.append((parse_manual_input(lat),parse_manual_input(lon)))
    
    else:
        print("ERROR: Invalid option. Please restart and select a valid option.")
        return
    
    #Now we can find the closest points
    closest_points = find_closest_points(pointsA, pointsB)
    print("\nClosest Points:")
    for i, point in enumerate(closest_points):
        print(f"Point {i+1}: {point}")


if __name__ == "__main__":
   main()

