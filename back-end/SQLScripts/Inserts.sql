delete from feedbackprofesores;
delete from profesores_materias;
delete from materias;
delete from clientes;
delete from profesores;

-- INSERCIONES DE MATERIAS PLAN 2023 DE LA TUP FRBB, CON SUS RESPECTIVOS TEMAS.

CALL TUProfe.insert_materia('Matemática', '2023', 'Números reales, funciones, límites, derivadas, integrales, álgebra lineal, ecuaciones diferenciales.');
CALL TUProfe.insert_materia('Estadística', '2023', 'Datos estadísticos, análisis combinatorio, estadística descriptiva, teoría de las probabilidades, variables aleatorias, distribuciones de probabilidad, teoría del muestreo, estimación.');
CALL TUProfe.insert_materia('Programación I', '2023', 'Introducción a los distintos paradigmas de programación, programación imperativa, concepto de algoritmo, estrategias de resolución de problemas, tipos de datos, variables y constantes, estructuras de control básicas, estructuras de datos, abstracciones con procedimientos y funciones, recursividad, algoritmos de búsqueda, recorrido y ordenamiento.');
CALL TUProfe.insert_materia('Arquitectura y Sistemas Operativos', '2023', 'Arquitectura de computadoras, estructura, características y clasificación de sistemas operativos, planificación e hilos en procesos, comunicación y sincronización entre procesos, gestión de memoria, sistemas de archivos, gestión de entrada/salida, interrupciones, introducción a las redes de datos, virtualización.');
CALL TUProfe.insert_materia('Programación II', '2023', 'Principios de la orientación a objetos, clases, atributos y métodos, constructores, enumeraciones, arreglos y colecciones, acceso a datos, gestión de altas, bajas, modificación y consultas (ABMC), introducción a servicios web.');
CALL TUProfe.insert_materia('Base de Datos I', '2023', 'Modelo conceptual de datos, modelo relacional, sistema de gestión de bases de datos relacional, diseño de base de datos, sentencias SQL para insertar, eliminar y actualizar datos, análisis de consistencia e integridad de datos, seguridad y privacidad en bases de datos.');
CALL TUProfe.insert_materia('Programación III', '2023', 'Autenticación por medios externos, aplicación de base de datos en tiempo real, programación del lado del cliente, programación del lado del servidor y comunicación con el cliente, arquitectura cliente-servidor.');
CALL TUProfe.insert_materia('Base de Datos II', '2023', 'Gestión avanzada de bases de datos, transacciones, concurrencia, recuperación ante fallos, optimización de consultas, administración de bases de datos, técnicas de replicación y particionamiento.');
CALL TUProfe.insert_materia('Metodología de Sistemas I', '2023', 'Análisis y diseño de sistemas de información, metodologías de desarrollo, modelos de ciclo de vida, herramientas CASE, documentación y especificaciones.');
CALL TUProfe.insert_materia('Programación IV', '2023', 'Desarrollo de aplicaciones distribuidas, programación concurrente, programación paralela, diseño y análisis de algoritmos, optimización de rendimiento.');
CALL TUProfe.insert_materia('Metodología de Sistemas II', '2023', 'Introducción a los patrones de diseño y desarrollo de software, buenas prácticas en el proceso de implementación de software, técnicas de optimización del ciclo de desarrollo de software, herramientas de verificación y validación en el desarrollo de software, herramientas de repositorios de software.');
CALL TUProfe.insert_materia('Gestión de Desarrollo de Software', '2023', 'Software. Proceso. Producto. Ingeniería de Requerimientos, propuesta de proyecto, descripción, objetivos, alcance, inclusiones, exclusiones, registro de interesados, criterios de aceptación, supuestos y restricciones del proyecto, estimación de tiempos y costos en proyectos de tecnologías de la información, calendarización del proyecto, cronograma de hitos del proyecto, definición de las iteraciones del proyecto, artefactos técnicos requeridos, reportes, indicadores, estadísticas, manuales e instructivos.');
CALL TUProfe.insert_materia('Introducción al Análisis de Datos', '2023', 'Introducción al análisis de datos, herramientas de análisis de datos, modelado de datos, aplicaciones del análisis de datos.');
CALL TUProfe.insert_materia('Inglés I', '2023', 'Lectura y comprensión de textos técnicos en inglés, vocabulario técnico, estructuras gramaticales, redacción de informes y documentos técnicos.');
CALL TUProfe.insert_materia('Inglés II', '2023', 'Avanzado de lectura y comprensión de textos técnicos en inglés, vocabulario técnico avanzado, estructuras gramaticales complejas, redacción avanzada de informes y documentos técnicos, presentación oral de temas técnicos.');
CALL TUProfe.insert_materia('Organización Empresarial', '2023', 'Teoría general de sistemas, información, conocimiento y toma de decisiones, organización y empresa, sistemas administrativos y contables, planificación, organización, dirección y control, gestión por procesos.');
CALL TUProfe.insert_materia('Legislación', '2023', 'Introducción al derecho y a las sociedades, legislación laboral, derecho informático y propiedad intelectual, responsabilidades civiles, penales y profesionales relacionadas con el desarrollo de software, actuación de los técnicos universitarios en programación durante los procesos judiciales, seguridad de la información.');

