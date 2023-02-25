--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 14.5

-- Started on 2023-02-25 19:35:51

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 25058)
-- Name: game_sessions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_sessions (
    id bigint NOT NULL,
    first_player_id bigint NOT NULL,
    second_player_id bigint NOT NULL,
    start_date date NOT NULL,
    start_time time without time zone NOT NULL,
    status boolean DEFAULT false NOT NULL
);


ALTER TABLE public.game_sessions OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 25056)
-- Name: game_sessions_first_player_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.game_sessions_first_player_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_sessions_first_player_id_seq OWNER TO postgres;

--
-- TOC entry 3342 (class 0 OID 0)
-- Dependencies: 212
-- Name: game_sessions_first_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.game_sessions_first_player_id_seq OWNED BY public.game_sessions.first_player_id;


--
-- TOC entry 211 (class 1259 OID 25055)
-- Name: game_sessions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.game_sessions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_sessions_id_seq OWNER TO postgres;

--
-- TOC entry 3343 (class 0 OID 0)
-- Dependencies: 211
-- Name: game_sessions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.game_sessions_id_seq OWNED BY public.game_sessions.id;


--
-- TOC entry 213 (class 1259 OID 25057)
-- Name: game_sessions_second_player_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.game_sessions_second_player_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.game_sessions_second_player_id_seq OWNER TO postgres;

--
-- TOC entry 3344 (class 0 OID 0)
-- Dependencies: 213
-- Name: game_sessions_second_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.game_sessions_second_player_id_seq OWNED BY public.game_sessions.second_player_id;


--
-- TOC entry 215 (class 1259 OID 25083)
-- Name: game_storage; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.game_storage (
    id bigint NOT NULL,
    game_session_id bigint NOT NULL,
    end_date date NOT NULL,
    end_time time without time zone NOT NULL,
    result text,
    history text
);


ALTER TABLE public.game_storage OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 25026)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id bigint NOT NULL,
    username character varying(16) NOT NULL,
    password character varying(128) NOT NULL,
    secret_question character varying(128) NOT NULL,
    answer character varying(16) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 25029)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 3345 (class 0 OID 0)
-- Dependencies: 210
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3176 (class 2604 OID 25061)
-- Name: game_sessions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sessions ALTER COLUMN id SET DEFAULT nextval('public.game_sessions_id_seq'::regclass);


--
-- TOC entry 3177 (class 2604 OID 25062)
-- Name: game_sessions first_player_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sessions ALTER COLUMN first_player_id SET DEFAULT nextval('public.game_sessions_first_player_id_seq'::regclass);


--
-- TOC entry 3178 (class 2604 OID 25063)
-- Name: game_sessions second_player_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sessions ALTER COLUMN second_player_id SET DEFAULT nextval('public.game_sessions_second_player_id_seq'::regclass);


--
-- TOC entry 3175 (class 2604 OID 25030)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3335 (class 0 OID 25058)
-- Dependencies: 214
-- Data for Name: game_sessions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.game_sessions (id, first_player_id, second_player_id, start_date, start_time, status) FROM stdin;
\.


--
-- TOC entry 3336 (class 0 OID 25083)
-- Dependencies: 215
-- Data for Name: game_storage; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.game_storage (id, game_session_id, end_date, end_time, result, history) FROM stdin;
\.


--
-- TOC entry 3330 (class 0 OID 25026)
-- Dependencies: 209
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, password, secret_question, answer) FROM stdin;
8	lo	21414	Favorite day of the week? 	Wednesday
9	Никнейм	123	Что? 	Что?
10	Ник	new_amesome_password	Что? 	Что?
11	TEST	new_password	question	answer
\.


--
-- TOC entry 3346 (class 0 OID 0)
-- Dependencies: 212
-- Name: game_sessions_first_player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.game_sessions_first_player_id_seq', 1, false);


--
-- TOC entry 3347 (class 0 OID 0)
-- Dependencies: 211
-- Name: game_sessions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.game_sessions_id_seq', 1, false);


--
-- TOC entry 3348 (class 0 OID 0)
-- Dependencies: 213
-- Name: game_sessions_second_player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.game_sessions_second_player_id_seq', 1, false);


--
-- TOC entry 3349 (class 0 OID 0)
-- Dependencies: 210
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 11, true);


--
-- TOC entry 3185 (class 2606 OID 25066)
-- Name: game_sessions game_sessions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sessions
    ADD CONSTRAINT game_sessions_pkey PRIMARY KEY (id);


--
-- TOC entry 3187 (class 2606 OID 25089)
-- Name: game_storage game_storage_id_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_storage
    ADD CONSTRAINT game_storage_id_pk PRIMARY KEY (id);


--
-- TOC entry 3181 (class 2606 OID 25082)
-- Name: users username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT username_key UNIQUE (username);


--
-- TOC entry 3183 (class 2606 OID 25068)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3188 (class 2606 OID 25069)
-- Name: game_sessions first_player_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sessions
    ADD CONSTRAINT first_player_id_fk FOREIGN KEY (first_player_id) REFERENCES public.users(id) NOT VALID;


--
-- TOC entry 3190 (class 2606 OID 25090)
-- Name: game_storage game_session_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_storage
    ADD CONSTRAINT game_session_id_fk FOREIGN KEY (game_session_id) REFERENCES public.game_sessions(id);


--
-- TOC entry 3189 (class 2606 OID 25074)
-- Name: game_sessions second_player_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.game_sessions
    ADD CONSTRAINT second_player_id_fk FOREIGN KEY (second_player_id) REFERENCES public.users(id) NOT VALID;


-- Completed on 2023-02-25 19:35:51

--
-- PostgreSQL database dump complete
--

