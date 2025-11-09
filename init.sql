CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO users (username) VALUES
  ('devops_user'),
  ('admin_user'),
  ('test_user')
ON CONFLICT (username) DO NOTHING;