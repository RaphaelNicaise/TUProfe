delimiter //
CREATE FUNCTION calcular_calificacion(claridad_profesor_calif INT, precio_profesor_calif INT, disponibilidad_profesor_calif INT)
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE calificacion DECIMAL(10,2);
    SET calificacion = (claridad_profesor_calif + precio_profesor_calif + disponibilidad_profesor_calif) / 3;
    RETURN calificacion;
END // 
delimiter ;