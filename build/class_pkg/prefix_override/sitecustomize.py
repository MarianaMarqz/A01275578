import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/mech1/MWorkspace/turtlebot_ws/install/class_pkg'
