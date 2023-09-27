from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped
import time, rclpy
from PySide2.QtCore import Signal, QObject

class Signals(QObject):
    position_updated = Signal(float, float, float, float)

class TopicSubscriber(Node):
    def __init__(self, signals):
        super().__init__('minimal_subscriber')
        self.signals = signals
        self.subscription = self.create_subscription(
        PoseWithCovarianceStamped,
        'amcl_pose',
        self.listener_callback,
        10)
        self.subscription
        self.pos_x = 0
        self.pos_y = 0
        self.ori_z = 0
        self.ori_w = 0
        self.last_saved_time = 0

    def listener_callback(self, msg):
        current_time = time.time()
        if current_time - self.last_saved_time >= 1: 
            self.pos_x = (float(msg.pose.pose.position.x))
            self.pos_y = (float(msg.pose.pose.position.y))
            self.ori_z = (float(msg.pose.pose.orientation.z))
            self.ori_w = (float(msg.pose.pose.orientation.w))
            self.signals.position_updated.emit(self.pos_x, self.pos_y, self.ori_z, self.ori_w)
            # print(self.pos_x, self.pos_y)

def start_node(signals):
    rclpy.init()
    topic_subscriber = TopicSubscriber(signals)
    rclpy.spin(topic_subscriber)
    topic_subscriber.destroy_node()
