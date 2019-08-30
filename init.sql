CREATE USER aidooit;
CREATE DATABASE aidooit;
GRANT ALL PRIVILEGES ON DATABASE aidooit TO aidooit;
\c aidooit
CREATE TABLE IF NOT EXISTS login_data
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    mobile TEXT NOT NULL,
    code TEXT NOT NULL
);
