# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| edge | parts | 8d2bbd3bd79baa8d22b29e9cb8b6034e9aebcf213d3c09a1f71424432916a4f6 | 2026-10-11 | nothing to change |
| edge | output | f0de7776dbbda69214b5586ad6a45e117e54ef50354134ede6be93a7c0fc01c5 | 2026-10-11 | nothing to change |
| harness | parts | 930401b8a1032aaecdfb275df0d76bb900eaea85e817d280c19ea3160646ed7a | 2026-10-11 | nothing to change |
| harness | output | 4e91cab4ef12377dadf347374c0a48952ffa3f083b7783f031c010d0a0b9550a | 2026-10-11 | nothing to change |
| maintain | parts | d7ff3d8434a9d48314cfb64f01439518c5dbebe06ea74f9090f26869506de397 | 2026-10-11 | nothing to change |
| maintain | output | 7fa0a6f971f00a6d7bfd3c83b4c22f0caf2d52247a7681673477a1618a4f17d5 | 2026-10-11 | nothing to change |
| mechanism-shape | parts | a891a82d5917a1c94c813b82629e13d7dbfb49b60d544bdaa27ec8d285ccea60 | 2026-10-11 | nothing to change |
| mechanism-shape | output | 33f1873a51e9fa0bd7c97d90f156c8c4046db585ec526ca2427ae3968aed7ec7 | 2026-10-11 | amended |
| questions | parts | d60233e40888d4ef3a568da62cbae3fc685d79c286bcb061a78aea634f17b814 | 2026-10-11 | nothing to change |
| questions | output | cfa927ff11ddd5a28b0c43fcb4fc6c6f5f34d305adba17cce314e0a1eb3ce05e | 2026-10-11 | nothing to change |
| ticket | parts | 9e780abccc7d5b65f58a244453af7e689771c37c53dd43e7d1e47a6c58d0708e | 2026-10-11 | nothing to change |
| ticket | output | 9062bf0e7ba5c4ecd775b641fe6847890f784be5bb7ca6ed3acf5aa33098283c | 2026-10-11 | nothing to change |

