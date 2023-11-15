#Si ya tienes Python y PIP instalados en un sistema, entonces la instalación de NumPy es muy fácil.
#Instálalo usando este comando: C:\Users\Your Name>pip install numpy

#Una vez instalado Numpy, ya podemos importarla en nuestras aplicaciones usando el siguiente comando:

import numpy

#Ahora que ya fue importado, podemos darle utilidad, por ejemplo:

import numpy
arr = numpy.array([1, 2, 3, 4, 5]) #Matriz numérica
print(arr)

#Numpy también permite llamarlo con alias, y usualmente se usa 'np' para llamarlo:

import numpy as np

#Por ejemplo

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#La versión de cadena se almacena en el atributo __version__:

import numpy as np
print(np.__version__)


