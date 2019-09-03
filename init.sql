CREATE USER aidooit;
CREATE DATABASE aidooit;
GRANT ALL PRIVILEGES ON DATABASE aidooit TO aidooit;
\c aidooit
CREATE TABLE IF NOT EXISTS login_data
(
    id SERIAL PRIMARY KEY,
    code TEXT NOT NULL,
    login_date TEXT NOT NULL
);
