
🤖 **Plot twist:** This README was crafted by an AI with a PhD in Documentation, then double-checked by a human ([@ragasimger](https://github.com/ragasimger)) who confirmed the AI hasn't secretly added plans for world domination.
Last verified: 2025-08-30 23:06:56 GMT+5:45.

# 🚀 APISIX + Dashboard + Route Registration (Dockerized Setup)

This repository provides a **ready-to-use Docker Compose setup** for running [Apache APISIX](https://apisix.apache.org/) (API Gateway), [APISIX Dashboard](https://apisix.apache.org/docs/dashboard/), and a lightweight **Python route registration service**.  

It is designed for developers who want a reproducible way to:  
- Run APISIX with **etcd** as the backend.  
- Manage routes visually via **APISIX Dashboard**.  
- Automatically register API routes and plugins using a **custom Python service**.  

---

## 📂 Project Structure

```
├── .env.sample               # Example environment variables
├── .gitignore
├── apisix-conf/             # APISIX Dockerfile + config templates
│   ├── Dockerfile
│   ├── config.yaml.template
│   └── entrypoint_wrapper.sh
├── dashboard-conf/          # APISIX Dashboard Dockerfile + config templates
│   ├── Dockerfile
│   ├── config.yaml.template
│   └── entrypoint.sh
├── docker-compose.yaml      # Orchestrates all services
└── register-route/         # Python service for route registration
    ├── Dockerfile
    ├── configs.py
    ├── requirements.txt
    ├── route_config_sample.py
    └── route_register.py
```

---

## 🛠 Components

### 1. **Etcd**
- Stores configuration for APISIX.  
- Runs on port **2379**.  
- Health check included in `docker-compose.yaml`.

### 2. **APISIX**
- Based on `apache/apisix:3.13.0-debian`.  
- Config templated using environment variables (`envsubst`).  
- Exposes:  
  - **9080** → APISIX Gateway (default traffic port)  
  - **9180 / 9091** → Admin API  
  - **9443** → HTTPS Gateway  

### 3. **APISIX Dashboard**
- Based on `apache/apisix-dashboard:3.0.1-alpine`.  
- Dashboard runs on **http://localhost:9000**.  
- Username/password set via `.env`.  

### 4. **Route Registration Service**
- A Python 3.11 service that registers routes into APISIX via the Admin API.  
- Configurable with `.env` values.  
- Example routes defined in [`route_config_sample.py`](register-route/route_config_sample.py).  
- Supports plugins such as:  
  - `limit-req` (rate limiting)  
  - `cors` (cross-origin support)  
  - `jwt-auth` (JWT authentication)  

---

## ⚡ Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/apisix-docker-setup.git
   cd apisix-docker-setup
   ```

2. **Setup environment variables**
   ```bash
   cp .env.sample .env
   ```
   Edit `.env` as needed (update API keys, ports, etc.).

3. **Start services**
   ```bash
   docker-compose up --build -d
   ```

4. **Access services**
   - APISIX Gateway → http://localhost:9080
   - APISIX Admin API → http://localhost:9180/apisix/admin
   - APISIX Dashboard → http://localhost:9000

5. **Register routes with python**
   The register-route/route_register.py script will POST(it's PUT request btw) predefined routes(from route_config_sample) to APISIX Admin API when started.
   Check logs:
   ```bash
   python register-route/route_register.py
   ```

## 🔑 Configuration

- APISIX Admin Key → set via `.env` (X_API_KEY).
- Dashboard Login → DASHBOARD_USERNAME / DASHBOARD_PASSWORD.
- Route Plugins → customize in register-route/route_config_sample.py.
- Timeouts, CORS, Rate Limits → configurable in `.env` and used in <code>configs.py</code>.

## 🔐 Security Notes

- Change default X_API_KEY, dashboard credentials, and route configs before production.
- Restrict allow_admin IPs in apisix-conf/config.yaml.template (avoid 0.0.0.0/0 in production).
- Use HTTPS (9443) and proper certificates for real deployments.

## 📜 License

This project is licensed under the Apache 2.0 License.

---

✅ With this setup, you can spin up APISIX + Dashboard + Routes in seconds and manage your APIs in a portable, containerized way.