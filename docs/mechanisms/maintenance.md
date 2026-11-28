# Maintenance marks

One row per mechanism per level, then each file that level was checked against, written by
`maintain.py --mark` when a maintenance finishes; the format is `/maintain`'s, in
`.agents/skills/maintain/MARKS-FORMAT.md`.

| mechanism | level | fingerprint | date | outcome |
|---|---|---|---|---|
| debugging | parts | f4d31bdcfe36e9126fdd4f746a5bc1b086b48b2069aa2aaca577b8e553886b8e | 2026-10-26 | nothing to change |
| debugging | output | f2e71219bb7f33bff5e31b3f16ec82d43735273db5cc5f2b2569616bcf5c5c9e | 2026-11-28 | nothing to change |
| delivery | parts | 5e85cb4d207b4c30a2c2cf8acaf90552e052a1084c2b8512dbfd82f1efb456d8 | 2026-11-17 | nothing to change |
| delivery | output | 35699a6086ab3ebe7cab5b374390b61bf7ceb13754fd5ac1330d2940f70ab3ac | 2026-11-28 | nothing to change |
| edge | parts | ebc684c056331f9edd1a57424764976f936b9d3d788bb3ec3d198514e35267dd | 2026-11-28 | nothing to change |
| edge | output | 163cede05cd142533475c07a3879b15bf846ad66c81eb4b61f1e2b41eb9e036c | 2026-11-28 | nothing to change |
| harness | parts | 7eba0d1bc980af4d2ddf0491ae4a0eef1b1f5b453d61f89e9d1d9543d1f86c5a | 2026-11-23 | nothing to change |
| harness | output | 00c31c9a56a1308820aed5814dc73d9404357dd788b57b87ffae13fb6d73d2d1 | 2026-11-24 | amended |
| maintain | parts | 05fa287341ca7978e7314f012aaae900f9523a1a0707c3b5f919de3dde4cbe1a | 2026-11-23 | nothing to change |
| maintain | output | 5531118ce1da68f6dcc2caa45d686a4c023fc8c53edbe146766f3c5378e7f16d | 2026-11-28 | nothing to change |
| mechanism-shape | parts | 9e79cfbba772d4528ce9e97c13e1caa5d1e1dc35d30a2620dd89531951c69f6c | 2026-11-25 | amended |
| mechanism-shape | output | e9d22f7fed3b7059a37a29c52108eaa7859c94f87008643c835608083a1957b6 | 2026-11-25 | nothing to change |
| pathfinder | parts | 240381740bbc577d543b5f4bf3e27b4d5e6ff7dde7795e662d9a6e9fb8e3bfdf | 2026-11-28 | nothing to change |
| pathfinder | output | 30eeb9a9bcef919908726070c99a9e7104bbd86137ab9ea529c01ac0e5a1da92 | 2026-11-28 | nothing to change |
| practice | parts | 530b2cd6d095be7554f7d5d5248f1f7fa29982679b3c8b73471a32ce54cf8522 | 2026-11-19 | nothing to change |
| practice | output | f5089c746bceefd9f55474b4a3078b138c86b332053096a06289b9b765de06f6 | 2026-11-28 | nothing to change |
| product | parts | 2b1fa5e8e20ef22d8645d06f94e6537373730fd431886e0e63004a5c6f5a1126 | 2026-11-16 | nothing to change |
| product | output | e3185fc427cc2dccfbed9455bcc273d41ab32e4746fb38e39d78e601e32bc7e3 | 2026-11-28 | nothing to change |
| questions | parts | 45c8bfaa5750132d18e696459c1aed43f1da27ab5acd59b90ecf7a6fbb0971ed | 2026-11-28 | amended |
| questions | output | 593d44ae408f77adf20a528ccaf017caba27cee543ba7d71f11a7195dd148156 | 2026-11-23 | nothing to change |
| session | parts | 6e7ea549dc83540da9b0296e4144fe5529dfd3b44702559a1285f0598b4d73bb | 2026-11-28 | amended |
| session | output | 2d5204d136071630d29df94dbf7358a542e1bd02e5732ed4bb8198268eab4b46 | 2026-11-25 | nothing to change |
| ticket | parts | bbb8bc4eedd486e5b6d4ca1bc94c9973e3339524a48760e068058e5257b12697 | 2026-11-28 | repaired |
| ticket | output | 5a60f69e1ecc89cfde0fac1a1099c33043673e863b50fc6f31b0e8bb49512fbb | 2026-11-24 | nothing to change |
| * | decisions | 421ac7a76e1a122a669ffcb0e2536bf5eb099f93 | 2026-11-28 | nothing to change |

