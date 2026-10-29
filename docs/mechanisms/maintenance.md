# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| debugging | parts | f4d31bdcfe36e9126fdd4f746a5bc1b086b48b2069aa2aaca577b8e553886b8e | 2026-10-26 | nothing to change |
| debugging | output | 2cf5b23c4b6425202b82436d6db49c80bb3e14baea034607de1f142259ea364c | 2026-10-26 | nothing to change |
| edge | parts | e6e14c7efa592ec2a651bfeb184d5efaae5e9c46c7fbc1dc5e3412efc00c8f7f | 2026-10-19 | nothing to change |
| edge | output | 58f7f343beded8e2e089e4e4d2c0c8969588169e085c287d9b41ac32b503c7b5 | 2026-10-26 | nothing to change |
| harness | parts | 7e49b7252c500ef8ec7d58b37c4b6ee890c5e851dea1bad2cb1896fbe340e0f2 | 2026-10-26 | nothing to change |
| harness | output | fdf461ec0a27dfa28d1af7c3f7d2f60c7c27f78e4ac04139417d825b0e6946e9 | 2026-10-26 | nothing to change |
| maintain | parts | f98b0358b2b722d5df8b835d2133e31de118d4eabde08458b6f0f1e620520530 | 2026-10-26 | amended |
| maintain | output | 55dc70b345443b193db2f66e45aecfe0b3a29e3d5f1e9f025514962e994aa47d | 2026-10-26 | nothing to change |
| mechanism-shape | parts | 6d616dd434d074615d066adc0fc4904efccda2e0c59470577fd6c30de42fcefc | 2026-10-26 | amended |
| mechanism-shape | output | 8b2c02112ffa576563652e7f9ca2c2b82bbf1aa98473699681e4aa7c3396d061 | 2026-10-26 | amended |
| product | parts | a00d42f5aa676837ec01d91eac6dac65d2036b260b70e2a12ada357fbbe9997b | 2026-10-26 | nothing to change |
| product | output | 0c66982358f43f1b10ce83b88316d142683ea0906416a71c5ddeba575daad434 | 2026-10-26 | nothing to change |
| questions | parts | 9342fdabb13b4850108b2263da5c55acf10fce6c051b2e59ab266121df5df7c8 | 2026-10-26 | nothing to change |
| questions | output | e7f3229fb7b930c6ac884304e92c6a581b15098db7627a8224e92d12cf6f6a4b | 2026-10-26 | nothing to change |
| session | parts | c875456af6848e12d1a3b411b84c3d47d0299724ccf762a795751997ffd3642e | 2026-10-26 | nothing to change |
| session | output | e209db6eb87c4a30b885864b7ffb6611b87ced14aa24c2dea7eefcb2d32910d3 | 2026-10-26 | nothing to change |
| ticket | parts | b2e4381e84d98dc9062a8831fd0c66cba70855ec8da87d1409190710eee4cc26 | 2026-10-26 | amended |
| ticket | output | ede7104aa46eb69573781ea4c2cdbedd8ececec8c5716bb7502ceb083d929c30 | 2026-10-26 | nothing to change |
| * | decisions | 2950f835586086ff7e9bf0f687d38b7fbb76e44e | 2026-10-29 | nothing to change |

