---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №4"
subtitle: "Модель гармонических колебаний."
author: "Волков Тимофей Евгеньевич"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian 
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Цель данной работы --- рассмотреть модель линейного гармонического осциллятора.

# Задание

## Вариант 17

Постройте фазовый портрет гармонического осциллятора и решение уравнения
гармонического осциллятора для следующих случаев

1. Колебания гармонического осциллятора без затуханий и без действий внешней
силы x'' + 12x = 0
2. Колебания гармонического осциллятора c затуханием и без действий внешней
силы x'' + 11x' + 2x = 0
3. Колебания гармонического осциллятора c затуханием и под действием внешней
силы x'' + 2x' +2x = 2cos(2t)

На интервале $t \in [0;51]$ (шаг 0.05) 
с начальными условиями x~0~ = 0.5, y~0~ = 1

# Выполнение лабораторной работы

## Постановка задачи

Движение грузика на пружинке, маятника, заряда в электрическом контуре, а
также эволюция во времени многих систем в физике, химии, биологии и других
науках при определенных предположениях можно описать одним и тем же
дифференциальным уравнением, которое в теории колебаний выступает в качестве
основной модели. Эта модель называется линейным гармоническим осциллятором.

Уравнение свободных колебаний гармонического осциллятора имеет
следующий вид:

$$
x'' + 2\gamma x' + \omega_{0}^2 x = 0
$$(1)

где x – переменная, описывающая состояние системы (смещение грузика, заряд
конденсатора и т.д.), $\gamma$ – параметр, характеризующий потери энергии (трение в
механической системе, сопротивление в контуре), $\omega_{0}$ – собственная частота
колебаний, t – время. (Обозначения $x'' = d^2x / dt^2, x' = dx / dt$)

Уравнение (1) есть линейное однородное дифференциальное уравнение
второго порядка и оно является примером линейной динамической системы.

При отсутствии потерь в системе ($\gamma$ = 0)вместо уравнения (1.1) получаем
уравнение консервативного осциллятора энергия колебания которого сохраняется
во времени.

$$
x'' + \omega_{0}^2x = 0
$$(2)

Для однозначной разрешимости уравнения второго порядка (2) необходимо
задать два начальных условия вида

$$
x(t_{0}) = x_{0}, x'(t_{0}) = y_{0}
$$(3)

Уравнение второго порядка (2) можно представить в виде системы двух
уравнений первого порядка:

$$
x' = y
$$
$$
y' = - \omega_{0}^2x
$$(4)

Начальные условия (3) для системы (4) примут вид:

$$
x(t_{0}) = x_{0}, y(t_{0}) = y_{0}
$$(5)

Независимые переменные x, y определяют пространство, в котором
«движется» решение. Это фазовое пространство системы, поскольку оно двумерно
будем называть его фазовой плоскостью.

Значение фазовых координат x, y в любой момент времени полностью
определяет состояние системы. Решению уравнения движения как функции
времени отвечает гладкая кривая в фазовой плоскости. Она называется фазовой
траекторией. Если множество различных решений (соответствующих различным 
начальным условиям) изобразить на одной фазовой плоскости, возникает общая
картина поведения системы. Такую картину, образованную набором фазовых
траекторий, называют фазовым портретом.

## Построение фазового портрета гармонических колебаний

Уравнение колебания гармонического осциллятора будет иметь вид

$$
x'' + g * x' + w * x = f(t)
$$(6)

где 

$g = 2\gamma$ --- затухание

$w = \omega_{0}^2$ --- частота

$f(t)$ --- действие внешней силы

Уравнение второго порядка (6) можно представить в виде системы двух
уравнений первого порядка:

$$
x' = y
$$

$$
y' = - wx - gy - f(t)
$$ 

На интервале $t \in [0;51]$ (шаг 0.05) 
с начальными условиями x~0 = 0.5, y~0 = 1

### Колебания гармонического осциллятора без затуханий и без действий внешней силы

Дано:

$$
x'' + 12x = 0
$$

Тогда начальные условия:

g = 0

w = 12

f(t) = 0

x~0~ = 0.5

y~0~ = 1

$t \in [0;51]$

Код программы в Python (fig. -@fig:001).

![Код программы](image/1.jpg){ #fig:001 width=70% }

Фазовый портрет( fig. -@fig:002).

![Фазовый портрет гармонического осциллятора без затуханий, без действия внешней силы](image/2.jpg){ #fig:002 width=70% }

### Колебания гармонического осциллятора c затуханием и без действий внешней силы

Дано:

$$
x'' + 11x' + 2x = 0
$$

Тогда начальные условия:

g = 11

w = 2

f(t) = 0

x~0~ = 0.5

y~0~ = 1

$t \in [0;51]$

Код программы в Python (fig. -@fig:003).

![Код программы](image/3.jpg){ #fig:003 width=70% }

Фазовый портрет( fig. -@fig:004).

![Фазовый портрет гармонического осциллятора с затуханием, без действия внешней силы](image/4.jpg){ #fig:004 width=70% }

### Колебания гармонического осциллятора c затуханием и под действием внешней силы 

Дано:

$$
x'' + 2x' +2x = 2cos(2t)
$$

Тогда начальные условия:

g = 2

w = 2

f(t) = 2cos(2t)

x~0~ = 0.5

y~0~ = 1

$t \in [0;51]$

Код программы в Python (fig. -@fig:005).

![Код программы](image/5.jpg){ #fig:005 width=70% }

Фазовый портрет( fig. -@fig:006).

![Фазовый портрет гармонического осциллятора с затуханием и под действием внешней силы](image/6.jpg){ #fig:006 width=70% }


# Выводы

Рассмотрел модель линейного гармонического осциллятора.
