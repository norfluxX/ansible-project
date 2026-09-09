CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  price DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE
);

INSERT INTO products (name, price) VALUES ('Keyboard', 49.99), ('Mouse', 19.99);
INSERT INTO users (name, email) VALUES ('Demo User', 'demo@example.com');
