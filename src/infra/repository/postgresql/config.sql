create schema if not exists ecom;

create table if not exists ecom.coupons (
    code varchar(50) primary key,
    discount_percentage smallint not null,
    expiring_date timestamp not null
);

create table if not exists ecom.orders (
    cpf bigint not null,
    issue_date timestamp not null,
    code varchar(12) primary key,
    id serial,
    coupon_code varchar(50) references ecom.coupons (code),
    shipping_fee decimal(10,2)
);

create table if not exists ecom.products (
    id serial primary key,
    description varchar(100) not null,
    price decimal(10,2) not null,
    height float not null,
    width float not null,
    depth float not null,
    weight float not null,
    info varchar(1000)
);

create table if not exists ecom.order_product (
    product_id integer references ecom.products (id),
    order_code varchar(12) references ecom.orders (code),
    quantity integer default 0,
    price decimal(10,2) not null,
    primary key (product_id, order_code)
);

create table if not exists ecom.stock (
    id serial primary key,
    product_id integer references ecom.products (id),
    out_operation bool not null,
    quantity integer not null,
    date timestamp not null default now()
);

create table if not exists ecom.taxes (
    product_id integer references ecom.products (id),
    type varchar(10) not null,
    value float not null default 0
);

insert into ecom.coupons values ('15OFF', 15, '2050-12-31 23:59:59');

insert into ecom.products (
    description,
    price,
    height,
    width,
    depth,
    weight
) 
values 
    ('book', 19.9, 15, 10, 2, 1000),
    ('pff2 mask', 2.8, 10, 10, 0.01, 50),
    ('vacuum cleaner', 227.9, 40, 30, 30, 5000);

insert into ecom.stock (
    product_id,
    out_operation,
    quantity,
    date
) values 
    (1, false, 100, now()),
    (2, false, 100, now()),
    (3, false, 100, now());

insert into ecom.taxes (product_id, type, value)
values 
    (1, 'default', 0.01),
    (1, 'november', 0.001),
    (2, 'default', 0.001),
    (2, 'november', 0),
    (3, 'default', 0.1),
    (3, 'november', 0.01);
