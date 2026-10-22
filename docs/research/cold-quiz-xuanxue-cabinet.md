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

**What the point says.** On this repository the baseline for *facts* is saturated: 185 ADRs with a
status line each and a plan whose sections carry state tell a cold reader nearly everything, at
~150k tokens and three and a half minutes. Headroom for points 2 and 3 is therefore not in hits but
in three other columns: the cost of the reconstruction; the drift a cold reader meets and nobody
had caught; and what the records cannot explain — the abandoned PR. Points 2 and 3 score those
columns beside the hits, on the same sample for point 2 and a fresh one for point 3.
