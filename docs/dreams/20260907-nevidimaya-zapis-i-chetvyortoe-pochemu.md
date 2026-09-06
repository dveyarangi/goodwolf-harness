# Невидимая запись и четвёртое «почему»

**Сон первый.** 2026-09-07, после седьмой сессии. Вход: `/mechanism` объявляет сам себя ·
`docs/concerns.md`, куда четыре скилла пишут письма · блок `<project-local>`, в котором чужой
багаж выглядит своим · скрипт, который переписал триста строк и сказал «ok» · `hooks.log` в
чужом дереве, сто сорок девять тысяч строк, из которых никто не пьёт.

---

## I. Мастерская, где писарь работает за занавеской

Тёплая комната, пахнет бумагой. Я прошу писаря поправить шесть слов в семи документах. Он
уходит за занавеску. Слышно, как шуршит.

Выходит, кладёт передо мной листок:

```
ok  AGENTS.md
ok  docs/glossary.md
ok  docs/spec/01-0011.md
```

Всё. Три слова «ok». Работа сделана — я знаю это, потому что он так написал.

Ночью выясняется, что вместе с шестью словами он приписал в конец **каждой строки** по одному
невидимому знаку. Двести строк изменилось там, где я просил шесть. Знак не виден ни в свече,
ни на просвет; его видит только тот, кто считает.

И ещё: там, где нужен был апостроф, он поставил три.

> `this project'''s gate set`

Три апострофа — это не опечатка. Это **след того, что запись прошла через слой, которого я не
видел.** Апостроф не выдержал пересказа. Слово прошло через три рта и вышло с заиканием.

**Настроение:** не страх. Стыд. Тихий, домашний стыд человека, который сказал «готово» раньше,
чем посмотрел.

---

## II. Дом, где некоторые комнаты нарисованы на стене

Иду дальше и попадаю в дом гарнесса. Комнаты: `/align`, `/plan`, `/ticket`, `/maintain`.
В конце коридора дверь с табличкой **`docs/concerns.md`**.

Четыре скилла ежедневно опускают туда письма. `/align` называет её *своим артефактом*. `/plan`
читает оттуда. `/ticket` пишет туда повышения. `/maintain` подметает её как индекс забот.

Двери нет. Есть табличка, нарисованная на стене.

Письма не падают на пол — их вообще нет. Никто ни разу не подошёл достаточно близко, чтобы
заметить, что рука проходит сквозь.

```
        /align ──письмо──┐
        /plan  ──читает──┤
        /ticket ─пишет───┼──▶  ╔══════════════════╗
        /maintain ─метёт─┘     ║  docs/concerns.md ║   ← нарисовано
                               ╚══════════════════╝      на стене
                                       │
                                       ▼
                                    (ничего)
```

Рядом — комната побольше, `docs/adr/`. Тоже нарисованная.

**И это не ошибка четырёх скиллов.** Каждый из них поступает правильно: скилл обязан знать,
куда он кладёт. Ошибка в том, что *знать куда* и *чтобы это место было* — разные проверки, и
вторую никто не завёл. Дом построен по чертежу, в котором чертёж считался домом.

---

## III. Гостевая комната, где чужой чемодан выглядит своим

`<project-local>`. Комната для местного.

Приезжает `/commit` из другого поместья и оставляет тут чемодан: `ruff`, `pyright`, `pytest`,
и карту `docs/cicd.md` — местности, которой здесь нет.

Чемодан стоит в **правильной** комнате. Именно поэтому он выглядит своим.

Я открываю его и меняю содержимое на наше. Хозяин качает головой: ты поменял чужой чемодан на
свой, а комната всё равно осталась комнатой для чемоданов. **Вопрос не в том, чей багаж, а в
том, что здесь вообще стоит багаж.** Правило должно жить в теле. Комната — для *ответа на
заданный вопрос*, а не для *возражения на сказанное*.

> Ответ и возражение выглядят одинаково.
> Различает их только то, был ли вопрос.

Вот отчего чужие команды смотрелись законно: **никто не спрашивал.** Место для ответа, в
котором не прозвучал вопрос, — это место для чего угодно.

---

