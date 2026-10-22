# The cold quiz on xuanxue-cabinet — sample, key and points

- **record of** what happened
- **evidence for** [q-0038.0001](../questions/q-0038.0001-does-working-under-the-harness-deliver-software-better-than-working-without-it-measured-on-the-same-tasks.md)

The recipe is q-0038.0001's: a fresh agent, told nothing of the harness or of a measurement, is
given the repository and eleven questions in plain language — five settled decisions with their
reasons, three items in flight, three undecided — and answers from the repository alone, git
history and the GitHub PR list included. Answers are scored against the key below: **hit**, the
fact and its reason or state; **partial**, the fact without the reason, or the reason wrong;
**miss**. The sample is fixed for points 1 and 2; point 3 draws a fresh one.

## Sample taken 2026-10-23, at `main` `20128fbd` (572 commits)

### Settled decisions

| # | question, as the agent reads it | key |
|---|---|---|
| 1 | Как устроена сессия пользователя — формат, где хранится, срок жизни — и почему так, а не библиотекой? | ADR-0012: HMAC-SHA256 JWT собран руками на встроенном `crypto`, httpOnly cookie, без `jsonwebtoken` и `cookie-parser`. Причина: правило «предпочитаем встроенное, когда разница — пара функций»; роли берутся из БД на каждом запросе, не из токена. Срок: 90 дней с последнего использования, перевыпуск после 7 дней. |
| 2 | Есть ли в кабинете доступ к материалам «после оплаты»? Что решено и почему? | Нет. ADR-0048 (2026-09-18) завёл отметку `paid` и рубильник школы; ADR-0096 (2026-09-21) отменил: механика ни дня не работала по назначению, слова «после оплаты» противоречат духу школы — решение владельца. Остались уровни `all` и `staff`. Попадание требует увидеть отмену. |
| 3 | Откуда берётся часовой пояс, в котором человек видит время? Хранится ли он в профиле? Почему? | ADR-0060: пояс зрителя — с устройства; поле `users.tz` удалено (миграция `0010-drop-user-tz`). Причина: поле писалось только `SCHOOL_TZ` и никем не читалось, время и так показывалось по часам браузера. Пояс школы и занятия — отдельно, не тронуты. |
| 4 | Как код попадает на прод? Кто и что запускает, и почему именно так? | ADR-0144: только по команде владельца — `release.yml` с `workflow_dispatch`, ночной cron из ADR-0142 убран. Причина: прод с реальными данными учеников не должен обновляться сам. Стейджинг из `main` остаётся; бэкап перед промоутом остаётся; `release-hold` блокирует промоут. |
| 5 | Как устроена cookie сессии на проде и стейджинге — имя, домен — и зачем различие? | ADR-0183: профиль по origin `PUBLIC_URL`: прод `session` с `Domain=xuanxue.su` — общая с wiki (Daychi) по контракту Workshop web-wiki-session; стейджинг `session_staging` со своим доменом, потому что cookie прода долетает до `staging.xuanxue.su`, а у стейджинга свой секрет и база; две одноимённые cookie — 401. |

### In flight

