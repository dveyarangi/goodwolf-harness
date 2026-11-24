# An outside audit of the whole project — 2026-11-20

A third pass over the whole tree by a reviewer outside it, brought by the user into the session
on [q-7rmmpw](../questions/q-7rmmpw-how-is-produced-work-gone-over-again-over-what-scope-by-what-criteria-by-whom-and-to-what-result.md)
on 2026-11-20 and kept as they gave it, in Russian, below. By its own account it ran the test
suite (1163 passed), counted all 1728 commits, read the store, session, corpus, edge, installer,
injector and mechanism scripts, the hook, the entry file, the glossary and all 25 skills, and
re-checked six findings against the source itself. It follows
[the audit of 2026-10-13](./external-audit-2026-10-13.md). Kept so its findings are given homes
and its claims can be re-checked against a later tree *(the user, 2026-11-20)*.

## What the session checked, at `e603e2c1`

| Claim | Found |
|---|---|
| The scripts lock nothing | holds — no `fcntl`, `msvcrt` or `O_EXCL`; [sessions.py](../../.agents/scripts/gw/sessions.py) says so. It is the decided contract, not a gap: [Interruption and recovery](../architecture.md#interruption-and-recovery) leaves simultaneous writers to the host *(the user, 2026-10-11)* |
| An entry is written with `write_text`, not atomically | holds — `_Draft.write` in [questions.py](../../.agents/scripts/gw/questions.py); `_replace`, which renames a staged copy, stands beside it unused there. A reader can meet half an entry |
| Check and write are apart: two sessions on one entry both pass | holds in part — the draft re-reads every entry it read before writing and refuses one that changed; the window between that re-read and the write stays |
| An unknown header line vanishes silently at the next write | holds — tried 2026-11-24 on a copy at `e603e2c1`: `lean` on an entry carrying an unknown line exits 0 and the line is gone. This row read «does not hold» until then, on a reading of the parser alone, the write never run |
| `git init` runs before the checks | holds in part — only into an empty folder inside no repository, and reported; a later refusal leaves the folder a repository |
| The README promises Python 3.12+, the code needs 3.13 | holds — `PurePosixPath.full_match` in harness.py and inject_rules.py, no version check |
| An update runs the installer of the fetched commit, unsigned | holds — the commit is resolved and named, nothing verifies it |
| The person's local home path stands in 328 public files | holds — 329 files; the first count here, 77, missed the escaped forms and the `ls -l` owner column |

Checked by the Хранитель session at `4314d5bf`, read-only, through a subagent:

| Claim | Found |
|---|---|
| «A push never follows a commit» against L2's «push each commit» | does not hold — the commit skill says a push is never *implied* and defers to the project's local file; L2 is this tree's answer |
| /verify → /maintain in the loop against «a landed slice is verified, not maintained» | holds in part — no contradiction, but only the maintain skill's body says the ring's step closes the verified unit's records; the entry file is silent |
| R8 broken by /ticket, /plan, /verify | holds in part — /plan and /verify break it, /ticket does not; align, debugging, mechanism and review-architecture do too; eleven cross-mechanism namings, no script checks it |
| window, wake, ring, shelf, contains, resembles missing from the glossary | holds — defined in neither glossary |
| AGENTS.md grown 7.5 → 26.7 KB | holds — 7,474 B on 2026-09-14, 26,709 B now; 44% installed blocks, the hand-authored text doubled |

Not checked: the hook's cost per message, the ceremony estimate, the commit statistics.

## Where each finding went

| Finding | Home |
|---|---|
| Non-atomic entry write; the re-read-to-write window | the Хранилище session |
| README's Python version | the Продукт session, with the README's ticket |
| The loop line silent on maintain after verify; window, wake, ring, shelf undefined; the entry file's growth | the Хранитель session |
| R8 broken by skills | [q-43dten](../questions/q-43dten-how-does-the-shape-check-hold-a-skill-to-naming-no-skill-of-another-installed-mechanism.md) |
| «contains» and «resembles» undefined | the Хранилище session, as Q1's test |
| Local paths and raw session dumps in the public repository | [q-mhwbg3](../questions/q-mhwbg3-what-of-the-trees-own-records-session-cases-transcripts-local-paths-may-stand-in-its-public-repository.md), the person's decision |

## The audit, as given

The whole text the person brought, word for word; the one change is the person's home path, written
`[домашний путь]` in two places. Until 2026-11-24 an abridged retelling by the session stood here
under this heading, the first assessment and the marks «по отчёту» left out of it.

```text
https://github.com/dveyarangi/goodwolf-harness
дай независимую оценку этому репозиторию, расскажи что там

Клонировал репозиторий и изучил README, правила и структуру скриптов; дальше проверю тесты и docs/, после чего напишу оценку.

Коротко: это серьёзно сделанный, но сильно переусложнённый харнесс для долгой работы с ИИ-агентами. Инженерное ядро сильное, а польза для чужого проекта пока не доказана. Оценка по чтению кода и документов — тесты и установщик я не запускал.

Что это

GoodWolf Harness — набор Markdown-правил и Python-скриптов (только стандартная библиотека, MIT) для Claude Code, Codex и Cursor. Он держит «память проекта» в файлах репозитория, чтобы агент не начинал каждую сессию с нуля.

Дерево открытых вопросов (docs/questions/, около 390 записей). Хук перед каждым сообщением подкладывает агенту «окно» вокруг текущего вопроса; векторного поиска нет.
Компиляция правил. Правило пишется один раз в *.rules.md, скрипт вставляет его в AGENTS.md и скиллы, проверка ловит расхождение копий.
«Соломенные псы». Временный текст привязан к открытому вопросу и всплывает на переписывание, когда вопрос закрыт.
Журнал провалов правил (docs/rule-failures.md, 98 записей). Каждый случай, когда агент проигнорировал правило, записывается, и правило ужесточается.
Цикл работы: /ticket → /plan → /implement → /verify → /maintain, плюс /recall, /align, /conclude для сессий.
Параллельные сессии видят друг друга; pre-push хук не пускает сломанные записи.

Масштаб: около 1730 коммитов за 72 дня (с 9 сентября), примерно 1,2 МБ Python, 1149 тестов, 24+ скилла. Звёзд и форков ноль, автор один; проект разрабатывается сам на себе.

Сильные стороны
Установщик и проверка дрейфа правил — лучшая часть. Внешний аудит от 13 октября, лежащий в репозитории, подтвердил руками, что они работают как заявлено.
Тестов больше, чем кода (test_harness.py — 159 КБ против 95 КБ у harness.py). Скрипты отказываются, а не угадывают, и не обращаются к сети.
Таблица четырёх видов документов (намерение / инвариант / факт / прошлое, и кто побеждает при споре с кодом) — ясная идея, переносимая в любой проект.
Честность к себе. Проект хранит внешние аудиты с неприятными выводами и сравнение «налога на контекст» с семью аналогами, где сам выглядит худшим.
Слабые стороны
Дорогой контекст. По собственному замеру — около 4000 токенов до первого сообщения против 370–2100 у аналогов (spec-kit, superpowers, beads, OpenSpec), плюс отчёт на старте и окно на каждое сообщение. AGENTS.md с октября вырос с 17 до 27 КБ.
Сходимость под вопросом. Контракт входа дошёл до версии 138, провалов правил 98. Значительная часть свежих коммитов — MAINTAIN и RULE-FAILURE, то есть харнесс обслуживает сам себя. Тот же аудит назвал доказательную базу и сходимость слабыми.
Закрытый язык. «Shape», «straw dog», «rung», «dial», «wake», «window» — правила написаны плотной прозой, которую трудно читать и человеку, и модели. Собственный принцип Оккама из AGENTS.md проект нарушает.
Нет внешнего подтверждения. Все метрики — из самого проекта и пары соседних проектов автора. Открытые issues от конца октября — это отчёты о неудачных установках (Windows, хуки не переносятся, зрелый репозиторий отвергает харнесс).
Большие файлы. questions.py — 2657 строк и 187 функций, harness.py — около 2000 строк.
Репозиторий весит 112 МБ в docs/, из них 92 МБ — docs/cases с сырыми дампами сессий и API-запросов.
На что обратить внимание

В 328 файлах публичного репозитория встречается локальный путь [домашний путь] — то есть имя пользователя Windows и сырые транскрипты сессий лежат в открытом доступе. Ключей API по шаблонам sk-ant-, ghp_, AKIA я не нашёл, но сами транскрипты на личные данные не вычитывал.

Вердикт

Как исследовательский проект и источник идей — сильно: компиляцию правил, привязку временных решений к вопросам и журнал провалов стоит заимствовать. Как продукт для чужого проекта — рано: порог входа высокий, цена в токенах заметная, установка на Windows шаткая. Главный риск — что объём правил растёт быстрее, чем их польза.

а сам репо ты читал?

Читал, но выборочно — не весь.

Что прочитал сам, из клона репозитория:

README.md целиком;
AGENTS.md — первые 150 строк из примерно 27 КБ;
.claude/settings.json и первые 80 строк hook.sh;
начало local.rules.md, docs/product.md, docs/rule-failures.md;
докстринг и список функций questions.py (сам код функций не читал);
одну запись из docs/questions/, начало внешнего аудита от 13 октября и сравнения «налога на контекст»;
список файлов с размерами, последние 200 коммитов из примерно 1730, список issues (заголовки, не тексты).

Что не читал:

тела скриптов — harness.py, inject_rules.py, sessions.py и остальные;
сами тесты — я только посчитал строки def test (1149);
24 скилла в .agents/skills/ и описания механизмов;
тикеты, RFC, почти все вопросы и исследования, docs/cases;
ничего не запускал.

Что из этого следует для оценки:

«Установщик и проверка дрейфа работают» — это вывод аудита, лежащего в самом репозитории, а не моя проверка. Аудит от 13 октября, с тех пор прошло около тысячи коммитов.
«Тестов больше, чем кода» — сравнение размеров файлов. Качество тестов я не оценивал.
«Скрипты не обращаются к сети» — по поиску импортов в .agents/scripts, не по чтению кода.
«Значительная часть коммитов — обслуживание самого себя» — впечатление от последних 30 заголовков, я не считал.
Замечания про закрытый язык, рост AGENTS.md, размер docs/ и пути [домашний путь] в 328 файлах — проверены напрямую.

Так что это оценка по документации, структуре и метаданным, а не ревью кода. Если нужна настоящая — могу прочитать ключевые скрипты и скиллы целиком и прогнать тесты.

чет поверхностная оценка какая-то

Справедливо. Делаю нормально: читаю код и скиллы целиком, запускаю тесты, считаю историю коммитов, а не сужу по заголовкам.

Три агента параллельно читают код и скиллы целиком; историю коммитов я уже посчитал, сейчас запускаю тесты.

Все три агента отчитались, тесты прошли; перепроверяю ключевые находки по коду сам, потом пишу оценку.

Вторая оценка, уже по коду: проект инженерно добротнее, чем средний «набор промптов», но его главные обещания (несколько сессий сразу, «отказ ничего не пишет», лёгкость для мелкой работы) код и правила выполняют лишь частично.

На чём основано
Запущено: тесты — 1163, все прошли (6 пропущено, 1 ожидаемый провал), 7 минут на прогон.
Посчитано: вся история, 1728 коммитов.
Прочитано целиком (тремя агентами параллельно): questions.py, sessions.py, docs_corpus.py, edges.py, harness.py, inject_rules.py, mechanisms.py, hook.sh, AGENTS.md, глоссарий, все 25 SKILL.md.
Перепроверено мной по исходникам: отсутствие блокировок, неатомарная запись, потеря строк заголовка, git init до проверок, запуск чужого установщика при обновлении, требование Python 3.13.
Не прочитано: сами тесты, большая часть описаний механизмов и побочных файлов скиллов, корпус docs/. Установщик не запускался. Находки ниже с пометкой «по отчёту» я сам не проверял.
Что подтвердилось как сильное
Установщик осторожен с чужим проектом. Читает git-объекты, а не рабочее дерево; отказывается перезаписывать существующие AGENTS.md, чужой pre-push хук, отредактированные файлы; на Windows вместо симлинка выдаёт точную команду mklink.
Компиляция правил дисциплинирована: один источник, блоки <installed>, побайтовое сравнение, проверяемый дрейф.
Хранилище вопросов валидирует весь черновик до записи и перечитывает байты перед ней. Хук не роняет хост.
Ссылки в скиллах настоящие: из 16 проверенных флагов и файлов существуют 15.
/impact и /verify — компактные и содержательные. «Прогон с нулём тестов — не проверка» — хорошее правило.
Что оказалось хуже, чем заявлено

Параллельные сессии не защищены.

В скриптах нет ни одной блокировки (поиск по fcntl, msvcrt, O_EXCL пуст).
Записи вопросов пишутся через write_text, не атомарно (questions.py:2573), хотя атомарная _replace лежит рядом и используется только миграцией.
Проверка и запись разнесены (questions.py:2231): две сессии, правящие одну запись, обе проходят, побеждает последняя.
sessions.py говорит это прямым текстом: «nothing is locked». Блокировка на запись запланирована в тикете 01-0010.0250.0110, но не построена.

Запись молча теряет данные. _entry_text выводит только известные поля (questions.py:2618), так что любая нераспознанная строка заголовка исчезает при следующей записи.

«Every refusal writes nothing» — неправда.

git init выполняется до проверок (harness.py:278).
main ловит только Refused, поэтому OSError посреди установки оставит часть файлов без отчёта.
Отката нет, и комментарии в коде это признают (по отчёту).

README обещает Python 3.12+, код требует 3.13. PurePosixPath.full_match появился в 3.13, проверки версии нет, падение будет поздним.

Обновление запускает установщик из скачанного коммита без пина и подписи (harness.py:205). Pre-push выполняет скрипты из пушимого коммита (по отчёту). Для своего репозитория это нормально, для чужой ветки — нет.

Цена на каждое сообщение (по отчёту). Хук запускает sh, git и Python, делает git ls-files по всему репозиторию, читает и хеширует все 392 записи (2,6 МБ) без кеша.

Правила местами невыполнимы.

Блок формата ответа в AGENTS.md (строки 46–93) — предложения по 150 слов, часть не разбирается со второго чтения.
Ключевые слова «window», «wake», «ring», «shelf» в глоссарии отсутствуют.
Правило размещения сообщения различает «contains» и «resembles», не определяя их.
Найдены прямые противоречия: «push никогда не следует из коммита» против «пушь каждый коммит»; /verify → /maintain в цикле против «принятый срез проверяется, а не обслуживается».
Собственное правило R8 нарушают /ticket, /plan, /verify.

Церемония. Однострочная правка по этим правилам — примерно 10–20 вызовов инструментов и 2–4 таблицы в ответе (оценка агента).

Что показывает история
Мера	Значение
Коммиты ALIGN (согласование решений)	487 из 1728, 28%
IMPLEMENT + FIX	318, 18%
Коммиты, трогающие скрипты	162, 9%
Правок файлов в docs/questions	3855
Правок файлов скриптов и тестов	610
AGENTS.md	7,5 КБ → 26,7 КБ за два месяца
Код без тестов	96 КБ → 554 КБ

Проект в основном производит записи о самом себе; код — меньшая часть работы. Всегда загружаемый файл правил вырос в 3,5 раза и не сжимается.

Вердикт

Ядро (установщик, компилятор правил, валидатор хранилища) — настоящая инженерия с тестами, идеи оттуда стоит брать. Но три вещи мешают считать это готовым для чужого проекта:

Параллельные сессии — заявленная функция без блокировок.
Постоянная цена: около 27 КБ правил плюс полный перечёт хранилища на каждое сообщение, независимо от размера задачи.
Правила написаны языком, который понятен только изнутри проекта, и уже противоречат сами себе.

Первое чинится за дни. Второе и третье — следствие того, как проект растёт, и требуют вычитания, а не добавления.
```
