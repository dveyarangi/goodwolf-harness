# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| edge | parts | 0466f57a1dfa6be6875322193d8645d99f410c2ec42aa49b1c7874de7ef2db61 | 2026-10-12 | nothing to change |
| edge | output | 299ce490fc68b5b4ee8e7ed2ddd8d46b67f2273a246d3e58b6da7bd913efcb3e | 2026-10-12 | nothing to change |
| harness | parts | 930401b8a1032aaecdfb275df0d76bb900eaea85e817d280c19ea3160646ed7a | 2026-10-11 | nothing to change |
| harness | output | 4e91cab4ef12377dadf347374c0a48952ffa3f083b7783f031c010d0a0b9550a | 2026-10-11 | nothing to change |
| maintain | parts | 01bad9b10b35e443a99c34c61df8b5c118c3bd8ab99be495dea0edd4b4e274d0 | 2026-10-12 | nothing to change |
| maintain | output | e1b7d84387967aa93f7e14efc1b411fde3e1ed1efb0db1b55a801d19051ef2c2 | 2026-10-12 | nothing to change |
| mechanism-shape | parts | 95e27f730e4997a42aac32192403dc95d77182df1e75316824eccf40712e4ffd | 2026-10-12 | amended |
| mechanism-shape | output | bfc233083cf7f765e196116a5619689d3925f86b76b8f5630eff9bc7598fd0d0 | 2026-10-12 | nothing to change |
| questions | parts | c07ed250140c77c54ae961dd21fcbd76c937413a09cdbecbce3700826012b994 | 2026-10-12 | nothing to change |
| questions | output | 75d792e76e3ab22f14d780dbd16b373b95365bba59f5748df1afca7afc85a6a8 | 2026-10-12 | nothing to change |
| ticket | parts | 3c4f504cce64c1beacfafa60d929f2180b13ec92ae6afb4e2d1c2583cb9e5db1 | 2026-10-12 | nothing to change |
| ticket | output | b478cd0c81e694aaa63efef8ffc9206d967e91c1ba8b78aa926fd0ad100353a0 | 2026-10-12 | nothing to change |

