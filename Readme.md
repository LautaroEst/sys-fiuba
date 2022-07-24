
# Repositorio no oficial de la Asignatura 86.05/66.74 - Señales y Sistemas de la FIUBA

---

## Temas de la materia

0. Introducción a Python
1. Señales continuas y discretas
2. Caracterización de Sistemas
3. Series de Fourier
4. Transformada de Fourier en tiempo continuo y discreto
5. Muestreo
6. Transformada discreta de Fourier (DFT)
7. Transformada de Laplace
8. Transformada Z
9. Sistemas en tiempo discreto
10. Espectrograma y transformada de Fourier de corto tiempo
11. Filtros digitales

## Instalación de Python con Anaconda

Hay diferentes maneras de utilizar Python en la práctica, aunque una de las más estandarizadas es a través de la distribución [Anaconda](https://www.anaconda.com/) del paquete abierto y gratuito [Conda](https://conda.io/en/latest/). Se recomienda fueremente utilizar este método para evitar problemas de compatibilidad con los notebooks del presente repositorio.

Para instalar Python con Anaconda en Linux, Windows o iOS se debe descargar el instalador correspondiente desde [este](https://www.anaconda.com/products/distribution) link y seguir los pasos [esta](https://docs.anaconda.com/anaconda/user-guide/getting-started/#) sección de la documentación. La documentación completa de Anaconda puede ser encontrada en [este](https://docs.anaconda.com/) link.

Una vez instalado, se recomienda crear un entorno virtual (*virutal enviroment*) usando el archivo [requirements.yml](./requirements.yml). Esto puede hacerse con la instrucción
```bash
conda env create -n ENVNAME --file requirements.yml
```
donde `ENVNAME` es el nombre del entorno. La documentación completa de Conda puede ser encontrada en [este](https://conda.io/projects/conda/en/latest/index.html) link. Para una lista de acceso rápido a los comandos, ver el [*cheet sheet* de Conda](https://conda.io/projects/conda/en/latest/_downloads/cb0ffc4c7b1e6c0e716c066d2b077faf/conda-4.12.pdf).

**Nota**: Cuando uno dice coloquialmente "instalar Python" en general se refiere a la [Máquina Virtual de Python] (https://www.devopsschool.com/blog/python-virtual-machine/#:~:text=Python%20Virtual%20Machine%20(PVM)%20is,instructions%20and%20display%20the%20output.), que es el programa que permite ejecutar los programas escritos en el [lenguaje de programación Python](https://www.python.org/). En nuestro caso, dejamos que el contexto solo se encargue de desambiguar estos dos términos :) 


