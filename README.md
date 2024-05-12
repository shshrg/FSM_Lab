**Принцип роботи**

Для симуляції свого дня я задала 6 станів - Sleep, Eat, Cry, Code, Walk та Play_Videogame. Перехід з одного стану в інший може спричинити випадкова подія, зміна часу або рандомний input (0 або 1). Я створила три події, які з певною ймовірністю можуть статись у будь-яку годину доби - Remember_Homework (Я згадую про дедлайн домашньої роботи), Check_Grades (Я перевіряю свої оцінки) та Hangout_With_Friends (Друг кличе мене гуляти). Деякі переходи залежать від часу - наприклад, о 14 та 19 годині я обов'язково піду їсти, якщо тільки не сталась подія Remember_homework, а о 22 я завжди йду спати. Якщо жодна з випадкових подій не сталась, то перехід залежить від input - 0 або 1, який рандомно обирається щогодини.

Принцип роботи симуляції зобрпжено на діаграмі нижче.

- Назви подій надто довгі, тому на діаграмі вони позначені наступним чином: Remember_Homework - event 1; Check_Grades - event 2; Hangout_With_Friends - event 3.

- Варто також зазначити, що випадкові події не можуть статись у деяких станах, бо це не реалістично, наприклад, у стані Sleep не може статись жодна подія (бо я сплю), а у стані Walk може статись лише Remember_Homework (бо я гуляю і не можу перевірити оцінки чи піти гуляти з друзями).

- Також в деяких випадках перехід залежить і від рандомної події, і від input - наприклад, після події Check_Grades я можу перейти у стан Cry, якщо input == 0 (оцінкт погані), або в інший стан, якщо input == 1 (оцінки хороші). На діаграмі такі випадки позначені як "event _ and _"

![image](https://github.com/shshrg/FSM_Lab/assets/149377587/d34d492e-e089-43f9-9208-808e3f2aa322)



**Приклади**
Ось декілька прикладів роботи моєї симуляції:

- Вдалий день
  ![image](https://github.com/shshrg/FSM_Lab/assets/149377587/69c164b4-1b9c-4ca4-bd01-7ca284c8de4b)
- І не дуже
  ![image](https://github.com/shshrg/FSM_Lab/assets/149377587/b15bda44-78a0-422f-a330-7495380e4efb)
