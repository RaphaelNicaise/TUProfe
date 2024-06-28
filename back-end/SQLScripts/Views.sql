USE TUProfe;

DROP VIEW IF EXISTS calificaciones_profesores;
CREATE VIEW calificaciones_profesores AS (
    SELECT id_profesor, AVG(calificacion) as calificacion_promedio
    FROM feedbackProfesores
    GROUP BY id_profesor
);