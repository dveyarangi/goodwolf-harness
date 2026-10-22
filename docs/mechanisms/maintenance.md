# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| edge | parts | e6e14c7efa592ec2a651bfeb184d5efaae5e9c46c7fbc1dc5e3412efc00c8f7f | 2026-10-19 | nothing to change |
| edge | output | 8b72c83d17721aa70cafe8fc3aa172e7da1f54ac6cca7f4138d691e284701df9 | 2026-10-23 | nothing to change |
| harness | parts | 61c4a9fc2e9c527a67c81be45217a284c6ccdde861b91acbdb5eb58685130cc0 | 2026-10-23 | repaired |
| harness | output | af62d3a83fa4e3380caf4ec22ad4c8fc4d834473641e6f19a3498d253d6b8ce5 | 2026-10-23 | nothing to change |
| maintain | parts | 1fc19548d65ad1626a95d701fa07307e02ad4027d36fc7bad61e09fa16b22091 | 2026-10-22 | amended |
| maintain | output | 8b2ba9d439a6035027a0f55fa8d5d9fc620e0ca45a61dc5d21264fc583d68f38 | 2026-10-23 | nothing to change |
| mechanism-shape | parts | cede82807adb5c0e0fe8f399fd4b33b4ee509f41f3a842daed3c228e0c364887 | 2026-10-23 | nothing to change |
| mechanism-shape | output | 4f186dca76530f86116b1e53041d437bcdac0e7ebcd1bab8fb5dbeb7f1fa52a6 | 2026-10-23 | nothing to change |
| product | parts | 9207784985dd606ba5e8fe2339da592286612f021f6f5f2349fd2abb294d3225 | 2026-10-19 | nothing to change |
| product | output | 3653467cd5ddea57eba722dbaee70a6979f3b352d06392a390e8cd3f81fbb3c5 | 2026-10-23 | nothing to change |
| questions | parts | 528a41ecf2c4f27f866454f968f7fbc8e1e4111223b534bc027381d57daad935 | 2026-10-23 | nothing to change |
| questions | output | b1c92870049c26a69d171851b0bfbdcf021a0450d0bd8b507ca0c84bfe0a9740 | 2026-10-23 | nothing to change |
| session | parts | fe8d0219edf522b566c3c5beb8de2e4509c411567f639f7f3f5b10bd73563c83 | 2026-10-23 | amended |
| session | output | 6d6d4baa7fdf812688702b4ac895cce2ca169800bf24e4470d9618e00fe8b5f7 | 2026-10-23 | nothing to change |
| ticket | parts | b2d6602531c81c96cb399c32320a53abb5efd41a6b5a44b7fc33543b00d13717 | 2026-10-23 | nothing to change |
| ticket | output | c9b4e129552b9946002d8c52afb1ebb830746495293e23ea6df463ebeba71dd2 | 2026-10-23 | nothing to change |

