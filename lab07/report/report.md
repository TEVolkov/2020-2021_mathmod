---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №7"
subtitle: "Эффективность рекламы."
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

Цель данной работы --- рассмотреть модель рекламной кампании.  

# Задание

## Вариант 17

Постройте график распространения рекламы, математическая модель которой описывается
следующим уравнением:

1. $dn/dt = (0.63 + 0.00013n(t))(N - n(t))$
2. $dn/dt = (0.000035 + 0.98n(t))(N - n(t))$
3. $dn/dt = (0.65sin(7t) + cos(3t)n(t))(N - n(t))$

При этом объем аудитории
N = 741
, в начальный момент о товаре знает 4 человека. Для
случая 2 определите в какой момент времени скорость распространения рекламы будет
иметь максимальное значение.

# Выполнение лабораторной работы

## Постановка задачи

Организуется рекламная кампания нового товара или услуги. Необходимо,
чтобы прибыль будущих продаж с избытком покрывала издержки на рекламу.
Вначале расходы могут превышать прибыль, поскольку лишь малая часть
потенциальных покупателей будет информирована о новинке. Затем, при
увеличении числа продаж, возрастает и прибыль, и, наконец, наступит момент,
когда рынок насытиться, и рекламировать товар станет бесполезным.

Предположим, что торговыми учреждениями реализуется некоторая
продукция, о которой в момент времени
t
из числа потенциальных покупателей
N
знает лишь
n
покупателей. Для ускорения сбыта продукции запускается реклама
по радио, телевидению и других средств массовой информации. После запуска
рекламной кампании информация о продукции начнет распространяться среди
потенциальных покупателей путем общения друг с другом. Таким образом, после
запуска рекламных объявлений скорость изменения числа знающих о продукции
людей пропорциональна как числу знающих о товаре покупателей, так и числу
покупателей о нем не знающих.

Модель рекламной кампании описывается следующими величинами.
Считаем, что dn/dt --- скорость изменения со временем числа потребителей,
узнавших о товаре и готовых его купить,
t - время, прошедшее с начала рекламной
кампании,
n(t) - число уже информированных клиентов. Эта величина
пропорциональна числу покупателей, еще не знающих о нем, это описывается
следующим образом:
$\alpha_{1}(t)(N - n(t))$
, где
N - общее число потенциальных
платежеспособных покупателей,
$\alpha_{1}(t) > 0$
--- характеризует интенсивность
рекламной кампании (зависит от затрат на рекламу в данный момент времени).
Помимо этого, узнавшие о товаре потребители также распространяют полученную
информацию среди потенциальных покупателей, не знающих о нем (в этом случае
работает т.н. сарафанное радио). Этот вклад в рекламу описывается величиной 
$\alpha_{2}(t)n(t)(N - n(t))$
, эта величина увеличивается с увеличением потребителей
узнавших о товаре. Математическая модель распространения рекламы описывается
уравнением:

$$
dn/dt = \alpha_{1}(t) + \alpha_{2}(t)n(t)(N - n(t))
$$(1)

При $\alpha_{1}(t) >> \alpha_{2}(t)$ получается модель типа модели Мальтуса, 
решение которой имеет вид

![График решения уравнения модели Мальтуса](image/1.jpg){ #fig:001 width=70% }

В обратном случае, при $\alpha_{1}(t) << \alpha_{2}(t)$

![График логистической кривой](image/2.jpg){ #fig:002 width=70% }

## Построение графиков

n(0) = 4 --- число информированных клиентов в начальный момент.

N = 741 --- общее число потенциальных платежеспособных покупателей.

### Первый случай

Дано:

$dn/dt = (0.63 + 0.00013n(t))(N - n(t))$

Тогда начальные условия:

$\alpha_{1} = 0.63$

$\alpha_{2} = 0.00013$

Код программы в Python (fig. -@fig:003).

![Код программы](image/3.jpg){ #fig:003 width=70% }

График (fig. -@fig:004).

![График распространения рекламы. Коэффициенты $\alpha_{1} = 0.63$, 
$\alpha_{2} = 0.00013$](image/4.jpg){ #fig:004 width=70% }

### Второй случай

Дано:

$dn/dt = (0.000035 + 0.98n(t))(N - n(t))$

Тогда начальные условия:

$\alpha_{1} = 0.000035$

$\alpha_{2} = 0.98$

Код программы в Python (fig. -@fig:005).

![Код программы](image/5.jpg){ #fig:005 width=70% }

График (fig. -@fig:006).

![График распространения рекламы. Коэффициенты $\alpha_{1} = 0.000035$, 
$\alpha_{2} = 0.98$](image/6.jpg){ #fig:006 width=70% }

### Третий слчай

Дано:

$dn/dt = (0.65sin(7t) + cos(3t)n(t))(N - n(t))$

Тогда начальные условия:

$\alpha_{1} = 0.65sin(7t)$

$\alpha_{2} = cos(3t)$

Код программы в Python (fig. -@fig:007).

![Код программы](image/7.jpg){ #fig:007 width=70% }

График (fig. -@fig:008).

![График распространения рекламы. $\alpha_{1}(t) = 0.65sin(7t)$, 
$\alpha_{2}(t) = cos(3t)$](image/8.jpg){ #fig:008 width=70% }

# Выводы

Рассмотрел модель рекламной кампании.
