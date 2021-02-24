create database real_estate;

create table listings {

	listing_id int auto_increment not null,
	owner_id int not null,
	address_id int not null,
	listed_date date not null,
	description varchar(300),
	arrangements varchar(100),
	price float,
	primary key (listing_id),
	foreign key (owner_id) references owners(owner_id),
	foreign key (address_id) references addresses(address_id)

}

create table owners {

	owner_id int auto_increment not null,
	first_name varchar(30) not null,
	last_name varchar(30) not null,
	email varchar(40),
	phone_number varchar(15)
	primary key (owner_id)
	
}

create table addresses {

	address_id int auto_increment not null,
	address varchar(50) not null,
	city varchar(40) not null,
	state varchar(2) not null,
	zip varchar(12) not null,
	primary key (address_id)

}

create user 'administrator' identified by 'password';
grant select on real_estate to 'administrator';
grant drop on real_estate to 'administrator';

create user 'user' identified by 'password';
grant select on listings to 'user';
