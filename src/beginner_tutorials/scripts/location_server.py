#!/usr/bin/env python

from __future__ import print_function

from beginner_tutorials.srv import *
import rospy
import simple_navigation_goals

def location_goals(req):
    simple_navigation_goals.initiate(req.location)
    return LocationSrvResponse('selesai')

def location_server_main():
    rospy.init_node('location_server_node')
    s = rospy.Service('location', LocationSrv, location_goals)
    print("Ready")
    rospy.spin()

if __name__ == "__main__":
    location_server_main()