| mechanism | level | file | fingerprint |
|---|---|---|---|
| debugging | parts | .agents/mechanisms/debugging/debugging.rules.md | 1276d40d429a505026183defde7246eef8894cfa9b55ea70d13e96dec9c99e7c |
| debugging | parts | .agents/skills/debugging/SKILL.md | aab980d308479cf3ad63959ad2f40a13306f290f9e5fa30e1b8894fb594d402a |
| debugging | output | .agents/mechanisms/debugging/debugging.md | ab6ea395d2b8e104beda08b4084e05cb16c12c23fe364ff328c919b001d25de7 |
| debugging | output | .agents/mechanisms/debugging/debugging.rules.md | 1276d40d429a505026183defde7246eef8894cfa9b55ea70d13e96dec9c99e7c |
| debugging | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 3b60c9739e9705f39e9929c4cfc79b102dca1ea6827a00d33928a0cae6d94cdd |
| debugging | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| debugging | output | .agents/skills/debugging/SKILL.md | aab980d308479cf3ad63959ad2f40a13306f290f9e5fa30e1b8894fb594d402a |
| debugging | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| debugging | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| delivery | parts | .agents/skills/implement/SKILL.md | f955100082f5a6ce89535e3a8b689b3a066d330db9227ea4151e572331949f3c |
| delivery | parts | .agents/skills/plan/SKILL.md | 432ba9f0621dfaa93b41440a873f5e623b43126dbcb978f33437ba2393333494 |
| delivery | parts | .agents/skills/verify/SKILL.md | c9dac24679cdb8e9d148360570af999333a3445ebf2a1086be5f5a76f5b71832 |
| delivery | output | .agents/mechanisms/delivery/delivery.md | beafaa6a7096c6ac988fe089c6f2cbe1187fc7ba04769c1b05cc088b5883be99 |
| delivery | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 3b60c9739e9705f39e9929c4cfc79b102dca1ea6827a00d33928a0cae6d94cdd |
| delivery | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| delivery | output | .agents/skills/implement/SKILL.md | f955100082f5a6ce89535e3a8b689b3a066d330db9227ea4151e572331949f3c |
| delivery | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| delivery | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| delivery | output | .agents/skills/plan/SKILL.md | 432ba9f0621dfaa93b41440a873f5e623b43126dbcb978f33437ba2393333494 |
| delivery | output | .agents/skills/verify/SKILL.md | c9dac24679cdb8e9d148360570af999333a3445ebf2a1086be5f5a76f5b71832 |
| edge | parts | .agents/mechanisms/edge/edge.rules.md | 59963f35ba6e27067f22082a704fab893f9ab6140333cb89f4d2c6480e135d19 |
| edge | parts | .agents/scripts/gw/edges.py | 5b80ae3a2313503103623bab2969670980fd83e647acd92c02394e23890b8f9b |
| edge | parts | .agents/scripts/gw/test/test_edges.py | 603ed723ea01d8a5929e8cd7d80011aa2725d1e827372cef8b2bf68653efc787 |
| edge | parts | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | parts | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/mechanisms/edge/edge.md | ba04f1ef332a963f081c3119ee580ca2b1cba278c5eca502524e70f2e945785e |
| edge | output | .agents/mechanisms/edge/edge.rules.md | 59963f35ba6e27067f22082a704fab893f9ab6140333cb89f4d2c6480e135d19 |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 3b60c9739e9705f39e9929c4cfc79b102dca1ea6827a00d33928a0cae6d94cdd |
| edge | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| edge | output | .agents/skills/edge/EDGE-FORMAT.md | a58e6acfc2cbc596e621ce1438054e78443b847ac9632167d7b987fa53016dd9 |
| edge | output | .agents/skills/edge/SKILL.md | 41465ccccefd8316a25191788d9207ec5e72c610fe668ec6c7ef1a9ef3f3034c |
| edge | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| edge | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| harness | parts | .agents/scripts/gw/entry_notice.py | f57c4d5fbd908cae9d01ac0b188abfd8be0b40632f06a75d845a5f294d7e5a34 |
| harness | parts | .agents/scripts/gw/harness.py | 68835bf76b31d49391452bb5a81714b72ea99fb8fc31b291222fe4b8588b5a75 |
| harness | parts | .agents/scripts/gw/test/test_entry_notice.py | 4a9f5e4ee3ae6aaba1576b4c9bcefffd60a540369726a4b403446b70daccb57d |
| harness | parts | .agents/scripts/gw/test/test_harness.py | 357706d260bfe8fc2a06e4f82ef777aec4ce24f81c10e5036a60bba8cc45554a |
| harness | parts | .agents/skills/harness/MEETING.md | 3fef853b2280dbe2583850f9ad9e3b4c2e663bc16070c932a45144f5636a33fc |
| harness | parts | .agents/skills/harness/SKILL.md | f6b4230a1f154d515b11619009e7eb9c44731e137e73fabae9bdc29db1719999 |
| harness | parts | AGENTS.md | 50b102e93a85a607a7595a6761d37f01464d620d13c7321bef1d6be36c6f9437 |
| harness | parts | CLAUDE.md | 336cc4fbf19beaada7ccf9986414fa91851a8d7a07dfb3ccbe800a69eed0ab49 |
| harness | output | .agents/mechanisms/harness/harness.md | 9cfcbf7e94a75d6ed6616eb37e988e85ff7879a8f95671f4fca040ba3e4445e9 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 8cbf8b1950f3990b6e84aef3c58248d34fb1a7effc2672eb237e224543f56eb3 |
| harness | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| harness | output | .agents/skills/harness/MEETING.md | 3fef853b2280dbe2583850f9ad9e3b4c2e663bc16070c932a45144f5636a33fc |
| harness | output | .agents/skills/harness/SKILL.md | f6b4230a1f154d515b11619009e7eb9c44731e137e73fabae9bdc29db1719999 |
| harness | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| harness | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| maintain | parts | .agents/mechanisms/maintain/maintain.rules.md | ea4b63ca08d32bb9d5cb493b41cb804082b1dc13046e52647af9c595fe5191d4 |
| maintain | parts | .agents/scripts/gw/maintain.py | d435893d6bf65fc4e474367b70de2b61b9cbc0ff11a38a33d0806c23feafcaf1 |
| maintain | parts | .agents/scripts/gw/straw_dogs.py | ce01cdbd5162766129d2b56c1815a3a054ded5167cbce6ba7f47437f22657925 |
| maintain | parts | .agents/scripts/gw/test/test_maintain.py | 861f0bd80c19777ad0cf1c838da8259688f6f2877f10574f7e62142ad65cf0dc |
| maintain | parts | .agents/scripts/gw/test/test_straw_dogs.py | d6f39f4245ffff85c0158dbb0202e0338b42238153adcbe33cecb2774b7ac697 |
| maintain | parts | .agents/skills/maintain/MARKS-FORMAT.md | c17c9a7ea7223bfec7e49b983ac666e9f4592fbfa4dcbf7b1210bc7cd24a4496 |
| maintain | parts | .agents/skills/maintain/SKILL.md | 597bc14fa8932c9ad0b4792f016a1fdbe8010415623fbdecdd70fefb9431e422 |
| maintain | output | .agents/mechanisms/maintain/maintain.md | 627ddca7710067db189095508de8c4f47c860791ac15dbbde853b615ef15eb85 |
| maintain | output | .agents/mechanisms/maintain/maintain.rules.md | ea4b63ca08d32bb9d5cb493b41cb804082b1dc13046e52647af9c595fe5191d4 |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 3b60c9739e9705f39e9929c4cfc79b102dca1ea6827a00d33928a0cae6d94cdd |
| maintain | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| maintain | output | .agents/skills/maintain/MARKS-FORMAT.md | c17c9a7ea7223bfec7e49b983ac666e9f4592fbfa4dcbf7b1210bc7cd24a4496 |
| maintain | output | .agents/skills/maintain/SKILL.md | 597bc14fa8932c9ad0b4792f016a1fdbe8010415623fbdecdd70fefb9431e422 |
| maintain | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| maintain | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| mechanism-shape | parts | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| mechanism-shape | parts | .agents/scripts/gw/amendment.py | 292ac2aff3fdfab55ffd112e0b74ad23ff9ad30e1d3ed0c4c41166dcdea5a607 |
| mechanism-shape | parts | .agents/scripts/gw/docs_corpus.py | 674b3360f04a556ad067f813ae1438d3d9597515f33c854557aabede72579ee5 |
| mechanism-shape | parts | .agents/scripts/gw/hook.sh | 5ee3472dddabd1b7697021b1bcbfca8e4b1d5964814123fc6970a1f6d0f822bb |
| mechanism-shape | parts | .agents/scripts/gw/inject_rules.py | aa70ae7c6e54e86ea0f2f1eb87613b63680876069ffb0f029bc03b9db34c3a7a |
| mechanism-shape | parts | .agents/scripts/gw/mechanisms.py | b774047deba21a24316d65c0e15df9d7111dd37e004e73d6f8edd37000e1212c |
| mechanism-shape | parts | .agents/scripts/gw/personal.py | a2b911215775b7567762a307789695ec111d3e40b00d7bcfb72bca22283f92bd |
| mechanism-shape | parts | .agents/scripts/gw/rule_failures.py | 7ead98b6202a4ce1ff95cede5a0a5eeec244db8651e7cabbe0a4b7a56a101d73 |
| mechanism-shape | parts | .agents/scripts/gw/test/repository.py | 30e2562f8075b0a47cc7b815866469f4aa3622ea2d78351a7816fedd823b993e |
| mechanism-shape | parts | .agents/scripts/gw/test/test_amendment.py | 2633d978ba8ceee67b0590e050cfaaf7025fb3d792198a88e9cca69f351688fb |
| mechanism-shape | parts | .agents/scripts/gw/test/test_inject_rules.py | c266446f42d2c61c086650a312e7a5abe922398f18a0fa2859c1ab311a92c1c5 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_mechanisms.py | 06b96d4c297a3403c8dda58bd8c7d2249edb4994d1c3a4fd9feca9c760a15003 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_personal.py | 714cb7b08d09dc4248030a131fd7d9695e5567edc787a3b942eb5a4e63ca070e |
| mechanism-shape | parts | .agents/scripts/gw/test/test_repository.py | 61c008b612db93199ef86349eb3a9931479c3c33de1724365f90b293593d0e69 |
| mechanism-shape | parts | .agents/scripts/gw/test/test_rule_failures.py | 227c4ba17ca6166bad8643be666d48c849416d59be9bf1f991470fa5cac1a01e |
| mechanism-shape | parts | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| mechanism-shape | parts | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 68e2e6d5e6bb21c05cba62f1422fcf0bb1942cacaccdb7659c92c91bb0a9a879 |
| mechanism-shape | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| mechanism-shape | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| mechanism-shape | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| pathfinder | parts | .agents/skills/pathfinder/BOARD.md | 5b26c0d16584414730b4c12a59794cce1fcfde5fde00b88765c7aca270e66857 |
| pathfinder | parts | .agents/skills/pathfinder/SKILL.md | c365bfefe4cc4420b7e78426a0b9193122262a5910cd0a1cd5c5e212f546ffdf |
| pathfinder | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 3b60c9739e9705f39e9929c4cfc79b102dca1ea6827a00d33928a0cae6d94cdd |
| pathfinder | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| pathfinder | output | .agents/mechanisms/pathfinder/pathfinder.md | 4a1e3967187de0526c72099232a1d9ca1abdc4da24cd1c9a02107f78906616f4 |
| pathfinder | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| pathfinder | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| pathfinder | output | .agents/skills/pathfinder/BOARD.md | 5b26c0d16584414730b4c12a59794cce1fcfde5fde00b88765c7aca270e66857 |
| pathfinder | output | .agents/skills/pathfinder/SKILL.md | c365bfefe4cc4420b7e78426a0b9193122262a5910cd0a1cd5c5e212f546ffdf |
| practice | parts | .agents/mechanisms/practice/practice.rules.md | 2c2f5e72ad0db2a012312ccfc4f821777d6f5b8db6333b6283aba42a1c1ceab3 |
| practice | parts | .agents/skills/improve-comments/SKILL.md | cfceab14d086898606baa4b3775d1b27e006f7c9c0afd32ad7ca8c67c2ed7194 |
| practice | parts | .agents/skills/tdd/SKILL.md | a62e8ddf6c9ff5fc2ea883418c9debaf435f00bb851e4918b4080a0711b75897 |
| practice | parts | .agents/skills/tdd/deep-modules.md | f2123700bf953db1740625686c75bdd145efd486357c47c6818c869fee657a32 |
| practice | parts | .agents/skills/tdd/interface-design.md | 764c5ff0e3fa6b4ab7095eb65ccc7201e090baf19fa16051dfdb72c06d27417d |
| practice | parts | .agents/skills/tdd/mocking.md | 3ceb807fdf4a47d6a93d4d9a891e5ba6d362a6247bd08adc451feebfc17361ef |
| practice | parts | .agents/skills/tdd/refactoring.md | 54fced22dd1911b7094c3fe7979b7c1a40d40be307482c4adf7dc0588f27d6cc |
| practice | parts | .agents/skills/tdd/tests.md | e12182f5c4c6a844b7c6ab4b8d2623b642aaaae5460fe58ed087efd4f3d5fb8a |
| practice | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 3b60c9739e9705f39e9929c4cfc79b102dca1ea6827a00d33928a0cae6d94cdd |
| practice | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| practice | output | .agents/mechanisms/practice/practice.md | 0008795e5ece201753925b49f362c61a00992084fcce37ff32c88571d611f8ec |
| practice | output | .agents/mechanisms/practice/practice.rules.md | 2c2f5e72ad0db2a012312ccfc4f821777d6f5b8db6333b6283aba42a1c1ceab3 |
| practice | output | .agents/skills/improve-comments/SKILL.md | cfceab14d086898606baa4b3775d1b27e006f7c9c0afd32ad7ca8c67c2ed7194 |
| practice | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| practice | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| practice | output | .agents/skills/tdd/SKILL.md | a62e8ddf6c9ff5fc2ea883418c9debaf435f00bb851e4918b4080a0711b75897 |
| practice | output | .agents/skills/tdd/deep-modules.md | f2123700bf953db1740625686c75bdd145efd486357c47c6818c869fee657a32 |
| practice | output | .agents/skills/tdd/interface-design.md | 764c5ff0e3fa6b4ab7095eb65ccc7201e090baf19fa16051dfdb72c06d27417d |
| practice | output | .agents/skills/tdd/mocking.md | 3ceb807fdf4a47d6a93d4d9a891e5ba6d362a6247bd08adc451feebfc17361ef |
| practice | output | .agents/skills/tdd/refactoring.md | 54fced22dd1911b7094c3fe7979b7c1a40d40be307482c4adf7dc0588f27d6cc |
| practice | output | .agents/skills/tdd/tests.md | e12182f5c4c6a844b7c6ab4b8d2623b642aaaae5460fe58ed087efd4f3d5fb8a |
| product | parts | .agents/mechanisms/product/product.rules.md | 05f71cc357a3c753f038e5920edf6bc6a59d3f39b8f9a61628a29cd03c0a0bac |
| product | parts | .agents/scripts/gw/product.py | f5adc3f9d552d52a98ebfd15e2c21dc8c3681f2bf8d8905e98ced134a92b65ab |
| product | parts | .agents/scripts/gw/test/test_product.py | 042847244df16ba86b1f899563aab8b8c86a012557804f400721d0ad0600da64 |
| product | parts | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | parts | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | parts | .agents/skills/product/SKILL.md | 62fffd510c4a5cbe6e3bfa21ce4663404176b735af067cc9ee522797d168d87e |
| product | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 3b60c9739e9705f39e9929c4cfc79b102dca1ea6827a00d33928a0cae6d94cdd |
| product | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| product | output | .agents/mechanisms/product/product.md | e1e3696c6f3723372bf98ada509e3870da89092ac09e60fba4b6bca53b3b6be9 |
| product | output | .agents/mechanisms/product/product.rules.md | 05f71cc357a3c753f038e5920edf6bc6a59d3f39b8f9a61628a29cd03c0a0bac |
| product | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| product | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| product | output | .agents/skills/product/PRODUCT-ARRIVAL.md | 640f700768657286a2f3e0617ab44919a05aef0339f059a92d5bd66fb324d205 |
| product | output | .agents/skills/product/PRODUCT-FORMAT.md | 0d1fb3937e4f005037b8fdac012af3bd6d21a4a18b4d5d700cb2f07cbbb09747 |
| product | output | .agents/skills/product/SKILL.md | 62fffd510c4a5cbe6e3bfa21ce4663404176b735af067cc9ee522797d168d87e |
| questions | parts | .agents/.gitattributes | bd95d1f719ab960c7d638d202a762ab72f356be5be7270623165327a47e28149 |
| questions | parts | .agents/mechanisms/questions/questions.rules.md | fb9aaf1a852a5e38d600620668fab518bb55fd32d175426000962507cc1df71e |
| questions | parts | .agents/scripts/gw/migrate_ids.py | e7339527196a47fabe32ee3b4f3f2ff135dba190f3c12100cb9f08ee1ebc5adf |
| questions | parts | .agents/scripts/gw/questions.py | afd487b2761a4031ae5e2e7876932269c1112b58f1f5b3402a5e8f0035ba24a5 |
| questions | parts | .agents/scripts/gw/test/test_migrate_ids.py | 24a6a5fb908cddf74d6b1f46f526b0eaeac56f8fd25fbde7f6354b5d4cd2aadb |
| questions | parts | .agents/scripts/gw/test/test_questions.py | 7260ae1b72add3b72f11a2a307f5f6a8dfa1d8a82b82b94353961c72323e4a8c |
| questions | parts | .agents/skills/questions/QUESTION-FORMAT.md | c48b06822f7dec62ecefa7a5a37be619a40e3a8a84c7aa1d363653d5e3a75f45 |
| questions | parts | .agents/skills/questions/SKILL.md | 37c77b8929ba8dc9216f33d28aa65bb57387d31a568f17471612ac1f4e00e982 |
| questions | parts | .agents/skills/questions/STORE-ARRIVAL.md | d5a88149eaffede34f1b7867f8b7e5c64b061466a6ee7f6938445e40bcd22e05 |
| questions | parts | .agents/skills/questions/hooks/.claude/settings.json | 7502eae6c772b16eef9d81a925f5fd2a26f4ac5d5562d64ba2fb5f4225318970 |
| questions | parts | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | parts | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 8f4a1761b1aa855b70c7afed438086784120e859096408a69bc4c923e2a558b0 |
| questions | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| questions | output | .agents/mechanisms/questions/questions.md | 38877b70fbea89d71f3b2b571a18af4401c5ebb98be879c7647e3f622776a9bb |
| questions | output | .agents/mechanisms/questions/questions.rules.md | 0eaf602d42593288d0f8a45cdb02850a6482aa4b59a4058460b8c62d754680a3 |
| questions | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| questions | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| questions | output | .agents/skills/questions/QUESTION-FORMAT.md | d07639b88b1418ec66a63a7c44ee12a36ca910b1ba375308a3e027c1244ee859 |
| questions | output | .agents/skills/questions/SKILL.md | 2c8d5405b3b964cb84e4b85737283a2e641bb8060262918130df5bbb67a15a9d |
| questions | output | .agents/skills/questions/STORE-ARRIVAL.md | d5a88149eaffede34f1b7867f8b7e5c64b061466a6ee7f6938445e40bcd22e05 |
| questions | output | .agents/skills/questions/hooks/.claude/settings.json | d05281c9c8b2fb88cf18fa45f11ac9ee146c8fc43cc2acba571891282f4dbce7 |
| questions | output | .agents/skills/questions/hooks/.codex/hooks.json | dee1313d892392fe04424e44608c4f5c7d44f608dbf80cc7822afa43b6f37ca4 |
| questions | output | .agents/skills/questions/hooks/.cursor/hooks.json | f26fb2ace2e616e7b5902c57a63489fde425ac411a5f54284f30bd67cbc99e6e |
| session | parts | .agents/mechanisms/session/session.rules.md | 15fafc6450d90dd43930ba2dbd54aadce350876957cd38d9653e0db4640de293 |
| session | parts | .agents/scripts/gw/pre_commit.sh | c57d57f185c4ae238c0eb6ab818164984b51d03caee4858d3ccad20bd2349870 |
| session | parts | .agents/scripts/gw/sessions.py | 98ed9e15dd6c5cc99c90b9360f6e21851fe44a0fdfae77ff34bc0cad8b76a694 |
| session | parts | .agents/scripts/gw/test/test_pre_commit.py | 8d699dc94a54694b8cf2562f4a844da94d8958ad63afa65ee0402b72492583f7 |
| session | parts | .agents/scripts/gw/test/test_sessions.py | a4578cf0214548eb07a8b80ade0b0855096bbbffa734e2585a49c6f19ba2ea5f |
| session | parts | .agents/skills/conclude/SKILL.md | 131a4619ec13e062819b6657d88da3d96b64560f020aeb06036909d2bd7f5fc7 |
| session | parts | .agents/skills/recall/MESSAGES.md | 0aff189661de95349b660b72d39519c14c7f417ac86192a7588cec1812859af7 |
| session | parts | .agents/skills/recall/SKILL.md | 43474a2d4d7f62d37392c096673c505f952ef69f62cf931fe870ad5af382951b |
| session | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 68e2e6d5e6bb21c05cba62f1422fcf0bb1942cacaccdb7659c92c91bb0a9a879 |
| session | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| session | output | .agents/mechanisms/session/session.md | ed1e655f3b8e3091b8c2ed345f61ef25a14eca4f31fe48390742483198ec1efb |
| session | output | .agents/mechanisms/session/session.rules.md | 15fafc6450d90dd43930ba2dbd54aadce350876957cd38d9653e0db4640de293 |
| session | output | .agents/skills/conclude/SKILL.md | 131a4619ec13e062819b6657d88da3d96b64560f020aeb06036909d2bd7f5fc7 |
| session | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| session | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| session | output | .agents/skills/recall/MESSAGES.md | 0aff189661de95349b660b72d39519c14c7f417ac86192a7588cec1812859af7 |
| session | output | .agents/skills/recall/SKILL.md | 43474a2d4d7f62d37392c096673c505f952ef69f62cf931fe870ad5af382951b |
| ticket | parts | .agents/mechanisms/ticket/ticket.rules.md | 928ca63fe552ebc0095879085ea899d20d6d14ac9ed7d5b37f3cb23db5380f09 |
| ticket | parts | .agents/scripts/gw/move_doc.py | 70330d82830e74a99616bc00c6dff891dce20a23cd590608d24b4da7a823d519 |
| ticket | parts | .agents/scripts/gw/test/test_citations.py | dbde70f3d00e122d5dcceda2fd5ad8c9cbe89ed98952cc44fe4f7778c67a8d4a |
| ticket | parts | .agents/scripts/gw/test/test_command_line.py | 09262b462449c13ca79a219ecd761cceeb880c8e5dd4dad3bfe0607b7f26bfca |
| ticket | parts | .agents/scripts/gw/test/test_failure_contract.py | c73da45c2072070446c9564617a20e009a75d709d490522fad1af909e12aa581 |
| ticket | parts | .agents/scripts/gw/test/test_paired_close.py | 92d8d5053f1a0538be598100133e00705ae10d783853373610a0acfa39f22945 |
| ticket | parts | .agents/scripts/gw/test/test_refusals.py | 4e4d4b918efe307d36b3489724539cc70edfe20c10e12e0a927425c7cab1970e |
| ticket | parts | .agents/scripts/gw/test/test_tickets.py | ab1f3c194b58e8aba35c81914a1b09b1697ff75d55d9967d32dfb46f0a68af22 |
| ticket | parts | .agents/scripts/gw/tickets.py | 06139b88d680d02aec3bc0dc02a77e76bc5a81e310c2e006f047118ce583a832 |
| ticket | parts | .agents/skills/ticket/SKILL.md | e40cf31fe0294d448c628b71b0e3de0635a7ba2822b56c97c0f7611d3047e0f4 |
| ticket | parts | .agents/skills/ticket/TICKET-FORMAT.md | d1c91b9de6d72d306459aee1cebb6e6198bfda49b375a282c40894a0bb28dfe6 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.md | 8cbf8b1950f3990b6e84aef3c58248d34fb1a7effc2672eb237e224543f56eb3 |
| ticket | output | .agents/mechanisms/mechanism-shape/mechanism-shape.rules.md | 265359d6d726005386c68cf36fc9a23558c6246cfa463582908ccece3eb5f7e9 |
| ticket | output | .agents/mechanisms/ticket/ticket.md | 0e70dcdb9a851246d643e20094d24d123ce2086f291b6e8bffe5a41ddd1b4276 |
| ticket | output | .agents/mechanisms/ticket/ticket.rules.md | 459397d32ba4ecba0bbc085da33a3c1c6319dfc281e340db64d0209add263cea |
| ticket | output | .agents/skills/mechanism/MECHANISM-FORMAT.md | fd234dae8e17cdd05aa9342c7b14ffbfc0d83549780df025e7196abae19d461a |
| ticket | output | .agents/skills/mechanism/SKILL.md | f68db94d5afa682f0c2a07ad03b20bd5f35becd9551dd5b3b3bbf5eeb76595bf |
| ticket | output | .agents/skills/ticket/SKILL.md | 150710526c0ff4ba32b5de6b522cd78a108cb9277519905aec0f6210b29c8777 |
| ticket | output | .agents/skills/ticket/TICKET-FORMAT.md | 5ee6d0df05252356106d8a6037bd96753525d1fce2b0a441d8dcc239c1efcf5c |
