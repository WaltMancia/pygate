from enum import Enum


class SecurityPolicy(str, Enum):

    PUBLIC = "public"

    JWT = "jwt"

    API_KEY = "api_key"

    JWT_OR_API_KEY = "jwt_or_api_key"
