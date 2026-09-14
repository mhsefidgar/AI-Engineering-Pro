-- Hands-on PostgreSQL lab: users, projects, and API requests
CREATE TABLE users (
  id BIGSERIAL PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  display_name TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE projects (
  id BIGSERIAL PRIMARY KEY,
  owner_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(owner_id, name)
);

CREATE TABLE api_requests (
  id BIGSERIAL PRIMARY KEY,
  user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
  request_id UUID NOT NULL,
  route TEXT NOT NULL,
  status_code INT NOT NULL CHECK (status_code BETWEEN 100 AND 599),
  latency_ms INT NOT NULL CHECK (latency_ms >= 0),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_projects_owner ON projects(owner_id);
CREATE INDEX idx_api_requests_created_at ON api_requests(created_at DESC);
CREATE INDEX idx_api_requests_route_created_at ON api_requests(route, created_at DESC);

-- Exercises:
-- 1. Insert three users and projects.
-- 2. Write a join returning project owner email.
-- 3. Use EXPLAIN ANALYZE on a recent-request query.
-- 4. Add pagination with created_at + id keyset ordering.
-- 5. Write a transaction that creates a project and audit event atomically.