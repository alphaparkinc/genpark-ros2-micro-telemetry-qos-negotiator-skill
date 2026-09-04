class Ros2MicroTelemetryQosNegotiatorClient:
    def negotiate_qos_profile(self, topic_name='/robot/telemetry/imu_raw', network_bandwidth_kbps=128, packet_loss_rate=0.04):
        return {
            'qos_negotiation_id': 'qos_neg_9918',
            'topic_name': topic_name,
            'selected_reliability': 'BEST_EFFORT' if packet_loss_rate > 0.05 else 'RELIABLE',
            'selected_durability': 'VOLATILE',
            'history_depth': 10,
            'deadline_period_ms': 50,
            'liveliness_lease_duration_ms': 200,
            'qos_profile_config_url': 'https://ros2.qos.genpark.ai/profiles/qos_neg_9918.xml'
        }