| mechanism | level | file | fingerprint |
|---|---|---|---|
| edge | parts | .agents/mechanisms/edge/edge.rules.md | bdcb4f08fad66430c01d1c97ff1fd23d7effbe90fd971156542ec3e815381bee |
| edge | parts | .agents/scripts/gw/edges.py | 68840b8119aede816e6324e215babf0691dbb38e4d58da90fe2487c1f5dfe06e |
| edge | parts | .agents/scripts/gw/test/test_edges.py | 1980d8e8ade71435c1d32b1c7fff4603d175897703dfa63d1e245dc19e2a3a7b |
| edge | parts | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | parts | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/mechanisms/edge/edge.md | 905530e3cd2922dc669ddbce412a623f84fc61cead71732c571b4339e32d394f |
| edge | output | .agents/mechanisms/edge/edge.rules.md | bdcb4f08fad66430c01d1c97ff1fd23d7effbe90fd971156542ec3e815381bee |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | da8e08b11172b96ebc1bd1dd104a0444ecf16858cf083ccf74d24379b3a080c3 |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| edge | output | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | output | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 9a745ac29f45671ea32ea078802e26088e8197bc144f4156653d1ae4dfec163b |
| edge | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
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
| maintain | parts | .agents/scripts/gw/maintain.py | 94179785a2656d62cbcbef7292fecb8d6598edd7b94aafe1008d230c1321bb25 |
| maintain | parts | .agents/scripts/gw/straw_dogs.py | 2dc6fcdf67158b8cca7cc3112156ff6ee3884316557ed4a1dab32f38a564cd12 |
| maintain | parts | .agents/scripts/gw/test/test_maintain.py | 752004ea1b7de3efcf4748c9a04cf18c31d09e1d841cbc2a1d5f8dd3e46ef03e |
| maintain | parts | .agents/scripts/gw/test/test_straw_dogs.py | fe474f7de0a07f7ce37ad56c0de40365f1cf2b70932bd4b5f7bd053e6065cf25 |
| maintain | parts | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | parts | .agents/skills/maintain/SKILL.md | 353efe112ec5a72a8e699e87e8f038f8f9f66aa8b5c86485f06725c6147b8767 |
| maintain | output | .agents/mechanisms/maintain/maintain.md | 11f86e7ecdf92c3212278294f8a9d2673b7ff79ad9696d3c61ae7cad5bdd4305 |
| maintain | output | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | da8e08b11172b96ebc1bd1dd104a0444ecf16858cf083ccf74d24379b3a080c3 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| maintain | output | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | output | .agents/skills/maintain/SKILL.md | 353efe112ec5a72a8e699e87e8f038f8f9f66aa8b5c86485f06725c6147b8767 |
| maintain | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 9a745ac29f45671ea32ea078802e26088e8197bc144f4156653d1ae4dfec163b |
| maintain | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| mechanism-shape | parts | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | 7f6bd0d708dbb6f825def33dc3b7406b0ce09ec3363402a12a542c8cb398b61c |
| mechanism-shape | parts | .agents/scripts/gw/inject_rules.py | 0669a7d497cd32f92c79f7a9ed5452c85b6bed1195054fe8d877415ee47bf849 |
| mechanism-shape | parts | .agents/scripts/gw/mechanisms.py | f5b5e58bd0a0bd0ba9025e95657be4c2f212c4f967d5ab30141a0a445214bc2e |
| mechanism-shape | parts | .agents/scripts/gw/test/repository.py | 421f300b5d4eceb06652e69ad37c3765a9a2c5bb9f107a8c2385d5344fd12fab |
| mechanism-shape | parts | .agents/scripts/gw/test/test_inject_rules.py | 75ad10456b00e6860686a034f3b4148141255fdd8c89e7e4794d8a1a55a3d496 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_mechanisms.py | 1bf38c754c4d8aa524a6c45e1063be0c87717135e43d5ce699f34be2c36fc559 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_repository.py | 61c008b612db93199ef86349eb3a9931479c3c33de1724365f90b293593d0e69 |
| mechanism-shape | parts | .agents/skills/mechanism/MECHANISM-FORMAT.md | 9a745ac29f45671ea32ea078802e26088e8197bc144f4156653d1ae4dfec163b |
| mechanism-shape | parts | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | da8e08b11172b96ebc1bd1dd104a0444ecf16858cf083ccf74d24379b3a080c3 |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 9a745ac29f45671ea32ea078802e26088e8197bc144f4156653d1ae4dfec163b |
| mechanism-shape | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| questions | parts | .agents/.gitattributes | bd95d1f719ab960c7d638d202a762ab72f356be5be7270623165327a47e28149 |
| questions | parts | .agents/mechanisms/questions/questions.rules.md | 8f6cfc73482171925b2c27e0063d07b5335547755fcbf499f2bba4ab9b977507 |
| questions | parts | .agents/scripts/gw/hook.sh | 0118d8145545019d8121a339242fc9795690bb554d2375a8f89a3b4de27ba83e |
| questions | parts | .agents/scripts/gw/questions.py | 45e0c553a8b6154b2c531aef8279453a8091cfb6484965af00a5c4a02feed09e |
| questions | parts | .agents/scripts/gw/test/test_questions.py | ac3b4d2e86e09a8ab5fb6cedc192f7f723b0345cff04b1e4286e326171de3f14 |
| questions | parts | .agents/skills/questions/SKILL.md | c2b6139274a16ef0d4dd3ce70e04370b82f77f0f6f7251d3d9704cf2ae0bc835 |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | b746ca845d89c543ba661000c5811fdac8d0f288fc94ce0c9ef079439aebac23 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | da8e08b11172b96ebc1bd1dd104a0444ecf16858cf083ccf74d24379b3a080c3 |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| questions | output | .agents/mechanisms/questions/questions.md | 71f16d3c6b109fb50df013418072e5d7a03412fc0f0055c31f9cc6e3952bc239 |
| questions | output | .agents/mechanisms/questions/questions.rules.md | 8f6cfc73482171925b2c27e0063d07b5335547755fcbf499f2bba4ab9b977507 |
| questions | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 9a745ac29f45671ea32ea078802e26088e8197bc144f4156653d1ae4dfec163b |
| questions | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| questions | output | .agents/skills/questions/SKILL.md | c2b6139274a16ef0d4dd3ce70e04370b82f77f0f6f7251d3d9704cf2ae0bc835 |
| questions | output | .agents/skills/questions/STORE-ARRIVAL.md | b746ca845d89c543ba661000c5811fdac8d0f288fc94ce0c9ef079439aebac23 |
| questions | output | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | output | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | output | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| ticket | parts | .agents/mechanisms/ticket/ticket.rules.md | a29e1c1b3c2bd8667aee2984e48ac369bb361c0c66a9fdb772b7b58be3c7c033 |
| ticket | parts | .agents/scripts/gw/move_doc.py | 413d8a502dd309b9a7fb286bc98a04659d390283ba7bc48958ed62b541d981d8 |
| ticket | parts | .agents/scripts/gw/test/test_citations.py | dbde70f3d00e122d5dcceda2fd5ad8c9cbe89ed98952cc44fe4f7778c67a8d4a |
| ticket | parts | .agents/scripts/gw/test/test_command_line.py | 7f038df6e53672efb853180ad059cf16126e9553323cb0487f29a79d3b03a875 |
| ticket | parts | .agents/scripts/gw/test/test_failure_contract.py | 144fb8e6e1e6e364690203dccf6102156d899938ec3de68a5e727163f96e6e37 |
| ticket | parts | .agents/scripts/gw/test/test_paired_close.py | 8a6f57f07c743bbfe594ab6002659943a07896e74328c61387e10006f6304315 |
| ticket | parts | .agents/scripts/gw/test/test_refusals.py | e57dc3df0c656820945a2be6824cc57fdcdba856738fc92c324223af6b6f45a2 |
| ticket | parts | .agents/scripts/gw/test/test_tickets.py | a05a628d5f23a76703fa1e19bbe4907354fadc43a15c02441ecdcc4f6d401a12 |
| ticket | parts | .agents/scripts/gw/tickets.py | ce9a68741c90da9911ccb99f2b98fae50fef694dd2e3d098eeed4726c5fc9322 |
| ticket | parts | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | parts | .agents/skills/ticket/SKILL.md | fa5788471a1f4866cb40bb34f78c73187ca66c0c2deea991163b3b28e21fe53f |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | d08faa438201df9f4a0461873c6522e35e9a688f2ca1ff208168bbf4d0d1197a |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | da8e08b11172b96ebc1bd1dd104a0444ecf16858cf083ccf74d24379b3a080c3 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| ticket | output | .agents/mechanisms/ticket/ticket.md | c897b5ea3bfc7e8978b4dfe884c684303216b974c6aabda4d14d772c0b4640b7 |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | a29e1c1b3c2bd8667aee2984e48ac369bb361c0c66a9fdb772b7b58be3c7c033 |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 9a745ac29f45671ea32ea078802e26088e8197bc144f4156653d1ae4dfec163b |
| ticket | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| ticket | output | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | output | .agents/skills/ticket/SKILL.md | fa5788471a1f4866cb40bb34f78c73187ca66c0c2deea991163b3b28e21fe53f |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | d08faa438201df9f4a0461873c6522e35e9a688f2ca1ff208168bbf4d0d1197a |
