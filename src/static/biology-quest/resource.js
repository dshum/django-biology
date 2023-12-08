const questions = [
  {
    id: "1.1",
    title: "Вопрос 1",
    question: "Одна из цепей ДНК имеет следующую последовательность нуклеотидов: <b>АГГЦЦТТТАТГГЦЦАТ</b>.<br>" +
      "Используя принцип комплементарности, постройте вторую цепь ДНК.<br>" +
      "Вводите ответ заглавными русскими буквами без пробелов.",
    answer: "ТЦЦГГАААТАЦЦГГТА",
    hint: "Используйте правило комплементарности: напротив А находится Т, напротив Т - А, напротив Г - Ц, напротив Ц - Г.",
    incorrect: "1.2",
    correct: "2.1"
  },
  {
    id: "1.2",
    title: "Вопрос 1, вариант 2",
    question: "Одна из цепей ДНК имеет следующую последовательность нуклеотидов: <b>ТЦЦГГАААТАЦЦГГТА</b>.<br>" +
      "Используя принцип комплементарности, постройте вторую цепь ДНК.<br>" +
      "Вводите ответ заглавными русскими буквами без пробелов.",
    answer: "ГЦЦТАТЦАГЦТТАЦЦАГ",
    hint: "Используйте правило комплементарности: напротив А находится Т, напротив Т - А, напротив Г - Ц, напротив Ц - Г.",
    incorrect: "1.3",
    correct: "2.1"
  },
  {
    id: "1.3",
    title: "Вопрос 1, вариант 3",
    question: "Одна из цепей ДНК имеет следующую последовательность нуклеотидов: <b>ГАГТТЦАТЦГГГТАЦЦГ</b>.<br>" +
      "Используя принцип комплементарности, постройте вторую цепь ДНК.<br>" +
      "Вводите ответ заглавными русскими буквами без пробелов.",
    answer: "ЦТЦААГТАГЦЦЦАТГГЦ",
    hint: "Используйте правило комплементарности: напротив А находится Т, напротив Т - А, напротив Г - Ц, напротив Ц - Г.",
    incorrect: "2.1",
    correct: "2.1"
  },

  {
    id: "2.1",
    title: "Вопрос 2",
    question: "Правило Чаргаффа, которое можно объяснить принципом комплементарности, гласит: " +
      "количество Т в двуцепочечной молекуле ДНК равно количеству А, а количество Г равно количеству Ц.<br>" +
      "Количество Ц во фрагменте двуцепочечной ДНК составляет 40 нуклеотидов.<br>" +
      "Общее количество нуклеотидов равно 250.<br>" +
      "Найдите а) количество Г; б) общее количество А+Т; в) количество А.<br>" +
      "Вводите ответ числами через запятую и пробел.",
    answer: "40, 170, 85",
    hint: "а) количество Г равно количеству Ц по правилу комплементарности; " +
      "б) количество А+Т = общее количество нуклеотидов в двуцепочечной ДНК минус Г и Ц. А+Т = 250-40*2 = 250-80 = 170; " +
      "в) количество А = количеству Т по правилу комплементарности. А = 170/2 = 85",
    incorrect: "2.2",
    correct: "finish"
  },
  {
    id: "2.2",
    title: "Вопрос 2, вариант 2",
    question: "Правило Чаргаффа, которое можно объяснить принципом комплементарности, гласит: " +
      "количество Т в двуцепочечной молекуле ДНК равно количеству А, а количество Г равно количеству Ц.<br>" +
      "Количество Г во фрагменте двуцепочечной ДНК составляет 35 нуклеотидов.<br>" +
      "Общее количество нуклеотидов равно 150.<br>" +
      "Найдите а) количество Ц; б) общее количество А+Т; в) количество А.<br>" +
      "Вводите ответ числами через запятую и пробел.",
    answer: "35, 80, 40",
    hint: "а) количество Г равно количеству Ц по правилу комплементарности; " +
          "б) количество А+Т = общее количество нуклеотидов в двуцепочечной ДНК минус Г и Ц. А+Т = 150-35*2 = 150-70 = 80; " +
          "в) количество А = количеству Т по правилу комплементарности. А = 80/2 = 40",
    incorrect: "2.3",
    correct: "finish"
  },
  {
    id: "2.3",
    title: "Вопрос 2, вариант 3",
    question: "Правило Чаргаффа, которое можно объяснить принципом комплементарности, гласит: " +
      "количество Т в двуцепочечной молекуле ДНК равно количеству А, а количество Г равно количеству Ц.<br>" +
      "Количество А во фрагменте двуцепочечной ДНК составляет 45 нуклеотидов.<br>" +
      "Общее количество нуклеотидов равно 200.<br>" +
      "Найдите а) количество Т; б) общее количество Г+Ц; в) количество Г.<br>" +
      "Вводите ответ числами через запятую и пробел.",
    answer: "45, 110, 55",
    hint: "а) количество Т равно количеству А по правилу комплементарности; " +
             "б) количество Г+Ц = общее количество нуклеотидов в двуцепочечной ДНК минус А и Т. Г+Ц = 200-45*2 = 200-90 = 110; " +
             "в) количество Г = количеству Ц по правилу комплементарности. Г = 110/2 = 55",
    incorrect: "finish",
    correct: "finish"
  },

  {
    id: "finish",
    title: "Финал!",
    question: "Вы прошли квест!",
  }
]