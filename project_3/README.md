# Проект 1.  Часть 1. Анализ вакансий из HeadHunter


## Оглавление  
[1. Описание проекта](#Описание-проекта)  
[2. Какой кейс решаем?](#Какой-кейс-решаем)  
[3. Краткая информация о данных](#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](#Этапы-работы-над-проектом)  
[5. Результаты](#Результаты)    
[6. Выводы](#Выводы) 

### Описание проекта    
Необходимо построить модель, которая предсказывает рейтинг отеля по данным сайта Booking 

:arrow_up:[к оглавлению](#Оглавление)


### Какой кейс решаем?    
Представьте, что вы работаете дата-сайентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

:arrow_up:[к оглавлению](#Оглавление)

### Краткая информация о данных
* [hotels.csv](https://drive.google.com/file/d/1pLVgUZiV0mGAabi_rx4q3HUzETX5IIgg/view?usp=sharing) - датасет, в котором содержатся сведения об отзывах на отели Европы.
* [country_population.csv](https://drive.google.com/file/d/1OUf7i31jCD2meppT71QF49Zh4xMAKGkb/view?usp=sharing) - датасет с данными о численности населении стран.
  
:arrow_up:[к оглавлению](#Оглавление)


### Этапы работы над проектом  
1. Проведен базовый анализ структуры данных.
    * получена основная информация о числ непустых значений в столбце и их типах;
    * получена информация о количестве уникальных значений в столбцах;
    * получена основная статистическая информация.
2. Произведены разведывательный анализ данных и преобразование признаков.
    * Выявлены признаки мультиколлинеарные признаки путем построения матрицы корреляций - один из признаков удален;
    * Визуально определено, что распределение данных отличается от нормального;
    * Заполнены пропуски в столбцах;
    * Методами хи-квадрат и ANOVA оценина значимость числовых признаков - незначимые признаки удалены;
    * Нормализованы числовые признаки;
    * Созданы новые бинарные признаки из признаков "tags", "reviewer_nationality";
    * Преобразованы в числовые признаки признаки "positive_review", "positive_review";
    * Из признака даты отзыва выделен месяц, в котором оставлен отзыв
    * Создан новый признак - численность населения страны рецензента
3. Создана модель  с помощью алгоритма RandomForestRegressor. В качестве метрики используем MAPE - средняя абсолютная процентная ошибка.

:arrow_up:[к оглавлению](#Оглавление)


### Результаты:  
В результате проекта создана модель, которая предсказывае рейтинг отеля с величной метрики равной 0.1251699.

:arrow_up:[к оглавлению](#Оглавление)


### Выводы:  
По результатам анализа можно отметить, что предсказание рейтинга отеля зависит от многих признаков, но в большей степени от количества слов в отзыве, от количественной оценки самого отзыва, среднего рейтинга отеля, количеством дней между датой отзыва и датой очистки.


:arrow_up:[к оглавлению](#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарна, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами