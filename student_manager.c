#include <stdio.h>
#include <string.h>

struct Estudiante {
    char nombre[100];
    int edad;
    float promedio;
    int activo; // 1 true, 0 false
};

int main() {
    struct Estudiante est;
    
    printf("=== Gestor de Datos de Estudiante - C ===\n");
    
    printf("Ingrese el nombre: ");
    fgets(est.nombre, 100, stdin);
    est.nombre[strcspn(est.nombre, "\n")] = 0; // remove newline
    
    printf("Ingrese la edad: ");
    scanf("%d", &est.edad);
    
    printf("Ingrese el promedio: ");
    scanf("%f", &est.promedio);
    
    char activo_str[10];
    printf("¿Está activo? (si/no): ");
    scanf("%s", activo_str);
    est.activo = (strcmp(activo_str, "si") == 0 || strcmp(activo_str, "sí") == 0);
    
    // Mostrar datos
    printf("\nDatos del estudiante:\n");
    printf("Nombre: %s\n", est.nombre);
    printf("Edad: %d\n", est.edad);
    printf("Promedio: %.2f\n", est.promedio);
    printf("Activo: %s\n", est.activo ? "Sí" : "No");
    
    // Operaciones
    est.edad++;
    int prom_entero = (int)(est.promedio + 0.5);
    char* estado = est.activo ? "Activo" : "Inactivo";
    
    printf("\nDespués de operaciones:\n");
    printf("Edad incrementada: %d\n", est.edad);
    printf("Promedio redondeado: %d\n", prom_entero);
    printf("Estado: %s\n", estado);
    
    // Tipos (sizeof)
    printf("\nTamaños (sizeof):\n");
    printf("Nombre: %zu bytes\n", sizeof(est.nombre));
    printf("Edad: %zu bytes\n", sizeof(est.edad));
    printf("Promedio: %zu bytes\n", sizeof(est.promedio));
    printf("Activo: %zu bytes\n", sizeof(est.activo));
    
    // Casos
    printf("\nCasos especiales:\n");
    float dec = 20.5;
    int entero = (int)dec;
    printf("Asignar decimal a entero: %d (con casting)\n", entero);
    
    // Sumar numero + string not possible easily
    printf("Sumar número + string: No directo, requiere manejo manual.\n");
    
    // Variable sin inicializar
    int sin_init;
    printf("Variable sin inicializar: valor garbage %d (undefined behavior)\n", sin_init);
    
    return 0;
}