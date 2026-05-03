CREATE DATABASE IF NOT EXISTS cyber_attack_analysis;
USE cyber_attack_analysis;

CREATE TABLE IF NOT EXISTS cyber_attacks (
    attack_id INT PRIMARY KEY,
    country VARCHAR(50),
    industry VARCHAR(50),
    attack_type VARCHAR(50),
    year INT,
    financial_loss FLOAT,
    records_stolen INT
);