#ejercicio numero 1
cursos_min = 2.5
cursos_prom = 4
cursos_max = 7
curso_dalto = 1.5

print('---------------')


print('el curso de dalto dura un')
dif_cursos_min = 100 - curso_dalto/cursos_min  * 100
print(f'{dif_cursos_min}% menos que el mas rapido')
dif_cursos_prom = 100 - curso_dalto/cursos_prom  * 100
print(f'{dif_cursos_prom}% menos que el promedio')
dif_cursos_max = 100 - curso_dalto * 1000//cursos_max /10
print(f'{dif_cursos_max}% menos que el curso mas lento')


#crudo video dalto
print('---------------')
crudo_promedio = 5
crudo_dalto = 3.5

dif_cursos_promedios = 100 - cursos_prom * 1000// crudo_promedio /10
print(f'el curso promedio elimino un {dif_cursos_promedios}% del video')
dif_cursos_dalto = 100 - curso_dalto *1000 // crudo_dalto /10
print(f'el curso dalto elimino un {dif_cursos_dalto}% del video')


#mostrando diferencias si los cursos duraran 10 horas
print('---------------')

print('Ver 10 horas equivale a')
print(f'Equivale a un {cursos_prom *100 // curso_dalto /10} horas de curso')
print(f'Equivale a un {curso_dalto *100 // cursos_prom /10} horas de curso')
