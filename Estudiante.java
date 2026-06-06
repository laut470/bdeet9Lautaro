import java.util.Scanner;

public class Estudiante {
    private String nombre;
    private int edad;
    private double promedio;
    private boolean activo;

    public Estudiante(String nombre, int edad, double promedio, boolean activo) {
        this.nombre = nombre;
        this.edad = edad;
        this.promedio = promedio;
        this.activo = activo;
    }

    public void mostrarDatos() {
        System.out.println("\nDatos del estudiante:");
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Promedio: " + promedio);
        System.out.println("Activo: " + (activo ? "Sí" : "No"));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=== Gestor de Datos de Estudiante - Java ===");

        System.out.print("Ingrese el nombre: ");
        String nombre = scanner.nextLine();
        
        System.out.print("Ingrese la edad: ");
        int edad = scanner.nextInt();
        
        System.out.print("Ingrese el promedio: ");
        double promedio = scanner.nextDouble();
        
        scanner.nextLine(); // consume newline
        System.out.print("¿Está activo? (si/no): ");
        boolean activo = scanner.nextLine().trim().equalsIgnoreCase("si") || 
                        scanner.nextLine().trim().equalsIgnoreCase("sí");

        Estudiante est = new Estudiante(nombre, edad, promedio, activo);
        est.mostrarDatos();

        // Operaciones
        est.edad++;
        int promEntero = (int) Math.round(est.promedio);
        String estado = est.activo ? "Activo" : "Inactivo";

        System.out.println("\nDespués de operaciones:");
        System.out.println("Edad incrementada: " + est.edad);
        System.out.println("Promedio redondeado: " + promEntero);
        System.out.println("Estado: " + estado);

        // Tipos
        System.out.println("\nTipos de datos:");
        System.out.println("Nombre: String");
        System.out.println("Edad: int");
        System.out.println("Promedio: double");
        System.out.println("Activo: boolean");

        // Casos
        System.out.println("\nCasos especiales:");
        double dec = 20.5;
        int ent = (int) dec;
        System.out.println("Asignar decimal a entero (casting): " + ent);

        try {
            // No direct sum in Java
            System.out.println("Sumar número + string: Requiere concatenación o parseo.");
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }

        // Local variable must be initialized
        // int sinInit; // Error if used without init
        System.out.println("Variable local sin inicializar: Error de compilación en Java.");

        scanner.close();
    }
}