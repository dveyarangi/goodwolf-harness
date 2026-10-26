# q-0038 What landscape does this project evolve in?

- **record of** what it intends to become
- **state** open
- **struck** 4, last 2026-10-26T10:32Z

**A peer harness built by one person for their own work, the user, 2026-10-25** — its agent's
account of itself, filed as
[peer-harness-self-report-2026-10-23](../research/peer-harness-self-report-2026-10-23.md). It
has eight things this harness lacks: a ladder of executors priced by cost, a budget ledger, an
instrument examined before it is used, a registry of hypotheses with verdicts, a judge from another
vendor, routines on a clock, mechanical checks on what a model quotes, and a single idempotent
writer. Like this tree, it records that the person catches every failure.

## 2026-10-26 — ClawRush, CharmOS and GoodWolf, a cold comparison

The user asked for an assessment and comparison. A fresh reader was given the repositories and the question of what each helps a person do, without this session's conclusions. The brief selected long-running delegated work as its frame and asked for alternative families, failure modes, confidence and the assumptions it supplied. The reader cloned the subjects afresh, read the additional primary sources named below, changed no source tree and ran no project code or tests. Its material follows verbatim; it is evidence, not a decision or an instruction.

> ## Families
>
> Читал холодные клоны: GoodWolf `49ceb1d`, CharmOS `9b9fa1d`, ClawRush `6b72ca0`; дополнительно — `claude-bible` README/SPEC, `agent-leash` README и `sqlite-graph-memory/bench/README.md` через GitHub. Исходное дерево не менял, проектный код и тесты не запускал. Ниже четыре самостоятельные трактовки; шкалы — аналитические, без общей оценки «зрелости».
>
> **1. «Вынесенная наружу память человека, продолжающая работу между сеансами».**
>
> Структурная связь: обе системы хранят материал вне контекста модели и возвращают его перед действием. Но объект памяти различен. CharmOS ориентирован на личный корпус, людей, агентов и прошлые разговоры; GoodWolf — на состояние проекта: вопросы, решения, основания, незавершённую работу. **Уверенность высокая**: это видно в [коде TurnState](https://github.com/tonydzi/charm-os/blob/main/modules/turnstate/turnstate_hook.py), [RDR](https://github.com/tonydzi/charm-os/blob/main/modules/rdr/rdr.py) и [архитектуре GoodWolf](/D:/Dev/AI/agents/docs/architecture.md).
>
> Шкала семейства: **архив → поиск → учёт актуальности и противоречий → проверенная помощь на новых задачах**. CharmOS публикует работающие по структуре архиватор и лексический поиск; семантический vault и CRM в этом репозитории остаются преимущественно архитектурным намерением. GoodWolf публикует более развитую организацию актуальности: типы документов, принятые решения, открытые вопросы, условные положения. Это не доказывает правильность восстановленного понимания. **Уверенность высокая о механизмах, низкая о сравнительном результате для человека.**
>
> Типовые сбои: сохранили текст, но не смысл; нашли прежнее решение, но приняли отменённое за действующее; индекс выглядит живым при остановившейся записи. Последнее прямо описано в [ClawRush: every-session-starts-with-recall](https://github.com/tonydzi/clawrush/blob/main/devlog/every-session-starts-with-recall.md). Опубликованный [memory-bench](https://github.com/tonydzi/sqlite-graph-memory/blob/main/bench/README.md) особенно показателен: **202 синтетические заметки, 91 вопрос; на шести вопросах об актуальном сроке извлечение находит нужные документы, но простой экстрактор 6/6 раз выбирает отменённое решение**. Это свидетельство конкретного дефекта опубликованной цепочки, не оценка всей частной системы и не проверка GoodWolf.
>
> **2. «Система ведения дела: удержать вопрос, доводы и право решить».**
>
> Здесь единица ценности — не найденная заметка, а решение, которое можно продолжить и пересмотреть с основаниями. У CharmOS это RDR и Decision Memo; у GoodWolf — дерево вопросов, `/align`, связанные решения и delivery ring. **Уверенность высокая.**
>
> Шкала: **шаблон решения → прослеживаемая история → управляемый переход от решения к работе → доказанная экономия человеческих решений**. GoodWolf структурно дальше по третьей ступени: вопрос связывается с работой, положением сессии и тем, что потребует переписывания. RDR пока предоставляет поиск, генерацию исследовательского промпта и каркас memo; код не обеспечивает обязательное прохождение цепочки. См. [rdr.py](https://github.com/tonydzi/charm-os/blob/main/modules/rdr/rdr.py), [GoodWolf questions.py](/D:/Dev/AI/agents/.agents/scripts/gw/questions.py), [AGENTS.md](/D:/Dev/AI/agents/AGENTS.md).
>
> Типовые сбои: неверно определить, какой вопрос содержит сообщение; завести избыточную бюрократию; учитывать закрытые вопросы вместо достигнутых результатов. GoodWolf имеет предметный [window test](/D:/Dev/AI/agents/docs/research/window-test-2026-09-28.md): **83 испытания**, хорошие близкие размещения, **два неверных корня из семи дальних переходов**. Но большие хранилища составлены копированием одной таксономии; дальний переход оценивался только на первом шаге. **Уверенность средняя в полезности окна, низкая в переносе результата на произвольные многолетние проекты.**
>
> **3. «Конституция делегирования: кто что вправе делать и как правило достигает действия».**
>
> Это самое плотное пересечение, которое легко пропустить, сравнивая GoodWolf только с CharmOS. Ближайший внешний собеседник — [claude-bible SPEC](https://github.com/tonydzi/claude-bible/blob/main/docs/SPEC.md): один дом правила, сжатый индекс, загрузка по случаю, источник полномочия, отменённые решения, обязательный вызывающий механизм. GoodWolf добавляет механическое распространение правил по адресатам, проверки расхождения и настройки установки: [inject_rules.py](/D:/Dev/AI/agents/.agents/scripts/gw/inject_rules.py). **Уверенность высокая.**
>
> Шкала: **правила в тексте → доставка правил в нужный момент → техническое ограничение действия → проверенная устойчивость к обходу**. GoodWolf сильнее представлен на второй ступени и в проверках целостности распространения. Публичный `claude-bible` — спецификация, шаблоны и примеры; [agent-leash](https://github.com/tonydzi/agent-leash) — модель контроля и scorecard, прямо обещающие работающий пример policy gate следующим шагом. Поэтому частную эксплуатацию нельзя считать целиком поставленной защитой.
>
> CharmOS публикует проверяемый постфактум прибор: [invariants.py](https://github.com/tonydzi/charm-os/blob/main/modules/eval-harness/invariants.py) и [scorecard](https://github.com/tonydzi/charm-os/blob/main/modules/eval-harness/benchmarks/consensus-safety-v0/scorecard.json): **317 событий, 64 решения; human gate 4/4 применимых случаев; независимая проверка 3/39**. Код проверяет события с отметками времени и различие `actor` у VERIFY/COMMIT. Он не удостоверяет человеческую личность, независимость мышления, правильность риск-класса или выполнение реального действия. **Уверенность высокая в узости измеряемого контракта; недостаточно данных для утверждения «флот безопасен».**
>
> Типовой сбой семейства — правило существует, но не достигает действия; либо достигает, но остаётся рекомендацией. Ни число правил, ни зелёная проверка формата не измеряют соблюдение всех смысловых обязательств.
>
> **4. «Лаборатория собственного способа работать».**
>
> Обе системы можно целиком прочитать как исследовательскую практику: эксплуатация обнаруживает отказ, отказ превращается в правило или прибор, следующая эксплуатация испытывает изменение. Здесь продукт — способность исправлять метод, а не сама память или workflow. **Уверенность высокая в структурном соответствии.**
>
> Шкала: **истории успеха → датированные отрицательные случаи → сохраняемые приборы и воспроизводимые результаты → независимые повторения и сравнение с альтернативой**. Обе вышли за рассказы. ClawRush публикует неудачные замены retrieval-компонентов и [оценочный скрипт](https://github.com/tonydzi/clawrush/blob/main/artifacts/brain_gold_eval.py); GoodWolf — тесты отказов, исходники экспериментов и [измерения затрат](/D:/Dev/AI/agents/docs/research/measures-2026-10-11/REPORT.md). Но обе практики существенно зависят от собственных операторов.
>
> GoodWolf сообщает **187 Claude Code сессий и 7,9 млрд учтённых токенов, 98,1% — повторное чтение из кэша**. Сам отчёт прямо запрещает причинное сравнение двух разных проектов. Это измерение нагрузки, не доказательство экономии. У ClawRush частные corpus/индексы и исходные эксплуатационные данные также ограничивают независимое повторение. **Уверенность высокая в наличии исследовательской дисциплины, низкая в доказанном превосходстве любого подхода.**
>
> ## What the tasking smuggled in
>
> - Слово «два подхода» делает едиными объектами дневник, частную эксплуатацию, набор отдельных репозиториев и переносимый harness. Их границы различаются.
> - «Длительная работа» заранее делает память главным объяснением; возможные реальные выигрыши — доступ к каналам, автоматизация рутины, качество оператора — остаются за рамкой.
> - «Что работает» смешивает исполнение скрипта, соблюдение процедуры, правильность решения и пользу человеку. Для каждого нужны разные данные.
> - Чтение GoodWolf его собственными инструкциями создаёт опасность принять его нормативную картину за наблюдаемое поведение. Здесь инструкции рассматривались как предмет исследования.
> - Нет общего набора задач, равного бюджета, общего оператора и измерения до/после. Честного рейтинга эффективности из этих источников не получается.
>
> ## Nothing to take
>
> Не беру семейство **«цифровой двойник личности»**: открытые механизмы подтверждают память и процедуры, но не воспроизведение личности на независимом hold-out.
>
> Не беру **«распределённая операционная система»**: машины и переговоры описаны, но сравниваемый GoodWolf не предоставляет соответствующий runtime, а открытый CharmOS не равен частному флоту.
>
> Не беру **«полноценный CRM против harness»** как сравнение готовых продуктов: CRM в CharmOS представлен моделью и синтетическими примерами; соответствующей задачи у GoodWolf нет. Это различие намерений, не состязание реализаций.
>

## 2026-10-26 — mechanisms to learn from BMAD

The user asked whether BMAD contains useful mechanisms for this harness. This is a source
inspection, not a trial of their effect. The inspected `main` tree was
[`61e01f82644c4bb533750cfa0d6d61ab61d2cc9b`](https://github.com/bmad-code-org/BMAD-METHOD/tree/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b).
Its README calls this line v7 preview alpha and keeps stable v6.12 separately. The earlier
[peer comparison](../research/peer-capabilities-2026-10-08.md#bmad-method-bmad-code-orgbmad-method)
and [context counts](../research/context-tax-peers-2026-10-11.md) remain dated observations;
their counts were not remeasured here. No BMAD workflow or test was executed.

Candidate transfers, not adopted decisions:

- **Lossless review triage.**
  [Triage](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/skills/bmad-code-review/step-03-triage.md)
  records every raw finding before deduplication, verifies its particular claim before assigning
  severity, retains refutations and uncertainty, then groups by shared root cause with links back
  to raw findings. The useful unit here is that accounting discipline, not a new reviewer role.
  The [edge-case lens](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/skills/bmad-build/review-prompts/edge-case-hunter.md)
  traces code before reading the plan's claims. Review is already being reconsidered under
  [q-0037.0015](q-0037.0015-how-is-produced-work-gone-over-again-over-what-scope-by-what-criteria-by-whom-and-to-what.md);
  this inspection settles none of that work. Limit: triage automatically trusts verification-gap
  findings, and that lens excludes prompts, skills and documents from its test-gap screen; those
  choices do not establish their suitability for a repository whose product includes instructions.
- **Executable skill evaluations, particularly activation.**
  [bmad-eval](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/skills/bmad-eval/SKILL.md)
  provides baseline, variant, quality and trigger modes, with runner scripts and script tests in
  the source tree. The inspected runners stage separate workspaces and record transcripts and
  run status. The [description loop](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/skills/bmad-eval/references/description-optimization.md)
  uses near-miss positive and negative queries, a fixed stratified train/test split, repeated runs
  and a score hidden from the description's author. That same set selects the winning variant
  and helps determine stopping, so its score is not an independent final test of the winner.
  The no-instruction/standing/new comparison is already accepted in
  [q-0037.0012.0009](q-0037.0012.0009-how-is-an-amendment-to-an-instruction-tested-before-it-lands-against-which-cases-chosen.md);
  BMAD offers implementation material, not a reason to reopen that decision. Its trigger runner
  uses an output canary as a proxy for activation. A clean workspace is not containment: its
  documented Codex harness example bypasses approvals and the sandbox. Three runs are BMAD's
  stated reporting threshold, not evidence of statistical sufficiency.
- **A light path with an explicit return to planning.**
  [Oneshot](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/skills/bmad-build/step-oneshot.md)
  keeps the intent and records the baseline revision and implementation notes. With automatic
  routing it returns to full planning when implementation exposes a user-visible gap; an explicitly
  pinned oneshot instead stops and asks the person. This is a concrete reference
  for the still-open
  [q-0037.0013.0003](q-0037.0013.0003-how-does-the-method-lighten-for-small-work-and-weigh-more-for-large.md),
  not a proposed second delivery ring. Route selection and review depth are separate settings;
  the light route does not inherently mean skipping review.
- **A research evidence boundary.**
  [Deep Recon](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/skills/bmad-deep-recon/SKILL.md)
  lets project context shape the questions but forbids treating it as evidence of external truth;
  research children receive only their brief unless named documents are explicitly granted.
  Our [discover](../../.agents/skills/discover/SKILL.md) already isolates an outside reading.
  The distinct candidate is the evidence boundary across ordinary external research, where a
  project's own account can otherwise return disguised as independent confirmation.
- **Mining repeated corrections, as a reserve source.**
  [From logs](https://github.com/bmad-code-org/BMAD-METHOD/blob/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/skills/bmad-toolsmith/approaches/from-logs.md)
  extracts repeated requests, tool sequences and verbatim corrections, excludes installed
  coverage and proposes at most three skill candidates. This can recover missed cases, but our
  accepted evaluation design already keeps retrospective transcript reading as a reserve behind
  capturing failures when they happen. It supplies no reason to add a parallel failure register.

The independent reading below received only the question of choosing practices from another
AI development process for an existing process that preserves decisions between sessions. It
was forbidden to read this repository and was given neither BMAD nor this session's candidate
list. Its material follows verbatim; it provides alternative frames, not evidence that any
candidate improves this harness.

> ## Families
>
> **1. Перенос между средами.** Шкала: *копирование при одинаковых условиях → адаптация при частичном совпадении → изобретение по мотивам*. Заимствование из чужого процесса обычно лежит посередине: переносится предполагаемая причина пользы, а её воплощение меняется. Структурное соответствие — одинаковая проблема при сопоставимых ограничениях; одинаковые файлы, команды и названия ролей его не доказывают. Провалы: перенести средство без проблемы, принять успех команды за эффект практики, не заметить, что принимающий процесс уже решает задачу другим способом. **Уверенность:** высокая в различении; низкая в положении конкретной практики без сведений о двух средах.
>
> **2. Проверка причинного эффекта.** Шкала: *правдоподобный рассказ → наблюдаемое совместное изменение → различимый эффект вмешательства*. Чужой удачный пример находится ближе к началу шкалы: он даёт гипотезу, которую можно испытывать на собственных случаях. Структурное соответствие появляется, когда можно назвать ожидаемое изменение поведения и отличить его от последствий других изменений. Провалы: одновременно заменить несколько практик; выбрать удобные случаи; считать объём записей или число проверок мерой качества; измерить ближайший выигрыш, пропустив стоимость следующих сессий. **Уверенность:** высокая в ограничениях свидетельства; средняя в возможности достаточно чистого испытания рабочего процесса.
>
> **3. Надёжность при отказах.** Шкала: *предотвращение ошибки → обнаружение → ограничение ущерба → восстановление*. Заимствование занимает место по тому, какой отказ оно обслуживает. Например, сохранённое решение помогает восстановить контекст; независимая проверка может обнаруживать ошибки — это разные функции. Структурное соответствие требует совпадения самого отказа и пути его распространения. Сходство с «памятью» или «контуром обратной связи» само по себе ничего не даёт. Провалы: добавить ещё одну проверку того, что уже проверяется; сохранить ошибочное решение надолго; усилить контроль настолько, что обход правил станет дешевле соблюдения. **Уверенность:** высокая в функциональном различении; средняя в переносимости отдельных средств защиты.
>
> **4. Изменение распределения власти.** Шкала: *личный приём → общая договорённость → обязательное правило → изменение права принимать решения*. Практика располагается здесь по своим последствиям: кто получает возможность разрешать, запрещать и пересматривать работу. Даже небольшой файл может оказаться далеко справа. Структурное соответствие — совпадение отношений между решением, его владельцем и исполнителем; сходство организационных названий недостаточно. Провалы: два конкурирующих источника истины; сохранённая рекомендация незаметно становится приказом; право пересмотра исчезает; стоимость правила оплачивает каждая сессия. **Уверенность:** высокая в полезности этого различения; низкая в оценке конкретного изменения без разбора действующих полномочий.
>
> ## What the tasking smuggled in
>
> Постановка предполагает, что:
>
> - работающий процесс стоит сохранять, хотя его работоспособность ещё не равна пригодности;
> - чужую практику можно отделить от навыков людей, инструментов и остальных договорённостей;
> - сохранение решений между сессиями — преимущество, хотя оно также сохраняет ошибки;
> - выбирать следует отдельные практики, хотя полезный эффект иногда принадлежит сочетанию;
> - заимствование вообще нужно: наблюдаемая трудность может требовать удаления собственного механизма.
>
> ## Nothing to take
>
> Заимствовать нечего, если не удаётся назвать собственную неудовлетворённую потребность, соответствующий ей механизм чужой практики и условия, при которых он перестаёт помогать. Тогда остаётся материал для вопросов. Общее присутствие ИИ, Markdown, ролей и нескольких сессий структурного соответствия не устанавливает.
