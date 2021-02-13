---
# Front matter
lang: ru-RU
title: "Отчёт по лабораторной работе №1"
subtitle: "Использование git. Использование Markdown для оформления отчётов."
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

Цель данной работы --- изучить работу git, а также познакомиться с основными возможностями разметки Markdown, с помощью подготовки отсчета.

# Задание

- Установить и подготовить git.
- Проверить роботоспособность.
- Выполнить отсчет в формате Markdown.

# Выполнение лабораторной работы

1. Выполните следующие команды, чтобы git узнал ваше имя и электронную почту (рис. -@fig:001).  
git config --global user.name "TEvolkov"  
git config --global user.email "adamkintel@gmail.com"
2. Настройка core.autocrlf с параметрами true и input делает все переводы строк текстовых файлов в главном репозитории одинаковы. core.autocrlf true - git автоматически конвертирует CRLF->LF при коммите и обратно LF->CRLF при выгрузке кода из репозитория на файловую систему (рис. -@fig:001).  
git config --global core.autocrlf true  
git config --global core.safecrlf true
3. Что бы избежать нечитаемых строк, установите соответствующий флаг (рис. -@fig:001).  
git config --global core.quotepath off

![Подготовка git](image/1.jpg){ #fig:001 width=70% }

4. Создайте репозиторий (рис. -@fig:002).  
git init
5. Создайте файл README.md, напишите в нем что-нибудь и добавьте все в репозиторий (рис. -@fig:002).  
touch README.md  
vi README.md  
git add .

![Создание репозитория](image/2.jpg){ #fig:002 width=70% }

6. Сделайте коммит (рис. -@fig:003).  
git commit -am "feat(main): add directories"

7. Привяжите и залейте файлы на github (рис. -@fig:003).  
git remote add origin https://github.com/TEVolkov/2020-2021_mathmod.git  
git push -u origin master

![Выкладывание на github](image/3.jpg){ #fig:003 width=70% }

# Выводы

Ознакомился с работой git и форматом Markdown.