| mechanism | level | file | fingerprint |
|---|---|---|---|
| edge | parts | .agents/mechanisms/edge/edge.rules.md | 59963f35ba6e27067f22082a704fab893f9ab6140333cb89f4d2c6480e135d19 |
| edge | parts | .agents/scripts/gw/edges.py | 68840b8119aede816e6324e215babf0691dbb38e4d58da90fe2487c1f5dfe06e |
| edge | parts | .agents/scripts/gw/test/test_edges.py | 1980d8e8ade71435c1d32b1c7fff4603d175897703dfa63d1e245dc19e2a3a7b |
| edge | parts | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | parts | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/mechanisms/edge/edge.md | ab4782a9b90306213ec009e555dca72c7b6571ec37a63d7dd4bd7d00af59a223 |
| edge | output | .agents/mechanisms/edge/edge.rules.md | 59963f35ba6e27067f22082a704fab893f9ab6140333cb89f4d2c6480e135d19 |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| edge | output | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | output | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| edge | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| harness | parts | .agents/scripts/gw/harness.py | 84f89d3ff842f7fab391938ec8300746e81f3192de371ca512847cea2a49935c |
| harness | parts | .agents/scripts/gw/test/test_harness.py | 14f035d925aee384f157ccd7e191b0c52b85d58d0e1536ab4b22bf3e13650fd7 |
| harness | parts | .agents/skills/harness/SKILL.md | 993348a51338084ac8e162bc38e37d2d85b1838333fd8a18633a473f9e0ecf2e |
| harness | parts | AGENTS.md | b5b012d9cbe122c5a88ee6054466ae0d878e5df87f98867db7fcd5c79a8ef587 |
| harness | parts | CLAUDE.md | 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49 |
| harness | output | .agents/mechanisms/harness/harness.md | b31940204e0e7ed9c3d49bf93b9c2b5f6181908a289a2de5b2b465374ea44270 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| harness | output | .agents/skills/harness/MEETING.md | 37f7953dd45b91d94fc5fd6bd77ca1735309c640781c3f30dea9a7211a65c8df |
| harness | output | .agents/skills/harness/SKILL.md | 993348a51338084ac8e162bc38e37d2d85b1838333fd8a18633a473f9e0ecf2e |
| harness | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| harness | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| maintain | parts | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | parts | .agents/scripts/gw/maintain.py | 08ecf2ff91fd8edfa6206f844a1c557a704155854d6d1e11e1651bf4cdc9c4c2 |
| maintain | parts | .agents/scripts/gw/straw_dogs.py | ce01cdbd5162766129d2b56c1815a3a054ded5167cbce6ba7f47437f22657925 |
| maintain | parts | .agents/scripts/gw/test/test_maintain.py | 752004ea1b7de3efcf4748c9a04cf18c31d09e1d841cbc2a1d5f8dd3e46ef03e |
| maintain | parts | .agents/scripts/gw/test/test_straw_dogs.py | d6f39f4245ffff85c0158dbb0202e0338b42238153adcbe33cecb2774b7ac697 |
| maintain | parts | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | parts | .agents/skills/maintain/SKILL.md | f757551a7abeab2fbdcccca753f8c2aee2900d0e2cfc4a859794cb639fec868f |
| maintain | output | .agents/mechanisms/maintain/maintain.md | 4947b99466b0bb47f698552360a23156078cbcd8d729085b9ec1948769122737 |
| maintain | output | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| maintain | output | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | output | .agents/skills/maintain/SKILL.md | f757551a7abeab2fbdcccca753f8c2aee2900d0e2cfc4a859794cb639fec868f |
| maintain | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| maintain | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| mechanism-shape | parts | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | 20a6bf08a7648453ea8a1d23ddcc141f8aa1cc2347bbb4bc46c28fb830070fcd |
| mechanism-shape | parts | .agents/scripts/gw/inject_rules.py | 6b9bcfd51543495869f0744a4e5dc4defe63092ed3631598fe7b798bdc9d3fd5 |
| mechanism-shape | parts | .agents/scripts/gw/mechanisms.py | 2e3e840ed34318d4796e0e1a2d027f7aff10df27ac86eaf7439c2f8c58c5e22d |
| mechanism-shape | parts | .agents/scripts/gw/test/repository.py | 421f300b5d4eceb06652e69ad37c3765a9a2c5bb9f107a8c2385d5344fd12fab |
| mechanism-shape | parts | .agents/scripts/gw/test/test_inject_rules.py | 066f82b461fb0a4413385072ac323a312c0e73437b159c046e530e2dd925860d |
| mechanism-shape | parts | .agents/scripts/gw/test/test_mechanisms.py | bdf423c1b4148a30361e538cf5ae1e5e9b800fd2bd31c9f16f41a6fbda4743f4 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_repository.py | 61c008b612db93199ef86349eb3a9931479c3c33de1724365f90b293593d0e69 |
| mechanism-shape | parts | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| mechanism-shape | parts | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| mechanism-shape | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| product | parts | .agents/mechanisms/product/product.rules.md | 05f71cc357a3c753f038e5920edf6bc6a59d3f39b8f9a61628a29cd03c0a0bac |
| product | parts | .agents/scripts/gw/product.py | 8a5bf81da67a44bf60f76b958af075f6dc8f319b973c42fe70c80ad225d19cea |
| product | parts | .agents/scripts/gw/test/test_product.py | 0eb917e0bb1c93f8644b910af8c2dd9d23b7ab5ada40b0fb292d1f440cf7c0c5 |
| product | parts | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | parts | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | parts | .agents/skills/product/SKILL.md | 69e74e5999ddaad12ab16555ac321b42cacd240e7793dd6b6c63b0879f67f481 |
| product | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| product | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| product | output | .agents/mechanisms/product/product.md | dbf73a93bd4c237061ba240b169aa88bb78807240929819db3173a4183607de9 |
| product | output | .agents/mechanisms/product/product.rules.md | 05f71cc357a3c753f038e5920edf6bc6a59d3f39b8f9a61628a29cd03c0a0bac |
| product | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| product | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| product | output | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | output | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | output | .agents/skills/product/SKILL.md | 69e74e5999ddaad12ab16555ac321b42cacd240e7793dd6b6c63b0879f67f481 |
| questions | parts | .agents/.gitattributes | bd95d1f719ab960c7d638d202a762ab72f356be5be7270623165327a47e28149 |
| questions | parts | .agents/mechanisms/questions/questions.rules.md | db8edb789517688203e8e9251a909d9ac384fe0bf9c3771d82411942b39cfa9b |
| questions | parts | .agents/scripts/gw/hook.sh | 0118d8145545019d8121a339242fc9795690bb554d2375a8f89a3b4de27ba83e |
| questions | parts | .agents/scripts/gw/questions.py | 62a6f88f3e287bb9e8bc8a536037417f15aa589dc60f5d36cf6270a56256c0df |
| questions | parts | .agents/scripts/gw/test/test_questions.py | 5f0fe8621805a9fe9488b7d2d0be63540a68588f2b9a8b3c08013e681fe336c9 |
| questions | parts | .agents/skills/questions/QUESTION-FORMAT.md | efbf0b2d2e629300953f7752c1dec9a40fd4c7a2de1beba465c26a9d000fa369 |
| questions | parts | .agents/skills/questions/SKILL.md | 5655eb89b1b451638441e6f80647743350d61f6edf0399e05c46f8f76b338e4a |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| questions | output | .agents/mechanisms/questions/questions.md | 6af1e49859ff1b940ef9bbdb5d051e2c99b9c5489919286573e1957a0df5da08 |
| questions | output | .agents/mechanisms/questions/questions.rules.md | db8edb789517688203e8e9251a909d9ac384fe0bf9c3771d82411942b39cfa9b |
| questions | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| questions | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| questions | output | .agents/skills/questions/QUESTION-FORMAT.md | efbf0b2d2e629300953f7752c1dec9a40fd4c7a2de1beba465c26a9d000fa369 |
| questions | output | .agents/skills/questions/SKILL.md | 5655eb89b1b451638441e6f80647743350d61f6edf0399e05c46f8f76b338e4a |
| questions | output | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | output | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | output | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | output | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| session | parts | .agents/mechanisms/session/session.rules.md | 0f57f697b28b772cd4573217518abcd8cfa3e05bd98a64e04f3d9892719e4116 |
| session | parts | .agents/scripts/gw/sessions.py | 59d01614816b3d105d60b0ff45fbb14dcd94d2890cf4cae5f96f32484bdd6c85 |
| session | parts | .agents/scripts/gw/test/test_sessions.py | 17398f92991625c1528c89b55af78582efa3251a7123c15e748235f59db0004f |
| session | parts | .agents/skills/conclude/SKILL.md | 2c812f0a10996f2431077370c2da42f4f55dbe9185eafdfe52bbeaedb9759a84 |
| session | parts | .agents/skills/recall/SKILL.md | d80a332103711966fb24ad2f35e5a3c3b91115670c5589e8a930b94208fa96b5 |
| session | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| session | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| session | output | .agents/mechanisms/session/session.md | 9bbcb1cf04165877166f1075dc91cefce599755ef5d294d71339cb6022733c00 |
| session | output | .agents/mechanisms/session/session.rules.md | 0f57f697b28b772cd4573217518abcd8cfa3e05bd98a64e04f3d9892719e4116 |
| session | output | .agents/skills/conclude/SKILL.md | 2c812f0a10996f2431077370c2da42f4f55dbe9185eafdfe52bbeaedb9759a84 |
| session | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| session | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| session | output | .agents/skills/recall/SKILL.md | d80a332103711966fb24ad2f35e5a3c3b91115670c5589e8a930b94208fa96b5 |
| ticket | parts | .agents/mechanisms/ticket/ticket.rules.md | d68098d896a17ed5ccef64842539dcbd943436ad28b46611e4242aea4728531b |
| ticket | parts | .agents/scripts/gw/move_doc.py | f366f5831c6eb9600e77228898893ebdfe879a20a9796f7fca6c29692fbb1efe |
| ticket | parts | .agents/scripts/gw/test/test_citations.py | dbde70f3d00e122d5dcceda2fd5ad8c9cbe89ed98952cc44fe4f7778c67a8d4a |
| ticket | parts | .agents/scripts/gw/test/test_command_line.py | 7f038df6e53672efb853180ad059cf16126e9553323cb0487f29a79d3b03a875 |
| ticket | parts | .agents/scripts/gw/test/test_failure_contract.py | fb98267bdfca71023f00f5a36ac2734afaeaced6ee20d671836583b22e7482c9 |
| ticket | parts | .agents/scripts/gw/test/test_paired_close.py | 8a6f57f07c743bbfe594ab6002659943a07896e74328c61387e10006f6304315 |
| ticket | parts | .agents/scripts/gw/test/test_refusals.py | e57dc3df0c656820945a2be6824cc57fdcdba856738fc92c324223af6b6f45a2 |
| ticket | parts | .agents/scripts/gw/test/test_tickets.py | 6d2eeb2f02c76f57c2a30d6e0bceb1021bfea90ac36476672b4ac67f217f18da |
| ticket | parts | .agents/scripts/gw/tickets.py | 1141d91ece7afab66a0b13521a94aef9dafb6801c334e3b07ea8043f4c5ff522 |
| ticket | parts | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | parts | .agents/skills/ticket/SKILL.md | 1d6897d3d3aca84f8f97afc05b4c74f8fd86f23853b3979391193453a83e220b |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | fcfd6a1d35dc87b259db95d4605e6c9cd0dd6e49cfbbad47ee817161960d35f0 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| ticket | output | .agents/mechanisms/ticket/ticket.md | 9eacbcdf94b35feccb1bc510db6d17603cfae32799185485661c9425ca34dd39 |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | d68098d896a17ed5ccef64842539dcbd943436ad28b46611e4242aea4728531b |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 2eee339e42db04c911ba26ee3f57ba8240c14042fe24d44bcb31e87d11aa9dea |
| ticket | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| ticket | output | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | output | .agents/skills/ticket/SKILL.md | 1d6897d3d3aca84f8f97afc05b4c74f8fd86f23853b3979391193453a83e220b |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | fcfd6a1d35dc87b259db95d4605e6c9cd0dd6e49cfbbad47ee817161960d35f0 |
