# EC530_HW1
Objective for the Assignment:  If the user gives you two arrays of geo location, match each point in the first array to the closest one in the second array. 
Code is written in C++ and uses the Haversine Formula as the method for finding shortest distance between two GPS points. The equation is provided below as
well as in the .cpp file itself. 

Haversine Formula: d = 2R * arcsin(sqrt(sin²(Δφ/2) + cos(φ1) * cos(φ2) * sin²(Δλ/2)))

d: Distance between the two points 
R: Earth's radius (approximately 6,371 km) 
φ1, φ2: Latitude of point 1 and point 2 respectively 
λ1, λ2: Longitude of point 1 and point 2 respectively 
Δφ: Latitude difference between the two points 
Δλ: Longitude difference between the two points

This code is also meant to use distances measured in km.

For this assignment, I collaborated with Angel Amaya in brainstorming how to approach the problem and what data structures to use. We discussed KD trees, but that was a bit confusing for me so I used a simpler approach that seemed more intuitive to me, even though the performance with the KD tree is much better.