-- INSERCIOES DE MATERIAS PLAN 2003 DE LA TUP FRBB, CON SUS RESPECTIVOS TEMAS

-- INSERCIONES DE CLIENTES RANDOM
-- Se hace mediante el archivo de carga de datos de prueba con ipynb

-- INSERCIONES DE PROFESORES RANDOM
-- CALL TUProfe.insert_profesor((nombre,apellido,mail,telefono,sobre_mi,RRSS)); 10 asi
CALL TUProfe.insert_profesor('Juan', 'Pérez', 'juan.perez@example.com', '1234567890', 'Sobre mí...', 'Twitter.com/pepe');
CALL TUProfe.insert_profesor('Ana', 'Gómez', 'ana.gomez@example.com', '0987654321', 'Sobre mí...', 'Facebook/pepe');
CALL TUProfe.insert_profesor('Luis', 'Martínez', 'luis.martinez@example.com', '1122334455', 'Sobre mí...', 'Instagram/papa');
CALL TUProfe.insert_profesor('Sofía', 'López', 'sofia.lopez@example.com', '5566778899', 'Sobre mí...', 'LinkedIn/sofia');
CALL TUProfe.insert_profesor('Carlos', 'Hernández', 'carlos.hernandez@example.com', '2233445566', 'Sobre mí...', 'Twitter/carlos');
CALL TUProfe.insert_profesor('Lucía', 'Jiménez', 'lucia.jimenez@example.com', '6677889900', 'Sobre mí...', 'Facebook/lucia');
CALL TUProfe.insert_profesor('Marco', 'Ruiz', 'marco.ruiz@example.com', '7788990011', 'Sobre mí...', 'Instagram/marco');
CALL TUProfe.insert_profesor('Elena', 'Morales', 'elena.morales@example.com', '8899001122', 'Sobre mí...', 'LinkedIn/elena');
CALL TUProfe.insert_profesor('Pablo', 'Navarro', 'pablo.navarro@example.com', '9900112233', 'Sobre mí...', 'Twitter/Pablo');
CALL TUProfe.insert_profesor('Marta', 'Díaz', 'marta.diaz@example.com', '0011223344', 'Sobre mí...', 'Facebook/Marta');


-- INSERTAR PROFESORES A MATERIAS
-- CALL TUProfe.insert_profesor_a_materia(id_profesor_existente, id_materia_existente); 
CALL TUProfe.insert_profesor_a_materia(1, 1);
CALL TUProfe.insert_profesor_a_materia(2, 2);
CALL TUProfe.insert_profesor_a_materia(3, 3);
CALL TUProfe.insert_profesor_a_materia(4, 4);
CALL TUProfe.insert_profesor_a_materia(5, 5);
CALL TUProfe.insert_profesor_a_materia(6, 6);
CALL TUProfe.insert_profesor_a_materia(7, 7);
CALL TUProfe.insert_profesor_a_materia(8, 8);
CALL TUProfe.insert_profesor_a_materia(9, 9);
CALL TUProfe.insert_profesor_a_materia(10, 10);
CALL TUProfe.insert_profesor_a_materia(1, 11);
CALL TUProfe.insert_profesor_a_materia(2, 12);
CALL TUProfe.insert_profesor_a_materia(3, 13);
CALL TUProfe.insert_profesor_a_materia(4, 14);
CALL TUProfe.insert_profesor_a_materia(5, 15);
CALL TUProfe.insert_profesor_a_materia(6, 16);
CALL TUProfe.insert_profesor_a_materia(7, 17);
CALL TUProfe.insert_profesor_a_materia(8, 3);
CALL TUProfe.insert_profesor_a_materia(9, 2);
CALL TUProfe.insert_profesor_a_materia(10, 1);


-- INSERTAR FEEDBACKS DE PROFESORES
-- CALL TUProfe.sendfeedback(id_profesor, id_cliente, comentario, calificacion_gral, claridad_profesor_calif, precio_profesor_calif, disponibilidad_profesor_calif);
CALL TUProfe.sendfeedback(1, 1, 'Excelente profesor, muy recomendable.', 5, 5, 5);
CALL TUProfe.sendfeedback(2, 2, 'Muy buen profesor, excelente trato.', 4, 5, 4);
CALL TUProfe.sendfeedback(3, 3, 'Muy buen profesor, excelente trato.', 3, 5, 3);
CALL TUProfe.sendfeedback(4, 4, 'Muy poco contenido de calidad pero excelente trato.', 4, 2, 4);
CALL TUProfe.sendfeedback(1,2,'Buen trato',4,3,1);
