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
| An unknown header line vanishes silently at the next write | does not hold — the reader reports it, "`…` is not a part of an entry" |
| `git init` runs before the checks | holds in part — only into an empty folder inside no repository, and reported; a later refusal leaves the folder a repository |
| The README promises Python 3.12+, the code needs 3.13 | holds — `PurePosixPath.full_match` in harness.py and inject_rules.py, no version check |
| An update runs the installer of the fetched commit, unsigned | holds — the commit is resolved and named, nothing verifies it |
| The person's local home path stands in 328 public files | holds, smaller — 77 tracked files, 74 of them in `docs/cases` (93 MB) |

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

Вторая оценка, уже по коду: проект инженерно добротнее, чем средний «набор промптов», но его
главные обещания (несколько сессий сразу, «отказ ничего не пишет», лёгкость для мелкой работы) код
и правила выполняют лишь частично.

**На чём основано.** Запущено: тесты — 1163, все прошли (6 пропущено, 1 ожидаемый провал),
7 минут на прогон. Посчитано: вся история, 1728 коммитов. Прочитано целиком (тремя агентами
параллельно): questions.py, sessions.py, docs_corpus.py, edges.py, harness.py, inject_rules.py,
mechanisms.py, hook.sh, AGENTS.md, глоссарий, все 25 SKILL.md. Перепроверено по исходникам:
отсутствие блокировок, неатомарная запись, потеря строк заголовка, git init до проверок, запуск
чужого установщика при обновлении, требование Python 3.13. Не прочитано: сами тесты, большая часть
описаний механизмов и побочных файлов скиллов, корпус docs/. Установщик не запускался.

**Что подтвердилось как сильное.**
- Установщик осторожен с чужим проектом. Читает git-объекты, а не рабочее дерево; отказывается
  перезаписывать существующие AGENTS.md, чужой pre-push хук, отредактированные файлы; на Windows
  вместо симлинка выдаёт точную команду mklink.
- Компиляция правил дисциплинирована: один источник, блоки `<installed>`, побайтовое сравнение,
  проверяемый дрейф.
- Хранилище вопросов валидирует весь черновик до записи и перечитывает байты перед ней. Хук не
  роняет хост.
- Ссылки в скиллах настоящие: из 16 проверенных флагов и файлов существуют 15.
- /impact и /verify — компактные и содержательные. «Прогон с нулём тестов — не проверка» —
  хорошее правило.

**Что оказалось хуже, чем заявлено.**
- Параллельные сессии не защищены. В скриптах нет ни одной блокировки. Записи вопросов пишутся
  через write_text, не атомарно, хотя атомарная `_replace` лежит рядом. Проверка и запись
  разнесены: две сессии, правящие одну запись, обе проходят, побеждает последняя.
- Запись молча теряет данные: `_entry_text` выводит только известные поля, нераспознанная строка
  заголовка исчезает при следующей записи.
- «Every refusal writes nothing» — неправда: git init выполняется до проверок; main ловит только
  Refused, OSError посреди установки оставит часть файлов без отчёта; отката нет.
- README обещает Python 3.12+, код требует 3.13 (`PurePosixPath.full_match`), проверки версии нет.
- Обновление запускает установщик из скачанного коммита без пина и подписи. Pre-push выполняет
  скрипты из пушимого коммита.
- Цена на каждое сообщение: хук запускает sh, git и Python, делает git ls-files по всему
  репозиторию, читает и хеширует все 392 записи (2,6 МБ) без кеша.
- Правила местами невыполнимы: блок формата ответа в AGENTS.md — предложения по 150 слов;
  «window», «wake», «ring», «shelf» в глоссарии отсутствуют; «contains» и «resembles» не
  определены; противоречия «push никогда не следует из коммита» против «пушь каждый коммит»,
  /verify → /maintain в цикле против «принятый срез проверяется, а не обслуживается»; правило R8
  нарушают /ticket, /plan, /verify.
- Церемония: однострочная правка — примерно 10–20 вызовов инструментов и 2–4 таблицы в ответе.

**Что показывает история.**

| Мера | Значение |
|---|---|
| Коммиты ALIGN | 487 из 1728, 28% |
| IMPLEMENT + FIX | 318, 18% |
| Коммиты, трогающие скрипты | 162, 9% |
| Правок файлов в docs/questions | 3855 |
| Правок файлов скриптов и тестов | 610 |
| AGENTS.md | 7,5 КБ → 26,7 КБ за два месяца |
| Код без тестов | 96 КБ → 554 КБ |

**Вердикт.** Ядро (установщик, компилятор правил, валидатор хранилища) — настоящая инженерия с
тестами. Три вещи мешают считать это готовым для чужого проекта: параллельные сессии без
блокировок; постоянная цена — около 27 КБ правил плюс полный перечёт хранилища на каждое
сообщение; правила написаны языком, понятным только изнутри, и уже противоречат сами себе. Первое
чинится за дни. Второе и третье — следствие того, как проект растёт, и требуют вычитания, а не
добавления.

Об открытом репозитории: в публичных файлах встречается локальный домашний путь — имя
пользователя Windows и сырые транскрипты сессий лежат в открытом доступе; `docs/cases` — 92 МБ
сырых дампов сессий и API-запросов.
