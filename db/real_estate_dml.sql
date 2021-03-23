-- users
insert into users (id, email, hashed_password, phone, is_active) values (1, 'jon@test.com', '12345', '407-555-8513', 1);

-- listings
insert into listings (id, title, price, address, city, state, zip, views, owner_id) values (1, 'Lake house', 150000, '123 Street St', 'Tampa', 'FL', '33163', 0, 1);
insert into listings (id, title, price, address, city, state, zip, views, owner_id) values (2, 'Beach house', 150000, '123 Avenue Ave', 'Orlando', 'FL', '32714', 0, 1);

-- photos
insert into photos (id, listing_id, src) values (1, 1, '/var/www/html/images/lake-house.jpg';
insert into photos (id, listing_id, src) values (2, 1, '/var/www/html/images/lake-house-bathroom.jpg';
insert into photos (id, listing_id, src) values (3, 2, '/var/www/html/images/beach-house.jpg';
insert into photos (id, listing_id, src) values (4, 2, '/var/www/html/images/beach-house-kitchen.jpg';
insert into photos (id, listing_id, src) values (5, 2, '/var/www/html/images/beach-house-porch.jpg';