-- Label 테이블 생성
CREATE TABLE IF NOT EXISTS label (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Contact 테이블 생성
CREATE TABLE IF NOT EXISTS contact (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    profile_picture VARCHAR(200),
    company VARCHAR(255),
    position VARCHAR(255),
    memo TEXT,
    address VARCHAR(255),
    birthday DATE,
    website VARCHAR(200),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- M2M 테이블 생성
CREATE TABLE IF NOT EXISTS contact_labels (
    contact_id INTEGER NOT NULL REFERENCES contact(id) ON DELETE CASCADE,
    label_id INTEGER NOT NULL REFERENCES label(id) ON DELETE CASCADE,
    PRIMARY KEY (contact_id, label_id)
);
