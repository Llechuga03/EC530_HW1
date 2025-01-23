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

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;


#define R 6371 //radius of the earth
#define PI 3.14159265

//function to convert values to radians
double toRadians(double degrees)
{
    double radians = degrees * (PI/180);
    return radians;
}

//functions to find the distance between points
double findDistance(double lat1, double lon1, double lat2, double lon2)
{
    //first convert all the measurements to radians
    lat1 = toRadians(lat1);
    lat2 = toRadians(lat2);
    lon1 = toRadians(lon1);
    lon2 = toRadians(lon2);

    //we need the differences for the formula
    double diffLat = lat2 - lat1;
    double diffLon = lon2 - lon1;

    //broke the formula into two parts
    double a = sin(diffLat / 2) * sin(diffLat / 2) + cos(lat1) * cos(lat2) * sin(diffLon / 2) * sin(diffLon / 2);
    double c = 2 * R * asin(sqrt(a));

    return c;
}

//main function that returns an array with the corresponding closest points
vector<int> matchPoints(const vector<pair<double,double>> &A, const vector<pair<double, double>> &B)
{
    //vector to store the matches in
    vector<int> closestPoints;

    for(size_t j=0; j<A.size(); j++)
    {
        double minDist = 1e9; //using a super large value to begin with
        double closest = -1; //placeholder value for now

        for(size_t i = 0; i<B.size(); i++)
        {
            double distance = findDistance(A[j].first, A[j].second, B[i].first, B[i].second); //use haversine formula

            if(distance < minDist) //checking to ensure we have the correct closest distance
            {
                minDist = distance;
                closest = i;
            }
        }
        closestPoints.push_back(closest); //after each point, push back the updated closest index
    }

    return closestPoints;
}
