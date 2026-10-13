# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| edge | parts | 0466f57a1dfa6be6875322193d8645d99f410c2ec42aa49b1c7874de7ef2db61 | 2026-10-12 | nothing to change |
| edge | output | 65802edf1a2ae1cdfb18b5e17b4eb45d70fab6fed348212627f737642bc040f5 | 2026-10-13 | nothing to change |
| harness | parts | af1c29a1680dbd2a8c98adace9483578ac37b35edae47d2fdd20774c853e4467 | 2026-10-13 | nothing to change |
| harness | output | 089da8a5c2be04815bf2273265f2e98737244d96057fa9385724f4c7e874aa7c | 2026-10-13 | nothing to change |
| maintain | parts | f8b153cb8761317ffca8d03f6aa87c66a2818228ec0842965c479293aa0d1f6c | 2026-10-13 | nothing to change |
| maintain | output | f7dac46456512388ed514aa3c8f1644835ddeaafb1ea7c53aea3cc2a6e3ed89d | 2026-10-13 | nothing to change |
| mechanism-shape | parts | e6f9e7aa5f6e0856e201ed1eff44dc8f54ffecfb2d20ab28eab2b3e4da23e6c4 | 2026-10-13 | nothing to change |
| mechanism-shape | output | 39beb8b7fa3e0eb7f7979b84791c6e66d01e5d483aac0bed8ac5bd7607ca836e | 2026-10-13 | nothing to change |
| product | parts | cbc6d67f5498360331ca4baef7e288d2bf96624aa549d7b11f2582fa2edb149b | 2026-10-13 | amended |
| questions | parts | 195d6532b6a0c7529bf64f6b3f9179d7b5072d1e1cd3967a3be33ad2e1606d86 | 2026-10-13 | nothing to change |
| questions | output | 411f74c93709b50d6d9481e618aa71cf607183c7543e68182b9abc34c83d7e72 | 2026-10-13 | nothing to change |
| ticket | parts | cb2d42ea115cc76d7e2daf7cd8ad90e4984912afb034fed2a63baec6d6141ff6 | 2026-10-13 | nothing to change |
| ticket | output | 69796cf18399b92c1fc31dae12bdebfe938f4df479fde1833fe6d124cb0d4ffe | 2026-10-13 | nothing to change |

