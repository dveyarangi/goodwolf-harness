# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| debugging | parts | 161b0018f05295045e5d628a40455cacbc5a223b715b96706a7b696ffadd670b | 2026-10-23 | nothing to change |
| debugging | output | 833973d7c921ba314d6eb43501db8f1bb954c11ce53e649be061b8ffefefe827 | 2026-10-25 | nothing to change |
| edge | parts | e6e14c7efa592ec2a651bfeb184d5efaae5e9c46c7fbc1dc5e3412efc00c8f7f | 2026-10-19 | nothing to change |
| edge | output | 0d5f07bc4d96e7c469eb6624c7b5c6c97636a3c8e63f56a52619f0c72356d8b9 | 2026-10-25 | nothing to change |
| harness | parts | ede648840bdad0b452a457f725ce2c3e983b3516587a68ca508f8af9fea6713e | 2026-10-24 | amended |
| harness | output | 89e48e29d84b00e075e3ff74ad7335d62cbcefcba5d2e50b8517eae600c2d852 | 2026-10-24 | nothing to change |
| maintain | parts | 0b7cf13da2a4aca51a0551b27b4b77c98d86091a0f43202bdadf6cb86d4ee8d9 | 2026-10-25 | nothing to change |
| maintain | output | 3f877b3ab23e1750adaaef3cf7858a6e1d2dff026588a95442f9450f96d6a622 | 2026-10-25 | nothing to change |
| mechanism-shape | parts | a88b8d7737794a49e2ee6405043d7437a30946e3db986de5a3681a9eef1d7df7 | 2026-10-25 | nothing to change |
| mechanism-shape | output | 6a89b08f2461c6cfd1aebac7bd7d85030afcbecc310da2752c591ac67f46e6da | 2026-10-25 | nothing to change |
| product | parts | c7aad792e03dccf07f58260f94e86a95625e856e4082ae6d3f3c19fbffd4613d | 2026-10-25 | nothing to change |
| product | output | 5b3a462f22a78d1e7e5ffd6a4852747efb8c934ee77e9130fc1c2bac93d46bf6 | 2026-10-25 | nothing to change |
| questions | parts | e9d71b5e55eb451d01c326e90e18b896cd4d77b56fffe327ffaf38a8e2b1a448 | 2026-10-25 | nothing to change |
| questions | output | e397cc3473802cfb9c1b846c20fe988cef3851a290ef6567b9707826452c0c10 | 2026-10-25 | nothing to change |
| session | parts | 42dca8df4bc8f6c4e4aeb38182fc2a385eef9131c8d8ba59390a37cb166522f3 | 2026-10-24 | nothing to change |
| session | output | 1f306eb43d955812405a3ed6632d541c51ecf67f8e13743642ba1151cf17f98e | 2026-10-24 | nothing to change |
| ticket | parts | d9ca62e68029b81f5e395bacff8751da5fa15457924718f4134cbc08590c53fb | 2026-10-25 | nothing to change |
| ticket | output | b2155acc1654fb562ac2b382effc3beb4442cd0eb75f5d8d7c851e41d00db785 | 2026-10-25 | nothing to change |

