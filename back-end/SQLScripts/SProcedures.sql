	use TUProfe;

	DELIMITER //
	DROP PROCEDURE IF EXISTS insert_cliente;
	CREATE PROCEDURE insert_cliente(
		IN in_nombre varchar(50), 
		IN in_apellido varchar(50), 
		IN in_mail varchar(100),
		IN in_password varchar(255),
		IN in_telefono varchar(30),
		IN in_descripcion varchar(255))
	BEGIN
		-- chequear que el mail no exista
		IF EXISTS (SELECT * FROM clientes WHERE mail = in_mail) THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El correo electrónico ya existe';
		ELSE
			INSERT INTO clientes (nombre,apellido,mail,password,telefono,descripcion) 
			VALUES (in_nombre,in_apellido,in_mail,in_password,in_telefono,in_descripcion);
		END IF;
	END //
	DELIMITER ;
	DROP PROCEDURE IF EXISTS insert_profesor;
	DELIMITER //
	CREATE PROCEDURE insert_profesor(
		IN in_nombre varchar(50),
		IN in_apellido varchar(50),
		IN in_mail varchar(100),
		IN in_telefono varchar(30),
		IN in_descripcion varchar(255),
		IN in_rrss varchar(255))
	BEGIN
		INSERT INTO profesores (nombre,apellido,mail,telefono,sobre_mi,RRSS)
		VALUES (in_nombre,in_apellido,in_mail,in_telefono,in_descripcion,in_rrss);
	END //
	DELIMITER ;
DROP PROCEDURE IF EXISTS sendfeedback;
DELIMITER //
CREATE PROCEDURE sendfeedback(
    IN in_id_profesor INT,
    IN in_id_cliente INT,
    IN in_comentario VARCHAR(255),
    IN in_claridad_profesor_calif INT,
    IN in_precio_profesor_calif INT,
    IN in_disponibilidad_profesor_calif INT
) 
BEGIN
    -- validar que el profesor y el cliente existan
    IF NOT EXISTS (SELECT * FROM profesores WHERE id_profesor = in_id_profesor) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El profesor no existe';
    ELSEIF NOT EXISTS (SELECT * FROM clientes WHERE id_cliente = in_id_cliente) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El cliente no existe';
    ELSE
        -- insertar esa informacion
		-- valida que el cliente ya no le haya dado feedback al profesor
		IF EXISTS (SELECT * FROM feedbackProfesores WHERE id_profesor = in_id_profesor AND id_cliente = in_id_cliente) THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El cliente ya ha dado feedback a este profesor';
		ELSE
			INSERT INTO feedbackProfesores (id_profesor, id_cliente, comentario, calificacion_gral, claridad_profesor_calif, precio_profesor_calif, disponibilidad_profesor_calif)
			VALUES (in_id_profesor, in_id_cliente, in_comentario, 
			calcular_calificacion(in_claridad_profesor_calif, in_precio_profesor_calif, in_disponibilidad_profesor_calif),
			in_claridad_profesor_calif, in_precio_profesor_calif, in_disponibilidad_profesor_calif);
		END IF;
    END IF;
END //
DELIMITER ;

	

	DROP PROCEDURE IF EXISTS insert_materia;
	DELIMITER //
	CREATE PROCEDURE insert_materia(
		IN in_nombre_materia varchar(100),
		IN in_plan varchar(4),
		IN in_descripcion text
	)
	BEGIN
		-- validar que la materia no exista
		IF EXISTS (SELECT * FROM materias WHERE nombre_materia = in_nombre_materia AND plan = in_plan) THEN
					SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La materia ya existe para el mismo plan';
				ELSE
					INSERT INTO materias (nombre_materia,plan,descripcion)
					VALUES (in_nombre_materia,in_plan,in_descripcion);
				END IF;
		
	END //
	DELIMITER ;
	DROP PROCEDURE IF EXISTS insert_profesor_a_materia;
	DELIMITER //
	CREATE PROCEDURE insert_profesor_a_materia(
		IN in_id_profesor INT,
		IN in_id_materia INT
	)
	BEGIN
		-- Validar que el profesor y la materia existan
		IF NOT EXISTS (SELECT * FROM profesores WHERE id_profesor = in_id_profesor) THEN
				SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El profesor no existe';
			ELSEIF NOT EXISTS (SELECT * FROM materias WHERE id_materia = in_id_materia) THEN
				SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La materia no existe';
			ELSE
				INSERT INTO profesores_materias (id_profesor,id_materia)
				VALUES (in_id_profesor,in_id_materia);
			END IF;
	END //
	DELIMITER ;
	DROP PROCEDURE IF EXISTS delete_profesor;
	DELIMITER //
	CREATE PROCEDURE delete_profesor(
		IN in_id_profesor INT
	)
	BEGIN
		-- Validar que el profesor exista
		IF NOT EXISTS (SELECT * FROM profesores WHERE id_profesor = in_id_profesor) THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El profesor no existe';
		ELSE
			DELETE FROM profesores WHERE id_profesor = in_id_profesor;
		END IF;
	END //
	DELIMITER ;
	DROP PROCEDURE IF EXISTS delete_cliente;
	DELIMITER //
	CREATE PROCEDURE delete_cliente(
		IN in_id_cliente INT
	)
	BEGIN
		-- Validar que el cliente exista
		IF NOT EXISTS (SELECT * FROM clientes WHERE id_cliente = in_id_cliente) THEN
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El cliente no existe';
		ELSE
			DELETE FROM clientes WHERE id_cliente = in_id_cliente;
		END IF;
	END //
	DELIMITER ;

