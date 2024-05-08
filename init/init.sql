CREATE TABLE "Rooms"
(
    id integer NOT NULL,
    room text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Rooms_pkey" PRIMARY KEY (id)
);

CREATE TABLE "Students"
(
    id bigint NOT NULL,
    birthday date,
    first_name text COLLATE pg_catalog."default" NOT NULL,
    room bigint,
    sex "char" NOT NULL,
    second_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Students_pkey" PRIMARY KEY (id),
    CONSTRAINT "FK_Students_Rooms" FOREIGN KEY (room)
        REFERENCES "Rooms" (id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE SET NULL
        NOT VALID
);
