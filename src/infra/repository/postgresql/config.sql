create schema if not exists ecom;

create table if not exists ecom.coupons (
    code varchar(50) primary key,
    discount_percentage smallint,
    expiring_date timestamp
);

create table if not exists ecom.orders (
    cpf bigint,
    issue_date timestamp,
    code varchar(12) primary key,
    id serial,
    coupon_code varchar(50) references ecom.coupons (code),
    shipping_fee decimal(10,2)
);

create table if not exists ecom.products (
    id serial primary key,
    description varchar(100),
    price decimal(10,2),
    info varchar(1000),
    volume float,
    density float
);

create table if not exists order_product (
    product_id integer references ecom.products (id),
    order_code varchar(12) references ecom.orders (code),
    quantity integer,
    price decimal(10,2),
    primary key (product_id, order_code)
);

create table if not exists stock (
    id serial primary key,
    product_id integer references ecom.products (id),
    quantity integer,
    date timestamp
);

create table if not exists taxes (
    product_id integer references ecom.products (id),
    type varchar(10),
    value float
);
