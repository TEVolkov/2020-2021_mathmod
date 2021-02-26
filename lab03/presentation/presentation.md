---
# Front matter
lang: ru-RU
title: "Лабораторная работа №3. Модель боевых действий."
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

Цель данной работы --- рассмотрть некоторые простейшие модели боевых действий --- модели Ланчестера.

## Задание

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

## Только регулярные войска

![График изменения численности войск](image/2.jpg){ #fig:001 width=70% }

## Регулярные войска и партизанские отряды

![График изменения численности войск](image/4.jpg){ #fig:002 width=70% }

