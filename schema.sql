-- Insert code to create Database Schema
-- This will create your .db database file for use
drop table if exists users;
drop table if exists trips;
drop table if exists user_trips;

create table users (
	user_id integer primary key, 
	username text,
	password text
);

create table trips (
	trip_id integer primary key,
	username text,
	destination text,
	trip_name text
);


create table user_trips (
	user_id integer,
	trip_id integer,
	foreign key(user_id) references users(user_id),
	foreign key(trip_id) references trips(trip_id)
);
