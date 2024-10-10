CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    creation_date TIMESTAMP
);

INSERT INTO students (name, email, creation_date) VALUES
('John Doe', 'johndoe@example.com', NOW()),
('Jane Smith', 'janesmith@example.com', NOW()),
('Alice Johnson', 'alicejohnson@example.com', NOW());