| mechanism | level | file | fingerprint |
|---|---|---|---|
| edge | parts | .agents/mechanisms/edge/edge.rules.md | bdcb4f08fad66430c01d1c97ff1fd23d7effbe90fd971156542ec3e815381bee |
| edge | parts | .agents/scripts/gw/edges.py | 68840b8119aede816e6324e215babf0691dbb38e4d58da90fe2487c1f5dfe06e |
| edge | parts | .agents/scripts/gw/test/test_edges.py | 1980d8e8ade71435c1d32b1c7fff4603d175897703dfa63d1e245dc19e2a3a7b |
| edge | parts | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | parts | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/mechanisms/edge/edge.md | ab4782a9b90306213ec009e555dca72c7b6571ec37a63d7dd4bd7d00af59a223 |
| edge | output | .agents/mechanisms/edge/edge.rules.md | bdcb4f08fad66430c01d1c97ff1fd23d7effbe90fd971156542ec3e815381bee |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 03179ed5a91a76be74c29fa9918e84bb73a1b13109d68dd8589a5f67f7cd0284 |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| edge | output | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | output | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| edge | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| harness | parts | .agents/scripts/gw/harness.py | 82c9b1edce04c1b88daaf8859777a1bd30f459d9b6404e5f30d06a435f4083d8 |
| harness | parts | .agents/scripts/gw/test/test_harness.py | 3bdd651722d36ff597989de0fe6cb18ba7fac6cdf3ee626ea478920d4d303a92 |
| harness | parts | .agents/skills/harness/SKILL.md | 4c7f72c9197aac8960c3b197ad270568e7363867cdceed154a1d77d7396b1af0 |
| harness | parts | AGENTS.md | 4d15841e15c655b7b49d65a12610d8e1839db171ae1eb4cddedd72ae4190f806 |
| harness | parts | CLAUDE.md | 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49 |
| harness | output | .agents/mechanisms/harness/harness.md | a87fc4eeea61f92c492d4d7bdb7821f77ed385d5ca68e34f19c4b608f3c40d2a |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 03179ed5a91a76be74c29fa9918e84bb73a1b13109d68dd8589a5f67f7cd0284 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| harness | output | .agents/skills/harness/SKILL.md | 4c7f72c9197aac8960c3b197ad270568e7363867cdceed154a1d77d7396b1af0 |
| harness | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| harness | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| maintain | parts | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | parts | .agents/scripts/gw/maintain.py | 89e39e230c0aaf9bdc0f396e75c06986b455445829c779f527e8340fd1f5fbee |
| maintain | parts | .agents/scripts/gw/straw_dogs.py | 2dc6fcdf67158b8cca7cc3112156ff6ee3884316557ed4a1dab32f38a564cd12 |
| maintain | parts | .agents/scripts/gw/test/test_maintain.py | 752004ea1b7de3efcf4748c9a04cf18c31d09e1d841cbc2a1d5f8dd3e46ef03e |
| maintain | parts | .agents/scripts/gw/test/test_straw_dogs.py | fe474f7de0a07f7ce37ad56c0de40365f1cf2b70932bd4b5f7bd053e6065cf25 |
| maintain | parts | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | parts | .agents/skills/maintain/SKILL.md | 453e41979180a249f75d2fb24e767a1cc92d6d86a95de9048a6b22465b519b3f |
| maintain | output | .agents/mechanisms/maintain/maintain.md | 6cf038d971b809e0673c107b55c61ba09a57d734041cf8ba6786b729b99127b5 |
| maintain | output | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 03179ed5a91a76be74c29fa9918e84bb73a1b13109d68dd8589a5f67f7cd0284 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| maintain | output | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | output | .agents/skills/maintain/SKILL.md | 453e41979180a249f75d2fb24e767a1cc92d6d86a95de9048a6b22465b519b3f |
| maintain | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| maintain | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| mechanism-shape | parts | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | b020b9940a009c6d42426a7697f2333d1f4b9e84b6240affcae324c8740ee80e |
| mechanism-shape | parts | .agents/scripts/gw/inject_rules.py | 0669a7d497cd32f92c79f7a9ed5452c85b6bed1195054fe8d877415ee47bf849 |
| mechanism-shape | parts | .agents/scripts/gw/mechanisms.py | 36326d2262ca570ececc44cdf45844c3e861eaefa138fda8e04039e32c8b5d1b |
| mechanism-shape | parts | .agents/scripts/gw/test/repository.py | 421f300b5d4eceb06652e69ad37c3765a9a2c5bb9f107a8c2385d5344fd12fab |
| mechanism-shape | parts | .agents/scripts/gw/test/test_inject_rules.py | 75ad10456b00e6860686a034f3b4148141255fdd8c89e7e4794d8a1a55a3d496 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_mechanisms.py | 1bf38c754c4d8aa524a6c45e1063be0c87717135e43d5ce699f34be2c36fc559 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_repository.py | 61c008b612db93199ef86349eb3a9931479c3c33de1724365f90b293593d0e69 |
| mechanism-shape | parts | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| mechanism-shape | parts | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 03179ed5a91a76be74c29fa9918e84bb73a1b13109d68dd8589a5f67f7cd0284 |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| mechanism-shape | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| product | parts | .agents/mechanisms/product/product.rules.md | 47306c186df125ccb87bb4d852a6c3c79796b264fc014e33a827522ac8fa918b |
| product | parts | .agents/scripts/gw/product.py | 8c8cd0533b14b1223a5492e3c6debc49e6bb441eb9b68408df28d993600932bf |
| product | parts | .agents/scripts/gw/test/test_product.py | e4e25947c4703a29a3975c320fd1c0eb446b38921cc3b4cfeddd2a2d712ff279 |
| product | parts | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | parts | .agents/skills/product/SKILL.md | 8b742d6b82ef1e5defaecc03328d26b968ed1a94162f8be506a2f2427321e2af |
| questions | parts | .agents/.gitattributes | bd95d1f719ab960c7d638d202a762ab72f356be5be7270623165327a47e28149 |
| questions | parts | .agents/mechanisms/questions/questions.rules.md | 35da1535183088be03f1124e3e29a8cb1ac353121d2530914949ba84f6c58eb3 |
| questions | parts | .agents/scripts/gw/hook.sh | 0118d8145545019d8121a339242fc9795690bb554d2375a8f89a3b4de27ba83e |
| questions | parts | .agents/scripts/gw/questions.py | 60e0cc0acba1d0600184166b996469fa84500c49b846a586caecf8c839376034 |
| questions | parts | .agents/scripts/gw/test/test_questions.py | 2252748dc2af18a2d475395f5f025a68ef0c19c4d0e8a9bfdb12746bebdaa6fd |
| questions | parts | .agents/skills/questions/SKILL.md | 1eb9232824ae51da5e6e8c1e83c16a2df2b11bce98c3ef64fe24f290047e308b |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 03179ed5a91a76be74c29fa9918e84bb73a1b13109d68dd8589a5f67f7cd0284 |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| questions | output | .agents/mechanisms/questions/questions.md | f7f5be1267588ebe83ddaeeb0fca1233df9c100d58d9df3ef1c5338f9ded5269 |
| questions | output | .agents/mechanisms/questions/questions.rules.md | 35da1535183088be03f1124e3e29a8cb1ac353121d2530914949ba84f6c58eb3 |
| questions | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| questions | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| questions | output | .agents/skills/questions/SKILL.md | 1eb9232824ae51da5e6e8c1e83c16a2df2b11bce98c3ef64fe24f290047e308b |
| questions | output | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | output | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | output | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | output | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| ticket | parts | .agents/mechanisms/ticket/ticket.rules.md | bae100215a0b14d53db5cec14ea0ed02c179048e284d62dc4d05f03e0727ced2 |
| ticket | parts | .agents/scripts/gw/move_doc.py | 538501d9bbaedb0b6424d7cf8c78c419a8578b344df2835279f42c78e9409a88 |
| ticket | parts | .agents/scripts/gw/test/test_citations.py | dbde70f3d00e122d5dcceda2fd5ad8c9cbe89ed98952cc44fe4f7778c67a8d4a |
| ticket | parts | .agents/scripts/gw/test/test_command_line.py | 7f038df6e53672efb853180ad059cf16126e9553323cb0487f29a79d3b03a875 |
| ticket | parts | .agents/scripts/gw/test/test_failure_contract.py | fb98267bdfca71023f00f5a36ac2734afaeaced6ee20d671836583b22e7482c9 |
| ticket | parts | .agents/scripts/gw/test/test_paired_close.py | 8a6f57f07c743bbfe594ab6002659943a07896e74328c61387e10006f6304315 |
| ticket | parts | .agents/scripts/gw/test/test_refusals.py | e57dc3df0c656820945a2be6824cc57fdcdba856738fc92c324223af6b6f45a2 |
| ticket | parts | .agents/scripts/gw/test/test_tickets.py | a05a628d5f23a76703fa1e19bbe4907354fadc43a15c02441ecdcc4f6d401a12 |
| ticket | parts | .agents/scripts/gw/tickets.py | 92c2136b7ceaef8f99ee195a9e934616c8fa187b5896322a6cc4af950ea18911 |
| ticket | parts | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | parts | .agents/skills/ticket/SKILL.md | 35b0a693da15377df5ffdb54be01f69c744cda3f0aef83fc1b736aea8b92d8e0 |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | e809aba42bae8a086587ed76a0dc6f80b8ddbdb5bc09e82a6f8b6008b107e3dc |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 03179ed5a91a76be74c29fa9918e84bb73a1b13109d68dd8589a5f67f7cd0284 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| ticket | output | .agents/mechanisms/ticket/ticket.md | 01495bcc7201db20ea13acd4a81193e765672ca70a3cd4a924596347ed65dbe9 |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | bae100215a0b14d53db5cec14ea0ed02c179048e284d62dc4d05f03e0727ced2 |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| ticket | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| ticket | output | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | output | .agents/skills/ticket/SKILL.md | 35b0a693da15377df5ffdb54be01f69c744cda3f0aef83fc1b736aea8b92d8e0 |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | e809aba42bae8a086587ed76a0dc6f80b8ddbdb5bc09e82a6f8b6008b107e3dc |
