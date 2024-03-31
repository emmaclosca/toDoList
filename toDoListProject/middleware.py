from venv import logger
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import logging

# for guidance, I have used:
# https://www.invicti.com/blog/web-security/http-security-headers/
# https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html#x-xss-protection
class Security(MiddlewareMixin):
    def process_response(self, request, response):
        # Add security headers for XSS attacks
        response["X-XSS-Protection"] = "1; mode=block"
        response["X-Content-Type-Options"] = "nosniff"
        response["X-Frame-Options"] = "DENY"
       
        # Add security headers for SQL injection
        response["X-SQL-Injection-Protection"] = "1"
        
        # Add security headers for sensitive data exposure
        response["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response["Feature-Policy"] = "camera 'none'; microphone 'none'"
        
        return response



    
    