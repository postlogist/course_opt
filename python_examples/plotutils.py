"""
Полезные функции для примеров курса по методам оптимизации

"""

import numpy as np # Работа с массивами
import matplotlib.pyplot as plt # Графики
from mpl_toolkits.mplot3d import axes3d #3d-графики
import sympy as sp # Пакет символьной математики

# Обход проблемы с отображением матриц - определяем функцию для их печати
from IPython.display import  Math
def printMatrix(m):
    """
    Функция для вывода в блокнот матриц SymPy.
    Использование: printMatrix(Матрица)
    """
    return Math(sp.latex(m))


# Функция для рисования поверхности
def plotSurface(f, xlim=(-10, 10), ylim=(-10, 10), steps=51, levels=10,
                 aspect='equal', size=(10, 10)):
    """
    Вывод графика поверхности функции двух переменных
    
    Аргументы:
    f - функция двух переменных
    xlim, ylim - диапазоны изменения переменных x и y
    steps - число шагов
    levels - количество уровней или набор уровней для построения изолиний
    aspect - соотношение масштабов по осям x и y
    size - размер рисунка
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Координаты узлов сетки для рисования графика
    xx = np.linspace(*xlim, num=steps)
    yy = np.linspace(*ylim, num=steps)        
    XX, YY = np.meshgrid(xx, yy)
    Z = f(XX, YY)    
    
    
    # Рисование поверхности
    ax.plot_surface(XX, YY, Z, rstride=8, cstride=8, alpha=0.3)
    cset = ax.contourf(XX, YY, Z, zdir='z', offset=-np.abs(Z.min()), cmap=plt.cm.viridis)

    ax.set_xlabel('X')
    #ax.set_xlim(*xlim)
    ax.set_ylabel('Y')
    #ax.set_ylim(*ylim)
    ax.set_zlabel('Z')
    #ax.set_zlim(-100, 100)


# Функция для рисования контурного графика
def plotContours(f, xlim=(-10, 10), ylim=(-10, 10), steps=51, levels=10,
                 aspect='equal', size=(10, 10), clim=(None, None)):
    """
    Вывод контурного графика функции двух переменных
    
    Аргументы:
    f - функция двух переменных
    xlim, ylim - диапазоны изменения переменных x и y
    steps - число шагов
    levels - количество уровней или набор уровней для построения изолиний
    aspect - соотношение масштабов по осям x и y
    size - размер рисунка
    clim - пределы для цветовой шкалы
    """
    
    # Координаты узлов сетки для рисования графика
    xx = np.linspace(*xlim, num=steps)
    yy = np.linspace(*ylim, num=steps)        
    XX, YY = np.meshgrid(xx, yy)
    Z = f(XX, YY)
    
    # Рисование контуров    
    csf = plt.contourf(XX, YY, Z, levels, cmap=plt.cm.viridis)
    plt.clim(*clim)
    plt.colorbar(csf, fraction=0.046, pad=0.04) # Подогнать размер цветовой шкалы под размер графика
    
    cs = plt.contour(XX, YY, Z, levels, colors='k')
    
    # Соотношение масштабоб по осям
    ax = plt.gca()
    ax.set_aspect('equal')
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    
    # Размер рисунка
    fig = plt.gcf()
    fig.set_size_inches(size)    

# Функция для добавления поля градиентов на контурный график
def addGradients(grad_f, xlim=None, ylim=None, steps=21):
    """
    Вывод векторного поля для градиента функции двух переменных
    
    Аргументы:
    grad_f - функция, возвращающая компоненты градиента
    xlim, ylim - диапазоны изменения переменных x и y
    steps - число шагов
    """
    
    ax = plt.gca()
    if xlim is None:
        xlim = ax.get_xlim()
    if ylim is None:
        ylim = ax.get_ylim()
    
    xx = np.linspace(*xlim, num=steps)
    yy = np.linspace(*ylim, num=steps)
    
    XX, YY = np.meshgrid(xx, yy)    
    U, V = grad_f(XX, YY)
    
    plt.quiver(XX,YY,U,V)


# Функция для добавления на контурный график градиента (и антиградиента) в заданной точке
def addGradient(x, y, grad_f, color='red', grad=True, antigrad=False, antiColor='lightSkyBlue'):
    """
    Вывод градиента функции двух переменных в указанных точках
    
    Аргументы:
    x, y - координаты точки (или векторы с координатами точек)
    grad_f - функция, возвращающая компоненты градиента
    color - цвет для точки и градиента
    grad - рисовать градиент?
    antigrad - рисовать антиградиент?
    antiColor - цвет для антиградиента
    """

    plt.plot(x, y, marker='o', markersize=8, mfc=color, mec=None, linestyle='none')  
    U, V = grad_f(x, y)
    if grad:
        plt.quiver(x,y,U,V, color=color)
    if antigrad:
        plt.quiver(x,y,-U,-V, color=antiColor)

# Функция для добавления на контурный график точки
def addPoint(x, y, color='lightskyblue'):
    """
    Вывод точки в указанных координатах
    
    Аргументы:
    x, y - координаты точки (или векторы с координатами точек)
    color - цвет для точки
    """

    plt.plot(x, y, marker='o', markersize=10, mfc=color, mec=None, linestyle='none')

# Функция для добавления на контурный график траектории поиска
def addPath(path, points=False, lines=True, search_dir=False, 
            point_color='red', line_color='white', search_dir_color='lightskyblue') :
    """
    Добавляет на график траекторию поиска
    
    Аргументы:
    path - траектория поиска
    points - рисовать точки
    lines - соединять точки линией
    search_dir - рисовать направление поиска
    point_color, line_color, search_dir_color - цвета    
    """
    
    
    X = np.zeros(len(path) + 1, dtype='float64')
    Y = np.zeros(len(path) + 1, dtype='float64')
    if search_dir:
        U = np.zeros(len(path), dtype='float64')
        V = np.zeros(len(path), dtype='float64')
    
    
    for i, s in enumerate(path):
        X[i] = s['Xk'][0]
        Y[i] = s['Xk'][1]
        if search_dir:
            U[i] = s['Sk'][0]
            V[i] = s['Sk'][1]        
    
    X[-1] = path[-1]['Xnext'][0]
    Y[-1] = path[-1]['Xnext'][1]
    
    if lines:
        plt.plot(X, Y, color=line_color)
    
    if points:
        plt.plot(X, Y, marker='o', mfc=point_color, mec=None, markersize=5, linestyle='none')
        
    if search_dir:
        plt.quiver(X[:-1], Y[:-1], U, V, units='dots', color=search_dir_color, headwidth=3, width=2)