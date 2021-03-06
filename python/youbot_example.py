# Copyright 2006-2014 Dr. Marc Andreas Freese. All rights reserved. 
# marc@coppeliarobotics.com
# www.coppeliarobotics.com
# 
# -------------------------------------------------------------------
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# 
# You are free to use/modify/distribute this file for whatever purpose!
# -------------------------------------------------------------------
#
# This file was automatically created for V-REP release V3.1.0 on January 20th 2014

# Make sure to have the server side running in V-REP: 
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

import vrep
import time

print('Program started')
vrep.simxFinish(-1) # just in case, close all opened connections
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
if clientID!=-1:
    print('Connected to remote API server')
    #res,objs=vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_oneshot_wait)
    #if res==vrep.simx_error_noerror:
    #    print('Number of objects in the scene: ',len(objs))
    #else:
    #    print('Remote API function call returned with error code: ',res)
    
    res,jh=vrep.simxGetObjectHandle(clientID, "arm_joint_1", vrep.simx_opmode_oneshot_wait)
    print("Joint Handle " + str(jh))
    res = vrep.simxSetJointTargetPosition(clientID, jh, 0.5, vrep.simx_opmode_oneshot)
    print("Result: " + str(res))
    time.sleep(1)
    vrep.simxFinish(clientID)
else:
    print('Failed connecting to remote API server')
print('Program ended')
