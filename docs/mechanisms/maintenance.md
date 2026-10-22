# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| edge | parts | e6e14c7efa592ec2a651bfeb184d5efaae5e9c46c7fbc1dc5e3412efc00c8f7f | 2026-10-19 | nothing to change |
| edge | output | 8cdc0edf39138e18b70395ff25f62994d57485edd96e42d614f5447542938f40 | 2026-10-19 | nothing to change |
| harness | parts | c5a7a78cedd272efcc982f41b8d7caeafd6b42b6963525ffb41a171956073ca6 | 2026-10-22 | nothing to change |
| harness | output | bd614110d4d648055dae928f0252a3da75d72ddb0362880f0319a6d3fa5b4510 | 2026-10-14 | nothing to change |
| maintain | parts | efc01f2b8dd685f86146b15f1d5f290e7dce6f1a6370680c280100414585eb04 | 2026-10-19 | amended |
| maintain | output | a3c2054236dfbf6b5fffbc8f84fcc174177ac7f601bc5061830dd987e00a41b2 | 2026-10-19 | nothing to change |
| mechanism-shape | parts | 0c6cc99c8afbacae55972ff931b31fdb415b9fe961d8f8536ce8546eea918312 | 2026-10-19 | nothing to change |
| mechanism-shape | output | 3c2a9607a162fa442fa479ac5d3842b8a399f6d2fba192595362745049d40b83 | 2026-10-19 | nothing to change |
| product | parts | 9207784985dd606ba5e8fe2339da592286612f021f6f5f2349fd2abb294d3225 | 2026-10-19 | nothing to change |
| product | output | c7bd0085b16a38a032ab98f269ae30e4bc5359dca0d524c99991cfa552fdfd77 | 2026-10-19 | nothing to change |
| questions | parts | 45f4343270e581ff07dc66aa07dd54bb17ca893811e6bddc5f35fe9cb8663d8c | 2026-10-22 | nothing to change |
| questions | output | 2196b5264561b61fa478278d74e7a2896ea656d6d8709fa6ec9c3f19cacb1014 | 2026-10-22 | nothing to change |
| ticket | parts | e4e29dd1df980406445f03c9bf6e693b183fefe736697d917372b63a03ac32e9 | 2026-10-19 | amended |
| ticket | output | 83d23568c3465f37f687e19f8e0f71a2302d46c98209c0b7a761b30d7165c5c4 | 2026-10-22 | nothing to change |

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
| edge | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| edge | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| harness | parts | .agents/scripts/gw/harness.py | 84f89d3ff842f7fab391938ec8300746e81f3192de371ca512847cea2a49935c |
| harness | parts | .agents/scripts/gw/test/test_harness.py | 14f035d925aee384f157ccd7e191b0c52b85d58d0e1536ab4b22bf3e13650fd7 |
| harness | parts | .agents/skills/harness/SKILL.md | 993348a51338084ac8e162bc38e37d2d85b1838333fd8a18633a473f9e0ecf2e |
| harness | parts | AGENTS.md | 7e97f1fec0d6c5fe3ef0ed3e5105933eee12d94f2d0f9016d2900dcee5fe7294 |
| harness | parts | CLAUDE.md | 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49 |
| harness | output | .agents/mechanisms/harness/harness.md | 0390f39281e7f60f661fc73b81ee3b6e25b5af01ed7d52d61ea9eab7b3ef8b36 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 03179ed5a91a76be74c29fa9918e84bb73a1b13109d68dd8589a5f67f7cd0284 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| harness | output | .agents/skills/harness/SKILL.md | 4a270360d7fb4227cc0b3442de92cbc30c9065ca212bbc56fd9d634fb72025d0 |
| harness | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| harness | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| maintain | parts | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | parts | .agents/scripts/gw/maintain.py | 89e39e230c0aaf9bdc0f396e75c06986b455445829c779f527e8340fd1f5fbee |
| maintain | parts | .agents/scripts/gw/straw_dogs.py | ce01cdbd5162766129d2b56c1815a3a054ded5167cbce6ba7f47437f22657925 |
| maintain | parts | .agents/scripts/gw/test/test_maintain.py | 752004ea1b7de3efcf4748c9a04cf18c31d09e1d841cbc2a1d5f8dd3e46ef03e |
| maintain | parts | .agents/scripts/gw/test/test_straw_dogs.py | d6f39f4245ffff85c0158dbb0202e0338b42238153adcbe33cecb2774b7ac697 |
| maintain | parts | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | parts | .agents/skills/maintain/SKILL.md | 6ba2bc394278d3a5426467cceb72e92b6d6165dcf3a36ffb5b40f3c007e812b8 |
| maintain | output | .agents/mechanisms/maintain/maintain.md | 78dd72ea13c69e1fb7ed0502e2d59fb6b36ccb18bb6bce4c96bc35403756a79e |
| maintain | output | .agents/mechanisms/maintain/maintain.rules.md | 1ce702ad5f0633581d11f18f0e1418257d2e35e363bb863ebc9fb544bd4725d9 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| maintain | output | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | output | .agents/skills/maintain/SKILL.md | 6ba2bc394278d3a5426467cceb72e92b6d6165dcf3a36ffb5b40f3c007e812b8 |
| maintain | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| maintain | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| mechanism-shape | parts | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | 20a6bf08a7648453ea8a1d23ddcc141f8aa1cc2347bbb4bc46c28fb830070fcd |
| mechanism-shape | parts | .agents/scripts/gw/inject_rules.py | 6b9bcfd51543495869f0744a4e5dc4defe63092ed3631598fe7b798bdc9d3fd5 |
| mechanism-shape | parts | .agents/scripts/gw/mechanisms.py | 9f6608007a7d70d21b6d491c41185ffd7599244f8bd577e27c0e33146ae1b90a |
| mechanism-shape | parts | .agents/scripts/gw/test/repository.py | 421f300b5d4eceb06652e69ad37c3765a9a2c5bb9f107a8c2385d5344fd12fab |
| mechanism-shape | parts | .agents/scripts/gw/test/test_inject_rules.py | 066f82b461fb0a4413385072ac323a312c0e73437b159c046e530e2dd925860d |
| mechanism-shape | parts | .agents/scripts/gw/test/test_mechanisms.py | 0bbe055180c966406217e5169c1d3769712b98ae1e3775a2f5762cbd6065b185 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_repository.py | 61c008b612db93199ef86349eb3a9931479c3c33de1724365f90b293593d0e69 |
| mechanism-shape | parts | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| mechanism-shape | parts | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| mechanism-shape | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| mechanism-shape | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
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
| product | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| product | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| product | output | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | output | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | output | .agents/skills/product/SKILL.md | 69e74e5999ddaad12ab16555ac321b42cacd240e7793dd6b6c63b0879f67f481 |
| questions | parts | .agents/.gitattributes | bd95d1f719ab960c7d638d202a762ab72f356be5be7270623165327a47e28149 |
| questions | parts | .agents/mechanisms/questions/questions.rules.md | 1260648c7a7556db55294819c1a1582b775dedc361a04f13e5284aaa42e02657 |
| questions | parts | .agents/scripts/gw/hook.sh | 0118d8145545019d8121a339242fc9795690bb554d2375a8f89a3b4de27ba83e |
| questions | parts | .agents/scripts/gw/questions.py | 013f5811a925a2877fa65c36b41f5621623952724dfa9840feec4062bf937f5b |
| questions | parts | .agents/scripts/gw/test/test_questions.py | ecf617d6901e6232dab82f1c4d7a05bd8bdb5af795766ae21fcd687536d303bd |
| questions | parts | .agents/skills/questions/QUESTION-FORMAT.md | eb7d7863b8a4ca80e8f4e1bbb9bc08f30481d007c4b74ee9163cd192ee2e29a6 |
| questions | parts | .agents/skills/questions/SKILL.md | 9afe0978af79816acf0aa86495e89f61681bc4e40af8a84918154f69ae177b52 |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| questions | output | .agents/mechanisms/questions/questions.md | 366bbbc97f07aacb9d7010adaad4e708e68ee99df3f32602026bf6f16c5b5b0c |
| questions | output | .agents/mechanisms/questions/questions.rules.md | 1260648c7a7556db55294819c1a1582b775dedc361a04f13e5284aaa42e02657 |
| questions | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| questions | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| questions | output | .agents/skills/questions/QUESTION-FORMAT.md | eb7d7863b8a4ca80e8f4e1bbb9bc08f30481d007c4b74ee9163cd192ee2e29a6 |
| questions | output | .agents/skills/questions/SKILL.md | 9afe0978af79816acf0aa86495e89f61681bc4e40af8a84918154f69ae177b52 |
| questions | output | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | output | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | output | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | output | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
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
| ticket | parts | .agents/skills/ticket/SKILL.md | 6970a291fe378255c30ed5eda1927df71b430b5baaed71f4c977d35a8b164078 |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | fcfd6a1d35dc87b259db95d4605e6c9cd0dd6e49cfbbad47ee817161960d35f0 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 926a299cc8b0af0fe4a11071c32f127d23e39db600c4124d31266e112a6ba70e |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2e681b0e5f05f91417d4745bfdb08f7d7d50152c91ad3db8b631b757dc941308 |
| ticket | output | .agents/mechanisms/ticket/ticket.md | 9eacbcdf94b35feccb1bc510db6d17603cfae32799185485661c9425ca34dd39 |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | d68098d896a17ed5ccef64842539dcbd943436ad28b46611e4242aea4728531b |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | daa56fcbacf1109796fa9fad70d7328d75edb16162502e856173d86169d08992 |
| ticket | output | .agents/skills/mechanism/SKILL.md | 14e6d50374c7372786200c1e2c3e622af31547b0fa9f23ecb359393d229ef0ed |
| ticket | output | .agents/skills/ticket/QUEUE-ARRIVAL.md | 415fe65d77b694401922169c06f14756369f52d3bff471216b491b7adee2ac5e |
| ticket | output | .agents/skills/ticket/SKILL.md | 6970a291fe378255c30ed5eda1927df71b430b5baaed71f4c977d35a8b164078 |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | fcfd6a1d35dc87b259db95d4605e6c9cd0dd6e49cfbbad47ee817161960d35f0 |
