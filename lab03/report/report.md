---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №3"
subtitle: "Модель боевых действий."
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

Цель данной работы --- рассмотрть некоторые простейшие модели боевых действий --- модели Ланчестера.

# Задание

## Вариант 17

Между страной Х и страной У идет война. Численность состава войск
исчисляется от начала войны, и являются временными функциями
x(t)
и
y(t). В 
начальный момент времени страна Х имеет армию численностью 20 850 человек, а
в распоряжении страны У армия численностью в 9 900 человек. Для упрощения
модели считаем, что коэффициенты
a, b, c, h 
постоянны. Также считаем
P(t)
и
Q(t)
непрерывные функции.

Постройте графики изменения численности войск армии Х и армии У для
следующих случаев:

1. Модель боевых действий между регулярными войсками
$$
(dx)/(dt) = -0.71x(t) - 0.85y(t) + sin(6t) + 1
$$

$$
(dy)/(dt) = -0.59x(t) - 0.73y(t) + cos(7t) + 1
$$

2. Модель ведения боевых действий с участием регулярных войск и партизанских отрядов 
$$
(dx)/(dt) = -0.71x(t) - 0.85y(t) + 1.5sin(2t)
$$

$$
(dy)/(dt) = -0.59x(t)y(t) - 0.73y(t) + 1.5cos(t)
$$

# Выполнение лабораторной работы

## Постановка задачи

Рассмотрим некоторые простейшие модели боевых действий – модели
Ланчестера. В противоборстве могут принимать участие как регулярные войска,
так и партизанские отряды. В общем случае главной характеристикой соперников
являются численности сторон. Если в какой-то момент времени одна из
численностей обращается в нуль, то данная сторона считается проигравшей (при
условии, что численность другой стороны в данный момент положительна).

Рассмотри два случая ведения боевых действий:
1. Боевые действия между регулярными войсками
2. Боевые действия с участием регулярных войск и партизанских отрядов

В первом случае численность регулярных войск определяется тремя
факторами:
- скорость уменьшения численности войск из-за причин, не связанных с
боевыми действиями (болезни, травмы, дезертирство);
- скорость потерь, обусловленных боевыми действиями
противоборствующих сторон (что связанно с качеством стратегии,
уровнем вооружения, профессионализмом солдат и т.п.);
- скорость поступления подкрепления (задаётся некоторой функцией от
времени).

В этом случае модель боевых действий между регулярными войсками
описывается следующим образом

$$
(dx)/(dt) = -a(t)x(t) - b(t)y(t) + P(t)
$$

$$
(dy)/(dt) = -c(t)x(t) - h(t)y(t) + Q(t)
$$

Потери, не связанные с боевыми действиями, описывают члены -a(t)x(t) и
-h(t)y(t)
, члены -b(t)y(t) и -c(t)x(t) отражают потери на поле боя.
Коэффициенты
b(t) и
c(t) указывают на эффективность боевых действий со
стороны у и х соответственно,
a(t) h(t)--- величины, характеризующие степень
влияния различных факторов на потери. Функции P(t), Q(t) учитывают 
возможность подхода подкрепления к войскам Х и У в течение одного дня.

Во втором случае в борьбу добавляются партизанские отряды. Нерегулярные
войска в отличии от постоянной армии менее уязвимы, так как действуют скрытно,
в этом случае сопернику приходится действовать неизбирательно, по площадям,
занимаемым партизанами. Поэтому считается, что темп потерь партизан,
проводящих свои операции в разных местах на некоторой известной территории,
пропорционален не только численности армейских соединений, но и численности
самих партизан. В результате модель принимает вид:

$$
(dx)/(dt) = -a(t)x(t) - b(t)y(t) + P(t)
$$

$$
(dy)/(dt) = -c(t)x(t)y(t) - h(t)y(t) + Q(t)
$$

## Построение графиков

В 
начальный момент времени страна Х имеет армию численностью 20 850 человек, а
в распоряжении страны У армия численностью в 9 900 человек.

### Модель боевых действий между регулярными войсками

Дано:
$$
(dx)/(dt) = -0.71x(t) - 0.85y(t) + sin(6t) + 1
$$

$$
(dy)/(dt) = -0.59x(t) - 0.73y(t) + cos(7t) + 1
$$

Тогда начальные условия:

x = 20850

y = 9900

a = 0.71

b = 0.85

c = 0.59

h = 0.73

P(t) = sin(6t) + 1

Q(t) = cos(7t) + 1

Код программы в Python (fig. -@fig:001).

![Код программы](image/1.jpg){ #fig:001 width=70% }

График изменения численности войск (армия x --- синий, аримя y --- оранжевый)( fig. -@fig:002).

![График изменения численности войск](image/2.jpg){ #fig:002 width=70% }

### Модель ведения боевых действий с участием регулярных войск и партизанских отрядов

Дано:
$$
(dx)/(dt) = -0.71x(t) - 0.85y(t) + 1.5sin(2t)
$$

$$
(dy)/(dt) = -0.59x(t)y(t) - 0.73y(t) + 1.5cos(t)
$$

Тогда начальные условия:

x = 20850

y = 9900

a = 0.71

b = 0.85

c = 0.59

h = 0.73

P(t) = 1.5sin(2t)

Q(t) = 1.5cos(t)

Код программы в Python (fig. -@fig:003).

![Код программы](image/3.jpg){ #fig:003 width=70% }

График изменения численности войск (армия x --- синий, аримя y --- оранжевый)(fig. -@fig:004).

![График изменения численности войск](image/4.jpg){ #fig:004 width=70% }

# Выводы

Рассмотрел некоторые простейшие модели боевых действий.