| mechanism | level | file | fingerprint |
|---|---|---|---|
| edge | parts | .agents/mechanisms/edge/edge.rules.md | bdcb4f08fad66430c01d1c97ff1fd23d7effbe90fd971156542ec3e815381bee |
| edge | parts | .agents/scripts/gw/edges.py | 5c29ebd7f6d8db384919ce4e51ad91dfee7da292a70395854166d2e435218e73 |
| edge | parts | .agents/scripts/gw/test/test_edges.py | 799fbc6c8fa549425b9d67bd061d855e8253ae8694ce7d000e3d01caddb38cea |
| edge | parts | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | parts | .agents/skills/edge/SKILL.md | ed66631b0643c9e09d90adb09bfdc22b43ec51ce330c523b7464402c1202e21a |
| edge | output | .agents/mechanisms/edge/edge.md | 905530e3cd2922dc669ddbce412a623f84fc61cead71732c571b4339e32d394f |
| edge | output | .agents/mechanisms/edge/edge.rules.md | bdcb4f08fad66430c01d1c97ff1fd23d7effbe90fd971156542ec3e815381bee |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e8b1f916df9ebb9fce639471879486b2b229d9a07dead8ba7ba0096d2a70f039 |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 32b1cf0e4a9df8c78e9289f3248d2154b601dd171dc1f1d77050a48ad09ad9dd |
| edge | output | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | output | .agents/skills/edge/SKILL.md | ed66631b0643c9e09d90adb09bfdc22b43ec51ce330c523b7464402c1202e21a |
| edge | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2f0bfa275a6e1fec6e76b0e2223f32908a79771ebeae86abe5ba4f7d7ff45b5a |
| edge | output | .agents/skills/mechanism/SKILL.md | 4737136791c168cbff85bba5e2a1f5ac6518bb06b3f511416784e0d422cf1703 |
| harness | parts | .agents/scripts/gw/harness.py | a0dfff04c5c1edd0e1585cc88f91586d7761a0dc713a1b6000f59a657c52f108 |
| harness | parts | .agents/scripts/gw/test/test_harness.py | e8c416467d24a3705c25715d2cd89e39e3147e627cb4142df659ba68ab593cd6 |
| harness | parts | .agents/skills/harness/SKILL.md | 66c433d9d250d2ea0e71af8bccfd9a591ae4972c29d77f550c17ae4b760b9241 |
| harness | parts | AGENTS.md | 51ccc9713d66410044ebc7d82063a2bc08524ff99a62325d758f68ec0419d93d |
| harness | parts | CLAUDE.md | 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49 |
| harness | output | .agents/mechanisms/harness/harness.md | 593080c51567c7e3c58fe07644911f4c3f5b290bcf5576aa10cfcc1a7810d70f |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e8b1f916df9ebb9fce639471879486b2b229d9a07dead8ba7ba0096d2a70f039 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 32b1cf0e4a9df8c78e9289f3248d2154b601dd171dc1f1d77050a48ad09ad9dd |
| harness | output | .agents/skills/harness/SKILL.md | 66c433d9d250d2ea0e71af8bccfd9a591ae4972c29d77f550c17ae4b760b9241 |
| harness | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2f0bfa275a6e1fec6e76b0e2223f32908a79771ebeae86abe5ba4f7d7ff45b5a |
| harness | output | .agents/skills/mechanism/SKILL.md | 4737136791c168cbff85bba5e2a1f5ac6518bb06b3f511416784e0d422cf1703 |
| maintain | parts | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | parts | .agents/scripts/gw/maintain.py | 027bcb41d2f79363efbaba31451e55e4876222e4f884515ab847d5e2997b91a0 |
| maintain | parts | .agents/scripts/gw/straw_dogs.py | 9862553ba62a7c059a0a52b13de7b8bec4b095ec5f7f09c03d2994732ddad516 |
| maintain | parts | .agents/scripts/gw/test/test_maintain.py | a4c184175b7299de8cd4ac613a740b8d6e80372c82206bfc1ac1305b7912159c |
| maintain | parts | .agents/scripts/gw/test/test_straw_dogs.py | ce9183b5bc4e17b50aea0d3e731fc7522d7e5f9c2513a7a370d91b74556233ef |
| maintain | parts | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | parts | .agents/skills/maintain/SKILL.md | 08ab10db8aa24a2fa6257668b7413a7ed51f0f9665070cf25d37d9cb985abf6f |
| maintain | output | .agents/mechanisms/maintain/maintain.md | 11f86e7ecdf92c3212278294f8a9d2673b7ff79ad9696d3c61ae7cad5bdd4305 |
| maintain | output | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e8b1f916df9ebb9fce639471879486b2b229d9a07dead8ba7ba0096d2a70f039 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 32b1cf0e4a9df8c78e9289f3248d2154b601dd171dc1f1d77050a48ad09ad9dd |
| maintain | output | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | output | .agents/skills/maintain/SKILL.md | 08ab10db8aa24a2fa6257668b7413a7ed51f0f9665070cf25d37d9cb985abf6f |
| maintain | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2f0bfa275a6e1fec6e76b0e2223f32908a79771ebeae86abe5ba4f7d7ff45b5a |
| maintain | output | .agents/skills/mechanism/SKILL.md | 4737136791c168cbff85bba5e2a1f5ac6518bb06b3f511416784e0d422cf1703 |
| mechanism-shape | parts | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 32b1cf0e4a9df8c78e9289f3248d2154b601dd171dc1f1d77050a48ad09ad9dd |
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | 192dbbdec86cafdff18cda7261bb4092cbf791993b55a6bfa5792ba4ccae1a7f |
| mechanism-shape | parts | .agents/scripts/gw/inject_rules.py | d3644f3cb2e1bc13fb1e79f3fa4894fe3cea39e40f2c4b4072f45103f7a21fb2 |
| mechanism-shape | parts | .agents/scripts/gw/mechanisms.py | e45bd11f6d58123c69ae2dc7cea76b28cd5169f9569df52968cdf74f411716ea |
| mechanism-shape | parts | .agents/scripts/gw/test/repository.py | fed406d3dd9fd91f3c4fe3a91f7315082c1d18deac1ea8f82e87ba2240d939d4 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_inject_rules.py | 1e2985e26530eb1ce090a2690fd29973f02862c466d020ea0abb13aca9075710 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_mechanisms.py | e37c00c2fddc1dad1008631fc82cd2caeada3181b8b48fb5f80ae59c43e83f30 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_repository.py | 1dc82f2bcf6dd760e13c92fb7b46cd566e6413c5561c3845b54204e45775f03a |
| mechanism-shape | parts | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2f0bfa275a6e1fec6e76b0e2223f32908a79771ebeae86abe5ba4f7d7ff45b5a |
| mechanism-shape | parts | .agents/skills/mechanism/SKILL.md | 4737136791c168cbff85bba5e2a1f5ac6518bb06b3f511416784e0d422cf1703 |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e8b1f916df9ebb9fce639471879486b2b229d9a07dead8ba7ba0096d2a70f039 |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 32b1cf0e4a9df8c78e9289f3248d2154b601dd171dc1f1d77050a48ad09ad9dd |
| mechanism-shape | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2f0bfa275a6e1fec6e76b0e2223f32908a79771ebeae86abe5ba4f7d7ff45b5a |
| mechanism-shape | output | .agents/skills/mechanism/SKILL.md | 4737136791c168cbff85bba5e2a1f5ac6518bb06b3f511416784e0d422cf1703 |
| questions | parts | .agents/.gitattributes | bd95d1f719ab960c7d638d202a762ab72f356be5be7270623165327a47e28149 |
| questions | parts | .agents/mechanisms/questions/questions.rules.md | 8f6cfc73482171925b2c27e0063d07b5335547755fcbf499f2bba4ab9b977507 |
| questions | parts | .agents/scripts/gw/hook.sh | a5c73e871f8cad9d3c818fde15879e78c502e2e16a2cdc21296cbac4efb81be8 |
| questions | parts | .agents/scripts/gw/questions.py | c4210b8be42ca4af3a10a332a950da1f6de30345fc0e797ad2243c48b88952b3 |
| questions | parts | .agents/scripts/gw/test/test_questions.py | 68db674eb8570b92dc96ac905eb6ceeb8dac3a72e97243a733e28ddf81b1ae4d |
| questions | parts | .agents/skills/questions/SKILL.md | 174fd15e1475385be4e1db694cb714d73502ca6f3940884c2563741a91a8fa70 |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | b746ca845d89c543ba661000c5811fdac8d0f288fc94ce0c9ef079439aebac23 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e8b1f916df9ebb9fce639471879486b2b229d9a07dead8ba7ba0096d2a70f039 |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 32b1cf0e4a9df8c78e9289f3248d2154b601dd171dc1f1d77050a48ad09ad9dd |
| questions | output | .agents/mechanisms/questions/questions.md | 71f16d3c6b109fb50df013418072e5d7a03412fc0f0055c31f9cc6e3952bc239 |
| questions | output | .agents/mechanisms/questions/questions.rules.md | 8f6cfc73482171925b2c27e0063d07b5335547755fcbf499f2bba4ab9b977507 |
| questions | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2f0bfa275a6e1fec6e76b0e2223f32908a79771ebeae86abe5ba4f7d7ff45b5a |
| questions | output | .agents/skills/mechanism/SKILL.md | 4737136791c168cbff85bba5e2a1f5ac6518bb06b3f511416784e0d422cf1703 |
| questions | output | .agents/skills/questions/SKILL.md | 174fd15e1475385be4e1db694cb714d73502ca6f3940884c2563741a91a8fa70 |
| questions | output | .agents/skills/questions/STORE-ARRIVAL.md | b746ca845d89c543ba661000c5811fdac8d0f288fc94ce0c9ef079439aebac23 |
| questions | output | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | output | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | output | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| ticket | parts | .agents/mechanisms/ticket/ticket.rules.md | a29e1c1b3c2bd8667aee2984e48ac369bb361c0c66a9fdb772b7b58be3c7c033 |
| ticket | parts | .agents/scripts/gw/move_doc.py | 69d4e36c60050b733af3796c3f3ce9445944d4dd3376755b78dc3a8f97a4375c |
| ticket | parts | .agents/scripts/gw/test/test_citations.py | a063c30c4ea5f532b1786d80e3822a7d952e3cd66292bdb0b9008b1ac5685385 |
| ticket | parts | .agents/scripts/gw/test/test_command_line.py | 96f1ca7aa5af3ad1803310bd3f44b75fe854608e0cbc4d2292dd50e8eb621ec5 |
| ticket | parts | .agents/scripts/gw/test/test_failure_contract.py | c596f8a61287b01fd20b5eb2189e13235454166c044742c2d68d77b8fe531a5e |
| ticket | parts | .agents/scripts/gw/test/test_paired_close.py | 161cb3fa091acb698862114aa47fd443175f66e053f05195a014308deeadb864 |
| ticket | parts | .agents/scripts/gw/test/test_refusals.py | 340c4a652f4eb68be974fd520914dff0a3dea08013d8da3268937b50680a9cd5 |
| ticket | parts | .agents/scripts/gw/test/test_tickets.py | e6b668e555543de3e2ae7a28f5831d5f3e03bf1b5778b306453f99c65846e1ca |
| ticket | parts | .agents/scripts/gw/tickets.py | 002cb8c5382d06e3b5fab2cc100d7521295324ce261ad04351dc83f230404250 |
| ticket | parts | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | parts | .agents/skills/ticket/SKILL.md | 367bee3d13015b6d7352e27260ce8ed9901206436b6765712841c7dc50f16b13 |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | d08faa438201df9f4a0461873c6522e35e9a688f2ca1ff208168bbf4d0d1197a |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e8b1f916df9ebb9fce639471879486b2b229d9a07dead8ba7ba0096d2a70f039 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 32b1cf0e4a9df8c78e9289f3248d2154b601dd171dc1f1d77050a48ad09ad9dd |
| ticket | output | .agents/mechanisms/ticket/ticket.md | c897b5ea3bfc7e8978b4dfe884c684303216b974c6aabda4d14d772c0b4640b7 |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | a29e1c1b3c2bd8667aee2984e48ac369bb361c0c66a9fdb772b7b58be3c7c033 |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2f0bfa275a6e1fec6e76b0e2223f32908a79771ebeae86abe5ba4f7d7ff45b5a |
| ticket | output | .agents/skills/mechanism/SKILL.md | 4737136791c168cbff85bba5e2a1f5ac6518bb06b3f511416784e0d422cf1703 |
| ticket | output | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | output | .agents/skills/ticket/SKILL.md | 367bee3d13015b6d7352e27260ce8ed9901206436b6765712841c7dc50f16b13 |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | d08faa438201df9f4a0461873c6522e35e9a688f2ca1ff208168bbf4d0d1197a |
