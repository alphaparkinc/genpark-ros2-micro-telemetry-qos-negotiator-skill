from client import Ros2MicroTelemetryQosNegotiatorClient

def main():
    client = Ros2MicroTelemetryQosNegotiatorClient()
    res = client.negotiate_qos_profile()
    print('ROS2 QoS Negotiator: ' + res['qos_negotiation_id'] + ' (' + res['topic_name'] + ')')
    print('Reliability: ' + res['selected_reliability'] + ' | Depth: ' + str(res['history_depth']))
    print('Config URL: ' + res['qos_profile_config_url'])

if __name__ == '__main__':
    main()
