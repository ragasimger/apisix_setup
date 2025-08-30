from decouple import config

# Base configuration
CONFIG_DICT = {
    "API_SIX_BASE_URL": config("API_SIX_BASE_URL", default="http://localhost:9180"),
    "X_API_KEY": config("X_API_KEY", default="edd1c9f034335f136f87eweeewewewwad84fde43rerb625c8f1"),
    "limit-req": {
        "rate": config("LIMIT_REQUEST_RATE", default=10, cast=int),
        "burst": config("LIMIT_REQUEST_BURST", default=5, cast=int),
        "key": config("LIMIT_REQUEST_KEY", default="remote_addr")
    },
    "cors": {
        "allow_origins": "*",
        "allow_methods": "GET,POST,PATCH,OPTIONS",
        "allow_headers": "Authorization,Content-Type",
        "max_age": 86400
    },
    "nodesurl": config("NODES_URL", default="192.168.1.129:8082"),
    "nodesurlcore": config("NODES_URL_CORE", default="192.168.1.129:8083"),
    "mediaurl" : config("MEDIA_URL", default="192.168.1.79:8082"),
    "connect_timeout": config("CONNECT_TIMEOUT", default=30000, cast=int),
    "send_timeout": config("SEND_TIMEOUT", default=60000, cast=int),
    "read_timeout": config("READ_TIMEOUT", default=60000, cast=int)
}