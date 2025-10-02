import rclpy
from rclpy.node import Node


'''
    We're going to implement an open loop controller/FSM to have the turtlebot
    draw a square on the screen. Below I have commented parts of the code that
    you need to fill in to make the logic complete.
'''

# We have to use the geometry_msgs/msg/Twist to control robots
# Write in here what the correct import should be
from geometry_msgs.msg import Twist

class DrawSquare(Node):

    def __init__(self):
        # Init the node with a name (this is the name that appears when running)
        # 'ros2 node list'
        super().__init__('draw_square')
        
        # Remember that the 'create_publisher' function takes in three arguments
        # Message Type | Topic Name | Queue Length
        # Fill in those values here
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

        # Functions running at 1Hz
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        
        self.spiral_msg = Twist()

        self.spiral_msg.linear.x = 1.0
        self.spiral_msg.angular.z = 3.0


    # Callback for the events
    def timer_callback(self):
        # If robot is turining
        
        # Call publisher here
        self.publisher_.publish(self.spiral_msg)

        if (self.spiral_msg.angular.z > 0):
            self.spiral_msg.angular.z -= 0.25

        if (self.spiral_msg.angular.z < 0):
            self.spiral_msg.angular.z = 0.0
        self.get_logger().info('Robot is Drawing a Spiral!')
            
       
        # Get logger function call similar to 'cout' in C++
        # or 'print()' in python
        

        # Flip the mode of the robot
        


def main(args=None):
    rclpy.init(args=args)

    draw_square = DrawSquare()

    # Spin function *important*
    # makes sure that the program does not terminate
    # immediately
    rclpy.spin(draw_square)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    draw_square.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()