USE TUProfe;

DROP VIEW IF EXISTS calificaciones_profesores;
CREATE VIEW calificaciones_profesores AS (
    SELECT id_profesor, AVG(calificacion_gral) as calificacion_promedio
    FROM feedbackProfesores
    GROUP BY id_profesor
);

DROP VIEW IF EXISTS info_profesores_materias;
CREATE VIEW info_profesores_materias AS (
    SELECT pm.id_materia,pm.id_profesor,m.nombre_materia,m.plan,
		   concat(p.nombre,' ',p.apellido) as Profesor,
		   p.mail,p.telefono,p.sobre_mi,p.RRSS
	FROM profesores_materias pm
	JOIN materias m ON m.id_materia = pm.id_materia
	JOIN profesores p ON p.id_profesor = pm.id_profesor
);



