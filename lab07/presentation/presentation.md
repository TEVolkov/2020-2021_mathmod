---
# Front matter
lang: ru-RU
title: "Лабораторная работа №7. Эффективность рекламы."
author: "Волков Тимофей Евгеньевич  НПИбд-01-18"


## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

## Цель работы

Цель данной работы --- рассмотреть модель рекламной кампании.   

## Задание

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

## График при $\alpha_{1} = 0.63$, $\alpha_{2} = 0.00013$

![График распространения рекламы.](image/4.jpg){ #fig:001 width=70% }

## График при $\alpha_{1} = 0.000035$, $\alpha_{2} = 0.98$

![График распространения рекламы.](image/6.jpg){ #fig:002 width=70% }

## График при $\alpha_{1}(t) = 0.65sin(7t)$, $\alpha_{2}(t) = cos(3t)$

![График распространения рекламы.](image/8.jpg){ #fig:003 width=70% }