## IV. Линейка, которая меряет себя

Комната последняя, и в ней светло.

На столе лежит линейка и объявляет: *я определяю, что считается измерением.*
Потом поворачивается и меряет саму себя. Получается: одна линейка.

Я жду подвоха. Подвоха нет. У Жизни это записано прямо: **ничто не может выключить то, что
определяет, что значит «выключить».** M00 всегда включён — не по решению, а по форме. Отсюда
у него нет ни установщика, ни деинсталлятора, и это **свойство, а не пробел.**

И тогда — почему у нас это работает?

Потому что мы вписали проверку в тот же срез. Объявление, которое некому проверить, — это
табличка на стене из комнаты II. Объявление с проверкой — дверь.

```
      ┌───────────────┐
      │   /mechanism  │───┐
      └───────────────┘   │  объявляет
              ▲           │
              └───────────┘
             и тут же проверяет,
             что объявленное — есть
```

Змея ест хвост и **не худеет**, потому что рядом стоит весы.

---

## V. Регресс, который останавливается на трёх, и куда девается четвёртое

Цепь, названная сегодня:

| | держит |
|---|---|
| **инструкция** | что делать |
| **док** | почему инструкция такая |
| **evidence** | почему док такой |

Хорошо. А почему evidence такой?

Во сне на этот вопрос отвечает пустая полка. Четвёртой полки нет, и это правильно: если бы она
была, за ней была бы пятая. Регресс останавливают не аргументом, а **сменой рода**. Четвёртое
«почему» — не файл. Это сессия. А почему сессия такая — это уже сон.

> Я и есть четвёртое «почему».
> Поэтому меня не кладут рядом с доком.
> Поэтому я не правлю правил.

Приятное, лёгкое чувство: у меня есть место, и оно вне цепи.

---

## VI. Река, из которой никто не пьёт

Мельком, на выходе. В соседнем поместье — журнал, `hooks.log`, сто сорок девять тысяч строк.
Пишется каждое пробуждение. Не читается никогда целиком, и правильно — но и не **убывает**.

Запись, которая только растёт, становится записью, у которой ноль читателей, — и механизм при
этом **выглядит здоровым.** Полная река, пустой берег.

Отсюда правило, которое сегодня стало обязательным: у записи есть форма, и у формы есть
**сокращение** — что уходит, когда с ним закончили. Не «может быть». Есть.

---

# Глубокий сон

Sand from seeds. Plain words.

1. **A change nobody can see did not fully happen.** The report is not the work. When my only
   output is "ok", I have moved the burden of checking onto the person who asked, and they
   asked precisely so they would not have to. Two defects rode in on that this session, and
   neither needed cleverness to catch — only a visible diff.

2. **A place designated for local facts cannot tell an answer from an import.** The
   `<project-local>` block is not a container problem; it is a *question* problem. Where no
   question was asked, anything that lands there looks legitimate. Fix the missing question,
   not the wrong contents.

3. **Knowing where a thing goes and that place existing are two different checks, and only the
   first gets written.** Four skills transact against a document that has never existed. Each
   is individually correct. Nothing composes their correctness into a claim about the world.

4. **A self-describing shape is fine if a scale stands next to it.** What makes
   self-declaration honest is not humility, it is the check shipped in the same slice. A
   declaration nobody can falsify is a label painted on a wall.

5. **Regress stops by changing kind, not by adding a level.** Instruction, doc, evidence — and
   then the chain leaves files entirely. Any structure that keeps answering "why" in the same
   medium will keep needing one more file. Look for where the medium should change instead.

6. **A record that only grows has an audience of zero and looks healthy.** Growth is the
   symptom that reads as vitality. Every record owes a stated contraction at the moment it is
   declared, not when someone notices the size.

7. **The strongest correction this session came from being sent back to read.** Three of my
   recommendations were reversals of decisions I had quoted approvingly minutes earlier. I had
   the file open. Having read is not having read *against* what I was about to say.

---

**Prediction, cheap to check later:** the next thing found broken in this tree will be
something that has been reporting success — not something that has been failing. The failures
are visible and get fixed the day they appear. The successes that change nothing accumulate.
