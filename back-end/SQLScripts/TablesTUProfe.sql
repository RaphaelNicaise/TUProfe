DROP SCHEMA IF EXISTS TUprofe;
CREATE SCHEMA IF NOT EXISTS TUProfe;
use TUProfe;

-- drop de todas las tablas
drop table if exists feedbackProfesores;
drop table if exists profesores_materias;
drop table if exists materias;
drop table if exists clientes;
drop table if exists profesores;

create table if not exists clientes (
	id_cliente int auto_increment,
	nombre varchar(50) not null,
	apellido varchar(50) not null,
	mail varchar(100) not null,
    password varchar(255) not null, -- Se van a guardar hasheadas
	telefono varchar(30),
	descripcion varchar(255),
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	primary key (id_cliente)
);

create table if not exists profesores (
	id_profesor int auto_increment,
	nombre varchar(50) not null,
	apellido varchar(50) not null,
	mail varchar(100) not null,
	telefono varchar(30),
	sobre_mi varchar(255) not null,
    foto_de_perfil LONGBLOB,
    RRSS varchar(255),
    fecha_inscripcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    primary key (id_profesor)
);

create table materias (
	id_materia int auto_increment,
    nombre_materia varchar(100) not null,
    plan varchar(4),
    descripcion text,
    primary key (id_materia)
);
create table profesores_materias (
	id_materia int not null,
    id_profesor int not null,
    CONSTRAINT fk_materia_profesor FOREIGN KEY (id_materia) REFERENCES materias(id_materia),
    CONSTRAINT fk_profesor_materia FOREIGN KEY (id_profesor) REFERENCES profesores(id_profesor)
);

create table feedbackProfesores (
	id_feedback int auto_increment,
    id_profesor int not null,
    id_cliente int not null,
    comentario text,
    calificacion_gral float check (calificacion_gral <=5 and calificacion_gral >= 0), -- se da el insert solo si esta entre 0 y 5
	claridad_profesor_calif int check (claridad_profesor_calif <=5 and claridad_profesor_calif >= 0),
    precio_profesor_calif  int check (precio_profesor_calif <= 5 and precio_profesor_calif >= 0),
    disponibilidad_profesor_calif int check (disponibilidad_profesor_calif <= 5 and disponibilidad_profesor_calif >= 0),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    primary key (id_feedback),
    constraint fk_profesor FOREIGN KEY (id_profesor) REFERENCES profesores(id_profesor),
    constraint fk_cliente FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)   
);

-- creacion de indices para distintos campos, para mejorar el rendimiento de las consultas

CREATE INDEX idx_clientes_nombre ON clientes (nombre);
CREATE INDEX idx_clientes_apellido ON clientes (apellido);
CREATE INDEX idx_clientes_mail ON clientes (mail);
CREATE INDEX idx_profesores_nombre ON profesores (nombre);
CREATE INDEX idx_profesores_apellido ON profesores (apellido);
CREATE INDEX idx_profesores_mail ON profesores (mail);
CREATE INDEX idx_materias_nombre_materia ON materias (nombre_materia);
CREATE INDEX idx_profesores_materias_id_materia ON profesores_materias (id_materia);
CREATE INDEX idx_profesores_materias_id_profesor ON profesores_materias (id_profesor);
CREATE INDEX idx_feedbackProfesores_id_profesor ON feedbackProfesores (id_profesor);
CREATE INDEX idx_feedbackProfesores_id_cliente ON feedbackProfesores (id_cliente);

