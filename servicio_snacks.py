import os.path
from maquina_snacks_proyecto.snack import Snack


class ServicioSnacks:
    NOMBRE_ARQUIVO = 'snacks.txt'

    def __init__(self):
        self.snacks = []
        # revisar si ya existe el archivo snacks
        if os.path.isfile(self.NOMBRE_ARQUIVO):
            self.snacks = self.obtener_snacks()

        #Si ya existe obtenemos los snacks del archivo
        else:
            self.cargar_snacks_iniciales()

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Papas', 70),
            Snack('Refresco', 50),
            Snack('Sandwich', 120),
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARQUIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(f'snack.escribir_snack()\n')

        except Exception as e:
            print(f'Error al guardar snacks en archivo: {e}')

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARQUIVO, 'r') as archivo:
                for linea in archivo:
                    if_snack, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snacks.append(snack)
        except Exception as e:
            print(f'Error al obtener el snacks en archivo: {e}')

        return snacks

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])
    def mostrar_snacks(self):
        print('--- Snacks en el Inventario ---')
        for snack in self.snacks:
            print(snack)
    def get_snacks(self):
        return self.snacks