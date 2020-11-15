from rest_framework.throttling import AnonRateThrottle


class AnonTenPerTenSecondsThrottle(AnonRateThrottle):
    def parse_rate(self, rate):
        return (10, 10)