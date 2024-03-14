#Para jugar con las tablas


'''Efectivamente, en situaciones normales, cuando usas la función print en Python, la salida se almacena en un búfer interno
 antes de mostrarse en la consola. Con el parámetro end=' ' en tu primera declaración print, estás diciéndole a Python que 
 agregue un espacio al final en lugar de un salto de línea. Esto significa que la salida está en el búfer hasta que se completa
 con un salto de línea o hasta que se vacía explícitamente.

Sin embargo, cuando agregas un retraso de tiempo y luego usas la función print para mostrar el resultado del cálculo,
la salida del primer print puede no aparecer de inmediato en la consola si el búfer no se vacía antes de que se imprima
el resultado. Al usar flush=True, estás forzando a que la salida se muestre de inmediato, evitando cualquier posible demora
en la visualización de la información en la consola. Esto garantiza que el resultado aparezca al lado de la ecuación como lo esperas.

osea que flush = true fuerza el vaciamiento del buffer?
Sí, exactamente. Cuando usas flush=True en la función print, estás forzando el vaciamiento del búfer interno,
lo que hace que la salida se muestre inmediatamente en la consola sin esperar a que el búfer se llene por completo. 
Esto puede ser útil en situaciones en las que necesitas asegurarte de que la salida se muestre de inmediato,
especialmente al trabajar con retrasos de tiempo y otras operaciones en las que deseas ver la información en tiempo real.'''


# The buffer is typically flushed when the last character is a newline (\n), indicating the end of a line. 
# However, you can also force the buffer to flush using flush=True in the print statement. Alternatively, 
# the buffer will be flushed naturally when the Python script finishes execution, as part of the cleanup process.
# Using flush=True provides a way to ensure that the output is immediately displayed, even if the buffer
# hasn't reached the newline character.

import time


def func_compute(n):
    return lambda x: n * x


n = int(input('Querido Joaquin: que tabla queres que te devuelva: '))

f = func_compute(n) #lambda x: 2 * x

for i in range(1,10):
    print(f'{i} x {n} = ', end=' ', flush = True ) #flush the buffer and print the multiplication
    time.sleep(2) #wait 2 seconds
    print(f(i)) #print result
