from rest_framework.throttling import UserRateThrottle

class RegisterThrottle(UserRateThrottle):
    rate="20/hour"

class TokenObtainThrottle(UserRateThrottle):
    rate="10/hour"

class TokenRefreshThrottle(UserRateThrottle):
    rate="5/hour"

class OrderRelatedThrottle(UserRateThrottle):
    rate="10/hour"

class GeneralAPIsThrottle(UserRateThrottle):
    rate="30/minute"
