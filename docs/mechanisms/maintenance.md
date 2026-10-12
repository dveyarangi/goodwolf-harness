# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| edge | parts | 0466f57a1dfa6be6875322193d8645d99f410c2ec42aa49b1c7874de7ef2db61 | 2026-10-12 | nothing to change |
| edge | output | 299ce490fc68b5b4ee8e7ed2ddd8d46b67f2273a246d3e58b6da7bd913efcb3e | 2026-10-12 | nothing to change |
| harness | parts | bd907c895dc0d43f231ef125a723c2ce22a9909d7514c5aa509ce75c3b9cd2fa | 2026-10-12 | nothing to change |
| harness | output | 3a79214247112ecd0543da8b68e3b3e1024c94de4e99861d854b2680466a9637 | 2026-10-12 | nothing to change |
| maintain | parts | 01bad9b10b35e443a99c34c61df8b5c118c3bd8ab99be495dea0edd4b4e274d0 | 2026-10-12 | nothing to change |
| maintain | output | e1b7d84387967aa93f7e14efc1b411fde3e1ed1efb0db1b55a801d19051ef2c2 | 2026-10-12 | nothing to change |
| mechanism-shape | parts | 5fb37a169deda5401804869c7f710c569cb3cd6875d8ad9b7bc4b3baf64acc0e | 2026-10-12 | nothing to change |
| mechanism-shape | output | bfc233083cf7f765e196116a5619689d3925f86b76b8f5630eff9bc7598fd0d0 | 2026-10-12 | nothing to change |
| questions | parts | 95de2ae8ee9225945eb6e4f6f6c50d23a68227e77966c50cde37cfd47f8eddfb | 2026-10-12 | nothing to change |
| questions | output | 59f400a5e5f2458e881713c02c1e1c87c416fce9d5d6515b50ba81acf7a99523 | 2026-10-12 | nothing to change |
| ticket | parts | 87330ed2d923bc2c523f7a806bb916110119eac51b3ba8834a4c77304939a1ef | 2026-10-12 | amended |
| ticket | output | 5de3e7d696faa0caf471386c2e009d14acc6f66c6dd2103cedf76b9e499cbefa | 2026-10-12 | nothing to change |

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
| harness | parts | .agents/scripts/gw/harness.py | 73d29bae8dc6611df4d97b9e1c70243758340afc9dae4c8b014a5523a1c8f6dd |
| harness | parts | .agents/scripts/gw/test/test_harness.py | f13176253874c26d64d7a07e40c0714128a03c747b6b5f86b2e640b8c8acb787 |
| harness | parts | .agents/skills/harness/SKILL.md | d0dbdd37247bf5f57cca55f736e327dc5fb62fe2b5077c669cd78bbf6d2288fa |
| harness | parts | AGENTS.md | c84c2405535bc2979b4b7317ee7ec7eda31461ec225bfc578dc0906b1d7c8ef3 |
| harness | parts | CLAUDE.md | 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49 |
| harness | output | .agents/mechanisms/harness/harness.md | ff660b5058371714013dced96f94a63024f27cd7aa948e7c1a85b45621d2301a |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | da8e08b11172b96ebc1bd1dd104a0444ecf16858cf083ccf74d24379b3a080c3 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| harness | output | .agents/skills/harness/SKILL.md | d0dbdd37247bf5f57cca55f736e327dc5fb62fe2b5077c669cd78bbf6d2288fa |
| harness | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 9a745ac29f45671ea32ea078802e26088e8197bc144f4156653d1ae4dfec163b |
| harness | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
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
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | b020b9940a009c6d42426a7697f2333d1f4b9e84b6240affcae324c8740ee80e |
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
| questions | parts | .agents/scripts/gw/questions.py | bb1099b749b78fee92befec7378efb055b20bf1f6fa752a8a87beb86c428f244 |
| questions | parts | .agents/scripts/gw/test/test_questions.py | b5de8463279f3c2f38574ae1d7ac432bacb2e13a563e445e8609fdc458e0cb4d |
| questions | parts | .agents/skills/questions/SKILL.md | c2b6139274a16ef0d4dd3ce70e04370b82f77f0f6f7251d3d9704cf2ae0bc835 |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | b746ca845d89c543ba661000c5811fdac8d0f288fc94ce0c9ef079439aebac23 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | da8e08b11172b96ebc1bd1dd104a0444ecf16858cf083ccf74d24379b3a080c3 |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| questions | output | .agents/mechanisms/questions/questions.md | 1cd99cd06d1ba3b9deb57b898a42105ea15ca9672cf03e26ab1467aa2fb80bfa |
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
| ticket | parts | .agents/scripts/gw/tickets.py | ef0ce5c41fd18c2abb5749c5e919f5010e9e56487526284af87b7e4e98cdfa8f |
| ticket | parts | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | parts | .agents/skills/ticket/SKILL.md | fa5788471a1f4866cb40bb34f78c73187ca66c0c2deea991163b3b28e21fe53f |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | d08faa438201df9f4a0461873c6522e35e9a688f2ca1ff208168bbf4d0d1197a |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | da8e08b11172b96ebc1bd1dd104a0444ecf16858cf083ccf74d24379b3a080c3 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| ticket | output | .agents/mechanisms/ticket/ticket.md | 69abb270baf71f9541dd550ea1ec06949b11dfadbbfb9cc5cb1a59f376750013 |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | a29e1c1b3c2bd8667aee2984e48ac369bb361c0c66a9fdb772b7b58be3c7c033 |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 9a745ac29f45671ea32ea078802e26088e8197bc144f4156653d1ae4dfec163b |
| ticket | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| ticket | output | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | output | .agents/skills/ticket/SKILL.md | fa5788471a1f4866cb40bb34f78c73187ca66c0c2deea991163b3b28e21fe53f |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | d08faa438201df9f4a0461873c6522e35e9a688f2ca1ff208168bbf4d0d1197a |
