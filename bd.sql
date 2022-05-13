-- Table: public.p2p_prices

-- DROP TABLE IF EXISTS public.p2p_prices;

CREATE TABLE IF NOT EXISTS public.p2p_prices
(
    crypto character varying COLLATE pg_catalog."default" NOT NULL,
    fiat character varying COLLATE pg_catalog."default" NOT NULL,
    value real NOT NULL,
    date date NOT NULL,
    CONSTRAINT p2p_prices_pkey PRIMARY KEY (fiat)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.p2p_prices
    OWNER to p2p;

-- FUNCTION: public.act_prices(character, character, numeric)

-- DROP FUNCTION IF EXISTS public.act_prices(character, character, numeric);

CREATE OR REPLACE FUNCTION public.act_prices(
	pcrypto character,
	pfiat character,
	pamount numeric)
    RETURNS void
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
declare
lastamount double precision;
vlbehavior character(30);
vlcolor character(30);
/**
Mantiene actualizada la tabla p2p_prices
GLOBAL DVCONSULTORES /Andrés Dominguez 12/05/2022
*/
begin
--borra el registro y lo vuelve a cargar
delete from p2p_prices where crypto = pcrypto and fiat = pfiat;
--Inserta registros
insert into p2p_prices (crypto, fiat, value, date) values (pcrypto, pfiat, pamount, now());
end;
$BODY$;

ALTER FUNCTION public.act_prices(character, character, numeric)
    OWNER TO p2p;

COMMENT ON FUNCTION public.act_prices(character, character, numeric)
    IS 'Mantiene act_prices';
