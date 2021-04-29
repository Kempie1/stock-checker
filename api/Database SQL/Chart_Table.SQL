-- auto-generated definition
create table chart
(
    ticker_symbol varchar(255) not null
        constraint chart_ticker_symbol_fkey
            references stock,
    time          integer,
    open          numeric,
    volume        numeric,
    low           numeric,
    high          numeric,
    close         numeric
);

alter table chart
    owner to oscwgisbzpavqv;

