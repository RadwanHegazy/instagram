from rest_framework.throttling import SimpleRateThrottle

class LoginThrottle(SimpleRateThrottle):
    scope = 'login'  # Unique scope for this throttle

    def get_cache_key(self, request, view):
        # Use the user's IP address as the cache key
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get('HTTP_X_FORWARDED_FOR').split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return f'login_throttle_{ip}'