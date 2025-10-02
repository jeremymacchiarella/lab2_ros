import rclpy
from rclpy.node import Node


'''
    We're going to implement an open loop controller/FSM to have the turtlebot
    draw a square on the screen. Below I have commented parts of the code that
    you need to fill in to make the logic complete.
'''
# TEST TEST TEST TEST TEST
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

        
        self.vert_msg = Twist()
        self.horiz_msg = Twist()
        self.turn_msg = Twist()



        self.vert_msg.linear.y = 1.0
        self.horiz_msg.linear.x = 1.0
        self.turn_msg.angular.z = 1.57*2

        self.state = 0



    # Callback for the events
    def timer_callback(self):
        # If robot is turining
        
        # Call publisher here
        if (self.state == 0):
            self.publisher_.publish(self.horiz_msg)
            self.get_logger().info('robot is moving right')
            self.state = 1
        elif (self.state == 1):
            self.publisher_.publish(self.vert_msg)
            self.get_logger().info('robot is moving down')
            self.state = 2
        elif (self.state == 2):
            self.publisher_.publish(self.turn_msg)
            self.get_logger().info('robot is turning')
            self.state = 3
        elif (self.state == 3):
            pass 



        
        
        
            
       
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