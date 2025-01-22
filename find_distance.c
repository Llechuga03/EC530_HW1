/*
Assignment 1 due 1/23/25
Objective: If the user gives you two arrays of geo location, match
each point in the first array to the closest one in the second array
*/

/*
The way to find the distance between to GPS locations ->

Haversine Formula: d = 2R * arcsin(sqrt(sin²(Δφ/2) + cos(φ1) * cos(φ2) * sin²(Δλ/2)))

d: Distance between the two points 
R: Earth's radius (approximately 6,371 km) 
φ1, φ2: Latitude of point 1 and point 2 respectively 
λ1, λ2: Longitude of point 1 and point 2 respectively 
Δφ: Latitude difference between the two points 
Δλ: Longitude difference between the two points 
*/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define R 6371

