-- 기본 Label 데이터 삽입
INSERT INTO label (name) VALUES
('Friend'),
('Family'),
('Work'),
('Colleague');

-- 기본 Contact 데이터 삽입
INSERT INTO contact (name, email, phone_number, profile_picture, company, position, memo, address, birthday, website) VALUES
('John Doe', 'john.doe@example.com', '1234567890', 'http://example.com/profile.jpg', 'Example Corp', 'Engineer', 'No memo', '123 Main St', '1985-01-01', 'http://example.com'),
('Jane Smith', 'jane.smith@example.com', '0987654321', 'http://example.com/profile2.jpg', 'Another Corp', 'Manager', 'No memo', '456 Elm St', '1990-05-15', 'http://example.com');

-- 기본 Contact-Label 관계 데이터 삽입
INSERT INTO contact_labels (contact_id, label_id) VALUES (1, 1), (1, 4), (2, 2), (2, 3);
