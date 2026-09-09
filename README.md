# Ansible Microservices Platform

A practical enterprise-style Ansible project for deploying a small e-commerce platform.

## Architecture

- `product-service` - FastAPI product API
- `user-service` - FastAPI user API
- `order-service` - FastAPI order API
- Nginx reverse proxy
- MySQL database
- Redis cache
- Prometheus + Grafana monitoring
- Bootstrap web UI dashboard

The application is intentionally small so the focus stays on Ansible.

## UI Dashboard

The project includes a responsive Bootstrap dashboard under `ui/index.html` and the UI is wired to the live FastAPI APIs through Nginx.

![E-Commerce Platform Dashboard](docs/ui-dashboard.svg)

### UI capabilities

- Dashboard metrics loaded from Product, User and Order services
- Product list from MySQL + **Add Product** form
- User list from MySQL + **Add User** form
- Order list from Redis + **Create Order** form
- Monitoring links to Prometheus and Grafana
- Same-origin API calls through Nginx, so no frontend framework or CORS configuration is required

Run the complete local stack:

```bash
docker compose -f docker-compose.yml up --build
```

Then open `http://localhost:8080`.

## API flow

```text
Browser
  │
  ▼
Nginx :8080
  ├── /                 → Bootstrap UI
  ├── /products         → Product Service → MySQL
  ├── /users            → User Service    → MySQL
  └── /orders           → Order Service   → Redis
```

The UI does not talk directly to MySQL or Redis; all data operations go through the FastAPI services.

## Repository goals

This repository demonstrates:

- inventories and environment separation
- group_vars / host_vars
- variables, defaults and facts
- roles, role dependencies and handlers
- templates and Jinja2
- loops, conditionals and registered variables
- `changed_when` / `failed_when`
- `become`, tags and check mode
- `delegate_to`, `run_once`, `serial`
- rolling deployments and health checks
- blocks / rescue / always
- Ansible Vault
- Docker deployment
- Prometheus/Grafana configuration
- backups and rollback
- Molecule, ansible-lint and GitHub Actions
- responsive Bootstrap UI

## Quick local application test

```bash
docker compose -f docker-compose.yml up --build
```

Then:

```bash
curl http://localhost:8080/products
curl http://localhost:8080/users
curl http://localhost:8080/orders/health
```

You can also exercise the UI by adding a product, adding a user, and creating an order from the dashboard.

## Ansible

Install the required collections:

```bash
ansible-galaxy collection install -r requirements.yml
```

Validate the repository:

```bash
ansible-playbook -i inventory/dev/hosts.yml playbooks/site.yml --syntax-check
ansible-playbook -i inventory/dev/hosts.yml playbooks/site.yml --check --diff
ansible-lint .
```

> Secrets are represented only by Vault placeholders. Never commit real passwords, API keys, SSH keys or tokens.