| mechanism | level | file | fingerprint |
|---|---|---|---|
| debugging | parts | .agents/mechanisms/debugging/debugging.rules.md | 0dc7d6c72884bdbef2c4e6166f4a8c9e21e77e0ea7ed79c25ee36117df734107 |
| debugging | parts | .agents/skills/debugging/SKILL.md | 61a1cdbaf867e3d3c79f51722e4e8838b11da1b9890f1db53d9df9d1cb21415d |
| debugging | output | .agents/mechanisms/debugging/debugging.md | 47f527dd8638ef9d6a391155c7d955acdf06a22a8c5b5c38cba83f7be8122f22 |
| debugging | output | .agents/mechanisms/debugging/debugging.rules.md | 0dc7d6c72884bdbef2c4e6166f4a8c9e21e77e0ea7ed79c25ee36117df734107 |
| debugging | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| debugging | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| debugging | output | .agents/skills/debugging/SKILL.md | 61a1cdbaf867e3d3c79f51722e4e8838b11da1b9890f1db53d9df9d1cb21415d |
| debugging | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fc2574353313d8b468530f599f7b3ef3e56ebbacd976b01655d438f949445daa |
| debugging | output | .agents/skills/mechanism/SKILL.md | c47a22059c2d8256084036efe2db72ddb68fb92cd7b92239c5cd0ff9dcb2fecf |
| edge | parts | .agents/mechanisms/edge/edge.rules.md | 59963f35ba6e27067f22082a704fab893f9ab6140333cb89f4d2c6480e135d19 |
| edge | parts | .agents/scripts/gw/edges.py | 68840b8119aede816e6324e215babf0691dbb38e4d58da90fe2487c1f5dfe06e |
| edge | parts | .agents/scripts/gw/test/test_edges.py | 1980d8e8ade71435c1d32b1c7fff4603d175897703dfa63d1e245dc19e2a3a7b |
| edge | parts | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | parts | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/mechanisms/edge/edge.md | ab4782a9b90306213ec009e555dca72c7b6571ec37a63d7dd4bd7d00af59a223 |
| edge | output | .agents/mechanisms/edge/edge.rules.md | 59963f35ba6e27067f22082a704fab893f9ab6140333cb89f4d2c6480e135d19 |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| edge | output | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | output | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fc2574353313d8b468530f599f7b3ef3e56ebbacd976b01655d438f949445daa |
| edge | output | .agents/skills/mechanism/SKILL.md | c47a22059c2d8256084036efe2db72ddb68fb92cd7b92239c5cd0ff9dcb2fecf |
| harness | parts | .agents/scripts/gw/harness.py | a34410e0aea019d99bbbea8981d9ceded8b1e4645a4acd1b4d7d76b4ca15ae76 |
| harness | parts | .agents/scripts/gw/test/test_harness.py | 0e978c7914ff384bbf5da294ec5cf1be017c9ea1c7588ad3910a9cea6185ef50 |
| harness | parts | .agents/skills/harness/MEETING.md | ff9c691c532cce157d0b9f45867a21e6cdbbfbf2a6d7b923364ecefff2b8b8de |
| harness | parts | .agents/skills/harness/SKILL.md | d0c89f0b97c36cc80d6b489b2369f5bbdf097cb79e3078eea76e05819c1c30b6 |
| harness | parts | AGENTS.md | 0d8fb61a582b3a4749cc02a00ea7f439f6bbfcfef0039a1ff51399f648aac417 |
| harness | parts | CLAUDE.md | 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49 |
| harness | output | .agents/mechanisms/harness/harness.md | 4ecb1eeee627704dc0d851f59475af6f13c0cbd20b6f87d7e05a650d22b10ca2 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| harness | output | .agents/skills/harness/MEETING.md | ff9c691c532cce157d0b9f45867a21e6cdbbfbf2a6d7b923364ecefff2b8b8de |
| harness | output | .agents/skills/harness/SKILL.md | d0c89f0b97c36cc80d6b489b2369f5bbdf097cb79e3078eea76e05819c1c30b6 |
| harness | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 422bbdf31e5378d2cd4967dec77648857a1d9f9211eeda56e2b3f5d292d4fab9 |
| harness | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| maintain | parts | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | parts | .agents/scripts/gw/maintain.py | 08ecf2ff91fd8edfa6206f844a1c557a704155854d6d1e11e1651bf4cdc9c4c2 |
| maintain | parts | .agents/scripts/gw/straw_dogs.py | ce01cdbd5162766129d2b56c1815a3a054ded5167cbce6ba7f47437f22657925 |
| maintain | parts | .agents/scripts/gw/test/test_maintain.py | 752004ea1b7de3efcf4748c9a04cf18c31d09e1d841cbc2a1d5f8dd3e46ef03e |
| maintain | parts | .agents/scripts/gw/test/test_straw_dogs.py | d6f39f4245ffff85c0158dbb0202e0338b42238153adcbe33cecb2774b7ac697 |
| maintain | parts | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | parts | .agents/skills/maintain/SKILL.md | bb604bd69d01df179672db56a6a448908e55eefa162fe4318f4ab1faa6bf4d21 |
| maintain | output | .agents/mechanisms/maintain/maintain.md | 4947b99466b0bb47f698552360a23156078cbcd8d729085b9ec1948769122737 |
| maintain | output | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| maintain | output | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | output | .agents/skills/maintain/SKILL.md | bb604bd69d01df179672db56a6a448908e55eefa162fe4318f4ab1faa6bf4d21 |
| maintain | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fc2574353313d8b468530f599f7b3ef3e56ebbacd976b01655d438f949445daa |
| maintain | output | .agents/skills/mechanism/SKILL.md | c47a22059c2d8256084036efe2db72ddb68fb92cd7b92239c5cd0ff9dcb2fecf |
| mechanism-shape | parts | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | 20a6bf08a7648453ea8a1d23ddcc141f8aa1cc2347bbb4bc46c28fb830070fcd |
| mechanism-shape | parts | .agents/scripts/gw/hook.sh | 686ae17cc84f575a9983818199e0c186c00644d37f9aa10e2e18b0993a987f8c |
| mechanism-shape | parts | .agents/scripts/gw/inject_rules.py | e5a5044242624e84406d1259b38ccdf2471bc1a9345bbb5f5af9153909bdd1e5 |
| mechanism-shape | parts | .agents/scripts/gw/mechanisms.py | 2e3e840ed34318d4796e0e1a2d027f7aff10df27ac86eaf7439c2f8c58c5e22d |
| mechanism-shape | parts | .agents/scripts/gw/test/repository.py | 421f300b5d4eceb06652e69ad37c3765a9a2c5bb9f107a8c2385d5344fd12fab |
| mechanism-shape | parts | .agents/scripts/gw/test/test_inject_rules.py | 641aec70dfee02347da2b0a6830bca992e872d51f3d460700bfb282b1ba12d4c |
| mechanism-shape | parts | .agents/scripts/gw/test/test_mechanisms.py | bdf423c1b4148a30361e538cf5ae1e5e9b800fd2bd31c9f16f41a6fbda4743f4 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_repository.py | 61c008b612db93199ef86349eb3a9931479c3c33de1724365f90b293593d0e69 |
| mechanism-shape | parts | .agents/skills/mechanism/MECHANISM-FORMAT.md | fc2574353313d8b468530f599f7b3ef3e56ebbacd976b01655d438f949445daa |
| mechanism-shape | parts | .agents/skills/mechanism/SKILL.md | c47a22059c2d8256084036efe2db72ddb68fb92cd7b92239c5cd0ff9dcb2fecf |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fc2574353313d8b468530f599f7b3ef3e56ebbacd976b01655d438f949445daa |
| mechanism-shape | output | .agents/skills/mechanism/SKILL.md | c47a22059c2d8256084036efe2db72ddb68fb92cd7b92239c5cd0ff9dcb2fecf |
| product | parts | .agents/mechanisms/product/product.rules.md | 05f71cc357a3c753f038e5920edf6bc6a59d3f39b8f9a61628a29cd03c0a0bac |
| product | parts | .agents/scripts/gw/product.py | 5f4accefb6d382d2b2053b2b9e5184f996940ff8571af41095e251cd33ad138a |
| product | parts | .agents/scripts/gw/test/test_product.py | 0eb917e0bb1c93f8644b910af8c2dd9d23b7ab5ada40b0fb292d1f440cf7c0c5 |
| product | parts | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | parts | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | parts | .agents/skills/product/SKILL.md | 69e74e5999ddaad12ab16555ac321b42cacd240e7793dd6b6c63b0879f67f481 |
| product | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| product | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| product | output | .agents/mechanisms/product/product.md | dbf73a93bd4c237061ba240b169aa88bb78807240929819db3173a4183607de9 |
| product | output | .agents/mechanisms/product/product.rules.md | 05f71cc357a3c753f038e5920edf6bc6a59d3f39b8f9a61628a29cd03c0a0bac |
| product | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fc2574353313d8b468530f599f7b3ef3e56ebbacd976b01655d438f949445daa |
| product | output | .agents/skills/mechanism/SKILL.md | c47a22059c2d8256084036efe2db72ddb68fb92cd7b92239c5cd0ff9dcb2fecf |
| product | output | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | output | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | output | .agents/skills/product/SKILL.md | 69e74e5999ddaad12ab16555ac321b42cacd240e7793dd6b6c63b0879f67f481 |
| questions | parts | .agents/.gitattributes | bd95d1f719ab960c7d638d202a762ab72f356be5be7270623165327a47e28149 |
| questions | parts | .agents/mechanisms/questions/questions.rules.md | fc25d27e5bb546ac50a633aebcd9cf3288e7aeb662f224ba282aae4540ec3345 |
| questions | parts | .agents/scripts/gw/questions.py | 8eec756aeb6e7844264fc5a4e14f0c6117753c1c5be70a59b8a00c936292e813 |
| questions | parts | .agents/scripts/gw/test/test_questions.py | 56f3235c23bb39db57f744513566ecd6ff03c9711a484d7f1ec781008d86df86 |
| questions | parts | .agents/skills/questions/QUESTION-FORMAT.md | efbf0b2d2e629300953f7752c1dec9a40fd4c7a2de1beba465c26a9d000fa369 |
| questions | parts | .agents/skills/questions/SKILL.md | 5655eb89b1b451638441e6f80647743350d61f6edf0399e05c46f8f76b338e4a |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| questions | output | .agents/mechanisms/questions/questions.md | 8f631df73ce6d6ef7789a2236690b270adb9cafda21e0b5b533ea3cda7f1a350 |
| questions | output | .agents/mechanisms/questions/questions.rules.md | fc25d27e5bb546ac50a633aebcd9cf3288e7aeb662f224ba282aae4540ec3345 |
| questions | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fc2574353313d8b468530f599f7b3ef3e56ebbacd976b01655d438f949445daa |
| questions | output | .agents/skills/mechanism/SKILL.md | c47a22059c2d8256084036efe2db72ddb68fb92cd7b92239c5cd0ff9dcb2fecf |
| questions | output | .agents/skills/questions/QUESTION-FORMAT.md | efbf0b2d2e629300953f7752c1dec9a40fd4c7a2de1beba465c26a9d000fa369 |
| questions | output | .agents/skills/questions/SKILL.md | 5655eb89b1b451638441e6f80647743350d61f6edf0399e05c46f8f76b338e4a |
| questions | output | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | output | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | output | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | output | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| session | parts | .agents/mechanisms/session/session.rules.md | 1345365f24e89ada89143aadd0933b4e28ed6dfeeaea0d84b96c7173b5fb93e1 |
| session | parts | .agents/scripts/gw/sessions.py | 59d01614816b3d105d60b0ff45fbb14dcd94d2890cf4cae5f96f32484bdd6c85 |
| session | parts | .agents/scripts/gw/test/test_sessions.py | 4837cd6fee3c361309dc66d9bfd8d14248597350f895f67846208831f613accc |
| session | parts | .agents/skills/conclude/SKILL.md | 2c812f0a10996f2431077370c2da42f4f55dbe9185eafdfe52bbeaedb9759a84 |
| session | parts | .agents/skills/recall/SKILL.md | d80a332103711966fb24ad2f35e5a3c3b91115670c5589e8a930b94208fa96b5 |
| session | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| session | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| session | output | .agents/mechanisms/session/session.md | 992b7f6a2686680f0b5410f358ab40a78caa10a9e7c2e1d2585ab6c78c4974eb |
| session | output | .agents/mechanisms/session/session.rules.md | 1345365f24e89ada89143aadd0933b4e28ed6dfeeaea0d84b96c7173b5fb93e1 |
| session | output | .agents/skills/conclude/SKILL.md | 2c812f0a10996f2431077370c2da42f4f55dbe9185eafdfe52bbeaedb9759a84 |
| session | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 422bbdf31e5378d2cd4967dec77648857a1d9f9211eeda56e2b3f5d292d4fab9 |
| session | output | .agents/skills/mechanism/SKILL.md | 8841707ffc23f691808d2d77177aeb5a7d1c4d0cc049842e00e09cd1a19fc9a2 |
| session | output | .agents/skills/recall/SKILL.md | d80a332103711966fb24ad2f35e5a3c3b91115670c5589e8a930b94208fa96b5 |
| ticket | parts | .agents/mechanisms/ticket/ticket.rules.md | 7d0340083009920181fdf1509eecfa63ba0903e8e789a1ed190b37f2c6255bb1 |
| ticket | parts | .agents/scripts/gw/move_doc.py | f366f5831c6eb9600e77228898893ebdfe879a20a9796f7fca6c29692fbb1efe |
| ticket | parts | .agents/scripts/gw/test/test_citations.py | dbde70f3d00e122d5dcceda2fd5ad8c9cbe89ed98952cc44fe4f7778c67a8d4a |
| ticket | parts | .agents/scripts/gw/test/test_command_line.py | 7f038df6e53672efb853180ad059cf16126e9553323cb0487f29a79d3b03a875 |
| ticket | parts | .agents/scripts/gw/test/test_failure_contract.py | fb98267bdfca71023f00f5a36ac2734afaeaced6ee20d671836583b22e7482c9 |
| ticket | parts | .agents/scripts/gw/test/test_paired_close.py | 8a6f57f07c743bbfe594ab6002659943a07896e74328c61387e10006f6304315 |
| ticket | parts | .agents/scripts/gw/test/test_refusals.py | e57dc3df0c656820945a2be6824cc57fdcdba856738fc92c324223af6b6f45a2 |
| ticket | parts | .agents/scripts/gw/test/test_tickets.py | d77724467475c5f62bfec8898ed3c4e31cb2184ae6595bcffac5e7aeac9c11b3 |
| ticket | parts | .agents/scripts/gw/tickets.py | 117bbe6077591447a07fca90f0616a1a807bfc0d3326ccc21ef7a3db4bc58395 |
| ticket | parts | .agents/skills/ticket/QUEUE-ARRIVAL.md | 36441d38441f80b5163e5bd2046d9e29284fc70e85e9fbe29123a8d4a51d0a1d |
| ticket | parts | .agents/skills/ticket/SKILL.md | 1d6897d3d3aca84f8f97afc05b4c74f8fd86f23853b3979391193453a83e220b |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | 709a6c5b14a2510bbc5fe34ad68f6d562a7b0792409ec18e27a3dab63dd60db6 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | e9b706af39fb0cc75410ca13549c86b5f43b4a26d0b31aee02b57b7be4a9280e |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| ticket | output | .agents/mechanisms/ticket/ticket.md | 813e90013105bd2455e61f92968326db56439aec20998937508a927bcf3b3a6f |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | 7d0340083009920181fdf1509eecfa63ba0903e8e789a1ed190b37f2c6255bb1 |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fc2574353313d8b468530f599f7b3ef3e56ebbacd976b01655d438f949445daa |
| ticket | output | .agents/skills/mechanism/SKILL.md | c47a22059c2d8256084036efe2db72ddb68fb92cd7b92239c5cd0ff9dcb2fecf |
| ticket | output | .agents/skills/ticket/QUEUE-ARRIVAL.md | 36441d38441f80b5163e5bd2046d9e29284fc70e85e9fbe29123a8d4a51d0a1d |
| ticket | output | .agents/skills/ticket/SKILL.md | 1d6897d3d3aca84f8f97afc05b4c74f8fd86f23853b3979391193453a83e220b |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | 709a6c5b14a2510bbc5fe34ad68f6d562a7b0792409ec18e27a3dab63dd60db6 |