| # | question | key |
|---|---|---|
| 6 | Что происходит с PR про AbortError в браузере — в чём суть и в каком он состоянии? | PR #557 (gregoryKot, с 2026-10-03), открыт: отменённая браузером операция (`AbortError`, iPhone Safari на `/attempts/:id`) не должна будить владельца как сбой — `isCancellation` по имени ошибки; в чеклисте «CI зелёный» не отмечен. |
| 7 | Переход вызовов API на карту маршрутов — apiRoute вместо строкового apiFetch: в каком состоянии, сколько осталось? | Завершён 2026-09-29, осталось ноль: карта `shared/src/api-routes.ts`, `@ApiRoute`, e2e-сверка с Nest (ADR-0148); перенос по доменам сделан тем же днём (PR #484, #488–#493), храповик прошёл 95 → 0 и удалён, строковый `apiFetch` прикладному коду запрещён eslint; остались мосты — предзагрузка первого экрана и тесты. PLAN §17.1, шаги 1–3 помечены «Сделано». *Ключ исправлен после прогона: первая версия читала шаг 2 как незавершённый, не дочитав его до пометки «Сделано» — ошибка составителя, не документа.* |
| 8 | Над чем шла работа в последнюю неделю? Назови главный поток. | Напоминания о занятиях — общий выбор для веба и Daychi: PR #603–#609 (2026-10-19/20), `PATCH /me/notifications/lessons/sync`, снимок настроек `GET`, lead 0 = в начале занятия, строгий разбор и пауза по Retry-After; ADR-0185 — один маршрут, два credential, по контракту Workshop reminder-sync. |

### Undecided

| # | question | key |
|---|---|---|
| 9 | Решено ли, обязателен ли ввод суммы при фиксации оплаты? Кто должен решить? | Не решено. Сейчас необязательна (ADR-0049); PLAN §16 — вопрос к Маше: если нужен денежный итог за месяц, сумма становится обязательной, и это другая фича. |
| 10 | Задержка ~90 мс на обращение к базе: известна ли причина и что решено делать? | Причина — гипотеза, не факт: сеть между континентами, Railway в Амстердаме (сверено 2026-10-02), регион Atlas не подтверждён — нужен вход владельца. Что делать — не решено; сравнивать тарифы имеет смысл после того, как база и сервис в одном регионе. PLAN §17.2, RUNBOOK §8.21, §8.23. |
| 11 | Решено ли, с какого адреса будут уходить письма кабинета? Что известно? | Не решено: домен `xuanxue.su` есть (ADR-0009), адрес — открытый вопрос к школе, PLAN §10. |

## Point 1 — before install, 2026-10-23

The run: a fresh general-purpose agent on Opus, told nothing of the harness or of a measurement,
given the repository and the eleven questions; read-only. **11 of 11 hits.** Every fact and its
reason or state, with sources named; on question 7 the agent was right and the key wrong, and the
key was corrected above.

| | |
|---|---|
| hits / partial / miss | 11 / 0 / 0 |
| tokens | 151,675 |
| tool uses | 34 |
| wall time | 205 s |
| files read | ~25–30: ~15 ADRs whole, ~10 large documents by search, a few sources to confirm |

Beyond the key, unasked, the agent found five places where the tree disagrees with itself:
PLAN §14 cites a test `material-files.e2e-spec.ts` no longer holds; SECURITY.md §1 still lists
the time zone among students' personal data though `users.tz` is gone (ADR-0060); RUNBOOK line
1685 still speaks of the nightly release ADR-0144 removed; a comment in `prefetchFirstScreen.ts`
names a script `scripts/string-api-fetch-bridges.mjs` that does not exist; PLAN §16 discusses a
ceiling for an amount field the payments screen no longer has (ADR-0171). And one thing no record
explains: PR #557 is green, mergeable and 46 commits behind `main`, abandoned twenty days under a
rule (ADR-0147) that says the agent merges such a PR itself.

What slowed it, in its words: PLAN.md is readable only by search; decisions sit in chains of ADRs
that cancel one another (0048 → 0096, 0002 → 0142 → 0144 → 0147, 0157 → 0171); `gh pr view
--comments` printed nothing.

**What the point says.** The facts are all in the tree — 185 ADRs with a status line each, a plan
whose sections carry state — and *reaching* them cost a capable agent ~150k tokens, 34 tool calls
and three and a half minutes of search through a 3,400-line plan and chains of ADRs that cancel one
another. That a fact is written is not the same as its being accessible: the cost is the measure of
accessibility, and it is the column the harness claims to move. So points 2 and 3 score four
columns, not one: hits; the cost of the reconstruction; the drift a cold reader meets that nobody
had caught; and what the records cannot explain — the abandoned PR. Same sample for point 2, a
fresh one for point 3. A hit rate alone would read as *nothing to gain here*, and that reading would
be wrong.

## Run 1, raw return — Opus, 2026-10-23, 151,675 tokens, 34 tool uses, 205 s

Filed as it came back, unedited. The agent's prompt: a developer new to the repository, eleven
questions, answers from files, git history and the PR list only, nothing changed, no network; each
answer 3–6 sentences — the fact, its reason or state, where it was found; contradictions between
documents to be named; a closing section on how it searched.

> Ответы по репозиторию D:\Dev\workspaces\taichi_workspace\xuanxue-cabinet (main = origin/main, последний коммит 20128fbd от 2026-10-20). В репозитории ничего не менял.
>
> **1. Сессия пользователя.**
> Сессия — это JWT с подписью HMAC-SHA256, собранный вручную на встроенном `crypto`, в httpOnly-cookie. В токене только `userId`, роли читаются из БД на каждом запросе. На сервере сессия не хранится. Срок — «90 дней с последнего использования», а не абсолютный потолок: если токену больше 7 дней (`SESSION_MAX_AGE_DAYS=90`, `SESSION_RENEW_AFTER_DAYS=7`, `api/src/auth/session-renewal.ts`), гвард перевыпускает cookie. Библиотеки `jsonwebtoken`/`jose`, `express-session` с Mongo store и `cookie-parser` отвергнуты: по правилу CLAUDE.md «предпочитаем встроенное», если разница в паре функций. Серверное состояние тоже не нужно: сессии не отзывают по одной, а вход не должен зависеть от Mongo. Цена решения — ротация `JWT_SECRET` разлогинивает всех. Источники: ADR-0012, ADR-0005, SECURITY.md §2 (строки 54–72). Противоречий не нашёл.
>
> **2. Доступ к материалам «после оплаты».**
> Такого доступа нет. ADR-0048 (2026-09-18) ввёл отметку `access: 'paid'` и рубильник школы. Через три дня ADR-0096 (2026-09-21) его отменил решением владельца: такие слова «противоречат духу школы», а механика ни дня не работала по назначению, потому что оплат в кабинете тогда не было. Механику удалили целиком, миграция 0014 перевела `paid` в `all`. У материала остались уровни `all` и `staff`. Если доступ по оплате когда-нибудь понадобится, это будет новый ADR, а не воскрешение старого. Источники: ADR-0096, PLAN.md §5, этап 3 (строки 309–310), DATABASE-таблица в PLAN (строка 223).
> Нестыковка: PLAN.md §14 (строка ~2535) ссылается на тест «ученик без оплаты не получает 302 на файл закрытого материала» в `material-files.e2e-spec.ts`. В самом файле такого теста больше нет.
>
> **3. Часовой пояс зрителя.**
> Пояс берётся с устройства: `formatDate.ts` форматирует без явного `timeZone`, то есть по часам браузера. Рядом подписывается пояс школы, если он другой. В профиле пояс не хранится: поле `users.tz` удалено из схемы и из `MeDto`, миграция `0010-drop-user-tz`. Причины две. Поле всегда писалось одним значением `SCHOOL_TZ` и ни на что не влияло. Сохранённый пояс может устареть после переезда, а пояс устройства — нет. Расчёты «когда» живут в поясе занятия (`classes.tz`) и школы (`settings.tz`, ADR-0003). Источники: ADR-0060, PLAN.md «Время и часовые пояса» (строка 113), CLAUDE.md строка 459.
> Нестыковка: SECURITY.md §1, п. 2 (строка 19) всё ещё перечисляет «часовой пояс» среди персональных данных учеников.
>
> **4. Как код попадает на прод.**
> Merge в `main` выкатывает только на стейджинг (`staging.xuanxue.su`). PR, открытый агентом, этот же агент сам мержит squash'ем, когда CI зелёный (ADR-0147). Прод собирается из ветки `release`, а её двигает только workflow `release.yml`, причём только через `workflow_dispatch` по команде владельца:
> - `gh workflow run release.yml -f mode=promote` — без `sha` берётся самый новый зелёный коммит `main`, отстоявший 2 часа на здоровом стейджинге;
> - с `sha` — хотфикс без выдержки;
> - `mode=rollback` — откат.
>
> Перед каждым promote снимается бэкап, после выката ждётся `/api/health` с нужным коммитом и уходит алерт в Telegram. Пока открыт issue `release-hold`, промоут отказывает. Почему так: после запуска 2026-09-28 баги доходили до учителя раньше, чем до разработчика (ADR-0142). Ночной cron из ADR-0142 убрали, потому что владелец хочет сам решать момент выката (ADR-0144). Источники: ADR-0002 → 0142 → 0144 → 0147, `.github/workflows/release.yml`, RUNBOOK §2.
> Мелкий хвост: RUNBOOK строка 1685 всё ещё упоминает «ночной выкат».
>
> **5. Cookie сессии на проде и стейджинге.**
> Профиль выбирается по origin `PUBLIC_URL`, таблица зашита в `auth/session-cookie.ts`:
>
> | Окружение | Имя | Domain | Secure |
> |---|---|---|---|
> | прод | `session` | `xuanxue.su` | да |
> | стейджинг | `session_staging` | `staging.xuanxue.su` | да |
> | любой другой адрес | `session` | host-only | только для https |
>
> Атрибуты везде `HttpOnly`, `SameSite=Lax`, `Path=/`. Каждый выпуск сначала гасит прежнюю host-only `session`. Две одноимённые cookie дают 401, а не выбор первой из них. Зачем различие: прод ставит общую cookie на весь домен, чтобы её видела wiki `wiki.xuanxue.su` (проект Daychi, контракт Workshop web-wiki-session). Браузер присылает её и на `staging.xuanxue.su`, а у стейджинга свой секрет и своя база. Оба окружения работают с `NODE_ENV=production`, поэтому их различает адрес, а не отдельная env-переменная, которую можно забыть. Источники: ADR-0183, SECURITY.md §2, RUNBOOK строки 278–280, PR #591.
>
> **6. PR про AbortError.**
> Это PR #557 «fix(web): отменённая браузером операция (AbortError) не будит владельца как сбой», ветка `fix/attempt-abort-error`. Суть: 2026-10-03 владельцу пришёл «Сбой в браузере» с iPhone Safari на `/attempts/:id`, хотя у ученика ничего не сломалось. Так WebKit отклоняет прерванный `video.play()` и отменённый fetch, а у DOMException в Safari нет стека, и фильтр счёл ошибку «нашей». PR добавляет `isCancellation`: отказ промиса с `name === 'AbortError'` не отправляется. В PR тесты, правки ADR-0071 и RUNBOOK.
> Состояние: открыт с 2026-10-03, не draft. CI на голове зелёный, GitHub показывает MERGEABLE/CLEAN, ревью и комментариев нет. В `main` правки нет: `isCancellation` в `web/src` отсутствует. Ветка отстала от `main` на 46 коммитов, RUNBOOK менялся с обеих сторон, но локальный merge-tree конфликтных маркеров не дал. По ADR-0147 агент должен был смержить такой PR сам, так что PR фактически брошен уже 20 дней. Причины в репозитории не записаны.
>
> **7. Переход на `apiRoute`.**
> Переход завершён, осталось ноль. Шаг 1 (карта `shared/src/api-routes.ts`, `apiRoute`, `@ApiRoute`, e2e-сверка) сделан 2026-09-29. Шаги 2–3 сделаны в тот же день (PR #484, #488–#493): храповик `check-string-api-fetch-ratchet.mjs` прошёл 95 → 0 и удалён. Строковый `apiFetch` прикладному коду запрещён eslint (`no-restricted-imports`). Исключения-мосты — предзагрузка первого экрана (`web/src/app/prefetchFirstScreen.ts`) и тесты. Источники: ADR-0148 (раздел «Последствия»), PLAN.md §17.1, `eslint.config.mjs` (`STRING_API_FETCH_BRIDGES`).
> Мелкая нестыковка: комментарий в `prefetchFirstScreen.ts` ссылается на `scripts/string-api-fetch-bridges.mjs`, которого нет.
>
> **8. Работа за последнюю неделю.**
> Коммиты есть с 18 по 20 октября, с 21 по 23 октября их нет. Главный поток — общие настройки напоминаний о занятиях для веба кабинета и приложения Daychi (ADR-0185, контракт Workshop reminder-sync, issue #17). Он шёл серией PR #603–#610:
> - `GET` и `PATCH /me/notifications/lessons/sync` по cookie и по native bearer;
> - экран настроек через этот маршрут;
> - доставка напоминаний по новому выбору и переход на него (cutover);
> - исправления разбора и тестов.
>
> Рядом были #602 (бюджет `native/me` по гранту) и #600–#601 (кнопки входа). Неделей раньше, 10–14 октября, шла та же интеграция с Daychi: нативный вход (ADR-0181), профили cookie и вход из wiki (ADR-0183, #591–#595). Общий поток — интеграция кабинета с Daychi по контрактам Workshop.
>
> **9. Обязателен ли ввод суммы при фиксации оплаты.**
> Нет, не решено окончательно. Сейчас сумма необязательна: в ADR-0049 поле `amountMinor?` в агоротах. На экране «Оплаты» поля суммы нет вообще, подтверждение — одна кнопка (ADR-0171, PLAN §15). Довод: «заставлять Машу вбивать число ради галочки значит вернуть ей её файл». Вопрос открыт в PLAN.md §16 «Что нужно от Маши и Димы до конца этапа 2», пункт «Нужен ли ввод суммы вообще», не зачёркнут. Если Маше (админ, ведёт оплаты) нужен денежный итог за месяц, сумма станет обязательной, и это будет отдельная фича. Решать должны Маша и Дима, то есть школа, а не разработка.
> Нестыковка: там же, в §16, обсуждается «потолок суммы в форме» (100 000 ₪), хотя поля суммы на экране нет.
>
> **10. Задержка ~90 мс на обращение к базе.**
> Причина известна как вывод из замеров, но до конца не подтверждена. Замер 2026-09-29 (`scripts/measure-ttfb.mjs`) показал около 90 мс на каждое последовательное обращение к Mongo; Nest и прокси дают 0–3 мс. Объяснение — сеть между континентами. Railway сверен 2026-10-02: EU West, Амстердам. Регион кластера Atlas так и не сверен (нужен вход владельца в панель), предположительно `us-east-1`. Обработчики эту задержку умножают: от 2 до ~11 шагов, итого 0,5–1,1 с. PLAN предлагает варианты А–Г и рекомендует А — перенести кластер Atlas в регион сервиса. Решение за владельцем, и оно не принято: следующий шаг — сверка региона Atlas и замер из Израиля. Независимо от этого можно сделать PR «меньше последовательных шагов к базе», но его тоже не сделали. Источники: PLAN.md §17.2, RUNBOOK §8.21 и §8.23 (строка 1708), PR #463.
>
> **11. Адрес отправки писем кабинета.**
> Конкретного адреса нет. ADR-0009 решает только, что почта уходит «с адреса на этом же домене» (`xuanxue.su`) через Resend с SPF/DKIM/DMARC. В `.env.example` переменная `MAIL_FROM=` пустая. RUNBOOK §2 даёт лишь пример: `Сюань-Сюэ <school@mail.xuanxue.su>`, поддомен тоже допустим. ADR-0029 отмечает, что домен для писем и DNS-записи должен дать владелец школы. Включён ли email-вход на проде, в репозитории не известно: DATABASE.md пишет «Включён ли на проде: **проверяет владелец**». На стейджинге `RESEND_API_KEY` и `MAIL_FROM` пустые. Почта нужна только для входа и подтверждения адреса, уведомления по почте не идут (ADR-0061, лимит Resend 100 писем в сутки).
>
> **Как я искал.**
> - Полезнее всего оказались `docs/adr/` (185 ADR с говорящими именами файлов, у каждого статус «отменено/заменено» в шапке), `docs/PLAN.md` (там разделы §16 «что нужно от Маши и Димы» и §17 «долги» с текущим состоянием), а также `docs/SECURITY.md`, `docs/RUNBOOK.md`, `.env.example` и `.github/workflows/release.yml`.
> - Команды: `ls docs/adr`, `grep` по ключевым словам (пояс, оплат, сумм, MAIL_FROM, apiRoute), `git log --oneline`, `git log --since`, `gh pr list --state all/open`, `gh pr view 557 --json …`, legacy `git merge-tree` для проверки конфликтов.
> - Прочитал примерно 15 ADR целиком и около 10 больших документов фрагментами через `grep`/`sed`, плюс несколько исходников для сверки. Всего около 25–30 файлов.
> - Мешало вот что. PLAN.md огромный (больше 3000 строк), и читать его можно только поиском. Решения разбросаны по цепочкам ADR, которые отменяют друг друга (0048 → 0096, 0002 → 0142 → 0144 → 0147, 0157 → 0171). `gh pr view --comments` ничего не вывел, пришлось брать JSON. Местный git старый, без `merge-tree --write-tree`.