| mechanism | level | file | fingerprint |
|---|---|---|---|
| debugging | parts | .agents/mechanisms/debugging/debugging.rules.md | 1276d40d429a505026183defde7246eef8894cfa9b55ea70d13e96dec9c99e7c |
| debugging | parts | .agents/skills/debugging/SKILL.md | aab980d308479cf3ad63959ad2f40a13306f290f9e5fa30e1b8894fb594d402a |
| debugging | output | .agents/mechanisms/debugging/debugging.md | 6d5d684fa721c8fa6e6a0e4f32c637751e68c2e8ff9ee350b78df16983fab7ea |
| debugging | output | .agents/mechanisms/debugging/debugging.rules.md | 1276d40d429a505026183defde7246eef8894cfa9b55ea70d13e96dec9c99e7c |
| debugging | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| debugging | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| debugging | output | .agents/skills/debugging/SKILL.md | aab980d308479cf3ad63959ad2f40a13306f290f9e5fa30e1b8894fb594d402a |
| debugging | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| debugging | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| edge | parts | .agents/mechanisms/edge/edge.rules.md | 59963f35ba6e27067f22082a704fab893f9ab6140333cb89f4d2c6480e135d19 |
| edge | parts | .agents/scripts/gw/edges.py | 68840b8119aede816e6324e215babf0691dbb38e4d58da90fe2487c1f5dfe06e |
| edge | parts | .agents/scripts/gw/test/test_edges.py | 1980d8e8ade71435c1d32b1c7fff4603d175897703dfa63d1e245dc19e2a3a7b |
| edge | parts | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | parts | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/mechanisms/edge/edge.md | ab4782a9b90306213ec009e555dca72c7b6571ec37a63d7dd4bd7d00af59a223 |
| edge | output | .agents/mechanisms/edge/edge.rules.md | 59963f35ba6e27067f22082a704fab893f9ab6140333cb89f4d2c6480e135d19 |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| edge | output | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | output | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| edge | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| harness | parts | .agents/scripts/gw/harness.py | 79e3075fe276ef0ce01ee12ff840a1dcfe1af2f15364cbeae5253266089c52e6 |
| harness | parts | .agents/scripts/gw/test/test_harness.py | 81c09dfd0cbfdd4e7194afc0af351c364e6fb96aaa2c627a332deabb3011279c |
| harness | parts | .agents/skills/harness/MEETING.md | cd39fb09797ee49597872ef0aca3565f8e8913d810611d8649e79fd6dc8969e5 |
| harness | parts | .agents/skills/harness/SKILL.md | 577f0ca35f276f53e52f16ec19d47a6e440275221dec007d7c90c169e55b9e86 |
| harness | parts | AGENTS.md | 678c0bc1eb58d51495da0df70f0d31c8194c2f62d19e7f4492e81f223002bcb9 |
| harness | parts | CLAUDE.md | 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49 |
| harness | output | .agents/mechanisms/harness/harness.md | b13d2619614cf9504c40684693d96640db97d40e62282865434ba7b914447aaa |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| harness | output | .agents/skills/harness/MEETING.md | cd39fb09797ee49597872ef0aca3565f8e8913d810611d8649e79fd6dc8969e5 |
| harness | output | .agents/skills/harness/SKILL.md | 577f0ca35f276f53e52f16ec19d47a6e440275221dec007d7c90c169e55b9e86 |
| harness | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| harness | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| maintain | parts | .agents/mechanisms/maintain/maintain.rules.md | 39c39f68154156cf7025f1e908f9b4375899ec5840891fda742ff5e4b62f3c64 |
| maintain | parts | .agents/scripts/gw/maintain.py | 08ecf2ff91fd8edfa6206f844a1c557a704155854d6d1e11e1651bf4cdc9c4c2 |
| maintain | parts | .agents/scripts/gw/straw_dogs.py | ce01cdbd5162766129d2b56c1815a3a054ded5167cbce6ba7f47437f22657925 |
| maintain | parts | .agents/scripts/gw/test/test_maintain.py | a34b5adf687dee072fd58a397901d7bfea2029f8c43f7a20d5c8c82aae01765e |
| maintain | parts | .agents/scripts/gw/test/test_straw_dogs.py | d6f39f4245ffff85c0158dbb0202e0338b42238153adcbe33cecb2774b7ac697 |
| maintain | parts | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | parts | .agents/skills/maintain/SKILL.md | 337ed56ddf5d4fc9f857e78c31819ee0b36ef39533ea8eab008436abce479fff |
| maintain | output | .agents/mechanisms/maintain/maintain.md | b251954cdce7982867b3eaf7ce48b7ec4595244db159e2b55f16495984517cc7 |
| maintain | output | .agents/mechanisms/maintain/maintain.rules.md | 39c39f68154156cf7025f1e908f9b4375899ec5840891fda742ff5e4b62f3c64 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| maintain | output | .agents/skills/maintain/MARKS-FORMAT.md | a3fded4eeb74b7670550fbb7df7e95f5c4ad4b89caeb854cd0bf145188ffe2b7 |
| maintain | output | .agents/skills/maintain/SKILL.md | 337ed56ddf5d4fc9f857e78c31819ee0b36ef39533ea8eab008436abce479fff |
| maintain | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| maintain | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| mechanism-shape | parts | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| mechanism-shape | parts | .agents/scripts/gw/amendment.py | 5ec686ae72fe17982ea04f78b75fa24d9e22f37c53f12fa2d0a9baf2b0186c34 |
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | 901f6fe3db9f3c53013193de5696789ee05b62e5ca90240109f30681812d152e |
| mechanism-shape | parts | .agents/scripts/gw/hook.sh | f34bda41f6ab5acb26fb0860f8507b79b9523cf2bc68e4085e500c840ca1ff40 |
| mechanism-shape | parts | .agents/scripts/gw/inject_rules.py | 69eb78d7621e4dbad96d47951caf7630f3f9ce8b5de4ed6bf71342eba9fe25a9 |
| mechanism-shape | parts | .agents/scripts/gw/mechanisms.py | 9282add2f1f8d312336255b19aa9a492d8968c45dd1fe837047d04362285facd |
| mechanism-shape | parts | .agents/scripts/gw/test/repository.py | 55db9dc32101c52e2e9a57581a514a15548273c9895ea229d768bd291ae008b9 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_amendment.py | 2633d978ba8ceee67b0590e050cfaaf7025fb3d792198a88e9cca69f351688fb |
| mechanism-shape | parts | .agents/scripts/gw/test/test_inject_rules.py | 2218140956b646bbaaccf147cb1ab5bdc80ce4adc5243e3451141eaec3774d23 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_mechanisms.py | 9da777b9f4f018360a8e815838aeff2db414cffd490ec069794c1ce375e3cf31 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_repository.py | 61c008b612db93199ef86349eb3a9931479c3c33de1724365f90b293593d0e69 |
| mechanism-shape | parts | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| mechanism-shape | parts | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| mechanism-shape | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| mechanism-shape | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| product | parts | .agents/mechanisms/product/product.rules.md | 05f71cc357a3c753f038e5920edf6bc6a59d3f39b8f9a61628a29cd03c0a0bac |
| product | parts | .agents/scripts/gw/product.py | 76ffe2f70f77f4bb4ab2cbb4c48f4a93bba69ab3441542ae18972f52d0e1743d |
| product | parts | .agents/scripts/gw/test/test_product.py | 042847244df16ba86b1f899563aab8b8c86a012557804f400721d0ad0600da64 |
| product | parts | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | parts | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | parts | .agents/skills/product/SKILL.md | 62fffd510c4a5cbe6e3bfa21ce4663404176b735af067cc9ee522797d168d87e |
| product | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| product | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| product | output | .agents/mechanisms/product/product.md | 3f626fd40a7c0465bb2f31b8fa2378c42ee6991970fb06ba29e4c577b0ec9634 |
| product | output | .agents/mechanisms/product/product.rules.md | 05f71cc357a3c753f038e5920edf6bc6a59d3f39b8f9a61628a29cd03c0a0bac |
| product | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| product | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| product | output | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | output | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | output | .agents/skills/product/SKILL.md | 62fffd510c4a5cbe6e3bfa21ce4663404176b735af067cc9ee522797d168d87e |
| questions | parts | .agents/.gitattributes | bd95d1f719ab960c7d638d202a762ab72f356be5be7270623165327a47e28149 |
| questions | parts | .agents/mechanisms/questions/questions.rules.md | fee40909d8085fdd4af888c3cd15e70259d238493e1c4cb5abc94a7fd61365c3 |
| questions | parts | .agents/scripts/gw/questions.py | 6fba8dfac7919a506277cbafc3101b20178d1cbe9feb19f1006514a08ba2a456 |
| questions | parts | .agents/scripts/gw/test/test_questions.py | 95f925b8e6d85dcc4796e0b8cb87a9555b45d48796ef3fc008cc5a713404fcf2 |
| questions | parts | .agents/skills/questions/QUESTION-FORMAT.md | 3e802403c52515aa953a60f2c062960c25972d8c4b96fecf27a5b5d488aa1f32 |
| questions | parts | .agents/skills/questions/SKILL.md | 6b8e5dc63a13976743962daaf9978094bf3eac167b80cdbb99972e526c8959ae |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| questions | output | .agents/mechanisms/questions/questions.md | 328270ea9e868a30031ce2512aa59a5b9767a90280cfcf64af7fa17a097acfdb |
| questions | output | .agents/mechanisms/questions/questions.rules.md | fee40909d8085fdd4af888c3cd15e70259d238493e1c4cb5abc94a7fd61365c3 |
| questions | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| questions | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| questions | output | .agents/skills/questions/QUESTION-FORMAT.md | 3e802403c52515aa953a60f2c062960c25972d8c4b96fecf27a5b5d488aa1f32 |
| questions | output | .agents/skills/questions/SKILL.md | 6b8e5dc63a13976743962daaf9978094bf3eac167b80cdbb99972e526c8959ae |
| questions | output | .agents/skills/questions/STORE-ARRIVAL.md | 705104bc52573cb61face69019835b073c9fd6841c54d157108b6c0f6ef4ef77 |
| questions | output | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | output | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | output | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| session | parts | .agents/mechanisms/session/session.rules.md | f6773f90fffdb0bf9597f9fcd95056ec52327c2820661edac09c316c48360788 |
| session | parts | .agents/scripts/gw/sessions.py | f69bdbe7c9856c97e498ad877511f15a407ccc17ff67da19b4f731144fce93c0 |
| session | parts | .agents/scripts/gw/test/test_sessions.py | d54de65ab04deebd7f0348aec28ca0a0f3d149e25634408e2dc648aa81fdf838 |
| session | parts | .agents/skills/conclude/SKILL.md | e801f3c2ae53d862cbd3095fac77cd2eacc391847d4c138a13d207c3598ebb87 |
| session | parts | .agents/skills/recall/SKILL.md | 8e2eff562a9e96fa04a2a2012c3125aee7eee0fc813492b864f97c3aa1a2e6a2 |
| session | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| session | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| session | output | .agents/mechanisms/session/session.md | 57b2f96144382c9daa0a974492d7c532bfec8b0d9793fad85c364064f8e92c0f |
| session | output | .agents/mechanisms/session/session.rules.md | f6773f90fffdb0bf9597f9fcd95056ec52327c2820661edac09c316c48360788 |
| session | output | .agents/skills/conclude/SKILL.md | e801f3c2ae53d862cbd3095fac77cd2eacc391847d4c138a13d207c3598ebb87 |
| session | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| session | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| session | output | .agents/skills/recall/SKILL.md | 8e2eff562a9e96fa04a2a2012c3125aee7eee0fc813492b864f97c3aa1a2e6a2 |
| ticket | parts | .agents/mechanisms/ticket/ticket.rules.md | aacf8a3087cd7dd9e59ba2b9f6114c3d872662ee8f17ccc57ba5ef72b8d4726d |
| ticket | parts | .agents/scripts/gw/move_doc.py | 70330d82830e74a99616bc00c6dff891dce20a23cd590608d24b4da7a823d519 |
| ticket | parts | .agents/scripts/gw/test/test_citations.py | dbde70f3d00e122d5dcceda2fd5ad8c9cbe89ed98952cc44fe4f7778c67a8d4a |
| ticket | parts | .agents/scripts/gw/test/test_command_line.py | 09262b462449c13ca79a219ecd761cceeb880c8e5dd4dad3bfe0607b7f26bfca |
| ticket | parts | .agents/scripts/gw/test/test_failure_contract.py | c73da45c2072070446c9564617a20e009a75d709d490522fad1af909e12aa581 |
| ticket | parts | .agents/scripts/gw/test/test_paired_close.py | 92d8d5053f1a0538be598100133e00705ae10d783853373610a0acfa39f22945 |
| ticket | parts | .agents/scripts/gw/test/test_refusals.py | 4e4d4b918efe307d36b3489724539cc70edfe20c10e12e0a927425c7cab1970e |
| ticket | parts | .agents/scripts/gw/test/test_tickets.py | 9a539859256f1c41df83ea9543b9106c2b4c57a7124403dfa18cafb2b755d03b |
| ticket | parts | .agents/scripts/gw/tickets.py | b68c4522ebb921d67388eb916eea5ecc160955cbbf2704a25df4d06082f0ce19 |
| ticket | parts | .agents/skills/ticket/SKILL.md | 4673c642721f176a3b2660869157564437ab758392340169c432ea9a7d22c23a |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | d6550c59d73a17cc28325b0212150b75cdf0ea20cd60502f7a3dca23350161c6 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | c5209fccca05ffce05cafa47a8627bb3f1b6e10e9061ed50ef6ffbd7b3663948 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 2a3f7d03dae1802dec73f41662155262fabacf6938a11a5d407e7d4aadf7a0ac |
| ticket | output | .agents/mechanisms/ticket/ticket.md | 8037bfb1d01cc2a50e3592df3df6d83f52b62611ca926474ad2d8d40b2b5b97b |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | aacf8a3087cd7dd9e59ba2b9f6114c3d872662ee8f17ccc57ba5ef72b8d4726d |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | 889c83499e5618cf0f3110e8ac29eefb83cd5707eff3e284f8f12d3adcf4a5be |
| ticket | output | .agents/skills/mechanism/SKILL.md | da071bc4930a5a37b972b3a46ac9ca82d005d587207e9d18bdd4b4a5dba660bd |
| ticket | output | .agents/skills/ticket/SKILL.md | 4673c642721f176a3b2660869157564437ab758392340169c432ea9a7d22c23a |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | d6550c59d73a17cc28325b0212150b75cdf0ea20cd60502f7a3dca23350161c6 |
