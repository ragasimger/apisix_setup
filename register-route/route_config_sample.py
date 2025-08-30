from configs import CONFIG_DICT as config

ROUTE_CONFIGS = [
    {
        "uri": "/api/v1/auth-app/*",
        "methods": ["GET","POST","OPTIONS"],
        "plugins": {
            "limit-req": config["limit-req"],
            "cors": config["cors"]
        },
        "upstream": {
            "type": "roundrobin",
            "nodes": {
                config["nodesurl"]: 1
            },
            "timeout": {
                "connect": config["connect_timeout"],
                "send": config["connect_timeout"],
                "read": config["connect_timeout"]
            }
        }
    },   
    {
        "uri": "/api/v1/another-app/*",
        "methods": ["GET","POST","OPTIONS"],
        "plugins": {
            "limit-req": config["limit-req"],
            "cors": config["cors"],
            "jwt-auth": {},
        },
        "upstream": {
            "type": "roundrobin",
            "nodes": {
                config["nodesurl"]: 1
            },
            "timeout": {
                "connect": config["connect_timeout"],
                "send": config["connect_timeout"],
                "read": config["connect_timeout"]
            }
        }
    },   
]