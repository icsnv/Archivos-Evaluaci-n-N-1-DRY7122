import yaml
datos = {
    'persona': [
        {'nombre': 'Ignacio'},
        {'apellido': 'Casanova'}
    ]
}
cadena_yaml = yaml.dump(datos)
print(cadena_yaml)
