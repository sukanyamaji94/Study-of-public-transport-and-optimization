# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:16:11 2020

@author: User
"""


# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:55:41 2020

@author: User
"""


import pulp as p

#create a Lp minimmization problem
Lp_prob = p.LpProblem('Problem',p.LpMinimize)
#create problem vaariables

x1	=	p.LpVariable("	x1	",lowBound=0, cat= 'Integer')
x2	=	p.LpVariable("	x2	",lowBound=0, cat= 'Integer')
x3	=	p.LpVariable("	x3	",lowBound=0, cat= 'Integer')
x4	=	p.LpVariable("	x4	",lowBound=0, cat= 'Integer')
x5	=	p.LpVariable("	x5	",lowBound=0, cat= 'Integer')
x6	=	p.LpVariable("	x6	",lowBound=0, cat= 'Integer')
x7	=	p.LpVariable("	x7	",lowBound=0, cat= 'Integer')
x8	=	p.LpVariable("	x8	",lowBound=0, cat= 'Integer')
x9	=	p.LpVariable("	x9	",lowBound=0, cat= 'Integer')
x10	=	p.LpVariable("	x10	",lowBound=0, cat= 'Integer')
x11	=	p.LpVariable("	x11	",lowBound=0, cat= 'Integer')
x12	=	p.LpVariable("	x12	",lowBound=0, cat= 'Integer')
x13	=	p.LpVariable("	x13	",lowBound=0, cat= 'Integer')
x14	=	p.LpVariable("	x14	",lowBound=0, cat= 'Integer')
x15	=	p.LpVariable("	x15	",lowBound=0, cat= 'Integer')
x16	=	p.LpVariable("	x16	",lowBound=0, cat= 'Integer')
x17	=	p.LpVariable("	x17	",lowBound=0, cat= 'Integer')
x18	=	p.LpVariable("	x18	",lowBound=0, cat= 'Integer')
x19	=	p.LpVariable("	x19	",lowBound=0, cat= 'Integer')
x20	=	p.LpVariable("	x20	",lowBound=0, cat= 'Integer')
x21	=	p.LpVariable("	x21	",lowBound=0, cat= 'Integer')
x22	=	p.LpVariable("	x22	",lowBound=0, cat= 'Integer')
x23	=	p.LpVariable("	x23	",lowBound=0, cat= 'Integer')
x24	=	p.LpVariable("	x24	",lowBound=0, cat= 'Integer')
x25	=	p.LpVariable("	x25	",lowBound=0, cat= 'Integer')
x26	=	p.LpVariable("	x26	",lowBound=0, cat= 'Integer')
x27	=	p.LpVariable("	x27	",lowBound=0, cat= 'Integer')
x28	=	p.LpVariable("	x28	",lowBound=0, cat= 'Integer')
x29	=	p.LpVariable("	x29	",lowBound=0, cat= 'Integer')
x30	=	p.LpVariable("	x30	",lowBound=0, cat= 'Integer')
x31	=	p.LpVariable("	x31	",lowBound=0, cat= 'Integer')
x32	=	p.LpVariable("	x32	",lowBound=0, cat= 'Integer')
x33	=	p.LpVariable("	x33	",lowBound=0, cat= 'Integer')
x34	=	p.LpVariable("	x34	",lowBound=0, cat= 'Integer')
x35	=	p.LpVariable("	x35	",lowBound=0, cat= 'Integer')
x36	=	p.LpVariable("	x36	",lowBound=0, cat= 'Integer')
x37	=	p.LpVariable("	x37	",lowBound=0, cat= 'Integer')
x38	=	p.LpVariable("	x38	",lowBound=0, cat= 'Integer')
x39	=	p.LpVariable("	x39	",lowBound=0, cat= 'Integer')
x40	=	p.LpVariable("	x40	",lowBound=0, cat= 'Integer')
x41	=	p.LpVariable("	x41	",lowBound=0, cat= 'Integer')
x42	=	p.LpVariable("	x42	",lowBound=0, cat= 'Integer')
x43	=	p.LpVariable("	x43	",lowBound=0, cat= 'Integer')
x44	=	p.LpVariable("	x44	",lowBound=0, cat= 'Integer')
x45	=	p.LpVariable("	x45	",lowBound=0, cat= 'Integer')
x46	=	p.LpVariable("	x46	",lowBound=0, cat= 'Integer')
x47	=	p.LpVariable("	x47	",lowBound=0, cat= 'Integer')
x48	=	p.LpVariable("	x48	",lowBound=0, cat= 'Integer')
x49	=	p.LpVariable("	x49	",lowBound=0, cat= 'Integer')
x50	=	p.LpVariable("	x50	",lowBound=0, cat= 'Integer')
x51	=	p.LpVariable("	x51	",lowBound=0, cat= 'Integer')
x52	=	p.LpVariable("	x52	",lowBound=0, cat= 'Integer')
x53	=	p.LpVariable("	x53	",lowBound=0, cat= 'Integer')
x54	=	p.LpVariable("	x54	",lowBound=0, cat= 'Integer')
x55	=	p.LpVariable("	x55	",lowBound=0, cat= 'Integer')
x56	=	p.LpVariable("	x56	",lowBound=0, cat= 'Integer')
x57	=	p.LpVariable("	x57	",lowBound=0, cat= 'Integer')
x58	=	p.LpVariable("	x58	",lowBound=0, cat= 'Integer')
x59	=	p.LpVariable("	x59	",lowBound=0, cat= 'Integer')
x60	=	p.LpVariable("	x60	",lowBound=0, cat= 'Integer')
x61	=	p.LpVariable("	x61	",lowBound=0, cat= 'Integer')
x62	=	p.LpVariable("	x62	",lowBound=0, cat= 'Integer')
x63	=	p.LpVariable("	x63	",lowBound=0, cat= 'Integer')
x64	=	p.LpVariable("	x64	",lowBound=0, cat= 'Integer')
x65	=	p.LpVariable("	x65	",lowBound=0, cat= 'Integer')
x66	=	p.LpVariable("	x66	",lowBound=0, cat= 'Integer')
x67	=	p.LpVariable("	x67	",lowBound=0, cat= 'Integer')
x68	=	p.LpVariable("	x68	",lowBound=0, cat= 'Integer')
x69	=	p.LpVariable("	x69	",lowBound=0, cat= 'Integer')
x70	=	p.LpVariable("	x70	",lowBound=0, cat= 'Integer')
x71	=	p.LpVariable("	x71	",lowBound=0, cat= 'Integer')
x72	=	p.LpVariable("	x72	",lowBound=0, cat= 'Integer')
x73	=	p.LpVariable("	x73	",lowBound=0, cat= 'Integer')
x74	=	p.LpVariable("	x74	",lowBound=0, cat= 'Integer')
x75	=	p.LpVariable("	x75	",lowBound=0, cat= 'Integer')
x76	=	p.LpVariable("	x76	",lowBound=0, cat= 'Integer')
x77	=	p.LpVariable("	x77	",lowBound=0, cat= 'Integer')
x78	=	p.LpVariable("	x78	",lowBound=0, cat= 'Integer')
x79	=	p.LpVariable("	x79	",lowBound=0, cat= 'Integer')
x80	=	p.LpVariable("	x80	",lowBound=0, cat= 'Integer')
x81	=	p.LpVariable("	x81	",lowBound=0, cat= 'Integer')
x82	=	p.LpVariable("	x82	",lowBound=0, cat= 'Integer')
x83	=	p.LpVariable("	x83	",lowBound=0, cat= 'Integer')
x84	=	p.LpVariable("	x84	",lowBound=0, cat= 'Integer')
x85	=	p.LpVariable("	x85	",lowBound=0, cat= 'Integer')
x86	=	p.LpVariable("	x86	",lowBound=0, cat= 'Integer')
x87	=	p.LpVariable("	x87	",lowBound=0, cat= 'Integer')
x88	=	p.LpVariable("	x88	",lowBound=0, cat= 'Integer')
x89	=	p.LpVariable("	x89	",lowBound=0, cat= 'Integer')
x90	=	p.LpVariable("	x90	",lowBound=0, cat= 'Integer')
x91	=	p.LpVariable("	x91	",lowBound=0, cat= 'Integer')
x92	=	p.LpVariable("	x92	",lowBound=0, cat= 'Integer')
x93	=	p.LpVariable("	x93	",lowBound=0, cat= 'Integer')
x94	=	p.LpVariable("	x94	",lowBound=0, cat= 'Integer')
x95	=	p.LpVariable("	x95	",lowBound=0, cat= 'Integer')
x96	=	p.LpVariable("	x96	",lowBound=0, cat= 'Integer')
x97	=	p.LpVariable("	x97	",lowBound=0, cat= 'Integer')
x98	=	p.LpVariable("	x98	",lowBound=0, cat= 'Integer')
x99	=	p.LpVariable("	x99	",lowBound=0, cat= 'Integer')
x100	=	p.LpVariable("	x100	",lowBound=0, cat= 'Integer')
x101	=	p.LpVariable("	x101	",lowBound=0, cat= 'Integer')
x102	=	p.LpVariable("	x102	",lowBound=0, cat= 'Integer')
x103	=	p.LpVariable("	x103	",lowBound=0, cat= 'Integer')
x104	=	p.LpVariable("	x104	",lowBound=0, cat= 'Integer')
x105	=	p.LpVariable("	x105	",lowBound=0, cat= 'Integer')
x106	=	p.LpVariable("	x106	",lowBound=0, cat= 'Integer')
x107	=	p.LpVariable("	x107	",lowBound=0, cat= 'Integer')
x108	=	p.LpVariable("	x108	",lowBound=0, cat= 'Integer')
x109	=	p.LpVariable("	x109	",lowBound=0, cat= 'Integer')
x110	=	p.LpVariable("	x110	",lowBound=0, cat= 'Integer')
x111	=	p.LpVariable("	x111	",lowBound=0, cat= 'Integer')
x112	=	p.LpVariable("	x112	",lowBound=0, cat= 'Integer')
x113	=	p.LpVariable("	x113	",lowBound=0, cat= 'Integer')
x114	=	p.LpVariable("	x114	",lowBound=0, cat= 'Integer')
x115	=	p.LpVariable("	x115	",lowBound=0, cat= 'Integer')
x116	=	p.LpVariable("	x116	",lowBound=0, cat= 'Integer')
x117	=	p.LpVariable("	x117	",lowBound=0, cat= 'Integer')
x118	=	p.LpVariable("	x118	",lowBound=0, cat= 'Integer')
x119	=	p.LpVariable("	x119	",lowBound=0, cat= 'Integer')
x120	=	p.LpVariable("	x120	",lowBound=0, cat= 'Integer')
x121	=	p.LpVariable("	x121	",lowBound=0, cat= 'Integer')
x122	=	p.LpVariable("	x122	",lowBound=0, cat= 'Integer')
x123	=	p.LpVariable("	x123	",lowBound=0, cat= 'Integer')
x124	=	p.LpVariable("	x124	",lowBound=0, cat= 'Integer')
x125	=	p.LpVariable("	x125	",lowBound=0, cat= 'Integer')
x126	=	p.LpVariable("	x126	",lowBound=0, cat= 'Integer')
x127	=	p.LpVariable("	x127	",lowBound=0, cat= 'Integer')
x128	=	p.LpVariable("	x128	",lowBound=0, cat= 'Integer')
x129	=	p.LpVariable("	x129	",lowBound=0, cat= 'Integer')
x130	=	p.LpVariable("	x130	",lowBound=0, cat= 'Integer')
x131	=	p.LpVariable("	x131	",lowBound=0, cat= 'Integer')
x132	=	p.LpVariable("	x132	",lowBound=0, cat= 'Integer')
x133	=	p.LpVariable("	x133	",lowBound=0, cat= 'Integer')
x134	=	p.LpVariable("	x134	",lowBound=0, cat= 'Integer')
x135	=	p.LpVariable("	x135	",lowBound=0, cat= 'Integer')
x136	=	p.LpVariable("	x136	",lowBound=0, cat= 'Integer')
x137	=	p.LpVariable("	x137	",lowBound=0, cat= 'Integer')
x138	=	p.LpVariable("	x138	",lowBound=0, cat= 'Integer')
x139	=	p.LpVariable("	x139	",lowBound=0, cat= 'Integer')
x140	=	p.LpVariable("	x140	",lowBound=0, cat= 'Integer')
x141	=	p.LpVariable("	x141	",lowBound=0, cat= 'Integer')
x142	=	p.LpVariable("	x142	",lowBound=0, cat= 'Integer')
x143	=	p.LpVariable("	x143	",lowBound=0, cat= 'Integer')
x144	=	p.LpVariable("	x144	",lowBound=0, cat= 'Integer')
x145	=	p.LpVariable("	x145	",lowBound=0, cat= 'Integer')
x146	=	p.LpVariable("	x146	",lowBound=0, cat= 'Integer')
x147	=	p.LpVariable("	x147	",lowBound=0, cat= 'Integer')
x148	=	p.LpVariable("	x148	",lowBound=0, cat= 'Integer')
x149	=	p.LpVariable("	x149	",lowBound=0, cat= 'Integer')
x150	=	p.LpVariable("	x150	",lowBound=0, cat= 'Integer')
x151	=	p.LpVariable("	x151	",lowBound=0, cat= 'Integer')
x152	=	p.LpVariable("	x152	",lowBound=0, cat= 'Integer')
x153	=	p.LpVariable("	x153	",lowBound=0, cat= 'Integer')
x154	=	p.LpVariable("	x154	",lowBound=0, cat= 'Integer')
x155	=	p.LpVariable("	x155	",lowBound=0, cat= 'Integer')
x156	=	p.LpVariable("	x156	",lowBound=0, cat= 'Integer')
x157	=	p.LpVariable("	x157	",lowBound=0, cat= 'Integer')
x158	=	p.LpVariable("	x158	",lowBound=0, cat= 'Integer')
x159	=	p.LpVariable("	x159	",lowBound=0, cat= 'Integer')
x160	=	p.LpVariable("	x160	",lowBound=0, cat= 'Integer')
x161	=	p.LpVariable("	x161	",lowBound=0, cat= 'Integer')
x162	=	p.LpVariable("	x162	",lowBound=0, cat= 'Integer')
x163	=	p.LpVariable("	x163	",lowBound=0, cat= 'Integer')
x164	=	p.LpVariable("	x164	",lowBound=0, cat= 'Integer')
x165	=	p.LpVariable("	x165	",lowBound=0, cat= 'Integer')
x166	=	p.LpVariable("	x166	",lowBound=0, cat= 'Integer')
x167	=	p.LpVariable("	x167	",lowBound=0, cat= 'Integer')
x168	=	p.LpVariable("	x168	",lowBound=0, cat= 'Integer')
x169	=	p.LpVariable("	x169	",lowBound=0, cat= 'Integer')
x170	=	p.LpVariable("	x170	",lowBound=0, cat= 'Integer')
x171	=	p.LpVariable("	x171	",lowBound=0, cat= 'Integer')
x172	=	p.LpVariable("	x172	",lowBound=0, cat= 'Integer')
x173	=	p.LpVariable("	x173	",lowBound=0, cat= 'Integer')
x174	=	p.LpVariable("	x174	",lowBound=0, cat= 'Integer')
x175	=	p.LpVariable("	x175	",lowBound=0, cat= 'Integer')
x176	=	p.LpVariable("	x176	",lowBound=0, cat= 'Integer')
x177	=	p.LpVariable("	x177	",lowBound=0, cat= 'Integer')
x178	=	p.LpVariable("	x178	",lowBound=0, cat= 'Integer')
x179	=	p.LpVariable("	x179	",lowBound=0, cat= 'Integer')
x180	=	p.LpVariable("	x180	",lowBound=0, cat= 'Integer')
x181	=	p.LpVariable("	x181	",lowBound=0, cat= 'Integer')
x182	=	p.LpVariable("	x182	",lowBound=0, cat= 'Integer')
x183	=	p.LpVariable("	x183	",lowBound=0, cat= 'Integer')
x184	=	p.LpVariable("	x184	",lowBound=0, cat= 'Integer')
x185	=	p.LpVariable("	x185	",lowBound=0, cat= 'Integer')
x186	=	p.LpVariable("	x186	",lowBound=0, cat= 'Integer')
x187	=	p.LpVariable("	x187	",lowBound=0, cat= 'Integer')
x188	=	p.LpVariable("	x188	",lowBound=0, cat= 'Integer')
x189	=	p.LpVariable("	x189	",lowBound=0, cat= 'Integer')
x190	=	p.LpVariable("	x190	",lowBound=0, cat= 'Integer')
x191	=	p.LpVariable("	x191	",lowBound=0, cat= 'Integer')
x192	=	p.LpVariable("	x192	",lowBound=0, cat= 'Integer')
x193	=	p.LpVariable("	x193	",lowBound=0, cat= 'Integer')
x194	=	p.LpVariable("	x194	",lowBound=0, cat= 'Integer')
x195	=	p.LpVariable("	x195	",lowBound=0, cat= 'Integer')
x196	=	p.LpVariable("	x196	",lowBound=0, cat= 'Integer')
x197	=	p.LpVariable("	x197	",lowBound=0, cat= 'Integer')
x198	=	p.LpVariable("	x198	",lowBound=0, cat= 'Integer')
x199	=	p.LpVariable("	x199	",lowBound=0, cat= 'Integer')
x200	=	p.LpVariable("	x200	",lowBound=0, cat= 'Integer')
x201	=	p.LpVariable("	x201	",lowBound=0, cat= 'Integer')
x202	=	p.LpVariable("	x202	",lowBound=0, cat= 'Integer')
x203	=	p.LpVariable("	x203	",lowBound=0, cat= 'Integer')
x204	=	p.LpVariable("	x204	",lowBound=0, cat= 'Integer')
x205	=	p.LpVariable("	x205	",lowBound=0, cat= 'Integer')
x206	=	p.LpVariable("	x206	",lowBound=0, cat= 'Integer')
x207	=	p.LpVariable("	x207	",lowBound=0, cat= 'Integer')
x208	=	p.LpVariable("	x208	",lowBound=0, cat= 'Integer')
x209	=	p.LpVariable("	x209	",lowBound=0, cat= 'Integer')
x210	=	p.LpVariable("	x210	",lowBound=0, cat= 'Integer')
x211	=	p.LpVariable("	x211	",lowBound=0, cat= 'Integer')
x212	=	p.LpVariable("	x212	",lowBound=0, cat= 'Integer')
x213	=	p.LpVariable("	x213	",lowBound=0, cat= 'Integer')
x214	=	p.LpVariable("	x214	",lowBound=0, cat= 'Integer')
x215	=	p.LpVariable("	x215	",lowBound=0, cat= 'Integer')
x216	=	p.LpVariable("	x216	",lowBound=0, cat= 'Integer')
x217	=	p.LpVariable("	x217	",lowBound=0, cat= 'Integer')
x218	=	p.LpVariable("	x218	",lowBound=0, cat= 'Integer')
x219	=	p.LpVariable("	x219	",lowBound=0, cat= 'Integer')
x220	=	p.LpVariable("	x220	",lowBound=0, cat= 'Integer')
x221	=	p.LpVariable("	x221	",lowBound=0, cat= 'Integer')
x222	=	p.LpVariable("	x222	",lowBound=0, cat= 'Integer')
x223	=	p.LpVariable("	x223	",lowBound=0, cat= 'Integer')
x224	=	p.LpVariable("	x224	",lowBound=0, cat= 'Integer')
x225	=	p.LpVariable("	x225	",lowBound=0, cat= 'Integer')
x226	=	p.LpVariable("	x226	",lowBound=0, cat= 'Integer')
x227	=	p.LpVariable("	x227	",lowBound=0, cat= 'Integer')
x228	=	p.LpVariable("	x228	",lowBound=0, cat= 'Integer')
x229	=	p.LpVariable("	x229	",lowBound=0, cat= 'Integer')
x230	=	p.LpVariable("	x230	",lowBound=0, cat= 'Integer')
x231	=	p.LpVariable("	x231	",lowBound=0, cat= 'Integer')
x232	=	p.LpVariable("	x232	",lowBound=0, cat= 'Integer')
x233	=	p.LpVariable("	x233	",lowBound=0, cat= 'Integer')
x234	=	p.LpVariable("	x234	",lowBound=0, cat= 'Integer')
x235	=	p.LpVariable("	x235	",lowBound=0, cat= 'Integer')
x236	=	p.LpVariable("	x236	",lowBound=0, cat= 'Integer')
x237	=	p.LpVariable("	x237	",lowBound=0, cat= 'Integer')
x238	=	p.LpVariable("	x238	",lowBound=0, cat= 'Integer')
x239	=	p.LpVariable("	x239	",lowBound=0, cat= 'Integer')
x240	=	p.LpVariable("	x240	",lowBound=0, cat= 'Integer')
x241	=	p.LpVariable("	x241	",lowBound=0, cat= 'Integer')
x242	=	p.LpVariable("	x242	",lowBound=0, cat= 'Integer')
x243	=	p.LpVariable("	x243	",lowBound=0, cat= 'Integer')
x244	=	p.LpVariable("	x244	",lowBound=0, cat= 'Integer')
x245	=	p.LpVariable("	x245	",lowBound=0, cat= 'Integer')
x246	=	p.LpVariable("	x246	",lowBound=0, cat= 'Integer')
x247	=	p.LpVariable("	x247	",lowBound=0, cat= 'Integer')
x248	=	p.LpVariable("	x248	",lowBound=0, cat= 'Integer')
x249	=	p.LpVariable("	x249	",lowBound=0, cat= 'Integer')
x250	=	p.LpVariable("	x250	",lowBound=0, cat= 'Integer')
x251	=	p.LpVariable("	x251	",lowBound=0, cat= 'Integer')
x252	=	p.LpVariable("	x252	",lowBound=0, cat= 'Integer')
x253	=	p.LpVariable("	x253	",lowBound=0, cat= 'Integer')
x254	=	p.LpVariable("	x254	",lowBound=0, cat= 'Integer')
x255	=	p.LpVariable("	x255	",lowBound=0, cat= 'Integer')
x256	=	p.LpVariable("	x256	",lowBound=0, cat= 'Integer')
x257	=	p.LpVariable("	x257	",lowBound=0, cat= 'Integer')
x258	=	p.LpVariable("	x258	",lowBound=0, cat= 'Integer')
x259	=	p.LpVariable("	x259	",lowBound=0, cat= 'Integer')
x260	=	p.LpVariable("	x260	",lowBound=0, cat= 'Integer')
x261	=	p.LpVariable("	x261	",lowBound=0, cat= 'Integer')
x262	=	p.LpVariable("	x262	",lowBound=0, cat= 'Integer')
x263	=	p.LpVariable("	x263	",lowBound=0, cat= 'Integer')
x264	=	p.LpVariable("	x264	",lowBound=0, cat= 'Integer')
x265	=	p.LpVariable("	x265	",lowBound=0, cat= 'Integer')
x266	=	p.LpVariable("	x266	",lowBound=0, cat= 'Integer')
x267	=	p.LpVariable("	x267	",lowBound=0, cat= 'Integer')
x268	=	p.LpVariable("	x268	",lowBound=0, cat= 'Integer')
x269	=	p.LpVariable("	x269	",lowBound=0, cat= 'Integer')
x270	=	p.LpVariable("	x270	",lowBound=0, cat= 'Integer')
x271	=	p.LpVariable("	x271	",lowBound=0, cat= 'Integer')
x272	=	p.LpVariable("	x272	",lowBound=0, cat= 'Integer')
x273	=	p.LpVariable("	x273	",lowBound=0, cat= 'Integer')
x274	=	p.LpVariable("	x274	",lowBound=0, cat= 'Integer')
x275	=	p.LpVariable("	x275	",lowBound=0, cat= 'Integer')
x276	=	p.LpVariable("	x276	",lowBound=0, cat= 'Integer')
x277	=	p.LpVariable("	x277	",lowBound=0, cat= 'Integer')
x278	=	p.LpVariable("	x278	",lowBound=0, cat= 'Integer')
x279	=	p.LpVariable("	x279	",lowBound=0, cat= 'Integer')
x280	=	p.LpVariable("	x280	",lowBound=0, cat= 'Integer')
x281	=	p.LpVariable("	x281	",lowBound=0, cat= 'Integer')
x282	=	p.LpVariable("	x282	",lowBound=0, cat= 'Integer')
x283	=	p.LpVariable("	x283	",lowBound=0, cat= 'Integer')
x284	=	p.LpVariable("	x284	",lowBound=0, cat= 'Integer')
x285	=	p.LpVariable("	x285	",lowBound=0, cat= 'Integer')
x286	=	p.LpVariable("	x286	",lowBound=0, cat= 'Integer')
x287	=	p.LpVariable("	x287	",lowBound=0, cat= 'Integer')
x288	=	p.LpVariable("	x288	",lowBound=0, cat= 'Integer')
x289	=	p.LpVariable("	x289	",lowBound=0, cat= 'Integer')
x290	=	p.LpVariable("	x290	",lowBound=0, cat= 'Integer')
x291	=	p.LpVariable("	x291	",lowBound=0, cat= 'Integer')
x292	=	p.LpVariable("	x292	",lowBound=0, cat= 'Integer')
x293	=	p.LpVariable("	x293	",lowBound=0, cat= 'Integer')
x294	=	p.LpVariable("	x294	",lowBound=0, cat= 'Integer')
x295	=	p.LpVariable("	x295	",lowBound=0, cat= 'Integer')
x296	=	p.LpVariable("	x296	",lowBound=0, cat= 'Integer')
x297	=	p.LpVariable("	x297	",lowBound=0, cat= 'Integer')
x298	=	p.LpVariable("	x298	",lowBound=0, cat= 'Integer')
x299	=	p.LpVariable("	x299	",lowBound=0, cat= 'Integer')
x300	=	p.LpVariable("	x300	",lowBound=0, cat= 'Integer')
x301	=	p.LpVariable("	x301	",lowBound=0, cat= 'Integer')
x302	=	p.LpVariable("	x302	",lowBound=0, cat= 'Integer')
x303	=	p.LpVariable("	x303	",lowBound=0, cat= 'Integer')
x304	=	p.LpVariable("	x304	",lowBound=0, cat= 'Integer')
x305	=	p.LpVariable("	x305	",lowBound=0, cat= 'Integer')
x306	=	p.LpVariable("	x306	",lowBound=0, cat= 'Integer')
x307	=	p.LpVariable("	x307	",lowBound=0, cat= 'Integer')
x308	=	p.LpVariable("	x308	",lowBound=0, cat= 'Integer')
x309	=	p.LpVariable("	x309	",lowBound=0, cat= 'Integer')
x310	=	p.LpVariable("	x310	",lowBound=0, cat= 'Integer')
x311	=	p.LpVariable("	x311	",lowBound=0, cat= 'Integer')
x312	=	p.LpVariable("	x312	",lowBound=0, cat= 'Integer')
x313	=	p.LpVariable("	x313	",lowBound=0, cat= 'Integer')
x314	=	p.LpVariable("	x314	",lowBound=0, cat= 'Integer')
x315	=	p.LpVariable("	x315	",lowBound=0, cat= 'Integer')
x316	=	p.LpVariable("	x316	",lowBound=0, cat= 'Integer')
x317	=	p.LpVariable("	x317	",lowBound=0, cat= 'Integer')
x318	=	p.LpVariable("	x318	",lowBound=0, cat= 'Integer')
x319	=	p.LpVariable("	x319	",lowBound=0, cat= 'Integer')
x320	=	p.LpVariable("	x320	",lowBound=0, cat= 'Integer')
x321	=	p.LpVariable("	x321	",lowBound=0, cat= 'Integer')
x322	=	p.LpVariable("	x322	",lowBound=0, cat= 'Integer')
x323	=	p.LpVariable("	x323	",lowBound=0, cat= 'Integer')
x324	=	p.LpVariable("	x324	",lowBound=0, cat= 'Integer')
x325	=	p.LpVariable("	x325	",lowBound=0, cat= 'Integer')
x326	=	p.LpVariable("	x326	",lowBound=0, cat= 'Integer')
x327	=	p.LpVariable("	x327	",lowBound=0, cat= 'Integer')
x328	=	p.LpVariable("	x328	",lowBound=0, cat= 'Integer')
x329	=	p.LpVariable("	x329	",lowBound=0, cat= 'Integer')
x330	=	p.LpVariable("	x330	",lowBound=0, cat= 'Integer')
x331	=	p.LpVariable("	x331	",lowBound=0, cat= 'Integer')
x332	=	p.LpVariable("	x332	",lowBound=0, cat= 'Integer')
x333	=	p.LpVariable("	x333	",lowBound=0, cat= 'Integer')
x334	=	p.LpVariable("	x334	",lowBound=0, cat= 'Integer')
x335	=	p.LpVariable("	x335	",lowBound=0, cat= 'Integer')
x336	=	p.LpVariable("	x336	",lowBound=0, cat= 'Integer')
x337	=	p.LpVariable("	x337	",lowBound=0, cat= 'Integer')
x338	=	p.LpVariable("	x338	",lowBound=0, cat= 'Integer')
x339	=	p.LpVariable("	x339	",lowBound=0, cat= 'Integer')
x340	=	p.LpVariable("	x340	",lowBound=0, cat= 'Integer')
x341	=	p.LpVariable("	x341	",lowBound=0, cat= 'Integer')
x342	=	p.LpVariable("	x342	",lowBound=0, cat= 'Integer')
x343	=	p.LpVariable("	x343	",lowBound=0, cat= 'Integer')
x344	=	p.LpVariable("	x344	",lowBound=0, cat= 'Integer')
x345	=	p.LpVariable("	x345	",lowBound=0, cat= 'Integer')
x346	=	p.LpVariable("	x346	",lowBound=0, cat= 'Integer')
x347	=	p.LpVariable("	x347	",lowBound=0, cat= 'Integer')
x348	=	p.LpVariable("	x348	",lowBound=0, cat= 'Integer')
x349	=	p.LpVariable("	x349	",lowBound=0, cat= 'Integer')
x350	=	p.LpVariable("	x350	",lowBound=0, cat= 'Integer')
x351	=	p.LpVariable("	x351	",lowBound=0, cat= 'Integer')
x352	=	p.LpVariable("	x352	",lowBound=0, cat= 'Integer')
x353	=	p.LpVariable("	x353	",lowBound=0, cat= 'Integer')
x354	=	p.LpVariable("	x354	",lowBound=0, cat= 'Integer')
x355	=	p.LpVariable("	x355	",lowBound=0, cat= 'Integer')
x356	=	p.LpVariable("	x356	",lowBound=0, cat= 'Integer')
x357	=	p.LpVariable("	x357	",lowBound=0, cat= 'Integer')
x358	=	p.LpVariable("	x358	",lowBound=0, cat= 'Integer')
x359	=	p.LpVariable("	x359	",lowBound=0, cat= 'Integer')
x360	=	p.LpVariable("	x360	",lowBound=0, cat= 'Integer')
x361	=	p.LpVariable("	x361	",lowBound=0, cat= 'Integer')
x362	=	p.LpVariable("	x362	",lowBound=0, cat= 'Integer')
x363	=	p.LpVariable("	x363	",lowBound=0, cat= 'Integer')
x364	=	p.LpVariable("	x364	",lowBound=0, cat= 'Integer')
x365	=	p.LpVariable("	x365	",lowBound=0, cat= 'Integer')
x366	=	p.LpVariable("	x366	",lowBound=0, cat= 'Integer')
x367	=	p.LpVariable("	x367	",lowBound=0, cat= 'Integer')
x368	=	p.LpVariable("	x368	",lowBound=0, cat= 'Integer')
x369	=	p.LpVariable("	x369	",lowBound=0, cat= 'Integer')
x370	=	p.LpVariable("	x370	",lowBound=0, cat= 'Integer')
x371	=	p.LpVariable("	x371	",lowBound=0, cat= 'Integer')
x372	=	p.LpVariable("	x372	",lowBound=0, cat= 'Integer')
x373	=	p.LpVariable("	x373	",lowBound=0, cat= 'Integer')
x374	=	p.LpVariable("	x374	",lowBound=0, cat= 'Integer')
x375	=	p.LpVariable("	x375	",lowBound=0, cat= 'Integer')
x376	=	p.LpVariable("	x376	",lowBound=0, cat= 'Integer')
x377	=	p.LpVariable("	x377	",lowBound=0, cat= 'Integer')
x378	=	p.LpVariable("	x378	",lowBound=0, cat= 'Integer')
x379	=	p.LpVariable("	x379	",lowBound=0, cat= 'Integer')
x380	=	p.LpVariable("	x380	",lowBound=0, cat= 'Integer')
x381	=	p.LpVariable("	x381	",lowBound=0, cat= 'Integer')
x382	=	p.LpVariable("	x382	",lowBound=0, cat= 'Integer')
x383	=	p.LpVariable("	x383	",lowBound=0, cat= 'Integer')
x384	=	p.LpVariable("	x384	",lowBound=0, cat= 'Integer')
x385	=	p.LpVariable("	x385	",lowBound=0, cat= 'Integer')
x386	=	p.LpVariable("	x386	",lowBound=0, cat= 'Integer')
x387	=	p.LpVariable("	x387	",lowBound=0, cat= 'Integer')
x388	=	p.LpVariable("	x388	",lowBound=0, cat= 'Integer')
x389	=	p.LpVariable("	x389	",lowBound=0, cat= 'Integer')
x390	=	p.LpVariable("	x390	",lowBound=0, cat= 'Integer')
x391	=	p.LpVariable("	x391	",lowBound=0, cat= 'Integer')
x392	=	p.LpVariable("	x392	",lowBound=0, cat= 'Integer')
x393	=	p.LpVariable("	x393	",lowBound=0, cat= 'Integer')
x394	=	p.LpVariable("	x394	",lowBound=0, cat= 'Integer')
x395	=	p.LpVariable("	x395	",lowBound=0, cat= 'Integer')
x396	=	p.LpVariable("	x396	",lowBound=0, cat= 'Integer')
x397	=	p.LpVariable("	x397	",lowBound=0, cat= 'Integer')
x398	=	p.LpVariable("	x398	",lowBound=0, cat= 'Integer')
x399	=	p.LpVariable("	x399	",lowBound=0, cat= 'Integer')
x400	=	p.LpVariable("	x400	",lowBound=0, cat= 'Integer')
x401	=	p.LpVariable("	x401	",lowBound=0, cat= 'Integer')
x402	=	p.LpVariable("	x402	",lowBound=0, cat= 'Integer')
x403	=	p.LpVariable("	x403	",lowBound=0, cat= 'Integer')
x404	=	p.LpVariable("	x404	",lowBound=0, cat= 'Integer')
x405	=	p.LpVariable("	x405	",lowBound=0, cat= 'Integer')
x406	=	p.LpVariable("	x406	",lowBound=0, cat= 'Integer')
x407	=	p.LpVariable("	x407	",lowBound=0, cat= 'Integer')
x408	=	p.LpVariable("	x408	",lowBound=0, cat= 'Integer')
x409	=	p.LpVariable("	x409	",lowBound=0, cat= 'Integer')
x410	=	p.LpVariable("	x410	",lowBound=0, cat= 'Integer')
x411	=	p.LpVariable("	x411	",lowBound=0, cat= 'Integer')
x412	=	p.LpVariable("	x412	",lowBound=0, cat= 'Integer')
x413	=	p.LpVariable("	x413	",lowBound=0, cat= 'Integer')
x414	=	p.LpVariable("	x414	",lowBound=0, cat= 'Integer')
x415	=	p.LpVariable("	x415	",lowBound=0, cat= 'Integer')
x416	=	p.LpVariable("	x416	",lowBound=0, cat= 'Integer')
x417	=	p.LpVariable("	x417	",lowBound=0, cat= 'Integer')
x418	=	p.LpVariable("	x418	",lowBound=0, cat= 'Integer')
x419	=	p.LpVariable("	x419	",lowBound=0, cat= 'Integer')
x420	=	p.LpVariable("	x420	",lowBound=0, cat= 'Integer')
x421	=	p.LpVariable("	x421	",lowBound=0, cat= 'Integer')
x422	=	p.LpVariable("	x422	",lowBound=0, cat= 'Integer')
x423	=	p.LpVariable("	x423	",lowBound=0, cat= 'Integer')
x424	=	p.LpVariable("	x424	",lowBound=0, cat= 'Integer')
x425	=	p.LpVariable("	x425	",lowBound=0, cat= 'Integer')
x426	=	p.LpVariable("	x426	",lowBound=0, cat= 'Integer')
x427	=	p.LpVariable("	x427	",lowBound=0, cat= 'Integer')
x428	=	p.LpVariable("	x428	",lowBound=0, cat= 'Integer')
x429	=	p.LpVariable("	x429	",lowBound=0, cat= 'Integer')
x430	=	p.LpVariable("	x430	",lowBound=0, cat= 'Integer')
x431	=	p.LpVariable("	x431	",lowBound=0, cat= 'Integer')
x432	=	p.LpVariable("	x432	",lowBound=0, cat= 'Integer')
x433	=	p.LpVariable("	x433	",lowBound=0, cat= 'Integer')
x434	=	p.LpVariable("	x434	",lowBound=0, cat= 'Integer')
x435	=	p.LpVariable("	x435	",lowBound=0, cat= 'Integer')
x436	=	p.LpVariable("	x436	",lowBound=0, cat= 'Integer')
x437	=	p.LpVariable("	x437	",lowBound=0, cat= 'Integer')
x438	=	p.LpVariable("	x438	",lowBound=0, cat= 'Integer')
x439	=	p.LpVariable("	x439	",lowBound=0, cat= 'Integer')
x440	=	p.LpVariable("	x440	",lowBound=0, cat= 'Integer')
x441	=	p.LpVariable("	x441	",lowBound=0, cat= 'Integer')
x442	=	p.LpVariable("	x442	",lowBound=0, cat= 'Integer')
x443	=	p.LpVariable("	x443	",lowBound=0, cat= 'Integer')
x444	=	p.LpVariable("	x444	",lowBound=0, cat= 'Integer')
x445	=	p.LpVariable("	x445	",lowBound=0, cat= 'Integer')
x446	=	p.LpVariable("	x446	",lowBound=0, cat= 'Integer')
x447	=	p.LpVariable("	x447	",lowBound=0, cat= 'Integer')
x448	=	p.LpVariable("	x448	",lowBound=0, cat= 'Integer')
x449	=	p.LpVariable("	x449	",lowBound=0, cat= 'Integer')
x450	=	p.LpVariable("	x450	",lowBound=0, cat= 'Integer')
x451	=	p.LpVariable("	x451	",lowBound=0, cat= 'Integer')
x452	=	p.LpVariable("	x452	",lowBound=0, cat= 'Integer')
x453	=	p.LpVariable("	x453	",lowBound=0, cat= 'Integer')
x454	=	p.LpVariable("	x454	",lowBound=0, cat= 'Integer')
x455	=	p.LpVariable("	x455	",lowBound=0, cat= 'Integer')
x456	=	p.LpVariable("	x456	",lowBound=0, cat= 'Integer')
x457	=	p.LpVariable("	x457	",lowBound=0, cat= 'Integer')
x458	=	p.LpVariable("	x458	",lowBound=0, cat= 'Integer')
x459	=	p.LpVariable("	x459	",lowBound=0, cat= 'Integer')
x460	=	p.LpVariable("	x460	",lowBound=0, cat= 'Integer')
x461	=	p.LpVariable("	x461	",lowBound=0, cat= 'Integer')
x462	=	p.LpVariable("	x462	",lowBound=0, cat= 'Integer')
x463	=	p.LpVariable("	x463	",lowBound=0, cat= 'Integer')
x464	=	p.LpVariable("	x464	",lowBound=0, cat= 'Integer')
x465	=	p.LpVariable("	x465	",lowBound=0, cat= 'Integer')
x466	=	p.LpVariable("	x466	",lowBound=0, cat= 'Integer')
x467	=	p.LpVariable("	x467	",lowBound=0, cat= 'Integer')
x468	=	p.LpVariable("	x468	",lowBound=0, cat= 'Integer')
x469	=	p.LpVariable("	x469	",lowBound=0, cat= 'Integer')
x470	=	p.LpVariable("	x470	",lowBound=0, cat= 'Integer')
x471	=	p.LpVariable("	x471	",lowBound=0, cat= 'Integer')
x472	=	p.LpVariable("	x472	",lowBound=0, cat= 'Integer')
x473	=	p.LpVariable("	x473	",lowBound=0, cat= 'Integer')
x474	=	p.LpVariable("	x474	",lowBound=0, cat= 'Integer')
x475	=	p.LpVariable("	x475	",lowBound=0, cat= 'Integer')
x476	=	p.LpVariable("	x476	",lowBound=0, cat= 'Integer')
x477	=	p.LpVariable("	x477	",lowBound=0, cat= 'Integer')
x478	=	p.LpVariable("	x478	",lowBound=0, cat= 'Integer')
x479	=	p.LpVariable("	x479	",lowBound=0, cat= 'Integer')
x480	=	p.LpVariable("	x480	",lowBound=0, cat= 'Integer')
x481	=	p.LpVariable("	x481	",lowBound=0, cat= 'Integer')
x482	=	p.LpVariable("	x482	",lowBound=0, cat= 'Integer')
x483	=	p.LpVariable("	x483	",lowBound=0, cat= 'Integer')
x484	=	p.LpVariable("	x484	",lowBound=0, cat= 'Integer')
x485	=	p.LpVariable("	x485	",lowBound=0, cat= 'Integer')
x486	=	p.LpVariable("	x486	",lowBound=0, cat= 'Integer')
x487	=	p.LpVariable("	x487	",lowBound=0, cat= 'Integer')
x488	=	p.LpVariable("	x488	",lowBound=0, cat= 'Integer')
x489	=	p.LpVariable("	x489	",lowBound=0, cat= 'Integer')
x490	=	p.LpVariable("	x490	",lowBound=0, cat= 'Integer')
x491	=	p.LpVariable("	x491	",lowBound=0, cat= 'Integer')
x492	=	p.LpVariable("	x492	",lowBound=0, cat= 'Integer')
x493	=	p.LpVariable("	x493	",lowBound=0, cat= 'Integer')
x494	=	p.LpVariable("	x494	",lowBound=0, cat= 'Integer')
x495	=	p.LpVariable("	x495	",lowBound=0, cat= 'Integer')
x496	=	p.LpVariable("	x496	",lowBound=0, cat= 'Integer')
x497	=	p.LpVariable("	x497	",lowBound=0, cat= 'Integer')
x498	=	p.LpVariable("	x498	",lowBound=0, cat= 'Integer')
x499	=	p.LpVariable("	x499	",lowBound=0, cat= 'Integer')
x500	=	p.LpVariable("	x500	",lowBound=0, cat= 'Integer')
x501	=	p.LpVariable("	x501	",lowBound=0, cat= 'Integer')
x502	=	p.LpVariable("	x502	",lowBound=0, cat= 'Integer')
x503	=	p.LpVariable("	x503	",lowBound=0, cat= 'Integer')
x504	=	p.LpVariable("	x504	",lowBound=0, cat= 'Integer')
x505	=	p.LpVariable("	x505	",lowBound=0, cat= 'Integer')
x506	=	p.LpVariable("	x506	",lowBound=0, cat= 'Integer')
x507	=	p.LpVariable("	x507	",lowBound=0, cat= 'Integer')
x508	=	p.LpVariable("	x508	",lowBound=0, cat= 'Integer')
x509	=	p.LpVariable("	x509	",lowBound=0, cat= 'Integer')
x510	=	p.LpVariable("	x510	",lowBound=0, cat= 'Integer')
x511	=	p.LpVariable("	x511	",lowBound=0, cat= 'Integer')
x512	=	p.LpVariable("	x512	",lowBound=0, cat= 'Integer')
x513	=	p.LpVariable("	x513	",lowBound=0, cat= 'Integer')
x514	=	p.LpVariable("	x514	",lowBound=0, cat= 'Integer')
x515	=	p.LpVariable("	x515	",lowBound=0, cat= 'Integer')
x516	=	p.LpVariable("	x516	",lowBound=0, cat= 'Integer')
x517	=	p.LpVariable("	x517	",lowBound=0, cat= 'Integer')
x518	=	p.LpVariable("	x518	",lowBound=0, cat= 'Integer')
x519	=	p.LpVariable("	x519	",lowBound=0, cat= 'Integer')
x520	=	p.LpVariable("	x520	",lowBound=0, cat= 'Integer')
x521	=	p.LpVariable("	x521	",lowBound=0, cat= 'Integer')
x522	=	p.LpVariable("	x522	",lowBound=0, cat= 'Integer')
x523	=	p.LpVariable("	x523	",lowBound=0, cat= 'Integer')
x524	=	p.LpVariable("	x524	",lowBound=0, cat= 'Integer')
x525	=	p.LpVariable("	x525	",lowBound=0, cat= 'Integer')
x526	=	p.LpVariable("	x526	",lowBound=0, cat= 'Integer')
x527	=	p.LpVariable("	x527	",lowBound=0, cat= 'Integer')
x528	=	p.LpVariable("	x528	",lowBound=0, cat= 'Integer')
x529	=	p.LpVariable("	x529	",lowBound=0, cat= 'Integer')
x530	=	p.LpVariable("	x530	",lowBound=0, cat= 'Integer')
x531	=	p.LpVariable("	x531	",lowBound=0, cat= 'Integer')
x532	=	p.LpVariable("	x532	",lowBound=0, cat= 'Integer')
x533	=	p.LpVariable("	x533	",lowBound=0, cat= 'Integer')
x534	=	p.LpVariable("	x534	",lowBound=0, cat= 'Integer')
x535	=	p.LpVariable("	x535	",lowBound=0, cat= 'Integer')
x536	=	p.LpVariable("	x536	",lowBound=0, cat= 'Integer')
x537	=	p.LpVariable("	x537	",lowBound=0, cat= 'Integer')
x538	=	p.LpVariable("	x538	",lowBound=0, cat= 'Integer')
x539	=	p.LpVariable("	x539	",lowBound=0, cat= 'Integer')
x540	=	p.LpVariable("	x540	",lowBound=0, cat= 'Integer')
x541	=	p.LpVariable("	x541	",lowBound=0, cat= 'Integer')
x542	=	p.LpVariable("	x542	",lowBound=0, cat= 'Integer')
x543	=	p.LpVariable("	x543	",lowBound=0, cat= 'Integer')
x544	=	p.LpVariable("	x544	",lowBound=0, cat= 'Integer')
x545	=	p.LpVariable("	x545	",lowBound=0, cat= 'Integer')
x546	=	p.LpVariable("	x546	",lowBound=0, cat= 'Integer')
x547	=	p.LpVariable("	x547	",lowBound=0, cat= 'Integer')
x548	=	p.LpVariable("	x548	",lowBound=0, cat= 'Integer')
x549	=	p.LpVariable("	x549	",lowBound=0, cat= 'Integer')
x550	=	p.LpVariable("	x550	",lowBound=0, cat= 'Integer')
x551	=	p.LpVariable("	x551	",lowBound=0, cat= 'Integer')
x552	=	p.LpVariable("	x552	",lowBound=0, cat= 'Integer')
x553	=	p.LpVariable("	x553	",lowBound=0, cat= 'Integer')
x554	=	p.LpVariable("	x554	",lowBound=0, cat= 'Integer')
x555	=	p.LpVariable("	x555	",lowBound=0, cat= 'Integer')
x556	=	p.LpVariable("	x556	",lowBound=0, cat= 'Integer')
x557	=	p.LpVariable("	x557	",lowBound=0, cat= 'Integer')
x558	=	p.LpVariable("	x558	",lowBound=0, cat= 'Integer')
x559	=	p.LpVariable("	x559	",lowBound=0, cat= 'Integer')
x560	=	p.LpVariable("	x560	",lowBound=0, cat= 'Integer')
x561	=	p.LpVariable("	x561	",lowBound=0, cat= 'Integer')
x562	=	p.LpVariable("	x562	",lowBound=0, cat= 'Integer')
x563	=	p.LpVariable("	x563	",lowBound=0, cat= 'Integer')
x564	=	p.LpVariable("	x564	",lowBound=0, cat= 'Integer')
x565	=	p.LpVariable("	x565	",lowBound=0, cat= 'Integer')
x566	=	p.LpVariable("	x566	",lowBound=0, cat= 'Integer')
x567	=	p.LpVariable("	x567	",lowBound=0, cat= 'Integer')
x568	=	p.LpVariable("	x568	",lowBound=0, cat= 'Integer')
x569	=	p.LpVariable("	x569	",lowBound=0, cat= 'Integer')
x570	=	p.LpVariable("	x570	",lowBound=0, cat= 'Integer')
x571	=	p.LpVariable("	x571	",lowBound=0, cat= 'Integer')
x572	=	p.LpVariable("	x572	",lowBound=0, cat= 'Integer')
x573	=	p.LpVariable("	x573	",lowBound=0, cat= 'Integer')
x574	=	p.LpVariable("	x574	",lowBound=0, cat= 'Integer')
x575	=	p.LpVariable("	x575	",lowBound=0, cat= 'Integer')
x576	=	p.LpVariable("	x576	",lowBound=0, cat= 'Integer')
x577	=	p.LpVariable("	x577	",lowBound=0, cat= 'Integer')
x578	=	p.LpVariable("	x578	",lowBound=0, cat= 'Integer')
x579	=	p.LpVariable("	x579	",lowBound=0, cat= 'Integer')
x580	=	p.LpVariable("	x580	",lowBound=0, cat= 'Integer')
x581	=	p.LpVariable("	x581	",lowBound=0, cat= 'Integer')
x582	=	p.LpVariable("	x582	",lowBound=0, cat= 'Integer')
x583	=	p.LpVariable("	x583	",lowBound=0, cat= 'Integer')
x584	=	p.LpVariable("	x584	",lowBound=0, cat= 'Integer')
x585	=	p.LpVariable("	x585	",lowBound=0, cat= 'Integer')
x586	=	p.LpVariable("	x586	",lowBound=0, cat= 'Integer')
x587	=	p.LpVariable("	x587	",lowBound=0, cat= 'Integer')
x588	=	p.LpVariable("	x588	",lowBound=0, cat= 'Integer')
x589	=	p.LpVariable("	x589	",lowBound=0, cat= 'Integer')
x590	=	p.LpVariable("	x590	",lowBound=0, cat= 'Integer')
x591	=	p.LpVariable("	x591	",lowBound=0, cat= 'Integer')
x592	=	p.LpVariable("	x592	",lowBound=0, cat= 'Integer')
x593	=	p.LpVariable("	x593	",lowBound=0, cat= 'Integer')
x594	=	p.LpVariable("	x594	",lowBound=0, cat= 'Integer')
x595	=	p.LpVariable("	x595	",lowBound=0, cat= 'Integer')
x596	=	p.LpVariable("	x596	",lowBound=0, cat= 'Integer')
x597	=	p.LpVariable("	x597	",lowBound=0, cat= 'Integer')
x598	=	p.LpVariable("	x598	",lowBound=0, cat= 'Integer')
x599	=	p.LpVariable("	x599	",lowBound=0, cat= 'Integer')
x600	=	p.LpVariable("	x600	",lowBound=0, cat= 'Integer')
x601	=	p.LpVariable("	x601	",lowBound=0, cat= 'Integer')
x602	=	p.LpVariable("	x602	",lowBound=0, cat= 'Integer')
x603	=	p.LpVariable("	x603	",lowBound=0, cat= 'Integer')
x604	=	p.LpVariable("	x604	",lowBound=0, cat= 'Integer')
x605	=	p.LpVariable("	x605	",lowBound=0, cat= 'Integer')
x606	=	p.LpVariable("	x606	",lowBound=0, cat= 'Integer')
x607	=	p.LpVariable("	x607	",lowBound=0, cat= 'Integer')
x608	=	p.LpVariable("	x608	",lowBound=0, cat= 'Integer')
x609	=	p.LpVariable("	x609	",lowBound=0, cat= 'Integer')
x610	=	p.LpVariable("	x610	",lowBound=0, cat= 'Integer')
x611	=	p.LpVariable("	x611	",lowBound=0, cat= 'Integer')
x612	=	p.LpVariable("	x612	",lowBound=0, cat= 'Integer')
x613	=	p.LpVariable("	x613	",lowBound=0, cat= 'Integer')
x614	=	p.LpVariable("	x614	",lowBound=0, cat= 'Integer')
x615	=	p.LpVariable("	x615	",lowBound=0, cat= 'Integer')
x616	=	p.LpVariable("	x616	",lowBound=0, cat= 'Integer')
x617	=	p.LpVariable("	x617	",lowBound=0, cat= 'Integer')
x618	=	p.LpVariable("	x618	",lowBound=0, cat= 'Integer')
x619	=	p.LpVariable("	x619	",lowBound=0, cat= 'Integer')
x620	=	p.LpVariable("	x620	",lowBound=0, cat= 'Integer')
x621	=	p.LpVariable("	x621	",lowBound=0, cat= 'Integer')
x622	=	p.LpVariable("	x622	",lowBound=0, cat= 'Integer')
x623	=	p.LpVariable("	x623	",lowBound=0, cat= 'Integer')
x624	=	p.LpVariable("	x624	",lowBound=0, cat= 'Integer')
x625	=	p.LpVariable("	x625	",lowBound=0, cat= 'Integer')
x626	=	p.LpVariable("	x626	",lowBound=0, cat= 'Integer')
x627	=	p.LpVariable("	x627	",lowBound=0, cat= 'Integer')
x628	=	p.LpVariable("	x628	",lowBound=0, cat= 'Integer')
x629	=	p.LpVariable("	x629	",lowBound=0, cat= 'Integer')
x630	=	p.LpVariable("	x630	",lowBound=0, cat= 'Integer')
x631	=	p.LpVariable("	x631	",lowBound=0, cat= 'Integer')
x632	=	p.LpVariable("	x632	",lowBound=0, cat= 'Integer')
x633	=	p.LpVariable("	x633	",lowBound=0, cat= 'Integer')
x634	=	p.LpVariable("	x634	",lowBound=0, cat= 'Integer')
x635	=	p.LpVariable("	x635	",lowBound=0, cat= 'Integer')
x636	=	p.LpVariable("	x636	",lowBound=0, cat= 'Integer')
x637	=	p.LpVariable("	x637	",lowBound=0, cat= 'Integer')
x638	=	p.LpVariable("	x638	",lowBound=0, cat= 'Integer')
x639	=	p.LpVariable("	x639	",lowBound=0, cat= 'Integer')
x640	=	p.LpVariable("	x640	",lowBound=0, cat= 'Integer')
x641	=	p.LpVariable("	x641	",lowBound=0, cat= 'Integer')
x642	=	p.LpVariable("	x642	",lowBound=0, cat= 'Integer')
x643	=	p.LpVariable("	x643	",lowBound=0, cat= 'Integer')
x644	=	p.LpVariable("	x644	",lowBound=0, cat= 'Integer')
x645	=	p.LpVariable("	x645	",lowBound=0, cat= 'Integer')
x646	=	p.LpVariable("	x646	",lowBound=0, cat= 'Integer')
x647	=	p.LpVariable("	x647	",lowBound=0, cat= 'Integer')
x648	=	p.LpVariable("	x648	",lowBound=0, cat= 'Integer')
x649	=	p.LpVariable("	x649	",lowBound=0, cat= 'Integer')
x650	=	p.LpVariable("	x650	",lowBound=0, cat= 'Integer')
x651	=	p.LpVariable("	x651	",lowBound=0, cat= 'Integer')
x652	=	p.LpVariable("	x652	",lowBound=0, cat= 'Integer')
x653	=	p.LpVariable("	x653	",lowBound=0, cat= 'Integer')
x654	=	p.LpVariable("	x654	",lowBound=0, cat= 'Integer')
x655	=	p.LpVariable("	x655	",lowBound=0, cat= 'Integer')
x656	=	p.LpVariable("	x656	",lowBound=0, cat= 'Integer')
x657	=	p.LpVariable("	x657	",lowBound=0, cat= 'Integer')
x658	=	p.LpVariable("	x658	",lowBound=0, cat= 'Integer')
x659	=	p.LpVariable("	x659	",lowBound=0, cat= 'Integer')
x660	=	p.LpVariable("	x660	",lowBound=0, cat= 'Integer')
x661	=	p.LpVariable("	x661	",lowBound=0, cat= 'Integer')
x662	=	p.LpVariable("	x662	",lowBound=0, cat= 'Integer')
x663	=	p.LpVariable("	x663	",lowBound=0, cat= 'Integer')
x664	=	p.LpVariable("	x664	",lowBound=0, cat= 'Integer')
x665	=	p.LpVariable("	x665	",lowBound=0, cat= 'Integer')
x666	=	p.LpVariable("	x666	",lowBound=0, cat= 'Integer')
x667	=	p.LpVariable("	x667	",lowBound=0, cat= 'Integer')
x668	=	p.LpVariable("	x668	",lowBound=0, cat= 'Integer')
x669	=	p.LpVariable("	x669	",lowBound=0, cat= 'Integer')
x670	=	p.LpVariable("	x670	",lowBound=0, cat= 'Integer')
x671	=	p.LpVariable("	x671	",lowBound=0, cat= 'Integer')
x672	=	p.LpVariable("	x672	",lowBound=0, cat= 'Integer')
x673	=	p.LpVariable("	x673	",lowBound=0, cat= 'Integer')
x674	=	p.LpVariable("	x674	",lowBound=0, cat= 'Integer')
x675	=	p.LpVariable("	x675	",lowBound=0, cat= 'Integer')
x676	=	p.LpVariable("	x676	",lowBound=0, cat= 'Integer')
x677	=	p.LpVariable("	x677	",lowBound=0, cat= 'Integer')
x678	=	p.LpVariable("	x678	",lowBound=0, cat= 'Integer')
x679	=	p.LpVariable("	x679	",lowBound=0, cat= 'Integer')
x680	=	p.LpVariable("	x680	",lowBound=0, cat= 'Integer')
x681	=	p.LpVariable("	x681	",lowBound=0, cat= 'Integer')
x682	=	p.LpVariable("	x682	",lowBound=0, cat= 'Integer')
x683	=	p.LpVariable("	x683	",lowBound=0, cat= 'Integer')
x684	=	p.LpVariable("	x684	",lowBound=0, cat= 'Integer')
x685	=	p.LpVariable("	x685	",lowBound=0, cat= 'Integer')
x686	=	p.LpVariable("	x686	",lowBound=0, cat= 'Integer')
x687	=	p.LpVariable("	x687	",lowBound=0, cat= 'Integer')
x688	=	p.LpVariable("	x688	",lowBound=0, cat= 'Integer')
x689	=	p.LpVariable("	x689	",lowBound=0, cat= 'Integer')
x690	=	p.LpVariable("	x690	",lowBound=0, cat= 'Integer')
x691	=	p.LpVariable("	x691	",lowBound=0, cat= 'Integer')
x692	=	p.LpVariable("	x692	",lowBound=0, cat= 'Integer')
x693	=	p.LpVariable("	x693	",lowBound=0, cat= 'Integer')
x694	=	p.LpVariable("	x694	",lowBound=0, cat= 'Integer')
x695	=	p.LpVariable("	x695	",lowBound=0, cat= 'Integer')
x696	=	p.LpVariable("	x696	",lowBound=0, cat= 'Integer')
x697	=	p.LpVariable("	x697	",lowBound=0, cat= 'Integer')
x698	=	p.LpVariable("	x698	",lowBound=0, cat= 'Integer')
x699	=	p.LpVariable("	x699	",lowBound=0, cat= 'Integer')
x700	=	p.LpVariable("	x700	",lowBound=0, cat= 'Integer')
x701	=	p.LpVariable("	x701	",lowBound=0, cat= 'Integer')
x702	=	p.LpVariable("	x702	",lowBound=0, cat= 'Integer')
x703	=	p.LpVariable("	x703	",lowBound=0, cat= 'Integer')
x704	=	p.LpVariable("	x704	",lowBound=0, cat= 'Integer')
x705	=	p.LpVariable("	x705	",lowBound=0, cat= 'Integer')
x706	=	p.LpVariable("	x706	",lowBound=0, cat= 'Integer')
x707	=	p.LpVariable("	x707	",lowBound=0, cat= 'Integer')
x708	=	p.LpVariable("	x708	",lowBound=0, cat= 'Integer')
x709	=	p.LpVariable("	x709	",lowBound=0, cat= 'Integer')
x710	=	p.LpVariable("	x710	",lowBound=0, cat= 'Integer')
x711	=	p.LpVariable("	x711	",lowBound=0, cat= 'Integer')
x712	=	p.LpVariable("	x712	",lowBound=0, cat= 'Integer')
x713	=	p.LpVariable("	x713	",lowBound=0, cat= 'Integer')
x714	=	p.LpVariable("	x714	",lowBound=0, cat= 'Integer')
x715	=	p.LpVariable("	x715	",lowBound=0, cat= 'Integer')
x716	=	p.LpVariable("	x716	",lowBound=0, cat= 'Integer')
x717	=	p.LpVariable("	x717	",lowBound=0, cat= 'Integer')
x718	=	p.LpVariable("	x718	",lowBound=0, cat= 'Integer')
x719	=	p.LpVariable("	x719	",lowBound=0, cat= 'Integer')
x720	=	p.LpVariable("	x720	",lowBound=0, cat= 'Integer')
x721	=	p.LpVariable("	x721	",lowBound=0, cat= 'Integer')
x722	=	p.LpVariable("	x722	",lowBound=0, cat= 'Integer')
x723	=	p.LpVariable("	x723	",lowBound=0, cat= 'Integer')
x724	=	p.LpVariable("	x724	",lowBound=0, cat= 'Integer')
x725	=	p.LpVariable("	x725	",lowBound=0, cat= 'Integer')
x726	=	p.LpVariable("	x726	",lowBound=0, cat= 'Integer')
x727	=	p.LpVariable("	x727	",lowBound=0, cat= 'Integer')
x728	=	p.LpVariable("	x728	",lowBound=0, cat= 'Integer')
x729	=	p.LpVariable("	x729	",lowBound=0, cat= 'Integer')
x730	=	p.LpVariable("	x730	",lowBound=0, cat= 'Integer')
x731	=	p.LpVariable("	x731	",lowBound=0, cat= 'Integer')
x732	=	p.LpVariable("	x732	",lowBound=0, cat= 'Integer')
x733	=	p.LpVariable("	x733	",lowBound=0, cat= 'Integer')
x734	=	p.LpVariable("	x734	",lowBound=0, cat= 'Integer')
x735	=	p.LpVariable("	x735	",lowBound=0, cat= 'Integer')
x736	=	p.LpVariable("	x736	",lowBound=0, cat= 'Integer')
x737	=	p.LpVariable("	x737	",lowBound=0, cat= 'Integer')
x738	=	p.LpVariable("	x738	",lowBound=0, cat= 'Integer')
x739	=	p.LpVariable("	x739	",lowBound=0, cat= 'Integer')
x740	=	p.LpVariable("	x740	",lowBound=0, cat= 'Integer')
x741	=	p.LpVariable("	x741	",lowBound=0, cat= 'Integer')
x742	=	p.LpVariable("	x742	",lowBound=0, cat= 'Integer')
x743	=	p.LpVariable("	x743	",lowBound=0, cat= 'Integer')
x744	=	p.LpVariable("	x744	",lowBound=0, cat= 'Integer')
x745	=	p.LpVariable("	x745	",lowBound=0, cat= 'Integer')
x746	=	p.LpVariable("	x746	",lowBound=0, cat= 'Integer')
x747	=	p.LpVariable("	x747	",lowBound=0, cat= 'Integer')
x748	=	p.LpVariable("	x748	",lowBound=0, cat= 'Integer')
x749	=	p.LpVariable("	x749	",lowBound=0, cat= 'Integer')
x750	=	p.LpVariable("	x750	",lowBound=0, cat= 'Integer')
x751	=	p.LpVariable("	x751	",lowBound=0, cat= 'Integer')
x752	=	p.LpVariable("	x752	",lowBound=0, cat= 'Integer')
x753	=	p.LpVariable("	x753	",lowBound=0, cat= 'Integer')
x754	=	p.LpVariable("	x754	",lowBound=0, cat= 'Integer')
x755	=	p.LpVariable("	x755	",lowBound=0, cat= 'Integer')
x756	=	p.LpVariable("	x756	",lowBound=0, cat= 'Integer')
x757	=	p.LpVariable("	x757	",lowBound=0, cat= 'Integer')
x758	=	p.LpVariable("	x758	",lowBound=0, cat= 'Integer')
x759	=	p.LpVariable("	x759	",lowBound=0, cat= 'Integer')
x760	=	p.LpVariable("	x760	",lowBound=0, cat= 'Integer')
x761	=	p.LpVariable("	x761	",lowBound=0, cat= 'Integer')
x762	=	p.LpVariable("	x762	",lowBound=0, cat= 'Integer')
x763	=	p.LpVariable("	x763	",lowBound=0, cat= 'Integer')
x764	=	p.LpVariable("	x764	",lowBound=0, cat= 'Integer')
x765	=	p.LpVariable("	x765	",lowBound=0, cat= 'Integer')
x766	=	p.LpVariable("	x766	",lowBound=0, cat= 'Integer')
x767	=	p.LpVariable("	x767	",lowBound=0, cat= 'Integer')
x768	=	p.LpVariable("	x768	",lowBound=0, cat= 'Integer')
x769	=	p.LpVariable("	x769	",lowBound=0, cat= 'Integer')
x770	=	p.LpVariable("	x770	",lowBound=0, cat= 'Integer')
x771	=	p.LpVariable("	x771	",lowBound=0, cat= 'Integer')
x772	=	p.LpVariable("	x772	",lowBound=0, cat= 'Integer')
x773	=	p.LpVariable("	x773	",lowBound=0, cat= 'Integer')
x774	=	p.LpVariable("	x774	",lowBound=0, cat= 'Integer')
x775	=	p.LpVariable("	x775	",lowBound=0, cat= 'Integer')
x776	=	p.LpVariable("	x776	",lowBound=0, cat= 'Integer')
x777	=	p.LpVariable("	x777	",lowBound=0, cat= 'Integer')
x778	=	p.LpVariable("	x778	",lowBound=0, cat= 'Integer')
x779	=	p.LpVariable("	x779	",lowBound=0, cat= 'Integer')
x780	=	p.LpVariable("	x780	",lowBound=0, cat= 'Integer')
x781	=	p.LpVariable("	x781	",lowBound=0, cat= 'Integer')
x782	=	p.LpVariable("	x782	",lowBound=0, cat= 'Integer')
x783	=	p.LpVariable("	x783	",lowBound=0, cat= 'Integer')
x784	=	p.LpVariable("	x784	",lowBound=0, cat= 'Integer')
x785	=	p.LpVariable("	x785	",lowBound=0, cat= 'Integer')
x786	=	p.LpVariable("	x786	",lowBound=0, cat= 'Integer')
x787	=	p.LpVariable("	x787	",lowBound=0, cat= 'Integer')
x788	=	p.LpVariable("	x788	",lowBound=0, cat= 'Integer')
x789	=	p.LpVariable("	x789	",lowBound=0, cat= 'Integer')
x790	=	p.LpVariable("	x790	",lowBound=0, cat= 'Integer')
x791	=	p.LpVariable("	x791	",lowBound=0, cat= 'Integer')
x792	=	p.LpVariable("	x792	",lowBound=0, cat= 'Integer')
x793	=	p.LpVariable("	x793	",lowBound=0, cat= 'Integer')
x794	=	p.LpVariable("	x794	",lowBound=0, cat= 'Integer')
x795	=	p.LpVariable("	x795	",lowBound=0, cat= 'Integer')
x796	=	p.LpVariable("	x796	",lowBound=0, cat= 'Integer')
x797	=	p.LpVariable("	x797	",lowBound=0, cat= 'Integer')
x798	=	p.LpVariable("	x798	",lowBound=0, cat= 'Integer')
x799	=	p.LpVariable("	x799	",lowBound=0, cat= 'Integer')
x800	=	p.LpVariable("	x800	",lowBound=0, cat= 'Integer')
x801	=	p.LpVariable("	x801	",lowBound=0, cat= 'Integer')
x802	=	p.LpVariable("	x802	",lowBound=0, cat= 'Integer')
x803	=	p.LpVariable("	x803	",lowBound=0, cat= 'Integer')
x804	=	p.LpVariable("	x804	",lowBound=0, cat= 'Integer')
x805	=	p.LpVariable("	x805	",lowBound=0, cat= 'Integer')
x806	=	p.LpVariable("	x806	",lowBound=0, cat= 'Integer')
x807	=	p.LpVariable("	x807	",lowBound=0, cat= 'Integer')
x808	=	p.LpVariable("	x808	",lowBound=0, cat= 'Integer')
x809	=	p.LpVariable("	x809	",lowBound=0, cat= 'Integer')
x810	=	p.LpVariable("	x810	",lowBound=0, cat= 'Integer')
x811	=	p.LpVariable("	x811	",lowBound=0, cat= 'Integer')
x812	=	p.LpVariable("	x812	",lowBound=0, cat= 'Integer')
x813	=	p.LpVariable("	x813	",lowBound=0, cat= 'Integer')
x814	=	p.LpVariable("	x814	",lowBound=0, cat= 'Integer')
x815	=	p.LpVariable("	x815	",lowBound=0, cat= 'Integer')
x816	=	p.LpVariable("	x816	",lowBound=0, cat= 'Integer')
x817	=	p.LpVariable("	x817	",lowBound=0, cat= 'Integer')
x818	=	p.LpVariable("	x818	",lowBound=0, cat= 'Integer')
x819	=	p.LpVariable("	x819	",lowBound=0, cat= 'Integer')
x820	=	p.LpVariable("	x820	",lowBound=0, cat= 'Integer')
x821	=	p.LpVariable("	x821	",lowBound=0, cat= 'Integer')
x822	=	p.LpVariable("	x822	",lowBound=0, cat= 'Integer')
x823	=	p.LpVariable("	x823	",lowBound=0, cat= 'Integer')
x824	=	p.LpVariable("	x824	",lowBound=0, cat= 'Integer')
x825	=	p.LpVariable("	x825	",lowBound=0, cat= 'Integer')
x826	=	p.LpVariable("	x826	",lowBound=0, cat= 'Integer')
x827	=	p.LpVariable("	x827	",lowBound=0, cat= 'Integer')
x828	=	p.LpVariable("	x828	",lowBound=0, cat= 'Integer')
x829	=	p.LpVariable("	x829	",lowBound=0, cat= 'Integer')
x830	=	p.LpVariable("	x830	",lowBound=0, cat= 'Integer')
x831	=	p.LpVariable("	x831	",lowBound=0, cat= 'Integer')
x832	=	p.LpVariable("	x832	",lowBound=0, cat= 'Integer')
x833	=	p.LpVariable("	x833	",lowBound=0, cat= 'Integer')
x834	=	p.LpVariable("	x834	",lowBound=0, cat= 'Integer')
x835	=	p.LpVariable("	x835	",lowBound=0, cat= 'Integer')
x836	=	p.LpVariable("	x836	",lowBound=0, cat= 'Integer')
x837	=	p.LpVariable("	x837	",lowBound=0, cat= 'Integer')
x838	=	p.LpVariable("	x838	",lowBound=0, cat= 'Integer')
x839	=	p.LpVariable("	x839	",lowBound=0, cat= 'Integer')
x840	=	p.LpVariable("	x840	",lowBound=0, cat= 'Integer')
x841	=	p.LpVariable("	x841	",lowBound=0, cat= 'Integer')
x842	=	p.LpVariable("	x842	",lowBound=0, cat= 'Integer')
x843	=	p.LpVariable("	x843	",lowBound=0, cat= 'Integer')
x844	=	p.LpVariable("	x844	",lowBound=0, cat= 'Integer')
x845	=	p.LpVariable("	x845	",lowBound=0, cat= 'Integer')
x846	=	p.LpVariable("	x846	",lowBound=0, cat= 'Integer')
x847	=	p.LpVariable("	x847	",lowBound=0, cat= 'Integer')
x848	=	p.LpVariable("	x848	",lowBound=0, cat= 'Integer')
x849	=	p.LpVariable("	x849	",lowBound=0, cat= 'Integer')
x850	=	p.LpVariable("	x850	",lowBound=0, cat= 'Integer')
x851	=	p.LpVariable("	x851	",lowBound=0, cat= 'Integer')
x852	=	p.LpVariable("	x852	",lowBound=0, cat= 'Integer')
x853	=	p.LpVariable("	x853	",lowBound=0, cat= 'Integer')
x854	=	p.LpVariable("	x854	",lowBound=0, cat= 'Integer')
x855	=	p.LpVariable("	x855	",lowBound=0, cat= 'Integer')
x856	=	p.LpVariable("	x856	",lowBound=0, cat= 'Integer')
x857	=	p.LpVariable("	x857	",lowBound=0, cat= 'Integer')
x858	=	p.LpVariable("	x858	",lowBound=0, cat= 'Integer')
x859	=	p.LpVariable("	x859	",lowBound=0, cat= 'Integer')
x860	=	p.LpVariable("	x860	",lowBound=0, cat= 'Integer')
x861	=	p.LpVariable("	x861	",lowBound=0, cat= 'Integer')
x862	=	p.LpVariable("	x862	",lowBound=0, cat= 'Integer')
x863	=	p.LpVariable("	x863	",lowBound=0, cat= 'Integer')
x864	=	p.LpVariable("	x864	",lowBound=0, cat= 'Integer')
x865	=	p.LpVariable("	x865	",lowBound=0, cat= 'Integer')
x866	=	p.LpVariable("	x866	",lowBound=0, cat= 'Integer')
x867	=	p.LpVariable("	x867	",lowBound=0, cat= 'Integer')
x868	=	p.LpVariable("	x868	",lowBound=0, cat= 'Integer')
x869	=	p.LpVariable("	x869	",lowBound=0, cat= 'Integer')
x870	=	p.LpVariable("	x870	",lowBound=0, cat= 'Integer')
x871	=	p.LpVariable("	x871	",lowBound=0, cat= 'Integer')
x872	=	p.LpVariable("	x872	",lowBound=0, cat= 'Integer')
x873	=	p.LpVariable("	x873	",lowBound=0, cat= 'Integer')
x874	=	p.LpVariable("	x874	",lowBound=0, cat= 'Integer')
x875	=	p.LpVariable("	x875	",lowBound=0, cat= 'Integer')
x876	=	p.LpVariable("	x876	",lowBound=0, cat= 'Integer')
x877	=	p.LpVariable("	x877	",lowBound=0, cat= 'Integer')
x878	=	p.LpVariable("	x878	",lowBound=0, cat= 'Integer')
x879	=	p.LpVariable("	x879	",lowBound=0, cat= 'Integer')
x880	=	p.LpVariable("	x880	",lowBound=0, cat= 'Integer')
x881	=	p.LpVariable("	x881	",lowBound=0, cat= 'Integer')
x882	=	p.LpVariable("	x882	",lowBound=0, cat= 'Integer')
x883	=	p.LpVariable("	x883	",lowBound=0, cat= 'Integer')
x884	=	p.LpVariable("	x884	",lowBound=0, cat= 'Integer')
x885	=	p.LpVariable("	x885	",lowBound=0, cat= 'Integer')
x886	=	p.LpVariable("	x886	",lowBound=0, cat= 'Integer')
x887	=	p.LpVariable("	x887	",lowBound=0, cat= 'Integer')
x888	=	p.LpVariable("	x888	",lowBound=0, cat= 'Integer')
x889	=	p.LpVariable("	x889	",lowBound=0, cat= 'Integer')
x890	=	p.LpVariable("	x890	",lowBound=0, cat= 'Integer')
x891	=	p.LpVariable("	x891	",lowBound=0, cat= 'Integer')
x892	=	p.LpVariable("	x892	",lowBound=0, cat= 'Integer')
x893	=	p.LpVariable("	x893	",lowBound=0, cat= 'Integer')
x894	=	p.LpVariable("	x894	",lowBound=0, cat= 'Integer')
x895	=	p.LpVariable("	x895	",lowBound=0, cat= 'Integer')
x896	=	p.LpVariable("	x896	",lowBound=0, cat= 'Integer')
x897	=	p.LpVariable("	x897	",lowBound=0, cat= 'Integer')
x898	=	p.LpVariable("	x898	",lowBound=0, cat= 'Integer')
x899	=	p.LpVariable("	x899	",lowBound=0, cat= 'Integer')
x900	=	p.LpVariable("	x900	",lowBound=0, cat= 'Integer')
x901	=	p.LpVariable("	x901	",lowBound=0, cat= 'Integer')
x902	=	p.LpVariable("	x902	",lowBound=0, cat= 'Integer')
x903	=	p.LpVariable("	x903	",lowBound=0, cat= 'Integer')
x904	=	p.LpVariable("	x904	",lowBound=0, cat= 'Integer')
x905	=	p.LpVariable("	x905	",lowBound=0, cat= 'Integer')
x906	=	p.LpVariable("	x906	",lowBound=0, cat= 'Integer')
x907	=	p.LpVariable("	x907	",lowBound=0, cat= 'Integer')
x908	=	p.LpVariable("	x908	",lowBound=0, cat= 'Integer')
x909	=	p.LpVariable("	x909	",lowBound=0, cat= 'Integer')
x910	=	p.LpVariable("	x910	",lowBound=0, cat= 'Integer')
x911	=	p.LpVariable("	x911	",lowBound=0, cat= 'Integer')
x912	=	p.LpVariable("	x912	",lowBound=0, cat= 'Integer')
x913	=	p.LpVariable("	x913	",lowBound=0, cat= 'Integer')
x914	=	p.LpVariable("	x914	",lowBound=0, cat= 'Integer')
x915	=	p.LpVariable("	x915	",lowBound=0, cat= 'Integer')
x916	=	p.LpVariable("	x916	",lowBound=0, cat= 'Integer')
x917	=	p.LpVariable("	x917	",lowBound=0, cat= 'Integer')
x918	=	p.LpVariable("	x918	",lowBound=0, cat= 'Integer')
x919	=	p.LpVariable("	x919	",lowBound=0, cat= 'Integer')
x920	=	p.LpVariable("	x920	",lowBound=0, cat= 'Integer')
x921	=	p.LpVariable("	x921	",lowBound=0, cat= 'Integer')
x922	=	p.LpVariable("	x922	",lowBound=0, cat= 'Integer')
x923	=	p.LpVariable("	x923	",lowBound=0, cat= 'Integer')
x924	=	p.LpVariable("	x924	",lowBound=0, cat= 'Integer')
x925	=	p.LpVariable("	x925	",lowBound=0, cat= 'Integer')
x926	=	p.LpVariable("	x926	",lowBound=0, cat= 'Integer')
x927	=	p.LpVariable("	x927	",lowBound=0, cat= 'Integer')
x928	=	p.LpVariable("	x928	",lowBound=0, cat= 'Integer')
x929	=	p.LpVariable("	x929	",lowBound=0, cat= 'Integer')
x930	=	p.LpVariable("	x930	",lowBound=0, cat= 'Integer')
x931	=	p.LpVariable("	x931	",lowBound=0, cat= 'Integer')
x932	=	p.LpVariable("	x932	",lowBound=0, cat= 'Integer')
x933	=	p.LpVariable("	x933	",lowBound=0, cat= 'Integer')
x934	=	p.LpVariable("	x934	",lowBound=0, cat= 'Integer')
x935	=	p.LpVariable("	x935	",lowBound=0, cat= 'Integer')
x936	=	p.LpVariable("	x936	",lowBound=0, cat= 'Integer')
x937	=	p.LpVariable("	x937	",lowBound=0, cat= 'Integer')
x938	=	p.LpVariable("	x938	",lowBound=0, cat= 'Integer')
x939	=	p.LpVariable("	x939	",lowBound=0, cat= 'Integer')
x940	=	p.LpVariable("	x940	",lowBound=0, cat= 'Integer')
x941	=	p.LpVariable("	x941	",lowBound=0, cat= 'Integer')
x942	=	p.LpVariable("	x942	",lowBound=0, cat= 'Integer')
x943	=	p.LpVariable("	x943	",lowBound=0, cat= 'Integer')
x944	=	p.LpVariable("	x944	",lowBound=0, cat= 'Integer')
x945	=	p.LpVariable("	x945	",lowBound=0, cat= 'Integer')
x946	=	p.LpVariable("	x946	",lowBound=0, cat= 'Integer')
x947	=	p.LpVariable("	x947	",lowBound=0, cat= 'Integer')
x948	=	p.LpVariable("	x948	",lowBound=0, cat= 'Integer')
x949	=	p.LpVariable("	x949	",lowBound=0, cat= 'Integer')
x950	=	p.LpVariable("	x950	",lowBound=0, cat= 'Integer')
x951	=	p.LpVariable("	x951	",lowBound=0, cat= 'Integer')
x952	=	p.LpVariable("	x952	",lowBound=0, cat= 'Integer')
x953	=	p.LpVariable("	x953	",lowBound=0, cat= 'Integer')
x954	=	p.LpVariable("	x954	",lowBound=0, cat= 'Integer')
x955	=	p.LpVariable("	x955	",lowBound=0, cat= 'Integer')
x956	=	p.LpVariable("	x956	",lowBound=0, cat= 'Integer')
x957	=	p.LpVariable("	x957	",lowBound=0, cat= 'Integer')
x958	=	p.LpVariable("	x958	",lowBound=0, cat= 'Integer')
x959	=	p.LpVariable("	x959	",lowBound=0, cat= 'Integer')
x960	=	p.LpVariable("	x960	",lowBound=0, cat= 'Integer')
x961	=	p.LpVariable("	x961	",lowBound=0, cat= 'Integer')
x962	=	p.LpVariable("	x962	",lowBound=0, cat= 'Integer')
x963	=	p.LpVariable("	x963	",lowBound=0, cat= 'Integer')
x964	=	p.LpVariable("	x964	",lowBound=0, cat= 'Integer')
x965	=	p.LpVariable("	x965	",lowBound=0, cat= 'Integer')
x966	=	p.LpVariable("	x966	",lowBound=0, cat= 'Integer')
x967	=	p.LpVariable("	x967	",lowBound=0, cat= 'Integer')
x968	=	p.LpVariable("	x968	",lowBound=0, cat= 'Integer')
x969	=	p.LpVariable("	x969	",lowBound=0, cat= 'Integer')
x970	=	p.LpVariable("	x970	",lowBound=0, cat= 'Integer')
x971	=	p.LpVariable("	x971	",lowBound=0, cat= 'Integer')
x972	=	p.LpVariable("	x972	",lowBound=0, cat= 'Integer')
x973	=	p.LpVariable("	x973	",lowBound=0, cat= 'Integer')
x974	=	p.LpVariable("	x974	",lowBound=0, cat= 'Integer')
x975	=	p.LpVariable("	x975	",lowBound=0, cat= 'Integer')
x976	=	p.LpVariable("	x976	",lowBound=0, cat= 'Integer')
x977	=	p.LpVariable("	x977	",lowBound=0, cat= 'Integer')
x978	=	p.LpVariable("	x978	",lowBound=0, cat= 'Integer')
x979	=	p.LpVariable("	x979	",lowBound=0, cat= 'Integer')
x980	=	p.LpVariable("	x980	",lowBound=0, cat= 'Integer')
x981	=	p.LpVariable("	x981	",lowBound=0, cat= 'Integer')
x982	=	p.LpVariable("	x982	",lowBound=0, cat= 'Integer')
x983	=	p.LpVariable("	x983	",lowBound=0, cat= 'Integer')
x984	=	p.LpVariable("	x984	",lowBound=0, cat= 'Integer')
x985	=	p.LpVariable("	x985	",lowBound=0, cat= 'Integer')
x986	=	p.LpVariable("	x986	",lowBound=0, cat= 'Integer')
x987	=	p.LpVariable("	x987	",lowBound=0, cat= 'Integer')
x988	=	p.LpVariable("	x988	",lowBound=0, cat= 'Integer')
x989	=	p.LpVariable("	x989	",lowBound=0, cat= 'Integer')
x990	=	p.LpVariable("	x990	",lowBound=0, cat= 'Integer')
x991	=	p.LpVariable("	x991	",lowBound=0, cat= 'Integer')
x992	=	p.LpVariable("	x992	",lowBound=0, cat= 'Integer')
x993	=	p.LpVariable("	x993	",lowBound=0, cat= 'Integer')
x994	=	p.LpVariable("	x994	",lowBound=0, cat= 'Integer')
x995	=	p.LpVariable("	x995	",lowBound=0, cat= 'Integer')
x996	=	p.LpVariable("	x996	",lowBound=0, cat= 'Integer')
x997	=	p.LpVariable("	x997	",lowBound=0, cat= 'Integer')
x998	=	p.LpVariable("	x998	",lowBound=0, cat= 'Integer')
x999	=	p.LpVariable("	x999	",lowBound=0, cat= 'Integer')
x1000	=	p.LpVariable("	x1000	",lowBound=0, cat= 'Integer')
x1001	=	p.LpVariable("	x1001	",lowBound=0, cat= 'Integer')
x1002	=	p.LpVariable("	x1002	",lowBound=0, cat= 'Integer')
x1003	=	p.LpVariable("	x1003	",lowBound=0, cat= 'Integer')
x1004	=	p.LpVariable("	x1004	",lowBound=0, cat= 'Integer')
x1005	=	p.LpVariable("	x1005	",lowBound=0, cat= 'Integer')
x1006	=	p.LpVariable("	x1006	",lowBound=0, cat= 'Integer')
x1007	=	p.LpVariable("	x1007	",lowBound=0, cat= 'Integer')
x1008	=	p.LpVariable("	x1008	",lowBound=0, cat= 'Integer')
x1009	=	p.LpVariable("	x1009	",lowBound=0, cat= 'Integer')
x1010	=	p.LpVariable("	x1010	",lowBound=0, cat= 'Integer')
x1011	=	p.LpVariable("	x1011	",lowBound=0, cat= 'Integer')
x1012	=	p.LpVariable("	x1012	",lowBound=0, cat= 'Integer')
x1013	=	p.LpVariable("	x1013	",lowBound=0, cat= 'Integer')
x1014	=	p.LpVariable("	x1014	",lowBound=0, cat= 'Integer')
x1015	=	p.LpVariable("	x1015	",lowBound=0, cat= 'Integer')
x1016	=	p.LpVariable("	x1016	",lowBound=0, cat= 'Integer')
x1017	=	p.LpVariable("	x1017	",lowBound=0, cat= 'Integer')
x1018	=	p.LpVariable("	x1018	",lowBound=0, cat= 'Integer')
x1019	=	p.LpVariable("	x1019	",lowBound=0, cat= 'Integer')
x1020	=	p.LpVariable("	x1020	",lowBound=0, cat= 'Integer')
x1021	=	p.LpVariable("	x1021	",lowBound=0, cat= 'Integer')
x1022	=	p.LpVariable("	x1022	",lowBound=0, cat= 'Integer')
x1023	=	p.LpVariable("	x1023	",lowBound=0, cat= 'Integer')
x1024	=	p.LpVariable("	x1024	",lowBound=0, cat= 'Integer')
x1025	=	p.LpVariable("	x1025	",lowBound=0, cat= 'Integer')
x1026	=	p.LpVariable("	x1026	",lowBound=0, cat= 'Integer')
x1027	=	p.LpVariable("	x1027	",lowBound=0, cat= 'Integer')
x1028	=	p.LpVariable("	x1028	",lowBound=0, cat= 'Integer')
x1029	=	p.LpVariable("	x1029	",lowBound=0, cat= 'Integer')
x1030	=	p.LpVariable("	x1030	",lowBound=0, cat= 'Integer')
x1031	=	p.LpVariable("	x1031	",lowBound=0, cat= 'Integer')
x1032	=	p.LpVariable("	x1032	",lowBound=0, cat= 'Integer')
x1033	=	p.LpVariable("	x1033	",lowBound=0, cat= 'Integer')
x1034	=	p.LpVariable("	x1034	",lowBound=0, cat= 'Integer')
x1035	=	p.LpVariable("	x1035	",lowBound=0, cat= 'Integer')
x1036	=	p.LpVariable("	x1036	",lowBound=0, cat= 'Integer')
x1037	=	p.LpVariable("	x1037	",lowBound=0, cat= 'Integer')
x1038	=	p.LpVariable("	x1038	",lowBound=0, cat= 'Integer')
x1039	=	p.LpVariable("	x1039	",lowBound=0, cat= 'Integer')
x1040	=	p.LpVariable("	x1040	",lowBound=0, cat= 'Integer')
x1041	=	p.LpVariable("	x1041	",lowBound=0, cat= 'Integer')
x1042	=	p.LpVariable("	x1042	",lowBound=0, cat= 'Integer')
x1043	=	p.LpVariable("	x1043	",lowBound=0, cat= 'Integer')
x1044	=	p.LpVariable("	x1044	",lowBound=0, cat= 'Integer')
x1045	=	p.LpVariable("	x1045	",lowBound=0, cat= 'Integer')
x1046	=	p.LpVariable("	x1046	",lowBound=0, cat= 'Integer')
x1047	=	p.LpVariable("	x1047	",lowBound=0, cat= 'Integer')
x1048	=	p.LpVariable("	x1048	",lowBound=0, cat= 'Integer')
x1049	=	p.LpVariable("	x1049	",lowBound=0, cat= 'Integer')
x1050	=	p.LpVariable("	x1050	",lowBound=0, cat= 'Integer')
x1051	=	p.LpVariable("	x1051	",lowBound=0, cat= 'Integer')
x1052	=	p.LpVariable("	x1052	",lowBound=0, cat= 'Integer')
x1053	=	p.LpVariable("	x1053	",lowBound=0, cat= 'Integer')
x1054	=	p.LpVariable("	x1054	",lowBound=0, cat= 'Integer')
x1055	=	p.LpVariable("	x1055	",lowBound=0, cat= 'Integer')
x1056	=	p.LpVariable("	x1056	",lowBound=0, cat= 'Integer')
x1057	=	p.LpVariable("	x1057	",lowBound=0, cat= 'Integer')
x1058	=	p.LpVariable("	x1058	",lowBound=0, cat= 'Integer')
x1059	=	p.LpVariable("	x1059	",lowBound=0, cat= 'Integer')
x1060	=	p.LpVariable("	x1060	",lowBound=0, cat= 'Integer')
x1061	=	p.LpVariable("	x1061	",lowBound=0, cat= 'Integer')
x1062	=	p.LpVariable("	x1062	",lowBound=0, cat= 'Integer')
x1063	=	p.LpVariable("	x1063	",lowBound=0, cat= 'Integer')
x1064	=	p.LpVariable("	x1064	",lowBound=0, cat= 'Integer')
x1065	=	p.LpVariable("	x1065	",lowBound=0, cat= 'Integer')
x1066	=	p.LpVariable("	x1066	",lowBound=0, cat= 'Integer')
x1067	=	p.LpVariable("	x1067	",lowBound=0, cat= 'Integer')
x1068	=	p.LpVariable("	x1068	",lowBound=0, cat= 'Integer')
x1069	=	p.LpVariable("	x1069	",lowBound=0, cat= 'Integer')
x1070	=	p.LpVariable("	x1070	",lowBound=0, cat= 'Integer')
x1071	=	p.LpVariable("	x1071	",lowBound=0, cat= 'Integer')
x1072	=	p.LpVariable("	x1072	",lowBound=0, cat= 'Integer')
x1073	=	p.LpVariable("	x1073	",lowBound=0, cat= 'Integer')
x1074	=	p.LpVariable("	x1074	",lowBound=0, cat= 'Integer')
x1075	=	p.LpVariable("	x1075	",lowBound=0, cat= 'Integer')
x1076	=	p.LpVariable("	x1076	",lowBound=0, cat= 'Integer')
x1077	=	p.LpVariable("	x1077	",lowBound=0, cat= 'Integer')
x1078	=	p.LpVariable("	x1078	",lowBound=0, cat= 'Integer')
x1079	=	p.LpVariable("	x1079	",lowBound=0, cat= 'Integer')
x1080	=	p.LpVariable("	x1080	",lowBound=0, cat= 'Integer')
x1081	=	p.LpVariable("	x1081	",lowBound=0, cat= 'Integer')
x1082	=	p.LpVariable("	x1082	",lowBound=0, cat= 'Integer')
x1083	=	p.LpVariable("	x1083	",lowBound=0, cat= 'Integer')
x1084	=	p.LpVariable("	x1084	",lowBound=0, cat= 'Integer')
x1085	=	p.LpVariable("	x1085	",lowBound=0, cat= 'Integer')
x1086	=	p.LpVariable("	x1086	",lowBound=0, cat= 'Integer')
x1087	=	p.LpVariable("	x1087	",lowBound=0, cat= 'Integer')
x1088	=	p.LpVariable("	x1088	",lowBound=0, cat= 'Integer')
x1089	=	p.LpVariable("	x1089	",lowBound=0, cat= 'Integer')
x1090	=	p.LpVariable("	x1090	",lowBound=0, cat= 'Integer')
x1091	=	p.LpVariable("	x1091	",lowBound=0, cat= 'Integer')
x1092	=	p.LpVariable("	x1092	",lowBound=0, cat= 'Integer')
x1093	=	p.LpVariable("	x1093	",lowBound=0, cat= 'Integer')
x1094	=	p.LpVariable("	x1094	",lowBound=0, cat= 'Integer')
x1095	=	p.LpVariable("	x1095	",lowBound=0, cat= 'Integer')
x1096	=	p.LpVariable("	x1096	",lowBound=0, cat= 'Integer')
x1097	=	p.LpVariable("	x1097	",lowBound=0, cat= 'Integer')
x1098	=	p.LpVariable("	x1098	",lowBound=0, cat= 'Integer')
x1099	=	p.LpVariable("	x1099	",lowBound=0, cat= 'Integer')
x1100	=	p.LpVariable("	x1100	",lowBound=0, cat= 'Integer')
x1101	=	p.LpVariable("	x1101	",lowBound=0, cat= 'Integer')
x1102	=	p.LpVariable("	x1102	",lowBound=0, cat= 'Integer')
x1103	=	p.LpVariable("	x1103	",lowBound=0, cat= 'Integer')
x1104	=	p.LpVariable("	x1104	",lowBound=0, cat= 'Integer')
x1105	=	p.LpVariable("	x1105	",lowBound=0, cat= 'Integer')
x1106	=	p.LpVariable("	x1106	",lowBound=0, cat= 'Integer')
x1107	=	p.LpVariable("	x1107	",lowBound=0, cat= 'Integer')
x1108	=	p.LpVariable("	x1108	",lowBound=0, cat= 'Integer')
x1109	=	p.LpVariable("	x1109	",lowBound=0, cat= 'Integer')
x1110	=	p.LpVariable("	x1110	",lowBound=0, cat= 'Integer')
x1111	=	p.LpVariable("	x1111	",lowBound=0, cat= 'Integer')
x1112	=	p.LpVariable("	x1112	",lowBound=0, cat= 'Integer')
x1113	=	p.LpVariable("	x1113	",lowBound=0, cat= 'Integer')
x1114	=	p.LpVariable("	x1114	",lowBound=0, cat= 'Integer')
x1115	=	p.LpVariable("	x1115	",lowBound=0, cat= 'Integer')
x1116	=	p.LpVariable("	x1116	",lowBound=0, cat= 'Integer')
x1117	=	p.LpVariable("	x1117	",lowBound=0, cat= 'Integer')
x1118	=	p.LpVariable("	x1118	",lowBound=0, cat= 'Integer')
x1119	=	p.LpVariable("	x1119	",lowBound=0, cat= 'Integer')
x1120	=	p.LpVariable("	x1120	",lowBound=0, cat= 'Integer')
x1121	=	p.LpVariable("	x1121	",lowBound=0, cat= 'Integer')
x1122	=	p.LpVariable("	x1122	",lowBound=0, cat= 'Integer')
x1123	=	p.LpVariable("	x1123	",lowBound=0, cat= 'Integer')
x1124	=	p.LpVariable("	x1124	",lowBound=0, cat= 'Integer')
x1125	=	p.LpVariable("	x1125	",lowBound=0, cat= 'Integer')
x1126	=	p.LpVariable("	x1126	",lowBound=0, cat= 'Integer')
x1127	=	p.LpVariable("	x1127	",lowBound=0, cat= 'Integer')
x1128	=	p.LpVariable("	x1128	",lowBound=0, cat= 'Integer')
x1129	=	p.LpVariable("	x1129	",lowBound=0, cat= 'Integer')
x1130	=	p.LpVariable("	x1130	",lowBound=0, cat= 'Integer')
x1131	=	p.LpVariable("	x1131	",lowBound=0, cat= 'Integer')
x1132	=	p.LpVariable("	x1132	",lowBound=0, cat= 'Integer')
x1133	=	p.LpVariable("	x1133	",lowBound=0, cat= 'Integer')
x1134	=	p.LpVariable("	x1134	",lowBound=0, cat= 'Integer')
x1135	=	p.LpVariable("	x1135	",lowBound=0, cat= 'Integer')
x1136	=	p.LpVariable("	x1136	",lowBound=0, cat= 'Integer')
x1137	=	p.LpVariable("	x1137	",lowBound=0, cat= 'Integer')
x1138	=	p.LpVariable("	x1138	",lowBound=0, cat= 'Integer')
x1139	=	p.LpVariable("	x1139	",lowBound=0, cat= 'Integer')
x1140	=	p.LpVariable("	x1140	",lowBound=0, cat= 'Integer')
x1141	=	p.LpVariable("	x1141	",lowBound=0, cat= 'Integer')
x1142	=	p.LpVariable("	x1142	",lowBound=0, cat= 'Integer')
x1143	=	p.LpVariable("	x1143	",lowBound=0, cat= 'Integer')
x1144	=	p.LpVariable("	x1144	",lowBound=0, cat= 'Integer')
x1145	=	p.LpVariable("	x1145	",lowBound=0, cat= 'Integer')
x1146	=	p.LpVariable("	x1146	",lowBound=0, cat= 'Integer')
x1147	=	p.LpVariable("	x1147	",lowBound=0, cat= 'Integer')
x1148	=	p.LpVariable("	x1148	",lowBound=0, cat= 'Integer')
x1149	=	p.LpVariable("	x1149	",lowBound=0, cat= 'Integer')
x1150	=	p.LpVariable("	x1150	",lowBound=0, cat= 'Integer')
x1151	=	p.LpVariable("	x1151	",lowBound=0, cat= 'Integer')
x1152	=	p.LpVariable("	x1152	",lowBound=0, cat= 'Integer')
x1153	=	p.LpVariable("	x1153	",lowBound=0, cat= 'Integer')
x1154	=	p.LpVariable("	x1154	",lowBound=0, cat= 'Integer')
x1155	=	p.LpVariable("	x1155	",lowBound=0, cat= 'Integer')
x1156	=	p.LpVariable("	x1156	",lowBound=0, cat= 'Integer')
x1157	=	p.LpVariable("	x1157	",lowBound=0, cat= 'Integer')
x1158	=	p.LpVariable("	x1158	",lowBound=0, cat= 'Integer')
x1159	=	p.LpVariable("	x1159	",lowBound=0, cat= 'Integer')
x1160	=	p.LpVariable("	x1160	",lowBound=0, cat= 'Integer')
x1161	=	p.LpVariable("	x1161	",lowBound=0, cat= 'Integer')
x1162	=	p.LpVariable("	x1162	",lowBound=0, cat= 'Integer')
x1163	=	p.LpVariable("	x1163	",lowBound=0, cat= 'Integer')
x1164	=	p.LpVariable("	x1164	",lowBound=0, cat= 'Integer')
x1165	=	p.LpVariable("	x1165	",lowBound=0, cat= 'Integer')
x1166	=	p.LpVariable("	x1166	",lowBound=0, cat= 'Integer')
x1167	=	p.LpVariable("	x1167	",lowBound=0, cat= 'Integer')
x1168	=	p.LpVariable("	x1168	",lowBound=0, cat= 'Integer')
x1169	=	p.LpVariable("	x1169	",lowBound=0, cat= 'Integer')
x1170	=	p.LpVariable("	x1170	",lowBound=0, cat= 'Integer')
x1171	=	p.LpVariable("	x1171	",lowBound=0, cat= 'Integer')
x1172	=	p.LpVariable("	x1172	",lowBound=0, cat= 'Integer')
x1173	=	p.LpVariable("	x1173	",lowBound=0, cat= 'Integer')
x1174	=	p.LpVariable("	x1174	",lowBound=0, cat= 'Integer')
x1175	=	p.LpVariable("	x1175	",lowBound=0, cat= 'Integer')
x1176	=	p.LpVariable("	x1176	",lowBound=0, cat= 'Integer')
x1177	=	p.LpVariable("	x1177	",lowBound=0, cat= 'Integer')
x1178	=	p.LpVariable("	x1178	",lowBound=0, cat= 'Integer')
x1179	=	p.LpVariable("	x1179	",lowBound=0, cat= 'Integer')
x1180	=	p.LpVariable("	x1180	",lowBound=0, cat= 'Integer')
x1181	=	p.LpVariable("	x1181	",lowBound=0, cat= 'Integer')
x1182	=	p.LpVariable("	x1182	",lowBound=0, cat= 'Integer')
x1183	=	p.LpVariable("	x1183	",lowBound=0, cat= 'Integer')
x1184	=	p.LpVariable("	x1184	",lowBound=0, cat= 'Integer')
x1185	=	p.LpVariable("	x1185	",lowBound=0, cat= 'Integer')
x1186	=	p.LpVariable("	x1186	",lowBound=0, cat= 'Integer')
x1187	=	p.LpVariable("	x1187	",lowBound=0, cat= 'Integer')
x1188	=	p.LpVariable("	x1188	",lowBound=0, cat= 'Integer')
x1189	=	p.LpVariable("	x1189	",lowBound=0, cat= 'Integer')
x1190	=	p.LpVariable("	x1190	",lowBound=0, cat= 'Integer')
x1191	=	p.LpVariable("	x1191	",lowBound=0, cat= 'Integer')
x1192	=	p.LpVariable("	x1192	",lowBound=0, cat= 'Integer')
x1193	=	p.LpVariable("	x1193	",lowBound=0, cat= 'Integer')
x1194	=	p.LpVariable("	x1194	",lowBound=0, cat= 'Integer')
x1195	=	p.LpVariable("	x1195	",lowBound=0, cat= 'Integer')
x1196	=	p.LpVariable("	x1196	",lowBound=0, cat= 'Integer')
x1197	=	p.LpVariable("	x1197	",lowBound=0, cat= 'Integer')
x1198	=	p.LpVariable("	x1198	",lowBound=0, cat= 'Integer')
x1199	=	p.LpVariable("	x1199	",lowBound=0, cat= 'Integer')
x1200	=	p.LpVariable("	x1200	",lowBound=0, cat= 'Integer')
x1201	=	p.LpVariable("	x1201	",lowBound=0, cat= 'Integer')
x1202	=	p.LpVariable("	x1202	",lowBound=0, cat= 'Integer')
x1203	=	p.LpVariable("	x1203	",lowBound=0, cat= 'Integer')
x1204	=	p.LpVariable("	x1204	",lowBound=0, cat= 'Integer')
x1205	=	p.LpVariable("	x1205	",lowBound=0, cat= 'Integer')
x1206	=	p.LpVariable("	x1206	",lowBound=0, cat= 'Integer')
x1207	=	p.LpVariable("	x1207	",lowBound=0, cat= 'Integer')
x1208	=	p.LpVariable("	x1208	",lowBound=0, cat= 'Integer')
x1209	=	p.LpVariable("	x1209	",lowBound=0, cat= 'Integer')
x1210	=	p.LpVariable("	x1210	",lowBound=0, cat= 'Integer')
x1211	=	p.LpVariable("	x1211	",lowBound=0, cat= 'Integer')
x1212	=	p.LpVariable("	x1212	",lowBound=0, cat= 'Integer')
x1213	=	p.LpVariable("	x1213	",lowBound=0, cat= 'Integer')
x1214	=	p.LpVariable("	x1214	",lowBound=0, cat= 'Integer')
x1215	=	p.LpVariable("	x1215	",lowBound=0, cat= 'Integer')
x1216	=	p.LpVariable("	x1216	",lowBound=0, cat= 'Integer')
x1217	=	p.LpVariable("	x1217	",lowBound=0, cat= 'Integer')
x1218	=	p.LpVariable("	x1218	",lowBound=0, cat= 'Integer')
x1219	=	p.LpVariable("	x1219	",lowBound=0, cat= 'Integer')
x1220	=	p.LpVariable("	x1220	",lowBound=0, cat= 'Integer')
x1221	=	p.LpVariable("	x1221	",lowBound=0, cat= 'Integer')
x1222	=	p.LpVariable("	x1222	",lowBound=0, cat= 'Integer')
x1223	=	p.LpVariable("	x1223	",lowBound=0, cat= 'Integer')
x1224	=	p.LpVariable("	x1224	",lowBound=0, cat= 'Integer')
x1225	=	p.LpVariable("	x1225	",lowBound=0, cat= 'Integer')
x1226	=	p.LpVariable("	x1226	",lowBound=0, cat= 'Integer')
x1227	=	p.LpVariable("	x1227	",lowBound=0, cat= 'Integer')
x1228	=	p.LpVariable("	x1228	",lowBound=0, cat= 'Integer')
x1229	=	p.LpVariable("	x1229	",lowBound=0, cat= 'Integer')
x1230	=	p.LpVariable("	x1230	",lowBound=0, cat= 'Integer')
x1231	=	p.LpVariable("	x1231	",lowBound=0, cat= 'Integer')
x1232	=	p.LpVariable("	x1232	",lowBound=0, cat= 'Integer')
x1233	=	p.LpVariable("	x1233	",lowBound=0, cat= 'Integer')
x1234	=	p.LpVariable("	x1234	",lowBound=0, cat= 'Integer')
x1235	=	p.LpVariable("	x1235	",lowBound=0, cat= 'Integer')
x1236	=	p.LpVariable("	x1236	",lowBound=0, cat= 'Integer')
x1237	=	p.LpVariable("	x1237	",lowBound=0, cat= 'Integer')
x1238	=	p.LpVariable("	x1238	",lowBound=0, cat= 'Integer')
x1239	=	p.LpVariable("	x1239	",lowBound=0, cat= 'Integer')
x1240	=	p.LpVariable("	x1240	",lowBound=0, cat= 'Integer')
x1241	=	p.LpVariable("	x1241	",lowBound=0, cat= 'Integer')
x1242	=	p.LpVariable("	x1242	",lowBound=0, cat= 'Integer')
x1243	=	p.LpVariable("	x1243	",lowBound=0, cat= 'Integer')
x1244	=	p.LpVariable("	x1244	",lowBound=0, cat= 'Integer')
x1245	=	p.LpVariable("	x1245	",lowBound=0, cat= 'Integer')
x1246	=	p.LpVariable("	x1246	",lowBound=0, cat= 'Integer')
x1247	=	p.LpVariable("	x1247	",lowBound=0, cat= 'Integer')
x1248	=	p.LpVariable("	x1248	",lowBound=0, cat= 'Integer')
x1249	=	p.LpVariable("	x1249	",lowBound=0, cat= 'Integer')
x1250	=	p.LpVariable("	x1250	",lowBound=0, cat= 'Integer')
x1251	=	p.LpVariable("	x1251	",lowBound=0, cat= 'Integer')
x1252	=	p.LpVariable("	x1252	",lowBound=0, cat= 'Integer')
x1253	=	p.LpVariable("	x1253	",lowBound=0, cat= 'Integer')
x1254	=	p.LpVariable("	x1254	",lowBound=0, cat= 'Integer')
x1255	=	p.LpVariable("	x1255	",lowBound=0, cat= 'Integer')
x1256	=	p.LpVariable("	x1256	",lowBound=0, cat= 'Integer')
x1257	=	p.LpVariable("	x1257	",lowBound=0, cat= 'Integer')
x1258	=	p.LpVariable("	x1258	",lowBound=0, cat= 'Integer')
x1259	=	p.LpVariable("	x1259	",lowBound=0, cat= 'Integer')
x1260	=	p.LpVariable("	x1260	",lowBound=0, cat= 'Integer')
x1261	=	p.LpVariable("	x1261	",lowBound=0, cat= 'Integer')
x1262	=	p.LpVariable("	x1262	",lowBound=0, cat= 'Integer')
x1263	=	p.LpVariable("	x1263	",lowBound=0, cat= 'Integer')
x1264	=	p.LpVariable("	x1264	",lowBound=0, cat= 'Integer')
x1265	=	p.LpVariable("	x1265	",lowBound=0, cat= 'Integer')
x1266	=	p.LpVariable("	x1266	",lowBound=0, cat= 'Integer')
x1267	=	p.LpVariable("	x1267	",lowBound=0, cat= 'Integer')
x1268	=	p.LpVariable("	x1268	",lowBound=0, cat= 'Integer')
x1269	=	p.LpVariable("	x1269	",lowBound=0, cat= 'Integer')
x1270	=	p.LpVariable("	x1270	",lowBound=0, cat= 'Integer')
x1271	=	p.LpVariable("	x1271	",lowBound=0, cat= 'Integer')
x1272	=	p.LpVariable("	x1272	",lowBound=0, cat= 'Integer')
x1273	=	p.LpVariable("	x1273	",lowBound=0, cat= 'Integer')
x1274	=	p.LpVariable("	x1274	",lowBound=0, cat= 'Integer')
x1275	=	p.LpVariable("	x1275	",lowBound=0, cat= 'Integer')
x1276	=	p.LpVariable("	x1276	",lowBound=0, cat= 'Integer')
x1277	=	p.LpVariable("	x1277	",lowBound=0, cat= 'Integer')
x1278	=	p.LpVariable("	x1278	",lowBound=0, cat= 'Integer')
x1279	=	p.LpVariable("	x1279	",lowBound=0, cat= 'Integer')
x1280	=	p.LpVariable("	x1280	",lowBound=0, cat= 'Integer')
x1281	=	p.LpVariable("	x1281	",lowBound=0, cat= 'Integer')
x1282	=	p.LpVariable("	x1282	",lowBound=0, cat= 'Integer')
x1283	=	p.LpVariable("	x1283	",lowBound=0, cat= 'Integer')
x1284	=	p.LpVariable("	x1284	",lowBound=0, cat= 'Integer')
x1285	=	p.LpVariable("	x1285	",lowBound=0, cat= 'Integer')
x1286	=	p.LpVariable("	x1286	",lowBound=0, cat= 'Integer')
x1287	=	p.LpVariable("	x1287	",lowBound=0, cat= 'Integer')
x1288	=	p.LpVariable("	x1288	",lowBound=0, cat= 'Integer')
x1289	=	p.LpVariable("	x1289	",lowBound=0, cat= 'Integer')
x1290	=	p.LpVariable("	x1290	",lowBound=0, cat= 'Integer')
x1291	=	p.LpVariable("	x1291	",lowBound=0, cat= 'Integer')
x1292	=	p.LpVariable("	x1292	",lowBound=0, cat= 'Integer')
x1293	=	p.LpVariable("	x1293	",lowBound=0, cat= 'Integer')
x1294	=	p.LpVariable("	x1294	",lowBound=0, cat= 'Integer')
x1295	=	p.LpVariable("	x1295	",lowBound=0, cat= 'Integer')
x1296	=	p.LpVariable("	x1296	",lowBound=0, cat= 'Integer')
x1297	=	p.LpVariable("	x1297	",lowBound=0, cat= 'Integer')
x1298	=	p.LpVariable("	x1298	",lowBound=0, cat= 'Integer')
x1299	=	p.LpVariable("	x1299	",lowBound=0, cat= 'Integer')
x1300	=	p.LpVariable("	x1300	",lowBound=0, cat= 'Integer')
x1301	=	p.LpVariable("	x1301	",lowBound=0, cat= 'Integer')
x1302	=	p.LpVariable("	x1302	",lowBound=0, cat= 'Integer')
x1303	=	p.LpVariable("	x1303	",lowBound=0, cat= 'Integer')
x1304	=	p.LpVariable("	x1304	",lowBound=0, cat= 'Integer')
x1305	=	p.LpVariable("	x1305	",lowBound=0, cat= 'Integer')
x1306	=	p.LpVariable("	x1306	",lowBound=0, cat= 'Integer')
x1307	=	p.LpVariable("	x1307	",lowBound=0, cat= 'Integer')
x1308	=	p.LpVariable("	x1308	",lowBound=0, cat= 'Integer')
x1309	=	p.LpVariable("	x1309	",lowBound=0, cat= 'Integer')
x1310	=	p.LpVariable("	x1310	",lowBound=0, cat= 'Integer')
x1311	=	p.LpVariable("	x1311	",lowBound=0, cat= 'Integer')
x1312	=	p.LpVariable("	x1312	",lowBound=0, cat= 'Integer')
x1313	=	p.LpVariable("	x1313	",lowBound=0, cat= 'Integer')
x1314	=	p.LpVariable("	x1314	",lowBound=0, cat= 'Integer')
x1315	=	p.LpVariable("	x1315	",lowBound=0, cat= 'Integer')
x1316	=	p.LpVariable("	x1316	",lowBound=0, cat= 'Integer')
x1317	=	p.LpVariable("	x1317	",lowBound=0, cat= 'Integer')
x1318	=	p.LpVariable("	x1318	",lowBound=0, cat= 'Integer')
x1319	=	p.LpVariable("	x1319	",lowBound=0, cat= 'Integer')
x1320	=	p.LpVariable("	x1320	",lowBound=0, cat= 'Integer')
x1321	=	p.LpVariable("	x1321	",lowBound=0, cat= 'Integer')
x1322	=	p.LpVariable("	x1322	",lowBound=0, cat= 'Integer')
x1323	=	p.LpVariable("	x1323	",lowBound=0, cat= 'Integer')
x1324	=	p.LpVariable("	x1324	",lowBound=0, cat= 'Integer')
x1325	=	p.LpVariable("	x1325	",lowBound=0, cat= 'Integer')
x1326	=	p.LpVariable("	x1326	",lowBound=0, cat= 'Integer')
x1327	=	p.LpVariable("	x1327	",lowBound=0, cat= 'Integer')
x1328	=	p.LpVariable("	x1328	",lowBound=0, cat= 'Integer')
x1329	=	p.LpVariable("	x1329	",lowBound=0, cat= 'Integer')
x1330	=	p.LpVariable("	x1330	",lowBound=0, cat= 'Integer')
x1331	=	p.LpVariable("	x1331	",lowBound=0, cat= 'Integer')
x1332	=	p.LpVariable("	x1332	",lowBound=0, cat= 'Integer')
x1333	=	p.LpVariable("	x1333	",lowBound=0, cat= 'Integer')
x1334	=	p.LpVariable("	x1334	",lowBound=0, cat= 'Integer')
x1335	=	p.LpVariable("	x1335	",lowBound=0, cat= 'Integer')
x1336	=	p.LpVariable("	x1336	",lowBound=0, cat= 'Integer')
x1337	=	p.LpVariable("	x1337	",lowBound=0, cat= 'Integer')
x1338	=	p.LpVariable("	x1338	",lowBound=0, cat= 'Integer')
x1339	=	p.LpVariable("	x1339	",lowBound=0, cat= 'Integer')
x1340	=	p.LpVariable("	x1340	",lowBound=0, cat= 'Integer')
x1341	=	p.LpVariable("	x1341	",lowBound=0, cat= 'Integer')
x1342	=	p.LpVariable("	x1342	",lowBound=0, cat= 'Integer')
x1343	=	p.LpVariable("	x1343	",lowBound=0, cat= 'Integer')
x1344	=	p.LpVariable("	x1344	",lowBound=0, cat= 'Integer')
x1345	=	p.LpVariable("	x1345	",lowBound=0, cat= 'Integer')
x1346	=	p.LpVariable("	x1346	",lowBound=0, cat= 'Integer')
x1347	=	p.LpVariable("	x1347	",lowBound=0, cat= 'Integer')
x1348	=	p.LpVariable("	x1348	",lowBound=0, cat= 'Integer')
x1349	=	p.LpVariable("	x1349	",lowBound=0, cat= 'Integer')
x1350	=	p.LpVariable("	x1350	",lowBound=0, cat= 'Integer')
x1351	=	p.LpVariable("	x1351	",lowBound=0, cat= 'Integer')
x1352	=	p.LpVariable("	x1352	",lowBound=0, cat= 'Integer')
x1353	=	p.LpVariable("	x1353	",lowBound=0, cat= 'Integer')
x1354	=	p.LpVariable("	x1354	",lowBound=0, cat= 'Integer')
x1355	=	p.LpVariable("	x1355	",lowBound=0, cat= 'Integer')
x1356	=	p.LpVariable("	x1356	",lowBound=0, cat= 'Integer')
x1357	=	p.LpVariable("	x1357	",lowBound=0, cat= 'Integer')
x1358	=	p.LpVariable("	x1358	",lowBound=0, cat= 'Integer')
x1359	=	p.LpVariable("	x1359	",lowBound=0, cat= 'Integer')
x1360	=	p.LpVariable("	x1360	",lowBound=0, cat= 'Integer')
x1361	=	p.LpVariable("	x1361	",lowBound=0, cat= 'Integer')
x1362	=	p.LpVariable("	x1362	",lowBound=0, cat= 'Integer')
x1363	=	p.LpVariable("	x1363	",lowBound=0, cat= 'Integer')
x1364	=	p.LpVariable("	x1364	",lowBound=0, cat= 'Integer')
x1365	=	p.LpVariable("	x1365	",lowBound=0, cat= 'Integer')
x1366	=	p.LpVariable("	x1366	",lowBound=0, cat= 'Integer')
x1367	=	p.LpVariable("	x1367	",lowBound=0, cat= 'Integer')
x1368	=	p.LpVariable("	x1368	",lowBound=0, cat= 'Integer')
x1369	=	p.LpVariable("	x1369	",lowBound=0, cat= 'Integer')
x1370	=	p.LpVariable("	x1370	",lowBound=0, cat= 'Integer')
x1371	=	p.LpVariable("	x1371	",lowBound=0, cat= 'Integer')
x1372	=	p.LpVariable("	x1372	",lowBound=0, cat= 'Integer')
x1373	=	p.LpVariable("	x1373	",lowBound=0, cat= 'Integer')
x1374	=	p.LpVariable("	x1374	",lowBound=0, cat= 'Integer')
x1375	=	p.LpVariable("	x1375	",lowBound=0, cat= 'Integer')
x1376	=	p.LpVariable("	x1376	",lowBound=0, cat= 'Integer')
x1377	=	p.LpVariable("	x1377	",lowBound=0, cat= 'Integer')
x1378	=	p.LpVariable("	x1378	",lowBound=0, cat= 'Integer')
x1379	=	p.LpVariable("	x1379	",lowBound=0, cat= 'Integer')
x1380	=	p.LpVariable("	x1380	",lowBound=0, cat= 'Integer')
x1381	=	p.LpVariable("	x1381	",lowBound=0, cat= 'Integer')
x1382	=	p.LpVariable("	x1382	",lowBound=0, cat= 'Integer')
x1383	=	p.LpVariable("	x1383	",lowBound=0, cat= 'Integer')
x1384	=	p.LpVariable("	x1384	",lowBound=0, cat= 'Integer')
x1385	=	p.LpVariable("	x1385	",lowBound=0, cat= 'Integer')
x1386	=	p.LpVariable("	x1386	",lowBound=0, cat= 'Integer')
x1387	=	p.LpVariable("	x1387	",lowBound=0, cat= 'Integer')
x1388	=	p.LpVariable("	x1388	",lowBound=0, cat= 'Integer')
x1389	=	p.LpVariable("	x1389	",lowBound=0, cat= 'Integer')
x1390	=	p.LpVariable("	x1390	",lowBound=0, cat= 'Integer')
x1391	=	p.LpVariable("	x1391	",lowBound=0, cat= 'Integer')
x1392	=	p.LpVariable("	x1392	",lowBound=0, cat= 'Integer')
x1393	=	p.LpVariable("	x1393	",lowBound=0, cat= 'Integer')
x1394	=	p.LpVariable("	x1394	",lowBound=0, cat= 'Integer')
x1395	=	p.LpVariable("	x1395	",lowBound=0, cat= 'Integer')
x1396	=	p.LpVariable("	x1396	",lowBound=0, cat= 'Integer')
x1397	=	p.LpVariable("	x1397	",lowBound=0, cat= 'Integer')
x1398	=	p.LpVariable("	x1398	",lowBound=0, cat= 'Integer')
x1399	=	p.LpVariable("	x1399	",lowBound=0, cat= 'Integer')
x1400	=	p.LpVariable("	x1400	",lowBound=0, cat= 'Integer')
x1401	=	p.LpVariable("	x1401	",lowBound=0, cat= 'Integer')
x1402	=	p.LpVariable("	x1402	",lowBound=0, cat= 'Integer')
x1403	=	p.LpVariable("	x1403	",lowBound=0, cat= 'Integer')
x1404	=	p.LpVariable("	x1404	",lowBound=0, cat= 'Integer')
x1405	=	p.LpVariable("	x1405	",lowBound=0, cat= 'Integer')
x1406	=	p.LpVariable("	x1406	",lowBound=0, cat= 'Integer')
x1407	=	p.LpVariable("	x1407	",lowBound=0, cat= 'Integer')
x1408	=	p.LpVariable("	x1408	",lowBound=0, cat= 'Integer')
x1409	=	p.LpVariable("	x1409	",lowBound=0, cat= 'Integer')
x1410	=	p.LpVariable("	x1410	",lowBound=0, cat= 'Integer')
x1411	=	p.LpVariable("	x1411	",lowBound=0, cat= 'Integer')
x1412	=	p.LpVariable("	x1412	",lowBound=0, cat= 'Integer')
x1413	=	p.LpVariable("	x1413	",lowBound=0, cat= 'Integer')
x1414	=	p.LpVariable("	x1414	",lowBound=0, cat= 'Integer')
x1415	=	p.LpVariable("	x1415	",lowBound=0, cat= 'Integer')
x1416	=	p.LpVariable("	x1416	",lowBound=0, cat= 'Integer')
x1417	=	p.LpVariable("	x1417	",lowBound=0, cat= 'Integer')
x1418	=	p.LpVariable("	x1418	",lowBound=0, cat= 'Integer')
x1419	=	p.LpVariable("	x1419	",lowBound=0, cat= 'Integer')
x1420	=	p.LpVariable("	x1420	",lowBound=0, cat= 'Integer')
x1421	=	p.LpVariable("	x1421	",lowBound=0, cat= 'Integer')
x1422	=	p.LpVariable("	x1422	",lowBound=0, cat= 'Integer')
x1423	=	p.LpVariable("	x1423	",lowBound=0, cat= 'Integer')
x1424	=	p.LpVariable("	x1424	",lowBound=0, cat= 'Integer')
x1425	=	p.LpVariable("	x1425	",lowBound=0, cat= 'Integer')
x1426	=	p.LpVariable("	x1426	",lowBound=0, cat= 'Integer')
x1427	=	p.LpVariable("	x1427	",lowBound=0, cat= 'Integer')
x1428	=	p.LpVariable("	x1428	",lowBound=0, cat= 'Integer')
x1429	=	p.LpVariable("	x1429	",lowBound=0, cat= 'Integer')
x1430	=	p.LpVariable("	x1430	",lowBound=0, cat= 'Integer')
x1431	=	p.LpVariable("	x1431	",lowBound=0, cat= 'Integer')
x1432	=	p.LpVariable("	x1432	",lowBound=0, cat= 'Integer')
x1433	=	p.LpVariable("	x1433	",lowBound=0, cat= 'Integer')
x1434	=	p.LpVariable("	x1434	",lowBound=0, cat= 'Integer')
x1435	=	p.LpVariable("	x1435	",lowBound=0, cat= 'Integer')
x1436	=	p.LpVariable("	x1436	",lowBound=0, cat= 'Integer')
x1437	=	p.LpVariable("	x1437	",lowBound=0, cat= 'Integer')
x1438	=	p.LpVariable("	x1438	",lowBound=0, cat= 'Integer')
x1439	=	p.LpVariable("	x1439	",lowBound=0, cat= 'Integer')
x1440	=	p.LpVariable("	x1440	",lowBound=0, cat= 'Integer')
x1441	=	p.LpVariable("	x1441	",lowBound=0, cat= 'Integer')
x1442	=	p.LpVariable("	x1442	",lowBound=0, cat= 'Integer')
x1443	=	p.LpVariable("	x1443	",lowBound=0, cat= 'Integer')
x1444	=	p.LpVariable("	x1444	",lowBound=0, cat= 'Integer')
x1445	=	p.LpVariable("	x1445	",lowBound=0, cat= 'Integer')
x1446	=	p.LpVariable("	x1446	",lowBound=0, cat= 'Integer')
x1447	=	p.LpVariable("	x1447	",lowBound=0, cat= 'Integer')
x1448	=	p.LpVariable("	x1448	",lowBound=0, cat= 'Integer')
x1449	=	p.LpVariable("	x1449	",lowBound=0, cat= 'Integer')
x1450	=	p.LpVariable("	x1450	",lowBound=0, cat= 'Integer')
x1451	=	p.LpVariable("	x1451	",lowBound=0, cat= 'Integer')
x1452	=	p.LpVariable("	x1452	",lowBound=0, cat= 'Integer')
x1453	=	p.LpVariable("	x1453	",lowBound=0, cat= 'Integer')
x1454	=	p.LpVariable("	x1454	",lowBound=0, cat= 'Integer')
x1455	=	p.LpVariable("	x1455	",lowBound=0, cat= 'Integer')
x1456	=	p.LpVariable("	x1456	",lowBound=0, cat= 'Integer')
x1457	=	p.LpVariable("	x1457	",lowBound=0, cat= 'Integer')
x1458	=	p.LpVariable("	x1458	",lowBound=0, cat= 'Integer')
x1459	=	p.LpVariable("	x1459	",lowBound=0, cat= 'Integer')
x1460	=	p.LpVariable("	x1460	",lowBound=0, cat= 'Integer')
x1461	=	p.LpVariable("	x1461	",lowBound=0, cat= 'Integer')
x1462	=	p.LpVariable("	x1462	",lowBound=0, cat= 'Integer')
x1463	=	p.LpVariable("	x1463	",lowBound=0, cat= 'Integer')
x1464	=	p.LpVariable("	x1464	",lowBound=0, cat= 'Integer')
x1465	=	p.LpVariable("	x1465	",lowBound=0, cat= 'Integer')
x1466	=	p.LpVariable("	x1466	",lowBound=0, cat= 'Integer')
x1467	=	p.LpVariable("	x1467	",lowBound=0, cat= 'Integer')
x1468	=	p.LpVariable("	x1468	",lowBound=0, cat= 'Integer')
x1469	=	p.LpVariable("	x1469	",lowBound=0, cat= 'Integer')
x1470	=	p.LpVariable("	x1470	",lowBound=0, cat= 'Integer')
x1471	=	p.LpVariable("	x1471	",lowBound=0, cat= 'Integer')
x1472	=	p.LpVariable("	x1472	",lowBound=0, cat= 'Integer')
x1473	=	p.LpVariable("	x1473	",lowBound=0, cat= 'Integer')
x1474	=	p.LpVariable("	x1474	",lowBound=0, cat= 'Integer')
x1475	=	p.LpVariable("	x1475	",lowBound=0, cat= 'Integer')
x1476	=	p.LpVariable("	x1476	",lowBound=0, cat= 'Integer')
x1477	=	p.LpVariable("	x1477	",lowBound=0, cat= 'Integer')
x1478	=	p.LpVariable("	x1478	",lowBound=0, cat= 'Integer')
x1479	=	p.LpVariable("	x1479	",lowBound=0, cat= 'Integer')
x1480	=	p.LpVariable("	x1480	",lowBound=0, cat= 'Integer')
x1481	=	p.LpVariable("	x1481	",lowBound=0, cat= 'Integer')
x1482	=	p.LpVariable("	x1482	",lowBound=0, cat= 'Integer')
x1483	=	p.LpVariable("	x1483	",lowBound=0, cat= 'Integer')
x1484	=	p.LpVariable("	x1484	",lowBound=0, cat= 'Integer')
x1485	=	p.LpVariable("	x1485	",lowBound=0, cat= 'Integer')
x1486	=	p.LpVariable("	x1486	",lowBound=0, cat= 'Integer')
x1487	=	p.LpVariable("	x1487	",lowBound=0, cat= 'Integer')
x1488	=	p.LpVariable("	x1488	",lowBound=0, cat= 'Integer')
x1489	=	p.LpVariable("	x1489	",lowBound=0, cat= 'Integer')
x1490	=	p.LpVariable("	x1490	",lowBound=0, cat= 'Integer')
x1491	=	p.LpVariable("	x1491	",lowBound=0, cat= 'Integer')
x1492	=	p.LpVariable("	x1492	",lowBound=0, cat= 'Integer')
x1493	=	p.LpVariable("	x1493	",lowBound=0, cat= 'Integer')
x1494	=	p.LpVariable("	x1494	",lowBound=0, cat= 'Integer')
x1495	=	p.LpVariable("	x1495	",lowBound=0, cat= 'Integer')
x1496	=	p.LpVariable("	x1496	",lowBound=0, cat= 'Integer')
x1497	=	p.LpVariable("	x1497	",lowBound=0, cat= 'Integer')
x1498	=	p.LpVariable("	x1498	",lowBound=0, cat= 'Integer')
x1499	=	p.LpVariable("	x1499	",lowBound=0, cat= 'Integer')
x1500	=	p.LpVariable("	x1500	",lowBound=0, cat= 'Integer')
x1501	=	p.LpVariable("	x1501	",lowBound=0, cat= 'Integer')
x1502	=	p.LpVariable("	x1502	",lowBound=0, cat= 'Integer')
x1503	=	p.LpVariable("	x1503	",lowBound=0, cat= 'Integer')
x1504	=	p.LpVariable("	x1504	",lowBound=0, cat= 'Integer')
x1505	=	p.LpVariable("	x1505	",lowBound=0, cat= 'Integer')
x1506	=	p.LpVariable("	x1506	",lowBound=0, cat= 'Integer')
x1507	=	p.LpVariable("	x1507	",lowBound=0, cat= 'Integer')
x1508	=	p.LpVariable("	x1508	",lowBound=0, cat= 'Integer')
x1509	=	p.LpVariable("	x1509	",lowBound=0, cat= 'Integer')
x1510	=	p.LpVariable("	x1510	",lowBound=0, cat= 'Integer')
x1511	=	p.LpVariable("	x1511	",lowBound=0, cat= 'Integer')
x1512	=	p.LpVariable("	x1512	",lowBound=0, cat= 'Integer')
x1513	=	p.LpVariable("	x1513	",lowBound=0, cat= 'Integer')
x1514	=	p.LpVariable("	x1514	",lowBound=0, cat= 'Integer')
x1515	=	p.LpVariable("	x1515	",lowBound=0, cat= 'Integer')
x1516	=	p.LpVariable("	x1516	",lowBound=0, cat= 'Integer')
x1517	=	p.LpVariable("	x1517	",lowBound=0, cat= 'Integer')
x1518	=	p.LpVariable("	x1518	",lowBound=0, cat= 'Integer')
x1519	=	p.LpVariable("	x1519	",lowBound=0, cat= 'Integer')
x1520	=	p.LpVariable("	x1520	",lowBound=0, cat= 'Integer')
x1521	=	p.LpVariable("	x1521	",lowBound=0, cat= 'Integer')
x1522	=	p.LpVariable("	x1522	",lowBound=0, cat= 'Integer')
x1523	=	p.LpVariable("	x1523	",lowBound=0, cat= 'Integer')
x1524	=	p.LpVariable("	x1524	",lowBound=0, cat= 'Integer')
x1525	=	p.LpVariable("	x1525	",lowBound=0, cat= 'Integer')
x1526	=	p.LpVariable("	x1526	",lowBound=0, cat= 'Integer')
x1527	=	p.LpVariable("	x1527	",lowBound=0, cat= 'Integer')
x1528	=	p.LpVariable("	x1528	",lowBound=0, cat= 'Integer')
x1529	=	p.LpVariable("	x1529	",lowBound=0, cat= 'Integer')
x1530	=	p.LpVariable("	x1530	",lowBound=0, cat= 'Integer')
x1531	=	p.LpVariable("	x1531	",lowBound=0, cat= 'Integer')
x1532	=	p.LpVariable("	x1532	",lowBound=0, cat= 'Integer')
x1533	=	p.LpVariable("	x1533	",lowBound=0, cat= 'Integer')
x1534	=	p.LpVariable("	x1534	",lowBound=0, cat= 'Integer')
x1535	=	p.LpVariable("	x1535	",lowBound=0, cat= 'Integer')
x1536	=	p.LpVariable("	x1536	",lowBound=0, cat= 'Integer')
x1537	=	p.LpVariable("	x1537	",lowBound=0, cat= 'Integer')
x1538	=	p.LpVariable("	x1538	",lowBound=0, cat= 'Integer')
x1539	=	p.LpVariable("	x1539	",lowBound=0, cat= 'Integer')
x1540	=	p.LpVariable("	x1540	",lowBound=0, cat= 'Integer')
x1541	=	p.LpVariable("	x1541	",lowBound=0, cat= 'Integer')
x1542	=	p.LpVariable("	x1542	",lowBound=0, cat= 'Integer')
x1543	=	p.LpVariable("	x1543	",lowBound=0, cat= 'Integer')
x1544	=	p.LpVariable("	x1544	",lowBound=0, cat= 'Integer')
x1545	=	p.LpVariable("	x1545	",lowBound=0, cat= 'Integer')
x1546	=	p.LpVariable("	x1546	",lowBound=0, cat= 'Integer')
x1547	=	p.LpVariable("	x1547	",lowBound=0, cat= 'Integer')
x1548	=	p.LpVariable("	x1548	",lowBound=0, cat= 'Integer')
x1549	=	p.LpVariable("	x1549	",lowBound=0, cat= 'Integer')
x1550	=	p.LpVariable("	x1550	",lowBound=0, cat= 'Integer')
x1551	=	p.LpVariable("	x1551	",lowBound=0, cat= 'Integer')
x1552	=	p.LpVariable("	x1552	",lowBound=0, cat= 'Integer')
x1553	=	p.LpVariable("	x1553	",lowBound=0, cat= 'Integer')
x1554	=	p.LpVariable("	x1554	",lowBound=0, cat= 'Integer')
x1555	=	p.LpVariable("	x1555	",lowBound=0, cat= 'Integer')
x1556	=	p.LpVariable("	x1556	",lowBound=0, cat= 'Integer')
x1557	=	p.LpVariable("	x1557	",lowBound=0, cat= 'Integer')
x1558	=	p.LpVariable("	x1558	",lowBound=0, cat= 'Integer')
x1559	=	p.LpVariable("	x1559	",lowBound=0, cat= 'Integer')
x1560	=	p.LpVariable("	x1560	",lowBound=0, cat= 'Integer')
x1561	=	p.LpVariable("	x1561	",lowBound=0, cat= 'Integer')
x1562	=	p.LpVariable("	x1562	",lowBound=0, cat= 'Integer')
x1563	=	p.LpVariable("	x1563	",lowBound=0, cat= 'Integer')
x1564	=	p.LpVariable("	x1564	",lowBound=0, cat= 'Integer')
x1565	=	p.LpVariable("	x1565	",lowBound=0, cat= 'Integer')
x1566	=	p.LpVariable("	x1566	",lowBound=0, cat= 'Integer')
x1567	=	p.LpVariable("	x1567	",lowBound=0, cat= 'Integer')
x1568	=	p.LpVariable("	x1568	",lowBound=0, cat= 'Integer')
x1569	=	p.LpVariable("	x1569	",lowBound=0, cat= 'Integer')
x1570	=	p.LpVariable("	x1570	",lowBound=0, cat= 'Integer')
x1571	=	p.LpVariable("	x1571	",lowBound=0, cat= 'Integer')
x1572	=	p.LpVariable("	x1572	",lowBound=0, cat= 'Integer')
x1573	=	p.LpVariable("	x1573	",lowBound=0, cat= 'Integer')
x1574	=	p.LpVariable("	x1574	",lowBound=0, cat= 'Integer')
x1575	=	p.LpVariable("	x1575	",lowBound=0, cat= 'Integer')
x1576	=	p.LpVariable("	x1576	",lowBound=0, cat= 'Integer')
x1577	=	p.LpVariable("	x1577	",lowBound=0, cat= 'Integer')
x1578	=	p.LpVariable("	x1578	",lowBound=0, cat= 'Integer')
x1579	=	p.LpVariable("	x1579	",lowBound=0, cat= 'Integer')
x1580	=	p.LpVariable("	x1580	",lowBound=0, cat= 'Integer')
x1581	=	p.LpVariable("	x1581	",lowBound=0, cat= 'Integer')
x1582	=	p.LpVariable("	x1582	",lowBound=0, cat= 'Integer')
x1583	=	p.LpVariable("	x1583	",lowBound=0, cat= 'Integer')
x1584	=	p.LpVariable("	x1584	",lowBound=0, cat= 'Integer')
x1585	=	p.LpVariable("	x1585	",lowBound=0, cat= 'Integer')
x1586	=	p.LpVariable("	x1586	",lowBound=0, cat= 'Integer')
x1587	=	p.LpVariable("	x1587	",lowBound=0, cat= 'Integer')
x1588	=	p.LpVariable("	x1588	",lowBound=0, cat= 'Integer')
x1589	=	p.LpVariable("	x1589	",lowBound=0, cat= 'Integer')
x1590	=	p.LpVariable("	x1590	",lowBound=0, cat= 'Integer')
x1591	=	p.LpVariable("	x1591	",lowBound=0, cat= 'Integer')
x1592	=	p.LpVariable("	x1592	",lowBound=0, cat= 'Integer')
x1593	=	p.LpVariable("	x1593	",lowBound=0, cat= 'Integer')
x1594	=	p.LpVariable("	x1594	",lowBound=0, cat= 'Integer')
x1595	=	p.LpVariable("	x1595	",lowBound=0, cat= 'Integer')
x1596	=	p.LpVariable("	x1596	",lowBound=0, cat= 'Integer')
x1597	=	p.LpVariable("	x1597	",lowBound=0, cat= 'Integer')
x1598	=	p.LpVariable("	x1598	",lowBound=0, cat= 'Integer')
x1599	=	p.LpVariable("	x1599	",lowBound=0, cat= 'Integer')
x1600	=	p.LpVariable("	x1600	",lowBound=0, cat= 'Integer')
x1601	=	p.LpVariable("	x1601	",lowBound=0, cat= 'Integer')
x1602	=	p.LpVariable("	x1602	",lowBound=0, cat= 'Integer')
x1603	=	p.LpVariable("	x1603	",lowBound=0, cat= 'Integer')
x1604	=	p.LpVariable("	x1604	",lowBound=0, cat= 'Integer')
x1605	=	p.LpVariable("	x1605	",lowBound=0, cat= 'Integer')
x1606	=	p.LpVariable("	x1606	",lowBound=0, cat= 'Integer')
x1607	=	p.LpVariable("	x1607	",lowBound=0, cat= 'Integer')
x1608	=	p.LpVariable("	x1608	",lowBound=0, cat= 'Integer')
x1609	=	p.LpVariable("	x1609	",lowBound=0, cat= 'Integer')
x1610	=	p.LpVariable("	x1610	",lowBound=0, cat= 'Integer')
x1611	=	p.LpVariable("	x1611	",lowBound=0, cat= 'Integer')
x1612	=	p.LpVariable("	x1612	",lowBound=0, cat= 'Integer')
x1613	=	p.LpVariable("	x1613	",lowBound=0, cat= 'Integer')
x1614	=	p.LpVariable("	x1614	",lowBound=0, cat= 'Integer')
x1615	=	p.LpVariable("	x1615	",lowBound=0, cat= 'Integer')
x1616	=	p.LpVariable("	x1616	",lowBound=0, cat= 'Integer')
x1617	=	p.LpVariable("	x1617	",lowBound=0, cat= 'Integer')
x1618	=	p.LpVariable("	x1618	",lowBound=0, cat= 'Integer')
x1619	=	p.LpVariable("	x1619	",lowBound=0, cat= 'Integer')
x1620	=	p.LpVariable("	x1620	",lowBound=0, cat= 'Integer')
x1621	=	p.LpVariable("	x1621	",lowBound=0, cat= 'Integer')
x1622	=	p.LpVariable("	x1622	",lowBound=0, cat= 'Integer')
x1623	=	p.LpVariable("	x1623	",lowBound=0, cat= 'Integer')
x1624	=	p.LpVariable("	x1624	",lowBound=0, cat= 'Integer')
x1625	=	p.LpVariable("	x1625	",lowBound=0, cat= 'Integer')
x1626	=	p.LpVariable("	x1626	",lowBound=0, cat= 'Integer')
x1627	=	p.LpVariable("	x1627	",lowBound=0, cat= 'Integer')
x1628	=	p.LpVariable("	x1628	",lowBound=0, cat= 'Integer')
x1629	=	p.LpVariable("	x1629	",lowBound=0, cat= 'Integer')
x1630	=	p.LpVariable("	x1630	",lowBound=0, cat= 'Integer')
x1631	=	p.LpVariable("	x1631	",lowBound=0, cat= 'Integer')
x1632	=	p.LpVariable("	x1632	",lowBound=0, cat= 'Integer')
x1633	=	p.LpVariable("	x1633	",lowBound=0, cat= 'Integer')
x1634	=	p.LpVariable("	x1634	",lowBound=0, cat= 'Integer')
x1635	=	p.LpVariable("	x1635	",lowBound=0, cat= 'Integer')
x1636	=	p.LpVariable("	x1636	",lowBound=0, cat= 'Integer')
x1637	=	p.LpVariable("	x1637	",lowBound=0, cat= 'Integer')
x1638	=	p.LpVariable("	x1638	",lowBound=0, cat= 'Integer')
x1639	=	p.LpVariable("	x1639	",lowBound=0, cat= 'Integer')
x1640	=	p.LpVariable("	x1640	",lowBound=0, cat= 'Integer')
x1641	=	p.LpVariable("	x1641	",lowBound=0, cat= 'Integer')
x1642	=	p.LpVariable("	x1642	",lowBound=0, cat= 'Integer')
x1643	=	p.LpVariable("	x1643	",lowBound=0, cat= 'Integer')
x1644	=	p.LpVariable("	x1644	",lowBound=0, cat= 'Integer')
x1645	=	p.LpVariable("	x1645	",lowBound=0, cat= 'Integer')
x1646	=	p.LpVariable("	x1646	",lowBound=0, cat= 'Integer')
x1647	=	p.LpVariable("	x1647	",lowBound=0, cat= 'Integer')
x1648	=	p.LpVariable("	x1648	",lowBound=0, cat= 'Integer')
x1649	=	p.LpVariable("	x1649	",lowBound=0, cat= 'Integer')
x1650	=	p.LpVariable("	x1650	",lowBound=0, cat= 'Integer')
x1651	=	p.LpVariable("	x1651	",lowBound=0, cat= 'Integer')
x1652	=	p.LpVariable("	x1652	",lowBound=0, cat= 'Integer')
x1653	=	p.LpVariable("	x1653	",lowBound=0, cat= 'Integer')
x1654	=	p.LpVariable("	x1654	",lowBound=0, cat= 'Integer')
x1655	=	p.LpVariable("	x1655	",lowBound=0, cat= 'Integer')
x1656	=	p.LpVariable("	x1656	",lowBound=0, cat= 'Integer')
x1657	=	p.LpVariable("	x1657	",lowBound=0, cat= 'Integer')
x1658	=	p.LpVariable("	x1658	",lowBound=0, cat= 'Integer')
x1659	=	p.LpVariable("	x1659	",lowBound=0, cat= 'Integer')
x1660	=	p.LpVariable("	x1660	",lowBound=0, cat= 'Integer')
x1661	=	p.LpVariable("	x1661	",lowBound=0, cat= 'Integer')
x1662	=	p.LpVariable("	x1662	",lowBound=0, cat= 'Integer')
x1663	=	p.LpVariable("	x1663	",lowBound=0, cat= 'Integer')
x1664	=	p.LpVariable("	x1664	",lowBound=0, cat= 'Integer')
x1665	=	p.LpVariable("	x1665	",lowBound=0, cat= 'Integer')
x1666	=	p.LpVariable("	x1666	",lowBound=0, cat= 'Integer')
x1667	=	p.LpVariable("	x1667	",lowBound=0, cat= 'Integer')
x1668	=	p.LpVariable("	x1668	",lowBound=0, cat= 'Integer')
x1669	=	p.LpVariable("	x1669	",lowBound=0, cat= 'Integer')
x1670	=	p.LpVariable("	x1670	",lowBound=0, cat= 'Integer')
x1671	=	p.LpVariable("	x1671	",lowBound=0, cat= 'Integer')
x1672	=	p.LpVariable("	x1672	",lowBound=0, cat= 'Integer')
x1673	=	p.LpVariable("	x1673	",lowBound=0, cat= 'Integer')
x1674	=	p.LpVariable("	x1674	",lowBound=0, cat= 'Integer')
x1675	=	p.LpVariable("	x1675	",lowBound=0, cat= 'Integer')
x1676	=	p.LpVariable("	x1676	",lowBound=0, cat= 'Integer')
x1677	=	p.LpVariable("	x1677	",lowBound=0, cat= 'Integer')
x1678	=	p.LpVariable("	x1678	",lowBound=0, cat= 'Integer')
x1679	=	p.LpVariable("	x1679	",lowBound=0, cat= 'Integer')
x1680	=	p.LpVariable("	x1680	",lowBound=0, cat= 'Integer')
x1681	=	p.LpVariable("	x1681	",lowBound=0, cat= 'Integer')
x1682	=	p.LpVariable("	x1682	",lowBound=0, cat= 'Integer')
x1683	=	p.LpVariable("	x1683	",lowBound=0, cat= 'Integer')
x1684	=	p.LpVariable("	x1684	",lowBound=0, cat= 'Integer')
x1685	=	p.LpVariable("	x1685	",lowBound=0, cat= 'Integer')
x1686	=	p.LpVariable("	x1686	",lowBound=0, cat= 'Integer')
x1687	=	p.LpVariable("	x1687	",lowBound=0, cat= 'Integer')
x1688	=	p.LpVariable("	x1688	",lowBound=0, cat= 'Integer')
x1689	=	p.LpVariable("	x1689	",lowBound=0, cat= 'Integer')
x1690	=	p.LpVariable("	x1690	",lowBound=0, cat= 'Integer')
x1691	=	p.LpVariable("	x1691	",lowBound=0, cat= 'Integer')
x1692	=	p.LpVariable("	x1692	",lowBound=0, cat= 'Integer')
x1693	=	p.LpVariable("	x1693	",lowBound=0, cat= 'Integer')
x1694	=	p.LpVariable("	x1694	",lowBound=0, cat= 'Integer')
x1695	=	p.LpVariable("	x1695	",lowBound=0, cat= 'Integer')
x1696	=	p.LpVariable("	x1696	",lowBound=0, cat= 'Integer')
x1697	=	p.LpVariable("	x1697	",lowBound=0, cat= 'Integer')
x1698	=	p.LpVariable("	x1698	",lowBound=0, cat= 'Integer')
x1699	=	p.LpVariable("	x1699	",lowBound=0, cat= 'Integer')
x1700	=	p.LpVariable("	x1700	",lowBound=0, cat= 'Integer')
x1701	=	p.LpVariable("	x1701	",lowBound=0, cat= 'Integer')
x1702	=	p.LpVariable("	x1702	",lowBound=0, cat= 'Integer')
x1703	=	p.LpVariable("	x1703	",lowBound=0, cat= 'Integer')
x1704	=	p.LpVariable("	x1704	",lowBound=0, cat= 'Integer')
x1705	=	p.LpVariable("	x1705	",lowBound=0, cat= 'Integer')
x1706	=	p.LpVariable("	x1706	",lowBound=0, cat= 'Integer')
x1707	=	p.LpVariable("	x1707	",lowBound=0, cat= 'Integer')
x1708	=	p.LpVariable("	x1708	",lowBound=0, cat= 'Integer')
x1709	=	p.LpVariable("	x1709	",lowBound=0, cat= 'Integer')
x1710	=	p.LpVariable("	x1710	",lowBound=0, cat= 'Integer')
x1711	=	p.LpVariable("	x1711	",lowBound=0, cat= 'Integer')
x1712	=	p.LpVariable("	x1712	",lowBound=0, cat= 'Integer')
x1713	=	p.LpVariable("	x1713	",lowBound=0, cat= 'Integer')
x1714	=	p.LpVariable("	x1714	",lowBound=0, cat= 'Integer')
x1715	=	p.LpVariable("	x1715	",lowBound=0, cat= 'Integer')
x1716	=	p.LpVariable("	x1716	",lowBound=0, cat= 'Integer')
x1717	=	p.LpVariable("	x1717	",lowBound=0, cat= 'Integer')
x1718	=	p.LpVariable("	x1718	",lowBound=0, cat= 'Integer')
x1719	=	p.LpVariable("	x1719	",lowBound=0, cat= 'Integer')
x1720	=	p.LpVariable("	x1720	",lowBound=0, cat= 'Integer')
x1721	=	p.LpVariable("	x1721	",lowBound=0, cat= 'Integer')
x1722	=	p.LpVariable("	x1722	",lowBound=0, cat= 'Integer')
x1723	=	p.LpVariable("	x1723	",lowBound=0, cat= 'Integer')
x1724	=	p.LpVariable("	x1724	",lowBound=0, cat= 'Integer')
x1725	=	p.LpVariable("	x1725	",lowBound=0, cat= 'Integer')
x1726	=	p.LpVariable("	x1726	",lowBound=0, cat= 'Integer')
x1727	=	p.LpVariable("	x1727	",lowBound=0, cat= 'Integer')
x1728	=	p.LpVariable("	x1728	",lowBound=0, cat= 'Integer')
x1729	=	p.LpVariable("	x1729	",lowBound=0, cat= 'Integer')
x1730	=	p.LpVariable("	x1730	",lowBound=0, cat= 'Integer')
x1731	=	p.LpVariable("	x1731	",lowBound=0, cat= 'Integer')
x1732	=	p.LpVariable("	x1732	",lowBound=0, cat= 'Integer')
x1733	=	p.LpVariable("	x1733	",lowBound=0, cat= 'Integer')
x1734	=	p.LpVariable("	x1734	",lowBound=0, cat= 'Integer')
x1735	=	p.LpVariable("	x1735	",lowBound=0, cat= 'Integer')
x1736	=	p.LpVariable("	x1736	",lowBound=0, cat= 'Integer')
x1737	=	p.LpVariable("	x1737	",lowBound=0, cat= 'Integer')
x1738	=	p.LpVariable("	x1738	",lowBound=0, cat= 'Integer')
x1739	=	p.LpVariable("	x1739	",lowBound=0, cat= 'Integer')
x1740	=	p.LpVariable("	x1740	",lowBound=0, cat= 'Integer')
x1741	=	p.LpVariable("	x1741	",lowBound=0, cat= 'Integer')
x1742	=	p.LpVariable("	x1742	",lowBound=0, cat= 'Integer')
x1743	=	p.LpVariable("	x1743	",lowBound=0, cat= 'Integer')
x1744	=	p.LpVariable("	x1744	",lowBound=0, cat= 'Integer')
x1745	=	p.LpVariable("	x1745	",lowBound=0, cat= 'Integer')
x1746	=	p.LpVariable("	x1746	",lowBound=0, cat= 'Integer')
x1747	=	p.LpVariable("	x1747	",lowBound=0, cat= 'Integer')
x1748	=	p.LpVariable("	x1748	",lowBound=0, cat= 'Integer')
x1749	=	p.LpVariable("	x1749	",lowBound=0, cat= 'Integer')
x1750	=	p.LpVariable("	x1750	",lowBound=0, cat= 'Integer')
x1751	=	p.LpVariable("	x1751	",lowBound=0, cat= 'Integer')
x1752	=	p.LpVariable("	x1752	",lowBound=0, cat= 'Integer')
x1753	=	p.LpVariable("	x1753	",lowBound=0, cat= 'Integer')
x1754	=	p.LpVariable("	x1754	",lowBound=0, cat= 'Integer')
x1755	=	p.LpVariable("	x1755	",lowBound=0, cat= 'Integer')
x1756	=	p.LpVariable("	x1756	",lowBound=0, cat= 'Integer')
x1757	=	p.LpVariable("	x1757	",lowBound=0, cat= 'Integer')
x1758	=	p.LpVariable("	x1758	",lowBound=0, cat= 'Integer')
x1759	=	p.LpVariable("	x1759	",lowBound=0, cat= 'Integer')
x1760	=	p.LpVariable("	x1760	",lowBound=0, cat= 'Integer')
x1761	=	p.LpVariable("	x1761	",lowBound=0, cat= 'Integer')
x1762	=	p.LpVariable("	x1762	",lowBound=0, cat= 'Integer')
x1763	=	p.LpVariable("	x1763	",lowBound=0, cat= 'Integer')
x1764	=	p.LpVariable("	x1764	",lowBound=0, cat= 'Integer')
x1765	=	p.LpVariable("	x1765	",lowBound=0, cat= 'Integer')
x1766	=	p.LpVariable("	x1766	",lowBound=0, cat= 'Integer')
x1767	=	p.LpVariable("	x1767	",lowBound=0, cat= 'Integer')
x1768	=	p.LpVariable("	x1768	",lowBound=0, cat= 'Integer')
x1769	=	p.LpVariable("	x1769	",lowBound=0, cat= 'Integer')
x1770	=	p.LpVariable("	x1770	",lowBound=0, cat= 'Integer')
x1771	=	p.LpVariable("	x1771	",lowBound=0, cat= 'Integer')
x1772	=	p.LpVariable("	x1772	",lowBound=0, cat= 'Integer')
x1773	=	p.LpVariable("	x1773	",lowBound=0, cat= 'Integer')
x1774	=	p.LpVariable("	x1774	",lowBound=0, cat= 'Integer')
x1775	=	p.LpVariable("	x1775	",lowBound=0, cat= 'Integer')
x1776	=	p.LpVariable("	x1776	",lowBound=0, cat= 'Integer')
x1777	=	p.LpVariable("	x1777	",lowBound=0, cat= 'Integer')
x1778	=	p.LpVariable("	x1778	",lowBound=0, cat= 'Integer')
x1779	=	p.LpVariable("	x1779	",lowBound=0, cat= 'Integer')
x1780	=	p.LpVariable("	x1780	",lowBound=0, cat= 'Integer')
x1781	=	p.LpVariable("	x1781	",lowBound=0, cat= 'Integer')
x1782	=	p.LpVariable("	x1782	",lowBound=0, cat= 'Integer')
x1783	=	p.LpVariable("	x1783	",lowBound=0, cat= 'Integer')
x1784	=	p.LpVariable("	x1784	",lowBound=0, cat= 'Integer')
x1785	=	p.LpVariable("	x1785	",lowBound=0, cat= 'Integer')
x1786	=	p.LpVariable("	x1786	",lowBound=0, cat= 'Integer')
x1787	=	p.LpVariable("	x1787	",lowBound=0, cat= 'Integer')
x1788	=	p.LpVariable("	x1788	",lowBound=0, cat= 'Integer')
x1789	=	p.LpVariable("	x1789	",lowBound=0, cat= 'Integer')
x1790	=	p.LpVariable("	x1790	",lowBound=0, cat= 'Integer')
x1791	=	p.LpVariable("	x1791	",lowBound=0, cat= 'Integer')
x1792	=	p.LpVariable("	x1792	",lowBound=0, cat= 'Integer')
x1793	=	p.LpVariable("	x1793	",lowBound=0, cat= 'Integer')
x1794	=	p.LpVariable("	x1794	",lowBound=0, cat= 'Integer')
x1795	=	p.LpVariable("	x1795	",lowBound=0, cat= 'Integer')
x1796	=	p.LpVariable("	x1796	",lowBound=0, cat= 'Integer')
x1797	=	p.LpVariable("	x1797	",lowBound=0, cat= 'Integer')
x1798	=	p.LpVariable("	x1798	",lowBound=0, cat= 'Integer')
x1799	=	p.LpVariable("	x1799	",lowBound=0, cat= 'Integer')
x1800	=	p.LpVariable("	x1800	",lowBound=0, cat= 'Integer')
x1801	=	p.LpVariable("	x1801	",lowBound=0, cat= 'Integer')
x1802	=	p.LpVariable("	x1802	",lowBound=0, cat= 'Integer')
x1803	=	p.LpVariable("	x1803	",lowBound=0, cat= 'Integer')
x1804	=	p.LpVariable("	x1804	",lowBound=0, cat= 'Integer')
x1805	=	p.LpVariable("	x1805	",lowBound=0, cat= 'Integer')
x1806	=	p.LpVariable("	x1806	",lowBound=0, cat= 'Integer')
x1807	=	p.LpVariable("	x1807	",lowBound=0, cat= 'Integer')
x1808	=	p.LpVariable("	x1808	",lowBound=0, cat= 'Integer')
x1809	=	p.LpVariable("	x1809	",lowBound=0, cat= 'Integer')
x1810	=	p.LpVariable("	x1810	",lowBound=0, cat= 'Integer')
x1811	=	p.LpVariable("	x1811	",lowBound=0, cat= 'Integer')
x1812	=	p.LpVariable("	x1812	",lowBound=0, cat= 'Integer')
x1813	=	p.LpVariable("	x1813	",lowBound=0, cat= 'Integer')
x1814	=	p.LpVariable("	x1814	",lowBound=0, cat= 'Integer')
x1815	=	p.LpVariable("	x1815	",lowBound=0, cat= 'Integer')
x1816	=	p.LpVariable("	x1816	",lowBound=0, cat= 'Integer')
x1817	=	p.LpVariable("	x1817	",lowBound=0, cat= 'Integer')
x1818	=	p.LpVariable("	x1818	",lowBound=0, cat= 'Integer')
x1819	=	p.LpVariable("	x1819	",lowBound=0, cat= 'Integer')
x1820	=	p.LpVariable("	x1820	",lowBound=0, cat= 'Integer')
x1821	=	p.LpVariable("	x1821	",lowBound=0, cat= 'Integer')
x1822	=	p.LpVariable("	x1822	",lowBound=0, cat= 'Integer')
x1823	=	p.LpVariable("	x1823	",lowBound=0, cat= 'Integer')
x1824	=	p.LpVariable("	x1824	",lowBound=0, cat= 'Integer')
x1825	=	p.LpVariable("	x1825	",lowBound=0, cat= 'Integer')
x1826	=	p.LpVariable("	x1826	",lowBound=0, cat= 'Integer')
x1827	=	p.LpVariable("	x1827	",lowBound=0, cat= 'Integer')
x1828	=	p.LpVariable("	x1828	",lowBound=0, cat= 'Integer')
x1829	=	p.LpVariable("	x1829	",lowBound=0, cat= 'Integer')
x1830	=	p.LpVariable("	x1830	",lowBound=0, cat= 'Integer')
x1831	=	p.LpVariable("	x1831	",lowBound=0, cat= 'Integer')
x1832	=	p.LpVariable("	x1832	",lowBound=0, cat= 'Integer')
x1833	=	p.LpVariable("	x1833	",lowBound=0, cat= 'Integer')
x1834	=	p.LpVariable("	x1834	",lowBound=0, cat= 'Integer')
x1835	=	p.LpVariable("	x1835	",lowBound=0, cat= 'Integer')
x1836	=	p.LpVariable("	x1836	",lowBound=0, cat= 'Integer')
x1837	=	p.LpVariable("	x1837	",lowBound=0, cat= 'Integer')
x1838	=	p.LpVariable("	x1838	",lowBound=0, cat= 'Integer')
x1839	=	p.LpVariable("	x1839	",lowBound=0, cat= 'Integer')
x1840	=	p.LpVariable("	x1840	",lowBound=0, cat= 'Integer')
x1841	=	p.LpVariable("	x1841	",lowBound=0, cat= 'Integer')
x1842	=	p.LpVariable("	x1842	",lowBound=0, cat= 'Integer')
x1843	=	p.LpVariable("	x1843	",lowBound=0, cat= 'Integer')
x1844	=	p.LpVariable("	x1844	",lowBound=0, cat= 'Integer')
x1845	=	p.LpVariable("	x1845	",lowBound=0, cat= 'Integer')
x1846	=	p.LpVariable("	x1846	",lowBound=0, cat= 'Integer')
x1847	=	p.LpVariable("	x1847	",lowBound=0, cat= 'Integer')
x1848	=	p.LpVariable("	x1848	",lowBound=0, cat= 'Integer')
x1849	=	p.LpVariable("	x1849	",lowBound=0, cat= 'Integer')
x1850	=	p.LpVariable("	x1850	",lowBound=0, cat= 'Integer')
x1851	=	p.LpVariable("	x1851	",lowBound=0, cat= 'Integer')
x1852	=	p.LpVariable("	x1852	",lowBound=0, cat= 'Integer')
x1853	=	p.LpVariable("	x1853	",lowBound=0, cat= 'Integer')
x1854	=	p.LpVariable("	x1854	",lowBound=0, cat= 'Integer')
x1855	=	p.LpVariable("	x1855	",lowBound=0, cat= 'Integer')
x1856	=	p.LpVariable("	x1856	",lowBound=0, cat= 'Integer')
x1857	=	p.LpVariable("	x1857	",lowBound=0, cat= 'Integer')
x1858	=	p.LpVariable("	x1858	",lowBound=0, cat= 'Integer')
x1859	=	p.LpVariable("	x1859	",lowBound=0, cat= 'Integer')
x1860	=	p.LpVariable("	x1860	",lowBound=0, cat= 'Integer')
x1861	=	p.LpVariable("	x1861	",lowBound=0, cat= 'Integer')
x1862	=	p.LpVariable("	x1862	",lowBound=0, cat= 'Integer')
x1863	=	p.LpVariable("	x1863	",lowBound=0, cat= 'Integer')
x1864	=	p.LpVariable("	x1864	",lowBound=0, cat= 'Integer')
x1865	=	p.LpVariable("	x1865	",lowBound=0, cat= 'Integer')
x1866	=	p.LpVariable("	x1866	",lowBound=0, cat= 'Integer')
x1867	=	p.LpVariable("	x1867	",lowBound=0, cat= 'Integer')
x1868	=	p.LpVariable("	x1868	",lowBound=0, cat= 'Integer')
x1869	=	p.LpVariable("	x1869	",lowBound=0, cat= 'Integer')
x1870	=	p.LpVariable("	x1870	",lowBound=0, cat= 'Integer')
x1871	=	p.LpVariable("	x1871	",lowBound=0, cat= 'Integer')
x1872	=	p.LpVariable("	x1872	",lowBound=0, cat= 'Integer')
x1873	=	p.LpVariable("	x1873	",lowBound=0, cat= 'Integer')
x1874	=	p.LpVariable("	x1874	",lowBound=0, cat= 'Integer')
x1875	=	p.LpVariable("	x1875	",lowBound=0, cat= 'Integer')
x1876	=	p.LpVariable("	x1876	",lowBound=0, cat= 'Integer')
x1877	=	p.LpVariable("	x1877	",lowBound=0, cat= 'Integer')
x1878	=	p.LpVariable("	x1878	",lowBound=0, cat= 'Integer')
x1879	=	p.LpVariable("	x1879	",lowBound=0, cat= 'Integer')
x1880	=	p.LpVariable("	x1880	",lowBound=0, cat= 'Integer')
x1881	=	p.LpVariable("	x1881	",lowBound=0, cat= 'Integer')
x1882	=	p.LpVariable("	x1882	",lowBound=0, cat= 'Integer')
x1883	=	p.LpVariable("	x1883	",lowBound=0, cat= 'Integer')
x1884	=	p.LpVariable("	x1884	",lowBound=0, cat= 'Integer')
x1885	=	p.LpVariable("	x1885	",lowBound=0, cat= 'Integer')
x1886	=	p.LpVariable("	x1886	",lowBound=0, cat= 'Integer')
x1887	=	p.LpVariable("	x1887	",lowBound=0, cat= 'Integer')
x1888	=	p.LpVariable("	x1888	",lowBound=0, cat= 'Integer')
x1889	=	p.LpVariable("	x1889	",lowBound=0, cat= 'Integer')
x1890	=	p.LpVariable("	x1890	",lowBound=0, cat= 'Integer')
x1891	=	p.LpVariable("	x1891	",lowBound=0, cat= 'Integer')
x1892	=	p.LpVariable("	x1892	",lowBound=0, cat= 'Integer')
x1893	=	p.LpVariable("	x1893	",lowBound=0, cat= 'Integer')
x1894	=	p.LpVariable("	x1894	",lowBound=0, cat= 'Integer')
x1895	=	p.LpVariable("	x1895	",lowBound=0, cat= 'Integer')
x1896	=	p.LpVariable("	x1896	",lowBound=0, cat= 'Integer')
x1897	=	p.LpVariable("	x1897	",lowBound=0, cat= 'Integer')
x1898	=	p.LpVariable("	x1898	",lowBound=0, cat= 'Integer')
x1899	=	p.LpVariable("	x1899	",lowBound=0, cat= 'Integer')
x1900	=	p.LpVariable("	x1900	",lowBound=0, cat= 'Integer')
x1901	=	p.LpVariable("	x1901	",lowBound=0, cat= 'Integer')
x1902	=	p.LpVariable("	x1902	",lowBound=0, cat= 'Integer')
x1903	=	p.LpVariable("	x1903	",lowBound=0, cat= 'Integer')
x1904	=	p.LpVariable("	x1904	",lowBound=0, cat= 'Integer')
x1905	=	p.LpVariable("	x1905	",lowBound=0, cat= 'Integer')
x1906	=	p.LpVariable("	x1906	",lowBound=0, cat= 'Integer')
x1907	=	p.LpVariable("	x1907	",lowBound=0, cat= 'Integer')
x1908	=	p.LpVariable("	x1908	",lowBound=0, cat= 'Integer')
x1909	=	p.LpVariable("	x1909	",lowBound=0, cat= 'Integer')
x1910	=	p.LpVariable("	x1910	",lowBound=0, cat= 'Integer')
x1911	=	p.LpVariable("	x1911	",lowBound=0, cat= 'Integer')
x1912	=	p.LpVariable("	x1912	",lowBound=0, cat= 'Integer')
x1913	=	p.LpVariable("	x1913	",lowBound=0, cat= 'Integer')
x1914	=	p.LpVariable("	x1914	",lowBound=0, cat= 'Integer')
x1915	=	p.LpVariable("	x1915	",lowBound=0, cat= 'Integer')
x1916	=	p.LpVariable("	x1916	",lowBound=0, cat= 'Integer')
x1917	=	p.LpVariable("	x1917	",lowBound=0, cat= 'Integer')
x1918	=	p.LpVariable("	x1918	",lowBound=0, cat= 'Integer')
x1919	=	p.LpVariable("	x1919	",lowBound=0, cat= 'Integer')
x1920	=	p.LpVariable("	x1920	",lowBound=0, cat= 'Integer')
x1921	=	p.LpVariable("	x1921	",lowBound=0, cat= 'Integer')
x1922	=	p.LpVariable("	x1922	",lowBound=0, cat= 'Integer')
x1923	=	p.LpVariable("	x1923	",lowBound=0, cat= 'Integer')
x1924	=	p.LpVariable("	x1924	",lowBound=0, cat= 'Integer')
x1925	=	p.LpVariable("	x1925	",lowBound=0, cat= 'Integer')
x1926	=	p.LpVariable("	x1926	",lowBound=0, cat= 'Integer')
x1927	=	p.LpVariable("	x1927	",lowBound=0, cat= 'Integer')
x1928	=	p.LpVariable("	x1928	",lowBound=0, cat= 'Integer')
x1929	=	p.LpVariable("	x1929	",lowBound=0, cat= 'Integer')
x1930	=	p.LpVariable("	x1930	",lowBound=0, cat= 'Integer')
x1931	=	p.LpVariable("	x1931	",lowBound=0, cat= 'Integer')
x1932	=	p.LpVariable("	x1932	",lowBound=0, cat= 'Integer')
x1933	=	p.LpVariable("	x1933	",lowBound=0, cat= 'Integer')
x1934	=	p.LpVariable("	x1934	",lowBound=0, cat= 'Integer')
x1935	=	p.LpVariable("	x1935	",lowBound=0, cat= 'Integer')
x1936	=	p.LpVariable("	x1936	",lowBound=0, cat= 'Integer')
x1937	=	p.LpVariable("	x1937	",lowBound=0, cat= 'Integer')
x1938	=	p.LpVariable("	x1938	",lowBound=0, cat= 'Integer')
x1939	=	p.LpVariable("	x1939	",lowBound=0, cat= 'Integer')
x1940	=	p.LpVariable("	x1940	",lowBound=0, cat= 'Integer')
x1941	=	p.LpVariable("	x1941	",lowBound=0, cat= 'Integer')
x1942	=	p.LpVariable("	x1942	",lowBound=0, cat= 'Integer')
x1943	=	p.LpVariable("	x1943	",lowBound=0, cat= 'Integer')
x1944	=	p.LpVariable("	x1944	",lowBound=0, cat= 'Integer')
x1945	=	p.LpVariable("	x1945	",lowBound=0, cat= 'Integer')
x1946	=	p.LpVariable("	x1946	",lowBound=0, cat= 'Integer')
x1947	=	p.LpVariable("	x1947	",lowBound=0, cat= 'Integer')
x1948	=	p.LpVariable("	x1948	",lowBound=0, cat= 'Integer')
x1949	=	p.LpVariable("	x1949	",lowBound=0, cat= 'Integer')
x1950	=	p.LpVariable("	x1950	",lowBound=0, cat= 'Integer')
x1951	=	p.LpVariable("	x1951	",lowBound=0, cat= 'Integer')
x1952	=	p.LpVariable("	x1952	",lowBound=0, cat= 'Integer')
x1953	=	p.LpVariable("	x1953	",lowBound=0, cat= 'Integer')
x1954	=	p.LpVariable("	x1954	",lowBound=0, cat= 'Integer')
x1955	=	p.LpVariable("	x1955	",lowBound=0, cat= 'Integer')
x1956	=	p.LpVariable("	x1956	",lowBound=0, cat= 'Integer')
x1957	=	p.LpVariable("	x1957	",lowBound=0, cat= 'Integer')
x1958	=	p.LpVariable("	x1958	",lowBound=0, cat= 'Integer')
x1959	=	p.LpVariable("	x1959	",lowBound=0, cat= 'Integer')
x1960	=	p.LpVariable("	x1960	",lowBound=0, cat= 'Integer')
x1961	=	p.LpVariable("	x1961	",lowBound=0, cat= 'Integer')
x1962	=	p.LpVariable("	x1962	",lowBound=0, cat= 'Integer')
x1963	=	p.LpVariable("	x1963	",lowBound=0, cat= 'Integer')
x1964	=	p.LpVariable("	x1964	",lowBound=0, cat= 'Integer')
x1965	=	p.LpVariable("	x1965	",lowBound=0, cat= 'Integer')
x1966	=	p.LpVariable("	x1966	",lowBound=0, cat= 'Integer')
x1967	=	p.LpVariable("	x1967	",lowBound=0, cat= 'Integer')
x1968	=	p.LpVariable("	x1968	",lowBound=0, cat= 'Integer')
x1969	=	p.LpVariable("	x1969	",lowBound=0, cat= 'Integer')
x1970	=	p.LpVariable("	x1970	",lowBound=0, cat= 'Integer')
x1971	=	p.LpVariable("	x1971	",lowBound=0, cat= 'Integer')
x1972	=	p.LpVariable("	x1972	",lowBound=0, cat= 'Integer')
x1973	=	p.LpVariable("	x1973	",lowBound=0, cat= 'Integer')
x1974	=	p.LpVariable("	x1974	",lowBound=0, cat= 'Integer')
x1975	=	p.LpVariable("	x1975	",lowBound=0, cat= 'Integer')
x1976	=	p.LpVariable("	x1976	",lowBound=0, cat= 'Integer')
x1977	=	p.LpVariable("	x1977	",lowBound=0, cat= 'Integer')
x1978	=	p.LpVariable("	x1978	",lowBound=0, cat= 'Integer')
x1979	=	p.LpVariable("	x1979	",lowBound=0, cat= 'Integer')
x1980	=	p.LpVariable("	x1980	",lowBound=0, cat= 'Integer')
x1981	=	p.LpVariable("	x1981	",lowBound=0, cat= 'Integer')
x1982	=	p.LpVariable("	x1982	",lowBound=0, cat= 'Integer')
x1983	=	p.LpVariable("	x1983	",lowBound=0, cat= 'Integer')
x1984	=	p.LpVariable("	x1984	",lowBound=0, cat= 'Integer')
x1985	=	p.LpVariable("	x1985	",lowBound=0, cat= 'Integer')
x1986	=	p.LpVariable("	x1986	",lowBound=0, cat= 'Integer')
x1987	=	p.LpVariable("	x1987	",lowBound=0, cat= 'Integer')
x1988	=	p.LpVariable("	x1988	",lowBound=0, cat= 'Integer')
x1989	=	p.LpVariable("	x1989	",lowBound=0, cat= 'Integer')
x1990	=	p.LpVariable("	x1990	",lowBound=0, cat= 'Integer')
x1991	=	p.LpVariable("	x1991	",lowBound=0, cat= 'Integer')
x1992	=	p.LpVariable("	x1992	",lowBound=0, cat= 'Integer')
x1993	=	p.LpVariable("	x1993	",lowBound=0, cat= 'Integer')
x1994	=	p.LpVariable("	x1994	",lowBound=0, cat= 'Integer')
x1995	=	p.LpVariable("	x1995	",lowBound=0, cat= 'Integer')
x1996	=	p.LpVariable("	x1996	",lowBound=0, cat= 'Integer')
x1997	=	p.LpVariable("	x1997	",lowBound=0, cat= 'Integer')
x1998	=	p.LpVariable("	x1998	",lowBound=0, cat= 'Integer')
x1999	=	p.LpVariable("	x1999	",lowBound=0, cat= 'Integer')
x2000	=	p.LpVariable("	x2000	",lowBound=0, cat= 'Integer')
x2001	=	p.LpVariable("	x2001	",lowBound=0, cat= 'Integer')
x2002	=	p.LpVariable("	x2002	",lowBound=0, cat= 'Integer')
x2003	=	p.LpVariable("	x2003	",lowBound=0, cat= 'Integer')
x2004	=	p.LpVariable("	x2004	",lowBound=0, cat= 'Integer')
x2005	=	p.LpVariable("	x2005	",lowBound=0, cat= 'Integer')
x2006	=	p.LpVariable("	x2006	",lowBound=0, cat= 'Integer')
x2007	=	p.LpVariable("	x2007	",lowBound=0, cat= 'Integer')
x2008	=	p.LpVariable("	x2008	",lowBound=0, cat= 'Integer')
x2009	=	p.LpVariable("	x2009	",lowBound=0, cat= 'Integer')
x2010	=	p.LpVariable("	x2010	",lowBound=0, cat= 'Integer')
x2011	=	p.LpVariable("	x2011	",lowBound=0, cat= 'Integer')
x2012	=	p.LpVariable("	x2012	",lowBound=0, cat= 'Integer')
x2013	=	p.LpVariable("	x2013	",lowBound=0, cat= 'Integer')
x2014	=	p.LpVariable("	x2014	",lowBound=0, cat= 'Integer')
x2015	=	p.LpVariable("	x2015	",lowBound=0, cat= 'Integer')
x2016	=	p.LpVariable("	x2016	",lowBound=0, cat= 'Integer')
x2017	=	p.LpVariable("	x2017	",lowBound=0, cat= 'Integer')
x2018	=	p.LpVariable("	x2018	",lowBound=0, cat= 'Integer')
x2019	=	p.LpVariable("	x2019	",lowBound=0, cat= 'Integer')
x2020	=	p.LpVariable("	x2020	",lowBound=0, cat= 'Integer')
x2021	=	p.LpVariable("	x2021	",lowBound=0, cat= 'Integer')
x2022	=	p.LpVariable("	x2022	",lowBound=0, cat= 'Integer')
x2023	=	p.LpVariable("	x2023	",lowBound=0, cat= 'Integer')
x2024	=	p.LpVariable("	x2024	",lowBound=0, cat= 'Integer')
x2025	=	p.LpVariable("	x2025	",lowBound=0, cat= 'Integer')
x2026	=	p.LpVariable("	x2026	",lowBound=0, cat= 'Integer')
x2027	=	p.LpVariable("	x2027	",lowBound=0, cat= 'Integer')
x2028	=	p.LpVariable("	x2028	",lowBound=0, cat= 'Integer')
x2029	=	p.LpVariable("	x2029	",lowBound=0, cat= 'Integer')
x2030	=	p.LpVariable("	x2030	",lowBound=0, cat= 'Integer')
x2031	=	p.LpVariable("	x2031	",lowBound=0, cat= 'Integer')
x2032	=	p.LpVariable("	x2032	",lowBound=0, cat= 'Integer')
x2033	=	p.LpVariable("	x2033	",lowBound=0, cat= 'Integer')
x2034	=	p.LpVariable("	x2034	",lowBound=0, cat= 'Integer')
x2035	=	p.LpVariable("	x2035	",lowBound=0, cat= 'Integer')
x2036	=	p.LpVariable("	x2036	",lowBound=0, cat= 'Integer')
x2037	=	p.LpVariable("	x2037	",lowBound=0, cat= 'Integer')
x2038	=	p.LpVariable("	x2038	",lowBound=0, cat= 'Integer')
x2039	=	p.LpVariable("	x2039	",lowBound=0, cat= 'Integer')
x2040	=	p.LpVariable("	x2040	",lowBound=0, cat= 'Integer')
x2041	=	p.LpVariable("	x2041	",lowBound=0, cat= 'Integer')
x2042	=	p.LpVariable("	x2042	",lowBound=0, cat= 'Integer')
x2043	=	p.LpVariable("	x2043	",lowBound=0, cat= 'Integer')
x2044	=	p.LpVariable("	x2044	",lowBound=0, cat= 'Integer')
x2045	=	p.LpVariable("	x2045	",lowBound=0, cat= 'Integer')
x2046	=	p.LpVariable("	x2046	",lowBound=0, cat= 'Integer')
x2047	=	p.LpVariable("	x2047	",lowBound=0, cat= 'Integer')
x2048	=	p.LpVariable("	x2048	",lowBound=0, cat= 'Integer')
x2049	=	p.LpVariable("	x2049	",lowBound=0, cat= 'Integer')
x2050	=	p.LpVariable("	x2050	",lowBound=0, cat= 'Integer')
x2051	=	p.LpVariable("	x2051	",lowBound=0, cat= 'Integer')
x2052	=	p.LpVariable("	x2052	",lowBound=0, cat= 'Integer')
x2053	=	p.LpVariable("	x2053	",lowBound=0, cat= 'Integer')
x2054	=	p.LpVariable("	x2054	",lowBound=0, cat= 'Integer')
x2055	=	p.LpVariable("	x2055	",lowBound=0, cat= 'Integer')
x2056	=	p.LpVariable("	x2056	",lowBound=0, cat= 'Integer')
x2057	=	p.LpVariable("	x2057	",lowBound=0, cat= 'Integer')
x2058	=	p.LpVariable("	x2058	",lowBound=0, cat= 'Integer')
x2059	=	p.LpVariable("	x2059	",lowBound=0, cat= 'Integer')
x2060	=	p.LpVariable("	x2060	",lowBound=0, cat= 'Integer')
x2061	=	p.LpVariable("	x2061	",lowBound=0, cat= 'Integer')
x2062	=	p.LpVariable("	x2062	",lowBound=0, cat= 'Integer')
x2063	=	p.LpVariable("	x2063	",lowBound=0, cat= 'Integer')
x2064	=	p.LpVariable("	x2064	",lowBound=0, cat= 'Integer')
x2065	=	p.LpVariable("	x2065	",lowBound=0, cat= 'Integer')
x2066	=	p.LpVariable("	x2066	",lowBound=0, cat= 'Integer')
x2067	=	p.LpVariable("	x2067	",lowBound=0, cat= 'Integer')
x2068	=	p.LpVariable("	x2068	",lowBound=0, cat= 'Integer')
x2069	=	p.LpVariable("	x2069	",lowBound=0, cat= 'Integer')
x2070	=	p.LpVariable("	x2070	",lowBound=0, cat= 'Integer')
x2071	=	p.LpVariable("	x2071	",lowBound=0, cat= 'Integer')
x2072	=	p.LpVariable("	x2072	",lowBound=0, cat= 'Integer')
x2073	=	p.LpVariable("	x2073	",lowBound=0, cat= 'Integer')
x2074	=	p.LpVariable("	x2074	",lowBound=0, cat= 'Integer')
x2075	=	p.LpVariable("	x2075	",lowBound=0, cat= 'Integer')
x2076	=	p.LpVariable("	x2076	",lowBound=0, cat= 'Integer')
x2077	=	p.LpVariable("	x2077	",lowBound=0, cat= 'Integer')
x2078	=	p.LpVariable("	x2078	",lowBound=0, cat= 'Integer')
x2079	=	p.LpVariable("	x2079	",lowBound=0, cat= 'Integer')
x2080	=	p.LpVariable("	x2080	",lowBound=0, cat= 'Integer')
x2081	=	p.LpVariable("	x2081	",lowBound=0, cat= 'Integer')
x2082	=	p.LpVariable("	x2082	",lowBound=0, cat= 'Integer')
x2083	=	p.LpVariable("	x2083	",lowBound=0, cat= 'Integer')
x2084	=	p.LpVariable("	x2084	",lowBound=0, cat= 'Integer')
x2085	=	p.LpVariable("	x2085	",lowBound=0, cat= 'Integer')
x2086	=	p.LpVariable("	x2086	",lowBound=0, cat= 'Integer')
x2087	=	p.LpVariable("	x2087	",lowBound=0, cat= 'Integer')
x2088	=	p.LpVariable("	x2088	",lowBound=0, cat= 'Integer')
x2089	=	p.LpVariable("	x2089	",lowBound=0, cat= 'Integer')
x2090	=	p.LpVariable("	x2090	",lowBound=0, cat= 'Integer')
x2091	=	p.LpVariable("	x2091	",lowBound=0, cat= 'Integer')
x2092	=	p.LpVariable("	x2092	",lowBound=0, cat= 'Integer')
x2093	=	p.LpVariable("	x2093	",lowBound=0, cat= 'Integer')
x2094	=	p.LpVariable("	x2094	",lowBound=0, cat= 'Integer')
x2095	=	p.LpVariable("	x2095	",lowBound=0, cat= 'Integer')
x2096	=	p.LpVariable("	x2096	",lowBound=0, cat= 'Integer')
x2097	=	p.LpVariable("	x2097	",lowBound=0, cat= 'Integer')
x2098	=	p.LpVariable("	x2098	",lowBound=0, cat= 'Integer')
x2099	=	p.LpVariable("	x2099	",lowBound=0, cat= 'Integer')
x2100	=	p.LpVariable("	x2100	",lowBound=0, cat= 'Integer')
x2101	=	p.LpVariable("	x2101	",lowBound=0, cat= 'Integer')
x2102	=	p.LpVariable("	x2102	",lowBound=0, cat= 'Integer')
x2103	=	p.LpVariable("	x2103	",lowBound=0, cat= 'Integer')
x2104	=	p.LpVariable("	x2104	",lowBound=0, cat= 'Integer')
x2105	=	p.LpVariable("	x2105	",lowBound=0, cat= 'Integer')
x2106	=	p.LpVariable("	x2106	",lowBound=0, cat= 'Integer')
x2107	=	p.LpVariable("	x2107	",lowBound=0, cat= 'Integer')
x2108	=	p.LpVariable("	x2108	",lowBound=0, cat= 'Integer')
x2109	=	p.LpVariable("	x2109	",lowBound=0, cat= 'Integer')
x2110	=	p.LpVariable("	x2110	",lowBound=0, cat= 'Integer')
x2111	=	p.LpVariable("	x2111	",lowBound=0, cat= 'Integer')
x2112	=	p.LpVariable("	x2112	",lowBound=0, cat= 'Integer')
x2113	=	p.LpVariable("	x2113	",lowBound=0, cat= 'Integer')
x2114	=	p.LpVariable("	x2114	",lowBound=0, cat= 'Integer')
x2115	=	p.LpVariable("	x2115	",lowBound=0, cat= 'Integer')
x2116	=	p.LpVariable("	x2116	",lowBound=0, cat= 'Integer')
x2117	=	p.LpVariable("	x2117	",lowBound=0, cat= 'Integer')
x2118	=	p.LpVariable("	x2118	",lowBound=0, cat= 'Integer')
x2119	=	p.LpVariable("	x2119	",lowBound=0, cat= 'Integer')
x2120	=	p.LpVariable("	x2120	",lowBound=0, cat= 'Integer')
x2121	=	p.LpVariable("	x2121	",lowBound=0, cat= 'Integer')
x2122	=	p.LpVariable("	x2122	",lowBound=0, cat= 'Integer')
x2123	=	p.LpVariable("	x2123	",lowBound=0, cat= 'Integer')
x2124	=	p.LpVariable("	x2124	",lowBound=0, cat= 'Integer')
x2125	=	p.LpVariable("	x2125	",lowBound=0, cat= 'Integer')
x2126	=	p.LpVariable("	x2126	",lowBound=0, cat= 'Integer')
x2127	=	p.LpVariable("	x2127	",lowBound=0, cat= 'Integer')
x2128	=	p.LpVariable("	x2128	",lowBound=0, cat= 'Integer')
x2129	=	p.LpVariable("	x2129	",lowBound=0, cat= 'Integer')
x2130	=	p.LpVariable("	x2130	",lowBound=0, cat= 'Integer')
x2131	=	p.LpVariable("	x2131	",lowBound=0, cat= 'Integer')
x2132	=	p.LpVariable("	x2132	",lowBound=0, cat= 'Integer')
x2133	=	p.LpVariable("	x2133	",lowBound=0, cat= 'Integer')
x2134	=	p.LpVariable("	x2134	",lowBound=0, cat= 'Integer')
x2135	=	p.LpVariable("	x2135	",lowBound=0, cat= 'Integer')
x2136	=	p.LpVariable("	x2136	",lowBound=0, cat= 'Integer')
x2137	=	p.LpVariable("	x2137	",lowBound=0, cat= 'Integer')
x2138	=	p.LpVariable("	x2138	",lowBound=0, cat= 'Integer')
x2139	=	p.LpVariable("	x2139	",lowBound=0, cat= 'Integer')
x2140	=	p.LpVariable("	x2140	",lowBound=0, cat= 'Integer')
x2141	=	p.LpVariable("	x2141	",lowBound=0, cat= 'Integer')
x2142	=	p.LpVariable("	x2142	",lowBound=0, cat= 'Integer')
x2143	=	p.LpVariable("	x2143	",lowBound=0, cat= 'Integer')
x2144	=	p.LpVariable("	x2144	",lowBound=0, cat= 'Integer')
x2145	=	p.LpVariable("	x2145	",lowBound=0, cat= 'Integer')
x2146	=	p.LpVariable("	x2146	",lowBound=0, cat= 'Integer')
x2147	=	p.LpVariable("	x2147	",lowBound=0, cat= 'Integer')
x2148	=	p.LpVariable("	x2148	",lowBound=0, cat= 'Integer')
x2149	=	p.LpVariable("	x2149	",lowBound=0, cat= 'Integer')
x2150	=	p.LpVariable("	x2150	",lowBound=0, cat= 'Integer')
x2151	=	p.LpVariable("	x2151	",lowBound=0, cat= 'Integer')
x2152	=	p.LpVariable("	x2152	",lowBound=0, cat= 'Integer')
x2153	=	p.LpVariable("	x2153	",lowBound=0, cat= 'Integer')
x2154	=	p.LpVariable("	x2154	",lowBound=0, cat= 'Integer')
x2155	=	p.LpVariable("	x2155	",lowBound=0, cat= 'Integer')
x2156	=	p.LpVariable("	x2156	",lowBound=0, cat= 'Integer')
x2157	=	p.LpVariable("	x2157	",lowBound=0, cat= 'Integer')
x2158	=	p.LpVariable("	x2158	",lowBound=0, cat= 'Integer')
x2159	=	p.LpVariable("	x2159	",lowBound=0, cat= 'Integer')
x2160	=	p.LpVariable("	x2160	",lowBound=0, cat= 'Integer')
x2161	=	p.LpVariable("	x2161	",lowBound=0, cat= 'Integer')
x2162	=	p.LpVariable("	x2162	",lowBound=0, cat= 'Integer')
x2163	=	p.LpVariable("	x2163	",lowBound=0, cat= 'Integer')
x2164	=	p.LpVariable("	x2164	",lowBound=0, cat= 'Integer')
x2165	=	p.LpVariable("	x2165	",lowBound=0, cat= 'Integer')
x2166	=	p.LpVariable("	x2166	",lowBound=0, cat= 'Integer')
x2167	=	p.LpVariable("	x2167	",lowBound=0, cat= 'Integer')
x2168	=	p.LpVariable("	x2168	",lowBound=0, cat= 'Integer')
x2169	=	p.LpVariable("	x2169	",lowBound=0, cat= 'Integer')
x2170	=	p.LpVariable("	x2170	",lowBound=0, cat= 'Integer')
x2171	=	p.LpVariable("	x2171	",lowBound=0, cat= 'Integer')
x2172	=	p.LpVariable("	x2172	",lowBound=0, cat= 'Integer')
x2173	=	p.LpVariable("	x2173	",lowBound=0, cat= 'Integer')
x2174	=	p.LpVariable("	x2174	",lowBound=0, cat= 'Integer')
x2175	=	p.LpVariable("	x2175	",lowBound=0, cat= 'Integer')
x2176	=	p.LpVariable("	x2176	",lowBound=0, cat= 'Integer')
x2177	=	p.LpVariable("	x2177	",lowBound=0, cat= 'Integer')
x2178	=	p.LpVariable("	x2178	",lowBound=0, cat= 'Integer')
x2179	=	p.LpVariable("	x2179	",lowBound=0, cat= 'Integer')
x2180	=	p.LpVariable("	x2180	",lowBound=0, cat= 'Integer')
x2181	=	p.LpVariable("	x2181	",lowBound=0, cat= 'Integer')
x2182	=	p.LpVariable("	x2182	",lowBound=0, cat= 'Integer')
x2183	=	p.LpVariable("	x2183	",lowBound=0, cat= 'Integer')
x2184	=	p.LpVariable("	x2184	",lowBound=0, cat= 'Integer')
x2185	=	p.LpVariable("	x2185	",lowBound=0, cat= 'Integer')
x2186	=	p.LpVariable("	x2186	",lowBound=0, cat= 'Integer')
x2187	=	p.LpVariable("	x2187	",lowBound=0, cat= 'Integer')
x2188	=	p.LpVariable("	x2188	",lowBound=0, cat= 'Integer')
x2189	=	p.LpVariable("	x2189	",lowBound=0, cat= 'Integer')
x2190	=	p.LpVariable("	x2190	",lowBound=0, cat= 'Integer')
x2191	=	p.LpVariable("	x2191	",lowBound=0, cat= 'Integer')
x2192	=	p.LpVariable("	x2192	",lowBound=0, cat= 'Integer')
x2193	=	p.LpVariable("	x2193	",lowBound=0, cat= 'Integer')
x2194	=	p.LpVariable("	x2194	",lowBound=0, cat= 'Integer')
x2195	=	p.LpVariable("	x2195	",lowBound=0, cat= 'Integer')
x2196	=	p.LpVariable("	x2196	",lowBound=0, cat= 'Integer')
x2197	=	p.LpVariable("	x2197	",lowBound=0, cat= 'Integer')
x2198	=	p.LpVariable("	x2198	",lowBound=0, cat= 'Integer')
x2199	=	p.LpVariable("	x2199	",lowBound=0, cat= 'Integer')
x2200	=	p.LpVariable("	x2200	",lowBound=0, cat= 'Integer')
x2201	=	p.LpVariable("	x2201	",lowBound=0, cat= 'Integer')
x2202	=	p.LpVariable("	x2202	",lowBound=0, cat= 'Integer')
x2203	=	p.LpVariable("	x2203	",lowBound=0, cat= 'Integer')
x2204	=	p.LpVariable("	x2204	",lowBound=0, cat= 'Integer')
x2205	=	p.LpVariable("	x2205	",lowBound=0, cat= 'Integer')
x2206	=	p.LpVariable("	x2206	",lowBound=0, cat= 'Integer')
x2207	=	p.LpVariable("	x2207	",lowBound=0, cat= 'Integer')
x2208	=	p.LpVariable("	x2208	",lowBound=0, cat= 'Integer')
x2209	=	p.LpVariable("	x2209	",lowBound=0, cat= 'Integer')
x2210	=	p.LpVariable("	x2210	",lowBound=0, cat= 'Integer')
x2211	=	p.LpVariable("	x2211	",lowBound=0, cat= 'Integer')
x2212	=	p.LpVariable("	x2212	",lowBound=0, cat= 'Integer')
x2213	=	p.LpVariable("	x2213	",lowBound=0, cat= 'Integer')
x2214	=	p.LpVariable("	x2214	",lowBound=0, cat= 'Integer')
x2215	=	p.LpVariable("	x2215	",lowBound=0, cat= 'Integer')
x2216	=	p.LpVariable("	x2216	",lowBound=0, cat= 'Integer')
x2217	=	p.LpVariable("	x2217	",lowBound=0, cat= 'Integer')
x2218	=	p.LpVariable("	x2218	",lowBound=0, cat= 'Integer')
x2219	=	p.LpVariable("	x2219	",lowBound=0, cat= 'Integer')
x2220	=	p.LpVariable("	x2220	",lowBound=0, cat= 'Integer')
x2221	=	p.LpVariable("	x2221	",lowBound=0, cat= 'Integer')
x2222	=	p.LpVariable("	x2222	",lowBound=0, cat= 'Integer')
x2223	=	p.LpVariable("	x2223	",lowBound=0, cat= 'Integer')
x2224	=	p.LpVariable("	x2224	",lowBound=0, cat= 'Integer')
x2225	=	p.LpVariable("	x2225	",lowBound=0, cat= 'Integer')
x2226	=	p.LpVariable("	x2226	",lowBound=0, cat= 'Integer')
x2227	=	p.LpVariable("	x2227	",lowBound=0, cat= 'Integer')
x2228	=	p.LpVariable("	x2228	",lowBound=0, cat= 'Integer')
x2229	=	p.LpVariable("	x2229	",lowBound=0, cat= 'Integer')
x2230	=	p.LpVariable("	x2230	",lowBound=0, cat= 'Integer')
x2231	=	p.LpVariable("	x2231	",lowBound=0, cat= 'Integer')
x2232	=	p.LpVariable("	x2232	",lowBound=0, cat= 'Integer')
x2233	=	p.LpVariable("	x2233	",lowBound=0, cat= 'Integer')
x2234	=	p.LpVariable("	x2234	",lowBound=0, cat= 'Integer')
x2235	=	p.LpVariable("	x2235	",lowBound=0, cat= 'Integer')
x2236	=	p.LpVariable("	x2236	",lowBound=0, cat= 'Integer')
x2237	=	p.LpVariable("	x2237	",lowBound=0, cat= 'Integer')
x2238	=	p.LpVariable("	x2238	",lowBound=0, cat= 'Integer')
x2239	=	p.LpVariable("	x2239	",lowBound=0, cat= 'Integer')
x2240	=	p.LpVariable("	x2240	",lowBound=0, cat= 'Integer')
x2241	=	p.LpVariable("	x2241	",lowBound=0, cat= 'Integer')
x2242	=	p.LpVariable("	x2242	",lowBound=0, cat= 'Integer')
x2243	=	p.LpVariable("	x2243	",lowBound=0, cat= 'Integer')
x2244	=	p.LpVariable("	x2244	",lowBound=0, cat= 'Integer')
x2245	=	p.LpVariable("	x2245	",lowBound=0, cat= 'Integer')
x2246	=	p.LpVariable("	x2246	",lowBound=0, cat= 'Integer')
x2247	=	p.LpVariable("	x2247	",lowBound=0, cat= 'Integer')
x2248	=	p.LpVariable("	x2248	",lowBound=0, cat= 'Integer')
x2249	=	p.LpVariable("	x2249	",lowBound=0, cat= 'Integer')
x2250	=	p.LpVariable("	x2250	",lowBound=0, cat= 'Integer')
x2251	=	p.LpVariable("	x2251	",lowBound=0, cat= 'Integer')
x2252	=	p.LpVariable("	x2252	",lowBound=0, cat= 'Integer')
x2253	=	p.LpVariable("	x2253	",lowBound=0, cat= 'Integer')
x2254	=	p.LpVariable("	x2254	",lowBound=0, cat= 'Integer')
x2255	=	p.LpVariable("	x2255	",lowBound=0, cat= 'Integer')
x2256	=	p.LpVariable("	x2256	",lowBound=0, cat= 'Integer')
x2257	=	p.LpVariable("	x2257	",lowBound=0, cat= 'Integer')
x2258	=	p.LpVariable("	x2258	",lowBound=0, cat= 'Integer')
x2259	=	p.LpVariable("	x2259	",lowBound=0, cat= 'Integer')
x2260	=	p.LpVariable("	x2260	",lowBound=0, cat= 'Integer')
x2261	=	p.LpVariable("	x2261	",lowBound=0, cat= 'Integer')
x2262	=	p.LpVariable("	x2262	",lowBound=0, cat= 'Integer')
x2263	=	p.LpVariable("	x2263	",lowBound=0, cat= 'Integer')
x2264	=	p.LpVariable("	x2264	",lowBound=0, cat= 'Integer')
x2265	=	p.LpVariable("	x2265	",lowBound=0, cat= 'Integer')
x2266	=	p.LpVariable("	x2266	",lowBound=0, cat= 'Integer')
x2267	=	p.LpVariable("	x2267	",lowBound=0, cat= 'Integer')
x2268	=	p.LpVariable("	x2268	",lowBound=0, cat= 'Integer')
x2269	=	p.LpVariable("	x2269	",lowBound=0, cat= 'Integer')
x2270	=	p.LpVariable("	x2270	",lowBound=0, cat= 'Integer')
x2271	=	p.LpVariable("	x2271	",lowBound=0, cat= 'Integer')
x2272	=	p.LpVariable("	x2272	",lowBound=0, cat= 'Integer')
x2273	=	p.LpVariable("	x2273	",lowBound=0, cat= 'Integer')
x2274	=	p.LpVariable("	x2274	",lowBound=0, cat= 'Integer')
x2275	=	p.LpVariable("	x2275	",lowBound=0, cat= 'Integer')
x2276	=	p.LpVariable("	x2276	",lowBound=0, cat= 'Integer')
x2277	=	p.LpVariable("	x2277	",lowBound=0, cat= 'Integer')
x2278	=	p.LpVariable("	x2278	",lowBound=0, cat= 'Integer')
x2279	=	p.LpVariable("	x2279	",lowBound=0, cat= 'Integer')
x2280	=	p.LpVariable("	x2280	",lowBound=0, cat= 'Integer')
x2281	=	p.LpVariable("	x2281	",lowBound=0, cat= 'Integer')
x2282	=	p.LpVariable("	x2282	",lowBound=0, cat= 'Integer')
x2283	=	p.LpVariable("	x2283	",lowBound=0, cat= 'Integer')
x2284	=	p.LpVariable("	x2284	",lowBound=0, cat= 'Integer')
x2285	=	p.LpVariable("	x2285	",lowBound=0, cat= 'Integer')
x2286	=	p.LpVariable("	x2286	",lowBound=0, cat= 'Integer')
x2287	=	p.LpVariable("	x2287	",lowBound=0, cat= 'Integer')
x2288	=	p.LpVariable("	x2288	",lowBound=0, cat= 'Integer')
x2289	=	p.LpVariable("	x2289	",lowBound=0, cat= 'Integer')
x2290	=	p.LpVariable("	x2290	",lowBound=0, cat= 'Integer')
x2291	=	p.LpVariable("	x2291	",lowBound=0, cat= 'Integer')
x2292	=	p.LpVariable("	x2292	",lowBound=0, cat= 'Integer')
x2293	=	p.LpVariable("	x2293	",lowBound=0, cat= 'Integer')
x2294	=	p.LpVariable("	x2294	",lowBound=0, cat= 'Integer')
x2295	=	p.LpVariable("	x2295	",lowBound=0, cat= 'Integer')
x2296	=	p.LpVariable("	x2296	",lowBound=0, cat= 'Integer')
x2297	=	p.LpVariable("	x2297	",lowBound=0, cat= 'Integer')
x2298	=	p.LpVariable("	x2298	",lowBound=0, cat= 'Integer')
x2299	=	p.LpVariable("	x2299	",lowBound=0, cat= 'Integer')
x2300	=	p.LpVariable("	x2300	",lowBound=0, cat= 'Integer')
x2301	=	p.LpVariable("	x2301	",lowBound=0, cat= 'Integer')
x2302	=	p.LpVariable("	x2302	",lowBound=0, cat= 'Integer')
x2303	=	p.LpVariable("	x2303	",lowBound=0, cat= 'Integer')
x2304	=	p.LpVariable("	x2304	",lowBound=0, cat= 'Integer')
x2305	=	p.LpVariable("	x2305	",lowBound=0, cat= 'Integer')
x2306	=	p.LpVariable("	x2306	",lowBound=0, cat= 'Integer')
x2307	=	p.LpVariable("	x2307	",lowBound=0, cat= 'Integer')
x2308	=	p.LpVariable("	x2308	",lowBound=0, cat= 'Integer')
x2309	=	p.LpVariable("	x2309	",lowBound=0, cat= 'Integer')
x2310	=	p.LpVariable("	x2310	",lowBound=0, cat= 'Integer')
x2311	=	p.LpVariable("	x2311	",lowBound=0, cat= 'Integer')
x2312	=	p.LpVariable("	x2312	",lowBound=0, cat= 'Integer')
x2313	=	p.LpVariable("	x2313	",lowBound=0, cat= 'Integer')
x2314	=	p.LpVariable("	x2314	",lowBound=0, cat= 'Integer')
x2315	=	p.LpVariable("	x2315	",lowBound=0, cat= 'Integer')
x2316	=	p.LpVariable("	x2316	",lowBound=0, cat= 'Integer')
x2317	=	p.LpVariable("	x2317	",lowBound=0, cat= 'Integer')
x2318	=	p.LpVariable("	x2318	",lowBound=0, cat= 'Integer')
x2319	=	p.LpVariable("	x2319	",lowBound=0, cat= 'Integer')
x2320	=	p.LpVariable("	x2320	",lowBound=0, cat= 'Integer')
x2321	=	p.LpVariable("	x2321	",lowBound=0, cat= 'Integer')
x2322	=	p.LpVariable("	x2322	",lowBound=0, cat= 'Integer')
x2323	=	p.LpVariable("	x2323	",lowBound=0, cat= 'Integer')
x2324	=	p.LpVariable("	x2324	",lowBound=0, cat= 'Integer')
x2325	=	p.LpVariable("	x2325	",lowBound=0, cat= 'Integer')
x2326	=	p.LpVariable("	x2326	",lowBound=0, cat= 'Integer')
x2327	=	p.LpVariable("	x2327	",lowBound=0, cat= 'Integer')
x2328	=	p.LpVariable("	x2328	",lowBound=0, cat= 'Integer')
x2329	=	p.LpVariable("	x2329	",lowBound=0, cat= 'Integer')
x2330	=	p.LpVariable("	x2330	",lowBound=0, cat= 'Integer')
x2331	=	p.LpVariable("	x2331	",lowBound=0, cat= 'Integer')
x2332	=	p.LpVariable("	x2332	",lowBound=0, cat= 'Integer')
x2333	=	p.LpVariable("	x2333	",lowBound=0, cat= 'Integer')
x2334	=	p.LpVariable("	x2334	",lowBound=0, cat= 'Integer')
x2335	=	p.LpVariable("	x2335	",lowBound=0, cat= 'Integer')
x2336	=	p.LpVariable("	x2336	",lowBound=0, cat= 'Integer')
x2337	=	p.LpVariable("	x2337	",lowBound=0, cat= 'Integer')
x2338	=	p.LpVariable("	x2338	",lowBound=0, cat= 'Integer')
x2339	=	p.LpVariable("	x2339	",lowBound=0, cat= 'Integer')
x2340	=	p.LpVariable("	x2340	",lowBound=0, cat= 'Integer')
x2341	=	p.LpVariable("	x2341	",lowBound=0, cat= 'Integer')
x2342	=	p.LpVariable("	x2342	",lowBound=0, cat= 'Integer')
x2343	=	p.LpVariable("	x2343	",lowBound=0, cat= 'Integer')
x2344	=	p.LpVariable("	x2344	",lowBound=0, cat= 'Integer')
x2345	=	p.LpVariable("	x2345	",lowBound=0, cat= 'Integer')
x2346	=	p.LpVariable("	x2346	",lowBound=0, cat= 'Integer')
x2347	=	p.LpVariable("	x2347	",lowBound=0, cat= 'Integer')
x2348	=	p.LpVariable("	x2348	",lowBound=0, cat= 'Integer')
x2349	=	p.LpVariable("	x2349	",lowBound=0, cat= 'Integer')
x2350	=	p.LpVariable("	x2350	",lowBound=0, cat= 'Integer')
x2351	=	p.LpVariable("	x2351	",lowBound=0, cat= 'Integer')
x2352	=	p.LpVariable("	x2352	",lowBound=0, cat= 'Integer')
x2353	=	p.LpVariable("	x2353	",lowBound=0, cat= 'Integer')
x2354	=	p.LpVariable("	x2354	",lowBound=0, cat= 'Integer')
x2355	=	p.LpVariable("	x2355	",lowBound=0, cat= 'Integer')
x2356	=	p.LpVariable("	x2356	",lowBound=0, cat= 'Integer')
x2357	=	p.LpVariable("	x2357	",lowBound=0, cat= 'Integer')
x2358	=	p.LpVariable("	x2358	",lowBound=0, cat= 'Integer')
x2359	=	p.LpVariable("	x2359	",lowBound=0, cat= 'Integer')
x2360	=	p.LpVariable("	x2360	",lowBound=0, cat= 'Integer')
x2361	=	p.LpVariable("	x2361	",lowBound=0, cat= 'Integer')
x2362	=	p.LpVariable("	x2362	",lowBound=0, cat= 'Integer')
x2363	=	p.LpVariable("	x2363	",lowBound=0, cat= 'Integer')
x2364	=	p.LpVariable("	x2364	",lowBound=0, cat= 'Integer')
x2365	=	p.LpVariable("	x2365	",lowBound=0, cat= 'Integer')
x2366	=	p.LpVariable("	x2366	",lowBound=0, cat= 'Integer')
x2367	=	p.LpVariable("	x2367	",lowBound=0, cat= 'Integer')
x2368	=	p.LpVariable("	x2368	",lowBound=0, cat= 'Integer')
x2369	=	p.LpVariable("	x2369	",lowBound=0, cat= 'Integer')
x2370	=	p.LpVariable("	x2370	",lowBound=0, cat= 'Integer')
x2371	=	p.LpVariable("	x2371	",lowBound=0, cat= 'Integer')
x2372	=	p.LpVariable("	x2372	",lowBound=0, cat= 'Integer')
x2373	=	p.LpVariable("	x2373	",lowBound=0, cat= 'Integer')
x2374	=	p.LpVariable("	x2374	",lowBound=0, cat= 'Integer')
x2375	=	p.LpVariable("	x2375	",lowBound=0, cat= 'Integer')
x2376	=	p.LpVariable("	x2376	",lowBound=0, cat= 'Integer')
x2377	=	p.LpVariable("	x2377	",lowBound=0, cat= 'Integer')
x2378	=	p.LpVariable("	x2378	",lowBound=0, cat= 'Integer')
x2379	=	p.LpVariable("	x2379	",lowBound=0, cat= 'Integer')
x2380	=	p.LpVariable("	x2380	",lowBound=0, cat= 'Integer')
x2381	=	p.LpVariable("	x2381	",lowBound=0, cat= 'Integer')
x2382	=	p.LpVariable("	x2382	",lowBound=0, cat= 'Integer')
x2383	=	p.LpVariable("	x2383	",lowBound=0, cat= 'Integer')
x2384	=	p.LpVariable("	x2384	",lowBound=0, cat= 'Integer')
x2385	=	p.LpVariable("	x2385	",lowBound=0, cat= 'Integer')
x2386	=	p.LpVariable("	x2386	",lowBound=0, cat= 'Integer')
x2387	=	p.LpVariable("	x2387	",lowBound=0, cat= 'Integer')
x2388	=	p.LpVariable("	x2388	",lowBound=0, cat= 'Integer')
x2389	=	p.LpVariable("	x2389	",lowBound=0, cat= 'Integer')
x2390	=	p.LpVariable("	x2390	",lowBound=0, cat= 'Integer')
x2391	=	p.LpVariable("	x2391	",lowBound=0, cat= 'Integer')
x2392	=	p.LpVariable("	x2392	",lowBound=0, cat= 'Integer')
x2393	=	p.LpVariable("	x2393	",lowBound=0, cat= 'Integer')
x2394	=	p.LpVariable("	x2394	",lowBound=0, cat= 'Integer')
x2395	=	p.LpVariable("	x2395	",lowBound=0, cat= 'Integer')
x2396	=	p.LpVariable("	x2396	",lowBound=0, cat= 'Integer')
x2397	=	p.LpVariable("	x2397	",lowBound=0, cat= 'Integer')
x2398	=	p.LpVariable("	x2398	",lowBound=0, cat= 'Integer')
x2399	=	p.LpVariable("	x2399	",lowBound=0, cat= 'Integer')
x2400	=	p.LpVariable("	x2400	",lowBound=0, cat= 'Integer')
x2401	=	p.LpVariable("	x2401	",lowBound=0, cat= 'Integer')
x2402	=	p.LpVariable("	x2402	",lowBound=0, cat= 'Integer')
x2403	=	p.LpVariable("	x2403	",lowBound=0, cat= 'Integer')
x2404	=	p.LpVariable("	x2404	",lowBound=0, cat= 'Integer')
x2405	=	p.LpVariable("	x2405	",lowBound=0, cat= 'Integer')
x2406	=	p.LpVariable("	x2406	",lowBound=0, cat= 'Integer')
x2407	=	p.LpVariable("	x2407	",lowBound=0, cat= 'Integer')
x2408	=	p.LpVariable("	x2408	",lowBound=0, cat= 'Integer')
x2409	=	p.LpVariable("	x2409	",lowBound=0, cat= 'Integer')
x2410	=	p.LpVariable("	x2410	",lowBound=0, cat= 'Integer')
x2411	=	p.LpVariable("	x2411	",lowBound=0, cat= 'Integer')
x2412	=	p.LpVariable("	x2412	",lowBound=0, cat= 'Integer')
x2413	=	p.LpVariable("	x2413	",lowBound=0, cat= 'Integer')
x2414	=	p.LpVariable("	x2414	",lowBound=0, cat= 'Integer')
x2415	=	p.LpVariable("	x2415	",lowBound=0, cat= 'Integer')
x2416	=	p.LpVariable("	x2416	",lowBound=0, cat= 'Integer')
x2417	=	p.LpVariable("	x2417	",lowBound=0, cat= 'Integer')
x2418	=	p.LpVariable("	x2418	",lowBound=0, cat= 'Integer')
x2419	=	p.LpVariable("	x2419	",lowBound=0, cat= 'Integer')
x2420	=	p.LpVariable("	x2420	",lowBound=0, cat= 'Integer')
x2421	=	p.LpVariable("	x2421	",lowBound=0, cat= 'Integer')
x2422	=	p.LpVariable("	x2422	",lowBound=0, cat= 'Integer')
x2423	=	p.LpVariable("	x2423	",lowBound=0, cat= 'Integer')
x2424	=	p.LpVariable("	x2424	",lowBound=0, cat= 'Integer')
x2425	=	p.LpVariable("	x2425	",lowBound=0, cat= 'Integer')
x2426	=	p.LpVariable("	x2426	",lowBound=0, cat= 'Integer')
x2427	=	p.LpVariable("	x2427	",lowBound=0, cat= 'Integer')
x2428	=	p.LpVariable("	x2428	",lowBound=0, cat= 'Integer')
x2429	=	p.LpVariable("	x2429	",lowBound=0, cat= 'Integer')
x2430	=	p.LpVariable("	x2430	",lowBound=0, cat= 'Integer')
x2431	=	p.LpVariable("	x2431	",lowBound=0, cat= 'Integer')
x2432	=	p.LpVariable("	x2432	",lowBound=0, cat= 'Integer')
x2433	=	p.LpVariable("	x2433	",lowBound=0, cat= 'Integer')
x2434	=	p.LpVariable("	x2434	",lowBound=0, cat= 'Integer')
x2435	=	p.LpVariable("	x2435	",lowBound=0, cat= 'Integer')
x2436	=	p.LpVariable("	x2436	",lowBound=0, cat= 'Integer')
x2437	=	p.LpVariable("	x2437	",lowBound=0, cat= 'Integer')
x2438	=	p.LpVariable("	x2438	",lowBound=0, cat= 'Integer')
x2439	=	p.LpVariable("	x2439	",lowBound=0, cat= 'Integer')
x2440	=	p.LpVariable("	x2440	",lowBound=0, cat= 'Integer')
x2441	=	p.LpVariable("	x2441	",lowBound=0, cat= 'Integer')
x2442	=	p.LpVariable("	x2442	",lowBound=0, cat= 'Integer')
x2443	=	p.LpVariable("	x2443	",lowBound=0, cat= 'Integer')
x2444	=	p.LpVariable("	x2444	",lowBound=0, cat= 'Integer')
x2445	=	p.LpVariable("	x2445	",lowBound=0, cat= 'Integer')
x2446	=	p.LpVariable("	x2446	",lowBound=0, cat= 'Integer')
x2447	=	p.LpVariable("	x2447	",lowBound=0, cat= 'Integer')
x2448	=	p.LpVariable("	x2448	",lowBound=0, cat= 'Integer')
x2449	=	p.LpVariable("	x2449	",lowBound=0, cat= 'Integer')
x2450	=	p.LpVariable("	x2450	",lowBound=0, cat= 'Integer')
x2451	=	p.LpVariable("	x2451	",lowBound=0, cat= 'Integer')
x2452	=	p.LpVariable("	x2452	",lowBound=0, cat= 'Integer')
x2453	=	p.LpVariable("	x2453	",lowBound=0, cat= 'Integer')
x2454	=	p.LpVariable("	x2454	",lowBound=0, cat= 'Integer')
x2455	=	p.LpVariable("	x2455	",lowBound=0, cat= 'Integer')
x2456	=	p.LpVariable("	x2456	",lowBound=0, cat= 'Integer')
x2457	=	p.LpVariable("	x2457	",lowBound=0, cat= 'Integer')
x2458	=	p.LpVariable("	x2458	",lowBound=0, cat= 'Integer')
x2459	=	p.LpVariable("	x2459	",lowBound=0, cat= 'Integer')
x2460	=	p.LpVariable("	x2460	",lowBound=0, cat= 'Integer')
x2461	=	p.LpVariable("	x2461	",lowBound=0, cat= 'Integer')
x2462	=	p.LpVariable("	x2462	",lowBound=0, cat= 'Integer')
x2463	=	p.LpVariable("	x2463	",lowBound=0, cat= 'Integer')
x2464	=	p.LpVariable("	x2464	",lowBound=0, cat= 'Integer')
x2465	=	p.LpVariable("	x2465	",lowBound=0, cat= 'Integer')
x2466	=	p.LpVariable("	x2466	",lowBound=0, cat= 'Integer')
x2467	=	p.LpVariable("	x2467	",lowBound=0, cat= 'Integer')
x2468	=	p.LpVariable("	x2468	",lowBound=0, cat= 'Integer')
x2469	=	p.LpVariable("	x2469	",lowBound=0, cat= 'Integer')
x2470	=	p.LpVariable("	x2470	",lowBound=0, cat= 'Integer')
x2471	=	p.LpVariable("	x2471	",lowBound=0, cat= 'Integer')
x2472	=	p.LpVariable("	x2472	",lowBound=0, cat= 'Integer')
x2473	=	p.LpVariable("	x2473	",lowBound=0, cat= 'Integer')
x2474	=	p.LpVariable("	x2474	",lowBound=0, cat= 'Integer')
x2475	=	p.LpVariable("	x2475	",lowBound=0, cat= 'Integer')
x2476	=	p.LpVariable("	x2476	",lowBound=0, cat= 'Integer')
x2477	=	p.LpVariable("	x2477	",lowBound=0, cat= 'Integer')
x2478	=	p.LpVariable("	x2478	",lowBound=0, cat= 'Integer')
x2479	=	p.LpVariable("	x2479	",lowBound=0, cat= 'Integer')
x2480	=	p.LpVariable("	x2480	",lowBound=0, cat= 'Integer')
x2481	=	p.LpVariable("	x2481	",lowBound=0, cat= 'Integer')
x2482	=	p.LpVariable("	x2482	",lowBound=0, cat= 'Integer')
x2483	=	p.LpVariable("	x2483	",lowBound=0, cat= 'Integer')
x2484	=	p.LpVariable("	x2484	",lowBound=0, cat= 'Integer')
x2485	=	p.LpVariable("	x2485	",lowBound=0, cat= 'Integer')
x2486	=	p.LpVariable("	x2486	",lowBound=0, cat= 'Integer')
x2487	=	p.LpVariable("	x2487	",lowBound=0, cat= 'Integer')
x2488	=	p.LpVariable("	x2488	",lowBound=0, cat= 'Integer')
x2489	=	p.LpVariable("	x2489	",lowBound=0, cat= 'Integer')
x2490	=	p.LpVariable("	x2490	",lowBound=0, cat= 'Integer')
x2491	=	p.LpVariable("	x2491	",lowBound=0, cat= 'Integer')
x2492	=	p.LpVariable("	x2492	",lowBound=0, cat= 'Integer')
x2493	=	p.LpVariable("	x2493	",lowBound=0, cat= 'Integer')
x2494	=	p.LpVariable("	x2494	",lowBound=0, cat= 'Integer')
x2495	=	p.LpVariable("	x2495	",lowBound=0, cat= 'Integer')
x2496	=	p.LpVariable("	x2496	",lowBound=0, cat= 'Integer')
x2497	=	p.LpVariable("	x2497	",lowBound=0, cat= 'Integer')
x2498	=	p.LpVariable("	x2498	",lowBound=0, cat= 'Integer')
x2499	=	p.LpVariable("	x2499	",lowBound=0, cat= 'Integer')
x2500	=	p.LpVariable("	x2500	",lowBound=0, cat= 'Integer')
x2501	=	p.LpVariable("	x2501	",lowBound=0, cat= 'Integer')
x2502	=	p.LpVariable("	x2502	",lowBound=0, cat= 'Integer')
x2503	=	p.LpVariable("	x2503	",lowBound=0, cat= 'Integer')
x2504	=	p.LpVariable("	x2504	",lowBound=0, cat= 'Integer')
x2505	=	p.LpVariable("	x2505	",lowBound=0, cat= 'Integer')
x2506	=	p.LpVariable("	x2506	",lowBound=0, cat= 'Integer')
x2507	=	p.LpVariable("	x2507	",lowBound=0, cat= 'Integer')
x2508	=	p.LpVariable("	x2508	",lowBound=0, cat= 'Integer')
x2509	=	p.LpVariable("	x2509	",lowBound=0, cat= 'Integer')
x2510	=	p.LpVariable("	x2510	",lowBound=0, cat= 'Integer')
x2511	=	p.LpVariable("	x2511	",lowBound=0, cat= 'Integer')
x2512	=	p.LpVariable("	x2512	",lowBound=0, cat= 'Integer')
x2513	=	p.LpVariable("	x2513	",lowBound=0, cat= 'Integer')
x2514	=	p.LpVariable("	x2514	",lowBound=0, cat= 'Integer')
x2515	=	p.LpVariable("	x2515	",lowBound=0, cat= 'Integer')
x2516	=	p.LpVariable("	x2516	",lowBound=0, cat= 'Integer')
x2517	=	p.LpVariable("	x2517	",lowBound=0, cat= 'Integer')
x2518	=	p.LpVariable("	x2518	",lowBound=0, cat= 'Integer')
x2519	=	p.LpVariable("	x2519	",lowBound=0, cat= 'Integer')
x2520	=	p.LpVariable("	x2520	",lowBound=0, cat= 'Integer')
x2521	=	p.LpVariable("	x2521	",lowBound=0, cat= 'Integer')
x2522	=	p.LpVariable("	x2522	",lowBound=0, cat= 'Integer')
x2523	=	p.LpVariable("	x2523	",lowBound=0, cat= 'Integer')
x2524	=	p.LpVariable("	x2524	",lowBound=0, cat= 'Integer')
x2525	=	p.LpVariable("	x2525	",lowBound=0, cat= 'Integer')
x2526	=	p.LpVariable("	x2526	",lowBound=0, cat= 'Integer')
x2527	=	p.LpVariable("	x2527	",lowBound=0, cat= 'Integer')
x2528	=	p.LpVariable("	x2528	",lowBound=0, cat= 'Integer')
x2529	=	p.LpVariable("	x2529	",lowBound=0, cat= 'Integer')
x2530	=	p.LpVariable("	x2530	",lowBound=0, cat= 'Integer')
x2531	=	p.LpVariable("	x2531	",lowBound=0, cat= 'Integer')
x2532	=	p.LpVariable("	x2532	",lowBound=0, cat= 'Integer')
x2533	=	p.LpVariable("	x2533	",lowBound=0, cat= 'Integer')
x2534	=	p.LpVariable("	x2534	",lowBound=0, cat= 'Integer')
x2535	=	p.LpVariable("	x2535	",lowBound=0, cat= 'Integer')
x2536	=	p.LpVariable("	x2536	",lowBound=0, cat= 'Integer')
x2537	=	p.LpVariable("	x2537	",lowBound=0, cat= 'Integer')
x2538	=	p.LpVariable("	x2538	",lowBound=0, cat= 'Integer')
x2539	=	p.LpVariable("	x2539	",lowBound=0, cat= 'Integer')
x2540	=	p.LpVariable("	x2540	",lowBound=0, cat= 'Integer')
x2541	=	p.LpVariable("	x2541	",lowBound=0, cat= 'Integer')
x2542	=	p.LpVariable("	x2542	",lowBound=0, cat= 'Integer')
x2543	=	p.LpVariable("	x2543	",lowBound=0, cat= 'Integer')
x2544	=	p.LpVariable("	x2544	",lowBound=0, cat= 'Integer')
x2545	=	p.LpVariable("	x2545	",lowBound=0, cat= 'Integer')
x2546	=	p.LpVariable("	x2546	",lowBound=0, cat= 'Integer')
x2547	=	p.LpVariable("	x2547	",lowBound=0, cat= 'Integer')
x2548	=	p.LpVariable("	x2548	",lowBound=0, cat= 'Integer')
x2549	=	p.LpVariable("	x2549	",lowBound=0, cat= 'Integer')
x2550	=	p.LpVariable("	x2550	",lowBound=0, cat= 'Integer')
x2551	=	p.LpVariable("	x2551	",lowBound=0, cat= 'Integer')
x2552	=	p.LpVariable("	x2552	",lowBound=0, cat= 'Integer')
x2553	=	p.LpVariable("	x2553	",lowBound=0, cat= 'Integer')
x2554	=	p.LpVariable("	x2554	",lowBound=0, cat= 'Integer')
x2555	=	p.LpVariable("	x2555	",lowBound=0, cat= 'Integer')
x2556	=	p.LpVariable("	x2556	",lowBound=0, cat= 'Integer')
x2557	=	p.LpVariable("	x2557	",lowBound=0, cat= 'Integer')
x2558	=	p.LpVariable("	x2558	",lowBound=0, cat= 'Integer')
x2559	=	p.LpVariable("	x2559	",lowBound=0, cat= 'Integer')
x2560	=	p.LpVariable("	x2560	",lowBound=0, cat= 'Integer')
x2561	=	p.LpVariable("	x2561	",lowBound=0, cat= 'Integer')
x2562	=	p.LpVariable("	x2562	",lowBound=0, cat= 'Integer')
x2563	=	p.LpVariable("	x2563	",lowBound=0, cat= 'Integer')
x2564	=	p.LpVariable("	x2564	",lowBound=0, cat= 'Integer')
x2565	=	p.LpVariable("	x2565	",lowBound=0, cat= 'Integer')
x2566	=	p.LpVariable("	x2566	",lowBound=0, cat= 'Integer')
x2567	=	p.LpVariable("	x2567	",lowBound=0, cat= 'Integer')
x2568	=	p.LpVariable("	x2568	",lowBound=0, cat= 'Integer')
x2569	=	p.LpVariable("	x2569	",lowBound=0, cat= 'Integer')
x2570	=	p.LpVariable("	x2570	",lowBound=0, cat= 'Integer')
x2571	=	p.LpVariable("	x2571	",lowBound=0, cat= 'Integer')
x2572	=	p.LpVariable("	x2572	",lowBound=0, cat= 'Integer')
x2573	=	p.LpVariable("	x2573	",lowBound=0, cat= 'Integer')
x2574	=	p.LpVariable("	x2574	",lowBound=0, cat= 'Integer')
x2575	=	p.LpVariable("	x2575	",lowBound=0, cat= 'Integer')
x2576	=	p.LpVariable("	x2576	",lowBound=0, cat= 'Integer')
x2577	=	p.LpVariable("	x2577	",lowBound=0, cat= 'Integer')
x2578	=	p.LpVariable("	x2578	",lowBound=0, cat= 'Integer')
x2579	=	p.LpVariable("	x2579	",lowBound=0, cat= 'Integer')
x2580	=	p.LpVariable("	x2580	",lowBound=0, cat= 'Integer')
x2581	=	p.LpVariable("	x2581	",lowBound=0, cat= 'Integer')
x2582	=	p.LpVariable("	x2582	",lowBound=0, cat= 'Integer')
x2583	=	p.LpVariable("	x2583	",lowBound=0, cat= 'Integer')
x2584	=	p.LpVariable("	x2584	",lowBound=0, cat= 'Integer')
x2585	=	p.LpVariable("	x2585	",lowBound=0, cat= 'Integer')
x2586	=	p.LpVariable("	x2586	",lowBound=0, cat= 'Integer')
x2587	=	p.LpVariable("	x2587	",lowBound=0, cat= 'Integer')
x2588	=	p.LpVariable("	x2588	",lowBound=0, cat= 'Integer')
x2589	=	p.LpVariable("	x2589	",lowBound=0, cat= 'Integer')
x2590	=	p.LpVariable("	x2590	",lowBound=0, cat= 'Integer')
x2591	=	p.LpVariable("	x2591	",lowBound=0, cat= 'Integer')
x2592	=	p.LpVariable("	x2592	",lowBound=0, cat= 'Integer')
x2593	=	p.LpVariable("	x2593	",lowBound=0, cat= 'Integer')
x2594	=	p.LpVariable("	x2594	",lowBound=0, cat= 'Integer')
x2595	=	p.LpVariable("	x2595	",lowBound=0, cat= 'Integer')
x2596	=	p.LpVariable("	x2596	",lowBound=0, cat= 'Integer')
x2597	=	p.LpVariable("	x2597	",lowBound=0, cat= 'Integer')
x2598	=	p.LpVariable("	x2598	",lowBound=0, cat= 'Integer')
x2599	=	p.LpVariable("	x2599	",lowBound=0, cat= 'Integer')
x2600	=	p.LpVariable("	x2600	",lowBound=0, cat= 'Integer')
x2601	=	p.LpVariable("	x2601	",lowBound=0, cat= 'Integer')
x2602	=	p.LpVariable("	x2602	",lowBound=0, cat= 'Integer')
x2603	=	p.LpVariable("	x2603	",lowBound=0, cat= 'Integer')
x2604	=	p.LpVariable("	x2604	",lowBound=0, cat= 'Integer')
x2605	=	p.LpVariable("	x2605	",lowBound=0, cat= 'Integer')
x2606	=	p.LpVariable("	x2606	",lowBound=0, cat= 'Integer')
x2607	=	p.LpVariable("	x2607	",lowBound=0, cat= 'Integer')
x2608	=	p.LpVariable("	x2608	",lowBound=0, cat= 'Integer')
x2609	=	p.LpVariable("	x2609	",lowBound=0, cat= 'Integer')
x2610	=	p.LpVariable("	x2610	",lowBound=0, cat= 'Integer')
x2611	=	p.LpVariable("	x2611	",lowBound=0, cat= 'Integer')
x2612	=	p.LpVariable("	x2612	",lowBound=0, cat= 'Integer')
x2613	=	p.LpVariable("	x2613	",lowBound=0, cat= 'Integer')
x2614	=	p.LpVariable("	x2614	",lowBound=0, cat= 'Integer')
x2615	=	p.LpVariable("	x2615	",lowBound=0, cat= 'Integer')
x2616	=	p.LpVariable("	x2616	",lowBound=0, cat= 'Integer')
x2617	=	p.LpVariable("	x2617	",lowBound=0, cat= 'Integer')
x2618	=	p.LpVariable("	x2618	",lowBound=0, cat= 'Integer')
x2619	=	p.LpVariable("	x2619	",lowBound=0, cat= 'Integer')
x2620	=	p.LpVariable("	x2620	",lowBound=0, cat= 'Integer')
x2621	=	p.LpVariable("	x2621	",lowBound=0, cat= 'Integer')
x2622	=	p.LpVariable("	x2622	",lowBound=0, cat= 'Integer')
x2623	=	p.LpVariable("	x2623	",lowBound=0, cat= 'Integer')
x2624	=	p.LpVariable("	x2624	",lowBound=0, cat= 'Integer')
x2625	=	p.LpVariable("	x2625	",lowBound=0, cat= 'Integer')
x2626	=	p.LpVariable("	x2626	",lowBound=0, cat= 'Integer')
x2627	=	p.LpVariable("	x2627	",lowBound=0, cat= 'Integer')
x2628	=	p.LpVariable("	x2628	",lowBound=0, cat= 'Integer')
x2629	=	p.LpVariable("	x2629	",lowBound=0, cat= 'Integer')
x2630	=	p.LpVariable("	x2630	",lowBound=0, cat= 'Integer')
x2631	=	p.LpVariable("	x2631	",lowBound=0, cat= 'Integer')
x2632	=	p.LpVariable("	x2632	",lowBound=0, cat= 'Integer')
x2633	=	p.LpVariable("	x2633	",lowBound=0, cat= 'Integer')
x2634	=	p.LpVariable("	x2634	",lowBound=0, cat= 'Integer')
x2635	=	p.LpVariable("	x2635	",lowBound=0, cat= 'Integer')
x2636	=	p.LpVariable("	x2636	",lowBound=0, cat= 'Integer')
x2637	=	p.LpVariable("	x2637	",lowBound=0, cat= 'Integer')
x2638	=	p.LpVariable("	x2638	",lowBound=0, cat= 'Integer')
x2639	=	p.LpVariable("	x2639	",lowBound=0, cat= 'Integer')
x2640	=	p.LpVariable("	x2640	",lowBound=0, cat= 'Integer')
x2641	=	p.LpVariable("	x2641	",lowBound=0, cat= 'Integer')
x2642	=	p.LpVariable("	x2642	",lowBound=0, cat= 'Integer')
x2643	=	p.LpVariable("	x2643	",lowBound=0, cat= 'Integer')
x2644	=	p.LpVariable("	x2644	",lowBound=0, cat= 'Integer')
x2645	=	p.LpVariable("	x2645	",lowBound=0, cat= 'Integer')
x2646	=	p.LpVariable("	x2646	",lowBound=0, cat= 'Integer')
x2647	=	p.LpVariable("	x2647	",lowBound=0, cat= 'Integer')
x2648	=	p.LpVariable("	x2648	",lowBound=0, cat= 'Integer')
x2649	=	p.LpVariable("	x2649	",lowBound=0, cat= 'Integer')
x2650	=	p.LpVariable("	x2650	",lowBound=0, cat= 'Integer')
x2651	=	p.LpVariable("	x2651	",lowBound=0, cat= 'Integer')
x2652	=	p.LpVariable("	x2652	",lowBound=0, cat= 'Integer')
x2653	=	p.LpVariable("	x2653	",lowBound=0, cat= 'Integer')
x2654	=	p.LpVariable("	x2654	",lowBound=0, cat= 'Integer')
x2655	=	p.LpVariable("	x2655	",lowBound=0, cat= 'Integer')
x2656	=	p.LpVariable("	x2656	",lowBound=0, cat= 'Integer')
x2657	=	p.LpVariable("	x2657	",lowBound=0, cat= 'Integer')
x2658	=	p.LpVariable("	x2658	",lowBound=0, cat= 'Integer')
x2659	=	p.LpVariable("	x2659	",lowBound=0, cat= 'Integer')
x2660	=	p.LpVariable("	x2660	",lowBound=0, cat= 'Integer')
x2661	=	p.LpVariable("	x2661	",lowBound=0, cat= 'Integer')
x2662	=	p.LpVariable("	x2662	",lowBound=0, cat= 'Integer')
x2663	=	p.LpVariable("	x2663	",lowBound=0, cat= 'Integer')
x2664	=	p.LpVariable("	x2664	",lowBound=0, cat= 'Integer')
x2665	=	p.LpVariable("	x2665	",lowBound=0, cat= 'Integer')
x2666	=	p.LpVariable("	x2666	",lowBound=0, cat= 'Integer')
x2667	=	p.LpVariable("	x2667	",lowBound=0, cat= 'Integer')
x2668	=	p.LpVariable("	x2668	",lowBound=0, cat= 'Integer')
x2669	=	p.LpVariable("	x2669	",lowBound=0, cat= 'Integer')
x2670	=	p.LpVariable("	x2670	",lowBound=0, cat= 'Integer')
x2671	=	p.LpVariable("	x2671	",lowBound=0, cat= 'Integer')
x2672	=	p.LpVariable("	x2672	",lowBound=0, cat= 'Integer')
x2673	=	p.LpVariable("	x2673	",lowBound=0, cat= 'Integer')
x2674	=	p.LpVariable("	x2674	",lowBound=0, cat= 'Integer')
x2675	=	p.LpVariable("	x2675	",lowBound=0, cat= 'Integer')
x2676	=	p.LpVariable("	x2676	",lowBound=0, cat= 'Integer')
x2677	=	p.LpVariable("	x2677	",lowBound=0, cat= 'Integer')
x2678	=	p.LpVariable("	x2678	",lowBound=0, cat= 'Integer')
x2679	=	p.LpVariable("	x2679	",lowBound=0, cat= 'Integer')
x2680	=	p.LpVariable("	x2680	",lowBound=0, cat= 'Integer')
x2681	=	p.LpVariable("	x2681	",lowBound=0, cat= 'Integer')
x2682	=	p.LpVariable("	x2682	",lowBound=0, cat= 'Integer')
x2683	=	p.LpVariable("	x2683	",lowBound=0, cat= 'Integer')
x2684	=	p.LpVariable("	x2684	",lowBound=0, cat= 'Integer')
x2685	=	p.LpVariable("	x2685	",lowBound=0, cat= 'Integer')
x2686	=	p.LpVariable("	x2686	",lowBound=0, cat= 'Integer')
x2687	=	p.LpVariable("	x2687	",lowBound=0, cat= 'Integer')
x2688	=	p.LpVariable("	x2688	",lowBound=0, cat= 'Integer')
x2689	=	p.LpVariable("	x2689	",lowBound=0, cat= 'Integer')
x2690	=	p.LpVariable("	x2690	",lowBound=0, cat= 'Integer')
x2691	=	p.LpVariable("	x2691	",lowBound=0, cat= 'Integer')
x2692	=	p.LpVariable("	x2692	",lowBound=0, cat= 'Integer')
x2693	=	p.LpVariable("	x2693	",lowBound=0, cat= 'Integer')
x2694	=	p.LpVariable("	x2694	",lowBound=0, cat= 'Integer')
x2695	=	p.LpVariable("	x2695	",lowBound=0, cat= 'Integer')
x2696	=	p.LpVariable("	x2696	",lowBound=0, cat= 'Integer')
x2697	=	p.LpVariable("	x2697	",lowBound=0, cat= 'Integer')
x2698	=	p.LpVariable("	x2698	",lowBound=0, cat= 'Integer')
x2699	=	p.LpVariable("	x2699	",lowBound=0, cat= 'Integer')
x2700	=	p.LpVariable("	x2700	",lowBound=0, cat= 'Integer')
x2701	=	p.LpVariable("	x2701	",lowBound=0, cat= 'Integer')
x2702	=	p.LpVariable("	x2702	",lowBound=0, cat= 'Integer')
x2703	=	p.LpVariable("	x2703	",lowBound=0, cat= 'Integer')
x2704	=	p.LpVariable("	x2704	",lowBound=0, cat= 'Integer')
x2705	=	p.LpVariable("	x2705	",lowBound=0, cat= 'Integer')
x2706	=	p.LpVariable("	x2706	",lowBound=0, cat= 'Integer')
x2707	=	p.LpVariable("	x2707	",lowBound=0, cat= 'Integer')
x2708	=	p.LpVariable("	x2708	",lowBound=0, cat= 'Integer')
x2709	=	p.LpVariable("	x2709	",lowBound=0, cat= 'Integer')
x2710	=	p.LpVariable("	x2710	",lowBound=0, cat= 'Integer')
x2711	=	p.LpVariable("	x2711	",lowBound=0, cat= 'Integer')
x2712	=	p.LpVariable("	x2712	",lowBound=0, cat= 'Integer')
x2713	=	p.LpVariable("	x2713	",lowBound=0, cat= 'Integer')
x2714	=	p.LpVariable("	x2714	",lowBound=0, cat= 'Integer')
x2715	=	p.LpVariable("	x2715	",lowBound=0, cat= 'Integer')
x2716	=	p.LpVariable("	x2716	",lowBound=0, cat= 'Integer')
x2717	=	p.LpVariable("	x2717	",lowBound=0, cat= 'Integer')
x2718	=	p.LpVariable("	x2718	",lowBound=0, cat= 'Integer')
x2719	=	p.LpVariable("	x2719	",lowBound=0, cat= 'Integer')
x2720	=	p.LpVariable("	x2720	",lowBound=0, cat= 'Integer')
x2721	=	p.LpVariable("	x2721	",lowBound=0, cat= 'Integer')
x2722	=	p.LpVariable("	x2722	",lowBound=0, cat= 'Integer')
x2723	=	p.LpVariable("	x2723	",lowBound=0, cat= 'Integer')
x2724	=	p.LpVariable("	x2724	",lowBound=0, cat= 'Integer')
x2725	=	p.LpVariable("	x2725	",lowBound=0, cat= 'Integer')
x2726	=	p.LpVariable("	x2726	",lowBound=0, cat= 'Integer')
x2727	=	p.LpVariable("	x2727	",lowBound=0, cat= 'Integer')
x2728	=	p.LpVariable("	x2728	",lowBound=0, cat= 'Integer')
x2729	=	p.LpVariable("	x2729	",lowBound=0, cat= 'Integer')
x2730	=	p.LpVariable("	x2730	",lowBound=0, cat= 'Integer')
x2731	=	p.LpVariable("	x2731	",lowBound=0, cat= 'Integer')
x2732	=	p.LpVariable("	x2732	",lowBound=0, cat= 'Integer')
x2733	=	p.LpVariable("	x2733	",lowBound=0, cat= 'Integer')
x2734	=	p.LpVariable("	x2734	",lowBound=0, cat= 'Integer')
x2735	=	p.LpVariable("	x2735	",lowBound=0, cat= 'Integer')
x2736	=	p.LpVariable("	x2736	",lowBound=0, cat= 'Integer')
x2737	=	p.LpVariable("	x2737	",lowBound=0, cat= 'Integer')
x2738	=	p.LpVariable("	x2738	",lowBound=0, cat= 'Integer')
x2739	=	p.LpVariable("	x2739	",lowBound=0, cat= 'Integer')
x2740	=	p.LpVariable("	x2740	",lowBound=0, cat= 'Integer')
x2741	=	p.LpVariable("	x2741	",lowBound=0, cat= 'Integer')
x2742	=	p.LpVariable("	x2742	",lowBound=0, cat= 'Integer')
x2743	=	p.LpVariable("	x2743	",lowBound=0, cat= 'Integer')
x2744	=	p.LpVariable("	x2744	",lowBound=0, cat= 'Integer')
x2745	=	p.LpVariable("	x2745	",lowBound=0, cat= 'Integer')
x2746	=	p.LpVariable("	x2746	",lowBound=0, cat= 'Integer')
x2747	=	p.LpVariable("	x2747	",lowBound=0, cat= 'Integer')
x2748	=	p.LpVariable("	x2748	",lowBound=0, cat= 'Integer')
x2749	=	p.LpVariable("	x2749	",lowBound=0, cat= 'Integer')
x2750	=	p.LpVariable("	x2750	",lowBound=0, cat= 'Integer')
x2751	=	p.LpVariable("	x2751	",lowBound=0, cat= 'Integer')
x2752	=	p.LpVariable("	x2752	",lowBound=0, cat= 'Integer')
x2753	=	p.LpVariable("	x2753	",lowBound=0, cat= 'Integer')
x2754	=	p.LpVariable("	x2754	",lowBound=0, cat= 'Integer')
x2755	=	p.LpVariable("	x2755	",lowBound=0, cat= 'Integer')
x2756	=	p.LpVariable("	x2756	",lowBound=0, cat= 'Integer')
x2757	=	p.LpVariable("	x2757	",lowBound=0, cat= 'Integer')
x2758	=	p.LpVariable("	x2758	",lowBound=0, cat= 'Integer')
x2759	=	p.LpVariable("	x2759	",lowBound=0, cat= 'Integer')
x2760	=	p.LpVariable("	x2760	",lowBound=0, cat= 'Integer')
x2761	=	p.LpVariable("	x2761	",lowBound=0, cat= 'Integer')
x2762	=	p.LpVariable("	x2762	",lowBound=0, cat= 'Integer')
x2763	=	p.LpVariable("	x2763	",lowBound=0, cat= 'Integer')
x2764	=	p.LpVariable("	x2764	",lowBound=0, cat= 'Integer')
x2765	=	p.LpVariable("	x2765	",lowBound=0, cat= 'Integer')
x2766	=	p.LpVariable("	x2766	",lowBound=0, cat= 'Integer')
x2767	=	p.LpVariable("	x2767	",lowBound=0, cat= 'Integer')
x2768	=	p.LpVariable("	x2768	",lowBound=0, cat= 'Integer')
x2769	=	p.LpVariable("	x2769	",lowBound=0, cat= 'Integer')
x2770	=	p.LpVariable("	x2770	",lowBound=0, cat= 'Integer')
x2771	=	p.LpVariable("	x2771	",lowBound=0, cat= 'Integer')
x2772	=	p.LpVariable("	x2772	",lowBound=0, cat= 'Integer')
x2773	=	p.LpVariable("	x2773	",lowBound=0, cat= 'Integer')
x2774	=	p.LpVariable("	x2774	",lowBound=0, cat= 'Integer')
x2775	=	p.LpVariable("	x2775	",lowBound=0, cat= 'Integer')
x2776	=	p.LpVariable("	x2776	",lowBound=0, cat= 'Integer')
x2777	=	p.LpVariable("	x2777	",lowBound=0, cat= 'Integer')
x2778	=	p.LpVariable("	x2778	",lowBound=0, cat= 'Integer')
x2779	=	p.LpVariable("	x2779	",lowBound=0, cat= 'Integer')
x2780	=	p.LpVariable("	x2780	",lowBound=0, cat= 'Integer')
x2781	=	p.LpVariable("	x2781	",lowBound=0, cat= 'Integer')
x2782	=	p.LpVariable("	x2782	",lowBound=0, cat= 'Integer')
x2783	=	p.LpVariable("	x2783	",lowBound=0, cat= 'Integer')
x2784	=	p.LpVariable("	x2784	",lowBound=0, cat= 'Integer')
x2785	=	p.LpVariable("	x2785	",lowBound=0, cat= 'Integer')
x2786	=	p.LpVariable("	x2786	",lowBound=0, cat= 'Integer')
x2787	=	p.LpVariable("	x2787	",lowBound=0, cat= 'Integer')
x2788	=	p.LpVariable("	x2788	",lowBound=0, cat= 'Integer')
x2789	=	p.LpVariable("	x2789	",lowBound=0, cat= 'Integer')
x2790	=	p.LpVariable("	x2790	",lowBound=0, cat= 'Integer')
x2791	=	p.LpVariable("	x2791	",lowBound=0, cat= 'Integer')
x2792	=	p.LpVariable("	x2792	",lowBound=0, cat= 'Integer')
x2793	=	p.LpVariable("	x2793	",lowBound=0, cat= 'Integer')
x2794	=	p.LpVariable("	x2794	",lowBound=0, cat= 'Integer')
x2795	=	p.LpVariable("	x2795	",lowBound=0, cat= 'Integer')
x2796	=	p.LpVariable("	x2796	",lowBound=0, cat= 'Integer')
x2797	=	p.LpVariable("	x2797	",lowBound=0, cat= 'Integer')
x2798	=	p.LpVariable("	x2798	",lowBound=0, cat= 'Integer')
x2799	=	p.LpVariable("	x2799	",lowBound=0, cat= 'Integer')
x2800	=	p.LpVariable("	x2800	",lowBound=0, cat= 'Integer')
x2801	=	p.LpVariable("	x2801	",lowBound=0, cat= 'Integer')
x2802	=	p.LpVariable("	x2802	",lowBound=0, cat= 'Integer')
x2803	=	p.LpVariable("	x2803	",lowBound=0, cat= 'Integer')
x2804	=	p.LpVariable("	x2804	",lowBound=0, cat= 'Integer')
x2805	=	p.LpVariable("	x2805	",lowBound=0, cat= 'Integer')
x2806	=	p.LpVariable("	x2806	",lowBound=0, cat= 'Integer')
x2807	=	p.LpVariable("	x2807	",lowBound=0, cat= 'Integer')
x2808	=	p.LpVariable("	x2808	",lowBound=0, cat= 'Integer')
x2809	=	p.LpVariable("	x2809	",lowBound=0, cat= 'Integer')
x2810	=	p.LpVariable("	x2810	",lowBound=0, cat= 'Integer')
x2811	=	p.LpVariable("	x2811	",lowBound=0, cat= 'Integer')
x2812	=	p.LpVariable("	x2812	",lowBound=0, cat= 'Integer')
x2813	=	p.LpVariable("	x2813	",lowBound=0, cat= 'Integer')
x2814	=	p.LpVariable("	x2814	",lowBound=0, cat= 'Integer')
x2815	=	p.LpVariable("	x2815	",lowBound=0, cat= 'Integer')
x2816	=	p.LpVariable("	x2816	",lowBound=0, cat= 'Integer')
x2817	=	p.LpVariable("	x2817	",lowBound=0, cat= 'Integer')
x2818	=	p.LpVariable("	x2818	",lowBound=0, cat= 'Integer')
x2819	=	p.LpVariable("	x2819	",lowBound=0, cat= 'Integer')
x2820	=	p.LpVariable("	x2820	",lowBound=0, cat= 'Integer')
x2821	=	p.LpVariable("	x2821	",lowBound=0, cat= 'Integer')
x2822	=	p.LpVariable("	x2822	",lowBound=0, cat= 'Integer')
x2823	=	p.LpVariable("	x2823	",lowBound=0, cat= 'Integer')
x2824	=	p.LpVariable("	x2824	",lowBound=0, cat= 'Integer')
x2825	=	p.LpVariable("	x2825	",lowBound=0, cat= 'Integer')
x2826	=	p.LpVariable("	x2826	",lowBound=0, cat= 'Integer')
x2827	=	p.LpVariable("	x2827	",lowBound=0, cat= 'Integer')
x2828	=	p.LpVariable("	x2828	",lowBound=0, cat= 'Integer')
x2829	=	p.LpVariable("	x2829	",lowBound=0, cat= 'Integer')
x2830	=	p.LpVariable("	x2830	",lowBound=0, cat= 'Integer')
x2831	=	p.LpVariable("	x2831	",lowBound=0, cat= 'Integer')
x2832	=	p.LpVariable("	x2832	",lowBound=0, cat= 'Integer')
x2833	=	p.LpVariable("	x2833	",lowBound=0, cat= 'Integer')
x2834	=	p.LpVariable("	x2834	",lowBound=0, cat= 'Integer')
x2835	=	p.LpVariable("	x2835	",lowBound=0, cat= 'Integer')
x2836	=	p.LpVariable("	x2836	",lowBound=0, cat= 'Integer')
x2837	=	p.LpVariable("	x2837	",lowBound=0, cat= 'Integer')
x2838	=	p.LpVariable("	x2838	",lowBound=0, cat= 'Integer')
x2839	=	p.LpVariable("	x2839	",lowBound=0, cat= 'Integer')
x2840	=	p.LpVariable("	x2840	",lowBound=0, cat= 'Integer')
x2841	=	p.LpVariable("	x2841	",lowBound=0, cat= 'Integer')
x2842	=	p.LpVariable("	x2842	",lowBound=0, cat= 'Integer')
x2843	=	p.LpVariable("	x2843	",lowBound=0, cat= 'Integer')
x2844	=	p.LpVariable("	x2844	",lowBound=0, cat= 'Integer')
x2845	=	p.LpVariable("	x2845	",lowBound=0, cat= 'Integer')
x2846	=	p.LpVariable("	x2846	",lowBound=0, cat= 'Integer')
x2847	=	p.LpVariable("	x2847	",lowBound=0, cat= 'Integer')
x2848	=	p.LpVariable("	x2848	",lowBound=0, cat= 'Integer')
x2849	=	p.LpVariable("	x2849	",lowBound=0, cat= 'Integer')
x2850	=	p.LpVariable("	x2850	",lowBound=0, cat= 'Integer')
x2851	=	p.LpVariable("	x2851	",lowBound=0, cat= 'Integer')
x2852	=	p.LpVariable("	x2852	",lowBound=0, cat= 'Integer')
x2853	=	p.LpVariable("	x2853	",lowBound=0, cat= 'Integer')
x2854	=	p.LpVariable("	x2854	",lowBound=0, cat= 'Integer')
x2855	=	p.LpVariable("	x2855	",lowBound=0, cat= 'Integer')
x2856	=	p.LpVariable("	x2856	",lowBound=0, cat= 'Integer')
x2857	=	p.LpVariable("	x2857	",lowBound=0, cat= 'Integer')
x2858	=	p.LpVariable("	x2858	",lowBound=0, cat= 'Integer')
x2859	=	p.LpVariable("	x2859	",lowBound=0, cat= 'Integer')
x2860	=	p.LpVariable("	x2860	",lowBound=0, cat= 'Integer')
x2861	=	p.LpVariable("	x2861	",lowBound=0, cat= 'Integer')
x2862	=	p.LpVariable("	x2862	",lowBound=0, cat= 'Integer')
x2863	=	p.LpVariable("	x2863	",lowBound=0, cat= 'Integer')
x2864	=	p.LpVariable("	x2864	",lowBound=0, cat= 'Integer')
x2865	=	p.LpVariable("	x2865	",lowBound=0, cat= 'Integer')
x2866	=	p.LpVariable("	x2866	",lowBound=0, cat= 'Integer')
x2867	=	p.LpVariable("	x2867	",lowBound=0, cat= 'Integer')
x2868	=	p.LpVariable("	x2868	",lowBound=0, cat= 'Integer')
x2869	=	p.LpVariable("	x2869	",lowBound=0, cat= 'Integer')
x2870	=	p.LpVariable("	x2870	",lowBound=0, cat= 'Integer')
x2871	=	p.LpVariable("	x2871	",lowBound=0, cat= 'Integer')
x2872	=	p.LpVariable("	x2872	",lowBound=0, cat= 'Integer')
x2873	=	p.LpVariable("	x2873	",lowBound=0, cat= 'Integer')
x2874	=	p.LpVariable("	x2874	",lowBound=0, cat= 'Integer')
x2875	=	p.LpVariable("	x2875	",lowBound=0, cat= 'Integer')
x2876	=	p.LpVariable("	x2876	",lowBound=0, cat= 'Integer')
x2877	=	p.LpVariable("	x2877	",lowBound=0, cat= 'Integer')
x2878	=	p.LpVariable("	x2878	",lowBound=0, cat= 'Integer')
x2879	=	p.LpVariable("	x2879	",lowBound=0, cat= 'Integer')
x2880	=	p.LpVariable("	x2880	",lowBound=0, cat= 'Integer')
x2881	=	p.LpVariable("	x2881	",lowBound=0, cat= 'Integer')
x2882	=	p.LpVariable("	x2882	",lowBound=0, cat= 'Integer')
x2883	=	p.LpVariable("	x2883	",lowBound=0, cat= 'Integer')
x2884	=	p.LpVariable("	x2884	",lowBound=0, cat= 'Integer')
x2885	=	p.LpVariable("	x2885	",lowBound=0, cat= 'Integer')
x2886	=	p.LpVariable("	x2886	",lowBound=0, cat= 'Integer')
x2887	=	p.LpVariable("	x2887	",lowBound=0, cat= 'Integer')
x2888	=	p.LpVariable("	x2888	",lowBound=0, cat= 'Integer')
x2889	=	p.LpVariable("	x2889	",lowBound=0, cat= 'Integer')
x2890	=	p.LpVariable("	x2890	",lowBound=0, cat= 'Integer')
x2891	=	p.LpVariable("	x2891	",lowBound=0, cat= 'Integer')
x2892	=	p.LpVariable("	x2892	",lowBound=0, cat= 'Integer')
x2893	=	p.LpVariable("	x2893	",lowBound=0, cat= 'Integer')
x2894	=	p.LpVariable("	x2894	",lowBound=0, cat= 'Integer')
x2895	=	p.LpVariable("	x2895	",lowBound=0, cat= 'Integer')
x2896	=	p.LpVariable("	x2896	",lowBound=0, cat= 'Integer')
x2897	=	p.LpVariable("	x2897	",lowBound=0, cat= 'Integer')
x2898	=	p.LpVariable("	x2898	",lowBound=0, cat= 'Integer')
x2899	=	p.LpVariable("	x2899	",lowBound=0, cat= 'Integer')
x2900	=	p.LpVariable("	x2900	",lowBound=0, cat= 'Integer')
x2901	=	p.LpVariable("	x2901	",lowBound=0, cat= 'Integer')
x2902	=	p.LpVariable("	x2902	",lowBound=0, cat= 'Integer')
x2903	=	p.LpVariable("	x2903	",lowBound=0, cat= 'Integer')
x2904	=	p.LpVariable("	x2904	",lowBound=0, cat= 'Integer')
x2905	=	p.LpVariable("	x2905	",lowBound=0, cat= 'Integer')
x2906	=	p.LpVariable("	x2906	",lowBound=0, cat= 'Integer')
x2907	=	p.LpVariable("	x2907	",lowBound=0, cat= 'Integer')
x2908	=	p.LpVariable("	x2908	",lowBound=0, cat= 'Integer')
x2909	=	p.LpVariable("	x2909	",lowBound=0, cat= 'Integer')
x2910	=	p.LpVariable("	x2910	",lowBound=0, cat= 'Integer')
x2911	=	p.LpVariable("	x2911	",lowBound=0, cat= 'Integer')
x2912	=	p.LpVariable("	x2912	",lowBound=0, cat= 'Integer')
x2913	=	p.LpVariable("	x2913	",lowBound=0, cat= 'Integer')
x2914	=	p.LpVariable("	x2914	",lowBound=0, cat= 'Integer')
x2915	=	p.LpVariable("	x2915	",lowBound=0, cat= 'Integer')
x2916	=	p.LpVariable("	x2916	",lowBound=0, cat= 'Integer')
x2917	=	p.LpVariable("	x2917	",lowBound=0, cat= 'Integer')
x2918	=	p.LpVariable("	x2918	",lowBound=0, cat= 'Integer')
x2919	=	p.LpVariable("	x2919	",lowBound=0, cat= 'Integer')
x2920	=	p.LpVariable("	x2920	",lowBound=0, cat= 'Integer')
x2921	=	p.LpVariable("	x2921	",lowBound=0, cat= 'Integer')
x2922	=	p.LpVariable("	x2922	",lowBound=0, cat= 'Integer')
x2923	=	p.LpVariable("	x2923	",lowBound=0, cat= 'Integer')
x2924	=	p.LpVariable("	x2924	",lowBound=0, cat= 'Integer')
x2925	=	p.LpVariable("	x2925	",lowBound=0, cat= 'Integer')
x2926	=	p.LpVariable("	x2926	",lowBound=0, cat= 'Integer')
x2927	=	p.LpVariable("	x2927	",lowBound=0, cat= 'Integer')
x2928	=	p.LpVariable("	x2928	",lowBound=0, cat= 'Integer')
x2929	=	p.LpVariable("	x2929	",lowBound=0, cat= 'Integer')
x2930	=	p.LpVariable("	x2930	",lowBound=0, cat= 'Integer')
x2931	=	p.LpVariable("	x2931	",lowBound=0, cat= 'Integer')
x2932	=	p.LpVariable("	x2932	",lowBound=0, cat= 'Integer')
x2933	=	p.LpVariable("	x2933	",lowBound=0, cat= 'Integer')
x2934	=	p.LpVariable("	x2934	",lowBound=0, cat= 'Integer')
x2935	=	p.LpVariable("	x2935	",lowBound=0, cat= 'Integer')
x2936	=	p.LpVariable("	x2936	",lowBound=0, cat= 'Integer')
x2937	=	p.LpVariable("	x2937	",lowBound=0, cat= 'Integer')
x2938	=	p.LpVariable("	x2938	",lowBound=0, cat= 'Integer')
x2939	=	p.LpVariable("	x2939	",lowBound=0, cat= 'Integer')
x2940	=	p.LpVariable("	x2940	",lowBound=0, cat= 'Integer')
x2941	=	p.LpVariable("	x2941	",lowBound=0, cat= 'Integer')
x2942	=	p.LpVariable("	x2942	",lowBound=0, cat= 'Integer')
x2943	=	p.LpVariable("	x2943	",lowBound=0, cat= 'Integer')
x2944	=	p.LpVariable("	x2944	",lowBound=0, cat= 'Integer')
x2945	=	p.LpVariable("	x2945	",lowBound=0, cat= 'Integer')
x2946	=	p.LpVariable("	x2946	",lowBound=0, cat= 'Integer')
x2947	=	p.LpVariable("	x2947	",lowBound=0, cat= 'Integer')
x2948	=	p.LpVariable("	x2948	",lowBound=0, cat= 'Integer')
x2949	=	p.LpVariable("	x2949	",lowBound=0, cat= 'Integer')
x2950	=	p.LpVariable("	x2950	",lowBound=0, cat= 'Integer')
x2951	=	p.LpVariable("	x2951	",lowBound=0, cat= 'Integer')
x2952	=	p.LpVariable("	x2952	",lowBound=0, cat= 'Integer')
x2953	=	p.LpVariable("	x2953	",lowBound=0, cat= 'Integer')
x2954	=	p.LpVariable("	x2954	",lowBound=0, cat= 'Integer')
x2955	=	p.LpVariable("	x2955	",lowBound=0, cat= 'Integer')
x2956	=	p.LpVariable("	x2956	",lowBound=0, cat= 'Integer')
x2957	=	p.LpVariable("	x2957	",lowBound=0, cat= 'Integer')
x2958	=	p.LpVariable("	x2958	",lowBound=0, cat= 'Integer')
x2959	=	p.LpVariable("	x2959	",lowBound=0, cat= 'Integer')
x2960	=	p.LpVariable("	x2960	",lowBound=0, cat= 'Integer')
x2961	=	p.LpVariable("	x2961	",lowBound=0, cat= 'Integer')
x2962	=	p.LpVariable("	x2962	",lowBound=0, cat= 'Integer')
x2963	=	p.LpVariable("	x2963	",lowBound=0, cat= 'Integer')
x2964	=	p.LpVariable("	x2964	",lowBound=0, cat= 'Integer')
x2965	=	p.LpVariable("	x2965	",lowBound=0, cat= 'Integer')
x2966	=	p.LpVariable("	x2966	",lowBound=0, cat= 'Integer')
x2967	=	p.LpVariable("	x2967	",lowBound=0, cat= 'Integer')
x2968	=	p.LpVariable("	x2968	",lowBound=0, cat= 'Integer')
x2969	=	p.LpVariable("	x2969	",lowBound=0, cat= 'Integer')
x2970	=	p.LpVariable("	x2970	",lowBound=0, cat= 'Integer')
x2971	=	p.LpVariable("	x2971	",lowBound=0, cat= 'Integer')
x2972	=	p.LpVariable("	x2972	",lowBound=0, cat= 'Integer')
x2973	=	p.LpVariable("	x2973	",lowBound=0, cat= 'Integer')
x2974	=	p.LpVariable("	x2974	",lowBound=0, cat= 'Integer')
x2975	=	p.LpVariable("	x2975	",lowBound=0, cat= 'Integer')
x2976	=	p.LpVariable("	x2976	",lowBound=0, cat= 'Integer')
x2977	=	p.LpVariable("	x2977	",lowBound=0, cat= 'Integer')
x2978	=	p.LpVariable("	x2978	",lowBound=0, cat= 'Integer')
x2979	=	p.LpVariable("	x2979	",lowBound=0, cat= 'Integer')
x2980	=	p.LpVariable("	x2980	",lowBound=0, cat= 'Integer')
x2981	=	p.LpVariable("	x2981	",lowBound=0, cat= 'Integer')
x2982	=	p.LpVariable("	x2982	",lowBound=0, cat= 'Integer')
x2983	=	p.LpVariable("	x2983	",lowBound=0, cat= 'Integer')
x2984	=	p.LpVariable("	x2984	",lowBound=0, cat= 'Integer')
x2985	=	p.LpVariable("	x2985	",lowBound=0, cat= 'Integer')
x2986	=	p.LpVariable("	x2986	",lowBound=0, cat= 'Integer')
x2987	=	p.LpVariable("	x2987	",lowBound=0, cat= 'Integer')
x2988	=	p.LpVariable("	x2988	",lowBound=0, cat= 'Integer')
x2989	=	p.LpVariable("	x2989	",lowBound=0, cat= 'Integer')
x2990	=	p.LpVariable("	x2990	",lowBound=0, cat= 'Integer')
x2991	=	p.LpVariable("	x2991	",lowBound=0, cat= 'Integer')
x2992	=	p.LpVariable("	x2992	",lowBound=0, cat= 'Integer')
x2993	=	p.LpVariable("	x2993	",lowBound=0, cat= 'Integer')
x2994	=	p.LpVariable("	x2994	",lowBound=0, cat= 'Integer')
x2995	=	p.LpVariable("	x2995	",lowBound=0, cat= 'Integer')
x2996	=	p.LpVariable("	x2996	",lowBound=0, cat= 'Integer')
x2997	=	p.LpVariable("	x2997	",lowBound=0, cat= 'Integer')
x2998	=	p.LpVariable("	x2998	",lowBound=0, cat= 'Integer')
x2999	=	p.LpVariable("	x2999	",lowBound=0, cat= 'Integer')
x3000	=	p.LpVariable("	x3000	",lowBound=0, cat= 'Integer')
x3001	=	p.LpVariable("	x3001	",lowBound=0, cat= 'Integer')
x3002	=	p.LpVariable("	x3002	",lowBound=0, cat= 'Integer')
x3003	=	p.LpVariable("	x3003	",lowBound=0, cat= 'Integer')
x3004	=	p.LpVariable("	x3004	",lowBound=0, cat= 'Integer')
x3005	=	p.LpVariable("	x3005	",lowBound=0, cat= 'Integer')
x3006	=	p.LpVariable("	x3006	",lowBound=0, cat= 'Integer')
x3007	=	p.LpVariable("	x3007	",lowBound=0, cat= 'Integer')
x3008	=	p.LpVariable("	x3008	",lowBound=0, cat= 'Integer')
x3009	=	p.LpVariable("	x3009	",lowBound=0, cat= 'Integer')
x3010	=	p.LpVariable("	x3010	",lowBound=0, cat= 'Integer')
x3011	=	p.LpVariable("	x3011	",lowBound=0, cat= 'Integer')
x3012	=	p.LpVariable("	x3012	",lowBound=0, cat= 'Integer')
x3013	=	p.LpVariable("	x3013	",lowBound=0, cat= 'Integer')
x3014	=	p.LpVariable("	x3014	",lowBound=0, cat= 'Integer')
x3015	=	p.LpVariable("	x3015	",lowBound=0, cat= 'Integer')
x3016	=	p.LpVariable("	x3016	",lowBound=0, cat= 'Integer')
x3017	=	p.LpVariable("	x3017	",lowBound=0, cat= 'Integer')
x3018	=	p.LpVariable("	x3018	",lowBound=0, cat= 'Integer')
x3019	=	p.LpVariable("	x3019	",lowBound=0, cat= 'Integer')
x3020	=	p.LpVariable("	x3020	",lowBound=0, cat= 'Integer')
x3021	=	p.LpVariable("	x3021	",lowBound=0, cat= 'Integer')
x3022	=	p.LpVariable("	x3022	",lowBound=0, cat= 'Integer')
x3023	=	p.LpVariable("	x3023	",lowBound=0, cat= 'Integer')
x3024	=	p.LpVariable("	x3024	",lowBound=0, cat= 'Integer')
x3025	=	p.LpVariable("	x3025	",lowBound=0, cat= 'Integer')
x3026	=	p.LpVariable("	x3026	",lowBound=0, cat= 'Integer')
x3027	=	p.LpVariable("	x3027	",lowBound=0, cat= 'Integer')
x3028	=	p.LpVariable("	x3028	",lowBound=0, cat= 'Integer')
x3029	=	p.LpVariable("	x3029	",lowBound=0, cat= 'Integer')
x3030	=	p.LpVariable("	x3030	",lowBound=0, cat= 'Integer')
x3031	=	p.LpVariable("	x3031	",lowBound=0, cat= 'Integer')
x3032	=	p.LpVariable("	x3032	",lowBound=0, cat= 'Integer')
x3033	=	p.LpVariable("	x3033	",lowBound=0, cat= 'Integer')
x3034	=	p.LpVariable("	x3034	",lowBound=0, cat= 'Integer')
x3035	=	p.LpVariable("	x3035	",lowBound=0, cat= 'Integer')
x3036	=	p.LpVariable("	x3036	",lowBound=0, cat= 'Integer')
x3037	=	p.LpVariable("	x3037	",lowBound=0, cat= 'Integer')
x3038	=	p.LpVariable("	x3038	",lowBound=0, cat= 'Integer')
x3039	=	p.LpVariable("	x3039	",lowBound=0, cat= 'Integer')
x3040	=	p.LpVariable("	x3040	",lowBound=0, cat= 'Integer')
x3041	=	p.LpVariable("	x3041	",lowBound=0, cat= 'Integer')
x3042	=	p.LpVariable("	x3042	",lowBound=0, cat= 'Integer')
x3043	=	p.LpVariable("	x3043	",lowBound=0, cat= 'Integer')
x3044	=	p.LpVariable("	x3044	",lowBound=0, cat= 'Integer')
x3045	=	p.LpVariable("	x3045	",lowBound=0, cat= 'Integer')
x3046	=	p.LpVariable("	x3046	",lowBound=0, cat= 'Integer')
x3047	=	p.LpVariable("	x3047	",lowBound=0, cat= 'Integer')
x3048	=	p.LpVariable("	x3048	",lowBound=0, cat= 'Integer')
x3049	=	p.LpVariable("	x3049	",lowBound=0, cat= 'Integer')
x3050	=	p.LpVariable("	x3050	",lowBound=0, cat= 'Integer')
x3051	=	p.LpVariable("	x3051	",lowBound=0, cat= 'Integer')
x3052	=	p.LpVariable("	x3052	",lowBound=0, cat= 'Integer')
x3053	=	p.LpVariable("	x3053	",lowBound=0, cat= 'Integer')
x3054	=	p.LpVariable("	x3054	",lowBound=0, cat= 'Integer')
x3055	=	p.LpVariable("	x3055	",lowBound=0, cat= 'Integer')
x3056	=	p.LpVariable("	x3056	",lowBound=0, cat= 'Integer')
x3057	=	p.LpVariable("	x3057	",lowBound=0, cat= 'Integer')
x3058	=	p.LpVariable("	x3058	",lowBound=0, cat= 'Integer')
x3059	=	p.LpVariable("	x3059	",lowBound=0, cat= 'Integer')
x3060	=	p.LpVariable("	x3060	",lowBound=0, cat= 'Integer')
x3061	=	p.LpVariable("	x3061	",lowBound=0, cat= 'Integer')
x3062	=	p.LpVariable("	x3062	",lowBound=0, cat= 'Integer')
x3063	=	p.LpVariable("	x3063	",lowBound=0, cat= 'Integer')
x3064	=	p.LpVariable("	x3064	",lowBound=0, cat= 'Integer')
x3065	=	p.LpVariable("	x3065	",lowBound=0, cat= 'Integer')
x3066	=	p.LpVariable("	x3066	",lowBound=0, cat= 'Integer')
x3067	=	p.LpVariable("	x3067	",lowBound=0, cat= 'Integer')
x3068	=	p.LpVariable("	x3068	",lowBound=0, cat= 'Integer')
x3069	=	p.LpVariable("	x3069	",lowBound=0, cat= 'Integer')
x3070	=	p.LpVariable("	x3070	",lowBound=0, cat= 'Integer')
x3071	=	p.LpVariable("	x3071	",lowBound=0, cat= 'Integer')
x3072	=	p.LpVariable("	x3072	",lowBound=0, cat= 'Integer')
x3073	=	p.LpVariable("	x3073	",lowBound=0, cat= 'Integer')
x3074	=	p.LpVariable("	x3074	",lowBound=0, cat= 'Integer')
x3075	=	p.LpVariable("	x3075	",lowBound=0, cat= 'Integer')
x3076	=	p.LpVariable("	x3076	",lowBound=0, cat= 'Integer')
x3077	=	p.LpVariable("	x3077	",lowBound=0, cat= 'Integer')
x3078	=	p.LpVariable("	x3078	",lowBound=0, cat= 'Integer')
x3079	=	p.LpVariable("	x3079	",lowBound=0, cat= 'Integer')
x3080	=	p.LpVariable("	x3080	",lowBound=0, cat= 'Integer')
x3081	=	p.LpVariable("	x3081	",lowBound=0, cat= 'Integer')
x3082	=	p.LpVariable("	x3082	",lowBound=0, cat= 'Integer')
x3083	=	p.LpVariable("	x3083	",lowBound=0, cat= 'Integer')
x3084	=	p.LpVariable("	x3084	",lowBound=0, cat= 'Integer')
x3085	=	p.LpVariable("	x3085	",lowBound=0, cat= 'Integer')
x3086	=	p.LpVariable("	x3086	",lowBound=0, cat= 'Integer')
x3087	=	p.LpVariable("	x3087	",lowBound=0, cat= 'Integer')
x3088	=	p.LpVariable("	x3088	",lowBound=0, cat= 'Integer')
x3089	=	p.LpVariable("	x3089	",lowBound=0, cat= 'Integer')
x3090	=	p.LpVariable("	x3090	",lowBound=0, cat= 'Integer')
x3091	=	p.LpVariable("	x3091	",lowBound=0, cat= 'Integer')
x3092	=	p.LpVariable("	x3092	",lowBound=0, cat= 'Integer')
x3093	=	p.LpVariable("	x3093	",lowBound=0, cat= 'Integer')
x3094	=	p.LpVariable("	x3094	",lowBound=0, cat= 'Integer')
x3095	=	p.LpVariable("	x3095	",lowBound=0, cat= 'Integer')
x3096	=	p.LpVariable("	x3096	",lowBound=0, cat= 'Integer')
x3097	=	p.LpVariable("	x3097	",lowBound=0, cat= 'Integer')
x3098	=	p.LpVariable("	x3098	",lowBound=0, cat= 'Integer')
x3099	=	p.LpVariable("	x3099	",lowBound=0, cat= 'Integer')
x3100	=	p.LpVariable("	x3100	",lowBound=0, cat= 'Integer')
x3101	=	p.LpVariable("	x3101	",lowBound=0, cat= 'Integer')
x3102	=	p.LpVariable("	x3102	",lowBound=0, cat= 'Integer')
x3103	=	p.LpVariable("	x3103	",lowBound=0, cat= 'Integer')
x3104	=	p.LpVariable("	x3104	",lowBound=0, cat= 'Integer')
x3105	=	p.LpVariable("	x3105	",lowBound=0, cat= 'Integer')
x3106	=	p.LpVariable("	x3106	",lowBound=0, cat= 'Integer')
x3107	=	p.LpVariable("	x3107	",lowBound=0, cat= 'Integer')
x3108	=	p.LpVariable("	x3108	",lowBound=0, cat= 'Integer')
x3109	=	p.LpVariable("	x3109	",lowBound=0, cat= 'Integer')
x3110	=	p.LpVariable("	x3110	",lowBound=0, cat= 'Integer')
x3111	=	p.LpVariable("	x3111	",lowBound=0, cat= 'Integer')
x3112	=	p.LpVariable("	x3112	",lowBound=0, cat= 'Integer')
x3113	=	p.LpVariable("	x3113	",lowBound=0, cat= 'Integer')
x3114	=	p.LpVariable("	x3114	",lowBound=0, cat= 'Integer')
x3115	=	p.LpVariable("	x3115	",lowBound=0, cat= 'Integer')
x3116	=	p.LpVariable("	x3116	",lowBound=0, cat= 'Integer')
x3117	=	p.LpVariable("	x3117	",lowBound=0, cat= 'Integer')
x3118	=	p.LpVariable("	x3118	",lowBound=0, cat= 'Integer')
x3119	=	p.LpVariable("	x3119	",lowBound=0, cat= 'Integer')
x3120	=	p.LpVariable("	x3120	",lowBound=0, cat= 'Integer')
x3121	=	p.LpVariable("	x3121	",lowBound=0, cat= 'Integer')
x3122	=	p.LpVariable("	x3122	",lowBound=0, cat= 'Integer')
x3123	=	p.LpVariable("	x3123	",lowBound=0, cat= 'Integer')
x3124	=	p.LpVariable("	x3124	",lowBound=0, cat= 'Integer')
x3125	=	p.LpVariable("	x3125	",lowBound=0, cat= 'Integer')
x3126	=	p.LpVariable("	x3126	",lowBound=0, cat= 'Integer')
x3127	=	p.LpVariable("	x3127	",lowBound=0, cat= 'Integer')
x3128	=	p.LpVariable("	x3128	",lowBound=0, cat= 'Integer')
x3129	=	p.LpVariable("	x3129	",lowBound=0, cat= 'Integer')
x3130	=	p.LpVariable("	x3130	",lowBound=0, cat= 'Integer')
x3131	=	p.LpVariable("	x3131	",lowBound=0, cat= 'Integer')
x3132	=	p.LpVariable("	x3132	",lowBound=0, cat= 'Integer')
x3133	=	p.LpVariable("	x3133	",lowBound=0, cat= 'Integer')
x3134	=	p.LpVariable("	x3134	",lowBound=0, cat= 'Integer')
x3135	=	p.LpVariable("	x3135	",lowBound=0, cat= 'Integer')
x3136	=	p.LpVariable("	x3136	",lowBound=0, cat= 'Integer')
x3137	=	p.LpVariable("	x3137	",lowBound=0, cat= 'Integer')
x3138	=	p.LpVariable("	x3138	",lowBound=0, cat= 'Integer')
x3139	=	p.LpVariable("	x3139	",lowBound=0, cat= 'Integer')
x3140	=	p.LpVariable("	x3140	",lowBound=0, cat= 'Integer')
x3141	=	p.LpVariable("	x3141	",lowBound=0, cat= 'Integer')
x3142	=	p.LpVariable("	x3142	",lowBound=0, cat= 'Integer')
x3143	=	p.LpVariable("	x3143	",lowBound=0, cat= 'Integer')
x3144	=	p.LpVariable("	x3144	",lowBound=0, cat= 'Integer')
x3145	=	p.LpVariable("	x3145	",lowBound=0, cat= 'Integer')
x3146	=	p.LpVariable("	x3146	",lowBound=0, cat= 'Integer')
x3147	=	p.LpVariable("	x3147	",lowBound=0, cat= 'Integer')
x3148	=	p.LpVariable("	x3148	",lowBound=0, cat= 'Integer')
x3149	=	p.LpVariable("	x3149	",lowBound=0, cat= 'Integer')
x3150	=	p.LpVariable("	x3150	",lowBound=0, cat= 'Integer')
x3151	=	p.LpVariable("	x3151	",lowBound=0, cat= 'Integer')
x3152	=	p.LpVariable("	x3152	",lowBound=0, cat= 'Integer')
x3153	=	p.LpVariable("	x3153	",lowBound=0, cat= 'Integer')
x3154	=	p.LpVariable("	x3154	",lowBound=0, cat= 'Integer')
x3155	=	p.LpVariable("	x3155	",lowBound=0, cat= 'Integer')
x3156	=	p.LpVariable("	x3156	",lowBound=0, cat= 'Integer')
x3157	=	p.LpVariable("	x3157	",lowBound=0, cat= 'Integer')
x3158	=	p.LpVariable("	x3158	",lowBound=0, cat= 'Integer')
x3159	=	p.LpVariable("	x3159	",lowBound=0, cat= 'Integer')
x3160	=	p.LpVariable("	x3160	",lowBound=0, cat= 'Integer')
x3161	=	p.LpVariable("	x3161	",lowBound=0, cat= 'Integer')
x3162	=	p.LpVariable("	x3162	",lowBound=0, cat= 'Integer')
x3163	=	p.LpVariable("	x3163	",lowBound=0, cat= 'Integer')
x3164	=	p.LpVariable("	x3164	",lowBound=0, cat= 'Integer')
x3165	=	p.LpVariable("	x3165	",lowBound=0, cat= 'Integer')
x3166	=	p.LpVariable("	x3166	",lowBound=0, cat= 'Integer')
x3167	=	p.LpVariable("	x3167	",lowBound=0, cat= 'Integer')
x3168	=	p.LpVariable("	x3168	",lowBound=0, cat= 'Integer')
x3169	=	p.LpVariable("	x3169	",lowBound=0, cat= 'Integer')
x3170	=	p.LpVariable("	x3170	",lowBound=0, cat= 'Integer')
x3171	=	p.LpVariable("	x3171	",lowBound=0, cat= 'Integer')
x3172	=	p.LpVariable("	x3172	",lowBound=0, cat= 'Integer')
x3173	=	p.LpVariable("	x3173	",lowBound=0, cat= 'Integer')
x3174	=	p.LpVariable("	x3174	",lowBound=0, cat= 'Integer')
x3175	=	p.LpVariable("	x3175	",lowBound=0, cat= 'Integer')
x3176	=	p.LpVariable("	x3176	",lowBound=0, cat= 'Integer')
x3177	=	p.LpVariable("	x3177	",lowBound=0, cat= 'Integer')
x3178	=	p.LpVariable("	x3178	",lowBound=0, cat= 'Integer')
x3179	=	p.LpVariable("	x3179	",lowBound=0, cat= 'Integer')
x3180	=	p.LpVariable("	x3180	",lowBound=0, cat= 'Integer')
x3181	=	p.LpVariable("	x3181	",lowBound=0, cat= 'Integer')
x3182	=	p.LpVariable("	x3182	",lowBound=0, cat= 'Integer')
x3183	=	p.LpVariable("	x3183	",lowBound=0, cat= 'Integer')
x3184	=	p.LpVariable("	x3184	",lowBound=0, cat= 'Integer')
x3185	=	p.LpVariable("	x3185	",lowBound=0, cat= 'Integer')
x3186	=	p.LpVariable("	x3186	",lowBound=0, cat= 'Integer')
x3187	=	p.LpVariable("	x3187	",lowBound=0, cat= 'Integer')
x3188	=	p.LpVariable("	x3188	",lowBound=0, cat= 'Integer')
x3189	=	p.LpVariable("	x3189	",lowBound=0, cat= 'Integer')
x3190	=	p.LpVariable("	x3190	",lowBound=0, cat= 'Integer')
x3191	=	p.LpVariable("	x3191	",lowBound=0, cat= 'Integer')
x3192	=	p.LpVariable("	x3192	",lowBound=0, cat= 'Integer')
x3193	=	p.LpVariable("	x3193	",lowBound=0, cat= 'Integer')
x3194	=	p.LpVariable("	x3194	",lowBound=0, cat= 'Integer')
x3195	=	p.LpVariable("	x3195	",lowBound=0, cat= 'Integer')
x3196	=	p.LpVariable("	x3196	",lowBound=0, cat= 'Integer')
x3197	=	p.LpVariable("	x3197	",lowBound=0, cat= 'Integer')
x3198	=	p.LpVariable("	x3198	",lowBound=0, cat= 'Integer')
x3199	=	p.LpVariable("	x3199	",lowBound=0, cat= 'Integer')
x3200	=	p.LpVariable("	x3200	",lowBound=0, cat= 'Integer')
x3201	=	p.LpVariable("	x3201	",lowBound=0, cat= 'Integer')
x3202	=	p.LpVariable("	x3202	",lowBound=0, cat= 'Integer')
x3203	=	p.LpVariable("	x3203	",lowBound=0, cat= 'Integer')
x3204	=	p.LpVariable("	x3204	",lowBound=0, cat= 'Integer')
x3205	=	p.LpVariable("	x3205	",lowBound=0, cat= 'Integer')
x3206	=	p.LpVariable("	x3206	",lowBound=0, cat= 'Integer')
x3207	=	p.LpVariable("	x3207	",lowBound=0, cat= 'Integer')
x3208	=	p.LpVariable("	x3208	",lowBound=0, cat= 'Integer')
x3209	=	p.LpVariable("	x3209	",lowBound=0, cat= 'Integer')
x3210	=	p.LpVariable("	x3210	",lowBound=0, cat= 'Integer')
x3211	=	p.LpVariable("	x3211	",lowBound=0, cat= 'Integer')
x3212	=	p.LpVariable("	x3212	",lowBound=0, cat= 'Integer')
x3213	=	p.LpVariable("	x3213	",lowBound=0, cat= 'Integer')
x3214	=	p.LpVariable("	x3214	",lowBound=0, cat= 'Integer')
x3215	=	p.LpVariable("	x3215	",lowBound=0, cat= 'Integer')
x3216	=	p.LpVariable("	x3216	",lowBound=0, cat= 'Integer')
x3217	=	p.LpVariable("	x3217	",lowBound=0, cat= 'Integer')
x3218	=	p.LpVariable("	x3218	",lowBound=0, cat= 'Integer')
x3219	=	p.LpVariable("	x3219	",lowBound=0, cat= 'Integer')
x3220	=	p.LpVariable("	x3220	",lowBound=0, cat= 'Integer')
x3221	=	p.LpVariable("	x3221	",lowBound=0, cat= 'Integer')
x3222	=	p.LpVariable("	x3222	",lowBound=0, cat= 'Integer')
x3223	=	p.LpVariable("	x3223	",lowBound=0, cat= 'Integer')
x3224	=	p.LpVariable("	x3224	",lowBound=0, cat= 'Integer')
x3225	=	p.LpVariable("	x3225	",lowBound=0, cat= 'Integer')
x3226	=	p.LpVariable("	x3226	",lowBound=0, cat= 'Integer')
x3227	=	p.LpVariable("	x3227	",lowBound=0, cat= 'Integer')
x3228	=	p.LpVariable("	x3228	",lowBound=0, cat= 'Integer')
x3229	=	p.LpVariable("	x3229	",lowBound=0, cat= 'Integer')
x3230	=	p.LpVariable("	x3230	",lowBound=0, cat= 'Integer')
x3231	=	p.LpVariable("	x3231	",lowBound=0, cat= 'Integer')
x3232	=	p.LpVariable("	x3232	",lowBound=0, cat= 'Integer')
x3233	=	p.LpVariable("	x3233	",lowBound=0, cat= 'Integer')
x3234	=	p.LpVariable("	x3234	",lowBound=0, cat= 'Integer')
x3235	=	p.LpVariable("	x3235	",lowBound=0, cat= 'Integer')
x3236	=	p.LpVariable("	x3236	",lowBound=0, cat= 'Integer')
x3237	=	p.LpVariable("	x3237	",lowBound=0, cat= 'Integer')
x3238	=	p.LpVariable("	x3238	",lowBound=0, cat= 'Integer')
x3239	=	p.LpVariable("	x3239	",lowBound=0, cat= 'Integer')
x3240	=	p.LpVariable("	x3240	",lowBound=0, cat= 'Integer')
x3241	=	p.LpVariable("	x3241	",lowBound=0, cat= 'Integer')
x3242	=	p.LpVariable("	x3242	",lowBound=0, cat= 'Integer')
x3243	=	p.LpVariable("	x3243	",lowBound=0, cat= 'Integer')
x3244	=	p.LpVariable("	x3244	",lowBound=0, cat= 'Integer')
x3245	=	p.LpVariable("	x3245	",lowBound=0, cat= 'Integer')
x3246	=	p.LpVariable("	x3246	",lowBound=0, cat= 'Integer')
x3247	=	p.LpVariable("	x3247	",lowBound=0, cat= 'Integer')
x3248	=	p.LpVariable("	x3248	",lowBound=0, cat= 'Integer')
x3249	=	p.LpVariable("	x3249	",lowBound=0, cat= 'Integer')
x3250	=	p.LpVariable("	x3250	",lowBound=0, cat= 'Integer')
x3251	=	p.LpVariable("	x3251	",lowBound=0, cat= 'Integer')
x3252	=	p.LpVariable("	x3252	",lowBound=0, cat= 'Integer')
x3253	=	p.LpVariable("	x3253	",lowBound=0, cat= 'Integer')
x3254	=	p.LpVariable("	x3254	",lowBound=0, cat= 'Integer')
x3255	=	p.LpVariable("	x3255	",lowBound=0, cat= 'Integer')
x3256	=	p.LpVariable("	x3256	",lowBound=0, cat= 'Integer')
x3257	=	p.LpVariable("	x3257	",lowBound=0, cat= 'Integer')
x3258	=	p.LpVariable("	x3258	",lowBound=0, cat= 'Integer')
x3259	=	p.LpVariable("	x3259	",lowBound=0, cat= 'Integer')
x3260	=	p.LpVariable("	x3260	",lowBound=0, cat= 'Integer')
x3261	=	p.LpVariable("	x3261	",lowBound=0, cat= 'Integer')
x3262	=	p.LpVariable("	x3262	",lowBound=0, cat= 'Integer')
x3263	=	p.LpVariable("	x3263	",lowBound=0, cat= 'Integer')
x3264	=	p.LpVariable("	x3264	",lowBound=0, cat= 'Integer')
x3265	=	p.LpVariable("	x3265	",lowBound=0, cat= 'Integer')
x3266	=	p.LpVariable("	x3266	",lowBound=0, cat= 'Integer')
x3267	=	p.LpVariable("	x3267	",lowBound=0, cat= 'Integer')
x3268	=	p.LpVariable("	x3268	",lowBound=0, cat= 'Integer')
x3269	=	p.LpVariable("	x3269	",lowBound=0, cat= 'Integer')
x3270	=	p.LpVariable("	x3270	",lowBound=0, cat= 'Integer')
x3271	=	p.LpVariable("	x3271	",lowBound=0, cat= 'Integer')
x3272	=	p.LpVariable("	x3272	",lowBound=0, cat= 'Integer')
x3273	=	p.LpVariable("	x3273	",lowBound=0, cat= 'Integer')
x3274	=	p.LpVariable("	x3274	",lowBound=0, cat= 'Integer')
x3275	=	p.LpVariable("	x3275	",lowBound=0, cat= 'Integer')
x3276	=	p.LpVariable("	x3276	",lowBound=0, cat= 'Integer')
x3277	=	p.LpVariable("	x3277	",lowBound=0, cat= 'Integer')
x3278	=	p.LpVariable("	x3278	",lowBound=0, cat= 'Integer')
x3279	=	p.LpVariable("	x3279	",lowBound=0, cat= 'Integer')
x3280	=	p.LpVariable("	x3280	",lowBound=0, cat= 'Integer')
x3281	=	p.LpVariable("	x3281	",lowBound=0, cat= 'Integer')
x3282	=	p.LpVariable("	x3282	",lowBound=0, cat= 'Integer')
x3283	=	p.LpVariable("	x3283	",lowBound=0, cat= 'Integer')
x3284	=	p.LpVariable("	x3284	",lowBound=0, cat= 'Integer')
x3285	=	p.LpVariable("	x3285	",lowBound=0, cat= 'Integer')
x3286	=	p.LpVariable("	x3286	",lowBound=0, cat= 'Integer')
x3287	=	p.LpVariable("	x3287	",lowBound=0, cat= 'Integer')
x3288	=	p.LpVariable("	x3288	",lowBound=0, cat= 'Integer')
x3289	=	p.LpVariable("	x3289	",lowBound=0, cat= 'Integer')
x3290	=	p.LpVariable("	x3290	",lowBound=0, cat= 'Integer')
x3291	=	p.LpVariable("	x3291	",lowBound=0, cat= 'Integer')
x3292	=	p.LpVariable("	x3292	",lowBound=0, cat= 'Integer')
x3293	=	p.LpVariable("	x3293	",lowBound=0, cat= 'Integer')
x3294	=	p.LpVariable("	x3294	",lowBound=0, cat= 'Integer')
x3295	=	p.LpVariable("	x3295	",lowBound=0, cat= 'Integer')
x3296	=	p.LpVariable("	x3296	",lowBound=0, cat= 'Integer')
x3297	=	p.LpVariable("	x3297	",lowBound=0, cat= 'Integer')
x3298	=	p.LpVariable("	x3298	",lowBound=0, cat= 'Integer')
x3299	=	p.LpVariable("	x3299	",lowBound=0, cat= 'Integer')
x3300	=	p.LpVariable("	x3300	",lowBound=0, cat= 'Integer')
x3301	=	p.LpVariable("	x3301	",lowBound=0, cat= 'Integer')
x3302	=	p.LpVariable("	x3302	",lowBound=0, cat= 'Integer')
x3303	=	p.LpVariable("	x3303	",lowBound=0, cat= 'Integer')
x3304	=	p.LpVariable("	x3304	",lowBound=0, cat= 'Integer')
x3305	=	p.LpVariable("	x3305	",lowBound=0, cat= 'Integer')
x3306	=	p.LpVariable("	x3306	",lowBound=0, cat= 'Integer')
x3307	=	p.LpVariable("	x3307	",lowBound=0, cat= 'Integer')
x3308	=	p.LpVariable("	x3308	",lowBound=0, cat= 'Integer')
x3309	=	p.LpVariable("	x3309	",lowBound=0, cat= 'Integer')
x3310	=	p.LpVariable("	x3310	",lowBound=0, cat= 'Integer')
x3311	=	p.LpVariable("	x3311	",lowBound=0, cat= 'Integer')
x3312	=	p.LpVariable("	x3312	",lowBound=0, cat= 'Integer')
x3313	=	p.LpVariable("	x3313	",lowBound=0, cat= 'Integer')
x3314	=	p.LpVariable("	x3314	",lowBound=0, cat= 'Integer')
x3315	=	p.LpVariable("	x3315	",lowBound=0, cat= 'Integer')
x3316	=	p.LpVariable("	x3316	",lowBound=0, cat= 'Integer')
x3317	=	p.LpVariable("	x3317	",lowBound=0, cat= 'Integer')
x3318	=	p.LpVariable("	x3318	",lowBound=0, cat= 'Integer')
x3319	=	p.LpVariable("	x3319	",lowBound=0, cat= 'Integer')
x3320	=	p.LpVariable("	x3320	",lowBound=0, cat= 'Integer')
x3321	=	p.LpVariable("	x3321	",lowBound=0, cat= 'Integer')
x3322	=	p.LpVariable("	x3322	",lowBound=0, cat= 'Integer')
x3323	=	p.LpVariable("	x3323	",lowBound=0, cat= 'Integer')
x3324	=	p.LpVariable("	x3324	",lowBound=0, cat= 'Integer')
x3325	=	p.LpVariable("	x3325	",lowBound=0, cat= 'Integer')
x3326	=	p.LpVariable("	x3326	",lowBound=0, cat= 'Integer')
x3327	=	p.LpVariable("	x3327	",lowBound=0, cat= 'Integer')
x3328	=	p.LpVariable("	x3328	",lowBound=0, cat= 'Integer')
x3329	=	p.LpVariable("	x3329	",lowBound=0, cat= 'Integer')
x3330	=	p.LpVariable("	x3330	",lowBound=0, cat= 'Integer')
x3331	=	p.LpVariable("	x3331	",lowBound=0, cat= 'Integer')
x3332	=	p.LpVariable("	x3332	",lowBound=0, cat= 'Integer')
x3333	=	p.LpVariable("	x3333	",lowBound=0, cat= 'Integer')
x3334	=	p.LpVariable("	x3334	",lowBound=0, cat= 'Integer')
x3335	=	p.LpVariable("	x3335	",lowBound=0, cat= 'Integer')
x3336	=	p.LpVariable("	x3336	",lowBound=0, cat= 'Integer')
x3337	=	p.LpVariable("	x3337	",lowBound=0, cat= 'Integer')
x3338	=	p.LpVariable("	x3338	",lowBound=0, cat= 'Integer')
x3339	=	p.LpVariable("	x3339	",lowBound=0, cat= 'Integer')
x3340	=	p.LpVariable("	x3340	",lowBound=0, cat= 'Integer')
x3341	=	p.LpVariable("	x3341	",lowBound=0, cat= 'Integer')
x3342	=	p.LpVariable("	x3342	",lowBound=0, cat= 'Integer')
x3343	=	p.LpVariable("	x3343	",lowBound=0, cat= 'Integer')
x3344	=	p.LpVariable("	x3344	",lowBound=0, cat= 'Integer')
x3345	=	p.LpVariable("	x3345	",lowBound=0, cat= 'Integer')
x3346	=	p.LpVariable("	x3346	",lowBound=0, cat= 'Integer')
x3347	=	p.LpVariable("	x3347	",lowBound=0, cat= 'Integer')
x3348	=	p.LpVariable("	x3348	",lowBound=0, cat= 'Integer')
x3349	=	p.LpVariable("	x3349	",lowBound=0, cat= 'Integer')
x3350	=	p.LpVariable("	x3350	",lowBound=0, cat= 'Integer')
x3351	=	p.LpVariable("	x3351	",lowBound=0, cat= 'Integer')
x3352	=	p.LpVariable("	x3352	",lowBound=0, cat= 'Integer')
x3353	=	p.LpVariable("	x3353	",lowBound=0, cat= 'Integer')
x3354	=	p.LpVariable("	x3354	",lowBound=0, cat= 'Integer')
x3355	=	p.LpVariable("	x3355	",lowBound=0, cat= 'Integer')
x3356	=	p.LpVariable("	x3356	",lowBound=0, cat= 'Integer')
x3357	=	p.LpVariable("	x3357	",lowBound=0, cat= 'Integer')
x3358	=	p.LpVariable("	x3358	",lowBound=0, cat= 'Integer')
x3359	=	p.LpVariable("	x3359	",lowBound=0, cat= 'Integer')
x3360	=	p.LpVariable("	x3360	",lowBound=0, cat= 'Integer')
x3361	=	p.LpVariable("	x3361	",lowBound=0, cat= 'Integer')
x3362	=	p.LpVariable("	x3362	",lowBound=0, cat= 'Integer')
x3363	=	p.LpVariable("	x3363	",lowBound=0, cat= 'Integer')
x3364	=	p.LpVariable("	x3364	",lowBound=0, cat= 'Integer')
x3365	=	p.LpVariable("	x3365	",lowBound=0, cat= 'Integer')
x3366	=	p.LpVariable("	x3366	",lowBound=0, cat= 'Integer')
x3367	=	p.LpVariable("	x3367	",lowBound=0, cat= 'Integer')
x3368	=	p.LpVariable("	x3368	",lowBound=0, cat= 'Integer')
x3369	=	p.LpVariable("	x3369	",lowBound=0, cat= 'Integer')
x3370	=	p.LpVariable("	x3370	",lowBound=0, cat= 'Integer')
x3371	=	p.LpVariable("	x3371	",lowBound=0, cat= 'Integer')
x3372	=	p.LpVariable("	x3372	",lowBound=0, cat= 'Integer')
x3373	=	p.LpVariable("	x3373	",lowBound=0, cat= 'Integer')
x3374	=	p.LpVariable("	x3374	",lowBound=0, cat= 'Integer')
x3375	=	p.LpVariable("	x3375	",lowBound=0, cat= 'Integer')
x3376	=	p.LpVariable("	x3376	",lowBound=0, cat= 'Integer')
x3377	=	p.LpVariable("	x3377	",lowBound=0, cat= 'Integer')
x3378	=	p.LpVariable("	x3378	",lowBound=0, cat= 'Integer')
x3379	=	p.LpVariable("	x3379	",lowBound=0, cat= 'Integer')
x3380	=	p.LpVariable("	x3380	",lowBound=0, cat= 'Integer')
x3381	=	p.LpVariable("	x3381	",lowBound=0, cat= 'Integer')
x3382	=	p.LpVariable("	x3382	",lowBound=0, cat= 'Integer')
x3383	=	p.LpVariable("	x3383	",lowBound=0, cat= 'Integer')
x3384	=	p.LpVariable("	x3384	",lowBound=0, cat= 'Integer')
x3385	=	p.LpVariable("	x3385	",lowBound=0, cat= 'Integer')
x3386	=	p.LpVariable("	x3386	",lowBound=0, cat= 'Integer')
x3387	=	p.LpVariable("	x3387	",lowBound=0, cat= 'Integer')
x3388	=	p.LpVariable("	x3388	",lowBound=0, cat= 'Integer')
x3389	=	p.LpVariable("	x3389	",lowBound=0, cat= 'Integer')
x3390	=	p.LpVariable("	x3390	",lowBound=0, cat= 'Integer')
x3391	=	p.LpVariable("	x3391	",lowBound=0, cat= 'Integer')
x3392	=	p.LpVariable("	x3392	",lowBound=0, cat= 'Integer')
x3393	=	p.LpVariable("	x3393	",lowBound=0, cat= 'Integer')
x3394	=	p.LpVariable("	x3394	",lowBound=0, cat= 'Integer')
x3395	=	p.LpVariable("	x3395	",lowBound=0, cat= 'Integer')
x3396	=	p.LpVariable("	x3396	",lowBound=0, cat= 'Integer')
x3397	=	p.LpVariable("	x3397	",lowBound=0, cat= 'Integer')
x3398	=	p.LpVariable("	x3398	",lowBound=0, cat= 'Integer')
x3399	=	p.LpVariable("	x3399	",lowBound=0, cat= 'Integer')
x3400	=	p.LpVariable("	x3400	",lowBound=0, cat= 'Integer')
x3401	=	p.LpVariable("	x3401	",lowBound=0, cat= 'Integer')
x3402	=	p.LpVariable("	x3402	",lowBound=0, cat= 'Integer')
x3403	=	p.LpVariable("	x3403	",lowBound=0, cat= 'Integer')
x3404	=	p.LpVariable("	x3404	",lowBound=0, cat= 'Integer')
x3405	=	p.LpVariable("	x3405	",lowBound=0, cat= 'Integer')
x3406	=	p.LpVariable("	x3406	",lowBound=0, cat= 'Integer')
x3407	=	p.LpVariable("	x3407	",lowBound=0, cat= 'Integer')
x3408	=	p.LpVariable("	x3408	",lowBound=0, cat= 'Integer')
x3409	=	p.LpVariable("	x3409	",lowBound=0, cat= 'Integer')
x3410	=	p.LpVariable("	x3410	",lowBound=0, cat= 'Integer')
x3411	=	p.LpVariable("	x3411	",lowBound=0, cat= 'Integer')
x3412	=	p.LpVariable("	x3412	",lowBound=0, cat= 'Integer')
x3413	=	p.LpVariable("	x3413	",lowBound=0, cat= 'Integer')
x3414	=	p.LpVariable("	x3414	",lowBound=0, cat= 'Integer')
x3415	=	p.LpVariable("	x3415	",lowBound=0, cat= 'Integer')
x3416	=	p.LpVariable("	x3416	",lowBound=0, cat= 'Integer')
x3417	=	p.LpVariable("	x3417	",lowBound=0, cat= 'Integer')
x3418	=	p.LpVariable("	x3418	",lowBound=0, cat= 'Integer')
x3419	=	p.LpVariable("	x3419	",lowBound=0, cat= 'Integer')
x3420	=	p.LpVariable("	x3420	",lowBound=0, cat= 'Integer')
x3421	=	p.LpVariable("	x3421	",lowBound=0, cat= 'Integer')
x3422	=	p.LpVariable("	x3422	",lowBound=0, cat= 'Integer')
x3423	=	p.LpVariable("	x3423	",lowBound=0, cat= 'Integer')
x3424	=	p.LpVariable("	x3424	",lowBound=0, cat= 'Integer')
x3425	=	p.LpVariable("	x3425	",lowBound=0, cat= 'Integer')
x3426	=	p.LpVariable("	x3426	",lowBound=0, cat= 'Integer')
x3427	=	p.LpVariable("	x3427	",lowBound=0, cat= 'Integer')
x3428	=	p.LpVariable("	x3428	",lowBound=0, cat= 'Integer')
x3429	=	p.LpVariable("	x3429	",lowBound=0, cat= 'Integer')
x3430	=	p.LpVariable("	x3430	",lowBound=0, cat= 'Integer')
x3431	=	p.LpVariable("	x3431	",lowBound=0, cat= 'Integer')
x3432	=	p.LpVariable("	x3432	",lowBound=0, cat= 'Integer')
x3433	=	p.LpVariable("	x3433	",lowBound=0, cat= 'Integer')
x3434	=	p.LpVariable("	x3434	",lowBound=0, cat= 'Integer')
x3435	=	p.LpVariable("	x3435	",lowBound=0, cat= 'Integer')
x3436	=	p.LpVariable("	x3436	",lowBound=0, cat= 'Integer')
x3437	=	p.LpVariable("	x3437	",lowBound=0, cat= 'Integer')
x3438	=	p.LpVariable("	x3438	",lowBound=0, cat= 'Integer')
x3439	=	p.LpVariable("	x3439	",lowBound=0, cat= 'Integer')
x3440	=	p.LpVariable("	x3440	",lowBound=0, cat= 'Integer')
x3441	=	p.LpVariable("	x3441	",lowBound=0, cat= 'Integer')
x3442	=	p.LpVariable("	x3442	",lowBound=0, cat= 'Integer')
x3443	=	p.LpVariable("	x3443	",lowBound=0, cat= 'Integer')
x3444	=	p.LpVariable("	x3444	",lowBound=0, cat= 'Integer')
x3445	=	p.LpVariable("	x3445	",lowBound=0, cat= 'Integer')
x3446	=	p.LpVariable("	x3446	",lowBound=0, cat= 'Integer')
x3447	=	p.LpVariable("	x3447	",lowBound=0, cat= 'Integer')
x3448	=	p.LpVariable("	x3448	",lowBound=0, cat= 'Integer')
x3449	=	p.LpVariable("	x3449	",lowBound=0, cat= 'Integer')
x3450	=	p.LpVariable("	x3450	",lowBound=0, cat= 'Integer')
x3451	=	p.LpVariable("	x3451	",lowBound=0, cat= 'Integer')
x3452	=	p.LpVariable("	x3452	",lowBound=0, cat= 'Integer')
x3453	=	p.LpVariable("	x3453	",lowBound=0, cat= 'Integer')
x3454	=	p.LpVariable("	x3454	",lowBound=0, cat= 'Integer')
x3455	=	p.LpVariable("	x3455	",lowBound=0, cat= 'Integer')
x3456	=	p.LpVariable("	x3456	",lowBound=0, cat= 'Integer')
x3457	=	p.LpVariable("	x3457	",lowBound=0, cat= 'Integer')
x3458	=	p.LpVariable("	x3458	",lowBound=0, cat= 'Integer')
x3459	=	p.LpVariable("	x3459	",lowBound=0, cat= 'Integer')
x3460	=	p.LpVariable("	x3460	",lowBound=0, cat= 'Integer')
x3461	=	p.LpVariable("	x3461	",lowBound=0, cat= 'Integer')
x3462	=	p.LpVariable("	x3462	",lowBound=0, cat= 'Integer')
x3463	=	p.LpVariable("	x3463	",lowBound=0, cat= 'Integer')
x3464	=	p.LpVariable("	x3464	",lowBound=0, cat= 'Integer')
x3465	=	p.LpVariable("	x3465	",lowBound=0, cat= 'Integer')
x3466	=	p.LpVariable("	x3466	",lowBound=0, cat= 'Integer')
x3467	=	p.LpVariable("	x3467	",lowBound=0, cat= 'Integer')
x3468	=	p.LpVariable("	x3468	",lowBound=0, cat= 'Integer')
x3469	=	p.LpVariable("	x3469	",lowBound=0, cat= 'Integer')
x3470	=	p.LpVariable("	x3470	",lowBound=0, cat= 'Integer')
x3471	=	p.LpVariable("	x3471	",lowBound=0, cat= 'Integer')
x3472	=	p.LpVariable("	x3472	",lowBound=0, cat= 'Integer')
x3473	=	p.LpVariable("	x3473	",lowBound=0, cat= 'Integer')
x3474	=	p.LpVariable("	x3474	",lowBound=0, cat= 'Integer')
x3475	=	p.LpVariable("	x3475	",lowBound=0, cat= 'Integer')
x3476	=	p.LpVariable("	x3476	",lowBound=0, cat= 'Integer')
x3477	=	p.LpVariable("	x3477	",lowBound=0, cat= 'Integer')
x3478	=	p.LpVariable("	x3478	",lowBound=0, cat= 'Integer')
x3479	=	p.LpVariable("	x3479	",lowBound=0, cat= 'Integer')
x3480	=	p.LpVariable("	x3480	",lowBound=0, cat= 'Integer')
x3481	=	p.LpVariable("	x3481	",lowBound=0, cat= 'Integer')
x3482	=	p.LpVariable("	x3482	",lowBound=0, cat= 'Integer')
x3483	=	p.LpVariable("	x3483	",lowBound=0, cat= 'Integer')
x3484	=	p.LpVariable("	x3484	",lowBound=0, cat= 'Integer')
x3485	=	p.LpVariable("	x3485	",lowBound=0, cat= 'Integer')
x3486	=	p.LpVariable("	x3486	",lowBound=0, cat= 'Integer')
x3487	=	p.LpVariable("	x3487	",lowBound=0, cat= 'Integer')
x3488	=	p.LpVariable("	x3488	",lowBound=0, cat= 'Integer')
x3489	=	p.LpVariable("	x3489	",lowBound=0, cat= 'Integer')
x3490	=	p.LpVariable("	x3490	",lowBound=0, cat= 'Integer')
x3491	=	p.LpVariable("	x3491	",lowBound=0, cat= 'Integer')
x3492	=	p.LpVariable("	x3492	",lowBound=0, cat= 'Integer')
x3493	=	p.LpVariable("	x3493	",lowBound=0, cat= 'Integer')
x3494	=	p.LpVariable("	x3494	",lowBound=0, cat= 'Integer')
x3495	=	p.LpVariable("	x3495	",lowBound=0, cat= 'Integer')
x3496	=	p.LpVariable("	x3496	",lowBound=0, cat= 'Integer')
x3497	=	p.LpVariable("	x3497	",lowBound=0, cat= 'Integer')
x3498	=	p.LpVariable("	x3498	",lowBound=0, cat= 'Integer')
x3499	=	p.LpVariable("	x3499	",lowBound=0, cat= 'Integer')
x3500	=	p.LpVariable("	x3500	",lowBound=0, cat= 'Integer')
x3501	=	p.LpVariable("	x3501	",lowBound=0, cat= 'Integer')
x3502	=	p.LpVariable("	x3502	",lowBound=0, cat= 'Integer')
x3503	=	p.LpVariable("	x3503	",lowBound=0, cat= 'Integer')
x3504	=	p.LpVariable("	x3504	",lowBound=0, cat= 'Integer')
x3505	=	p.LpVariable("	x3505	",lowBound=0, cat= 'Integer')
x3506	=	p.LpVariable("	x3506	",lowBound=0, cat= 'Integer')
x3507	=	p.LpVariable("	x3507	",lowBound=0, cat= 'Integer')
x3508	=	p.LpVariable("	x3508	",lowBound=0, cat= 'Integer')
x3509	=	p.LpVariable("	x3509	",lowBound=0, cat= 'Integer')
x3510	=	p.LpVariable("	x3510	",lowBound=0, cat= 'Integer')
x3511	=	p.LpVariable("	x3511	",lowBound=0, cat= 'Integer')
x3512	=	p.LpVariable("	x3512	",lowBound=0, cat= 'Integer')
x3513	=	p.LpVariable("	x3513	",lowBound=0, cat= 'Integer')
x3514	=	p.LpVariable("	x3514	",lowBound=0, cat= 'Integer')
x3515	=	p.LpVariable("	x3515	",lowBound=0, cat= 'Integer')
x3516	=	p.LpVariable("	x3516	",lowBound=0, cat= 'Integer')
x3517	=	p.LpVariable("	x3517	",lowBound=0, cat= 'Integer')
x3518	=	p.LpVariable("	x3518	",lowBound=0, cat= 'Integer')
x3519	=	p.LpVariable("	x3519	",lowBound=0, cat= 'Integer')
x3520	=	p.LpVariable("	x3520	",lowBound=0, cat= 'Integer')
x3521	=	p.LpVariable("	x3521	",lowBound=0, cat= 'Integer')
x3522	=	p.LpVariable("	x3522	",lowBound=0, cat= 'Integer')
x3523	=	p.LpVariable("	x3523	",lowBound=0, cat= 'Integer')
x3524	=	p.LpVariable("	x3524	",lowBound=0, cat= 'Integer')
x3525	=	p.LpVariable("	x3525	",lowBound=0, cat= 'Integer')
x3526	=	p.LpVariable("	x3526	",lowBound=0, cat= 'Integer')
x3527	=	p.LpVariable("	x3527	",lowBound=0, cat= 'Integer')
x3528	=	p.LpVariable("	x3528	",lowBound=0, cat= 'Integer')
x3529	=	p.LpVariable("	x3529	",lowBound=0, cat= 'Integer')
x3530	=	p.LpVariable("	x3530	",lowBound=0, cat= 'Integer')
x3531	=	p.LpVariable("	x3531	",lowBound=0, cat= 'Integer')
x3532	=	p.LpVariable("	x3532	",lowBound=0, cat= 'Integer')
x3533	=	p.LpVariable("	x3533	",lowBound=0, cat= 'Integer')
x3534	=	p.LpVariable("	x3534	",lowBound=0, cat= 'Integer')
x3535	=	p.LpVariable("	x3535	",lowBound=0, cat= 'Integer')
x3536	=	p.LpVariable("	x3536	",lowBound=0, cat= 'Integer')
x3537	=	p.LpVariable("	x3537	",lowBound=0, cat= 'Integer')
x3538	=	p.LpVariable("	x3538	",lowBound=0, cat= 'Integer')
x3539	=	p.LpVariable("	x3539	",lowBound=0, cat= 'Integer')
x3540	=	p.LpVariable("	x3540	",lowBound=0, cat= 'Integer')
x3541	=	p.LpVariable("	x3541	",lowBound=0, cat= 'Integer')
x3542	=	p.LpVariable("	x3542	",lowBound=0, cat= 'Integer')
x3543	=	p.LpVariable("	x3543	",lowBound=0, cat= 'Integer')
x3544	=	p.LpVariable("	x3544	",lowBound=0, cat= 'Integer')
x3545	=	p.LpVariable("	x3545	",lowBound=0, cat= 'Integer')
x3546	=	p.LpVariable("	x3546	",lowBound=0, cat= 'Integer')
x3547	=	p.LpVariable("	x3547	",lowBound=0, cat= 'Integer')
x3548	=	p.LpVariable("	x3548	",lowBound=0, cat= 'Integer')
x3549	=	p.LpVariable("	x3549	",lowBound=0, cat= 'Integer')
x3550	=	p.LpVariable("	x3550	",lowBound=0, cat= 'Integer')
x3551	=	p.LpVariable("	x3551	",lowBound=0, cat= 'Integer')
x3552	=	p.LpVariable("	x3552	",lowBound=0, cat= 'Integer')
x3553	=	p.LpVariable("	x3553	",lowBound=0, cat= 'Integer')
x3554	=	p.LpVariable("	x3554	",lowBound=0, cat= 'Integer')
x3555	=	p.LpVariable("	x3555	",lowBound=0, cat= 'Integer')
x3556	=	p.LpVariable("	x3556	",lowBound=0, cat= 'Integer')
x3557	=	p.LpVariable("	x3557	",lowBound=0, cat= 'Integer')
x3558	=	p.LpVariable("	x3558	",lowBound=0, cat= 'Integer')
x3559	=	p.LpVariable("	x3559	",lowBound=0, cat= 'Integer')
x3560	=	p.LpVariable("	x3560	",lowBound=0, cat= 'Integer')
x3561	=	p.LpVariable("	x3561	",lowBound=0, cat= 'Integer')
x3562	=	p.LpVariable("	x3562	",lowBound=0, cat= 'Integer')
x3563	=	p.LpVariable("	x3563	",lowBound=0, cat= 'Integer')
x3564	=	p.LpVariable("	x3564	",lowBound=0, cat= 'Integer')
x3565	=	p.LpVariable("	x3565	",lowBound=0, cat= 'Integer')
x3566	=	p.LpVariable("	x3566	",lowBound=0, cat= 'Integer')
x3567	=	p.LpVariable("	x3567	",lowBound=0, cat= 'Integer')
x3568	=	p.LpVariable("	x3568	",lowBound=0, cat= 'Integer')
x3569	=	p.LpVariable("	x3569	",lowBound=0, cat= 'Integer')
x3570	=	p.LpVariable("	x3570	",lowBound=0, cat= 'Integer')
x3571	=	p.LpVariable("	x3571	",lowBound=0, cat= 'Integer')
x3572	=	p.LpVariable("	x3572	",lowBound=0, cat= 'Integer')
x3573	=	p.LpVariable("	x3573	",lowBound=0, cat= 'Integer')
x3574	=	p.LpVariable("	x3574	",lowBound=0, cat= 'Integer')
x3575	=	p.LpVariable("	x3575	",lowBound=0, cat= 'Integer')
x3576	=	p.LpVariable("	x3576	",lowBound=0, cat= 'Integer')
x3577	=	p.LpVariable("	x3577	",lowBound=0, cat= 'Integer')
x3578	=	p.LpVariable("	x3578	",lowBound=0, cat= 'Integer')
x3579	=	p.LpVariable("	x3579	",lowBound=0, cat= 'Integer')
x3580	=	p.LpVariable("	x3580	",lowBound=0, cat= 'Integer')
x3581	=	p.LpVariable("	x3581	",lowBound=0, cat= 'Integer')
x3582	=	p.LpVariable("	x3582	",lowBound=0, cat= 'Integer')
x3583	=	p.LpVariable("	x3583	",lowBound=0, cat= 'Integer')
x3584	=	p.LpVariable("	x3584	",lowBound=0, cat= 'Integer')
x3585	=	p.LpVariable("	x3585	",lowBound=0, cat= 'Integer')
x3586	=	p.LpVariable("	x3586	",lowBound=0, cat= 'Integer')
x3587	=	p.LpVariable("	x3587	",lowBound=0, cat= 'Integer')
x3588	=	p.LpVariable("	x3588	",lowBound=0, cat= 'Integer')
x3589	=	p.LpVariable("	x3589	",lowBound=0, cat= 'Integer')
x3590	=	p.LpVariable("	x3590	",lowBound=0, cat= 'Integer')
x3591	=	p.LpVariable("	x3591	",lowBound=0, cat= 'Integer')
x3592	=	p.LpVariable("	x3592	",lowBound=0, cat= 'Integer')
x3593	=	p.LpVariable("	x3593	",lowBound=0, cat= 'Integer')
x3594	=	p.LpVariable("	x3594	",lowBound=0, cat= 'Integer')
x3595	=	p.LpVariable("	x3595	",lowBound=0, cat= 'Integer')
x3596	=	p.LpVariable("	x3596	",lowBound=0, cat= 'Integer')
x3597	=	p.LpVariable("	x3597	",lowBound=0, cat= 'Integer')
x3598	=	p.LpVariable("	x3598	",lowBound=0, cat= 'Integer')
x3599	=	p.LpVariable("	x3599	",lowBound=0, cat= 'Integer')
x3600	=	p.LpVariable("	x3600	",lowBound=0, cat= 'Integer')
x3601	=	p.LpVariable("	x3601	",lowBound=0, cat= 'Integer')
x3602	=	p.LpVariable("	x3602	",lowBound=0, cat= 'Integer')
x3603	=	p.LpVariable("	x3603	",lowBound=0, cat= 'Integer')
x3604	=	p.LpVariable("	x3604	",lowBound=0, cat= 'Integer')
x3605	=	p.LpVariable("	x3605	",lowBound=0, cat= 'Integer')
x3606	=	p.LpVariable("	x3606	",lowBound=0, cat= 'Integer')
x3607	=	p.LpVariable("	x3607	",lowBound=0, cat= 'Integer')
x3608	=	p.LpVariable("	x3608	",lowBound=0, cat= 'Integer')
x3609	=	p.LpVariable("	x3609	",lowBound=0, cat= 'Integer')
x3610	=	p.LpVariable("	x3610	",lowBound=0, cat= 'Integer')
x3611	=	p.LpVariable("	x3611	",lowBound=0, cat= 'Integer')
x3612	=	p.LpVariable("	x3612	",lowBound=0, cat= 'Integer')
x3613	=	p.LpVariable("	x3613	",lowBound=0, cat= 'Integer')
x3614	=	p.LpVariable("	x3614	",lowBound=0, cat= 'Integer')
x3615	=	p.LpVariable("	x3615	",lowBound=0, cat= 'Integer')
x3616	=	p.LpVariable("	x3616	",lowBound=0, cat= 'Integer')
x3617	=	p.LpVariable("	x3617	",lowBound=0, cat= 'Integer')
x3618	=	p.LpVariable("	x3618	",lowBound=0, cat= 'Integer')
x3619	=	p.LpVariable("	x3619	",lowBound=0, cat= 'Integer')
x3620	=	p.LpVariable("	x3620	",lowBound=0, cat= 'Integer')
x3621	=	p.LpVariable("	x3621	",lowBound=0, cat= 'Integer')
x3622	=	p.LpVariable("	x3622	",lowBound=0, cat= 'Integer')
x3623	=	p.LpVariable("	x3623	",lowBound=0, cat= 'Integer')
x3624	=	p.LpVariable("	x3624	",lowBound=0, cat= 'Integer')
x3625	=	p.LpVariable("	x3625	",lowBound=0, cat= 'Integer')
x3626	=	p.LpVariable("	x3626	",lowBound=0, cat= 'Integer')
x3627	=	p.LpVariable("	x3627	",lowBound=0, cat= 'Integer')
x3628	=	p.LpVariable("	x3628	",lowBound=0, cat= 'Integer')
x3629	=	p.LpVariable("	x3629	",lowBound=0, cat= 'Integer')
x3630	=	p.LpVariable("	x3630	",lowBound=0, cat= 'Integer')
x3631	=	p.LpVariable("	x3631	",lowBound=0, cat= 'Integer')
x3632	=	p.LpVariable("	x3632	",lowBound=0, cat= 'Integer')
x3633	=	p.LpVariable("	x3633	",lowBound=0, cat= 'Integer')
x3634	=	p.LpVariable("	x3634	",lowBound=0, cat= 'Integer')
x3635	=	p.LpVariable("	x3635	",lowBound=0, cat= 'Integer')
x3636	=	p.LpVariable("	x3636	",lowBound=0, cat= 'Integer')
x3637	=	p.LpVariable("	x3637	",lowBound=0, cat= 'Integer')
x3638	=	p.LpVariable("	x3638	",lowBound=0, cat= 'Integer')
x3639	=	p.LpVariable("	x3639	",lowBound=0, cat= 'Integer')
x3640	=	p.LpVariable("	x3640	",lowBound=0, cat= 'Integer')
x3641	=	p.LpVariable("	x3641	",lowBound=0, cat= 'Integer')
x3642	=	p.LpVariable("	x3642	",lowBound=0, cat= 'Integer')
x3643	=	p.LpVariable("	x3643	",lowBound=0, cat= 'Integer')
x3644	=	p.LpVariable("	x3644	",lowBound=0, cat= 'Integer')
x3645	=	p.LpVariable("	x3645	",lowBound=0, cat= 'Integer')
x3646	=	p.LpVariable("	x3646	",lowBound=0, cat= 'Integer')
x3647	=	p.LpVariable("	x3647	",lowBound=0, cat= 'Integer')
x3648	=	p.LpVariable("	x3648	",lowBound=0, cat= 'Integer')
x3649	=	p.LpVariable("	x3649	",lowBound=0, cat= 'Integer')
x3650	=	p.LpVariable("	x3650	",lowBound=0, cat= 'Integer')
x3651	=	p.LpVariable("	x3651	",lowBound=0, cat= 'Integer')
x3652	=	p.LpVariable("	x3652	",lowBound=0, cat= 'Integer')
x3653	=	p.LpVariable("	x3653	",lowBound=0, cat= 'Integer')
x3654	=	p.LpVariable("	x3654	",lowBound=0, cat= 'Integer')
x3655	=	p.LpVariable("	x3655	",lowBound=0, cat= 'Integer')
x3656	=	p.LpVariable("	x3656	",lowBound=0, cat= 'Integer')
x3657	=	p.LpVariable("	x3657	",lowBound=0, cat= 'Integer')
x3658	=	p.LpVariable("	x3658	",lowBound=0, cat= 'Integer')
x3659	=	p.LpVariable("	x3659	",lowBound=0, cat= 'Integer')
x3660	=	p.LpVariable("	x3660	",lowBound=0, cat= 'Integer')
x3661	=	p.LpVariable("	x3661	",lowBound=0, cat= 'Integer')
x3662	=	p.LpVariable("	x3662	",lowBound=0, cat= 'Integer')
x3663	=	p.LpVariable("	x3663	",lowBound=0, cat= 'Integer')
x3664	=	p.LpVariable("	x3664	",lowBound=0, cat= 'Integer')
x3665	=	p.LpVariable("	x3665	",lowBound=0, cat= 'Integer')
x3666	=	p.LpVariable("	x3666	",lowBound=0, cat= 'Integer')
x3667	=	p.LpVariable("	x3667	",lowBound=0, cat= 'Integer')
x3668	=	p.LpVariable("	x3668	",lowBound=0, cat= 'Integer')
x3669	=	p.LpVariable("	x3669	",lowBound=0, cat= 'Integer')
x3670	=	p.LpVariable("	x3670	",lowBound=0, cat= 'Integer')
x3671	=	p.LpVariable("	x3671	",lowBound=0, cat= 'Integer')
x3672	=	p.LpVariable("	x3672	",lowBound=0, cat= 'Integer')
x3673	=	p.LpVariable("	x3673	",lowBound=0, cat= 'Integer')
x3674	=	p.LpVariable("	x3674	",lowBound=0, cat= 'Integer')
x3675	=	p.LpVariable("	x3675	",lowBound=0, cat= 'Integer')
x3676	=	p.LpVariable("	x3676	",lowBound=0, cat= 'Integer')
x3677	=	p.LpVariable("	x3677	",lowBound=0, cat= 'Integer')
x3678	=	p.LpVariable("	x3678	",lowBound=0, cat= 'Integer')
x3679	=	p.LpVariable("	x3679	",lowBound=0, cat= 'Integer')
x3680	=	p.LpVariable("	x3680	",lowBound=0, cat= 'Integer')
x3681	=	p.LpVariable("	x3681	",lowBound=0, cat= 'Integer')
x3682	=	p.LpVariable("	x3682	",lowBound=0, cat= 'Integer')
x3683	=	p.LpVariable("	x3683	",lowBound=0, cat= 'Integer')
x3684	=	p.LpVariable("	x3684	",lowBound=0, cat= 'Integer')
x3685	=	p.LpVariable("	x3685	",lowBound=0, cat= 'Integer')
x3686	=	p.LpVariable("	x3686	",lowBound=0, cat= 'Integer')
x3687	=	p.LpVariable("	x3687	",lowBound=0, cat= 'Integer')
x3688	=	p.LpVariable("	x3688	",lowBound=0, cat= 'Integer')
x3689	=	p.LpVariable("	x3689	",lowBound=0, cat= 'Integer')
x3690	=	p.LpVariable("	x3690	",lowBound=0, cat= 'Integer')
x3691	=	p.LpVariable("	x3691	",lowBound=0, cat= 'Integer')
x3692	=	p.LpVariable("	x3692	",lowBound=0, cat= 'Integer')
x3693	=	p.LpVariable("	x3693	",lowBound=0, cat= 'Integer')
x3694	=	p.LpVariable("	x3694	",lowBound=0, cat= 'Integer')
x3695	=	p.LpVariable("	x3695	",lowBound=0, cat= 'Integer')
x3696	=	p.LpVariable("	x3696	",lowBound=0, cat= 'Integer')
x3697	=	p.LpVariable("	x3697	",lowBound=0, cat= 'Integer')
x3698	=	p.LpVariable("	x3698	",lowBound=0, cat= 'Integer')
x3699	=	p.LpVariable("	x3699	",lowBound=0, cat= 'Integer')
x3700	=	p.LpVariable("	x3700	",lowBound=0, cat= 'Integer')
x3701	=	p.LpVariable("	x3701	",lowBound=0, cat= 'Integer')
x3702	=	p.LpVariable("	x3702	",lowBound=0, cat= 'Integer')
x3703	=	p.LpVariable("	x3703	",lowBound=0, cat= 'Integer')
x3704	=	p.LpVariable("	x3704	",lowBound=0, cat= 'Integer')
x3705	=	p.LpVariable("	x3705	",lowBound=0, cat= 'Integer')
x3706	=	p.LpVariable("	x3706	",lowBound=0, cat= 'Integer')
x3707	=	p.LpVariable("	x3707	",lowBound=0, cat= 'Integer')
x3708	=	p.LpVariable("	x3708	",lowBound=0, cat= 'Integer')
x3709	=	p.LpVariable("	x3709	",lowBound=0, cat= 'Integer')
x3710	=	p.LpVariable("	x3710	",lowBound=0, cat= 'Integer')
x3711	=	p.LpVariable("	x3711	",lowBound=0, cat= 'Integer')
x3712	=	p.LpVariable("	x3712	",lowBound=0, cat= 'Integer')
x3713	=	p.LpVariable("	x3713	",lowBound=0, cat= 'Integer')
x3714	=	p.LpVariable("	x3714	",lowBound=0, cat= 'Integer')
x3715	=	p.LpVariable("	x3715	",lowBound=0, cat= 'Integer')
x3716	=	p.LpVariable("	x3716	",lowBound=0, cat= 'Integer')
x3717	=	p.LpVariable("	x3717	",lowBound=0, cat= 'Integer')
x3718	=	p.LpVariable("	x3718	",lowBound=0, cat= 'Integer')
x3719	=	p.LpVariable("	x3719	",lowBound=0, cat= 'Integer')
x3720	=	p.LpVariable("	x3720	",lowBound=0, cat= 'Integer')
x3721	=	p.LpVariable("	x3721	",lowBound=0, cat= 'Integer')
x3722	=	p.LpVariable("	x3722	",lowBound=0, cat= 'Integer')
x3723	=	p.LpVariable("	x3723	",lowBound=0, cat= 'Integer')
x3724	=	p.LpVariable("	x3724	",lowBound=0, cat= 'Integer')
x3725	=	p.LpVariable("	x3725	",lowBound=0, cat= 'Integer')
x3726	=	p.LpVariable("	x3726	",lowBound=0, cat= 'Integer')
x3727	=	p.LpVariable("	x3727	",lowBound=0, cat= 'Integer')
x3728	=	p.LpVariable("	x3728	",lowBound=0, cat= 'Integer')
x3729	=	p.LpVariable("	x3729	",lowBound=0, cat= 'Integer')
x3730	=	p.LpVariable("	x3730	",lowBound=0, cat= 'Integer')
x3731	=	p.LpVariable("	x3731	",lowBound=0, cat= 'Integer')
x3732	=	p.LpVariable("	x3732	",lowBound=0, cat= 'Integer')
x3733	=	p.LpVariable("	x3733	",lowBound=0, cat= 'Integer')
x3734	=	p.LpVariable("	x3734	",lowBound=0, cat= 'Integer')
x3735	=	p.LpVariable("	x3735	",lowBound=0, cat= 'Integer')
x3736	=	p.LpVariable("	x3736	",lowBound=0, cat= 'Integer')
x3737	=	p.LpVariable("	x3737	",lowBound=0, cat= 'Integer')
x3738	=	p.LpVariable("	x3738	",lowBound=0, cat= 'Integer')
x3739	=	p.LpVariable("	x3739	",lowBound=0, cat= 'Integer')
x3740	=	p.LpVariable("	x3740	",lowBound=0, cat= 'Integer')
x3741	=	p.LpVariable("	x3741	",lowBound=0, cat= 'Integer')
x3742	=	p.LpVariable("	x3742	",lowBound=0, cat= 'Integer')
x3743	=	p.LpVariable("	x3743	",lowBound=0, cat= 'Integer')
x3744	=	p.LpVariable("	x3744	",lowBound=0, cat= 'Integer')
x3745	=	p.LpVariable("	x3745	",lowBound=0, cat= 'Integer')
x3746	=	p.LpVariable("	x3746	",lowBound=0, cat= 'Integer')
x3747	=	p.LpVariable("	x3747	",lowBound=0, cat= 'Integer')
x3748	=	p.LpVariable("	x3748	",lowBound=0, cat= 'Integer')
x3749	=	p.LpVariable("	x3749	",lowBound=0, cat= 'Integer')
x3750	=	p.LpVariable("	x3750	",lowBound=0, cat= 'Integer')
x3751	=	p.LpVariable("	x3751	",lowBound=0, cat= 'Integer')
x3752	=	p.LpVariable("	x3752	",lowBound=0, cat= 'Integer')
x3753	=	p.LpVariable("	x3753	",lowBound=0, cat= 'Integer')
x3754	=	p.LpVariable("	x3754	",lowBound=0, cat= 'Integer')
x3755	=	p.LpVariable("	x3755	",lowBound=0, cat= 'Integer')
x3756	=	p.LpVariable("	x3756	",lowBound=0, cat= 'Integer')
x3757	=	p.LpVariable("	x3757	",lowBound=0, cat= 'Integer')
x3758	=	p.LpVariable("	x3758	",lowBound=0, cat= 'Integer')
x3759	=	p.LpVariable("	x3759	",lowBound=0, cat= 'Integer')
x3760	=	p.LpVariable("	x3760	",lowBound=0, cat= 'Integer')
x3761	=	p.LpVariable("	x3761	",lowBound=0, cat= 'Integer')
x3762	=	p.LpVariable("	x3762	",lowBound=0, cat= 'Integer')
x3763	=	p.LpVariable("	x3763	",lowBound=0, cat= 'Integer')
x3764	=	p.LpVariable("	x3764	",lowBound=0, cat= 'Integer')
x3765	=	p.LpVariable("	x3765	",lowBound=0, cat= 'Integer')
x3766	=	p.LpVariable("	x3766	",lowBound=0, cat= 'Integer')
x3767	=	p.LpVariable("	x3767	",lowBound=0, cat= 'Integer')
x3768	=	p.LpVariable("	x3768	",lowBound=0, cat= 'Integer')
x3769	=	p.LpVariable("	x3769	",lowBound=0, cat= 'Integer')
x3770	=	p.LpVariable("	x3770	",lowBound=0, cat= 'Integer')
x3771	=	p.LpVariable("	x3771	",lowBound=0, cat= 'Integer')
x3772	=	p.LpVariable("	x3772	",lowBound=0, cat= 'Integer')
x3773	=	p.LpVariable("	x3773	",lowBound=0, cat= 'Integer')
x3774	=	p.LpVariable("	x3774	",lowBound=0, cat= 'Integer')
x3775	=	p.LpVariable("	x3775	",lowBound=0, cat= 'Integer')
x3776	=	p.LpVariable("	x3776	",lowBound=0, cat= 'Integer')
x3777	=	p.LpVariable("	x3777	",lowBound=0, cat= 'Integer')
x3778	=	p.LpVariable("	x3778	",lowBound=0, cat= 'Integer')
x3779	=	p.LpVariable("	x3779	",lowBound=0, cat= 'Integer')
x3780	=	p.LpVariable("	x3780	",lowBound=0, cat= 'Integer')
x3781	=	p.LpVariable("	x3781	",lowBound=0, cat= 'Integer')
x3782	=	p.LpVariable("	x3782	",lowBound=0, cat= 'Integer')
x3783	=	p.LpVariable("	x3783	",lowBound=0, cat= 'Integer')
x3784	=	p.LpVariable("	x3784	",lowBound=0, cat= 'Integer')
x3785	=	p.LpVariable("	x3785	",lowBound=0, cat= 'Integer')
x3786	=	p.LpVariable("	x3786	",lowBound=0, cat= 'Integer')
x3787	=	p.LpVariable("	x3787	",lowBound=0, cat= 'Integer')
x3788	=	p.LpVariable("	x3788	",lowBound=0, cat= 'Integer')
x3789	=	p.LpVariable("	x3789	",lowBound=0, cat= 'Integer')
x3790	=	p.LpVariable("	x3790	",lowBound=0, cat= 'Integer')
x3791	=	p.LpVariable("	x3791	",lowBound=0, cat= 'Integer')
x3792	=	p.LpVariable("	x3792	",lowBound=0, cat= 'Integer')
x3793	=	p.LpVariable("	x3793	",lowBound=0, cat= 'Integer')
x3794	=	p.LpVariable("	x3794	",lowBound=0, cat= 'Integer')
x3795	=	p.LpVariable("	x3795	",lowBound=0, cat= 'Integer')
x3796	=	p.LpVariable("	x3796	",lowBound=0, cat= 'Integer')
x3797	=	p.LpVariable("	x3797	",lowBound=0, cat= 'Integer')
x3798	=	p.LpVariable("	x3798	",lowBound=0, cat= 'Integer')
x3799	=	p.LpVariable("	x3799	",lowBound=0, cat= 'Integer')
x3800	=	p.LpVariable("	x3800	",lowBound=0, cat= 'Integer')
x3801	=	p.LpVariable("	x3801	",lowBound=0, cat= 'Integer')
x3802	=	p.LpVariable("	x3802	",lowBound=0, cat= 'Integer')
x3803	=	p.LpVariable("	x3803	",lowBound=0, cat= 'Integer')
x3804	=	p.LpVariable("	x3804	",lowBound=0, cat= 'Integer')
x3805	=	p.LpVariable("	x3805	",lowBound=0, cat= 'Integer')
x3806	=	p.LpVariable("	x3806	",lowBound=0, cat= 'Integer')
x3807	=	p.LpVariable("	x3807	",lowBound=0, cat= 'Integer')
x3808	=	p.LpVariable("	x3808	",lowBound=0, cat= 'Integer')
x3809	=	p.LpVariable("	x3809	",lowBound=0, cat= 'Integer')
x3810	=	p.LpVariable("	x3810	",lowBound=0, cat= 'Integer')
x3811	=	p.LpVariable("	x3811	",lowBound=0, cat= 'Integer')
x3812	=	p.LpVariable("	x3812	",lowBound=0, cat= 'Integer')
x3813	=	p.LpVariable("	x3813	",lowBound=0, cat= 'Integer')
x3814	=	p.LpVariable("	x3814	",lowBound=0, cat= 'Integer')
x3815	=	p.LpVariable("	x3815	",lowBound=0, cat= 'Integer')
x3816	=	p.LpVariable("	x3816	",lowBound=0, cat= 'Integer')
x3817	=	p.LpVariable("	x3817	",lowBound=0, cat= 'Integer')
x3818	=	p.LpVariable("	x3818	",lowBound=0, cat= 'Integer')
x3819	=	p.LpVariable("	x3819	",lowBound=0, cat= 'Integer')
x3820	=	p.LpVariable("	x3820	",lowBound=0, cat= 'Integer')
x3821	=	p.LpVariable("	x3821	",lowBound=0, cat= 'Integer')
x3822	=	p.LpVariable("	x3822	",lowBound=0, cat= 'Integer')
x3823	=	p.LpVariable("	x3823	",lowBound=0, cat= 'Integer')
x3824	=	p.LpVariable("	x3824	",lowBound=0, cat= 'Integer')
x3825	=	p.LpVariable("	x3825	",lowBound=0, cat= 'Integer')
x3826	=	p.LpVariable("	x3826	",lowBound=0, cat= 'Integer')
x3827	=	p.LpVariable("	x3827	",lowBound=0, cat= 'Integer')
x3828	=	p.LpVariable("	x3828	",lowBound=0, cat= 'Integer')
x3829	=	p.LpVariable("	x3829	",lowBound=0, cat= 'Integer')
x3830	=	p.LpVariable("	x3830	",lowBound=0, cat= 'Integer')
x3831	=	p.LpVariable("	x3831	",lowBound=0, cat= 'Integer')
x3832	=	p.LpVariable("	x3832	",lowBound=0, cat= 'Integer')
x3833	=	p.LpVariable("	x3833	",lowBound=0, cat= 'Integer')
x3834	=	p.LpVariable("	x3834	",lowBound=0, cat= 'Integer')
x3835	=	p.LpVariable("	x3835	",lowBound=0, cat= 'Integer')
x3836	=	p.LpVariable("	x3836	",lowBound=0, cat= 'Integer')
x3837	=	p.LpVariable("	x3837	",lowBound=0, cat= 'Integer')
x3838	=	p.LpVariable("	x3838	",lowBound=0, cat= 'Integer')
x3839	=	p.LpVariable("	x3839	",lowBound=0, cat= 'Integer')
x3840	=	p.LpVariable("	x3840	",lowBound=0, cat= 'Integer')
x3841	=	p.LpVariable("	x3841	",lowBound=0, cat= 'Integer')
x3842	=	p.LpVariable("	x3842	",lowBound=0, cat= 'Integer')
x3843	=	p.LpVariable("	x3843	",lowBound=0, cat= 'Integer')
x3844	=	p.LpVariable("	x3844	",lowBound=0, cat= 'Integer')
x3845	=	p.LpVariable("	x3845	",lowBound=0, cat= 'Integer')
x3846	=	p.LpVariable("	x3846	",lowBound=0, cat= 'Integer')
x3847	=	p.LpVariable("	x3847	",lowBound=0, cat= 'Integer')
x3848	=	p.LpVariable("	x3848	",lowBound=0, cat= 'Integer')
x3849	=	p.LpVariable("	x3849	",lowBound=0, cat= 'Integer')
x3850	=	p.LpVariable("	x3850	",lowBound=0, cat= 'Integer')
x3851	=	p.LpVariable("	x3851	",lowBound=0, cat= 'Integer')
x3852	=	p.LpVariable("	x3852	",lowBound=0, cat= 'Integer')
x3853	=	p.LpVariable("	x3853	",lowBound=0, cat= 'Integer')
x3854	=	p.LpVariable("	x3854	",lowBound=0, cat= 'Integer')
x3855	=	p.LpVariable("	x3855	",lowBound=0, cat= 'Integer')
x3856	=	p.LpVariable("	x3856	",lowBound=0, cat= 'Integer')
x3857	=	p.LpVariable("	x3857	",lowBound=0, cat= 'Integer')
x3858	=	p.LpVariable("	x3858	",lowBound=0, cat= 'Integer')
x3859	=	p.LpVariable("	x3859	",lowBound=0, cat= 'Integer')
x3860	=	p.LpVariable("	x3860	",lowBound=0, cat= 'Integer')
x3861	=	p.LpVariable("	x3861	",lowBound=0, cat= 'Integer')
x3862	=	p.LpVariable("	x3862	",lowBound=0, cat= 'Integer')
x3863	=	p.LpVariable("	x3863	",lowBound=0, cat= 'Integer')
x3864	=	p.LpVariable("	x3864	",lowBound=0, cat= 'Integer')
x3865	=	p.LpVariable("	x3865	",lowBound=0, cat= 'Integer')
x3866	=	p.LpVariable("	x3866	",lowBound=0, cat= 'Integer')
x3867	=	p.LpVariable("	x3867	",lowBound=0, cat= 'Integer')
x3868	=	p.LpVariable("	x3868	",lowBound=0, cat= 'Integer')
x3869	=	p.LpVariable("	x3869	",lowBound=0, cat= 'Integer')
x3870	=	p.LpVariable("	x3870	",lowBound=0, cat= 'Integer')
x3871	=	p.LpVariable("	x3871	",lowBound=0, cat= 'Integer')
x3872	=	p.LpVariable("	x3872	",lowBound=0, cat= 'Integer')
x3873	=	p.LpVariable("	x3873	",lowBound=0, cat= 'Integer')
x3874	=	p.LpVariable("	x3874	",lowBound=0, cat= 'Integer')
x3875	=	p.LpVariable("	x3875	",lowBound=0, cat= 'Integer')
x3876	=	p.LpVariable("	x3876	",lowBound=0, cat= 'Integer')
x3877	=	p.LpVariable("	x3877	",lowBound=0, cat= 'Integer')
x3878	=	p.LpVariable("	x3878	",lowBound=0, cat= 'Integer')
x3879	=	p.LpVariable("	x3879	",lowBound=0, cat= 'Integer')
x3880	=	p.LpVariable("	x3880	",lowBound=0, cat= 'Integer')
x3881	=	p.LpVariable("	x3881	",lowBound=0, cat= 'Integer')
x3882	=	p.LpVariable("	x3882	",lowBound=0, cat= 'Integer')
x3883	=	p.LpVariable("	x3883	",lowBound=0, cat= 'Integer')
x3884	=	p.LpVariable("	x3884	",lowBound=0, cat= 'Integer')
x3885	=	p.LpVariable("	x3885	",lowBound=0, cat= 'Integer')
x3886	=	p.LpVariable("	x3886	",lowBound=0, cat= 'Integer')
x3887	=	p.LpVariable("	x3887	",lowBound=0, cat= 'Integer')
x3888	=	p.LpVariable("	x3888	",lowBound=0, cat= 'Integer')
x3889	=	p.LpVariable("	x3889	",lowBound=0, cat= 'Integer')
x3890	=	p.LpVariable("	x3890	",lowBound=0, cat= 'Integer')
x3891	=	p.LpVariable("	x3891	",lowBound=0, cat= 'Integer')
x3892	=	p.LpVariable("	x3892	",lowBound=0, cat= 'Integer')
x3893	=	p.LpVariable("	x3893	",lowBound=0, cat= 'Integer')
x3894	=	p.LpVariable("	x3894	",lowBound=0, cat= 'Integer')
x3895	=	p.LpVariable("	x3895	",lowBound=0, cat= 'Integer')
x3896	=	p.LpVariable("	x3896	",lowBound=0, cat= 'Integer')
x3897	=	p.LpVariable("	x3897	",lowBound=0, cat= 'Integer')
x3898	=	p.LpVariable("	x3898	",lowBound=0, cat= 'Integer')
x3899	=	p.LpVariable("	x3899	",lowBound=0, cat= 'Integer')
x3900	=	p.LpVariable("	x3900	",lowBound=0, cat= 'Integer')
x3901	=	p.LpVariable("	x3901	",lowBound=0, cat= 'Integer')
x3902	=	p.LpVariable("	x3902	",lowBound=0, cat= 'Integer')
x3903	=	p.LpVariable("	x3903	",lowBound=0, cat= 'Integer')
x3904	=	p.LpVariable("	x3904	",lowBound=0, cat= 'Integer')
x3905	=	p.LpVariable("	x3905	",lowBound=0, cat= 'Integer')
x3906	=	p.LpVariable("	x3906	",lowBound=0, cat= 'Integer')
x3907	=	p.LpVariable("	x3907	",lowBound=0, cat= 'Integer')
x3908	=	p.LpVariable("	x3908	",lowBound=0, cat= 'Integer')
x3909	=	p.LpVariable("	x3909	",lowBound=0, cat= 'Integer')
x3910	=	p.LpVariable("	x3910	",lowBound=0, cat= 'Integer')
x3911	=	p.LpVariable("	x3911	",lowBound=0, cat= 'Integer')
x3912	=	p.LpVariable("	x3912	",lowBound=0, cat= 'Integer')
x3913	=	p.LpVariable("	x3913	",lowBound=0, cat= 'Integer')
x3914	=	p.LpVariable("	x3914	",lowBound=0, cat= 'Integer')
x3915	=	p.LpVariable("	x3915	",lowBound=0, cat= 'Integer')
x3916	=	p.LpVariable("	x3916	",lowBound=0, cat= 'Integer')
x3917	=	p.LpVariable("	x3917	",lowBound=0, cat= 'Integer')
x3918	=	p.LpVariable("	x3918	",lowBound=0, cat= 'Integer')
x3919	=	p.LpVariable("	x3919	",lowBound=0, cat= 'Integer')
x3920	=	p.LpVariable("	x3920	",lowBound=0, cat= 'Integer')
x3921	=	p.LpVariable("	x3921	",lowBound=0, cat= 'Integer')
x3922	=	p.LpVariable("	x3922	",lowBound=0, cat= 'Integer')
x3923	=	p.LpVariable("	x3923	",lowBound=0, cat= 'Integer')
x3924	=	p.LpVariable("	x3924	",lowBound=0, cat= 'Integer')
x3925	=	p.LpVariable("	x3925	",lowBound=0, cat= 'Integer')
x3926	=	p.LpVariable("	x3926	",lowBound=0, cat= 'Integer')
x3927	=	p.LpVariable("	x3927	",lowBound=0, cat= 'Integer')
x3928	=	p.LpVariable("	x3928	",lowBound=0, cat= 'Integer')
x3929	=	p.LpVariable("	x3929	",lowBound=0, cat= 'Integer')
x3930	=	p.LpVariable("	x3930	",lowBound=0, cat= 'Integer')
x3931	=	p.LpVariable("	x3931	",lowBound=0, cat= 'Integer')
x3932	=	p.LpVariable("	x3932	",lowBound=0, cat= 'Integer')
x3933	=	p.LpVariable("	x3933	",lowBound=0, cat= 'Integer')
x3934	=	p.LpVariable("	x3934	",lowBound=0, cat= 'Integer')
x3935	=	p.LpVariable("	x3935	",lowBound=0, cat= 'Integer')
x3936	=	p.LpVariable("	x3936	",lowBound=0, cat= 'Integer')
x3937	=	p.LpVariable("	x3937	",lowBound=0, cat= 'Integer')
x3938	=	p.LpVariable("	x3938	",lowBound=0, cat= 'Integer')
x3939	=	p.LpVariable("	x3939	",lowBound=0, cat= 'Integer')
x3940	=	p.LpVariable("	x3940	",lowBound=0, cat= 'Integer')
x3941	=	p.LpVariable("	x3941	",lowBound=0, cat= 'Integer')
x3942	=	p.LpVariable("	x3942	",lowBound=0, cat= 'Integer')
x3943	=	p.LpVariable("	x3943	",lowBound=0, cat= 'Integer')
x3944	=	p.LpVariable("	x3944	",lowBound=0, cat= 'Integer')
x3945	=	p.LpVariable("	x3945	",lowBound=0, cat= 'Integer')
x3946	=	p.LpVariable("	x3946	",lowBound=0, cat= 'Integer')
x3947	=	p.LpVariable("	x3947	",lowBound=0, cat= 'Integer')
x3948	=	p.LpVariable("	x3948	",lowBound=0, cat= 'Integer')
x3949	=	p.LpVariable("	x3949	",lowBound=0, cat= 'Integer')
x3950	=	p.LpVariable("	x3950	",lowBound=0, cat= 'Integer')
x3951	=	p.LpVariable("	x3951	",lowBound=0, cat= 'Integer')
x3952	=	p.LpVariable("	x3952	",lowBound=0, cat= 'Integer')
x3953	=	p.LpVariable("	x3953	",lowBound=0, cat= 'Integer')
x3954	=	p.LpVariable("	x3954	",lowBound=0, cat= 'Integer')
x3955	=	p.LpVariable("	x3955	",lowBound=0, cat= 'Integer')
x3956	=	p.LpVariable("	x3956	",lowBound=0, cat= 'Integer')
x3957	=	p.LpVariable("	x3957	",lowBound=0, cat= 'Integer')
x3958	=	p.LpVariable("	x3958	",lowBound=0, cat= 'Integer')
x3959	=	p.LpVariable("	x3959	",lowBound=0, cat= 'Integer')
x3960	=	p.LpVariable("	x3960	",lowBound=0, cat= 'Integer')
x3961	=	p.LpVariable("	x3961	",lowBound=0, cat= 'Integer')
x3962	=	p.LpVariable("	x3962	",lowBound=0, cat= 'Integer')
x3963	=	p.LpVariable("	x3963	",lowBound=0, cat= 'Integer')
x3964	=	p.LpVariable("	x3964	",lowBound=0, cat= 'Integer')
x3965	=	p.LpVariable("	x3965	",lowBound=0, cat= 'Integer')
x3966	=	p.LpVariable("	x3966	",lowBound=0, cat= 'Integer')
x3967	=	p.LpVariable("	x3967	",lowBound=0, cat= 'Integer')
x3968	=	p.LpVariable("	x3968	",lowBound=0, cat= 'Integer')
x3969	=	p.LpVariable("	x3969	",lowBound=0, cat= 'Integer')
x3970	=	p.LpVariable("	x3970	",lowBound=0, cat= 'Integer')
x3971	=	p.LpVariable("	x3971	",lowBound=0, cat= 'Integer')
x3972	=	p.LpVariable("	x3972	",lowBound=0, cat= 'Integer')
x3973	=	p.LpVariable("	x3973	",lowBound=0, cat= 'Integer')
x3974	=	p.LpVariable("	x3974	",lowBound=0, cat= 'Integer')
x3975	=	p.LpVariable("	x3975	",lowBound=0, cat= 'Integer')
x3976	=	p.LpVariable("	x3976	",lowBound=0, cat= 'Integer')
x3977	=	p.LpVariable("	x3977	",lowBound=0, cat= 'Integer')
x3978	=	p.LpVariable("	x3978	",lowBound=0, cat= 'Integer')
x3979	=	p.LpVariable("	x3979	",lowBound=0, cat= 'Integer')
x3980	=	p.LpVariable("	x3980	",lowBound=0, cat= 'Integer')
x3981	=	p.LpVariable("	x3981	",lowBound=0, cat= 'Integer')
x3982	=	p.LpVariable("	x3982	",lowBound=0, cat= 'Integer')
x3983	=	p.LpVariable("	x3983	",lowBound=0, cat= 'Integer')
x3984	=	p.LpVariable("	x3984	",lowBound=0, cat= 'Integer')
x3985	=	p.LpVariable("	x3985	",lowBound=0, cat= 'Integer')
x3986	=	p.LpVariable("	x3986	",lowBound=0, cat= 'Integer')
x3987	=	p.LpVariable("	x3987	",lowBound=0, cat= 'Integer')
x3988	=	p.LpVariable("	x3988	",lowBound=0, cat= 'Integer')
x3989	=	p.LpVariable("	x3989	",lowBound=0, cat= 'Integer')
x3990	=	p.LpVariable("	x3990	",lowBound=0, cat= 'Integer')
x3991	=	p.LpVariable("	x3991	",lowBound=0, cat= 'Integer')
x3992	=	p.LpVariable("	x3992	",lowBound=0, cat= 'Integer')
x3993	=	p.LpVariable("	x3993	",lowBound=0, cat= 'Integer')
x3994	=	p.LpVariable("	x3994	",lowBound=0, cat= 'Integer')
x3995	=	p.LpVariable("	x3995	",lowBound=0, cat= 'Integer')
x3996	=	p.LpVariable("	x3996	",lowBound=0, cat= 'Integer')
x3997	=	p.LpVariable("	x3997	",lowBound=0, cat= 'Integer')
x3998	=	p.LpVariable("	x3998	",lowBound=0, cat= 'Integer')
x3999	=	p.LpVariable("	x3999	",lowBound=0, cat= 'Integer')
x4000	=	p.LpVariable("	x4000	",lowBound=0, cat= 'Integer')
x4001	=	p.LpVariable("	x4001	",lowBound=0, cat= 'Integer')
x4002	=	p.LpVariable("	x4002	",lowBound=0, cat= 'Integer')
x4003	=	p.LpVariable("	x4003	",lowBound=0, cat= 'Integer')
x4004	=	p.LpVariable("	x4004	",lowBound=0, cat= 'Integer')
x4005	=	p.LpVariable("	x4005	",lowBound=0, cat= 'Integer')
x4006	=	p.LpVariable("	x4006	",lowBound=0, cat= 'Integer')
x4007	=	p.LpVariable("	x4007	",lowBound=0, cat= 'Integer')
x4008	=	p.LpVariable("	x4008	",lowBound=0, cat= 'Integer')
x4009	=	p.LpVariable("	x4009	",lowBound=0, cat= 'Integer')
x4010	=	p.LpVariable("	x4010	",lowBound=0, cat= 'Integer')
x4011	=	p.LpVariable("	x4011	",lowBound=0, cat= 'Integer')
x4012	=	p.LpVariable("	x4012	",lowBound=0, cat= 'Integer')
x4013	=	p.LpVariable("	x4013	",lowBound=0, cat= 'Integer')
x4014	=	p.LpVariable("	x4014	",lowBound=0, cat= 'Integer')
x4015	=	p.LpVariable("	x4015	",lowBound=0, cat= 'Integer')
x4016	=	p.LpVariable("	x4016	",lowBound=0, cat= 'Integer')
x4017	=	p.LpVariable("	x4017	",lowBound=0, cat= 'Integer')
x4018	=	p.LpVariable("	x4018	",lowBound=0, cat= 'Integer')
x4019	=	p.LpVariable("	x4019	",lowBound=0, cat= 'Integer')
x4020	=	p.LpVariable("	x4020	",lowBound=0, cat= 'Integer')
x4021	=	p.LpVariable("	x4021	",lowBound=0, cat= 'Integer')
x4022	=	p.LpVariable("	x4022	",lowBound=0, cat= 'Integer')
x4023	=	p.LpVariable("	x4023	",lowBound=0, cat= 'Integer')
x4024	=	p.LpVariable("	x4024	",lowBound=0, cat= 'Integer')
x4025	=	p.LpVariable("	x4025	",lowBound=0, cat= 'Integer')
x4026	=	p.LpVariable("	x4026	",lowBound=0, cat= 'Integer')
x4027	=	p.LpVariable("	x4027	",lowBound=0, cat= 'Integer')
x4028	=	p.LpVariable("	x4028	",lowBound=0, cat= 'Integer')
x4029	=	p.LpVariable("	x4029	",lowBound=0, cat= 'Integer')
x4030	=	p.LpVariable("	x4030	",lowBound=0, cat= 'Integer')
x4031	=	p.LpVariable("	x4031	",lowBound=0, cat= 'Integer')
x4032	=	p.LpVariable("	x4032	",lowBound=0, cat= 'Integer')
x4033	=	p.LpVariable("	x4033	",lowBound=0, cat= 'Integer')
x4034	=	p.LpVariable("	x4034	",lowBound=0, cat= 'Integer')
x4035	=	p.LpVariable("	x4035	",lowBound=0, cat= 'Integer')
x4036	=	p.LpVariable("	x4036	",lowBound=0, cat= 'Integer')
x4037	=	p.LpVariable("	x4037	",lowBound=0, cat= 'Integer')
x4038	=	p.LpVariable("	x4038	",lowBound=0, cat= 'Integer')
x4039	=	p.LpVariable("	x4039	",lowBound=0, cat= 'Integer')
x4040	=	p.LpVariable("	x4040	",lowBound=0, cat= 'Integer')
x4041	=	p.LpVariable("	x4041	",lowBound=0, cat= 'Integer')
x4042	=	p.LpVariable("	x4042	",lowBound=0, cat= 'Integer')
x4043	=	p.LpVariable("	x4043	",lowBound=0, cat= 'Integer')
x4044	=	p.LpVariable("	x4044	",lowBound=0, cat= 'Integer')
x4045	=	p.LpVariable("	x4045	",lowBound=0, cat= 'Integer')
x4046	=	p.LpVariable("	x4046	",lowBound=0, cat= 'Integer')
x4047	=	p.LpVariable("	x4047	",lowBound=0, cat= 'Integer')
x4048	=	p.LpVariable("	x4048	",lowBound=0, cat= 'Integer')
x4049	=	p.LpVariable("	x4049	",lowBound=0, cat= 'Integer')
x4050	=	p.LpVariable("	x4050	",lowBound=0, cat= 'Integer')
x4051	=	p.LpVariable("	x4051	",lowBound=0, cat= 'Integer')
x4052	=	p.LpVariable("	x4052	",lowBound=0, cat= 'Integer')
x4053	=	p.LpVariable("	x4053	",lowBound=0, cat= 'Integer')
x4054	=	p.LpVariable("	x4054	",lowBound=0, cat= 'Integer')
x4055	=	p.LpVariable("	x4055	",lowBound=0, cat= 'Integer')
x4056	=	p.LpVariable("	x4056	",lowBound=0, cat= 'Integer')
x4057	=	p.LpVariable("	x4057	",lowBound=0, cat= 'Integer')
x4058	=	p.LpVariable("	x4058	",lowBound=0, cat= 'Integer')
x4059	=	p.LpVariable("	x4059	",lowBound=0, cat= 'Integer')
x4060	=	p.LpVariable("	x4060	",lowBound=0, cat= 'Integer')
x4061	=	p.LpVariable("	x4061	",lowBound=0, cat= 'Integer')
x4062	=	p.LpVariable("	x4062	",lowBound=0, cat= 'Integer')
x4063	=	p.LpVariable("	x4063	",lowBound=0, cat= 'Integer')
x4064	=	p.LpVariable("	x4064	",lowBound=0, cat= 'Integer')
x4065	=	p.LpVariable("	x4065	",lowBound=0, cat= 'Integer')
x4066	=	p.LpVariable("	x4066	",lowBound=0, cat= 'Integer')
x4067	=	p.LpVariable("	x4067	",lowBound=0, cat= 'Integer')
x4068	=	p.LpVariable("	x4068	",lowBound=0, cat= 'Integer')
x4069	=	p.LpVariable("	x4069	",lowBound=0, cat= 'Integer')
x4070	=	p.LpVariable("	x4070	",lowBound=0, cat= 'Integer')
x4071	=	p.LpVariable("	x4071	",lowBound=0, cat= 'Integer')
x4072	=	p.LpVariable("	x4072	",lowBound=0, cat= 'Integer')
x4073	=	p.LpVariable("	x4073	",lowBound=0, cat= 'Integer')
x4074	=	p.LpVariable("	x4074	",lowBound=0, cat= 'Integer')
x4075	=	p.LpVariable("	x4075	",lowBound=0, cat= 'Integer')
x4076	=	p.LpVariable("	x4076	",lowBound=0, cat= 'Integer')
x4077	=	p.LpVariable("	x4077	",lowBound=0, cat= 'Integer')
x4078	=	p.LpVariable("	x4078	",lowBound=0, cat= 'Integer')
x4079	=	p.LpVariable("	x4079	",lowBound=0, cat= 'Integer')
x4080	=	p.LpVariable("	x4080	",lowBound=0, cat= 'Integer')
x4081	=	p.LpVariable("	x4081	",lowBound=0, cat= 'Integer')
x4082	=	p.LpVariable("	x4082	",lowBound=0, cat= 'Integer')
x4083	=	p.LpVariable("	x4083	",lowBound=0, cat= 'Integer')
x4084	=	p.LpVariable("	x4084	",lowBound=0, cat= 'Integer')
x4085	=	p.LpVariable("	x4085	",lowBound=0, cat= 'Integer')
x4086	=	p.LpVariable("	x4086	",lowBound=0, cat= 'Integer')
x4087	=	p.LpVariable("	x4087	",lowBound=0, cat= 'Integer')
x4088	=	p.LpVariable("	x4088	",lowBound=0, cat= 'Integer')
x4089	=	p.LpVariable("	x4089	",lowBound=0, cat= 'Integer')
x4090	=	p.LpVariable("	x4090	",lowBound=0, cat= 'Integer')
x4091	=	p.LpVariable("	x4091	",lowBound=0, cat= 'Integer')
x4092	=	p.LpVariable("	x4092	",lowBound=0, cat= 'Integer')
x4093	=	p.LpVariable("	x4093	",lowBound=0, cat= 'Integer')
x4094	=	p.LpVariable("	x4094	",lowBound=0, cat= 'Integer')
x4095	=	p.LpVariable("	x4095	",lowBound=0, cat= 'Integer')
x4096	=	p.LpVariable("	x4096	",lowBound=0, cat= 'Integer')
x4097	=	p.LpVariable("	x4097	",lowBound=0, cat= 'Integer')
x4098	=	p.LpVariable("	x4098	",lowBound=0, cat= 'Integer')
x4099	=	p.LpVariable("	x4099	",lowBound=0, cat= 'Integer')
x4100	=	p.LpVariable("	x4100	",lowBound=0, cat= 'Integer')
x4101	=	p.LpVariable("	x4101	",lowBound=0, cat= 'Integer')
x4102	=	p.LpVariable("	x4102	",lowBound=0, cat= 'Integer')
x4103	=	p.LpVariable("	x4103	",lowBound=0, cat= 'Integer')
x4104	=	p.LpVariable("	x4104	",lowBound=0, cat= 'Integer')
x4105	=	p.LpVariable("	x4105	",lowBound=0, cat= 'Integer')
x4106	=	p.LpVariable("	x4106	",lowBound=0, cat= 'Integer')
x4107	=	p.LpVariable("	x4107	",lowBound=0, cat= 'Integer')
x4108	=	p.LpVariable("	x4108	",lowBound=0, cat= 'Integer')
x4109	=	p.LpVariable("	x4109	",lowBound=0, cat= 'Integer')
x4110	=	p.LpVariable("	x4110	",lowBound=0, cat= 'Integer')
x4111	=	p.LpVariable("	x4111	",lowBound=0, cat= 'Integer')
x4112	=	p.LpVariable("	x4112	",lowBound=0, cat= 'Integer')
x4113	=	p.LpVariable("	x4113	",lowBound=0, cat= 'Integer')
x4114	=	p.LpVariable("	x4114	",lowBound=0, cat= 'Integer')
x4115	=	p.LpVariable("	x4115	",lowBound=0, cat= 'Integer')
x4116	=	p.LpVariable("	x4116	",lowBound=0, cat= 'Integer')
x4117	=	p.LpVariable("	x4117	",lowBound=0, cat= 'Integer')
x4118	=	p.LpVariable("	x4118	",lowBound=0, cat= 'Integer')
x4119	=	p.LpVariable("	x4119	",lowBound=0, cat= 'Integer')
x4120	=	p.LpVariable("	x4120	",lowBound=0, cat= 'Integer')
x4121	=	p.LpVariable("	x4121	",lowBound=0, cat= 'Integer')
x4122	=	p.LpVariable("	x4122	",lowBound=0, cat= 'Integer')
x4123	=	p.LpVariable("	x4123	",lowBound=0, cat= 'Integer')
x4124	=	p.LpVariable("	x4124	",lowBound=0, cat= 'Integer')
x4125	=	p.LpVariable("	x4125	",lowBound=0, cat= 'Integer')
x4126	=	p.LpVariable("	x4126	",lowBound=0, cat= 'Integer')
x4127	=	p.LpVariable("	x4127	",lowBound=0, cat= 'Integer')
x4128	=	p.LpVariable("	x4128	",lowBound=0, cat= 'Integer')
x4129	=	p.LpVariable("	x4129	",lowBound=0, cat= 'Integer')
x4130	=	p.LpVariable("	x4130	",lowBound=0, cat= 'Integer')
x4131	=	p.LpVariable("	x4131	",lowBound=0, cat= 'Integer')
x4132	=	p.LpVariable("	x4132	",lowBound=0, cat= 'Integer')
x4133	=	p.LpVariable("	x4133	",lowBound=0, cat= 'Integer')
x4134	=	p.LpVariable("	x4134	",lowBound=0, cat= 'Integer')
x4135	=	p.LpVariable("	x4135	",lowBound=0, cat= 'Integer')
x4136	=	p.LpVariable("	x4136	",lowBound=0, cat= 'Integer')
x4137	=	p.LpVariable("	x4137	",lowBound=0, cat= 'Integer')
x4138	=	p.LpVariable("	x4138	",lowBound=0, cat= 'Integer')
x4139	=	p.LpVariable("	x4139	",lowBound=0, cat= 'Integer')
x4140	=	p.LpVariable("	x4140	",lowBound=0, cat= 'Integer')
x4141	=	p.LpVariable("	x4141	",lowBound=0, cat= 'Integer')
x4142	=	p.LpVariable("	x4142	",lowBound=0, cat= 'Integer')
x4143	=	p.LpVariable("	x4143	",lowBound=0, cat= 'Integer')
x4144	=	p.LpVariable("	x4144	",lowBound=0, cat= 'Integer')
x4145	=	p.LpVariable("	x4145	",lowBound=0, cat= 'Integer')
x4146	=	p.LpVariable("	x4146	",lowBound=0, cat= 'Integer')
x4147	=	p.LpVariable("	x4147	",lowBound=0, cat= 'Integer')
x4148	=	p.LpVariable("	x4148	",lowBound=0, cat= 'Integer')
x4149	=	p.LpVariable("	x4149	",lowBound=0, cat= 'Integer')
x4150	=	p.LpVariable("	x4150	",lowBound=0, cat= 'Integer')
x4151	=	p.LpVariable("	x4151	",lowBound=0, cat= 'Integer')
x4152	=	p.LpVariable("	x4152	",lowBound=0, cat= 'Integer')
x4153	=	p.LpVariable("	x4153	",lowBound=0, cat= 'Integer')
x4154	=	p.LpVariable("	x4154	",lowBound=0, cat= 'Integer')
x4155	=	p.LpVariable("	x4155	",lowBound=0, cat= 'Integer')
x4156	=	p.LpVariable("	x4156	",lowBound=0, cat= 'Integer')
x4157	=	p.LpVariable("	x4157	",lowBound=0, cat= 'Integer')
x4158	=	p.LpVariable("	x4158	",lowBound=0, cat= 'Integer')
x4159	=	p.LpVariable("	x4159	",lowBound=0, cat= 'Integer')
x4160	=	p.LpVariable("	x4160	",lowBound=0, cat= 'Integer')
x4161	=	p.LpVariable("	x4161	",lowBound=0, cat= 'Integer')
x4162	=	p.LpVariable("	x4162	",lowBound=0, cat= 'Integer')
x4163	=	p.LpVariable("	x4163	",lowBound=0, cat= 'Integer')
x4164	=	p.LpVariable("	x4164	",lowBound=0, cat= 'Integer')
x4165	=	p.LpVariable("	x4165	",lowBound=0, cat= 'Integer')
x4166	=	p.LpVariable("	x4166	",lowBound=0, cat= 'Integer')
x4167	=	p.LpVariable("	x4167	",lowBound=0, cat= 'Integer')
x4168	=	p.LpVariable("	x4168	",lowBound=0, cat= 'Integer')
x4169	=	p.LpVariable("	x4169	",lowBound=0, cat= 'Integer')
x4170	=	p.LpVariable("	x4170	",lowBound=0, cat= 'Integer')
x4171	=	p.LpVariable("	x4171	",lowBound=0, cat= 'Integer')
x4172	=	p.LpVariable("	x4172	",lowBound=0, cat= 'Integer')
x4173	=	p.LpVariable("	x4173	",lowBound=0, cat= 'Integer')
x4174	=	p.LpVariable("	x4174	",lowBound=0, cat= 'Integer')
x4175	=	p.LpVariable("	x4175	",lowBound=0, cat= 'Integer')
x4176	=	p.LpVariable("	x4176	",lowBound=0, cat= 'Integer')
x4177	=	p.LpVariable("	x4177	",lowBound=0, cat= 'Integer')
x4178	=	p.LpVariable("	x4178	",lowBound=0, cat= 'Integer')
x4179	=	p.LpVariable("	x4179	",lowBound=0, cat= 'Integer')
x4180	=	p.LpVariable("	x4180	",lowBound=0, cat= 'Integer')
x4181	=	p.LpVariable("	x4181	",lowBound=0, cat= 'Integer')
x4182	=	p.LpVariable("	x4182	",lowBound=0, cat= 'Integer')
x4183	=	p.LpVariable("	x4183	",lowBound=0, cat= 'Integer')
x4184	=	p.LpVariable("	x4184	",lowBound=0, cat= 'Integer')
x4185	=	p.LpVariable("	x4185	",lowBound=0, cat= 'Integer')
x4186	=	p.LpVariable("	x4186	",lowBound=0, cat= 'Integer')
x4187	=	p.LpVariable("	x4187	",lowBound=0, cat= 'Integer')
x4188	=	p.LpVariable("	x4188	",lowBound=0, cat= 'Integer')
x4189	=	p.LpVariable("	x4189	",lowBound=0, cat= 'Integer')
x4190	=	p.LpVariable("	x4190	",lowBound=0, cat= 'Integer')
x4191	=	p.LpVariable("	x4191	",lowBound=0, cat= 'Integer')
x4192	=	p.LpVariable("	x4192	",lowBound=0, cat= 'Integer')
x4193	=	p.LpVariable("	x4193	",lowBound=0, cat= 'Integer')
x4194	=	p.LpVariable("	x4194	",lowBound=0, cat= 'Integer')
x4195	=	p.LpVariable("	x4195	",lowBound=0, cat= 'Integer')
x4196	=	p.LpVariable("	x4196	",lowBound=0, cat= 'Integer')
x4197	=	p.LpVariable("	x4197	",lowBound=0, cat= 'Integer')
x4198	=	p.LpVariable("	x4198	",lowBound=0, cat= 'Integer')
x4199	=	p.LpVariable("	x4199	",lowBound=0, cat= 'Integer')
x4200	=	p.LpVariable("	x4200	",lowBound=0, cat= 'Integer')
x4201	=	p.LpVariable("	x4201	",lowBound=0, cat= 'Integer')
x4202	=	p.LpVariable("	x4202	",lowBound=0, cat= 'Integer')
x4203	=	p.LpVariable("	x4203	",lowBound=0, cat= 'Integer')
x4204	=	p.LpVariable("	x4204	",lowBound=0, cat= 'Integer')
x4205	=	p.LpVariable("	x4205	",lowBound=0, cat= 'Integer')
x4206	=	p.LpVariable("	x4206	",lowBound=0, cat= 'Integer')
x4207	=	p.LpVariable("	x4207	",lowBound=0, cat= 'Integer')
x4208	=	p.LpVariable("	x4208	",lowBound=0, cat= 'Integer')
x4209	=	p.LpVariable("	x4209	",lowBound=0, cat= 'Integer')
x4210	=	p.LpVariable("	x4210	",lowBound=0, cat= 'Integer')
x4211	=	p.LpVariable("	x4211	",lowBound=0, cat= 'Integer')
x4212	=	p.LpVariable("	x4212	",lowBound=0, cat= 'Integer')
x4213	=	p.LpVariable("	x4213	",lowBound=0, cat= 'Integer')
x4214	=	p.LpVariable("	x4214	",lowBound=0, cat= 'Integer')
x4215	=	p.LpVariable("	x4215	",lowBound=0, cat= 'Integer')
x4216	=	p.LpVariable("	x4216	",lowBound=0, cat= 'Integer')
x4217	=	p.LpVariable("	x4217	",lowBound=0, cat= 'Integer')
x4218	=	p.LpVariable("	x4218	",lowBound=0, cat= 'Integer')
x4219	=	p.LpVariable("	x4219	",lowBound=0, cat= 'Integer')
x4220	=	p.LpVariable("	x4220	",lowBound=0, cat= 'Integer')
x4221	=	p.LpVariable("	x4221	",lowBound=0, cat= 'Integer')
x4222	=	p.LpVariable("	x4222	",lowBound=0, cat= 'Integer')
x4223	=	p.LpVariable("	x4223	",lowBound=0, cat= 'Integer')
x4224	=	p.LpVariable("	x4224	",lowBound=0, cat= 'Integer')
x4225	=	p.LpVariable("	x4225	",lowBound=0, cat= 'Integer')
x4226	=	p.LpVariable("	x4226	",lowBound=0, cat= 'Integer')
x4227	=	p.LpVariable("	x4227	",lowBound=0, cat= 'Integer')
x4228	=	p.LpVariable("	x4228	",lowBound=0, cat= 'Integer')
x4229	=	p.LpVariable("	x4229	",lowBound=0, cat= 'Integer')
x4230	=	p.LpVariable("	x4230	",lowBound=0, cat= 'Integer')
x4231	=	p.LpVariable("	x4231	",lowBound=0, cat= 'Integer')
x4232	=	p.LpVariable("	x4232	",lowBound=0, cat= 'Integer')
x4233	=	p.LpVariable("	x4233	",lowBound=0, cat= 'Integer')
x4234	=	p.LpVariable("	x4234	",lowBound=0, cat= 'Integer')
x4235	=	p.LpVariable("	x4235	",lowBound=0, cat= 'Integer')
x4236	=	p.LpVariable("	x4236	",lowBound=0, cat= 'Integer')
x4237	=	p.LpVariable("	x4237	",lowBound=0, cat= 'Integer')
x4238	=	p.LpVariable("	x4238	",lowBound=0, cat= 'Integer')
x4239	=	p.LpVariable("	x4239	",lowBound=0, cat= 'Integer')
x4240	=	p.LpVariable("	x4240	",lowBound=0, cat= 'Integer')
x4241	=	p.LpVariable("	x4241	",lowBound=0, cat= 'Integer')
x4242	=	p.LpVariable("	x4242	",lowBound=0, cat= 'Integer')
x4243	=	p.LpVariable("	x4243	",lowBound=0, cat= 'Integer')
x4244	=	p.LpVariable("	x4244	",lowBound=0, cat= 'Integer')
x4245	=	p.LpVariable("	x4245	",lowBound=0, cat= 'Integer')
x4246	=	p.LpVariable("	x4246	",lowBound=0, cat= 'Integer')
x4247	=	p.LpVariable("	x4247	",lowBound=0, cat= 'Integer')
x4248	=	p.LpVariable("	x4248	",lowBound=0, cat= 'Integer')
x4249	=	p.LpVariable("	x4249	",lowBound=0, cat= 'Integer')
x4250	=	p.LpVariable("	x4250	",lowBound=0, cat= 'Integer')
x4251	=	p.LpVariable("	x4251	",lowBound=0, cat= 'Integer')
x4252	=	p.LpVariable("	x4252	",lowBound=0, cat= 'Integer')
x4253	=	p.LpVariable("	x4253	",lowBound=0, cat= 'Integer')
x4254	=	p.LpVariable("	x4254	",lowBound=0, cat= 'Integer')
x4255	=	p.LpVariable("	x4255	",lowBound=0, cat= 'Integer')
x4256	=	p.LpVariable("	x4256	",lowBound=0, cat= 'Integer')
x4257	=	p.LpVariable("	x4257	",lowBound=0, cat= 'Integer')
x4258	=	p.LpVariable("	x4258	",lowBound=0, cat= 'Integer')
x4259	=	p.LpVariable("	x4259	",lowBound=0, cat= 'Integer')
x4260	=	p.LpVariable("	x4260	",lowBound=0, cat= 'Integer')
x4261	=	p.LpVariable("	x4261	",lowBound=0, cat= 'Integer')
x4262	=	p.LpVariable("	x4262	",lowBound=0, cat= 'Integer')
x4263	=	p.LpVariable("	x4263	",lowBound=0, cat= 'Integer')
x4264	=	p.LpVariable("	x4264	",lowBound=0, cat= 'Integer')
x4265	=	p.LpVariable("	x4265	",lowBound=0, cat= 'Integer')
x4266	=	p.LpVariable("	x4266	",lowBound=0, cat= 'Integer')
x4267	=	p.LpVariable("	x4267	",lowBound=0, cat= 'Integer')
x4268	=	p.LpVariable("	x4268	",lowBound=0, cat= 'Integer')
x4269	=	p.LpVariable("	x4269	",lowBound=0, cat= 'Integer')
x4270	=	p.LpVariable("	x4270	",lowBound=0, cat= 'Integer')
x4271	=	p.LpVariable("	x4271	",lowBound=0, cat= 'Integer')
x4272	=	p.LpVariable("	x4272	",lowBound=0, cat= 'Integer')
x4273	=	p.LpVariable("	x4273	",lowBound=0, cat= 'Integer')
x4274	=	p.LpVariable("	x4274	",lowBound=0, cat= 'Integer')
x4275	=	p.LpVariable("	x4275	",lowBound=0, cat= 'Integer')
x4276	=	p.LpVariable("	x4276	",lowBound=0, cat= 'Integer')
x4277	=	p.LpVariable("	x4277	",lowBound=0, cat= 'Integer')
x4278	=	p.LpVariable("	x4278	",lowBound=0, cat= 'Integer')
x4279	=	p.LpVariable("	x4279	",lowBound=0, cat= 'Integer')
x4280	=	p.LpVariable("	x4280	",lowBound=0, cat= 'Integer')
x4281	=	p.LpVariable("	x4281	",lowBound=0, cat= 'Integer')
x4282	=	p.LpVariable("	x4282	",lowBound=0, cat= 'Integer')
x4283	=	p.LpVariable("	x4283	",lowBound=0, cat= 'Integer')
x4284	=	p.LpVariable("	x4284	",lowBound=0, cat= 'Integer')
x4285	=	p.LpVariable("	x4285	",lowBound=0, cat= 'Integer')
x4286	=	p.LpVariable("	x4286	",lowBound=0, cat= 'Integer')
x4287	=	p.LpVariable("	x4287	",lowBound=0, cat= 'Integer')
x4288	=	p.LpVariable("	x4288	",lowBound=0, cat= 'Integer')
x4289	=	p.LpVariable("	x4289	",lowBound=0, cat= 'Integer')
x4290	=	p.LpVariable("	x4290	",lowBound=0, cat= 'Integer')
x4291	=	p.LpVariable("	x4291	",lowBound=0, cat= 'Integer')
x4292	=	p.LpVariable("	x4292	",lowBound=0, cat= 'Integer')
x4293	=	p.LpVariable("	x4293	",lowBound=0, cat= 'Integer')
x4294	=	p.LpVariable("	x4294	",lowBound=0, cat= 'Integer')
x4295	=	p.LpVariable("	x4295	",lowBound=0, cat= 'Integer')
x4296	=	p.LpVariable("	x4296	",lowBound=0, cat= 'Integer')
x4297	=	p.LpVariable("	x4297	",lowBound=0, cat= 'Integer')
x4298	=	p.LpVariable("	x4298	",lowBound=0, cat= 'Integer')
x4299	=	p.LpVariable("	x4299	",lowBound=0, cat= 'Integer')
x4300	=	p.LpVariable("	x4300	",lowBound=0, cat= 'Integer')
x4301	=	p.LpVariable("	x4301	",lowBound=0, cat= 'Integer')
x4302	=	p.LpVariable("	x4302	",lowBound=0, cat= 'Integer')
x4303	=	p.LpVariable("	x4303	",lowBound=0, cat= 'Integer')
x4304	=	p.LpVariable("	x4304	",lowBound=0, cat= 'Integer')
x4305	=	p.LpVariable("	x4305	",lowBound=0, cat= 'Integer')
x4306	=	p.LpVariable("	x4306	",lowBound=0, cat= 'Integer')
x4307	=	p.LpVariable("	x4307	",lowBound=0, cat= 'Integer')
x4308	=	p.LpVariable("	x4308	",lowBound=0, cat= 'Integer')
x4309	=	p.LpVariable("	x4309	",lowBound=0, cat= 'Integer')
x4310	=	p.LpVariable("	x4310	",lowBound=0, cat= 'Integer')
x4311	=	p.LpVariable("	x4311	",lowBound=0, cat= 'Integer')
x4312	=	p.LpVariable("	x4312	",lowBound=0, cat= 'Integer')
x4313	=	p.LpVariable("	x4313	",lowBound=0, cat= 'Integer')
x4314	=	p.LpVariable("	x4314	",lowBound=0, cat= 'Integer')
x4315	=	p.LpVariable("	x4315	",lowBound=0, cat= 'Integer')
x4316	=	p.LpVariable("	x4316	",lowBound=0, cat= 'Integer')
x4317	=	p.LpVariable("	x4317	",lowBound=0, cat= 'Integer')
x4318	=	p.LpVariable("	x4318	",lowBound=0, cat= 'Integer')
x4319	=	p.LpVariable("	x4319	",lowBound=0, cat= 'Integer')
x4320	=	p.LpVariable("	x4320	",lowBound=0, cat= 'Integer')
x4321	=	p.LpVariable("	x4321	",lowBound=0, cat= 'Integer')
x4322	=	p.LpVariable("	x4322	",lowBound=0, cat= 'Integer')
x4323	=	p.LpVariable("	x4323	",lowBound=0, cat= 'Integer')
x4324	=	p.LpVariable("	x4324	",lowBound=0, cat= 'Integer')
x4325	=	p.LpVariable("	x4325	",lowBound=0, cat= 'Integer')
x4326	=	p.LpVariable("	x4326	",lowBound=0, cat= 'Integer')
x4327	=	p.LpVariable("	x4327	",lowBound=0, cat= 'Integer')
x4328	=	p.LpVariable("	x4328	",lowBound=0, cat= 'Integer')
x4329	=	p.LpVariable("	x4329	",lowBound=0, cat= 'Integer')
x4330	=	p.LpVariable("	x4330	",lowBound=0, cat= 'Integer')
x4331	=	p.LpVariable("	x4331	",lowBound=0, cat= 'Integer')
x4332	=	p.LpVariable("	x4332	",lowBound=0, cat= 'Integer')
x4333	=	p.LpVariable("	x4333	",lowBound=0, cat= 'Integer')
x4334	=	p.LpVariable("	x4334	",lowBound=0, cat= 'Integer')
x4335	=	p.LpVariable("	x4335	",lowBound=0, cat= 'Integer')
x4336	=	p.LpVariable("	x4336	",lowBound=0, cat= 'Integer')
x4337	=	p.LpVariable("	x4337	",lowBound=0, cat= 'Integer')
x4338	=	p.LpVariable("	x4338	",lowBound=0, cat= 'Integer')
x4339	=	p.LpVariable("	x4339	",lowBound=0, cat= 'Integer')
x4340	=	p.LpVariable("	x4340	",lowBound=0, cat= 'Integer')
x4341	=	p.LpVariable("	x4341	",lowBound=0, cat= 'Integer')
x4342	=	p.LpVariable("	x4342	",lowBound=0, cat= 'Integer')
x4343	=	p.LpVariable("	x4343	",lowBound=0, cat= 'Integer')
x4344	=	p.LpVariable("	x4344	",lowBound=0, cat= 'Integer')
x4345	=	p.LpVariable("	x4345	",lowBound=0, cat= 'Integer')
x4346	=	p.LpVariable("	x4346	",lowBound=0, cat= 'Integer')
x4347	=	p.LpVariable("	x4347	",lowBound=0, cat= 'Integer')
x4348	=	p.LpVariable("	x4348	",lowBound=0, cat= 'Integer')
x4349	=	p.LpVariable("	x4349	",lowBound=0, cat= 'Integer')
x4350	=	p.LpVariable("	x4350	",lowBound=0, cat= 'Integer')
x4351	=	p.LpVariable("	x4351	",lowBound=0, cat= 'Integer')
x4352	=	p.LpVariable("	x4352	",lowBound=0, cat= 'Integer')
x4353	=	p.LpVariable("	x4353	",lowBound=0, cat= 'Integer')
x4354	=	p.LpVariable("	x4354	",lowBound=0, cat= 'Integer')
x4355	=	p.LpVariable("	x4355	",lowBound=0, cat= 'Integer')
x4356	=	p.LpVariable("	x4356	",lowBound=0, cat= 'Integer')
x4357	=	p.LpVariable("	x4357	",lowBound=0, cat= 'Integer')
x4358	=	p.LpVariable("	x4358	",lowBound=0, cat= 'Integer')
x4359	=	p.LpVariable("	x4359	",lowBound=0, cat= 'Integer')
x4360	=	p.LpVariable("	x4360	",lowBound=0, cat= 'Integer')
x4361	=	p.LpVariable("	x4361	",lowBound=0, cat= 'Integer')
x4362	=	p.LpVariable("	x4362	",lowBound=0, cat= 'Integer')
x4363	=	p.LpVariable("	x4363	",lowBound=0, cat= 'Integer')
x4364	=	p.LpVariable("	x4364	",lowBound=0, cat= 'Integer')
x4365	=	p.LpVariable("	x4365	",lowBound=0, cat= 'Integer')
x4366	=	p.LpVariable("	x4366	",lowBound=0, cat= 'Integer')
x4367	=	p.LpVariable("	x4367	",lowBound=0, cat= 'Integer')
x4368	=	p.LpVariable("	x4368	",lowBound=0, cat= 'Integer')
x4369	=	p.LpVariable("	x4369	",lowBound=0, cat= 'Integer')
x4370	=	p.LpVariable("	x4370	",lowBound=0, cat= 'Integer')
x4371	=	p.LpVariable("	x4371	",lowBound=0, cat= 'Integer')
x4372	=	p.LpVariable("	x4372	",lowBound=0, cat= 'Integer')
x4373	=	p.LpVariable("	x4373	",lowBound=0, cat= 'Integer')
x4374	=	p.LpVariable("	x4374	",lowBound=0, cat= 'Integer')
x4375	=	p.LpVariable("	x4375	",lowBound=0, cat= 'Integer')
x4376	=	p.LpVariable("	x4376	",lowBound=0, cat= 'Integer')
x4377	=	p.LpVariable("	x4377	",lowBound=0, cat= 'Integer')
x4378	=	p.LpVariable("	x4378	",lowBound=0, cat= 'Integer')
x4379	=	p.LpVariable("	x4379	",lowBound=0, cat= 'Integer')
x4380	=	p.LpVariable("	x4380	",lowBound=0, cat= 'Integer')
x4381	=	p.LpVariable("	x4381	",lowBound=0, cat= 'Integer')
x4382	=	p.LpVariable("	x4382	",lowBound=0, cat= 'Integer')
x4383	=	p.LpVariable("	x4383	",lowBound=0, cat= 'Integer')
x4384	=	p.LpVariable("	x4384	",lowBound=0, cat= 'Integer')
x4385	=	p.LpVariable("	x4385	",lowBound=0, cat= 'Integer')
x4386	=	p.LpVariable("	x4386	",lowBound=0, cat= 'Integer')
x4387	=	p.LpVariable("	x4387	",lowBound=0, cat= 'Integer')
x4388	=	p.LpVariable("	x4388	",lowBound=0, cat= 'Integer')
x4389	=	p.LpVariable("	x4389	",lowBound=0, cat= 'Integer')
x4390	=	p.LpVariable("	x4390	",lowBound=0, cat= 'Integer')
x4391	=	p.LpVariable("	x4391	",lowBound=0, cat= 'Integer')
x4392	=	p.LpVariable("	x4392	",lowBound=0, cat= 'Integer')
x4393	=	p.LpVariable("	x4393	",lowBound=0, cat= 'Integer')
x4394	=	p.LpVariable("	x4394	",lowBound=0, cat= 'Integer')
x4395	=	p.LpVariable("	x4395	",lowBound=0, cat= 'Integer')
x4396	=	p.LpVariable("	x4396	",lowBound=0, cat= 'Integer')
x4397	=	p.LpVariable("	x4397	",lowBound=0, cat= 'Integer')
x4398	=	p.LpVariable("	x4398	",lowBound=0, cat= 'Integer')
x4399	=	p.LpVariable("	x4399	",lowBound=0, cat= 'Integer')
x4400	=	p.LpVariable("	x4400	",lowBound=0, cat= 'Integer')
x4401	=	p.LpVariable("	x4401	",lowBound=0, cat= 'Integer')
x4402	=	p.LpVariable("	x4402	",lowBound=0, cat= 'Integer')
x4403	=	p.LpVariable("	x4403	",lowBound=0, cat= 'Integer')
x4404	=	p.LpVariable("	x4404	",lowBound=0, cat= 'Integer')
x4405	=	p.LpVariable("	x4405	",lowBound=0, cat= 'Integer')
x4406	=	p.LpVariable("	x4406	",lowBound=0, cat= 'Integer')
x4407	=	p.LpVariable("	x4407	",lowBound=0, cat= 'Integer')
x4408	=	p.LpVariable("	x4408	",lowBound=0, cat= 'Integer')
x4409	=	p.LpVariable("	x4409	",lowBound=0, cat= 'Integer')
x4410	=	p.LpVariable("	x4410	",lowBound=0, cat= 'Integer')
x4411	=	p.LpVariable("	x4411	",lowBound=0, cat= 'Integer')
x4412	=	p.LpVariable("	x4412	",lowBound=0, cat= 'Integer')
x4413	=	p.LpVariable("	x4413	",lowBound=0, cat= 'Integer')
x4414	=	p.LpVariable("	x4414	",lowBound=0, cat= 'Integer')
x4415	=	p.LpVariable("	x4415	",lowBound=0, cat= 'Integer')
x4416	=	p.LpVariable("	x4416	",lowBound=0, cat= 'Integer')
x4417	=	p.LpVariable("	x4417	",lowBound=0, cat= 'Integer')
x4418	=	p.LpVariable("	x4418	",lowBound=0, cat= 'Integer')
x4419	=	p.LpVariable("	x4419	",lowBound=0, cat= 'Integer')
x4420	=	p.LpVariable("	x4420	",lowBound=0, cat= 'Integer')
x4421	=	p.LpVariable("	x4421	",lowBound=0, cat= 'Integer')
x4422	=	p.LpVariable("	x4422	",lowBound=0, cat= 'Integer')
x4423	=	p.LpVariable("	x4423	",lowBound=0, cat= 'Integer')
x4424	=	p.LpVariable("	x4424	",lowBound=0, cat= 'Integer')
x4425	=	p.LpVariable("	x4425	",lowBound=0, cat= 'Integer')
x4426	=	p.LpVariable("	x4426	",lowBound=0, cat= 'Integer')
x4427	=	p.LpVariable("	x4427	",lowBound=0, cat= 'Integer')
x4428	=	p.LpVariable("	x4428	",lowBound=0, cat= 'Integer')
x4429	=	p.LpVariable("	x4429	",lowBound=0, cat= 'Integer')
x4430	=	p.LpVariable("	x4430	",lowBound=0, cat= 'Integer')
x4431	=	p.LpVariable("	x4431	",lowBound=0, cat= 'Integer')
x4432	=	p.LpVariable("	x4432	",lowBound=0, cat= 'Integer')
x4433	=	p.LpVariable("	x4433	",lowBound=0, cat= 'Integer')
x4434	=	p.LpVariable("	x4434	",lowBound=0, cat= 'Integer')
x4435	=	p.LpVariable("	x4435	",lowBound=0, cat= 'Integer')
x4436	=	p.LpVariable("	x4436	",lowBound=0, cat= 'Integer')
x4437	=	p.LpVariable("	x4437	",lowBound=0, cat= 'Integer')
x4438	=	p.LpVariable("	x4438	",lowBound=0, cat= 'Integer')
x4439	=	p.LpVariable("	x4439	",lowBound=0, cat= 'Integer')
x4440	=	p.LpVariable("	x4440	",lowBound=0, cat= 'Integer')
x4441	=	p.LpVariable("	x4441	",lowBound=0, cat= 'Integer')
x4442	=	p.LpVariable("	x4442	",lowBound=0, cat= 'Integer')
x4443	=	p.LpVariable("	x4443	",lowBound=0, cat= 'Integer')
x4444	=	p.LpVariable("	x4444	",lowBound=0, cat= 'Integer')
x4445	=	p.LpVariable("	x4445	",lowBound=0, cat= 'Integer')
x4446	=	p.LpVariable("	x4446	",lowBound=0, cat= 'Integer')
x4447	=	p.LpVariable("	x4447	",lowBound=0, cat= 'Integer')
x4448	=	p.LpVariable("	x4448	",lowBound=0, cat= 'Integer')
x4449	=	p.LpVariable("	x4449	",lowBound=0, cat= 'Integer')
x4450	=	p.LpVariable("	x4450	",lowBound=0, cat= 'Integer')
x4451	=	p.LpVariable("	x4451	",lowBound=0, cat= 'Integer')
x4452	=	p.LpVariable("	x4452	",lowBound=0, cat= 'Integer')
x4453	=	p.LpVariable("	x4453	",lowBound=0, cat= 'Integer')
x4454	=	p.LpVariable("	x4454	",lowBound=0, cat= 'Integer')
x4455	=	p.LpVariable("	x4455	",lowBound=0, cat= 'Integer')
x4456	=	p.LpVariable("	x4456	",lowBound=0, cat= 'Integer')
x4457	=	p.LpVariable("	x4457	",lowBound=0, cat= 'Integer')
x4458	=	p.LpVariable("	x4458	",lowBound=0, cat= 'Integer')
x4459	=	p.LpVariable("	x4459	",lowBound=0, cat= 'Integer')
x4460	=	p.LpVariable("	x4460	",lowBound=0, cat= 'Integer')
x4461	=	p.LpVariable("	x4461	",lowBound=0, cat= 'Integer')
x4462	=	p.LpVariable("	x4462	",lowBound=0, cat= 'Integer')
x4463	=	p.LpVariable("	x4463	",lowBound=0, cat= 'Integer')
x4464	=	p.LpVariable("	x4464	",lowBound=0, cat= 'Integer')
x4465	=	p.LpVariable("	x4465	",lowBound=0, cat= 'Integer')
x4466	=	p.LpVariable("	x4466	",lowBound=0, cat= 'Integer')
x4467	=	p.LpVariable("	x4467	",lowBound=0, cat= 'Integer')
x4468	=	p.LpVariable("	x4468	",lowBound=0, cat= 'Integer')
x4469	=	p.LpVariable("	x4469	",lowBound=0, cat= 'Integer')
x4470	=	p.LpVariable("	x4470	",lowBound=0, cat= 'Integer')
x4471	=	p.LpVariable("	x4471	",lowBound=0, cat= 'Integer')
x4472	=	p.LpVariable("	x4472	",lowBound=0, cat= 'Integer')
x4473	=	p.LpVariable("	x4473	",lowBound=0, cat= 'Integer')
x4474	=	p.LpVariable("	x4474	",lowBound=0, cat= 'Integer')
x4475	=	p.LpVariable("	x4475	",lowBound=0, cat= 'Integer')
x4476	=	p.LpVariable("	x4476	",lowBound=0, cat= 'Integer')
x4477	=	p.LpVariable("	x4477	",lowBound=0, cat= 'Integer')
x4478	=	p.LpVariable("	x4478	",lowBound=0, cat= 'Integer')
x4479	=	p.LpVariable("	x4479	",lowBound=0, cat= 'Integer')
x4480	=	p.LpVariable("	x4480	",lowBound=0, cat= 'Integer')
x4481	=	p.LpVariable("	x4481	",lowBound=0, cat= 'Integer')
x4482	=	p.LpVariable("	x4482	",lowBound=0, cat= 'Integer')
x4483	=	p.LpVariable("	x4483	",lowBound=0, cat= 'Integer')
x4484	=	p.LpVariable("	x4484	",lowBound=0, cat= 'Integer')
x4485	=	p.LpVariable("	x4485	",lowBound=0, cat= 'Integer')
x4486	=	p.LpVariable("	x4486	",lowBound=0, cat= 'Integer')
x4487	=	p.LpVariable("	x4487	",lowBound=0, cat= 'Integer')
x4488	=	p.LpVariable("	x4488	",lowBound=0, cat= 'Integer')
x4489	=	p.LpVariable("	x4489	",lowBound=0, cat= 'Integer')
x4490	=	p.LpVariable("	x4490	",lowBound=0, cat= 'Integer')
x4491	=	p.LpVariable("	x4491	",lowBound=0, cat= 'Integer')
x4492	=	p.LpVariable("	x4492	",lowBound=0, cat= 'Integer')
x4493	=	p.LpVariable("	x4493	",lowBound=0, cat= 'Integer')
x4494	=	p.LpVariable("	x4494	",lowBound=0, cat= 'Integer')
x4495	=	p.LpVariable("	x4495	",lowBound=0, cat= 'Integer')
x4496	=	p.LpVariable("	x4496	",lowBound=0, cat= 'Integer')
x4497	=	p.LpVariable("	x4497	",lowBound=0, cat= 'Integer')
x4498	=	p.LpVariable("	x4498	",lowBound=0, cat= 'Integer')
x4499	=	p.LpVariable("	x4499	",lowBound=0, cat= 'Integer')
x4500	=	p.LpVariable("	x4500	",lowBound=0, cat= 'Integer')
x4501	=	p.LpVariable("	x4501	",lowBound=0, cat= 'Integer')
x4502	=	p.LpVariable("	x4502	",lowBound=0, cat= 'Integer')
x4503	=	p.LpVariable("	x4503	",lowBound=0, cat= 'Integer')
x4504	=	p.LpVariable("	x4504	",lowBound=0, cat= 'Integer')
x4505	=	p.LpVariable("	x4505	",lowBound=0, cat= 'Integer')
x4506	=	p.LpVariable("	x4506	",lowBound=0, cat= 'Integer')
x4507	=	p.LpVariable("	x4507	",lowBound=0, cat= 'Integer')
x4508	=	p.LpVariable("	x4508	",lowBound=0, cat= 'Integer')
x4509	=	p.LpVariable("	x4509	",lowBound=0, cat= 'Integer')
x4510	=	p.LpVariable("	x4510	",lowBound=0, cat= 'Integer')
x4511	=	p.LpVariable("	x4511	",lowBound=0, cat= 'Integer')
x4512	=	p.LpVariable("	x4512	",lowBound=0, cat= 'Integer')
x4513	=	p.LpVariable("	x4513	",lowBound=0, cat= 'Integer')
x4514	=	p.LpVariable("	x4514	",lowBound=0, cat= 'Integer')
x4515	=	p.LpVariable("	x4515	",lowBound=0, cat= 'Integer')
x4516	=	p.LpVariable("	x4516	",lowBound=0, cat= 'Integer')
x4517	=	p.LpVariable("	x4517	",lowBound=0, cat= 'Integer')
x4518	=	p.LpVariable("	x4518	",lowBound=0, cat= 'Integer')
x4519	=	p.LpVariable("	x4519	",lowBound=0, cat= 'Integer')
x4520	=	p.LpVariable("	x4520	",lowBound=0, cat= 'Integer')
x4521	=	p.LpVariable("	x4521	",lowBound=0, cat= 'Integer')
x4522	=	p.LpVariable("	x4522	",lowBound=0, cat= 'Integer')
x4523	=	p.LpVariable("	x4523	",lowBound=0, cat= 'Integer')
x4524	=	p.LpVariable("	x4524	",lowBound=0, cat= 'Integer')
x4525	=	p.LpVariable("	x4525	",lowBound=0, cat= 'Integer')
x4526	=	p.LpVariable("	x4526	",lowBound=0, cat= 'Integer')
x4527	=	p.LpVariable("	x4527	",lowBound=0, cat= 'Integer')
x4528	=	p.LpVariable("	x4528	",lowBound=0, cat= 'Integer')
x4529	=	p.LpVariable("	x4529	",lowBound=0, cat= 'Integer')
x4530	=	p.LpVariable("	x4530	",lowBound=0, cat= 'Integer')
x4531	=	p.LpVariable("	x4531	",lowBound=0, cat= 'Integer')
x4532	=	p.LpVariable("	x4532	",lowBound=0, cat= 'Integer')
x4533	=	p.LpVariable("	x4533	",lowBound=0, cat= 'Integer')
x4534	=	p.LpVariable("	x4534	",lowBound=0, cat= 'Integer')
x4535	=	p.LpVariable("	x4535	",lowBound=0, cat= 'Integer')
x4536	=	p.LpVariable("	x4536	",lowBound=0, cat= 'Integer')
x4537	=	p.LpVariable("	x4537	",lowBound=0, cat= 'Integer')
x4538	=	p.LpVariable("	x4538	",lowBound=0, cat= 'Integer')
x4539	=	p.LpVariable("	x4539	",lowBound=0, cat= 'Integer')
x4540	=	p.LpVariable("	x4540	",lowBound=0, cat= 'Integer')
x4541	=	p.LpVariable("	x4541	",lowBound=0, cat= 'Integer')
x4542	=	p.LpVariable("	x4542	",lowBound=0, cat= 'Integer')
x4543	=	p.LpVariable("	x4543	",lowBound=0, cat= 'Integer')
x4544	=	p.LpVariable("	x4544	",lowBound=0, cat= 'Integer')
x4545	=	p.LpVariable("	x4545	",lowBound=0, cat= 'Integer')
x4546	=	p.LpVariable("	x4546	",lowBound=0, cat= 'Integer')
x4547	=	p.LpVariable("	x4547	",lowBound=0, cat= 'Integer')
x4548	=	p.LpVariable("	x4548	",lowBound=0, cat= 'Integer')
x4549	=	p.LpVariable("	x4549	",lowBound=0, cat= 'Integer')
x4550	=	p.LpVariable("	x4550	",lowBound=0, cat= 'Integer')
x4551	=	p.LpVariable("	x4551	",lowBound=0, cat= 'Integer')
x4552	=	p.LpVariable("	x4552	",lowBound=0, cat= 'Integer')
x4553	=	p.LpVariable("	x4553	",lowBound=0, cat= 'Integer')
x4554	=	p.LpVariable("	x4554	",lowBound=0, cat= 'Integer')
x4555	=	p.LpVariable("	x4555	",lowBound=0, cat= 'Integer')
x4556	=	p.LpVariable("	x4556	",lowBound=0, cat= 'Integer')
x4557	=	p.LpVariable("	x4557	",lowBound=0, cat= 'Integer')
x4558	=	p.LpVariable("	x4558	",lowBound=0, cat= 'Integer')
x4559	=	p.LpVariable("	x4559	",lowBound=0, cat= 'Integer')
x4560	=	p.LpVariable("	x4560	",lowBound=0, cat= 'Integer')
x4561	=	p.LpVariable("	x4561	",lowBound=0, cat= 'Integer')
x4562	=	p.LpVariable("	x4562	",lowBound=0, cat= 'Integer')
x4563	=	p.LpVariable("	x4563	",lowBound=0, cat= 'Integer')
x4564	=	p.LpVariable("	x4564	",lowBound=0, cat= 'Integer')
x4565	=	p.LpVariable("	x4565	",lowBound=0, cat= 'Integer')
x4566	=	p.LpVariable("	x4566	",lowBound=0, cat= 'Integer')
x4567	=	p.LpVariable("	x4567	",lowBound=0, cat= 'Integer')
x4568	=	p.LpVariable("	x4568	",lowBound=0, cat= 'Integer')
x4569	=	p.LpVariable("	x4569	",lowBound=0, cat= 'Integer')
x4570	=	p.LpVariable("	x4570	",lowBound=0, cat= 'Integer')
x4571	=	p.LpVariable("	x4571	",lowBound=0, cat= 'Integer')
x4572	=	p.LpVariable("	x4572	",lowBound=0, cat= 'Integer')
x4573	=	p.LpVariable("	x4573	",lowBound=0, cat= 'Integer')
x4574	=	p.LpVariable("	x4574	",lowBound=0, cat= 'Integer')
x4575	=	p.LpVariable("	x4575	",lowBound=0, cat= 'Integer')
x4576	=	p.LpVariable("	x4576	",lowBound=0, cat= 'Integer')
x4577	=	p.LpVariable("	x4577	",lowBound=0, cat= 'Integer')
x4578	=	p.LpVariable("	x4578	",lowBound=0, cat= 'Integer')
x4579	=	p.LpVariable("	x4579	",lowBound=0, cat= 'Integer')
x4580	=	p.LpVariable("	x4580	",lowBound=0, cat= 'Integer')
x4581	=	p.LpVariable("	x4581	",lowBound=0, cat= 'Integer')
x4582	=	p.LpVariable("	x4582	",lowBound=0, cat= 'Integer')
x4583	=	p.LpVariable("	x4583	",lowBound=0, cat= 'Integer')
x4584	=	p.LpVariable("	x4584	",lowBound=0, cat= 'Integer')
x4585	=	p.LpVariable("	x4585	",lowBound=0, cat= 'Integer')
x4586	=	p.LpVariable("	x4586	",lowBound=0, cat= 'Integer')
x4587	=	p.LpVariable("	x4587	",lowBound=0, cat= 'Integer')
x4588	=	p.LpVariable("	x4588	",lowBound=0, cat= 'Integer')
x4589	=	p.LpVariable("	x4589	",lowBound=0, cat= 'Integer')
x4590	=	p.LpVariable("	x4590	",lowBound=0, cat= 'Integer')
x4591	=	p.LpVariable("	x4591	",lowBound=0, cat= 'Integer')
x4592	=	p.LpVariable("	x4592	",lowBound=0, cat= 'Integer')
x4593	=	p.LpVariable("	x4593	",lowBound=0, cat= 'Integer')
x4594	=	p.LpVariable("	x4594	",lowBound=0, cat= 'Integer')
x4595	=	p.LpVariable("	x4595	",lowBound=0, cat= 'Integer')
x4596	=	p.LpVariable("	x4596	",lowBound=0, cat= 'Integer')
x4597	=	p.LpVariable("	x4597	",lowBound=0, cat= 'Integer')
x4598	=	p.LpVariable("	x4598	",lowBound=0, cat= 'Integer')
x4599	=	p.LpVariable("	x4599	",lowBound=0, cat= 'Integer')
x4600	=	p.LpVariable("	x4600	",lowBound=0, cat= 'Integer')
x4601	=	p.LpVariable("	x4601	",lowBound=0, cat= 'Integer')
x4602	=	p.LpVariable("	x4602	",lowBound=0, cat= 'Integer')
x4603	=	p.LpVariable("	x4603	",lowBound=0, cat= 'Integer')
x4604	=	p.LpVariable("	x4604	",lowBound=0, cat= 'Integer')
x4605	=	p.LpVariable("	x4605	",lowBound=0, cat= 'Integer')
x4606	=	p.LpVariable("	x4606	",lowBound=0, cat= 'Integer')
x4607	=	p.LpVariable("	x4607	",lowBound=0, cat= 'Integer')
x4608	=	p.LpVariable("	x4608	",lowBound=0, cat= 'Integer')
x4609	=	p.LpVariable("	x4609	",lowBound=0, cat= 'Integer')
x4610	=	p.LpVariable("	x4610	",lowBound=0, cat= 'Integer')
x4611	=	p.LpVariable("	x4611	",lowBound=0, cat= 'Integer')
x4612	=	p.LpVariable("	x4612	",lowBound=0, cat= 'Integer')
x4613	=	p.LpVariable("	x4613	",lowBound=0, cat= 'Integer')
x4614	=	p.LpVariable("	x4614	",lowBound=0, cat= 'Integer')
x4615	=	p.LpVariable("	x4615	",lowBound=0, cat= 'Integer')
x4616	=	p.LpVariable("	x4616	",lowBound=0, cat= 'Integer')
x4617	=	p.LpVariable("	x4617	",lowBound=0, cat= 'Integer')
x4618	=	p.LpVariable("	x4618	",lowBound=0, cat= 'Integer')
x4619	=	p.LpVariable("	x4619	",lowBound=0, cat= 'Integer')
x4620	=	p.LpVariable("	x4620	",lowBound=0, cat= 'Integer')
x4621	=	p.LpVariable("	x4621	",lowBound=0, cat= 'Integer')
x4622	=	p.LpVariable("	x4622	",lowBound=0, cat= 'Integer')
x4623	=	p.LpVariable("	x4623	",lowBound=0, cat= 'Integer')
x4624	=	p.LpVariable("	x4624	",lowBound=0, cat= 'Integer')
x4625	=	p.LpVariable("	x4625	",lowBound=0, cat= 'Integer')
x4626	=	p.LpVariable("	x4626	",lowBound=0, cat= 'Integer')
x4627	=	p.LpVariable("	x4627	",lowBound=0, cat= 'Integer')
x4628	=	p.LpVariable("	x4628	",lowBound=0, cat= 'Integer')
x4629	=	p.LpVariable("	x4629	",lowBound=0, cat= 'Integer')
x4630	=	p.LpVariable("	x4630	",lowBound=0, cat= 'Integer')
x4631	=	p.LpVariable("	x4631	",lowBound=0, cat= 'Integer')
x4632	=	p.LpVariable("	x4632	",lowBound=0, cat= 'Integer')
x4633	=	p.LpVariable("	x4633	",lowBound=0, cat= 'Integer')
x4634	=	p.LpVariable("	x4634	",lowBound=0, cat= 'Integer')
x4635	=	p.LpVariable("	x4635	",lowBound=0, cat= 'Integer')
x4636	=	p.LpVariable("	x4636	",lowBound=0, cat= 'Integer')
x4637	=	p.LpVariable("	x4637	",lowBound=0, cat= 'Integer')
x4638	=	p.LpVariable("	x4638	",lowBound=0, cat= 'Integer')
x4639	=	p.LpVariable("	x4639	",lowBound=0, cat= 'Integer')
x4640	=	p.LpVariable("	x4640	",lowBound=0, cat= 'Integer')
x4641	=	p.LpVariable("	x4641	",lowBound=0, cat= 'Integer')
x4642	=	p.LpVariable("	x4642	",lowBound=0, cat= 'Integer')
x4643	=	p.LpVariable("	x4643	",lowBound=0, cat= 'Integer')
x4644	=	p.LpVariable("	x4644	",lowBound=0, cat= 'Integer')
x4645	=	p.LpVariable("	x4645	",lowBound=0, cat= 'Integer')
x4646	=	p.LpVariable("	x4646	",lowBound=0, cat= 'Integer')
x4647	=	p.LpVariable("	x4647	",lowBound=0, cat= 'Integer')
x4648	=	p.LpVariable("	x4648	",lowBound=0, cat= 'Integer')
x4649	=	p.LpVariable("	x4649	",lowBound=0, cat= 'Integer')
x4650	=	p.LpVariable("	x4650	",lowBound=0, cat= 'Integer')
x4651	=	p.LpVariable("	x4651	",lowBound=0, cat= 'Integer')
x4652	=	p.LpVariable("	x4652	",lowBound=0, cat= 'Integer')
x4653	=	p.LpVariable("	x4653	",lowBound=0, cat= 'Integer')
x4654	=	p.LpVariable("	x4654	",lowBound=0, cat= 'Integer')
x4655	=	p.LpVariable("	x4655	",lowBound=0, cat= 'Integer')
x4656	=	p.LpVariable("	x4656	",lowBound=0, cat= 'Integer')
x4657	=	p.LpVariable("	x4657	",lowBound=0, cat= 'Integer')
x4658	=	p.LpVariable("	x4658	",lowBound=0, cat= 'Integer')
x4659	=	p.LpVariable("	x4659	",lowBound=0, cat= 'Integer')
x4660	=	p.LpVariable("	x4660	",lowBound=0, cat= 'Integer')
x4661	=	p.LpVariable("	x4661	",lowBound=0, cat= 'Integer')
x4662	=	p.LpVariable("	x4662	",lowBound=0, cat= 'Integer')
x4663	=	p.LpVariable("	x4663	",lowBound=0, cat= 'Integer')
x4664	=	p.LpVariable("	x4664	",lowBound=0, cat= 'Integer')
x4665	=	p.LpVariable("	x4665	",lowBound=0, cat= 'Integer')
x4666	=	p.LpVariable("	x4666	",lowBound=0, cat= 'Integer')
x4667	=	p.LpVariable("	x4667	",lowBound=0, cat= 'Integer')
x4668	=	p.LpVariable("	x4668	",lowBound=0, cat= 'Integer')
x4669	=	p.LpVariable("	x4669	",lowBound=0, cat= 'Integer')
x4670	=	p.LpVariable("	x4670	",lowBound=0, cat= 'Integer')
x4671	=	p.LpVariable("	x4671	",lowBound=0, cat= 'Integer')
x4672	=	p.LpVariable("	x4672	",lowBound=0, cat= 'Integer')
x4673	=	p.LpVariable("	x4673	",lowBound=0, cat= 'Integer')
x4674	=	p.LpVariable("	x4674	",lowBound=0, cat= 'Integer')
x4675	=	p.LpVariable("	x4675	",lowBound=0, cat= 'Integer')
x4676	=	p.LpVariable("	x4676	",lowBound=0, cat= 'Integer')
x4677	=	p.LpVariable("	x4677	",lowBound=0, cat= 'Integer')
x4678	=	p.LpVariable("	x4678	",lowBound=0, cat= 'Integer')
x4679	=	p.LpVariable("	x4679	",lowBound=0, cat= 'Integer')
x4680	=	p.LpVariable("	x4680	",lowBound=0, cat= 'Integer')
x4681	=	p.LpVariable("	x4681	",lowBound=0, cat= 'Integer')
x4682	=	p.LpVariable("	x4682	",lowBound=0, cat= 'Integer')
x4683	=	p.LpVariable("	x4683	",lowBound=0, cat= 'Integer')
x4684	=	p.LpVariable("	x4684	",lowBound=0, cat= 'Integer')
x4685	=	p.LpVariable("	x4685	",lowBound=0, cat= 'Integer')
x4686	=	p.LpVariable("	x4686	",lowBound=0, cat= 'Integer')
x4687	=	p.LpVariable("	x4687	",lowBound=0, cat= 'Integer')
x4688	=	p.LpVariable("	x4688	",lowBound=0, cat= 'Integer')
x4689	=	p.LpVariable("	x4689	",lowBound=0, cat= 'Integer')
x4690	=	p.LpVariable("	x4690	",lowBound=0, cat= 'Integer')
x4691	=	p.LpVariable("	x4691	",lowBound=0, cat= 'Integer')
x4692	=	p.LpVariable("	x4692	",lowBound=0, cat= 'Integer')
x4693	=	p.LpVariable("	x4693	",lowBound=0, cat= 'Integer')
x4694	=	p.LpVariable("	x4694	",lowBound=0, cat= 'Integer')
x4695	=	p.LpVariable("	x4695	",lowBound=0, cat= 'Integer')
x4696	=	p.LpVariable("	x4696	",lowBound=0, cat= 'Integer')
x4697	=	p.LpVariable("	x4697	",lowBound=0, cat= 'Integer')
x4698	=	p.LpVariable("	x4698	",lowBound=0, cat= 'Integer')
x4699	=	p.LpVariable("	x4699	",lowBound=0, cat= 'Integer')
x4700	=	p.LpVariable("	x4700	",lowBound=0, cat= 'Integer')
x4701	=	p.LpVariable("	x4701	",lowBound=0, cat= 'Integer')
x4702	=	p.LpVariable("	x4702	",lowBound=0, cat= 'Integer')
x4703	=	p.LpVariable("	x4703	",lowBound=0, cat= 'Integer')
x4704	=	p.LpVariable("	x4704	",lowBound=0, cat= 'Integer')
x4705	=	p.LpVariable("	x4705	",lowBound=0, cat= 'Integer')
x4706	=	p.LpVariable("	x4706	",lowBound=0, cat= 'Integer')
x4707	=	p.LpVariable("	x4707	",lowBound=0, cat= 'Integer')
x4708	=	p.LpVariable("	x4708	",lowBound=0, cat= 'Integer')
x4709	=	p.LpVariable("	x4709	",lowBound=0, cat= 'Integer')
x4710	=	p.LpVariable("	x4710	",lowBound=0, cat= 'Integer')
x4711	=	p.LpVariable("	x4711	",lowBound=0, cat= 'Integer')
x4712	=	p.LpVariable("	x4712	",lowBound=0, cat= 'Integer')
x4713	=	p.LpVariable("	x4713	",lowBound=0, cat= 'Integer')
x4714	=	p.LpVariable("	x4714	",lowBound=0, cat= 'Integer')
x4715	=	p.LpVariable("	x4715	",lowBound=0, cat= 'Integer')
x4716	=	p.LpVariable("	x4716	",lowBound=0, cat= 'Integer')
x4717	=	p.LpVariable("	x4717	",lowBound=0, cat= 'Integer')
x4718	=	p.LpVariable("	x4718	",lowBound=0, cat= 'Integer')
x4719	=	p.LpVariable("	x4719	",lowBound=0, cat= 'Integer')
x4720	=	p.LpVariable("	x4720	",lowBound=0, cat= 'Integer')
x4721	=	p.LpVariable("	x4721	",lowBound=0, cat= 'Integer')
x4722	=	p.LpVariable("	x4722	",lowBound=0, cat= 'Integer')
x4723	=	p.LpVariable("	x4723	",lowBound=0, cat= 'Integer')
x4724	=	p.LpVariable("	x4724	",lowBound=0, cat= 'Integer')
x4725	=	p.LpVariable("	x4725	",lowBound=0, cat= 'Integer')
x4726	=	p.LpVariable("	x4726	",lowBound=0, cat= 'Integer')
x4727	=	p.LpVariable("	x4727	",lowBound=0, cat= 'Integer')
x4728	=	p.LpVariable("	x4728	",lowBound=0, cat= 'Integer')
x4729	=	p.LpVariable("	x4729	",lowBound=0, cat= 'Integer')
x4730	=	p.LpVariable("	x4730	",lowBound=0, cat= 'Integer')
x4731	=	p.LpVariable("	x4731	",lowBound=0, cat= 'Integer')
x4732	=	p.LpVariable("	x4732	",lowBound=0, cat= 'Integer')
x4733	=	p.LpVariable("	x4733	",lowBound=0, cat= 'Integer')
x4734	=	p.LpVariable("	x4734	",lowBound=0, cat= 'Integer')
x4735	=	p.LpVariable("	x4735	",lowBound=0, cat= 'Integer')
x4736	=	p.LpVariable("	x4736	",lowBound=0, cat= 'Integer')
x4737	=	p.LpVariable("	x4737	",lowBound=0, cat= 'Integer')
x4738	=	p.LpVariable("	x4738	",lowBound=0, cat= 'Integer')
x4739	=	p.LpVariable("	x4739	",lowBound=0, cat= 'Integer')
x4740	=	p.LpVariable("	x4740	",lowBound=0, cat= 'Integer')
x4741	=	p.LpVariable("	x4741	",lowBound=0, cat= 'Integer')
x4742	=	p.LpVariable("	x4742	",lowBound=0, cat= 'Integer')
x4743	=	p.LpVariable("	x4743	",lowBound=0, cat= 'Integer')
x4744	=	p.LpVariable("	x4744	",lowBound=0, cat= 'Integer')
x4745	=	p.LpVariable("	x4745	",lowBound=0, cat= 'Integer')
x4746	=	p.LpVariable("	x4746	",lowBound=0, cat= 'Integer')
x4747	=	p.LpVariable("	x4747	",lowBound=0, cat= 'Integer')
x4748	=	p.LpVariable("	x4748	",lowBound=0, cat= 'Integer')
x4749	=	p.LpVariable("	x4749	",lowBound=0, cat= 'Integer')
x4750	=	p.LpVariable("	x4750	",lowBound=0, cat= 'Integer')
x4751	=	p.LpVariable("	x4751	",lowBound=0, cat= 'Integer')
x4752	=	p.LpVariable("	x4752	",lowBound=0, cat= 'Integer')
x4753	=	p.LpVariable("	x4753	",lowBound=0, cat= 'Integer')
x4754	=	p.LpVariable("	x4754	",lowBound=0, cat= 'Integer')
x4755	=	p.LpVariable("	x4755	",lowBound=0, cat= 'Integer')
x4756	=	p.LpVariable("	x4756	",lowBound=0, cat= 'Integer')
x4757	=	p.LpVariable("	x4757	",lowBound=0, cat= 'Integer')
x4758	=	p.LpVariable("	x4758	",lowBound=0, cat= 'Integer')
x4759	=	p.LpVariable("	x4759	",lowBound=0, cat= 'Integer')
x4760	=	p.LpVariable("	x4760	",lowBound=0, cat= 'Integer')
x4761	=	p.LpVariable("	x4761	",lowBound=0, cat= 'Integer')
x4762	=	p.LpVariable("	x4762	",lowBound=0, cat= 'Integer')
x4763	=	p.LpVariable("	x4763	",lowBound=0, cat= 'Integer')
x4764	=	p.LpVariable("	x4764	",lowBound=0, cat= 'Integer')
x4765	=	p.LpVariable("	x4765	",lowBound=0, cat= 'Integer')
x4766	=	p.LpVariable("	x4766	",lowBound=0, cat= 'Integer')
x4767	=	p.LpVariable("	x4767	",lowBound=0, cat= 'Integer')
x4768	=	p.LpVariable("	x4768	",lowBound=0, cat= 'Integer')
x4769	=	p.LpVariable("	x4769	",lowBound=0, cat= 'Integer')
x4770	=	p.LpVariable("	x4770	",lowBound=0, cat= 'Integer')
x4771	=	p.LpVariable("	x4771	",lowBound=0, cat= 'Integer')
x4772	=	p.LpVariable("	x4772	",lowBound=0, cat= 'Integer')
x4773	=	p.LpVariable("	x4773	",lowBound=0, cat= 'Integer')
x4774	=	p.LpVariable("	x4774	",lowBound=0, cat= 'Integer')
x4775	=	p.LpVariable("	x4775	",lowBound=0, cat= 'Integer')
x4776	=	p.LpVariable("	x4776	",lowBound=0, cat= 'Integer')
x4777	=	p.LpVariable("	x4777	",lowBound=0, cat= 'Integer')
x4778	=	p.LpVariable("	x4778	",lowBound=0, cat= 'Integer')
x4779	=	p.LpVariable("	x4779	",lowBound=0, cat= 'Integer')
x4780	=	p.LpVariable("	x4780	",lowBound=0, cat= 'Integer')
x4781	=	p.LpVariable("	x4781	",lowBound=0, cat= 'Integer')
x4782	=	p.LpVariable("	x4782	",lowBound=0, cat= 'Integer')
x4783	=	p.LpVariable("	x4783	",lowBound=0, cat= 'Integer')
x4784	=	p.LpVariable("	x4784	",lowBound=0, cat= 'Integer')
x4785	=	p.LpVariable("	x4785	",lowBound=0, cat= 'Integer')
x4786	=	p.LpVariable("	x4786	",lowBound=0, cat= 'Integer')
x4787	=	p.LpVariable("	x4787	",lowBound=0, cat= 'Integer')
x4788	=	p.LpVariable("	x4788	",lowBound=0, cat= 'Integer')
x4789	=	p.LpVariable("	x4789	",lowBound=0, cat= 'Integer')
x4790	=	p.LpVariable("	x4790	",lowBound=0, cat= 'Integer')
x4791	=	p.LpVariable("	x4791	",lowBound=0, cat= 'Integer')
x4792	=	p.LpVariable("	x4792	",lowBound=0, cat= 'Integer')
x4793	=	p.LpVariable("	x4793	",lowBound=0, cat= 'Integer')
x4794	=	p.LpVariable("	x4794	",lowBound=0, cat= 'Integer')
x4795	=	p.LpVariable("	x4795	",lowBound=0, cat= 'Integer')
x4796	=	p.LpVariable("	x4796	",lowBound=0, cat= 'Integer')
x4797	=	p.LpVariable("	x4797	",lowBound=0, cat= 'Integer')
x4798	=	p.LpVariable("	x4798	",lowBound=0, cat= 'Integer')
x4799	=	p.LpVariable("	x4799	",lowBound=0, cat= 'Integer')
x4800	=	p.LpVariable("	x4800	",lowBound=0, cat= 'Integer')
x4801	=	p.LpVariable("	x4801	",lowBound=0, cat= 'Integer')
x4802	=	p.LpVariable("	x4802	",lowBound=0, cat= 'Integer')
x4803	=	p.LpVariable("	x4803	",lowBound=0, cat= 'Integer')
x4804	=	p.LpVariable("	x4804	",lowBound=0, cat= 'Integer')
x4805	=	p.LpVariable("	x4805	",lowBound=0, cat= 'Integer')
x4806	=	p.LpVariable("	x4806	",lowBound=0, cat= 'Integer')
x4807	=	p.LpVariable("	x4807	",lowBound=0, cat= 'Integer')
x4808	=	p.LpVariable("	x4808	",lowBound=0, cat= 'Integer')
x4809	=	p.LpVariable("	x4809	",lowBound=0, cat= 'Integer')
x4810	=	p.LpVariable("	x4810	",lowBound=0, cat= 'Integer')
x4811	=	p.LpVariable("	x4811	",lowBound=0, cat= 'Integer')
x4812	=	p.LpVariable("	x4812	",lowBound=0, cat= 'Integer')
x4813	=	p.LpVariable("	x4813	",lowBound=0, cat= 'Integer')
x4814	=	p.LpVariable("	x4814	",lowBound=0, cat= 'Integer')
x4815	=	p.LpVariable("	x4815	",lowBound=0, cat= 'Integer')
x4816	=	p.LpVariable("	x4816	",lowBound=0, cat= 'Integer')
x4817	=	p.LpVariable("	x4817	",lowBound=0, cat= 'Integer')
x4818	=	p.LpVariable("	x4818	",lowBound=0, cat= 'Integer')
x4819	=	p.LpVariable("	x4819	",lowBound=0, cat= 'Integer')
x4820	=	p.LpVariable("	x4820	",lowBound=0, cat= 'Integer')
x4821	=	p.LpVariable("	x4821	",lowBound=0, cat= 'Integer')
x4822	=	p.LpVariable("	x4822	",lowBound=0, cat= 'Integer')
x4823	=	p.LpVariable("	x4823	",lowBound=0, cat= 'Integer')
x4824	=	p.LpVariable("	x4824	",lowBound=0, cat= 'Integer')
x4825	=	p.LpVariable("	x4825	",lowBound=0, cat= 'Integer')
x4826	=	p.LpVariable("	x4826	",lowBound=0, cat= 'Integer')
x4827	=	p.LpVariable("	x4827	",lowBound=0, cat= 'Integer')
x4828	=	p.LpVariable("	x4828	",lowBound=0, cat= 'Integer')
x4829	=	p.LpVariable("	x4829	",lowBound=0, cat= 'Integer')
x4830	=	p.LpVariable("	x4830	",lowBound=0, cat= 'Integer')
x4831	=	p.LpVariable("	x4831	",lowBound=0, cat= 'Integer')
x4832	=	p.LpVariable("	x4832	",lowBound=0, cat= 'Integer')
x4833	=	p.LpVariable("	x4833	",lowBound=0, cat= 'Integer')
x4834	=	p.LpVariable("	x4834	",lowBound=0, cat= 'Integer')
x4835	=	p.LpVariable("	x4835	",lowBound=0, cat= 'Integer')
x4836	=	p.LpVariable("	x4836	",lowBound=0, cat= 'Integer')
x4837	=	p.LpVariable("	x4837	",lowBound=0, cat= 'Integer')
x4838	=	p.LpVariable("	x4838	",lowBound=0, cat= 'Integer')
x4839	=	p.LpVariable("	x4839	",lowBound=0, cat= 'Integer')
x4840	=	p.LpVariable("	x4840	",lowBound=0, cat= 'Integer')
x4841	=	p.LpVariable("	x4841	",lowBound=0, cat= 'Integer')
x4842	=	p.LpVariable("	x4842	",lowBound=0, cat= 'Integer')
x4843	=	p.LpVariable("	x4843	",lowBound=0, cat= 'Integer')
x4844	=	p.LpVariable("	x4844	",lowBound=0, cat= 'Integer')
x4845	=	p.LpVariable("	x4845	",lowBound=0, cat= 'Integer')
x4846	=	p.LpVariable("	x4846	",lowBound=0, cat= 'Integer')
x4847	=	p.LpVariable("	x4847	",lowBound=0, cat= 'Integer')
x4848	=	p.LpVariable("	x4848	",lowBound=0, cat= 'Integer')
x4849	=	p.LpVariable("	x4849	",lowBound=0, cat= 'Integer')
x4850	=	p.LpVariable("	x4850	",lowBound=0, cat= 'Integer')
x4851	=	p.LpVariable("	x4851	",lowBound=0, cat= 'Integer')
x4852	=	p.LpVariable("	x4852	",lowBound=0, cat= 'Integer')
x4853	=	p.LpVariable("	x4853	",lowBound=0, cat= 'Integer')
x4854	=	p.LpVariable("	x4854	",lowBound=0, cat= 'Integer')
x4855	=	p.LpVariable("	x4855	",lowBound=0, cat= 'Integer')
x4856	=	p.LpVariable("	x4856	",lowBound=0, cat= 'Integer')
x4857	=	p.LpVariable("	x4857	",lowBound=0, cat= 'Integer')
x4858	=	p.LpVariable("	x4858	",lowBound=0, cat= 'Integer')
x4859	=	p.LpVariable("	x4859	",lowBound=0, cat= 'Integer')
x4860	=	p.LpVariable("	x4860	",lowBound=0, cat= 'Integer')
x4861	=	p.LpVariable("	x4861	",lowBound=0, cat= 'Integer')
x4862	=	p.LpVariable("	x4862	",lowBound=0, cat= 'Integer')
x4863	=	p.LpVariable("	x4863	",lowBound=0, cat= 'Integer')
x4864	=	p.LpVariable("	x4864	",lowBound=0, cat= 'Integer')
x4865	=	p.LpVariable("	x4865	",lowBound=0, cat= 'Integer')
x4866	=	p.LpVariable("	x4866	",lowBound=0, cat= 'Integer')
x4867	=	p.LpVariable("	x4867	",lowBound=0, cat= 'Integer')
x4868	=	p.LpVariable("	x4868	",lowBound=0, cat= 'Integer')
x4869	=	p.LpVariable("	x4869	",lowBound=0, cat= 'Integer')
x4870	=	p.LpVariable("	x4870	",lowBound=0, cat= 'Integer')
x4871	=	p.LpVariable("	x4871	",lowBound=0, cat= 'Integer')
x4872	=	p.LpVariable("	x4872	",lowBound=0, cat= 'Integer')
x4873	=	p.LpVariable("	x4873	",lowBound=0, cat= 'Integer')
x4874	=	p.LpVariable("	x4874	",lowBound=0, cat= 'Integer')
x4875	=	p.LpVariable("	x4875	",lowBound=0, cat= 'Integer')
x4876	=	p.LpVariable("	x4876	",lowBound=0, cat= 'Integer')
x4877	=	p.LpVariable("	x4877	",lowBound=0, cat= 'Integer')
x4878	=	p.LpVariable("	x4878	",lowBound=0, cat= 'Integer')
x4879	=	p.LpVariable("	x4879	",lowBound=0, cat= 'Integer')
x4880	=	p.LpVariable("	x4880	",lowBound=0, cat= 'Integer')
x4881	=	p.LpVariable("	x4881	",lowBound=0, cat= 'Integer')
x4882	=	p.LpVariable("	x4882	",lowBound=0, cat= 'Integer')
x4883	=	p.LpVariable("	x4883	",lowBound=0, cat= 'Integer')
x4884	=	p.LpVariable("	x4884	",lowBound=0, cat= 'Integer')
x4885	=	p.LpVariable("	x4885	",lowBound=0, cat= 'Integer')
x4886	=	p.LpVariable("	x4886	",lowBound=0, cat= 'Integer')
x4887	=	p.LpVariable("	x4887	",lowBound=0, cat= 'Integer')
x4888	=	p.LpVariable("	x4888	",lowBound=0, cat= 'Integer')
x4889	=	p.LpVariable("	x4889	",lowBound=0, cat= 'Integer')
x4890	=	p.LpVariable("	x4890	",lowBound=0, cat= 'Integer')
x4891	=	p.LpVariable("	x4891	",lowBound=0, cat= 'Integer')
x4892	=	p.LpVariable("	x4892	",lowBound=0, cat= 'Integer')
x4893	=	p.LpVariable("	x4893	",lowBound=0, cat= 'Integer')
x4894	=	p.LpVariable("	x4894	",lowBound=0, cat= 'Integer')
x4895	=	p.LpVariable("	x4895	",lowBound=0, cat= 'Integer')
x4896	=	p.LpVariable("	x4896	",lowBound=0, cat= 'Integer')
x4897	=	p.LpVariable("	x4897	",lowBound=0, cat= 'Integer')
x4898	=	p.LpVariable("	x4898	",lowBound=0, cat= 'Integer')
x4899	=	p.LpVariable("	x4899	",lowBound=0, cat= 'Integer')
x4900	=	p.LpVariable("	x4900	",lowBound=0, cat= 'Integer')
x4901	=	p.LpVariable("	x4901	",lowBound=0, cat= 'Integer')
x4902	=	p.LpVariable("	x4902	",lowBound=0, cat= 'Integer')
x4903	=	p.LpVariable("	x4903	",lowBound=0, cat= 'Integer')
x4904	=	p.LpVariable("	x4904	",lowBound=0, cat= 'Integer')
x4905	=	p.LpVariable("	x4905	",lowBound=0, cat= 'Integer')
x4906	=	p.LpVariable("	x4906	",lowBound=0, cat= 'Integer')
x4907	=	p.LpVariable("	x4907	",lowBound=0, cat= 'Integer')
x4908	=	p.LpVariable("	x4908	",lowBound=0, cat= 'Integer')
x4909	=	p.LpVariable("	x4909	",lowBound=0, cat= 'Integer')
x4910	=	p.LpVariable("	x4910	",lowBound=0, cat= 'Integer')
x4911	=	p.LpVariable("	x4911	",lowBound=0, cat= 'Integer')
x4912	=	p.LpVariable("	x4912	",lowBound=0, cat= 'Integer')
x4913	=	p.LpVariable("	x4913	",lowBound=0, cat= 'Integer')
x4914	=	p.LpVariable("	x4914	",lowBound=0, cat= 'Integer')
x4915	=	p.LpVariable("	x4915	",lowBound=0, cat= 'Integer')
x4916	=	p.LpVariable("	x4916	",lowBound=0, cat= 'Integer')
x4917	=	p.LpVariable("	x4917	",lowBound=0, cat= 'Integer')
x4918	=	p.LpVariable("	x4918	",lowBound=0, cat= 'Integer')
x4919	=	p.LpVariable("	x4919	",lowBound=0, cat= 'Integer')
x4920	=	p.LpVariable("	x4920	",lowBound=0, cat= 'Integer')
x4921	=	p.LpVariable("	x4921	",lowBound=0, cat= 'Integer')
x4922	=	p.LpVariable("	x4922	",lowBound=0, cat= 'Integer')
x4923	=	p.LpVariable("	x4923	",lowBound=0, cat= 'Integer')
x4924	=	p.LpVariable("	x4924	",lowBound=0, cat= 'Integer')
x4925	=	p.LpVariable("	x4925	",lowBound=0, cat= 'Integer')
x4926	=	p.LpVariable("	x4926	",lowBound=0, cat= 'Integer')
x4927	=	p.LpVariable("	x4927	",lowBound=0, cat= 'Integer')
x4928	=	p.LpVariable("	x4928	",lowBound=0, cat= 'Integer')
x4929	=	p.LpVariable("	x4929	",lowBound=0, cat= 'Integer')
x4930	=	p.LpVariable("	x4930	",lowBound=0, cat= 'Integer')
x4931	=	p.LpVariable("	x4931	",lowBound=0, cat= 'Integer')
x4932	=	p.LpVariable("	x4932	",lowBound=0, cat= 'Integer')
x4933	=	p.LpVariable("	x4933	",lowBound=0, cat= 'Integer')
x4934	=	p.LpVariable("	x4934	",lowBound=0, cat= 'Integer')
x4935	=	p.LpVariable("	x4935	",lowBound=0, cat= 'Integer')
x4936	=	p.LpVariable("	x4936	",lowBound=0, cat= 'Integer')
x4937	=	p.LpVariable("	x4937	",lowBound=0, cat= 'Integer')
x4938	=	p.LpVariable("	x4938	",lowBound=0, cat= 'Integer')
x4939	=	p.LpVariable("	x4939	",lowBound=0, cat= 'Integer')
x4940	=	p.LpVariable("	x4940	",lowBound=0, cat= 'Integer')
x4941	=	p.LpVariable("	x4941	",lowBound=0, cat= 'Integer')
x4942	=	p.LpVariable("	x4942	",lowBound=0, cat= 'Integer')
x4943	=	p.LpVariable("	x4943	",lowBound=0, cat= 'Integer')
x4944	=	p.LpVariable("	x4944	",lowBound=0, cat= 'Integer')
x4945	=	p.LpVariable("	x4945	",lowBound=0, cat= 'Integer')
x4946	=	p.LpVariable("	x4946	",lowBound=0, cat= 'Integer')
x4947	=	p.LpVariable("	x4947	",lowBound=0, cat= 'Integer')
x4948	=	p.LpVariable("	x4948	",lowBound=0, cat= 'Integer')
x4949	=	p.LpVariable("	x4949	",lowBound=0, cat= 'Integer')
x4950	=	p.LpVariable("	x4950	",lowBound=0, cat= 'Integer')
x4951	=	p.LpVariable("	x4951	",lowBound=0, cat= 'Integer')
x4952	=	p.LpVariable("	x4952	",lowBound=0, cat= 'Integer')
x4953	=	p.LpVariable("	x4953	",lowBound=0, cat= 'Integer')
x4954	=	p.LpVariable("	x4954	",lowBound=0, cat= 'Integer')
x4955	=	p.LpVariable("	x4955	",lowBound=0, cat= 'Integer')
x4956	=	p.LpVariable("	x4956	",lowBound=0, cat= 'Integer')
x4957	=	p.LpVariable("	x4957	",lowBound=0, cat= 'Integer')
x4958	=	p.LpVariable("	x4958	",lowBound=0, cat= 'Integer')
x4959	=	p.LpVariable("	x4959	",lowBound=0, cat= 'Integer')
x4960	=	p.LpVariable("	x4960	",lowBound=0, cat= 'Integer')
x4961	=	p.LpVariable("	x4961	",lowBound=0, cat= 'Integer')
x4962	=	p.LpVariable("	x4962	",lowBound=0, cat= 'Integer')
x4963	=	p.LpVariable("	x4963	",lowBound=0, cat= 'Integer')
x4964	=	p.LpVariable("	x4964	",lowBound=0, cat= 'Integer')
x4965	=	p.LpVariable("	x4965	",lowBound=0, cat= 'Integer')
x4966	=	p.LpVariable("	x4966	",lowBound=0, cat= 'Integer')
x4967	=	p.LpVariable("	x4967	",lowBound=0, cat= 'Integer')
x4968	=	p.LpVariable("	x4968	",lowBound=0, cat= 'Integer')
x4969	=	p.LpVariable("	x4969	",lowBound=0, cat= 'Integer')
x4970	=	p.LpVariable("	x4970	",lowBound=0, cat= 'Integer')
x4971	=	p.LpVariable("	x4971	",lowBound=0, cat= 'Integer')
x4972	=	p.LpVariable("	x4972	",lowBound=0, cat= 'Integer')
x4973	=	p.LpVariable("	x4973	",lowBound=0, cat= 'Integer')
x4974	=	p.LpVariable("	x4974	",lowBound=0, cat= 'Integer')
x4975	=	p.LpVariable("	x4975	",lowBound=0, cat= 'Integer')
x4976	=	p.LpVariable("	x4976	",lowBound=0, cat= 'Integer')
x4977	=	p.LpVariable("	x4977	",lowBound=0, cat= 'Integer')
x4978	=	p.LpVariable("	x4978	",lowBound=0, cat= 'Integer')
x4979	=	p.LpVariable("	x4979	",lowBound=0, cat= 'Integer')
x4980	=	p.LpVariable("	x4980	",lowBound=0, cat= 'Integer')
x4981	=	p.LpVariable("	x4981	",lowBound=0, cat= 'Integer')
x4982	=	p.LpVariable("	x4982	",lowBound=0, cat= 'Integer')
x4983	=	p.LpVariable("	x4983	",lowBound=0, cat= 'Integer')
x4984	=	p.LpVariable("	x4984	",lowBound=0, cat= 'Integer')
x4985	=	p.LpVariable("	x4985	",lowBound=0, cat= 'Integer')
x4986	=	p.LpVariable("	x4986	",lowBound=0, cat= 'Integer')
x4987	=	p.LpVariable("	x4987	",lowBound=0, cat= 'Integer')
x4988	=	p.LpVariable("	x4988	",lowBound=0, cat= 'Integer')
x4989	=	p.LpVariable("	x4989	",lowBound=0, cat= 'Integer')
x4990	=	p.LpVariable("	x4990	",lowBound=0, cat= 'Integer')
x4991	=	p.LpVariable("	x4991	",lowBound=0, cat= 'Integer')
x4992	=	p.LpVariable("	x4992	",lowBound=0, cat= 'Integer')
x4993	=	p.LpVariable("	x4993	",lowBound=0, cat= 'Integer')
x4994	=	p.LpVariable("	x4994	",lowBound=0, cat= 'Integer')
x4995	=	p.LpVariable("	x4995	",lowBound=0, cat= 'Integer')
x4996	=	p.LpVariable("	x4996	",lowBound=0, cat= 'Integer')
x4997	=	p.LpVariable("	x4997	",lowBound=0, cat= 'Integer')
x4998	=	p.LpVariable("	x4998	",lowBound=0, cat= 'Integer')
x4999	=	p.LpVariable("	x4999	",lowBound=0, cat= 'Integer')
x5000	=	p.LpVariable("	x5000	",lowBound=0, cat= 'Integer')
x5001	=	p.LpVariable("	x5001	",lowBound=0, cat= 'Integer')
x5002	=	p.LpVariable("	x5002	",lowBound=0, cat= 'Integer')
x5003	=	p.LpVariable("	x5003	",lowBound=0, cat= 'Integer')
x5004	=	p.LpVariable("	x5004	",lowBound=0, cat= 'Integer')
x5005	=	p.LpVariable("	x5005	",lowBound=0, cat= 'Integer')
x5006	=	p.LpVariable("	x5006	",lowBound=0, cat= 'Integer')
x5007	=	p.LpVariable("	x5007	",lowBound=0, cat= 'Integer')
x5008	=	p.LpVariable("	x5008	",lowBound=0, cat= 'Integer')
x5009	=	p.LpVariable("	x5009	",lowBound=0, cat= 'Integer')
x5010	=	p.LpVariable("	x5010	",lowBound=0, cat= 'Integer')
x5011	=	p.LpVariable("	x5011	",lowBound=0, cat= 'Integer')
x5012	=	p.LpVariable("	x5012	",lowBound=0, cat= 'Integer')
x5013	=	p.LpVariable("	x5013	",lowBound=0, cat= 'Integer')
x5014	=	p.LpVariable("	x5014	",lowBound=0, cat= 'Integer')
x5015	=	p.LpVariable("	x5015	",lowBound=0, cat= 'Integer')
x5016	=	p.LpVariable("	x5016	",lowBound=0, cat= 'Integer')
x5017	=	p.LpVariable("	x5017	",lowBound=0, cat= 'Integer')
x5018	=	p.LpVariable("	x5018	",lowBound=0, cat= 'Integer')
x5019	=	p.LpVariable("	x5019	",lowBound=0, cat= 'Integer')
x5020	=	p.LpVariable("	x5020	",lowBound=0, cat= 'Integer')
x5021	=	p.LpVariable("	x5021	",lowBound=0, cat= 'Integer')
x5022	=	p.LpVariable("	x5022	",lowBound=0, cat= 'Integer')
x5023	=	p.LpVariable("	x5023	",lowBound=0, cat= 'Integer')
x5024	=	p.LpVariable("	x5024	",lowBound=0, cat= 'Integer')
x5025	=	p.LpVariable("	x5025	",lowBound=0, cat= 'Integer')
x5026	=	p.LpVariable("	x5026	",lowBound=0, cat= 'Integer')
x5027	=	p.LpVariable("	x5027	",lowBound=0, cat= 'Integer')
x5028	=	p.LpVariable("	x5028	",lowBound=0, cat= 'Integer')
x5029	=	p.LpVariable("	x5029	",lowBound=0, cat= 'Integer')
x5030	=	p.LpVariable("	x5030	",lowBound=0, cat= 'Integer')
x5031	=	p.LpVariable("	x5031	",lowBound=0, cat= 'Integer')
x5032	=	p.LpVariable("	x5032	",lowBound=0, cat= 'Integer')
x5033	=	p.LpVariable("	x5033	",lowBound=0, cat= 'Integer')
x5034	=	p.LpVariable("	x5034	",lowBound=0, cat= 'Integer')
x5035	=	p.LpVariable("	x5035	",lowBound=0, cat= 'Integer')
x5036	=	p.LpVariable("	x5036	",lowBound=0, cat= 'Integer')
x5037	=	p.LpVariable("	x5037	",lowBound=0, cat= 'Integer')
x5038	=	p.LpVariable("	x5038	",lowBound=0, cat= 'Integer')
x5039	=	p.LpVariable("	x5039	",lowBound=0, cat= 'Integer')
x5040	=	p.LpVariable("	x5040	",lowBound=0, cat= 'Integer')
x5041	=	p.LpVariable("	x5041	",lowBound=0, cat= 'Integer')
x5042	=	p.LpVariable("	x5042	",lowBound=0, cat= 'Integer')
x5043	=	p.LpVariable("	x5043	",lowBound=0, cat= 'Integer')
x5044	=	p.LpVariable("	x5044	",lowBound=0, cat= 'Integer')
x5045	=	p.LpVariable("	x5045	",lowBound=0, cat= 'Integer')
x5046	=	p.LpVariable("	x5046	",lowBound=0, cat= 'Integer')
x5047	=	p.LpVariable("	x5047	",lowBound=0, cat= 'Integer')
x5048	=	p.LpVariable("	x5048	",lowBound=0, cat= 'Integer')
x5049	=	p.LpVariable("	x5049	",lowBound=0, cat= 'Integer')
x5050	=	p.LpVariable("	x5050	",lowBound=0, cat= 'Integer')
x5051	=	p.LpVariable("	x5051	",lowBound=0, cat= 'Integer')
x5052	=	p.LpVariable("	x5052	",lowBound=0, cat= 'Integer')
x5053	=	p.LpVariable("	x5053	",lowBound=0, cat= 'Integer')
x5054	=	p.LpVariable("	x5054	",lowBound=0, cat= 'Integer')
x5055	=	p.LpVariable("	x5055	",lowBound=0, cat= 'Integer')
x5056	=	p.LpVariable("	x5056	",lowBound=0, cat= 'Integer')
x5057	=	p.LpVariable("	x5057	",lowBound=0, cat= 'Integer')
x5058	=	p.LpVariable("	x5058	",lowBound=0, cat= 'Integer')
x5059	=	p.LpVariable("	x5059	",lowBound=0, cat= 'Integer')
x5060	=	p.LpVariable("	x5060	",lowBound=0, cat= 'Integer')
x5061	=	p.LpVariable("	x5061	",lowBound=0, cat= 'Integer')
x5062	=	p.LpVariable("	x5062	",lowBound=0, cat= 'Integer')
x5063	=	p.LpVariable("	x5063	",lowBound=0, cat= 'Integer')
x5064	=	p.LpVariable("	x5064	",lowBound=0, cat= 'Integer')
x5065	=	p.LpVariable("	x5065	",lowBound=0, cat= 'Integer')
x5066	=	p.LpVariable("	x5066	",lowBound=0, cat= 'Integer')
x5067	=	p.LpVariable("	x5067	",lowBound=0, cat= 'Integer')
x5068	=	p.LpVariable("	x5068	",lowBound=0, cat= 'Integer')
x5069	=	p.LpVariable("	x5069	",lowBound=0, cat= 'Integer')
x5070	=	p.LpVariable("	x5070	",lowBound=0, cat= 'Integer')
x5071	=	p.LpVariable("	x5071	",lowBound=0, cat= 'Integer')
x5072	=	p.LpVariable("	x5072	",lowBound=0, cat= 'Integer')
x5073	=	p.LpVariable("	x5073	",lowBound=0, cat= 'Integer')
x5074	=	p.LpVariable("	x5074	",lowBound=0, cat= 'Integer')
x5075	=	p.LpVariable("	x5075	",lowBound=0, cat= 'Integer')
x5076	=	p.LpVariable("	x5076	",lowBound=0, cat= 'Integer')
x5077	=	p.LpVariable("	x5077	",lowBound=0, cat= 'Integer')
x5078	=	p.LpVariable("	x5078	",lowBound=0, cat= 'Integer')
x5079	=	p.LpVariable("	x5079	",lowBound=0, cat= 'Integer')
x5080	=	p.LpVariable("	x5080	",lowBound=0, cat= 'Integer')
x5081	=	p.LpVariable("	x5081	",lowBound=0, cat= 'Integer')
x5082	=	p.LpVariable("	x5082	",lowBound=0, cat= 'Integer')
x5083	=	p.LpVariable("	x5083	",lowBound=0, cat= 'Integer')
x5084	=	p.LpVariable("	x5084	",lowBound=0, cat= 'Integer')
x5085	=	p.LpVariable("	x5085	",lowBound=0, cat= 'Integer')
x5086	=	p.LpVariable("	x5086	",lowBound=0, cat= 'Integer')
x5087	=	p.LpVariable("	x5087	",lowBound=0, cat= 'Integer')
x5088	=	p.LpVariable("	x5088	",lowBound=0, cat= 'Integer')
x5089	=	p.LpVariable("	x5089	",lowBound=0, cat= 'Integer')
x5090	=	p.LpVariable("	x5090	",lowBound=0, cat= 'Integer')
x5091	=	p.LpVariable("	x5091	",lowBound=0, cat= 'Integer')
x5092	=	p.LpVariable("	x5092	",lowBound=0, cat= 'Integer')
x5093	=	p.LpVariable("	x5093	",lowBound=0, cat= 'Integer')
x5094	=	p.LpVariable("	x5094	",lowBound=0, cat= 'Integer')
x5095	=	p.LpVariable("	x5095	",lowBound=0, cat= 'Integer')
x5096	=	p.LpVariable("	x5096	",lowBound=0, cat= 'Integer')
x5097	=	p.LpVariable("	x5097	",lowBound=0, cat= 'Integer')
x5098	=	p.LpVariable("	x5098	",lowBound=0, cat= 'Integer')
x5099	=	p.LpVariable("	x5099	",lowBound=0, cat= 'Integer')
x5100	=	p.LpVariable("	x5100	",lowBound=0, cat= 'Integer')
x5101	=	p.LpVariable("	x5101	",lowBound=0, cat= 'Integer')
x5102	=	p.LpVariable("	x5102	",lowBound=0, cat= 'Integer')
x5103	=	p.LpVariable("	x5103	",lowBound=0, cat= 'Integer')
x5104	=	p.LpVariable("	x5104	",lowBound=0, cat= 'Integer')
x5105	=	p.LpVariable("	x5105	",lowBound=0, cat= 'Integer')
x5106	=	p.LpVariable("	x5106	",lowBound=0, cat= 'Integer')
x5107	=	p.LpVariable("	x5107	",lowBound=0, cat= 'Integer')
x5108	=	p.LpVariable("	x5108	",lowBound=0, cat= 'Integer')
x5109	=	p.LpVariable("	x5109	",lowBound=0, cat= 'Integer')
x5110	=	p.LpVariable("	x5110	",lowBound=0, cat= 'Integer')
x5111	=	p.LpVariable("	x5111	",lowBound=0, cat= 'Integer')
x5112	=	p.LpVariable("	x5112	",lowBound=0, cat= 'Integer')
x5113	=	p.LpVariable("	x5113	",lowBound=0, cat= 'Integer')
x5114	=	p.LpVariable("	x5114	",lowBound=0, cat= 'Integer')
x5115	=	p.LpVariable("	x5115	",lowBound=0, cat= 'Integer')
x5116	=	p.LpVariable("	x5116	",lowBound=0, cat= 'Integer')
x5117	=	p.LpVariable("	x5117	",lowBound=0, cat= 'Integer')
x5118	=	p.LpVariable("	x5118	",lowBound=0, cat= 'Integer')
x5119	=	p.LpVariable("	x5119	",lowBound=0, cat= 'Integer')
x5120	=	p.LpVariable("	x5120	",lowBound=0, cat= 'Integer')
x5121	=	p.LpVariable("	x5121	",lowBound=0, cat= 'Integer')
x5122	=	p.LpVariable("	x5122	",lowBound=0, cat= 'Integer')
x5123	=	p.LpVariable("	x5123	",lowBound=0, cat= 'Integer')
x5124	=	p.LpVariable("	x5124	",lowBound=0, cat= 'Integer')
x5125	=	p.LpVariable("	x5125	",lowBound=0, cat= 'Integer')
x5126	=	p.LpVariable("	x5126	",lowBound=0, cat= 'Integer')
x5127	=	p.LpVariable("	x5127	",lowBound=0, cat= 'Integer')
x5128	=	p.LpVariable("	x5128	",lowBound=0, cat= 'Integer')
x5129	=	p.LpVariable("	x5129	",lowBound=0, cat= 'Integer')
x5130	=	p.LpVariable("	x5130	",lowBound=0, cat= 'Integer')
x5131	=	p.LpVariable("	x5131	",lowBound=0, cat= 'Integer')
x5132	=	p.LpVariable("	x5132	",lowBound=0, cat= 'Integer')
x5133	=	p.LpVariable("	x5133	",lowBound=0, cat= 'Integer')
x5134	=	p.LpVariable("	x5134	",lowBound=0, cat= 'Integer')
x5135	=	p.LpVariable("	x5135	",lowBound=0, cat= 'Integer')
x5136	=	p.LpVariable("	x5136	",lowBound=0, cat= 'Integer')
x5137	=	p.LpVariable("	x5137	",lowBound=0, cat= 'Integer')
x5138	=	p.LpVariable("	x5138	",lowBound=0, cat= 'Integer')
x5139	=	p.LpVariable("	x5139	",lowBound=0, cat= 'Integer')
x5140	=	p.LpVariable("	x5140	",lowBound=0, cat= 'Integer')
x5141	=	p.LpVariable("	x5141	",lowBound=0, cat= 'Integer')
x5142	=	p.LpVariable("	x5142	",lowBound=0, cat= 'Integer')
x5143	=	p.LpVariable("	x5143	",lowBound=0, cat= 'Integer')
x5144	=	p.LpVariable("	x5144	",lowBound=0, cat= 'Integer')
x5145	=	p.LpVariable("	x5145	",lowBound=0, cat= 'Integer')
x5146	=	p.LpVariable("	x5146	",lowBound=0, cat= 'Integer')
x5147	=	p.LpVariable("	x5147	",lowBound=0, cat= 'Integer')
x5148	=	p.LpVariable("	x5148	",lowBound=0, cat= 'Integer')
x5149	=	p.LpVariable("	x5149	",lowBound=0, cat= 'Integer')
x5150	=	p.LpVariable("	x5150	",lowBound=0, cat= 'Integer')
x5151	=	p.LpVariable("	x5151	",lowBound=0, cat= 'Integer')
x5152	=	p.LpVariable("	x5152	",lowBound=0, cat= 'Integer')
x5153	=	p.LpVariable("	x5153	",lowBound=0, cat= 'Integer')
x5154	=	p.LpVariable("	x5154	",lowBound=0, cat= 'Integer')
x5155	=	p.LpVariable("	x5155	",lowBound=0, cat= 'Integer')
x5156	=	p.LpVariable("	x5156	",lowBound=0, cat= 'Integer')
x5157	=	p.LpVariable("	x5157	",lowBound=0, cat= 'Integer')
x5158	=	p.LpVariable("	x5158	",lowBound=0, cat= 'Integer')
x5159	=	p.LpVariable("	x5159	",lowBound=0, cat= 'Integer')
x5160	=	p.LpVariable("	x5160	",lowBound=0, cat= 'Integer')
x5161	=	p.LpVariable("	x5161	",lowBound=0, cat= 'Integer')
x5162	=	p.LpVariable("	x5162	",lowBound=0, cat= 'Integer')
x5163	=	p.LpVariable("	x5163	",lowBound=0, cat= 'Integer')
x5164	=	p.LpVariable("	x5164	",lowBound=0, cat= 'Integer')
x5165	=	p.LpVariable("	x5165	",lowBound=0, cat= 'Integer')
x5166	=	p.LpVariable("	x5166	",lowBound=0, cat= 'Integer')
x5167	=	p.LpVariable("	x5167	",lowBound=0, cat= 'Integer')
x5168	=	p.LpVariable("	x5168	",lowBound=0, cat= 'Integer')
x5169	=	p.LpVariable("	x5169	",lowBound=0, cat= 'Integer')
x5170	=	p.LpVariable("	x5170	",lowBound=0, cat= 'Integer')
x5171	=	p.LpVariable("	x5171	",lowBound=0, cat= 'Integer')
x5172	=	p.LpVariable("	x5172	",lowBound=0, cat= 'Integer')
x5173	=	p.LpVariable("	x5173	",lowBound=0, cat= 'Integer')
x5174	=	p.LpVariable("	x5174	",lowBound=0, cat= 'Integer')
x5175	=	p.LpVariable("	x5175	",lowBound=0, cat= 'Integer')
x5176	=	p.LpVariable("	x5176	",lowBound=0, cat= 'Integer')
x5177	=	p.LpVariable("	x5177	",lowBound=0, cat= 'Integer')
x5178	=	p.LpVariable("	x5178	",lowBound=0, cat= 'Integer')
x5179	=	p.LpVariable("	x5179	",lowBound=0, cat= 'Integer')
x5180	=	p.LpVariable("	x5180	",lowBound=0, cat= 'Integer')
x5181	=	p.LpVariable("	x5181	",lowBound=0, cat= 'Integer')
x5182	=	p.LpVariable("	x5182	",lowBound=0, cat= 'Integer')
x5183	=	p.LpVariable("	x5183	",lowBound=0, cat= 'Integer')
x5184	=	p.LpVariable("	x5184	",lowBound=0, cat= 'Integer')
x5185	=	p.LpVariable("	x5185	",lowBound=0, cat= 'Integer')
x5186	=	p.LpVariable("	x5186	",lowBound=0, cat= 'Integer')
x5187	=	p.LpVariable("	x5187	",lowBound=0, cat= 'Integer')
x5188	=	p.LpVariable("	x5188	",lowBound=0, cat= 'Integer')
x5189	=	p.LpVariable("	x5189	",lowBound=0, cat= 'Integer')
x5190	=	p.LpVariable("	x5190	",lowBound=0, cat= 'Integer')
x5191	=	p.LpVariable("	x5191	",lowBound=0, cat= 'Integer')
x5192	=	p.LpVariable("	x5192	",lowBound=0, cat= 'Integer')
x5193	=	p.LpVariable("	x5193	",lowBound=0, cat= 'Integer')
x5194	=	p.LpVariable("	x5194	",lowBound=0, cat= 'Integer')
x5195	=	p.LpVariable("	x5195	",lowBound=0, cat= 'Integer')
x5196	=	p.LpVariable("	x5196	",lowBound=0, cat= 'Integer')
x5197	=	p.LpVariable("	x5197	",lowBound=0, cat= 'Integer')
x5198	=	p.LpVariable("	x5198	",lowBound=0, cat= 'Integer')
x5199	=	p.LpVariable("	x5199	",lowBound=0, cat= 'Integer')
x5200	=	p.LpVariable("	x5200	",lowBound=0, cat= 'Integer')
x5201	=	p.LpVariable("	x5201	",lowBound=0, cat= 'Integer')
x5202	=	p.LpVariable("	x5202	",lowBound=0, cat= 'Integer')
x5203	=	p.LpVariable("	x5203	",lowBound=0, cat= 'Integer')
x5204	=	p.LpVariable("	x5204	",lowBound=0, cat= 'Integer')
x5205	=	p.LpVariable("	x5205	",lowBound=0, cat= 'Integer')
x5206	=	p.LpVariable("	x5206	",lowBound=0, cat= 'Integer')
x5207	=	p.LpVariable("	x5207	",lowBound=0, cat= 'Integer')
x5208	=	p.LpVariable("	x5208	",lowBound=0, cat= 'Integer')
x5209	=	p.LpVariable("	x5209	",lowBound=0, cat= 'Integer')
x5210	=	p.LpVariable("	x5210	",lowBound=0, cat= 'Integer')
x5211	=	p.LpVariable("	x5211	",lowBound=0, cat= 'Integer')
x5212	=	p.LpVariable("	x5212	",lowBound=0, cat= 'Integer')
x5213	=	p.LpVariable("	x5213	",lowBound=0, cat= 'Integer')
x5214	=	p.LpVariable("	x5214	",lowBound=0, cat= 'Integer')
x5215	=	p.LpVariable("	x5215	",lowBound=0, cat= 'Integer')
x5216	=	p.LpVariable("	x5216	",lowBound=0, cat= 'Integer')
x5217	=	p.LpVariable("	x5217	",lowBound=0, cat= 'Integer')
x5218	=	p.LpVariable("	x5218	",lowBound=0, cat= 'Integer')
x5219	=	p.LpVariable("	x5219	",lowBound=0, cat= 'Integer')
x5220	=	p.LpVariable("	x5220	",lowBound=0, cat= 'Integer')
x5221	=	p.LpVariable("	x5221	",lowBound=0, cat= 'Integer')
x5222	=	p.LpVariable("	x5222	",lowBound=0, cat= 'Integer')
x5223	=	p.LpVariable("	x5223	",lowBound=0, cat= 'Integer')
x5224	=	p.LpVariable("	x5224	",lowBound=0, cat= 'Integer')
x5225	=	p.LpVariable("	x5225	",lowBound=0, cat= 'Integer')
x5226	=	p.LpVariable("	x5226	",lowBound=0, cat= 'Integer')
x5227	=	p.LpVariable("	x5227	",lowBound=0, cat= 'Integer')
x5228	=	p.LpVariable("	x5228	",lowBound=0, cat= 'Integer')
x5229	=	p.LpVariable("	x5229	",lowBound=0, cat= 'Integer')
x5230	=	p.LpVariable("	x5230	",lowBound=0, cat= 'Integer')
x5231	=	p.LpVariable("	x5231	",lowBound=0, cat= 'Integer')
x5232	=	p.LpVariable("	x5232	",lowBound=0, cat= 'Integer')
x5233	=	p.LpVariable("	x5233	",lowBound=0, cat= 'Integer')
x5234	=	p.LpVariable("	x5234	",lowBound=0, cat= 'Integer')
x5235	=	p.LpVariable("	x5235	",lowBound=0, cat= 'Integer')
x5236	=	p.LpVariable("	x5236	",lowBound=0, cat= 'Integer')
x5237	=	p.LpVariable("	x5237	",lowBound=0, cat= 'Integer')
x5238	=	p.LpVariable("	x5238	",lowBound=0, cat= 'Integer')
x5239	=	p.LpVariable("	x5239	",lowBound=0, cat= 'Integer')
x5240	=	p.LpVariable("	x5240	",lowBound=0, cat= 'Integer')
x5241	=	p.LpVariable("	x5241	",lowBound=0, cat= 'Integer')
x5242	=	p.LpVariable("	x5242	",lowBound=0, cat= 'Integer')
x5243	=	p.LpVariable("	x5243	",lowBound=0, cat= 'Integer')
x5244	=	p.LpVariable("	x5244	",lowBound=0, cat= 'Integer')
x5245	=	p.LpVariable("	x5245	",lowBound=0, cat= 'Integer')
x5246	=	p.LpVariable("	x5246	",lowBound=0, cat= 'Integer')
x5247	=	p.LpVariable("	x5247	",lowBound=0, cat= 'Integer')
x5248	=	p.LpVariable("	x5248	",lowBound=0, cat= 'Integer')
x5249	=	p.LpVariable("	x5249	",lowBound=0, cat= 'Integer')
x5250	=	p.LpVariable("	x5250	",lowBound=0, cat= 'Integer')
x5251	=	p.LpVariable("	x5251	",lowBound=0, cat= 'Integer')
x5252	=	p.LpVariable("	x5252	",lowBound=0, cat= 'Integer')
x5253	=	p.LpVariable("	x5253	",lowBound=0, cat= 'Integer')
x5254	=	p.LpVariable("	x5254	",lowBound=0, cat= 'Integer')
x5255	=	p.LpVariable("	x5255	",lowBound=0, cat= 'Integer')
x5256	=	p.LpVariable("	x5256	",lowBound=0, cat= 'Integer')
x5257	=	p.LpVariable("	x5257	",lowBound=0, cat= 'Integer')
x5258	=	p.LpVariable("	x5258	",lowBound=0, cat= 'Integer')
x5259	=	p.LpVariable("	x5259	",lowBound=0, cat= 'Integer')
x5260	=	p.LpVariable("	x5260	",lowBound=0, cat= 'Integer')
x5261	=	p.LpVariable("	x5261	",lowBound=0, cat= 'Integer')
x5262	=	p.LpVariable("	x5262	",lowBound=0, cat= 'Integer')
x5263	=	p.LpVariable("	x5263	",lowBound=0, cat= 'Integer')
x5264	=	p.LpVariable("	x5264	",lowBound=0, cat= 'Integer')
x5265	=	p.LpVariable("	x5265	",lowBound=0, cat= 'Integer')
x5266	=	p.LpVariable("	x5266	",lowBound=0, cat= 'Integer')
x5267	=	p.LpVariable("	x5267	",lowBound=0, cat= 'Integer')
x5268	=	p.LpVariable("	x5268	",lowBound=0, cat= 'Integer')
x5269	=	p.LpVariable("	x5269	",lowBound=0, cat= 'Integer')
x5270	=	p.LpVariable("	x5270	",lowBound=0, cat= 'Integer')
x5271	=	p.LpVariable("	x5271	",lowBound=0, cat= 'Integer')
x5272	=	p.LpVariable("	x5272	",lowBound=0, cat= 'Integer')
x5273	=	p.LpVariable("	x5273	",lowBound=0, cat= 'Integer')
x5274	=	p.LpVariable("	x5274	",lowBound=0, cat= 'Integer')
x5275	=	p.LpVariable("	x5275	",lowBound=0, cat= 'Integer')
x5276	=	p.LpVariable("	x5276	",lowBound=0, cat= 'Integer')
x5277	=	p.LpVariable("	x5277	",lowBound=0, cat= 'Integer')
x5278	=	p.LpVariable("	x5278	",lowBound=0, cat= 'Integer')
x5279	=	p.LpVariable("	x5279	",lowBound=0, cat= 'Integer')
x5280	=	p.LpVariable("	x5280	",lowBound=0, cat= 'Integer')
x5281	=	p.LpVariable("	x5281	",lowBound=0, cat= 'Integer')
x5282	=	p.LpVariable("	x5282	",lowBound=0, cat= 'Integer')
x5283	=	p.LpVariable("	x5283	",lowBound=0, cat= 'Integer')
x5284	=	p.LpVariable("	x5284	",lowBound=0, cat= 'Integer')
x5285	=	p.LpVariable("	x5285	",lowBound=0, cat= 'Integer')
x5286	=	p.LpVariable("	x5286	",lowBound=0, cat= 'Integer')
x5287	=	p.LpVariable("	x5287	",lowBound=0, cat= 'Integer')
x5288	=	p.LpVariable("	x5288	",lowBound=0, cat= 'Integer')
x5289	=	p.LpVariable("	x5289	",lowBound=0, cat= 'Integer')
x5290	=	p.LpVariable("	x5290	",lowBound=0, cat= 'Integer')
x5291	=	p.LpVariable("	x5291	",lowBound=0, cat= 'Integer')
x5292	=	p.LpVariable("	x5292	",lowBound=0, cat= 'Integer')
x5293	=	p.LpVariable("	x5293	",lowBound=0, cat= 'Integer')
x5294	=	p.LpVariable("	x5294	",lowBound=0, cat= 'Integer')
x5295	=	p.LpVariable("	x5295	",lowBound=0, cat= 'Integer')
x5296	=	p.LpVariable("	x5296	",lowBound=0, cat= 'Integer')
x5297	=	p.LpVariable("	x5297	",lowBound=0, cat= 'Integer')
x5298	=	p.LpVariable("	x5298	",lowBound=0, cat= 'Integer')
x5299	=	p.LpVariable("	x5299	",lowBound=0, cat= 'Integer')
x5300	=	p.LpVariable("	x5300	",lowBound=0, cat= 'Integer')
x5301	=	p.LpVariable("	x5301	",lowBound=0, cat= 'Integer')
x5302	=	p.LpVariable("	x5302	",lowBound=0, cat= 'Integer')
x5303	=	p.LpVariable("	x5303	",lowBound=0, cat= 'Integer')
x5304	=	p.LpVariable("	x5304	",lowBound=0, cat= 'Integer')
x5305	=	p.LpVariable("	x5305	",lowBound=0, cat= 'Integer')
x5306	=	p.LpVariable("	x5306	",lowBound=0, cat= 'Integer')
x5307	=	p.LpVariable("	x5307	",lowBound=0, cat= 'Integer')
x5308	=	p.LpVariable("	x5308	",lowBound=0, cat= 'Integer')
x5309	=	p.LpVariable("	x5309	",lowBound=0, cat= 'Integer')
x5310	=	p.LpVariable("	x5310	",lowBound=0, cat= 'Integer')
x5311	=	p.LpVariable("	x5311	",lowBound=0, cat= 'Integer')
x5312	=	p.LpVariable("	x5312	",lowBound=0, cat= 'Integer')
x5313	=	p.LpVariable("	x5313	",lowBound=0, cat= 'Integer')
x5314	=	p.LpVariable("	x5314	",lowBound=0, cat= 'Integer')
x5315	=	p.LpVariable("	x5315	",lowBound=0, cat= 'Integer')
x5316	=	p.LpVariable("	x5316	",lowBound=0, cat= 'Integer')
x5317	=	p.LpVariable("	x5317	",lowBound=0, cat= 'Integer')
x5318	=	p.LpVariable("	x5318	",lowBound=0, cat= 'Integer')
x5319	=	p.LpVariable("	x5319	",lowBound=0, cat= 'Integer')
x5320	=	p.LpVariable("	x5320	",lowBound=0, cat= 'Integer')
x5321	=	p.LpVariable("	x5321	",lowBound=0, cat= 'Integer')
x5322	=	p.LpVariable("	x5322	",lowBound=0, cat= 'Integer')
x5323	=	p.LpVariable("	x5323	",lowBound=0, cat= 'Integer')
x5324	=	p.LpVariable("	x5324	",lowBound=0, cat= 'Integer')
x5325	=	p.LpVariable("	x5325	",lowBound=0, cat= 'Integer')
x5326	=	p.LpVariable("	x5326	",lowBound=0, cat= 'Integer')
x5327	=	p.LpVariable("	x5327	",lowBound=0, cat= 'Integer')
x5328	=	p.LpVariable("	x5328	",lowBound=0, cat= 'Integer')
x5329	=	p.LpVariable("	x5329	",lowBound=0, cat= 'Integer')
x5330	=	p.LpVariable("	x5330	",lowBound=0, cat= 'Integer')
x5331	=	p.LpVariable("	x5331	",lowBound=0, cat= 'Integer')
x5332	=	p.LpVariable("	x5332	",lowBound=0, cat= 'Integer')
x5333	=	p.LpVariable("	x5333	",lowBound=0, cat= 'Integer')
x5334	=	p.LpVariable("	x5334	",lowBound=0, cat= 'Integer')
x5335	=	p.LpVariable("	x5335	",lowBound=0, cat= 'Integer')
x5336	=	p.LpVariable("	x5336	",lowBound=0, cat= 'Integer')
x5337	=	p.LpVariable("	x5337	",lowBound=0, cat= 'Integer')
x5338	=	p.LpVariable("	x5338	",lowBound=0, cat= 'Integer')
x5339	=	p.LpVariable("	x5339	",lowBound=0, cat= 'Integer')
x5340	=	p.LpVariable("	x5340	",lowBound=0, cat= 'Integer')
x5341	=	p.LpVariable("	x5341	",lowBound=0, cat= 'Integer')
x5342	=	p.LpVariable("	x5342	",lowBound=0, cat= 'Integer')
x5343	=	p.LpVariable("	x5343	",lowBound=0, cat= 'Integer')
x5344	=	p.LpVariable("	x5344	",lowBound=0, cat= 'Integer')
x5345	=	p.LpVariable("	x5345	",lowBound=0, cat= 'Integer')
x5346	=	p.LpVariable("	x5346	",lowBound=0, cat= 'Integer')
x5347	=	p.LpVariable("	x5347	",lowBound=0, cat= 'Integer')
x5348	=	p.LpVariable("	x5348	",lowBound=0, cat= 'Integer')
x5349	=	p.LpVariable("	x5349	",lowBound=0, cat= 'Integer')
x5350	=	p.LpVariable("	x5350	",lowBound=0, cat= 'Integer')
x5351	=	p.LpVariable("	x5351	",lowBound=0, cat= 'Integer')
x5352	=	p.LpVariable("	x5352	",lowBound=0, cat= 'Integer')
x5353	=	p.LpVariable("	x5353	",lowBound=0, cat= 'Integer')
x5354	=	p.LpVariable("	x5354	",lowBound=0, cat= 'Integer')
x5355	=	p.LpVariable("	x5355	",lowBound=0, cat= 'Integer')
x5356	=	p.LpVariable("	x5356	",lowBound=0, cat= 'Integer')
x5357	=	p.LpVariable("	x5357	",lowBound=0, cat= 'Integer')
x5358	=	p.LpVariable("	x5358	",lowBound=0, cat= 'Integer')
x5359	=	p.LpVariable("	x5359	",lowBound=0, cat= 'Integer')
x5360	=	p.LpVariable("	x5360	",lowBound=0, cat= 'Integer')
x5361	=	p.LpVariable("	x5361	",lowBound=0, cat= 'Integer')
x5362	=	p.LpVariable("	x5362	",lowBound=0, cat= 'Integer')
x5363	=	p.LpVariable("	x5363	",lowBound=0, cat= 'Integer')
x5364	=	p.LpVariable("	x5364	",lowBound=0, cat= 'Integer')
x5365	=	p.LpVariable("	x5365	",lowBound=0, cat= 'Integer')
x5366	=	p.LpVariable("	x5366	",lowBound=0, cat= 'Integer')
x5367	=	p.LpVariable("	x5367	",lowBound=0, cat= 'Integer')
x5368	=	p.LpVariable("	x5368	",lowBound=0, cat= 'Integer')
x5369	=	p.LpVariable("	x5369	",lowBound=0, cat= 'Integer')
x5370	=	p.LpVariable("	x5370	",lowBound=0, cat= 'Integer')
x5371	=	p.LpVariable("	x5371	",lowBound=0, cat= 'Integer')
x5372	=	p.LpVariable("	x5372	",lowBound=0, cat= 'Integer')
x5373	=	p.LpVariable("	x5373	",lowBound=0, cat= 'Integer')
x5374	=	p.LpVariable("	x5374	",lowBound=0, cat= 'Integer')
x5375	=	p.LpVariable("	x5375	",lowBound=0, cat= 'Integer')
x5376	=	p.LpVariable("	x5376	",lowBound=0, cat= 'Integer')
x5377	=	p.LpVariable("	x5377	",lowBound=0, cat= 'Integer')
x5378	=	p.LpVariable("	x5378	",lowBound=0, cat= 'Integer')
x5379	=	p.LpVariable("	x5379	",lowBound=0, cat= 'Integer')
x5380	=	p.LpVariable("	x5380	",lowBound=0, cat= 'Integer')
x5381	=	p.LpVariable("	x5381	",lowBound=0, cat= 'Integer')
x5382	=	p.LpVariable("	x5382	",lowBound=0, cat= 'Integer')
x5383	=	p.LpVariable("	x5383	",lowBound=0, cat= 'Integer')
x5384	=	p.LpVariable("	x5384	",lowBound=0, cat= 'Integer')
x5385	=	p.LpVariable("	x5385	",lowBound=0, cat= 'Integer')
x5386	=	p.LpVariable("	x5386	",lowBound=0, cat= 'Integer')
x5387	=	p.LpVariable("	x5387	",lowBound=0, cat= 'Integer')
x5388	=	p.LpVariable("	x5388	",lowBound=0, cat= 'Integer')
x5389	=	p.LpVariable("	x5389	",lowBound=0, cat= 'Integer')
x5390	=	p.LpVariable("	x5390	",lowBound=0, cat= 'Integer')
x5391	=	p.LpVariable("	x5391	",lowBound=0, cat= 'Integer')
x5392	=	p.LpVariable("	x5392	",lowBound=0, cat= 'Integer')
x5393	=	p.LpVariable("	x5393	",lowBound=0, cat= 'Integer')
x5394	=	p.LpVariable("	x5394	",lowBound=0, cat= 'Integer')
x5395	=	p.LpVariable("	x5395	",lowBound=0, cat= 'Integer')
x5396	=	p.LpVariable("	x5396	",lowBound=0, cat= 'Integer')
x5397	=	p.LpVariable("	x5397	",lowBound=0, cat= 'Integer')
x5398	=	p.LpVariable("	x5398	",lowBound=0, cat= 'Integer')
x5399	=	p.LpVariable("	x5399	",lowBound=0, cat= 'Integer')
x5400	=	p.LpVariable("	x5400	",lowBound=0, cat= 'Integer')
x5401	=	p.LpVariable("	x5401	",lowBound=0, cat= 'Integer')
x5402	=	p.LpVariable("	x5402	",lowBound=0, cat= 'Integer')
x5403	=	p.LpVariable("	x5403	",lowBound=0, cat= 'Integer')




#objective function

Lp_prob += x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13+x14+x15+x16+x17+x18+x19+x20+x21+x22+x23+x24+x25+x26+x27+x28+x29+x30+x31+x32+x33+x34+x35+x36+x37+x38+x39+x40+x41+x42+x43+x44+x45+x46+x47+x48+x49+x50+x51+x52+x53+x54+x55+x56+x57+x58+x59+x60+x61+x62+x63+x64+x65+x66+x67+x68+x69+x70+x71+x72+x73+x74+x75+x76+x77+x78+x79+x80+x81+x82+x83+x84+x85+x86+x87+x88+x89+x90+x91+x92+x93+x94+x95+x96+x97+x98+x99+x100+x101+x102+x103+x104+x105+x106+x107+x108+x109+x110+x111+x112+x113+x114+x115+x116+x117+x118+x119+x120+x121+x122+x123+x124+x125+x126+x127+x128+x129+x130+x131+x132+x133+x134+x135+x136+x137+x138+x139+x140+x141+x142+x143+x144+x145+x146+x147+x148+x149+x150+x151+x152+x153+x154+x155+x156+x157+x158+x159+x160+x161+x162+x163+x164+x165+x166+x167+x168+x169+x170+x171+x172+x173+x174+x175+x176+x177+x178+x179+x180+x181+x182+x183+x184+x185+x186+x187+x188+x189+x190+x191+x192+x193+x194+x195+x196+x197+x198+x199+x200+x201+x202+x203+x204+x205+x206+x207+x208+x209+x210+x211+x212+x213+x214+x215+x216+x217+x218+x219+x220+x221+x222+x223+x224+x225+x226+x227+x228+x229+x230+x231+x232+x233+x234+x235+x236+x237+x238+x239+x240+x241+x242+x243+x244+x245+x246+x247+x248+x249+x250+x251+x252+x253+x254+x255+x256+x257+x258+x259+x260+x261+x262+x263+x264+x265+x266+x267+x268+x269+x270+x271+x272+x273+x274+x275+x276+x277+x278+x279+x280+x281+x282+x283+x284+x285+x286+x287+x288+x289+x290+x291+x292+x293+x294+x295+x296+x297+x298+x299+x300+x301+x302+x303+x304+x305+x306+x307+x308+x309+x310+x311+x312+x313+x314+x315+x316+x317+x318+x319+x320+x321+x322+x323+x324+x325+x326+x327+x328+x329+x330+x331+x332+x333+x334+x335+x336+x337+x338+x339+x340+x341+x342+x343+x344+x345+x346+x347+x348+x349+x350+x351+x352+x353+x354+x355+x356+x357+x358+x359+x360+x361+x362+x363+x364+x365+x366+x367+x368+x369+x370+x371+x372+x373+x374+x375+x376+x377+x378+x379+x380+x381+x382+x383+x384+x385+x386+x387+x388+x389+x390+x391+x392+x393+x394+x395+x396+x397+x398+x399+x400+x401+x402+x403+x404+x405+x406+x407+x408+x409+x410+x411+x412+x413+x414+x415+x416+x417+x418+x419+x420+x421+x422+x423+x424+x425+x426+x427+x428+x429+x430+x431+x432+x433+x434+x435+x436+x437+x438+x439+x440+x441+x442+x443+x444+x445+x446+x447+x448+x449+x450+x451+x452+x453+x454+x455+x456+x457+x458+x459+x460+x461+x462+x463+x464+x465+x466+x467+x468+x469+x470+x471+x472+x473+x474+x475+x476+x477+x478+x479+x480+x481+x482+x483+x484+x485+x486+x487+x488+x489+x490+x491+x492+x493+x494+x495+x496+x497+x498+x499+x500+x501+x502+x503+x504+x505+x506+x507+x508+x509+x510+x511+x512+x513+x514+x515+x516+x517+x518+x519+x520+x521+x522+x523+x524+x525+x526+x527+x528+x529+x530+x531+x532+x533+x534+x535+x536+x537+x538+x539+x540+x541+x542+x543+x544+x545+x546+x547+x548+x549+x550+x551+x552+x553+x554+x555+x556+x557+x558+x559+x560+x561+x562+x563+x564+x565+x566+x567+x568+x569+x570+x571+x572+x573+x574+x575+x576+x577+x578+x579+x580+x581+x582+x583+x584+x585+x586+x587+x588+x589+x590+x591+x592+x593+x594+x595+x596+x597+x598+x599+x600+x601+x602+x603+x604+x605+x606+x607+x608+x609+x610+x611+x612+x613+x614+x615+x616+x617+x618+x619+x620+x621+x622+x623+x624+x625+x626+x627+x628+x629+x630+x631+x632+x633+x634+x635+x636+x637+x638+x639+x640+x641+x642+x643+x644+x645+x646+x647+x648+x649+x650+x651+x652+x653+x654+x655+x656+x657+x658+x659+x660+x661+x662+x663+x664+x665+x666+x667+x668+x669+x670+x671+x672+x673+x674+x675+x676+x677+x678+x679+x680+x681+x682+x683+x684+x685+x686+x687+x688+x689+x690+x691+x692+x693+x694+x695+x696+x697+x698+x699+x700+x701+x702+x703+x704+x705+x706+x707+x708+x709+x710+x711+x712+x713+x714+x715+x716+x717+x718+x719+x720+x721+x722+x723+x724+x725+x726+x727+x728+x729+x730+x731+x732+x733+x734+x735+x736+x737+x738+x739+x740+x741+x742+x743+x744+x745+x746+x747+x748+x749+x750+x751+x752+x753+x754+x755+x756+x757+x758+x759+x760+x761+x762+x763+x764+x765+x766+x767+x768+x769+x770+x771+x772+x773+x774+x775+x776+x777+x778+x779+x780+x781+x782+x783+x784+x785+x786+x787+x788+x789+x790+x791+x792+x793+x794+x795+x796+x797+x798+x799+x800+x801+x802+x803+x804+x805+x806+x807+x808+x809+x810+x811+x812+x813+x814+x815+x816+x817+x818+x819+x820+x821+x822+x823+x824+x825+x826+x827+x828+x829+x830+x831+x832+x833+x834+x835+x836+x837+x838+x839+x840+x841+x842+x843+x844+x845+x846+x847+x848+x849+x850+x851+x852+x853+x854+x855+x856+x857+x858+x859+x860+x861+x862+x863+x864+x865+x866+x867+x868+x869+x870+x871+x872+x873+x874+x875+x876+x877+x878+x879+x880+x881+x882+x883+x884+x885+x886+x887+x888+x889+x890+x891+x892+x893+x894+x895+x896+x897+x898+x899+x900+x901+x902+x903+x904+x905+x906+x907+x908+x909+x910+x911+x912+x913+x914+x915+x916+x917+x918+x919+x920+x921+x922+x923+x924+x925+x926+x927+x928+x929+x930+x931+x932+x933+x934+x935+x936+x937+x938+x939+x940+x941+x942+x943+x944+x945+x946+x947+x948+x949+x950+x951+x952+x953+x954+x955+x956+x957+x958+x959+x960+x961+x962+x963+x964+x965+x966+x967+x968+x969+x970+x971+x972+x973+x974+x975+x976+x977+x978+x979+x980+x981+x982+x983+x984+x985+x986+x987+x988+x989+x990+x991+x992+x993+x994+x995+x996+x997+x998+x999+x1000+x1001+x1002+x1003+x1004+x1005+x1006+x1007+x1008+x1009+x1010+x1011+x1012+x1013+x1014+x1015+x1016+x1017+x1018+x1019+x1020+x1021+x1022+x1023+x1024+x1025+x1026+x1027+x1028+x1029+x1030+x1031+x1032+x1033+x1034+x1035+x1036+x1037+x1038+x1039+x1040+x1041+x1042+x1043+x1044+x1045+x1046+x1047+x1048+x1049+x1050+x1051+x1052+x1053+x1054+x1055+x1056+x1057+x1058+x1059+x1060+x1061+x1062+x1063+x1064+x1065+x1066+x1067+x1068+x1069+x1070+x1071+x1072+x1073+x1074+x1075+x1076+x1077+x1078+x1079+x1080+x1081+x1082+x1083+x1084+x1085+x1086+x1087+x1088+x1089+x1090+x1091+x1092+x1093+x1094+x1095+x1096+x1097+x1098+x1099+x1100+x1101+x1102+x1103+x1104+x1105+x1106+x1107+x1108+x1109+x1110+x1111+x1112+x1113+x1114+x1115+x1116+x1117+x1118+x1119+x1120+x1121+x1122+x1123+x1124+x1125+x1126+x1127+x1128+x1129+x1130+x1131+x1132+x1133+x1134+x1135+x1136+x1137+x1138+x1139+x1140+x1141+x1142+x1143+x1144+x1145+x1146+x1147+x1148+x1149+x1150+x1151+x1152+x1153+x1154+x1155+x1156+x1157+x1158+x1159+x1160+x1161+x1162+x1163+x1164+x1165+x1166+x1167+x1168+x1169+x1170+x1171+x1172+x1173+x1174+x1175+x1176+x1177+x1178+x1179+x1180+x1181+x1182+x1183+x1184+x1185+x1186+x1187+x1188+x1189+x1190+x1191+x1192+x1193+x1194+x1195+x1196+x1197+x1198+x1199+x1200+x1201+x1202+x1203+x1204+x1205+x1206+x1207+x1208+x1209+x1210+x1211+x1212+x1213+x1214+x1215+x1216+x1217+x1218+x1219+x1220+x1221+x1222+x1223+x1224+x1225+x1226+x1227+x1228+x1229+x1230+x1231+x1232+x1233+x1234+x1235+x1236+x1237+x1238+x1239+x1240+x1241+x1242+x1243+x1244+x1245+x1246+x1247+x1248+x1249+x1250+x1251+x1252+x1253+x1254+x1255+x1256+x1257+x1258+x1259+x1260+x1261+x1262+x1263+x1264+x1265+x1266+x1267+x1268+x1269+x1270+x1271+x1272+x1273+x1274+x1275+x1276+x1277+x1278+x1279+x1280+x1281+x1282+x1283+x1284+x1285+x1286+x1287+x1288+x1289+x1290+x1291+x1292+x1293+x1294+x1295+x1296+x1297+x1298+x1299+x1300+x1301+x1302+x1303+x1304+x1305+x1306+x1307+x1308+x1309+x1310+x1311+x1312+x1313+x1314+x1315+x1316+x1317+x1318+x1319+x1320+x1321+x1322+x1323+x1324+x1325+x1326+x1327+x1328+x1329+x1330+x1331+x1332+x1333+x1334+x1335+x1336+x1337+x1338+x1339+x1340+x1341+x1342+x1343+x1344+x1345+x1346+x1347+x1348+x1349+x1350+x1351+x1352+x1353+x1354+x1355+x1356+x1357+x1358+x1359+x1360+x1361+x1362+x1363+x1364+x1365+x1366+x1367+x1368+x1369+x1370+x1371+x1372+x1373+x1374+x1375+x1376+x1377+x1378+x1379+x1380+x1381+x1382+x1383+x1384+x1385+x1386+x1387+x1388+x1389+x1390+x1391+x1392+x1393+x1394+x1395+x1396+x1397+x1398+x1399+x1400+x1401+x1402+x1403+x1404+x1405+x1406+x1407+x1408+x1409+x1410+x1411+x1412+x1413+x1414+x1415+x1416+x1417+x1418+x1419+x1420+x1421+x1422+x1423+x1424+x1425+x1426+x1427+x1428+x1429+x1430+x1431+x1432+x1433+x1434+x1435+x1436+x1437+x1438+x1439+x1440+x1441+x1442+x1443+x1444+x1445+x1446+x1447+x1448+x1449+x1450+x1451+x1452+x1453+x1454+x1455+x1456+x1457+x1458+x1459+x1460+x1461+x1462+x1463+x1464+x1465+x1466+x1467+x1468+x1469+x1470+x1471+x1472+x1473+x1474+x1475+x1476+x1477+x1478+x1479+x1480+x1481+x1482+x1483+x1484+x1485+x1486+x1487+x1488+x1489+x1490+x1491+x1492+x1493+x1494+x1495+x1496+x1497+x1498+x1499+x1500+x1501+x1502+x1503+x1504+x1505+x1506+x1507+x1508+x1509+x1510+x1511+x1512+x1513+x1514+x1515+x1516+x1517+x1518+x1519+x1520+x1521+x1522+x1523+x1524+x1525+x1526+x1527+x1528+x1529+x1530+x1531+x1532+x1533+x1534+x1535+x1536+x1537+x1538+x1539+x1540+x1541+x1542+x1543+x1544+x1545+x1546+x1547+x1548+x1549+x1550+x1551+x1552+x1553+x1554+x1555+x1556+x1557+x1558+x1559+x1560+x1561+x1562+x1563+x1564+x1565+x1566+x1567+x1568+x1569+x1570+x1571+x1572+x1573+x1574+x1575+x1576+x1577+x1578+x1579+x1580+x1581+x1582+x1583+x1584+x1585+x1586+x1587+x1588+x1589+x1590+x1591+x1592+x1593+x1594+x1595+x1596+x1597+x1598+x1599+x1600+x1601+x1602+x1603+x1604+x1605+x1606+x1607+x1608+x1609+x1610+x1611+x1612+x1613+x1614+x1615+x1616+x1617+x1618+x1619+x1620+x1621+x1622+x1623+x1624+x1625+x1626+x1627+x1628+x1629+x1630+x1631+x1632+x1633+x1634+x1635+x1636+x1637+x1638+x1639+x1640+x1641+x1642+x1643+x1644+x1645+x1646+x1647+x1648+x1649+x1650+x1651+x1652+x1653+x1654+x1655+x1656+x1657+x1658+x1659+x1660+x1661+x1662+x1663+x1664+x1665+x1666+x1667+x1668+x1669+x1670+x1671+x1672+x1673+x1674+x1675+x1676+x1677+x1678+x1679+x1680+x1681+x1682+x1683+x1684+x1685+x1686+x1687+x1688+x1689+x1690+x1691+x1692+x1693+x1694+x1695+x1696+x1697+x1698+x1699+x1700+x1701+x1702+x1703+x1704+x1705+x1706+x1707+x1708+x1709+x1710+x1711+x1712+x1713+x1714+x1715+x1716+x1717+x1718+x1719+x1720+x1721+x1722+x1723+x1724+x1725+x1726+x1727+x1728+x1729+x1730+x1731+x1732+x1733+x1734+x1735+x1736+x1737+x1738+x1739+x1740+x1741+x1742+x1743+x1744+x1745+x1746+x1747+x1748+x1749+x1750+x1751+x1752+x1753+x1754+x1755+x1756+x1757+x1758+x1759+x1760+x1761+x1762+x1763+x1764+x1765+x1766+x1767+x1768+x1769+x1770+x1771+x1772+x1773+x1774+x1775+x1776+x1777+x1778+x1779+x1780+x1781+x1782+x1783+x1784+x1785+x1786+x1787+x1788+x1789+x1790+x1791+x1792+x1793+x1794+x1795+x1796+x1797+x1798+x1799+x1800+x1801+x1802+x1803+x1804+x1805+x1806+x1807+x1808+x1809+x1810+x1811+x1812+x1813+x1814+x1815+x1816+x1817+x1818+x1819+x1820+x1821+x1822+x1823+x1824+x1825+x1826+x1827+x1828+x1829+x1830+x1831+x1832+x1833+x1834+x1835+x1836+x1837+x1838+x1839+x1840+x1841+x1842+x1843+x1844+x1845+x1846+x1847+x1848+x1849+x1850+x1851+x1852+x1853+x1854+x1855+x1856+x1857+x1858+x1859+x1860+x1861+x1862+x1863+x1864+x1865+x1866+x1867+x1868+x1869+x1870+x1871+x1872+x1873+x1874+x1875+x1876+x1877+x1878+x1879+x1880+x1881+x1882+x1883+x1884+x1885+x1886+x1887+x1888+x1889+x1890+x1891+x1892+x1893+x1894+x1895+x1896+x1897+x1898+x1899+x1900+x1901+x1902+x1903+x1904+x1905+x1906+x1907+x1908+x1909+x1910+x1911+x1912+x1913+x1914+x1915+x1916+x1917+x1918+x1919+x1920+x1921+x1922+x1923+x1924+x1925+x1926+x1927+x1928+x1929+x1930+x1931+x1932+x1933+x1934+x1935+x1936+x1937+x1938+x1939+x1940+x1941+x1942+x1943+x1944+x1945+x1946+x1947+x1948+x1949+x1950+x1951+x1952+x1953+x1954+x1955+x1956+x1957+x1958+x1959+x1960+x1961+x1962+x1963+x1964+x1965+x1966+x1967+x1968+x1969+x1970+x1971+x1972+x1973+x1974+x1975+x1976+x1977+x1978+x1979+x1980+x1981+x1982+x1983+x1984+x1985+x1986+x1987+x1988+x1989+x1990+x1991+x1992+x1993+x1994+x1995+x1996+x1997+x1998+x1999+x2000+x2001+x2002+x2003+x2004+x2005+x2006+x2007+x2008+x2009+x2010+x2011+x2012+x2013+x2014+x2015+x2016+x2017+x2018+x2019+x2020+x2021+x2022+x2023+x2024+x2025+x2026+x2027+x2028+x2029+x2030+x2031+x2032+x2033+x2034+x2035+x2036+x2037+x2038+x2039+x2040+x2041+x2042+x2043+x2044+x2045+x2046+x2047+x2048+x2049+x2050+x2051+x2052+x2053+x2054+x2055+x2056+x2057+x2058+x2059+x2060+x2061+x2062+x2063+x2064+x2065+x2066+x2067+x2068+x2069+x2070+x2071+x2072+x2073+x2074+x2075+x2076+x2077+x2078+x2079+x2080+x2081+x2082+x2083+x2084+x2085+x2086+x2087+x2088+x2089+x2090+x2091+x2092+x2093+x2094+x2095+x2096+x2097+x2098+x2099+x2100+x2101+x2102+x2103+x2104+x2105+x2106+x2107+x2108+x2109+x2110+x2111+x2112+x2113+x2114+x2115+x2116+x2117+x2118+x2119+x2120+x2121+x2122+x2123+x2124+x2125+x2126+x2127+x2128+x2129+x2130+x2131+x2132+x2133+x2134+x2135+x2136+x2137+x2138+x2139+x2140+x2141+x2142+x2143+x2144+x2145+x2146+x2147+x2148+x2149+x2150+x2151+x2152+x2153+x2154+x2155+x2156+x2157+x2158+x2159+x2160+x2161+x2162+x2163+x2164+x2165+x2166+x2167+x2168+x2169+x2170+x2171+x2172+x2173+x2174+x2175+x2176+x2177+x2178+x2179+x2180+x2181+x2182+x2183+x2184+x2185+x2186+x2187+x2188+x2189+x2190+x2191+x2192+x2193+x2194+x2195+x2196+x2197+x2198+x2199+x2200+x2201+x2202+x2203+x2204+x2205+x2206+x2207+x2208+x2209+x2210+x2211+x2212+x2213+x2214+x2215+x2216+x2217+x2218+x2219+x2220+x2221+x2222+x2223+x2224+x2225+x2226+x2227+x2228+x2229+x2230+x2231+x2232+x2233+x2234+x2235+x2236+x2237+x2238+x2239+x2240+x2241+x2242+x2243+x2244+x2245+x2246+x2247+x2248+x2249+x2250+x2251+x2252+x2253+x2254+x2255+x2256+x2257+x2258+x2259+x2260+x2261+x2262+x2263+x2264+x2265+x2266+x2267+x2268+x2269+x2270+x2271+x2272+x2273+x2274+x2275+x2276+x2277+x2278+x2279+x2280+x2281+x2282+x2283+x2284+x2285+x2286+x2287+x2288+x2289+x2290+x2291+x2292+x2293+x2294+x2295+x2296+x2297+x2298+x2299+x2300+x2301+x2302+x2303+x2304+x2305+x2306+x2307+x2308+x2309+x2310+x2311+x2312+x2313+x2314+x2315+x2316+x2317+x2318+x2319+x2320+x2321+x2322+x2323+x2324+x2325+x2326+x2327+x2328+x2329+x2330+x2331+x2332+x2333+x2334+x2335+x2336+x2337+x2338+x2339+x2340+x2341+x2342+x2343+x2344+x2345+x2346+x2347+x2348+x2349+x2350+x2351+x2352+x2353+x2354+x2355+x2356+x2357+x2358+x2359+x2360+x2361+x2362+x2363+x2364+x2365+x2366+x2367+x2368+x2369+x2370+x2371+x2372+x2373+x2374+x2375+x2376+x2377+x2378+x2379+x2380+x2381+x2382+x2383+x2384+x2385+x2386+x2387+x2388+x2389+x2390+x2391+x2392+x2393+x2394+x2395+x2396+x2397+x2398+x2399+x2400+x2401+x2402+x2403+x2404+x2405+x2406+x2407+x2408+x2409+x2410+x2411+x2412+x2413+x2414+x2415+x2416+x2417+x2418+x2419+x2420+x2421+x2422+x2423+x2424+x2425+x2426+x2427+x2428+x2429+x2430+x2431+x2432+x2433+x2434+x2435+x2436+x2437+x2438+x2439+x2440+x2441+x2442+x2443+x2444+x2445+x2446+x2447+x2448+x2449+x2450+x2451+x2452+x2453+x2454+x2455+x2456+x2457+x2458+x2459+x2460+x2461+x2462+x2463+x2464+x2465+x2466+x2467+x2468+x2469+x2470+x2471+x2472+x2473+x2474+x2475+x2476+x2477+x2478+x2479+x2480+x2481+x2482+x2483+x2484+x2485+x2486+x2487+x2488+x2489+x2490+x2491+x2492+x2493+x2494+x2495+x2496+x2497+x2498+x2499+x2500+x2501+x2502+x2503+x2504+x2505+x2506+x2507+x2508+x2509+x2510+x2511+x2512+x2513+x2514+x2515+x2516+x2517+x2518+x2519+x2520+x2521+x2522+x2523+x2524+x2525+x2526+x2527+x2528+x2529+x2530+x2531+x2532+x2533+x2534+x2535+x2536+x2537+x2538+x2539+x2540+x2541+x2542+x2543+x2544+x2545+x2546+x2547+x2548+x2549+x2550+x2551+x2552+x2553+x2554+x2555+x2556+x2557+x2558+x2559+x2560+x2561+x2562+x2563+x2564+x2565+x2566+x2567+x2568+x2569+x2570+x2571+x2572+x2573+x2574+x2575+x2576+x2577+x2578+x2579+x2580+x2581+x2582+x2583+x2584+x2585+x2586+x2587+x2588+x2589+x2590+x2591+x2592+x2593+x2594+x2595+x2596+x2597+x2598+x2599+x2600+x2601+x2602+x2603+x2604+x2605+x2606+x2607+x2608+x2609+x2610+x2611+x2612+x2613+x2614+x2615+x2616+x2617+x2618+x2619+x2620+x2621+x2622+x2623+x2624+x2625+x2626+x2627+x2628+x2629+x2630+x2631+x2632+x2633+x2634+x2635+x2636+x2637+x2638+x2639+x2640+x2641+x2642+x2643+x2644+x2645+x2646+x2647+x2648+x2649+x2650+x2651+x2652+x2653+x2654+x2655+x2656+x2657+x2658+x2659+x2660+x2661+x2662+x2663+x2664+x2665+x2666+x2667+x2668+x2669+x2670+x2671+x2672+x2673+x2674+x2675+x2676+x2677+x2678+x2679+x2680+x2681+x2682+x2683+x2684+x2685+x2686+x2687+x2688+x2689+x2690+x2691+x2692+x2693+x2694+x2695+x2696+x2697+x2698+x2699+x2700+x2701+x2702+x2703+x2704+x2705+x2706+x2707+x2708+x2709+x2710+x2711+x2712+x2713+x2714+x2715+x2716+x2717+x2718+x2719+x2720+x2721+x2722+x2723+x2724+x2725+x2726+x2727+x2728+x2729+x2730+x2731+x2732+x2733+x2734+x2735+x2736+x2737+x2738+x2739+x2740+x2741+x2742+x2743+x2744+x2745+x2746+x2747+x2748+x2749+x2750+x2751+x2752+x2753+x2754+x2755+x2756+x2757+x2758+x2759+x2760+x2761+x2762+x2763+x2764+x2765+x2766+x2767+x2768+x2769+x2770+x2771+x2772+x2773+x2774+x2775+x2776+x2777+x2778+x2779+x2780+x2781+x2782+x2783+x2784+x2785+x2786+x2787+x2788+x2789+x2790+x2791+x2792+x2793+x2794+x2795+x2796+x2797+x2798+x2799+x2800+x2801+x2802+x2803+x2804+x2805+x2806+x2807+x2808+x2809+x2810+x2811+x2812+x2813+x2814+x2815+x2816+x2817+x2818+x2819+x2820+x2821+x2822+x2823+x2824+x2825+x2826+x2827+x2828+x2829+x2830+x2831+x2832+x2833+x2834+x2835+x2836+x2837+x2838+x2839+x2840+x2841+x2842+x2843+x2844+x2845+x2846+x2847+x2848+x2849+x2850+x2851+x2852+x2853+x2854+x2855+x2856+x2857+x2858+x2859+x2860+x2861+x2862+x2863+x2864+x2865+x2866+x2867+x2868+x2869+x2870+x2871+x2872+x2873+x2874+x2875+x2876+x2877+x2878+x2879+x2880+x2881+x2882+x2883+x2884+x2885+x2886+x2887+x2888+x2889+x2890+x2891+x2892+x2893+x2894+x2895+x2896+x2897+x2898+x2899+x2900+x2901+x2902+x2903+x2904+x2905+x2906+x2907+x2908+x2909+x2910+x2911+x2912+x2913+x2914+x2915+x2916+x2917+x2918+x2919+x2920+x2921+x2922+x2923+x2924+x2925+x2926+x2927+x2928+x2929+x2930+x2931+x2932+x2933+x2934+x2935+x2936+x2937+x2938+x2939+x2940+x2941+x2942+x2943+x2944+x2945+x2946+x2947+x2948+x2949+x2950+x2951+x2952+x2953+x2954+x2955+x2956+x2957+x2958+x2959+x2960+x2961+x2962+x2963+x2964+x2965+x2966+x2967+x2968+x2969+x2970+x2971+x2972+x2973+x2974+x2975+x2976+x2977+x2978+x2979+x2980+x2981+x2982+x2983+x2984+x2985+x2986+x2987+x2988+x2989+x2990+x2991+x2992+x2993+x2994+x2995+x2996+x2997+x2998+x2999+x3000+x3001+x3002+x3003+x3004+x3005+x3006+x3007+x3008+x3009+x3010+x3011+x3012+x3013+x3014+x3015+x3016+x3017+x3018+x3019+x3020+x3021+x3022+x3023+x3024+x3025+x3026+x3027+x3028+x3029+x3030+x3031+x3032+x3033+x3034+x3035+x3036+x3037+x3038+x3039+x3040+x3041+x3042+x3043+x3044+x3045+x3046+x3047+x3048+x3049+x3050+x3051+x3052+x3053+x3054+x3055+x3056+x3057+x3058+x3059+x3060+x3061+x3062+x3063+x3064+x3065+x3066+x3067+x3068+x3069+x3070+x3071+x3072+x3073+x3074+x3075+x3076+x3077+x3078+x3079+x3080+x3081+x3082+x3083+x3084+x3085+x3086+x3087+x3088+x3089+x3090+x3091+x3092+x3093+x3094+x3095+x3096+x3097+x3098+x3099+x3100+x3101+x3102+x3103+x3104+x3105+x3106+x3107+x3108+x3109+x3110+x3111+x3112+x3113+x3114+x3115+x3116+x3117+x3118+x3119+x3120+x3121+x3122+x3123+x3124+x3125+x3126+x3127+x3128+x3129+x3130+x3131+x3132+x3133+x3134+x3135+x3136+x3137+x3138+x3139+x3140+x3141+x3142+x3143+x3144+x3145+x3146+x3147+x3148+x3149+x3150+x3151+x3152+x3153+x3154+x3155+x3156+x3157+x3158+x3159+x3160+x3161+x3162+x3163+x3164+x3165+x3166+x3167+x3168+x3169+x3170+x3171+x3172+x3173+x3174+x3175+x3176+x3177+x3178+x3179+x3180+x3181+x3182+x3183+x3184+x3185+x3186+x3187+x3188+x3189+x3190+x3191+x3192+x3193+x3194+x3195+x3196+x3197+x3198+x3199+x3200+x3201+x3202+x3203+x3204+x3205+x3206+x3207+x3208+x3209+x3210+x3211+x3212+x3213+x3214+x3215+x3216+x3217+x3218+x3219+x3220+x3221+x3222+x3223+x3224+x3225+x3226+x3227+x3228+x3229+x3230+x3231+x3232+x3233+x3234+x3235+x3236+x3237+x3238+x3239+x3240+x3241+x3242+x3243+x3244+x3245+x3246+x3247+x3248+x3249+x3250+x3251+x3252+x3253+x3254+x3255+x3256+x3257+x3258+x3259+x3260+x3261+x3262+x3263+x3264+x3265+x3266+x3267+x3268+x3269+x3270+x3271+x3272+x3273+x3274+x3275+x3276+x3277+x3278+x3279+x3280+x3281+x3282+x3283+x3284+x3285+x3286+x3287+x3288+x3289+x3290+x3291+x3292+x3293+x3294+x3295+x3296+x3297+x3298+x3299+x3300+x3301+x3302+x3303+x3304+x3305+x3306+x3307+x3308+x3309+x3310+x3311+x3312+x3313+x3314+x3315+x3316+x3317+x3318+x3319+x3320+x3321+x3322+x3323+x3324+x3325+x3326+x3327+x3328+x3329+x3330+x3331+x3332+x3333+x3334+x3335+x3336+x3337+x3338+x3339+x3340+x3341+x3342+x3343+x3344+x3345+x3346+x3347+x3348+x3349+x3350+x3351+x3352+x3353+x3354+x3355+x3356+x3357+x3358+x3359+x3360+x3361+x3362+x3363+x3364+x3365+x3366+x3367+x3368+x3369+x3370+x3371+x3372+x3373+x3374+x3375+x3376+x3377+x3378+x3379+x3380+x3381+x3382+x3383+x3384+x3385+x3386+x3387+x3388+x3389+x3390+x3391+x3392+x3393+x3394+x3395+x3396+x3397+x3398+x3399+x3400+x3401+x3402+x3403+x3404+x3405+x3406+x3407+x3408+x3409+x3410+x3411+x3412+x3413+x3414+x3415+x3416+x3417+x3418+x3419+x3420+x3421+x3422+x3423+x3424+x3425+x3426+x3427+x3428+x3429+x3430+x3431+x3432+x3433+x3434+x3435+x3436+x3437+x3438+x3439+x3440+x3441+x3442+x3443+x3444+x3445+x3446+x3447+x3448+x3449+x3450+x3451+x3452+x3453+x3454+x3455+x3456+x3457+x3458+x3459+x3460+x3461+x3462+x3463+x3464+x3465+x3466+x3467+x3468+x3469+x3470+x3471+x3472+x3473+x3474+x3475+x3476+x3477+x3478+x3479+x3480+x3481+x3482+x3483+x3484+x3485+x3486+x3487+x3488+x3489+x3490+x3491+x3492+x3493+x3494+x3495+x3496+x3497+x3498+x3499+x3500+x3501+x3502+x3503+x3504+x3505+x3506+x3507+x3508+x3509+x3510+x3511+x3512+x3513+x3514+x3515+x3516+x3517+x3518+x3519+x3520+x3521+x3522+x3523+x3524+x3525+x3526+x3527+x3528+x3529+x3530+x3531+x3532+x3533+x3534+x3535+x3536+x3537+x3538+x3539+x3540+x3541+x3542+x3543+x3544+x3545+x3546+x3547+x3548+x3549+x3550+x3551+x3552+x3553+x3554+x3555+x3556+x3557+x3558+x3559+x3560+x3561+x3562+x3563+x3564+x3565+x3566+x3567+x3568+x3569+x3570+x3571+x3572+x3573+x3574+x3575+x3576+x3577+x3578+x3579+x3580+x3581+x3582+x3583+x3584+x3585+x3586+x3587+x3588+x3589+x3590+x3591+x3592+x3593+x3594+x3595+x3596+x3597+x3598+x3599+x3600+x3601+x3602+x3603+x3604+x3605+x3606+x3607+x3608+x3609+x3610+x3611+x3612+x3613+x3614+x3615+x3616+x3617+x3618+x3619+x3620+x3621+x3622+x3623+x3624+x3625+x3626+x3627+x3628+x3629+x3630+x3631+x3632+x3633+x3634+x3635+x3636+x3637+x3638+x3639+x3640+x3641+x3642+x3643+x3644+x3645+x3646+x3647+x3648+x3649+x3650+x3651+x3652+x3653+x3654+x3655+x3656+x3657+x3658+x3659+x3660+x3661+x3662+x3663+x3664+x3665+x3666+x3667+x3668+x3669+x3670+x3671+x3672+x3673+x3674+x3675+x3676+x3677+x3678+x3679+x3680+x3681+x3682+x3683+x3684+x3685+x3686+x3687+x3688+x3689+x3690+x3691+x3692+x3693+x3694+x3695+x3696+x3697+x3698+x3699+x3700+x3701+x3702+x3703+x3704+x3705+x3706+x3707+x3708+x3709+x3710+x3711+x3712+x3713+x3714+x3715+x3716+x3717+x3718+x3719+x3720+x3721+x3722+x3723+x3724+x3725+x3726+x3727+x3728+x3729+x3730+x3731+x3732+x3733+x3734+x3735+x3736+x3737+x3738+x3739+x3740+x3741+x3742+x3743+x3744+x3745+x3746+x3747+x3748+x3749+x3750+x3751+x3752+x3753+x3754+x3755+x3756+x3757+x3758+x3759+x3760+x3761+x3762+x3763+x3764+x3765+x3766+x3767+x3768+x3769+x3770+x3771+x3772+x3773+x3774+x3775+x3776+x3777+x3778+x3779+x3780+x3781+x3782+x3783+x3784+x3785+x3786+x3787+x3788+x3789+x3790+x3791+x3792+x3793+x3794+x3795+x3796+x3797+x3798+x3799+x3800+x3801+x3802+x3803+x3804+x3805+x3806+x3807+x3808+x3809+x3810+x3811+x3812+x3813+x3814+x3815+x3816+x3817+x3818+x3819+x3820+x3821+x3822+x3823+x3824+x3825+x3826+x3827+x3828+x3829+x3830+x3831+x3832+x3833+x3834+x3835+x3836+x3837+x3838+x3839+x3840+x3841+x3842+x3843+x3844+x3845+x3846+x3847+x3848+x3849+x3850+x3851+x3852+x3853+x3854+x3855+x3856+x3857+x3858+x3859+x3860+x3861+x3862+x3863+x3864+x3865+x3866+x3867+x3868+x3869+x3870+x3871+x3872+x3873+x3874+x3875+x3876+x3877+x3878+x3879+x3880+x3881+x3882+x3883+x3884+x3885+x3886+x3887+x3888+x3889+x3890+x3891+x3892+x3893+x3894+x3895+x3896+x3897+x3898+x3899+x3900+x3901+x3902+x3903+x3904+x3905+x3906+x3907+x3908+x3909+x3910+x3911+x3912+x3913+x3914+x3915+x3916+x3917+x3918+x3919+x3920+x3921+x3922+x3923+x3924+x3925+x3926+x3927+x3928+x3929+x3930+x3931+x3932+x3933+x3934+x3935+x3936+x3937+x3938+x3939+x3940+x3941+x3942+x3943+x3944+x3945+x3946+x3947+x3948+x3949+x3950+x3951+x3952+x3953+x3954+x3955+x3956+x3957+x3958+x3959+x3960+x3961+x3962+x3963+x3964+x3965+x3966+x3967+x3968+x3969+x3970+x3971+x3972+x3973+x3974+x3975+x3976+x3977+x3978+x3979+x3980+x3981+x3982+x3983+x3984+x3985+x3986+x3987+x3988+x3989+x3990+x3991+x3992+x3993+x3994+x3995+x3996+x3997+x3998+x3999+x4000+x4001+x4002+x4003+x4004+x4005+x4006+x4007+x4008+x4009+x4010+x4011+x4012+x4013+x4014+x4015+x4016+x4017+x4018+x4019+x4020+x4021+x4022+x4023+x4024+x4025+x4026+x4027+x4028+x4029+x4030+x4031+x4032+x4033+x4034+x4035+x4036+x4037+x4038+x4039+x4040+x4041+x4042+x4043+x4044+x4045+x4046+x4047+x4048+x4049+x4050+x4051+x4052+x4053+x4054+x4055+x4056+x4057+x4058+x4059+x4060+x4061+x4062+x4063+x4064+x4065+x4066+x4067+x4068+x4069+x4070+x4071+x4072+x4073+x4074+x4075+x4076+x4077+x4078+x4079+x4080+x4081+x4082+x4083+x4084+x4085+x4086+x4087+x4088+x4089+x4090+x4091+x4092+x4093+x4094+x4095+x4096+x4097+x4098+x4099+x4100+x4101+x4102+x4103+x4104+x4105+x4106+x4107+x4108+x4109+x4110+x4111+x4112+x4113+x4114+x4115+x4116+x4117+x4118+x4119+x4120+x4121+x4122+x4123+x4124+x4125+x4126+x4127+x4128+x4129+x4130+x4131+x4132+x4133+x4134+x4135+x4136+x4137+x4138+x4139+x4140+x4141+x4142+x4143+x4144+x4145+x4146+x4147+x4148+x4149+x4150+x4151+x4152+x4153+x4154+x4155+x4156+x4157+x4158+x4159+x4160+x4161+x4162+x4163+x4164+x4165+x4166+x4167+x4168+x4169+x4170+x4171+x4172+x4173+x4174+x4175+x4176+x4177+x4178+x4179+x4180+x4181+x4182+x4183+x4184+x4185+x4186+x4187+x4188+x4189+x4190+x4191+x4192+x4193+x4194+x4195+x4196+x4197+x4198+x4199+x4200+x4201+x4202+x4203+x4204+x4205+x4206+x4207+x4208+x4209+x4210+x4211+x4212+x4213+x4214+x4215+x4216+x4217+x4218+x4219+x4220+x4221+x4222+x4223+x4224+x4225+x4226+x4227+x4228+x4229+x4230+x4231+x4232+x4233+x4234+x4235+x4236+x4237+x4238+x4239+x4240+x4241+x4242+x4243+x4244+x4245+x4246+x4247+x4248+x4249+x4250+x4251+x4252+x4253+x4254+x4255+x4256+x4257+x4258+x4259+x4260+x4261+x4262+x4263+x4264+x4265+x4266+x4267+x4268+x4269+x4270+x4271+x4272+x4273+x4274+x4275+x4276+x4277+x4278+x4279+x4280+x4281+x4282+x4283+x4284+x4285+x4286+x4287+x4288+x4289+x4290+x4291+x4292+x4293+x4294+x4295+x4296+x4297+x4298+x4299+x4300+x4301+x4302+x4303+x4304+x4305+x4306+x4307+x4308+x4309+x4310+x4311+x4312+x4313+x4314+x4315+x4316+x4317+x4318+x4319+x4320+x4321+x4322+x4323+x4324+x4325+x4326+x4327+x4328+x4329+x4330+x4331+x4332+x4333+x4334+x4335+x4336+x4337+x4338+x4339+x4340+x4341+x4342+x4343+x4344+x4345+x4346+x4347+x4348+x4349+x4350+x4351+x4352+x4353+x4354+x4355+x4356+x4357+x4358+x4359+x4360+x4361+x4362+x4363+x4364+x4365+x4366+x4367+x4368+x4369+x4370+x4371+x4372+x4373+x4374+x4375+x4376+x4377+x4378+x4379+x4380+x4381+x4382+x4383+x4384+x4385+x4386+x4387+x4388+x4389+x4390+x4391+x4392+x4393+x4394+x4395+x4396+x4397+x4398+x4399+x4400+x4401+x4402+x4403+x4404+x4405+x4406+x4407+x4408+x4409+x4410+x4411+x4412+x4413+x4414+x4415+x4416+x4417+x4418+x4419+x4420+x4421+x4422+x4423+x4424+x4425+x4426+x4427+x4428+x4429+x4430+x4431+x4432+x4433+x4434+x4435+x4436+x4437+x4438+x4439+x4440+x4441+x4442+x4443+x4444+x4445+x4446+x4447+x4448+x4449+x4450+x4451+x4452+x4453+x4454+x4455+x4456+x4457+x4458+x4459+x4460+x4461+x4462+x4463+x4464+x4465+x4466+x4467+x4468+x4469+x4470+x4471+x4472+x4473+x4474+x4475+x4476+x4477+x4478+x4479+x4480+x4481+x4482+x4483+x4484+x4485+x4486+x4487+x4488+x4489+x4490+x4491+x4492+x4493+x4494+x4495+x4496+x4497+x4498+x4499+x4500+x4501+x4502+x4503+x4504+x4505+x4506+x4507+x4508+x4509+x4510+x4511+x4512+x4513+x4514+x4515+x4516+x4517+x4518+x4519+x4520+x4521+x4522+x4523+x4524+x4525+x4526+x4527+x4528+x4529+x4530+x4531+x4532+x4533+x4534+x4535+x4536+x4537+x4538+x4539+x4540+x4541+x4542+x4543+x4544+x4545+x4546+x4547+x4548+x4549+x4550+x4551+x4552+x4553+x4554+x4555+x4556+x4557+x4558+x4559+x4560+x4561+x4562+x4563+x4564+x4565+x4566+x4567+x4568+x4569+x4570+x4571+x4572+x4573+x4574+x4575+x4576+x4577+x4578+x4579+x4580+x4581+x4582+x4583+x4584+x4585+x4586+x4587+x4588+x4589+x4590+x4591+x4592+x4593+x4594+x4595+x4596+x4597+x4598+x4599+x4600+x4601+x4602+x4603+x4604+x4605+x4606+x4607+x4608+x4609+x4610+x4611+x4612+x4613+x4614+x4615+x4616+x4617+x4618+x4619+x4620+x4621+x4622+x4623+x4624+x4625+x4626+x4627+x4628+x4629+x4630+x4631+x4632+x4633+x4634+x4635+x4636+x4637+x4638+x4639+x4640+x4641+x4642+x4643+x4644+x4645+x4646+x4647+x4648+x4649+x4650+x4651+x4652+x4653+x4654+x4655+x4656+x4657+x4658+x4659+x4660+x4661+x4662+x4663+x4664+x4665+x4666+x4667+x4668+x4669+x4670+x4671+x4672+x4673+x4674+x4675+x4676+x4677+x4678+x4679+x4680+x4681+x4682+x4683+x4684+x4685+x4686+x4687+x4688+x4689+x4690+x4691+x4692+x4693+x4694+x4695+x4696+x4697+x4698+x4699+x4700+x4701+x4702+x4703+x4704+x4705+x4706+x4707+x4708+x4709+x4710+x4711+x4712+x4713+x4714+x4715+x4716+x4717+x4718+x4719+x4720+x4721+x4722+x4723+x4724+x4725+x4726+x4727+x4728+x4729+x4730+x4731+x4732+x4733+x4734+x4735+x4736+x4737+x4738+x4739+x4740+x4741+x4742+x4743+x4744+x4745+x4746+x4747+x4748+x4749+x4750+x4751+x4752+x4753+x4754+x4755+x4756+x4757+x4758+x4759+x4760+x4761+x4762+x4763+x4764+x4765+x4766+x4767+x4768+x4769+x4770+x4771+x4772+x4773+x4774+x4775+x4776+x4777+x4778+x4779+x4780+x4781+x4782+x4783+x4784+x4785+x4786+x4787+x4788+x4789+x4790+x4791+x4792+x4793+x4794+x4795+x4796+x4797+x4798+x4799+x4800+x4801+x4802+x4803+x4804+x4805+x4806+x4807+x4808+x4809+x4810+x4811+x4812+x4813+x4814+x4815+x4816+x4817+x4818+x4819+x4820+x4821+x4822+x4823+x4824+x4825+x4826+x4827+x4828+x4829+x4830+x4831+x4832+x4833+x4834+x4835+x4836+x4837+x4838+x4839+x4840+x4841+x4842+x4843+x4844+x4845+x4846+x4847+x4848+x4849+x4850+x4851+x4852+x4853+x4854+x4855+x4856+x4857+x4858+x4859+x4860+x4861+x4862+x4863+x4864+x4865+x4866+x4867+x4868+x4869+x4870+x4871+x4872+x4873+x4874+x4875+x4876+x4877+x4878+x4879+x4880+x4881+x4882+x4883+x4884+x4885+x4886+x4887+x4888+x4889+x4890+x4891+x4892+x4893+x4894+x4895+x4896+x4897+x4898+x4899+x4900+x4901+x4902+x4903+x4904+x4905+x4906+x4907+x4908+x4909+x4910+x4911+x4912+x4913+x4914+x4915+x4916+x4917+x4918+x4919+x4920+x4921+x4922+x4923+x4924+x4925+x4926+x4927+x4928+x4929+x4930+x4931+x4932+x4933+x4934+x4935+x4936+x4937+x4938+x4939+x4940+x4941+x4942+x4943+x4944+x4945+x4946+x4947+x4948+x4949+x4950+x4951+x4952+x4953+x4954+x4955+x4956+x4957+x4958+x4959+x4960+x4961+x4962+x4963+x4964+x4965+x4966+x4967+x4968+x4969+x4970+x4971+x4972+x4973+x4974+x4975+x4976+x4977+x4978+x4979+x4980+x4981+x4982+x4983+x4984+x4985+x4986+x4987+x4988+x4989+x4990+x4991+x4992+x4993+x4994+x4995+x4996+x4997+x4998+x4999+x5000+x5001+x5002+x5003+x5004+x5005+x5006+x5007+x5008+x5009+x5010+x5011+x5012+x5013+x5014+x5015+x5016+x5017+x5018+x5019+x5020+x5021+x5022+x5023+x5024+x5025+x5026+x5027+x5028+x5029+x5030+x5031+x5032+x5033+x5034+x5035+x5036+x5037+x5038+x5039+x5040+x5041+x5042+x5043+x5044+x5045+x5046+x5047+x5048+x5049+x5050+x5051+x5052+x5053+x5054+x5055+x5056+x5057+x5058+x5059+x5060+x5061+x5062+x5063+x5064+x5065+x5066+x5067+x5068+x5069+x5070+x5071+x5072+x5073+x5074+x5075+x5076+x5077+x5078+x5079+x5080+x5081+x5082+x5083+x5084+x5085+x5086+x5087+x5088+x5089+x5090+x5091+x5092+x5093+x5094+x5095+x5096+x5097+x5098+x5099+x5100+x5101+x5102+x5103+x5104+x5105+x5106+x5107+x5108+x5109+x5110+x5111+x5112+x5113+x5114+x5115+x5116+x5117+x5118+x5119+x5120+x5121+x5122+x5123+x5124+x5125+x5126+x5127+x5128+x5129+x5130+x5131+x5132+x5133+x5134+x5135+x5136+x5137+x5138+x5139+x5140+x5141+x5142+x5143+x5144+x5145+x5146+x5147+x5148+x5149+x5150+x5151+x5152+x5153+x5154+x5155+x5156+x5157+x5158+x5159+x5160+x5161+x5162+x5163+x5164+x5165+x5166+x5167+x5168+x5169+x5170+x5171+x5172+x5173+x5174+x5175+x5176+x5177+x5178+x5179+x5180+x5181+x5182+x5183+x5184+x5185+x5186+x5187+x5188+x5189+x5190+x5191+x5192+x5193+x5194+x5195+x5196+x5197+x5198+x5199+x5200+x5201+x5202+x5203+x5204+x5205+x5206+x5207+x5208+x5209+x5210+x5211+x5212+x5213+x5214+x5215+x5216+x5217+x5218+x5219+x5220+x5221+x5222+x5223+x5224+x5225+x5226+x5227+x5228+x5229+x5230+x5231+x5232+x5233+x5234+x5235+x5236+x5237+x5238+x5239+x5240+x5241+x5242+x5243+x5244+x5245+x5246+x5247+x5248+x5249+x5250+x5251+x5252+x5253+x5254+x5255+x5256+x5257+x5258+x5259+x5260+x5261+x5262+x5263+x5264+x5265+x5266+x5267+x5268+x5269+x5270+x5271+x5272+x5273+x5274+x5275+x5276+x5277+x5278+x5279+x5280+x5281+x5282+x5283+x5284+x5285+x5286+x5287+x5288+x5289+x5290+x5291+x5292+x5293+x5294+x5295+x5296+x5297+x5298+x5299+x5300+x5301+x5302+x5303+x5304+x5305+x5306+x5307+x5308+x5309+x5310+x5311+x5312+x5313+x5314+x5315+x5316+x5317+x5318+x5319+x5320+x5321+x5322+x5323+x5324+x5325+x5326+x5327+x5328+x5329+x5330+x5331+x5332+x5333+x5334+x5335+x5336+x5337+x5338+x5339+x5340+x5341+x5342+x5343+x5344+x5345+x5346+x5347+x5348+x5349+x5350+x5351+x5352+x5353+x5354+x5355+x5356+x5357+x5358+x5359+x5360+x5361+x5362+x5363+x5364+x5365+x5366+x5367+x5368+x5369+x5370+x5371+x5372+x5373+x5374+x5375+x5376+x5377+x5378+x5379+x5380+x5381+x5382+x5383+x5384+x5385+x5386+x5387+x5388+x5389+x5390+x5391+x5392+x5393+x5394+x5395+x5396+x5397+x5398+x5399+x5400+x5401+x5402+x5403

#constraints
Lp_prob +=x1 + x2  >=1

Lp_prob +=x1 + x2 + x3  >=1

Lp_prob +=x1 + x2 + x3 + x4  >=1

Lp_prob +=x1 + x2 + x3 + x5  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x8 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x18 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x61 + x63  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x43 + x61 + x63  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x44 + x55 + x61  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x44 + x45 + x55 + x61  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x47 + x61 + x63  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x54 + x55 + x61  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x55 + x61  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x61  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x61 + x63  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x66 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x72  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x73  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x74  >=1

Lp_prob +=x1 + x2  >=1

Lp_prob +=x2 + x3  >=1

Lp_prob +=x2 + x3 + x4  >=1

Lp_prob +=x2 + x3 + x5  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x7  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x8 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x18 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x43 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x44 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x44 + x45 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x47 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x54 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x4 + x61  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x4 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x74  >=1

Lp_prob +=x1 + x2 + x3  >=1

Lp_prob +=x2 + x3  >=1

Lp_prob +=x3 + x4  >=1

Lp_prob +=x3 + x5  >=1

Lp_prob +=x3 + x5 + x6 + x72  >=1

Lp_prob +=x3 + x5 + x7  >=1

Lp_prob +=x3 + x5 + x6 + x8 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x72  >=1

Lp_prob +=x3 + x5 + x7 + x11  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x18 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x4 + x42 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x42 + x43 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x44 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x44 + x45 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x42 + x47 + x61 + x63  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x4 + x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x4 + x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x54 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x55 + x61  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x4 + x61  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x4 + x61 + x63  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x72  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4  >=1

Lp_prob +=x2 + x3 + x4  >=1

Lp_prob +=x3 + x4  >=1

Lp_prob +=x3 + x4 + x5  >=1

Lp_prob +=x4 + x6  >=1

Lp_prob +=x3 + x4 + x5 + x7  >=1

Lp_prob +=x4 + x6 + x8  >=1

Lp_prob +=x4 + x6 + x9  >=1

Lp_prob +=x4 + x6 + x9 + x10  >=1

Lp_prob +=x3 + x4 + x5 + x7 + x11  >=1

Lp_prob +=x4 + x6 + x8 + x12 + x13  >=1

Lp_prob +=x4 + x6 + x8 + x13  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15  >=1

Lp_prob +=x4 + x6 + x8 + x12 + x13 + x16  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x17 + x18  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x18  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x19  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x19 + x20  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x22  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x22 + x24  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x26 + x27 + x28  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x27 + x28  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x28  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x34 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x41 + x62 + x64 + x66  >=1

Lp_prob +=x4 + x42 + x61 + x63  >=1

Lp_prob +=x4 + x42 + x43 + x61 + x63  >=1

Lp_prob +=x4 + x44 + x55 + x61  >=1

Lp_prob +=x4 + x44 + x45 + x55 + x61  >=1

Lp_prob +=x4 + x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x4 + x42 + x47 + x61 + x63  >=1

Lp_prob +=x4 + x6 + x9 + x41 + x48 + x62 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x49 + x64 + x66  >=1

Lp_prob +=x4 + x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x4 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66  >=1

Lp_prob +=x4 + x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x4 + x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x4 + x54 + x55 + x61  >=1

Lp_prob +=x4 + x55 + x61  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71  >=1

Lp_prob +=x4 + x61  >=1

Lp_prob +=x4 + x6 + x9 + x62 + x64 + x66  >=1

Lp_prob +=x4 + x61 + x63  >=1

Lp_prob +=x4 + x6 + x9 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x66  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x22 + x69  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x4 + x6 + x9 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x72  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5  >=1

Lp_prob +=x2 + x3 + x5  >=1

Lp_prob +=x3 + x5  >=1

Lp_prob +=x3 + x4 + x5  >=1

Lp_prob +=x5 + x6 + x72  >=1

Lp_prob +=x5 + x7  >=1

Lp_prob +=x5 + x6 + x8 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x72  >=1

Lp_prob +=x5 + x7 + x11  >=1

Lp_prob +=x5 + x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x17  >=1

Lp_prob +=x5 + x7 + x11 + x18 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x44 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x46 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x47 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x47 + x50 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x4 + x5 + x54 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x5 + x55 + x61  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x4 + x5 + x61  >=1

Lp_prob +=x5 + x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x62 + x63 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x5 + x6 + x9 + x66 + x72  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x5 + x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x5 + x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x5 + x72  >=1

Lp_prob +=x5 + x7 + x11 + x73  >=1

Lp_prob +=x5 + x7 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x72  >=1

Lp_prob +=x4 + x6  >=1

Lp_prob +=x5 + x6 + x72  >=1

Lp_prob +=x6 + x7 + x8 + x74  >=1

Lp_prob +=x6 + x8  >=1

Lp_prob +=x6 + x9  >=1

Lp_prob +=x6 + x9 + x10  >=1

Lp_prob +=x6 + x7 + x8 + x11 + x74  >=1

Lp_prob +=x6 + x8 + x12 + x13  >=1

Lp_prob +=x6 + x8 + x13  >=1

Lp_prob +=x6 + x8 + x13 + x14  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15  >=1

Lp_prob +=x6 + x8 + x12 + x13 + x16  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x17 + x18  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x18  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x19  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x19 + x20  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x24  >=1

Lp_prob +=x6 + x9 + x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x6 + x9 + x10 + x26 + x27 + x28  >=1

Lp_prob +=x6 + x9 + x10 + x27 + x28  >=1

Lp_prob +=x6 + x9 + x10 + x28  >=1

Lp_prob +=x6 + x9 + x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x34 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x46 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x47 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x48 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x47 + x50 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66  >=1

Lp_prob +=x4 + x6 + x54 + x55 + x61  >=1

Lp_prob +=x4 + x6 + x55 + x61  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x61  >=1

Lp_prob +=x6 + x9 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x64 + x66  >=1

Lp_prob +=x6 + x9 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x6 + x9 + x66  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x69  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x6 + x9 + x66 + x71  >=1

Lp_prob +=x6 + x72  >=1

Lp_prob +=x6 + x8 + x13 + x73  >=1

Lp_prob +=x6 + x8 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7  >=1

Lp_prob +=x2 + x3 + x5 + x7  >=1

Lp_prob +=x3 + x5 + x7  >=1

Lp_prob +=x3 + x4 + x5 + x7  >=1

Lp_prob +=x5 + x7  >=1

Lp_prob +=x6 + x7 + x8 + x74  >=1

Lp_prob +=x7 + x8 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x74  >=1

Lp_prob +=x7 + x11  >=1

Lp_prob +=x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x7 + x11 + x13 + x73  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x7 + x11 + x17  >=1

Lp_prob +=x7 + x11 + x18 + x73  >=1

Lp_prob +=x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x7 + x11 + x17 + x20  >=1

Lp_prob +=x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x28 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x33 + x34 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x36 + x74  >=1

Lp_prob +=x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x24 + x38 + x73  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x48 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x51 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59 + x74  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x24 + x38 + x60 + x73  >=1

Lp_prob +=x3 + x4 + x5 + x7 + x61  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x62 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x62 + x63 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x62 + x64 + x65 + x66 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x66 + x74  >=1

Lp_prob +=x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x24 + x38 + x68 + x73  >=1

Lp_prob +=x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x7 + x8 + x10 + x28 + x71 + x74  >=1

Lp_prob +=x5 + x7 + x72  >=1

Lp_prob +=x7 + x11 + x73  >=1

Lp_prob +=x7 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x8 + x74  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x8 + x74  >=1

Lp_prob +=x3 + x5 + x7 + x8 + x74  >=1

Lp_prob +=x4 + x6 + x8  >=1

Lp_prob +=x5 + x7 + x8 + x74  >=1

Lp_prob +=x6 + x8  >=1

Lp_prob +=x7 + x8 + x74  >=1

Lp_prob +=x6 + x8 + x9  >=1

Lp_prob +=x8 + x10  >=1

Lp_prob +=x7 + x8 + x11 + x74  >=1

Lp_prob +=x8 + x12 + x13  >=1

Lp_prob +=x8 + x13  >=1

Lp_prob +=x8 + x13 + x14  >=1

Lp_prob +=x8 + x13 + x14 + x15  >=1

Lp_prob +=x8 + x12 + x13 + x16  >=1

Lp_prob +=x8 + x13 + x14 + x17 + x18  >=1

Lp_prob +=x8 + x13 + x14 + x18  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x19  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x19 + x20  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x22  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x22 + x24  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28  >=1

Lp_prob +=x8 + x10 + x27 + x28  >=1

Lp_prob +=x8 + x10 + x28  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x33 + x34  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x36  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x48  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x4 + x6 + x8 + x61  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x6 + x8 + x9 + x64 + x66  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x6 + x8 + x9 + x66  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x22 + x69  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x8 + x10 + x28 + x71  >=1

Lp_prob +=x6 + x8 + x72  >=1

Lp_prob +=x8 + x13 + x73  >=1

Lp_prob +=x8 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x72  >=1

Lp_prob +=x4 + x6 + x9  >=1

Lp_prob +=x5 + x6 + x9 + x72  >=1

Lp_prob +=x6 + x9  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x74  >=1

Lp_prob +=x6 + x8 + x9  >=1

Lp_prob +=x9 + x10  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x74  >=1

Lp_prob +=x9 + x10 + x12  >=1

Lp_prob +=x6 + x8 + x9 + x13  >=1

Lp_prob +=x9 + x10 + x12 + x14  >=1

Lp_prob +=x9 + x10 + x12 + x15 + x16  >=1

Lp_prob +=x9 + x10 + x12 + x16  >=1

Lp_prob +=x9 + x10 + x12 + x14 + x17 + x18  >=1

Lp_prob +=x9 + x10 + x12 + x14 + x18  >=1

Lp_prob +=x9 + x10 + x12 + x15 + x16 + x19  >=1

Lp_prob +=x9 + x10 + x12 + x15 + x16 + x19 + x20  >=1

Lp_prob +=x9 + x10 + x12 + x16 + x21 + x22 + x69  >=1

Lp_prob +=x9 + x10 + x12 + x16 + x22  >=1

Lp_prob +=x9 + x10 + x23 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x9 + x10 + x24 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x9 + x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x9 + x10 + x26 + x27 + x28  >=1

Lp_prob +=x9 + x10 + x27 + x28  >=1

Lp_prob +=x9 + x10 + x28  >=1

Lp_prob +=x9 + x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x9 + x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x9 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x9 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x9 + x34 + x66 + x71  >=1

Lp_prob +=x9 + x35 + x64 + x66  >=1

Lp_prob +=x9 + x35 + x36 + x64 + x66  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71  >=1

Lp_prob +=x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x46 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x47 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x48 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x35 + x36 + x49 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x47 + x50 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x48 + x51 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x54 + x55 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x55 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x35 + x36 + x49 + x56 + x64 + x66  >=1

Lp_prob +=x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66  >=1

Lp_prob +=x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71  >=1

Lp_prob +=x9 + x61 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x9 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x9 + x64 + x66  >=1

Lp_prob +=x9 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x9 + x66  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71  >=1

Lp_prob +=x9 + x10 + x12 + x16 + x22 + x69  >=1

Lp_prob +=x9 + x10 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x9 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x72  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x10  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x72  >=1

Lp_prob +=x6 + x9 + x10  >=1

Lp_prob +=x7 + x8 + x10 + x74  >=1

Lp_prob +=x8 + x10  >=1

Lp_prob +=x9 + x10  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x74  >=1

Lp_prob +=x10 + x12  >=1

Lp_prob +=x8 + x10 + x13  >=1

Lp_prob +=x10 + x12 + x14  >=1

Lp_prob +=x10 + x12 + x15 + x16  >=1

Lp_prob +=x10 + x12 + x16  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18  >=1

Lp_prob +=x10 + x12 + x14 + x18  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x20  >=1

Lp_prob +=x10 + x12 + x16 + x21 + x22 + x69  >=1

Lp_prob +=x10 + x12 + x16 + x22  >=1

Lp_prob +=x10 + x23 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x10 + x24 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x10 + x26 + x27 + x28  >=1

Lp_prob +=x10 + x27 + x28  >=1

Lp_prob +=x10 + x28  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32  >=1

Lp_prob +=x10 + x27 + x28 + x33 + x34  >=1

Lp_prob +=x10 + x27 + x28 + x34  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x36  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x48  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32 + x49  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x10 + x28 + x61 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x10 + x28 + x66 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x69  >=1

Lp_prob +=x10 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x10 + x28 + x71  >=1

Lp_prob +=x6 + x9 + x10 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x73  >=1

Lp_prob +=x8 + x10 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11  >=1

Lp_prob +=x3 + x5 + x7 + x11  >=1

Lp_prob +=x3 + x4 + x5 + x7 + x11  >=1

Lp_prob +=x5 + x7 + x11  >=1

Lp_prob +=x6 + x7 + x8 + x11 + x74  >=1

Lp_prob +=x7 + x11  >=1

Lp_prob +=x7 + x8 + x11 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x74  >=1

Lp_prob +=x11 + x12 + x13 + x73  >=1

Lp_prob +=x11 + x13 + x73  >=1

Lp_prob +=x11 + x13 + x14 + x73  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x11 + x17  >=1

Lp_prob +=x11 + x18 + x73  >=1

Lp_prob +=x11 + x18 + x19 + x73  >=1

Lp_prob +=x11 + x17 + x20  >=1

Lp_prob +=x11 + x17 + x20 + x21  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x26 + x73  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x28 + x74  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x33 + x73  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x74  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x73  >=1

Lp_prob +=x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x24 + x38 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x40 + x59 + x73  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x74  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x48 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x51 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x73  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x74  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x74  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x58 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x58 + x73  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x59 + x73  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x24 + x38 + x60 + x73  >=1

Lp_prob +=x3 + x4 + x5 + x7 + x11 + x61  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x62 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x62 + x63 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x62 + x64 + x65 + x66 + x74  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x66 + x74  >=1

Lp_prob +=x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x24 + x38 + x68 + x73  >=1

Lp_prob +=x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x28 + x71 + x74  >=1

Lp_prob +=x5 + x7 + x11 + x72  >=1

Lp_prob +=x11 + x73  >=1

Lp_prob +=x7 + x11 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x12 + x13  >=1

Lp_prob +=x5 + x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x6 + x8 + x12 + x13  >=1

Lp_prob +=x7 + x11 + x12 + x13 + x73  >=1

Lp_prob +=x8 + x12 + x13  >=1

Lp_prob +=x9 + x10 + x12  >=1

Lp_prob +=x10 + x12  >=1

Lp_prob +=x11 + x12 + x13 + x73  >=1

Lp_prob +=x12 + x13  >=1

Lp_prob +=x12 + x14  >=1

Lp_prob +=x12 + x15 + x16  >=1

Lp_prob +=x12 + x16  >=1

Lp_prob +=x12 + x14 + x17 + x18  >=1

Lp_prob +=x12 + x14 + x18  >=1

Lp_prob +=x12 + x15 + x16 + x19  >=1

Lp_prob +=x12 + x15 + x16 + x19 + x20  >=1

Lp_prob +=x12 + x16 + x21 + x22 + x69  >=1

Lp_prob +=x12 + x16 + x22  >=1

Lp_prob +=x12 + x16 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x12 + x16 + x22 + x24  >=1

Lp_prob +=x12 + x16 + x25  >=1

Lp_prob +=x12 + x16 + x25 + x26  >=1

Lp_prob +=x10 + x12 + x27 + x28  >=1

Lp_prob +=x10 + x12 + x28  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x16 + x25 + x30  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x12 + x16 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x12 + x16 + x22 + x24 + x38  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x12 + x16 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x10 + x12 + x28 + x61 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x28 + x66 + x71  >=1

Lp_prob +=x12 + x16 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x12 + x16 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x12 + x16 + x22 + x69  >=1

Lp_prob +=x12 + x16 + x22 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x28 + x71  >=1

Lp_prob +=x6 + x8 + x12 + x13 + x72  >=1

Lp_prob +=x12 + x13 + x73  >=1

Lp_prob +=x12 + x13 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x73  >=1

Lp_prob +=x6 + x8 + x13  >=1

Lp_prob +=x7 + x11 + x13 + x73  >=1

Lp_prob +=x8 + x13  >=1

Lp_prob +=x6 + x8 + x9 + x13  >=1

Lp_prob +=x8 + x10 + x13  >=1

Lp_prob +=x11 + x13 + x73  >=1

Lp_prob +=x12 + x13  >=1

Lp_prob +=x13 + x14  >=1

Lp_prob +=x13 + x14 + x15  >=1

Lp_prob +=x12 + x13 + x16  >=1

Lp_prob +=x13 + x14 + x17 + x18  >=1

Lp_prob +=x13 + x14 + x18  >=1

Lp_prob +=x13 + x14 + x15 + x19  >=1

Lp_prob +=x13 + x14 + x15 + x19 + x20  >=1

Lp_prob +=x13 + x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x22  >=1

Lp_prob +=x13 + x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24  >=1

Lp_prob +=x12 + x13 + x16 + x25  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x26  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28  >=1

Lp_prob +=x8 + x10 + x13 + x28  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x13 + x14 + x15 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x61  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x64 + x66  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x66  >=1

Lp_prob +=x13 + x14 + x15 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x8 + x10 + x13 + x28 + x71  >=1

Lp_prob +=x6 + x8 + x13 + x72  >=1

Lp_prob +=x13 + x73  >=1

Lp_prob +=x13 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x14  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x73  >=1

Lp_prob +=x8 + x13 + x14  >=1

Lp_prob +=x9 + x10 + x12 + x14  >=1

Lp_prob +=x10 + x12 + x14  >=1

Lp_prob +=x11 + x13 + x14 + x73  >=1

Lp_prob +=x12 + x14  >=1

Lp_prob +=x13 + x14  >=1

Lp_prob +=x14 + x15  >=1

Lp_prob +=x12 + x14 + x16  >=1

Lp_prob +=x14 + x17 + x18  >=1

Lp_prob +=x14 + x18  >=1

Lp_prob +=x14 + x15 + x19  >=1

Lp_prob +=x14 + x15 + x19 + x20  >=1

Lp_prob +=x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x14 + x15 + x22  >=1

Lp_prob +=x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x14 + x15 + x22 + x24  >=1

Lp_prob +=x12 + x14 + x16 + x25  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x26  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28  >=1

Lp_prob +=x10 + x12 + x14 + x28  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x14 + x15 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x14 + x15 + x22 + x24 + x38  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x14 + x15 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x61  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x66 + x71  >=1

Lp_prob +=x14 + x15 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x14 + x15 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x14 + x15 + x22 + x69  >=1

Lp_prob +=x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x71  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x72  >=1

Lp_prob +=x13 + x14 + x73  >=1

Lp_prob +=x13 + x14 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x8 + x13 + x14 + x15  >=1

Lp_prob +=x9 + x10 + x12 + x15 + x16  >=1

Lp_prob +=x10 + x12 + x15 + x16  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x73  >=1

Lp_prob +=x12 + x15 + x16  >=1

Lp_prob +=x13 + x14 + x15  >=1

Lp_prob +=x14 + x15  >=1

Lp_prob +=x15 + x16  >=1

Lp_prob +=x14 + x15 + x17 + x18  >=1

Lp_prob +=x14 + x15 + x18  >=1

Lp_prob +=x15 + x19  >=1

Lp_prob +=x15 + x19 + x20  >=1

Lp_prob +=x15 + x21 + x22 + x69  >=1

Lp_prob +=x15 + x22  >=1

Lp_prob +=x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x15 + x22 + x24  >=1

Lp_prob +=x15 + x16 + x25  >=1

Lp_prob +=x15 + x16 + x25 + x26  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x28  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30  >=1

Lp_prob +=x15 + x16 + x25 + x30  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x15 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x15 + x22 + x24 + x38  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x15 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x28 + x66 + x71  >=1

Lp_prob +=x15 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x15 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x15 + x22 + x69  >=1

Lp_prob +=x15 + x22 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x28 + x71  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x72  >=1

Lp_prob +=x13 + x14 + x15 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x12 + x13 + x16  >=1

Lp_prob +=x5 + x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x6 + x8 + x12 + x13 + x16  >=1

Lp_prob +=x7 + x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x8 + x12 + x13 + x16  >=1

Lp_prob +=x9 + x10 + x12 + x16  >=1

Lp_prob +=x10 + x12 + x16  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x73  >=1

Lp_prob +=x12 + x16  >=1

Lp_prob +=x12 + x13 + x16  >=1

Lp_prob +=x12 + x14 + x16  >=1

Lp_prob +=x15 + x16  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18  >=1

Lp_prob +=x12 + x14 + x16 + x18  >=1

Lp_prob +=x15 + x16 + x19  >=1

Lp_prob +=x15 + x16 + x19 + x20  >=1

Lp_prob +=x16 + x21 + x22 + x69  >=1

Lp_prob +=x16 + x22  >=1

Lp_prob +=x16 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x16 + x22 + x24  >=1

Lp_prob +=x16 + x25  >=1

Lp_prob +=x16 + x25 + x26  >=1

Lp_prob +=x16 + x25 + x26 + x27  >=1

Lp_prob +=x10 + x12 + x16 + x28  >=1

Lp_prob +=x16 + x25 + x29 + x30  >=1

Lp_prob +=x16 + x25 + x30  >=1

Lp_prob +=x16 + x25 + x30 + x31  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x16 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x16 + x22 + x24 + x38  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x16 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x10 + x12 + x16 + x28 + x66 + x71  >=1

Lp_prob +=x16 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x16 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x16 + x22 + x69  >=1

Lp_prob +=x16 + x22 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x16 + x28 + x71  >=1

Lp_prob +=x6 + x8 + x12 + x13 + x16 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x17 + x18  >=1

Lp_prob +=x5 + x7 + x11 + x17  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x17 + x18  >=1

Lp_prob +=x7 + x11 + x17  >=1

Lp_prob +=x8 + x13 + x14 + x17 + x18  >=1

Lp_prob +=x9 + x10 + x12 + x14 + x17 + x18  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18  >=1

Lp_prob +=x11 + x17  >=1

Lp_prob +=x12 + x14 + x17 + x18  >=1

Lp_prob +=x13 + x14 + x17 + x18  >=1

Lp_prob +=x14 + x17 + x18  >=1

Lp_prob +=x14 + x15 + x17 + x18  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18  >=1

Lp_prob +=x17 + x18  >=1

Lp_prob +=x17 + x18 + x19  >=1

Lp_prob +=x17 + x20  >=1

Lp_prob +=x17 + x20 + x21  >=1

Lp_prob +=x14 + x15 + x17 + x18 + x22  >=1

Lp_prob +=x17 + x20 + x21 + x23  >=1

Lp_prob +=x14 + x15 + x17 + x18 + x22 + x24  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x26  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x14 + x15 + x17 + x18 + x22 + x24 + x38  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x14 + x15 + x17 + x18 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x17 + x18 + x61  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x66 + x71  >=1

Lp_prob +=x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x17 + x20 + x21 + x23 + x37 + x67 + x68  >=1

Lp_prob +=x17 + x18 + x19 + x69  >=1

Lp_prob +=x17 + x18 + x19 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x71  >=1

Lp_prob +=x17 + x18 + x72 + x73 + x74  >=1

Lp_prob +=x17 + x18 + x73  >=1

Lp_prob +=x17 + x18 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x18 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x18 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x18 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x18  >=1

Lp_prob +=x5 + x7 + x11 + x18 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x18  >=1

Lp_prob +=x7 + x11 + x18 + x73  >=1

Lp_prob +=x8 + x13 + x14 + x18  >=1

Lp_prob +=x9 + x10 + x12 + x14 + x18  >=1

Lp_prob +=x10 + x12 + x14 + x18  >=1

Lp_prob +=x11 + x18 + x73  >=1

Lp_prob +=x12 + x14 + x18  >=1

Lp_prob +=x13 + x14 + x18  >=1

Lp_prob +=x14 + x18  >=1

Lp_prob +=x14 + x15 + x18  >=1

Lp_prob +=x12 + x14 + x16 + x18  >=1

Lp_prob +=x17 + x18  >=1

Lp_prob +=x18 + x19  >=1

Lp_prob +=x18 + x19 + x20  >=1

Lp_prob +=x18 + x19 + x21 + x69  >=1

Lp_prob +=x14 + x15 + x18 + x22  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x69  >=1

Lp_prob +=x14 + x15 + x18 + x22 + x24  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x26  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x69  >=1

Lp_prob +=x14 + x15 + x18 + x22 + x24 + x38  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x14 + x15 + x18 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x18 + x61  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x66 + x71  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x14 + x15 + x18 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x18 + x19 + x69  >=1

Lp_prob +=x18 + x19 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x71  >=1

Lp_prob +=x18 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x73  >=1

Lp_prob +=x18 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x19  >=1

Lp_prob +=x5 + x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x19  >=1

Lp_prob +=x7 + x11 + x18 + x19 + x73  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x19  >=1

Lp_prob +=x9 + x10 + x12 + x15 + x16 + x19  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19  >=1

Lp_prob +=x11 + x18 + x19 + x73  >=1

Lp_prob +=x12 + x15 + x16 + x19  >=1

Lp_prob +=x13 + x14 + x15 + x19  >=1

Lp_prob +=x14 + x15 + x19  >=1

Lp_prob +=x15 + x19  >=1

Lp_prob +=x15 + x16 + x19  >=1

Lp_prob +=x17 + x18 + x19  >=1

Lp_prob +=x18 + x19  >=1

Lp_prob +=x19 + x20  >=1

Lp_prob +=x19 + x21 + x69  >=1

Lp_prob +=x15 + x19 + x22  >=1

Lp_prob +=x19 + x21 + x23 + x69  >=1

Lp_prob +=x15 + x19 + x22 + x24  >=1

Lp_prob +=x15 + x16 + x19 + x25  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x28  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x19 + x21 + x23 + x37 + x69  >=1

Lp_prob +=x15 + x19 + x22 + x24 + x38  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x15 + x19 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x28 + x66 + x71  >=1

Lp_prob +=x19 + x21 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x15 + x19 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x19 + x69  >=1

Lp_prob +=x19 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x28 + x71  >=1

Lp_prob +=x18 + x19 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x73  >=1

Lp_prob +=x18 + x19 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x19 + x20  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x19 + x20  >=1

Lp_prob +=x7 + x11 + x17 + x20  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x19 + x20  >=1

Lp_prob +=x9 + x10 + x12 + x15 + x16 + x19 + x20  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x20  >=1

Lp_prob +=x11 + x17 + x20  >=1

Lp_prob +=x12 + x15 + x16 + x19 + x20  >=1

Lp_prob +=x13 + x14 + x15 + x19 + x20  >=1

Lp_prob +=x14 + x15 + x19 + x20  >=1

Lp_prob +=x15 + x19 + x20  >=1

Lp_prob +=x15 + x16 + x19 + x20  >=1

Lp_prob +=x17 + x20  >=1

Lp_prob +=x18 + x19 + x20  >=1

Lp_prob +=x19 + x20  >=1

Lp_prob +=x20 + x21  >=1

Lp_prob +=x15 + x19 + x20 + x22  >=1

Lp_prob +=x20 + x21 + x23  >=1

Lp_prob +=x15 + x19 + x20 + x22 + x24  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x20 + x28  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x20 + x21 + x23 + x37  >=1

Lp_prob +=x15 + x19 + x20 + x22 + x24 + x38  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x15 + x19 + x20 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x20 + x28 + x66 + x71  >=1

Lp_prob +=x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x20 + x21 + x23 + x37 + x67 + x68  >=1

Lp_prob +=x19 + x20 + x69  >=1

Lp_prob +=x19 + x20 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x20 + x28 + x71  >=1

Lp_prob +=x18 + x19 + x20 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x20 + x73  >=1

Lp_prob +=x18 + x19 + x20 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x7 + x11 + x17 + x20 + x21  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x9 + x10 + x12 + x16 + x21 + x22 + x69  >=1

Lp_prob +=x10 + x12 + x16 + x21 + x22 + x69  >=1

Lp_prob +=x11 + x17 + x20 + x21  >=1

Lp_prob +=x12 + x16 + x21 + x22 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x14 + x15 + x21 + x22 + x69  >=1

Lp_prob +=x15 + x21 + x22 + x69  >=1

Lp_prob +=x16 + x21 + x22 + x69  >=1

Lp_prob +=x17 + x20 + x21  >=1

Lp_prob +=x18 + x19 + x21 + x69  >=1

Lp_prob +=x19 + x21 + x69  >=1

Lp_prob +=x20 + x21  >=1

Lp_prob +=x21 + x22 + x69  >=1

Lp_prob +=x21 + x23  >=1

Lp_prob +=x21 + x23 + x24 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x70  >=1

Lp_prob +=x10 + x12 + x16 + x21 + x22 + x28 + x69  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x30 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x38 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x70  >=1

Lp_prob +=x21 + x23 + x37  >=1

Lp_prob +=x21 + x23 + x24 + x38 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x38 + x39 + x70  >=1

Lp_prob +=x21 + x23 + x37 + x40 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x48 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x51 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x38 + x39 + x56 + x58 + x70  >=1

Lp_prob +=x21 + x23 + x37 + x40 + x57 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x38 + x39 + x58 + x70  >=1

Lp_prob +=x21 + x23 + x37 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x21 + x23 + x37 + x60 + x67 + x68  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x64 + x70  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65 + x70  >=1

Lp_prob +=x10 + x12 + x16 + x21 + x22 + x28 + x66 + x69 + x71  >=1

Lp_prob +=x21 + x23 + x37 + x67  >=1

Lp_prob +=x21 + x23 + x37 + x67 + x68  >=1

Lp_prob +=x21 + x69  >=1

Lp_prob +=x21 + x23 + x70  >=1

Lp_prob +=x10 + x12 + x16 + x21 + x22 + x28 + x69 + x71  >=1

Lp_prob +=x18 + x19 + x21 + x69 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x21 + x69 + x73  >=1

Lp_prob +=x18 + x19 + x21 + x69 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x22  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x22  >=1

Lp_prob +=x9 + x10 + x12 + x16 + x22  >=1

Lp_prob +=x10 + x12 + x16 + x22  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x12 + x16 + x22  >=1

Lp_prob +=x13 + x14 + x15 + x22  >=1

Lp_prob +=x14 + x15 + x22  >=1

Lp_prob +=x15 + x22  >=1

Lp_prob +=x16 + x22  >=1

Lp_prob +=x14 + x15 + x17 + x18 + x22  >=1

Lp_prob +=x14 + x15 + x18 + x22  >=1

Lp_prob +=x15 + x19 + x22  >=1

Lp_prob +=x15 + x19 + x20 + x22  >=1

Lp_prob +=x21 + x22 + x69  >=1

Lp_prob +=x21 + x22 + x23 + x69  >=1

Lp_prob +=x22 + x24  >=1

Lp_prob +=x22 + x24 + x25  >=1

Lp_prob +=x22 + x24 + x25 + x26  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30  >=1

Lp_prob +=x22 + x24 + x25 + x30  >=1

Lp_prob +=x22 + x24 + x31 + x38  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x22 + x24 + x38  >=1

Lp_prob +=x22 + x24 + x31 + x38 + x39  >=1

Lp_prob +=x22 + x24 + x38 + x40 + x59 + x60  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x50 + x51  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x51  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x22 + x24 + x31 + x38 + x39 + x56 + x58  >=1

Lp_prob +=x22 + x24 + x38 + x40 + x57 + x59 + x60  >=1

Lp_prob +=x22 + x24 + x31 + x38 + x39 + x58  >=1

Lp_prob +=x22 + x24 + x38 + x59 + x60  >=1

Lp_prob +=x22 + x24 + x38 + x60  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x66 + x71  >=1

Lp_prob +=x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x22 + x24 + x38 + x68  >=1

Lp_prob +=x22 + x69  >=1

Lp_prob +=x22 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x71  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x72  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x7 + x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x9 + x10 + x23 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x10 + x23 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x11 + x17 + x20 + x21 + x23  >=1

Lp_prob +=x12 + x16 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x14 + x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x15 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x16 + x21 + x22 + x23 + x69  >=1

Lp_prob +=x17 + x20 + x21 + x23  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x69  >=1

Lp_prob +=x19 + x21 + x23 + x69  >=1

Lp_prob +=x20 + x21 + x23  >=1

Lp_prob +=x21 + x23  >=1

Lp_prob +=x21 + x22 + x23 + x69  >=1

Lp_prob +=x23 + x24 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x30 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x38 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x70  >=1

Lp_prob +=x23 + x37  >=1

Lp_prob +=x23 + x24 + x38 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x38 + x39 + x70  >=1

Lp_prob +=x23 + x37 + x40 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x48 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x51 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x70  >=1

Lp_prob +=x23 + x24 + x31 + x38 + x39 + x56 + x58 + x70  >=1

Lp_prob +=x23 + x37 + x40 + x57 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x23 + x24 + x31 + x38 + x39 + x58 + x70  >=1

Lp_prob +=x23 + x37 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x23 + x37 + x60 + x67 + x68  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x64 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x28 + x66 + x70 + x71  >=1

Lp_prob +=x23 + x37 + x67  >=1

Lp_prob +=x23 + x37 + x67 + x68  >=1

Lp_prob +=x21 + x23 + x69  >=1

Lp_prob +=x23 + x70  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x28 + x70 + x71  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x69 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x69 + x73  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x69 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x22 + x24  >=1

Lp_prob +=x5 + x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x24  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x22 + x24  >=1

Lp_prob +=x9 + x10 + x24 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x10 + x24 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x12 + x16 + x22 + x24  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24  >=1

Lp_prob +=x14 + x15 + x22 + x24  >=1

Lp_prob +=x15 + x22 + x24  >=1

Lp_prob +=x16 + x22 + x24  >=1

Lp_prob +=x14 + x15 + x17 + x18 + x22 + x24  >=1

Lp_prob +=x14 + x15 + x18 + x22 + x24  >=1

Lp_prob +=x15 + x19 + x22 + x24  >=1

Lp_prob +=x15 + x19 + x20 + x22 + x24  >=1

Lp_prob +=x21 + x23 + x24 + x70  >=1

Lp_prob +=x22 + x24  >=1

Lp_prob +=x23 + x24 + x70  >=1

Lp_prob +=x24 + x25  >=1

Lp_prob +=x24 + x25 + x26  >=1

Lp_prob +=x24 + x25 + x26 + x27  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x24 + x25 + x29 + x30  >=1

Lp_prob +=x24 + x25 + x30  >=1

Lp_prob +=x24 + x31 + x38  >=1

Lp_prob +=x24 + x31 + x32 + x38  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x24 + x37 + x38  >=1

Lp_prob +=x24 + x38  >=1

Lp_prob +=x24 + x31 + x38 + x39  >=1

Lp_prob +=x24 + x38 + x40 + x59 + x60  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x51  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x56 + x58  >=1

Lp_prob +=x24 + x38 + x40 + x57 + x59 + x60  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x58  >=1

Lp_prob +=x24 + x38 + x59 + x60  >=1

Lp_prob +=x24 + x38 + x60  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x66 + x71  >=1

Lp_prob +=x24 + x37 + x38 + x67  >=1

Lp_prob +=x24 + x38 + x68  >=1

Lp_prob +=x24 + x69 + x70  >=1

Lp_prob +=x24 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x71  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x24 + x72  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x9 + x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x73  >=1

Lp_prob +=x12 + x16 + x25  >=1

Lp_prob +=x12 + x13 + x16 + x25  >=1

Lp_prob +=x12 + x14 + x16 + x25  >=1

Lp_prob +=x15 + x16 + x25  >=1

Lp_prob +=x16 + x25  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25  >=1

Lp_prob +=x15 + x16 + x19 + x25  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x70  >=1

Lp_prob +=x22 + x24 + x25  >=1

Lp_prob +=x23 + x24 + x25 + x70  >=1

Lp_prob +=x24 + x25  >=1

Lp_prob +=x25 + x26  >=1

Lp_prob +=x25 + x26 + x27  >=1

Lp_prob +=x25 + x26 + x27 + x28  >=1

Lp_prob +=x25 + x29 + x30  >=1

Lp_prob +=x25 + x30  >=1

Lp_prob +=x25 + x30 + x31  >=1

Lp_prob +=x25 + x29 + x30 + x32  >=1

Lp_prob +=x25 + x29 + x30 + x33  >=1

Lp_prob +=x25 + x26 + x27 + x34  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x25 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x25 + x30 + x31 + x38  >=1

Lp_prob +=x25 + x30 + x31 + x39  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x25 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x66 + x71  >=1

Lp_prob +=x25 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x25 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x24 + x25 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x70  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x71  >=1

Lp_prob +=x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x26 + x27 + x28  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x26 + x27 + x28  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28  >=1

Lp_prob +=x9 + x10 + x26 + x27 + x28  >=1

Lp_prob +=x10 + x26 + x27 + x28  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x26 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x26  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x26  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x26  >=1

Lp_prob +=x15 + x16 + x25 + x26  >=1

Lp_prob +=x16 + x25 + x26  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x26  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x26  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x70  >=1

Lp_prob +=x24 + x25 + x26  >=1

Lp_prob +=x25 + x26  >=1

Lp_prob +=x26 + x27  >=1

Lp_prob +=x26 + x27 + x28  >=1

Lp_prob +=x26 + x29  >=1

Lp_prob +=x25 + x26 + x30  >=1

Lp_prob +=x25 + x26 + x30 + x31  >=1

Lp_prob +=x26 + x29 + x32  >=1

Lp_prob +=x26 + x29 + x33  >=1

Lp_prob +=x26 + x27 + x34  >=1

Lp_prob +=x26 + x27 + x34 + x35  >=1

Lp_prob +=x26 + x29 + x33 + x36  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x38  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x39  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x26 + x29 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x26 + x29 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x26 + x29 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x26 + x29 + x33 + x36 + x48  >=1

Lp_prob +=x26 + x29 + x32 + x49  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x26 + x27 + x28 + x66 + x71  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x70  >=1

Lp_prob +=x26 + x27 + x28 + x71  >=1

Lp_prob +=x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x26 + x73  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x27 + x28  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x27 + x28  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28  >=1

Lp_prob +=x9 + x10 + x27 + x28  >=1

Lp_prob +=x10 + x27 + x28  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27  >=1

Lp_prob +=x16 + x25 + x26 + x27  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27  >=1

Lp_prob +=x25 + x26 + x27  >=1

Lp_prob +=x26 + x27  >=1

Lp_prob +=x27 + x28  >=1

Lp_prob +=x26 + x27 + x29  >=1

Lp_prob +=x25 + x26 + x27 + x30  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31  >=1

Lp_prob +=x26 + x27 + x29 + x32  >=1

Lp_prob +=x27 + x33 + x34  >=1

Lp_prob +=x27 + x34  >=1

Lp_prob +=x27 + x34 + x35  >=1

Lp_prob +=x27 + x34 + x35 + x36  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x38  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x39  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x27 + x34 + x35 + x41  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x48  >=1

Lp_prob +=x26 + x27 + x29 + x32 + x49  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x26 + x27 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x26 + x27 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x26 + x27 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x62  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x27 + x34 + x35 + x64  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x27 + x28 + x66 + x71  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x70  >=1

Lp_prob +=x27 + x28 + x71  >=1

Lp_prob +=x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x28  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x28  >=1

Lp_prob +=x7 + x8 + x10 + x28 + x74  >=1

Lp_prob +=x8 + x10 + x28  >=1

Lp_prob +=x9 + x10 + x28  >=1

Lp_prob +=x10 + x28  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x28 + x74  >=1

Lp_prob +=x10 + x12 + x28  >=1

Lp_prob +=x8 + x10 + x13 + x28  >=1

Lp_prob +=x10 + x12 + x14 + x28  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x28  >=1

Lp_prob +=x10 + x12 + x16 + x28  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x28  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x20 + x28  >=1

Lp_prob +=x10 + x12 + x16 + x21 + x22 + x28 + x69  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28  >=1

Lp_prob +=x25 + x26 + x27 + x28  >=1

Lp_prob +=x26 + x27 + x28  >=1

Lp_prob +=x27 + x28  >=1

Lp_prob +=x26 + x27 + x28 + x29  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32  >=1

Lp_prob +=x27 + x28 + x33 + x34  >=1

Lp_prob +=x27 + x28 + x34  >=1

Lp_prob +=x27 + x28 + x34 + x35  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x36  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x38  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x39  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x48  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32 + x49  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x28 + x61 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x28 + x64 + x66 + x71  >=1

Lp_prob +=x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x28 + x66 + x71  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x69  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x28 + x71  >=1

Lp_prob +=x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x28 + x73  >=1

Lp_prob +=x8 + x10 + x28 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x9 + x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30  >=1

Lp_prob +=x16 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30  >=1

Lp_prob +=x25 + x29 + x30  >=1

Lp_prob +=x26 + x29  >=1

Lp_prob +=x26 + x27 + x29  >=1

Lp_prob +=x26 + x27 + x28 + x29  >=1

Lp_prob +=x29 + x30  >=1

Lp_prob +=x29 + x31 + x32  >=1

Lp_prob +=x29 + x32  >=1

Lp_prob +=x29 + x33  >=1

Lp_prob +=x29 + x33 + x34  >=1

Lp_prob +=x29 + x33 + x35 + x36  >=1

Lp_prob +=x29 + x33 + x36  >=1

Lp_prob +=x29 + x31 + x32 + x37 + x38  >=1

Lp_prob +=x29 + x31 + x32 + x38  >=1

Lp_prob +=x29 + x31 + x32 + x39  >=1

Lp_prob +=x29 + x31 + x32 + x39 + x40 + x59  >=1

Lp_prob +=x29 + x33 + x36 + x41 + x48  >=1

Lp_prob +=x29 + x33 + x36 + x42 + x47 + x48  >=1

Lp_prob +=x29 + x33 + x36 + x43 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x33 + x36 + x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x29 + x33 + x36 + x48  >=1

Lp_prob +=x29 + x32 + x49  >=1

Lp_prob +=x29 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x29 + x32 + x49 + x51  >=1

Lp_prob +=x29 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x29 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x29 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x29 + x33 + x36 + x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x29 + x32 + x49 + x56  >=1

Lp_prob +=x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x29 + x31 + x32 + x39 + x58  >=1

Lp_prob +=x29 + x31 + x32 + x39 + x59  >=1

Lp_prob +=x29 + x31 + x32 + x38 + x60  >=1

Lp_prob +=x29 + x33 + x36 + x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x29 + x33 + x36 + x41 + x48 + x62  >=1

Lp_prob +=x29 + x33 + x36 + x42 + x47 + x48 + x63  >=1

Lp_prob +=x29 + x33 + x35 + x36 + x64  >=1

Lp_prob +=x29 + x33 + x36 + x41 + x48 + x62 + x65  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x66 + x71  >=1

Lp_prob +=x29 + x31 + x32 + x37 + x38 + x67  >=1

Lp_prob +=x29 + x31 + x32 + x38 + x68  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x70  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x71  >=1

Lp_prob +=x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x73  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x5 + x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x9 + x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x30  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30  >=1

Lp_prob +=x15 + x16 + x25 + x30  >=1

Lp_prob +=x16 + x25 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x30 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x30  >=1

Lp_prob +=x23 + x24 + x25 + x30 + x70  >=1

Lp_prob +=x24 + x25 + x30  >=1

Lp_prob +=x25 + x30  >=1

Lp_prob +=x25 + x26 + x30  >=1

Lp_prob +=x25 + x26 + x27 + x30  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30  >=1

Lp_prob +=x29 + x30  >=1

Lp_prob +=x30 + x31  >=1

Lp_prob +=x29 + x30 + x32  >=1

Lp_prob +=x29 + x30 + x33  >=1

Lp_prob +=x29 + x30 + x33 + x34  >=1

Lp_prob +=x29 + x30 + x33 + x35 + x36  >=1

Lp_prob +=x29 + x30 + x33 + x36  >=1

Lp_prob +=x30 + x31 + x37 + x38  >=1

Lp_prob +=x30 + x31 + x38  >=1

Lp_prob +=x30 + x31 + x39  >=1

Lp_prob +=x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x41 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x42 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x43 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x29 + x30 + x32 + x49  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x30 + x31 + x39 + x58  >=1

Lp_prob +=x30 + x31 + x39 + x59  >=1

Lp_prob +=x30 + x31 + x38 + x60  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x41 + x48 + x62  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x42 + x47 + x48 + x63  >=1

Lp_prob +=x29 + x30 + x33 + x35 + x36 + x64  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x41 + x48 + x62 + x65  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x66 + x71  >=1

Lp_prob +=x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x30 + x31 + x38 + x68  >=1

Lp_prob +=x24 + x25 + x30 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x30 + x70  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x71  >=1

Lp_prob +=x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31  >=1

Lp_prob +=x16 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x38 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x38  >=1

Lp_prob +=x23 + x24 + x31 + x38 + x70  >=1

Lp_prob +=x24 + x31 + x38  >=1

Lp_prob +=x25 + x30 + x31  >=1

Lp_prob +=x25 + x26 + x30 + x31  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31  >=1

Lp_prob +=x29 + x31 + x32  >=1

Lp_prob +=x30 + x31  >=1

Lp_prob +=x31 + x32  >=1

Lp_prob +=x31 + x32 + x33  >=1

Lp_prob +=x31 + x32 + x33 + x34  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x49  >=1

Lp_prob +=x31 + x32 + x36 + x49  >=1

Lp_prob +=x31 + x37 + x38  >=1

Lp_prob +=x31 + x38  >=1

Lp_prob +=x31 + x39  >=1

Lp_prob +=x31 + x39 + x40 + x59  >=1

Lp_prob +=x31 + x32 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x49  >=1

Lp_prob +=x31 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x31 + x32 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x31 + x39 + x56 + x58  >=1

Lp_prob +=x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x31 + x39 + x58  >=1

Lp_prob +=x31 + x39 + x59  >=1

Lp_prob +=x31 + x38 + x60  >=1

Lp_prob +=x31 + x32 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x31 + x32 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x49 + x64  >=1

Lp_prob +=x31 + x32 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x31 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x38 + x68  >=1

Lp_prob +=x24 + x31 + x38 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32  >=1

Lp_prob +=x9 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38  >=1

Lp_prob +=x25 + x29 + x30 + x32  >=1

Lp_prob +=x26 + x29 + x32  >=1

Lp_prob +=x26 + x27 + x29 + x32  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32  >=1

Lp_prob +=x29 + x32  >=1

Lp_prob +=x29 + x30 + x32  >=1

Lp_prob +=x31 + x32  >=1

Lp_prob +=x32 + x33  >=1

Lp_prob +=x32 + x33 + x34  >=1

Lp_prob +=x32 + x35 + x36 + x49  >=1

Lp_prob +=x32 + x36 + x49  >=1

Lp_prob +=x31 + x32 + x37 + x38  >=1

Lp_prob +=x31 + x32 + x38  >=1

Lp_prob +=x31 + x32 + x39  >=1

Lp_prob +=x31 + x32 + x39 + x40 + x59  >=1

Lp_prob +=x32 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x32 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x32 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x32 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x32 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x32 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x32 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x32 + x48 + x49 + x51  >=1

Lp_prob +=x32 + x49  >=1

Lp_prob +=x32 + x49 + x50 + x51  >=1

Lp_prob +=x32 + x49 + x51  >=1

Lp_prob +=x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x32 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x32 + x49 + x56  >=1

Lp_prob +=x32 + x49 + x56 + x57  >=1

Lp_prob +=x31 + x32 + x39 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x60  >=1

Lp_prob +=x32 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x32 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x32 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x32 + x35 + x36 + x49 + x64  >=1

Lp_prob +=x32 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x68  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x70  >=1

Lp_prob +=x32 + x33 + x34 + x71  >=1

Lp_prob +=x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x73  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x33 + x34 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x33 + x34  >=1

Lp_prob +=x9 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x10 + x27 + x28 + x33 + x34  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x33 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33  >=1

Lp_prob +=x25 + x29 + x30 + x33  >=1

Lp_prob +=x26 + x29 + x33  >=1

Lp_prob +=x27 + x33 + x34  >=1

Lp_prob +=x27 + x28 + x33 + x34  >=1

Lp_prob +=x29 + x33  >=1

Lp_prob +=x29 + x30 + x33  >=1

Lp_prob +=x31 + x32 + x33  >=1

Lp_prob +=x32 + x33  >=1

Lp_prob +=x33 + x34  >=1

Lp_prob +=x33 + x35 + x36  >=1

Lp_prob +=x33 + x36  >=1

Lp_prob +=x31 + x32 + x33 + x37 + x38  >=1

Lp_prob +=x31 + x32 + x33 + x38  >=1

Lp_prob +=x31 + x32 + x33 + x39  >=1

Lp_prob +=x31 + x32 + x33 + x39 + x40 + x59  >=1

Lp_prob +=x33 + x36 + x41 + x48  >=1

Lp_prob +=x33 + x36 + x42 + x47 + x48  >=1

Lp_prob +=x33 + x36 + x43 + x46 + x47 + x48  >=1

Lp_prob +=x33 + x36 + x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x33 + x36 + x47 + x48  >=1

Lp_prob +=x33 + x36 + x48  >=1

Lp_prob +=x33 + x36 + x49  >=1

Lp_prob +=x33 + x36 + x47 + x48 + x50  >=1

Lp_prob +=x33 + x36 + x48 + x51  >=1

Lp_prob +=x33 + x36 + x46 + x47 + x48 + x52  >=1

Lp_prob +=x33 + x36 + x45 + x46 + x47 + x48 + x53  >=1

Lp_prob +=x33 + x36 + x45 + x46 + x47 + x48 + x53 + x54  >=1

Lp_prob +=x33 + x36 + x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x33 + x36 + x49 + x56  >=1

Lp_prob +=x33 + x36 + x49 + x56 + x57  >=1

Lp_prob +=x31 + x32 + x33 + x39 + x58  >=1

Lp_prob +=x31 + x32 + x33 + x39 + x59  >=1

Lp_prob +=x31 + x32 + x33 + x38 + x60  >=1

Lp_prob +=x33 + x36 + x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x33 + x36 + x41 + x48 + x62  >=1

Lp_prob +=x33 + x36 + x42 + x47 + x48 + x63  >=1

Lp_prob +=x33 + x35 + x36 + x64  >=1

Lp_prob +=x33 + x36 + x41 + x48 + x62 + x65  >=1

Lp_prob +=x33 + x34 + x66 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x32 + x33 + x38 + x68  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x70  >=1

Lp_prob +=x33 + x34 + x71  >=1

Lp_prob +=x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x33 + x34 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x34 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x34 + x66 + x71  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34  >=1

Lp_prob +=x9 + x34 + x66 + x71  >=1

Lp_prob +=x10 + x27 + x28 + x34  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34  >=1

Lp_prob +=x25 + x26 + x27 + x34  >=1

Lp_prob +=x26 + x27 + x34  >=1

Lp_prob +=x27 + x34  >=1

Lp_prob +=x27 + x28 + x34  >=1

Lp_prob +=x29 + x33 + x34  >=1

Lp_prob +=x29 + x30 + x33 + x34  >=1

Lp_prob +=x31 + x32 + x33 + x34  >=1

Lp_prob +=x32 + x33 + x34  >=1

Lp_prob +=x33 + x34  >=1

Lp_prob +=x34 + x35  >=1

Lp_prob +=x34 + x35 + x36  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x40 + x59  >=1

Lp_prob +=x34 + x35 + x41  >=1

Lp_prob +=x34 + x35 + x41 + x42  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x34 + x35 + x41 + x48  >=1

Lp_prob +=x34 + x35 + x36 + x49  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x34 + x35 + x41 + x48 + x51  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x56  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x56 + x57  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x58  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x59  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x60  >=1

Lp_prob +=x34 + x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x34 + x35 + x41 + x62  >=1

Lp_prob +=x34 + x35 + x41 + x62 + x63  >=1

Lp_prob +=x34 + x35 + x64  >=1

Lp_prob +=x34 + x35 + x41 + x62 + x65  >=1

Lp_prob +=x34 + x66 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x70  >=1

Lp_prob +=x34 + x71  >=1

Lp_prob +=x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x9 + x35 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35  >=1

Lp_prob +=x26 + x27 + x34 + x35  >=1

Lp_prob +=x27 + x34 + x35  >=1

Lp_prob +=x27 + x28 + x34 + x35  >=1

Lp_prob +=x29 + x33 + x35 + x36  >=1

Lp_prob +=x29 + x30 + x33 + x35 + x36  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x49  >=1

Lp_prob +=x32 + x35 + x36 + x49  >=1

Lp_prob +=x33 + x35 + x36  >=1

Lp_prob +=x34 + x35  >=1

Lp_prob +=x35 + x36  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x37 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x39 + x49  >=1

Lp_prob +=x35 + x36 + x40 + x49 + x56 + x58  >=1

Lp_prob +=x35 + x41  >=1

Lp_prob +=x35 + x41 + x42  >=1

Lp_prob +=x35 + x41 + x42 + x43  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x35 + x41 + x42 + x47  >=1

Lp_prob +=x35 + x41 + x48  >=1

Lp_prob +=x35 + x36 + x49  >=1

Lp_prob +=x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x35 + x41 + x48 + x51  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x35 + x36 + x49 + x56  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x57  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x39 + x49 + x59  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x60  >=1

Lp_prob +=x35 + x41 + x61 + x62 + x63  >=1

Lp_prob +=x35 + x41 + x62  >=1

Lp_prob +=x35 + x41 + x62 + x63  >=1

Lp_prob +=x35 + x64  >=1

Lp_prob +=x35 + x41 + x62 + x65  >=1

Lp_prob +=x35 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x37 + x38 + x49 + x67  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x70  >=1

Lp_prob +=x34 + x35 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x36 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x36  >=1

Lp_prob +=x9 + x35 + x36 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x36  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36  >=1

Lp_prob +=x26 + x29 + x33 + x36  >=1

Lp_prob +=x27 + x34 + x35 + x36  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x36  >=1

Lp_prob +=x29 + x33 + x36  >=1

Lp_prob +=x29 + x30 + x33 + x36  >=1

Lp_prob +=x31 + x32 + x36 + x49  >=1

Lp_prob +=x32 + x36 + x49  >=1

Lp_prob +=x33 + x36  >=1

Lp_prob +=x34 + x35 + x36  >=1

Lp_prob +=x35 + x36  >=1

Lp_prob +=x31 + x32 + x36 + x37 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x36 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x36 + x39 + x49  >=1

Lp_prob +=x36 + x40 + x49 + x56 + x58  >=1

Lp_prob +=x36 + x41 + x48  >=1

Lp_prob +=x36 + x42 + x47 + x48  >=1

Lp_prob +=x36 + x43 + x46 + x47 + x48  >=1

Lp_prob +=x36 + x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x36 + x46 + x47 + x48  >=1

Lp_prob +=x36 + x47 + x48  >=1

Lp_prob +=x36 + x48  >=1

Lp_prob +=x36 + x49  >=1

Lp_prob +=x36 + x47 + x48 + x50  >=1

Lp_prob +=x36 + x48 + x51  >=1

Lp_prob +=x36 + x46 + x47 + x48 + x52  >=1

Lp_prob +=x36 + x45 + x46 + x47 + x48 + x53  >=1

Lp_prob +=x36 + x45 + x46 + x47 + x48 + x53 + x54  >=1

Lp_prob +=x36 + x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x36 + x49 + x56  >=1

Lp_prob +=x36 + x49 + x56 + x57  >=1

Lp_prob +=x36 + x49 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x36 + x39 + x49 + x59  >=1

Lp_prob +=x31 + x32 + x36 + x38 + x49 + x60  >=1

Lp_prob +=x36 + x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x36 + x41 + x48 + x62  >=1

Lp_prob +=x36 + x42 + x47 + x48 + x63  >=1

Lp_prob +=x35 + x36 + x64  >=1

Lp_prob +=x36 + x41 + x48 + x62 + x65  >=1

Lp_prob +=x35 + x36 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x36 + x37 + x38 + x49 + x67  >=1

Lp_prob +=x31 + x32 + x36 + x38 + x49 + x68  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x70  >=1

Lp_prob +=x34 + x35 + x36 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x36 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71  >=1

Lp_prob +=x7 + x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x11 + x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x12 + x16 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x14 + x15 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x15 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x16 + x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x17 + x20 + x21 + x23 + x37  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x69  >=1

Lp_prob +=x19 + x21 + x23 + x37 + x69  >=1

Lp_prob +=x20 + x21 + x23 + x37  >=1

Lp_prob +=x21 + x23 + x37  >=1

Lp_prob +=x21 + x22 + x23 + x37 + x69  >=1

Lp_prob +=x23 + x37  >=1

Lp_prob +=x24 + x37 + x38  >=1

Lp_prob +=x25 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x37 + x38  >=1

Lp_prob +=x29 + x31 + x32 + x37 + x38  >=1

Lp_prob +=x30 + x31 + x37 + x38  >=1

Lp_prob +=x31 + x37 + x38  >=1

Lp_prob +=x31 + x32 + x37 + x38  >=1

Lp_prob +=x31 + x32 + x33 + x37 + x38  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x37 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x36 + x37 + x38 + x49  >=1

Lp_prob +=x37 + x38  >=1

Lp_prob +=x31 + x37 + x38 + x39  >=1

Lp_prob +=x37 + x40 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x31 + x37 + x38 + x39 + x56 + x58  >=1

Lp_prob +=x37 + x40 + x57 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x31 + x37 + x38 + x39 + x58  >=1

Lp_prob +=x37 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x37 + x60 + x67 + x68  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x37 + x38 + x49 + x64  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71  >=1

Lp_prob +=x37 + x67  >=1

Lp_prob +=x37 + x67 + x68  >=1

Lp_prob +=x21 + x23 + x37 + x69  >=1

Lp_prob +=x23 + x37 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x69 + x73  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x69 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x24 + x38 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x24 + x38 + x73  >=1

Lp_prob +=x12 + x16 + x22 + x24 + x38  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38  >=1

Lp_prob +=x14 + x15 + x22 + x24 + x38  >=1

Lp_prob +=x15 + x22 + x24 + x38  >=1

Lp_prob +=x16 + x22 + x24 + x38  >=1

Lp_prob +=x14 + x15 + x17 + x18 + x22 + x24 + x38  >=1

Lp_prob +=x14 + x15 + x18 + x22 + x24 + x38  >=1

Lp_prob +=x15 + x19 + x22 + x24 + x38  >=1

Lp_prob +=x15 + x19 + x20 + x22 + x24 + x38  >=1

Lp_prob +=x21 + x23 + x24 + x38 + x70  >=1

Lp_prob +=x22 + x24 + x38  >=1

Lp_prob +=x23 + x24 + x38 + x70  >=1

Lp_prob +=x24 + x38  >=1

Lp_prob +=x25 + x30 + x31 + x38  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x38  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x38  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x38  >=1

Lp_prob +=x29 + x31 + x32 + x38  >=1

Lp_prob +=x30 + x31 + x38  >=1

Lp_prob +=x31 + x38  >=1

Lp_prob +=x31 + x32 + x38  >=1

Lp_prob +=x31 + x32 + x33 + x38  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x36 + x38 + x49  >=1

Lp_prob +=x37 + x38  >=1

Lp_prob +=x31 + x38 + x39  >=1

Lp_prob +=x38 + x40 + x59 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x38 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x38 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x38 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x31 + x38 + x39 + x56 + x58  >=1

Lp_prob +=x38 + x40 + x57 + x59 + x60  >=1

Lp_prob +=x31 + x38 + x39 + x58  >=1

Lp_prob +=x38 + x59 + x60  >=1

Lp_prob +=x38 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x64  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x66 + x71  >=1

Lp_prob +=x37 + x38 + x67  >=1

Lp_prob +=x38 + x68  >=1

Lp_prob +=x24 + x38 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x38 + x39 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x38 + x39  >=1

Lp_prob +=x23 + x24 + x31 + x38 + x39 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39  >=1

Lp_prob +=x25 + x30 + x31 + x39  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x39  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x39  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x39  >=1

Lp_prob +=x29 + x31 + x32 + x39  >=1

Lp_prob +=x30 + x31 + x39  >=1

Lp_prob +=x31 + x39  >=1

Lp_prob +=x31 + x32 + x39  >=1

Lp_prob +=x31 + x32 + x33 + x39  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x39 + x49  >=1

Lp_prob +=x31 + x32 + x36 + x39 + x49  >=1

Lp_prob +=x31 + x37 + x38 + x39  >=1

Lp_prob +=x31 + x38 + x39  >=1

Lp_prob +=x39 + x40 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x39 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x39 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x39 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x39 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x49  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x31 + x32 + x39 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x39 + x56 + x58  >=1

Lp_prob +=x39 + x56 + x57 + x58  >=1

Lp_prob +=x39 + x58  >=1

Lp_prob +=x39 + x59  >=1

Lp_prob +=x39 + x59 + x60  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x39 + x49 + x64  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x66 + x71  >=1

Lp_prob +=x39 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x39 + x59 + x60 + x68  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x40 + x59 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x21 + x23 + x37 + x40 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x22 + x24 + x38 + x40 + x59 + x60  >=1

Lp_prob +=x23 + x37 + x40 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x24 + x38 + x40 + x59 + x60  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x29 + x31 + x32 + x39 + x40 + x59  >=1

Lp_prob +=x30 + x31 + x39 + x40 + x59  >=1

Lp_prob +=x31 + x39 + x40 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x40 + x59  >=1

Lp_prob +=x31 + x32 + x33 + x39 + x40 + x59  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x40 + x59  >=1

Lp_prob +=x35 + x36 + x40 + x49 + x56 + x58  >=1

Lp_prob +=x36 + x40 + x49 + x56 + x58  >=1

Lp_prob +=x37 + x40 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x38 + x40 + x59 + x60  >=1

Lp_prob +=x39 + x40 + x59  >=1

Lp_prob +=x40 + x41 + x48 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x40 + x42 + x47 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x40 + x43 + x46 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x40 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x40 + x45 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x40 + x46 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x40 + x47 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x40 + x48 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x40 + x49 + x56 + x58  >=1

Lp_prob +=x40 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x40 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x40 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x40 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x40 + x49 + x50 + x51 + x52 + x53 + x54 + x56 + x58  >=1

Lp_prob +=x40 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x56 + x58  >=1

Lp_prob +=x40 + x56 + x58  >=1

Lp_prob +=x40 + x57  >=1

Lp_prob +=x40 + x58  >=1

Lp_prob +=x40 + x59  >=1

Lp_prob +=x40 + x59 + x60  >=1

Lp_prob +=x40 + x42 + x47 + x49 + x50 + x51 + x56 + x58 + x61 + x63  >=1

Lp_prob +=x40 + x41 + x48 + x49 + x51 + x56 + x58 + x62  >=1

Lp_prob +=x40 + x42 + x47 + x49 + x50 + x51 + x56 + x58 + x63  >=1

Lp_prob +=x35 + x36 + x40 + x49 + x56 + x58 + x64  >=1

Lp_prob +=x40 + x41 + x48 + x49 + x51 + x56 + x58 + x62 + x65  >=1

Lp_prob +=x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x40 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x40 + x59 + x60 + x68  >=1

Lp_prob +=x24 + x38 + x40 + x59 + x60 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x40 + x59 + x60 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x40 + x59 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x40 + x59 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x41 + x62 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x9 + x41 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41  >=1

Lp_prob +=x27 + x34 + x35 + x41  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41  >=1

Lp_prob +=x29 + x33 + x36 + x41 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x41 + x48  >=1

Lp_prob +=x31 + x32 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x32 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x33 + x36 + x41 + x48  >=1

Lp_prob +=x34 + x35 + x41  >=1

Lp_prob +=x35 + x41  >=1

Lp_prob +=x36 + x41 + x48  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51  >=1

Lp_prob +=x40 + x41 + x48 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x41 + x42  >=1

Lp_prob +=x41 + x42 + x43  >=1

Lp_prob +=x41 + x42 + x43 + x44  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x41 + x42 + x43 + x46  >=1

Lp_prob +=x41 + x42 + x47  >=1

Lp_prob +=x41 + x48  >=1

Lp_prob +=x41 + x48 + x49 + x51  >=1

Lp_prob +=x41 + x42 + x47 + x50  >=1

Lp_prob +=x41 + x48 + x51  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x57  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x60  >=1

Lp_prob +=x41 + x61 + x62 + x63  >=1

Lp_prob +=x41 + x62  >=1

Lp_prob +=x41 + x62 + x63  >=1

Lp_prob +=x41 + x62 + x64  >=1

Lp_prob +=x41 + x62 + x65  >=1

Lp_prob +=x41 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x42 + x61 + x63  >=1

Lp_prob +=x4 + x42 + x61 + x63  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x9 + x41 + x42 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42  >=1

Lp_prob +=x29 + x33 + x36 + x42 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x42 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x32 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x33 + x36 + x42 + x47 + x48  >=1

Lp_prob +=x34 + x35 + x41 + x42  >=1

Lp_prob +=x35 + x41 + x42  >=1

Lp_prob +=x36 + x42 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x40 + x42 + x47 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x41 + x42  >=1

Lp_prob +=x42 + x43  >=1

Lp_prob +=x42 + x43 + x44  >=1

Lp_prob +=x42 + x43 + x44 + x45  >=1

Lp_prob +=x42 + x43 + x46  >=1

Lp_prob +=x42 + x47  >=1

Lp_prob +=x42 + x47 + x48  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x42 + x47 + x50  >=1

Lp_prob +=x42 + x47 + x50 + x51  >=1

Lp_prob +=x42 + x43 + x46 + x52  >=1

Lp_prob +=x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x42 + x43 + x44 + x55  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x57  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x60  >=1

Lp_prob +=x42 + x61 + x63  >=1

Lp_prob +=x41 + x42 + x62  >=1

Lp_prob +=x42 + x63  >=1

Lp_prob +=x41 + x42 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x43 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x43 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x42 + x43 + x61 + x63  >=1

Lp_prob +=x4 + x42 + x43 + x61 + x63  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x29 + x33 + x36 + x43 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x43 + x46 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x32 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x33 + x36 + x43 + x46 + x47 + x48  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43  >=1

Lp_prob +=x35 + x41 + x42 + x43  >=1

Lp_prob +=x36 + x43 + x46 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x38 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x39 + x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x40 + x43 + x46 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x43  >=1

Lp_prob +=x42 + x43  >=1

Lp_prob +=x43 + x44  >=1

Lp_prob +=x43 + x44 + x45  >=1

Lp_prob +=x43 + x46  >=1

Lp_prob +=x43 + x46 + x47  >=1

Lp_prob +=x43 + x46 + x47 + x48  >=1

Lp_prob +=x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x43 + x46 + x50 + x52  >=1

Lp_prob +=x43 + x46 + x50 + x51 + x52  >=1

Lp_prob +=x43 + x46 + x52  >=1

Lp_prob +=x43 + x44 + x45 + x53  >=1

Lp_prob +=x43 + x44 + x54 + x55  >=1

Lp_prob +=x43 + x44 + x55  >=1

Lp_prob +=x43 + x46 + x49 + x50 + x51 + x52 + x56  >=1

Lp_prob +=x43 + x46 + x49 + x50 + x51 + x52 + x56 + x57  >=1

Lp_prob +=x43 + x46 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x43 + x46 + x49 + x50 + x51 + x52 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x43 + x46 + x49 + x50 + x51 + x52 + x60  >=1

Lp_prob +=x42 + x43 + x61 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x62  >=1

Lp_prob +=x42 + x43 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x43 + x46 + x49 + x50 + x51 + x52 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x43 + x46 + x49 + x50 + x51 + x52 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x44 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x44 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x44 + x55 + x61  >=1

Lp_prob +=x4 + x44 + x55 + x61  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x44 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x29 + x33 + x36 + x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x32 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x33 + x36 + x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44  >=1

Lp_prob +=x36 + x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x39 + x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x40 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x43 + x44  >=1

Lp_prob +=x42 + x43 + x44  >=1

Lp_prob +=x43 + x44  >=1

Lp_prob +=x44 + x45  >=1

Lp_prob +=x44 + x45 + x46  >=1

Lp_prob +=x44 + x45 + x46 + x47  >=1

Lp_prob +=x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x44 + x45 + x50 + x52 + x53  >=1

Lp_prob +=x44 + x45 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x44 + x45 + x52 + x53  >=1

Lp_prob +=x44 + x45 + x53  >=1

Lp_prob +=x44 + x54 + x55  >=1

Lp_prob +=x44 + x55  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x56  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x56 + x57  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x60  >=1

Lp_prob +=x44 + x55 + x61  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x62  >=1

Lp_prob +=x42 + x43 + x44 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x44 + x45 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x44 + x45 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x44 + x45 + x55 + x61  >=1

Lp_prob +=x4 + x44 + x45 + x55 + x61  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x74  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x26 + x29 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x29 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x32 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x33 + x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x36 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x38 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x39 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x40 + x45 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45  >=1

Lp_prob +=x42 + x43 + x44 + x45  >=1

Lp_prob +=x43 + x44 + x45  >=1

Lp_prob +=x44 + x45  >=1

Lp_prob +=x45 + x46  >=1

Lp_prob +=x45 + x46 + x47  >=1

Lp_prob +=x45 + x46 + x47 + x48  >=1

Lp_prob +=x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x45 + x50 + x52 + x53  >=1

Lp_prob +=x45 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x45 + x52 + x53  >=1

Lp_prob +=x45 + x53  >=1

Lp_prob +=x45 + x53 + x54  >=1

Lp_prob +=x44 + x45 + x55  >=1

Lp_prob +=x45 + x49 + x50 + x51 + x52 + x53 + x56  >=1

Lp_prob +=x45 + x49 + x50 + x51 + x52 + x53 + x56 + x57  >=1

Lp_prob +=x45 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x45 + x49 + x50 + x51 + x52 + x53 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x45 + x49 + x50 + x51 + x52 + x53 + x60  >=1

Lp_prob +=x44 + x45 + x55 + x61  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x62  >=1

Lp_prob +=x42 + x43 + x44 + x45 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x45 + x49 + x50 + x51 + x52 + x53 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x45 + x49 + x50 + x51 + x52 + x53 + x68  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x45 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x4 + x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x46 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x46 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x46 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x74  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x26 + x29 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x29 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x32 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x33 + x36 + x46 + x47 + x48  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x46  >=1

Lp_prob +=x36 + x46 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x38 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x39 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x40 + x46 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x43 + x46  >=1

Lp_prob +=x42 + x43 + x46  >=1

Lp_prob +=x43 + x46  >=1

Lp_prob +=x44 + x45 + x46  >=1

Lp_prob +=x45 + x46  >=1

Lp_prob +=x46 + x47  >=1

Lp_prob +=x46 + x47 + x48  >=1

Lp_prob +=x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x46 + x50 + x52  >=1

Lp_prob +=x46 + x50 + x51 + x52  >=1

Lp_prob +=x46 + x52  >=1

Lp_prob +=x45 + x46 + x53  >=1

Lp_prob +=x45 + x46 + x53 + x54  >=1

Lp_prob +=x44 + x45 + x46 + x55  >=1

Lp_prob +=x46 + x49 + x50 + x51 + x52 + x56  >=1

Lp_prob +=x46 + x49 + x50 + x51 + x52 + x56 + x57  >=1

Lp_prob +=x46 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x46 + x49 + x50 + x51 + x52 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x46 + x49 + x50 + x51 + x52 + x60  >=1

Lp_prob +=x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x62  >=1

Lp_prob +=x42 + x43 + x46 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x46 + x49 + x50 + x51 + x52 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x46 + x49 + x50 + x51 + x52 + x68  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x46 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x46 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x47 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x47 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x42 + x47 + x61 + x63  >=1

Lp_prob +=x4 + x42 + x47 + x61 + x63  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x47 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x47 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x9 + x41 + x42 + x47 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x26 + x29 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x29 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x32 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x33 + x36 + x47 + x48  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x47  >=1

Lp_prob +=x35 + x41 + x42 + x47  >=1

Lp_prob +=x36 + x47 + x48  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x40 + x47 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x47  >=1

Lp_prob +=x42 + x47  >=1

Lp_prob +=x43 + x46 + x47  >=1

Lp_prob +=x44 + x45 + x46 + x47  >=1

Lp_prob +=x45 + x46 + x47  >=1

Lp_prob +=x46 + x47  >=1

Lp_prob +=x47 + x48  >=1

Lp_prob +=x47 + x49 + x50 + x51  >=1

Lp_prob +=x47 + x50  >=1

Lp_prob +=x47 + x50 + x51  >=1

Lp_prob +=x46 + x47 + x52  >=1

Lp_prob +=x45 + x46 + x47 + x53  >=1

Lp_prob +=x45 + x46 + x47 + x53 + x54  >=1

Lp_prob +=x44 + x45 + x46 + x47 + x55  >=1

Lp_prob +=x47 + x49 + x50 + x51 + x56  >=1

Lp_prob +=x47 + x49 + x50 + x51 + x56 + x57  >=1

Lp_prob +=x47 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x47 + x49 + x50 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x47 + x49 + x50 + x51 + x60  >=1

Lp_prob +=x42 + x47 + x61 + x63  >=1

Lp_prob +=x41 + x42 + x47 + x62  >=1

Lp_prob +=x42 + x47 + x63  >=1

Lp_prob +=x41 + x42 + x47 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x47 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x47 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x47 + x49 + x50 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x47 + x49 + x50 + x51 + x68  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x47 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x47 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x41 + x48 + x62 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x48 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x48 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x48  >=1

Lp_prob +=x9 + x41 + x48 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x48  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x48 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x29 + x30 + x33 + x36 + x48 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x23 + x24 + x25 + x29 + x30 + x33 + x36 + x48 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x25 + x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x26 + x29 + x33 + x36 + x48  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x48  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x48  >=1

Lp_prob +=x29 + x33 + x36 + x48  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x48  >=1

Lp_prob +=x31 + x32 + x48 + x49 + x51  >=1

Lp_prob +=x32 + x48 + x49 + x51  >=1

Lp_prob +=x33 + x36 + x48  >=1

Lp_prob +=x34 + x35 + x41 + x48  >=1

Lp_prob +=x35 + x41 + x48  >=1

Lp_prob +=x36 + x48  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x48 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x48 + x49 + x51  >=1

Lp_prob +=x40 + x48 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x41 + x48  >=1

Lp_prob +=x42 + x47 + x48  >=1

Lp_prob +=x43 + x46 + x47 + x48  >=1

Lp_prob +=x44 + x45 + x46 + x47 + x48  >=1

Lp_prob +=x45 + x46 + x47 + x48  >=1

Lp_prob +=x46 + x47 + x48  >=1

Lp_prob +=x47 + x48  >=1

Lp_prob +=x48 + x49 + x51  >=1

Lp_prob +=x47 + x48 + x50  >=1

Lp_prob +=x48 + x51  >=1

Lp_prob +=x46 + x47 + x48 + x52  >=1

Lp_prob +=x45 + x46 + x47 + x48 + x53  >=1

Lp_prob +=x45 + x46 + x47 + x48 + x53 + x54  >=1

Lp_prob +=x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x48 + x49 + x51 + x56  >=1

Lp_prob +=x48 + x49 + x51 + x56 + x57  >=1

Lp_prob +=x48 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x48 + x49 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x48 + x49 + x51 + x60  >=1

Lp_prob +=x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x41 + x48 + x62  >=1

Lp_prob +=x42 + x47 + x48 + x63  >=1

Lp_prob +=x41 + x48 + x62 + x64  >=1

Lp_prob +=x41 + x48 + x62 + x65  >=1

Lp_prob +=x41 + x48 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x48 + x49 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x48 + x49 + x51 + x68  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x48 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x48 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x48 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x48 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x48 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x49 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49  >=1

Lp_prob +=x9 + x35 + x36 + x49 + x64 + x66  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32 + x49  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49  >=1

Lp_prob +=x26 + x29 + x32 + x49  >=1

Lp_prob +=x26 + x27 + x29 + x32 + x49  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32 + x49  >=1

Lp_prob +=x29 + x32 + x49  >=1

Lp_prob +=x29 + x30 + x32 + x49  >=1

Lp_prob +=x31 + x32 + x49  >=1

Lp_prob +=x32 + x49  >=1

Lp_prob +=x33 + x36 + x49  >=1

Lp_prob +=x34 + x35 + x36 + x49  >=1

Lp_prob +=x35 + x36 + x49  >=1

Lp_prob +=x36 + x49  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x38 + x49  >=1

Lp_prob +=x31 + x32 + x39 + x49  >=1

Lp_prob +=x40 + x49 + x56 + x58  >=1

Lp_prob +=x41 + x48 + x49 + x51  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51  >=1

Lp_prob +=x43 + x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x45 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x46 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x47 + x49 + x50 + x51  >=1

Lp_prob +=x48 + x49 + x51  >=1

Lp_prob +=x49 + x50 + x51  >=1

Lp_prob +=x49 + x51  >=1

Lp_prob +=x49 + x50 + x51 + x52  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x49 + x56  >=1

Lp_prob +=x49 + x56 + x57  >=1

Lp_prob +=x49 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x60  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x35 + x36 + x49 + x64  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x35 + x36 + x49 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x68  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x70  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x73  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x4 + x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x47 + x50 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x47 + x50 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x9 + x41 + x42 + x47 + x50 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x50 + x51  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x29 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x49 + x50 + x51  >=1

Lp_prob +=x32 + x49 + x50 + x51  >=1

Lp_prob +=x33 + x36 + x47 + x48 + x50  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x35 + x41 + x42 + x47 + x50  >=1

Lp_prob +=x36 + x47 + x48 + x50  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51  >=1

Lp_prob +=x40 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x47 + x50  >=1

Lp_prob +=x42 + x47 + x50  >=1

Lp_prob +=x43 + x46 + x50 + x52  >=1

Lp_prob +=x44 + x45 + x50 + x52 + x53  >=1

Lp_prob +=x45 + x50 + x52 + x53  >=1

Lp_prob +=x46 + x50 + x52  >=1

Lp_prob +=x47 + x50  >=1

Lp_prob +=x47 + x48 + x50  >=1

Lp_prob +=x49 + x50 + x51  >=1

Lp_prob +=x50 + x51  >=1

Lp_prob +=x50 + x52  >=1

Lp_prob +=x50 + x52 + x53  >=1

Lp_prob +=x50 + x52 + x53 + x54  >=1

Lp_prob +=x44 + x45 + x50 + x52 + x53 + x55  >=1

Lp_prob +=x49 + x50 + x51 + x56  >=1

Lp_prob +=x49 + x50 + x51 + x56 + x57  >=1

Lp_prob +=x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x60  >=1

Lp_prob +=x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x41 + x42 + x47 + x50 + x62  >=1

Lp_prob +=x42 + x47 + x50 + x63  >=1

Lp_prob +=x41 + x42 + x47 + x50 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x47 + x50 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x47 + x50 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x68  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x47 + x50 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x47 + x50 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x51 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x9 + x41 + x48 + x51 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x51 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x51 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x51  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x51 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x51  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x26 + x27 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32 + x49 + x51  >=1

Lp_prob +=x29 + x32 + x49 + x51  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x49 + x51  >=1

Lp_prob +=x32 + x49 + x51  >=1

Lp_prob +=x33 + x36 + x48 + x51  >=1

Lp_prob +=x34 + x35 + x41 + x48 + x51  >=1

Lp_prob +=x35 + x41 + x48 + x51  >=1

Lp_prob +=x36 + x48 + x51  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x51  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x51  >=1

Lp_prob +=x40 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x41 + x48 + x51  >=1

Lp_prob +=x42 + x47 + x50 + x51  >=1

Lp_prob +=x43 + x46 + x50 + x51 + x52  >=1

Lp_prob +=x44 + x45 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x45 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x46 + x50 + x51 + x52  >=1

Lp_prob +=x47 + x50 + x51  >=1

Lp_prob +=x48 + x51  >=1

Lp_prob +=x49 + x51  >=1

Lp_prob +=x50 + x51  >=1

Lp_prob +=x50 + x51 + x52  >=1

Lp_prob +=x50 + x51 + x52 + x53  >=1

Lp_prob +=x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x44 + x45 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x49 + x51 + x56  >=1

Lp_prob +=x49 + x51 + x56 + x57  >=1

Lp_prob +=x49 + x51 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x51 + x60  >=1

Lp_prob +=x42 + x47 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x41 + x48 + x51 + x62  >=1

Lp_prob +=x42 + x47 + x50 + x51 + x63  >=1

Lp_prob +=x41 + x48 + x51 + x62 + x64  >=1

Lp_prob +=x41 + x48 + x51 + x62 + x65  >=1

Lp_prob +=x41 + x48 + x51 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x51 + x68  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x51 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x51 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x48 + x51 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x51 + x73  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x51 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x4 + x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x29 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x32 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x33 + x36 + x46 + x47 + x48 + x52  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x36 + x46 + x47 + x48 + x52  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52  >=1

Lp_prob +=x40 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52  >=1

Lp_prob +=x42 + x43 + x46 + x52  >=1

Lp_prob +=x43 + x46 + x52  >=1

Lp_prob +=x44 + x45 + x52 + x53  >=1

Lp_prob +=x45 + x52 + x53  >=1

Lp_prob +=x46 + x52  >=1

Lp_prob +=x46 + x47 + x52  >=1

Lp_prob +=x46 + x47 + x48 + x52  >=1

Lp_prob +=x49 + x50 + x51 + x52  >=1

Lp_prob +=x50 + x52  >=1

Lp_prob +=x50 + x51 + x52  >=1

Lp_prob +=x52 + x53  >=1

Lp_prob +=x52 + x53 + x54  >=1

Lp_prob +=x44 + x45 + x52 + x53 + x55  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x56  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x56 + x57  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x60  >=1

Lp_prob +=x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52 + x62  >=1

Lp_prob +=x42 + x43 + x46 + x52 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x68  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x46 + x52 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x4 + x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x5 + x6 + x9 + x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53 + x74  >=1

Lp_prob +=x12 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x29 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x32 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x33 + x36 + x45 + x46 + x47 + x48 + x53  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x36 + x45 + x46 + x47 + x48 + x53  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x40 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x42 + x43 + x44 + x45 + x53  >=1

Lp_prob +=x43 + x44 + x45 + x53  >=1

Lp_prob +=x44 + x45 + x53  >=1

Lp_prob +=x45 + x53  >=1

Lp_prob +=x45 + x46 + x53  >=1

Lp_prob +=x45 + x46 + x47 + x53  >=1

Lp_prob +=x45 + x46 + x47 + x48 + x53  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53  >=1

Lp_prob +=x50 + x52 + x53  >=1

Lp_prob +=x50 + x51 + x52 + x53  >=1

Lp_prob +=x52 + x53  >=1

Lp_prob +=x53 + x54  >=1

Lp_prob +=x44 + x45 + x53 + x55  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x56  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x56 + x57  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x53 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x60  >=1

Lp_prob +=x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53 + x62  >=1

Lp_prob +=x42 + x43 + x44 + x45 + x53 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x53 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x68  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53 + x71  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x54 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x54 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x54 + x55 + x61  >=1

Lp_prob +=x4 + x54 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x5 + x54 + x55 + x61  >=1

Lp_prob +=x4 + x6 + x54 + x55 + x61  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x54 + x55 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x15 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x23 + x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x29 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x31 + x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x32 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x33 + x36 + x45 + x46 + x47 + x48 + x53 + x54  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x36 + x45 + x46 + x47 + x48 + x53 + x54  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x40 + x49 + x50 + x51 + x52 + x53 + x54 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x42 + x43 + x44 + x54 + x55  >=1

Lp_prob +=x43 + x44 + x54 + x55  >=1

Lp_prob +=x44 + x54 + x55  >=1

Lp_prob +=x45 + x53 + x54  >=1

Lp_prob +=x45 + x46 + x53 + x54  >=1

Lp_prob +=x45 + x46 + x47 + x53 + x54  >=1

Lp_prob +=x45 + x46 + x47 + x48 + x53 + x54  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x50 + x52 + x53 + x54  >=1

Lp_prob +=x50 + x51 + x52 + x53 + x54  >=1

Lp_prob +=x52 + x53 + x54  >=1

Lp_prob +=x53 + x54  >=1

Lp_prob +=x54 + x55  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x54 + x56  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x54 + x56 + x57  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x54 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x53 + x54 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x60  >=1

Lp_prob +=x54 + x55 + x61  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55 + x62  >=1

Lp_prob +=x42 + x43 + x44 + x54 + x55 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x68  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x71  >=1

Lp_prob +=x4 + x6 + x54 + x55 + x61 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x55 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x55 + x61  >=1

Lp_prob +=x4 + x55 + x61  >=1

Lp_prob +=x3 + x4 + x5 + x55 + x61  >=1

Lp_prob +=x4 + x6 + x55 + x61  >=1

Lp_prob +=x7 + x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x9 + x41 + x42 + x43 + x44 + x55 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x74  >=1

Lp_prob +=x10 + x12 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x10 + x12 + x14 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x29 + x33 + x36 + x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x31 + x32 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x32 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x33 + x36 + x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x35 + x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x36 + x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x31 + x32 + x39 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x40 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x56 + x58  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55  >=1

Lp_prob +=x42 + x43 + x44 + x55  >=1

Lp_prob +=x43 + x44 + x55  >=1

Lp_prob +=x44 + x55  >=1

Lp_prob +=x44 + x45 + x55  >=1

Lp_prob +=x44 + x45 + x46 + x55  >=1

Lp_prob +=x44 + x45 + x46 + x47 + x55  >=1

Lp_prob +=x44 + x45 + x46 + x47 + x48 + x55  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x44 + x45 + x50 + x52 + x53 + x55  >=1

Lp_prob +=x44 + x45 + x50 + x51 + x52 + x53 + x55  >=1

Lp_prob +=x44 + x45 + x52 + x53 + x55  >=1

Lp_prob +=x44 + x45 + x53 + x55  >=1

Lp_prob +=x54 + x55  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x56  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x56 + x57  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x56 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x59  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x60  >=1

Lp_prob +=x55 + x61  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55 + x62  >=1

Lp_prob +=x42 + x43 + x44 + x55 + x63  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55 + x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x70  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x55 + x71  >=1

Lp_prob +=x4 + x6 + x55 + x61 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x73  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x9 + x35 + x36 + x49 + x56 + x64 + x66  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x58 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x38 + x39 + x56 + x58 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x38 + x39 + x56 + x58  >=1

Lp_prob +=x23 + x24 + x31 + x38 + x39 + x56 + x58 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x56 + x58  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x26 + x27 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32 + x49 + x56  >=1

Lp_prob +=x29 + x32 + x49 + x56  >=1

Lp_prob +=x30 + x31 + x39 + x56 + x58  >=1

Lp_prob +=x31 + x39 + x56 + x58  >=1

Lp_prob +=x32 + x49 + x56  >=1

Lp_prob +=x33 + x36 + x49 + x56  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x56  >=1

Lp_prob +=x35 + x36 + x49 + x56  >=1

Lp_prob +=x36 + x49 + x56  >=1

Lp_prob +=x31 + x37 + x38 + x39 + x56 + x58  >=1

Lp_prob +=x31 + x38 + x39 + x56 + x58  >=1

Lp_prob +=x39 + x56 + x58  >=1

Lp_prob +=x40 + x56 + x58  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56  >=1

Lp_prob +=x43 + x46 + x49 + x50 + x51 + x52 + x56  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x56  >=1

Lp_prob +=x45 + x49 + x50 + x51 + x52 + x53 + x56  >=1

Lp_prob +=x46 + x49 + x50 + x51 + x52 + x56  >=1

Lp_prob +=x47 + x49 + x50 + x51 + x56  >=1

Lp_prob +=x48 + x49 + x51 + x56  >=1

Lp_prob +=x49 + x56  >=1

Lp_prob +=x49 + x50 + x51 + x56  >=1

Lp_prob +=x49 + x51 + x56  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x56  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x56  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x54 + x56  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x56  >=1

Lp_prob +=x56 + x57  >=1

Lp_prob +=x56 + x58  >=1

Lp_prob +=x39 + x56 + x58 + x59  >=1

Lp_prob +=x39 + x56 + x58 + x59 + x60  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x61 + x63  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x62  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x63  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x64  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x62 + x65  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x64 + x66  >=1

Lp_prob +=x39 + x56 + x58 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x39 + x56 + x58 + x59 + x60 + x68  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x56 + x58 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x56 + x58 + x70  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x56 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x58 + x73  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66  >=1

Lp_prob +=x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x21 + x23 + x37 + x40 + x57 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x22 + x24 + x38 + x40 + x57 + x59 + x60  >=1

Lp_prob +=x23 + x37 + x40 + x57 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x24 + x38 + x40 + x57 + x59 + x60  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x26 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x26 + x27 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x29 + x32 + x49 + x56 + x57  >=1

Lp_prob +=x30 + x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x31 + x39 + x56 + x57 + x58  >=1

Lp_prob +=x32 + x49 + x56 + x57  >=1

Lp_prob +=x33 + x36 + x49 + x56 + x57  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x56 + x57  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x57  >=1

Lp_prob +=x36 + x49 + x56 + x57  >=1

Lp_prob +=x37 + x40 + x57 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x38 + x40 + x57 + x59 + x60  >=1

Lp_prob +=x39 + x56 + x57 + x58  >=1

Lp_prob +=x40 + x57  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x57  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x57  >=1

Lp_prob +=x43 + x46 + x49 + x50 + x51 + x52 + x56 + x57  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x56 + x57  >=1

Lp_prob +=x45 + x49 + x50 + x51 + x52 + x53 + x56 + x57  >=1

Lp_prob +=x46 + x49 + x50 + x51 + x52 + x56 + x57  >=1

Lp_prob +=x47 + x49 + x50 + x51 + x56 + x57  >=1

Lp_prob +=x48 + x49 + x51 + x56 + x57  >=1

Lp_prob +=x49 + x56 + x57  >=1

Lp_prob +=x49 + x50 + x51 + x56 + x57  >=1

Lp_prob +=x49 + x51 + x56 + x57  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x56 + x57  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x56 + x57  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x54 + x56 + x57  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x56 + x57  >=1

Lp_prob +=x56 + x57  >=1

Lp_prob +=x56 + x57 + x58  >=1

Lp_prob +=x40 + x57 + x59  >=1

Lp_prob +=x40 + x57 + x59 + x60  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x57 + x61 + x63  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x57 + x62  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x57 + x63  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x57 + x64  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x57 + x62 + x65  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x57 + x64 + x66  >=1

Lp_prob +=x40 + x57 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x40 + x57 + x59 + x60 + x68  >=1

Lp_prob +=x24 + x38 + x40 + x57 + x59 + x60 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x40 + x57 + x59 + x60 + x70  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x56 + x57 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58 + x73  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x58 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x21 + x23 + x24 + x31 + x38 + x39 + x58 + x70  >=1

Lp_prob +=x22 + x24 + x31 + x38 + x39 + x58  >=1

Lp_prob +=x23 + x24 + x31 + x38 + x39 + x58 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x58  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58  >=1

Lp_prob +=x29 + x31 + x32 + x39 + x58  >=1

Lp_prob +=x30 + x31 + x39 + x58  >=1

Lp_prob +=x31 + x39 + x58  >=1

Lp_prob +=x31 + x32 + x39 + x58  >=1

Lp_prob +=x31 + x32 + x33 + x39 + x58  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x58  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x58  >=1

Lp_prob +=x36 + x49 + x56 + x58  >=1

Lp_prob +=x31 + x37 + x38 + x39 + x58  >=1

Lp_prob +=x31 + x38 + x39 + x58  >=1

Lp_prob +=x39 + x58  >=1

Lp_prob +=x40 + x58  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x43 + x46 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x45 + x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x46 + x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x47 + x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x48 + x49 + x51 + x56 + x58  >=1

Lp_prob +=x49 + x56 + x58  >=1

Lp_prob +=x49 + x50 + x51 + x56 + x58  >=1

Lp_prob +=x49 + x51 + x56 + x58  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x56 + x58  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x56 + x58  >=1

Lp_prob +=x49 + x50 + x51 + x52 + x53 + x54 + x56 + x58  >=1

Lp_prob +=x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x56 + x58  >=1

Lp_prob +=x56 + x58  >=1

Lp_prob +=x56 + x57 + x58  >=1

Lp_prob +=x39 + x58 + x59  >=1

Lp_prob +=x39 + x58 + x59 + x60  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x58 + x61 + x63  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x58 + x62  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x58 + x63  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x58 + x64  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x58 + x62 + x65  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x39 + x58 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x39 + x58 + x59 + x60 + x68  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x58 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x58 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x58 + x71  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x58 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71  >=1

Lp_prob +=x7 + x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x11 + x12 + x13 + x16 + x25 + x30 + x31 + x39 + x59 + x73  >=1

Lp_prob +=x12 + x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x12 + x14 + x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x15 + x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x16 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x12 + x14 + x16 + x17 + x18 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x12 + x14 + x16 + x18 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x21 + x23 + x37 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x22 + x24 + x38 + x59 + x60  >=1

Lp_prob +=x23 + x37 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x24 + x38 + x59 + x60  >=1

Lp_prob +=x25 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59  >=1

Lp_prob +=x29 + x31 + x32 + x39 + x59  >=1

Lp_prob +=x30 + x31 + x39 + x59  >=1

Lp_prob +=x31 + x39 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x59  >=1

Lp_prob +=x31 + x32 + x33 + x39 + x59  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x59  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x39 + x49 + x59  >=1

Lp_prob +=x31 + x32 + x36 + x39 + x49 + x59  >=1

Lp_prob +=x37 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x38 + x59 + x60  >=1

Lp_prob +=x39 + x59  >=1

Lp_prob +=x40 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x43 + x46 + x49 + x50 + x51 + x52 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x45 + x49 + x50 + x51 + x52 + x53 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x46 + x49 + x50 + x51 + x52 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x47 + x49 + x50 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x48 + x49 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x51 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x53 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x49 + x50 + x51 + x52 + x53 + x54 + x59  >=1

Lp_prob +=x31 + x32 + x39 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x59  >=1

Lp_prob +=x39 + x56 + x58 + x59  >=1

Lp_prob +=x40 + x57 + x59  >=1

Lp_prob +=x39 + x58 + x59  >=1

Lp_prob +=x59 + x60  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x59 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x59 + x62  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x59 + x63  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x39 + x49 + x59 + x64  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x59 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71  >=1

Lp_prob +=x59 + x60 + x67 + x68  >=1

Lp_prob +=x59 + x60 + x68  >=1

Lp_prob +=x24 + x38 + x59 + x60 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x59 + x60 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x59 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x59 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x24 + x38 + x60 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x24 + x38 + x60 + x73  >=1

Lp_prob +=x12 + x16 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x14 + x15 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x15 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x16 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x14 + x15 + x17 + x18 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x14 + x15 + x18 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x15 + x19 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x15 + x19 + x20 + x22 + x24 + x38 + x60  >=1

Lp_prob +=x21 + x23 + x37 + x60 + x67 + x68  >=1

Lp_prob +=x22 + x24 + x38 + x60  >=1

Lp_prob +=x23 + x37 + x60 + x67 + x68  >=1

Lp_prob +=x24 + x38 + x60  >=1

Lp_prob +=x25 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x38 + x60  >=1

Lp_prob +=x29 + x31 + x32 + x38 + x60  >=1

Lp_prob +=x30 + x31 + x38 + x60  >=1

Lp_prob +=x31 + x38 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x60  >=1

Lp_prob +=x31 + x32 + x33 + x38 + x60  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x60  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x60  >=1

Lp_prob +=x31 + x32 + x36 + x38 + x49 + x60  >=1

Lp_prob +=x37 + x60 + x67 + x68  >=1

Lp_prob +=x38 + x60  >=1

Lp_prob +=x39 + x59 + x60  >=1

Lp_prob +=x40 + x59 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x43 + x46 + x49 + x50 + x51 + x52 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x45 + x49 + x50 + x51 + x52 + x53 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x46 + x49 + x50 + x51 + x52 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x47 + x49 + x50 + x51 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x48 + x49 + x51 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x51 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x60  >=1

Lp_prob +=x39 + x56 + x58 + x59 + x60  >=1

Lp_prob +=x40 + x57 + x59 + x60  >=1

Lp_prob +=x39 + x58 + x59 + x60  >=1

Lp_prob +=x59 + x60  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x60 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x60 + x62  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x60 + x63  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x60 + x64  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x60 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71  >=1

Lp_prob +=x60 + x67 + x68  >=1

Lp_prob +=x60 + x68  >=1

Lp_prob +=x24 + x38 + x60 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x60 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x60 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x60 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x60 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x61  >=1

Lp_prob +=x2 + x3 + x4 + x61  >=1

Lp_prob +=x3 + x4 + x61  >=1

Lp_prob +=x4 + x61  >=1

Lp_prob +=x3 + x4 + x5 + x61  >=1

Lp_prob +=x4 + x6 + x61  >=1

Lp_prob +=x3 + x4 + x5 + x7 + x61  >=1

Lp_prob +=x4 + x6 + x8 + x61  >=1

Lp_prob +=x9 + x61 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x10 + x28 + x61 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x3 + x4 + x5 + x7 + x11 + x61  >=1

Lp_prob +=x10 + x12 + x28 + x61 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x61  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x61  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x17 + x18 + x61  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x18 + x61  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x27 + x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x28 + x61 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x29 + x33 + x36 + x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x32 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x33 + x36 + x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x34 + x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x35 + x61 + x62 + x63 + x64  >=1

Lp_prob +=x36 + x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x40 + x42 + x47 + x49 + x50 + x51 + x56 + x58 + x61 + x63  >=1

Lp_prob +=x41 + x61 + x62 + x63  >=1

Lp_prob +=x42 + x61 + x63  >=1

Lp_prob +=x42 + x43 + x61 + x63  >=1

Lp_prob +=x44 + x55 + x61  >=1

Lp_prob +=x44 + x45 + x55 + x61  >=1

Lp_prob +=x42 + x43 + x46 + x61 + x63  >=1

Lp_prob +=x42 + x47 + x61 + x63  >=1

Lp_prob +=x42 + x47 + x48 + x61 + x63  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x42 + x47 + x50 + x61 + x63  >=1

Lp_prob +=x42 + x47 + x50 + x51 + x61 + x63  >=1

Lp_prob +=x42 + x43 + x46 + x52 + x61 + x63  >=1

Lp_prob +=x44 + x45 + x53 + x55 + x61  >=1

Lp_prob +=x54 + x55 + x61  >=1

Lp_prob +=x55 + x61  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x61 + x63  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x57 + x61 + x63  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x58 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x59 + x61 + x63  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x60 + x61 + x63  >=1

Lp_prob +=x61 + x62 + x63  >=1

Lp_prob +=x61 + x63  >=1

Lp_prob +=x61 + x62 + x63 + x64  >=1

Lp_prob +=x61 + x62 + x63 + x65  >=1

Lp_prob +=x61 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x61 + x63 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x61 + x63 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x61 + x62 + x63 + x64 + x70  >=1

Lp_prob +=x61 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x4 + x6 + x61 + x72  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x61 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x61 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x62 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x62 + x64 + x66  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x62 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x64 + x66  >=1

Lp_prob +=x9 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x62 + x64 + x66 + x74  >=1

Lp_prob +=x10 + x12 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x64 + x66  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x27 + x34 + x35 + x62 + x64  >=1

Lp_prob +=x28 + x62 + x64 + x66 + x71  >=1

Lp_prob +=x29 + x33 + x36 + x41 + x48 + x62  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x41 + x48 + x62  >=1

Lp_prob +=x31 + x32 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x32 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x33 + x36 + x41 + x48 + x62  >=1

Lp_prob +=x34 + x35 + x62 + x64  >=1

Lp_prob +=x35 + x62 + x64  >=1

Lp_prob +=x36 + x41 + x48 + x62  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x40 + x41 + x48 + x49 + x51 + x56 + x58 + x62  >=1

Lp_prob +=x41 + x62  >=1

Lp_prob +=x41 + x42 + x62  >=1

Lp_prob +=x41 + x42 + x43 + x62  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x62  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x62  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x62  >=1

Lp_prob +=x41 + x42 + x47 + x62  >=1

Lp_prob +=x41 + x48 + x62  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x62  >=1

Lp_prob +=x41 + x42 + x47 + x50 + x62  >=1

Lp_prob +=x41 + x48 + x51 + x62  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52 + x62  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53 + x62  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55 + x62  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55 + x62  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x62  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x57 + x62  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x58 + x62  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x59 + x62  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x60 + x62  >=1

Lp_prob +=x61 + x62 + x63  >=1

Lp_prob +=x62 + x63  >=1

Lp_prob +=x62 + x64  >=1

Lp_prob +=x62 + x65  >=1

Lp_prob +=x62 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x62 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x62 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x70  >=1

Lp_prob +=x62 + x64 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x64 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x64 + x66 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x4 + x61 + x63  >=1

Lp_prob +=x2 + x3 + x4 + x61 + x63  >=1

Lp_prob +=x3 + x4 + x61 + x63  >=1

Lp_prob +=x4 + x61 + x63  >=1

Lp_prob +=x5 + x6 + x9 + x62 + x63 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x62 + x63 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x9 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x10 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x62 + x63 + x64 + x66 + x74  >=1

Lp_prob +=x10 + x12 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x27 + x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x28 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x29 + x33 + x36 + x42 + x47 + x48 + x63  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x42 + x47 + x48 + x63  >=1

Lp_prob +=x31 + x32 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x32 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x33 + x36 + x42 + x47 + x48 + x63  >=1

Lp_prob +=x34 + x35 + x62 + x63 + x64  >=1

Lp_prob +=x35 + x62 + x63 + x64  >=1

Lp_prob +=x36 + x42 + x47 + x48 + x63  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x40 + x42 + x47 + x49 + x50 + x51 + x56 + x58 + x63  >=1

Lp_prob +=x41 + x62 + x63  >=1

Lp_prob +=x42 + x63  >=1

Lp_prob +=x42 + x43 + x63  >=1

Lp_prob +=x42 + x43 + x44 + x63  >=1

Lp_prob +=x42 + x43 + x44 + x45 + x63  >=1

Lp_prob +=x42 + x43 + x46 + x63  >=1

Lp_prob +=x42 + x47 + x63  >=1

Lp_prob +=x42 + x47 + x48 + x63  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x63  >=1

Lp_prob +=x42 + x47 + x50 + x63  >=1

Lp_prob +=x42 + x47 + x50 + x51 + x63  >=1

Lp_prob +=x42 + x43 + x46 + x52 + x63  >=1

Lp_prob +=x42 + x43 + x44 + x45 + x53 + x63  >=1

Lp_prob +=x42 + x43 + x44 + x54 + x55 + x63  >=1

Lp_prob +=x42 + x43 + x44 + x55 + x63  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x63  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x57 + x63  >=1

Lp_prob +=x42 + x47 + x49 + x50 + x51 + x56 + x58 + x63  >=1

Lp_prob +=x31 + x32 + x39 + x42 + x47 + x49 + x50 + x51 + x59 + x63  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x60 + x63  >=1

Lp_prob +=x61 + x63  >=1

Lp_prob +=x62 + x63  >=1

Lp_prob +=x62 + x63 + x64  >=1

Lp_prob +=x62 + x63 + x65  >=1

Lp_prob +=x62 + x63 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x63 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x63 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x63 + x64 + x70  >=1

Lp_prob +=x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x62 + x63 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x63 + x64 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x63 + x64 + x66 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x64 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x64 + x66  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x64 + x66  >=1

Lp_prob +=x9 + x64 + x66  >=1

Lp_prob +=x10 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x64 + x66 + x74  >=1

Lp_prob +=x10 + x12 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x64 + x66  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x64 + x66 + x71  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x64 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x64 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x64  >=1

Lp_prob +=x27 + x34 + x35 + x64  >=1

Lp_prob +=x28 + x64 + x66 + x71  >=1

Lp_prob +=x29 + x33 + x35 + x36 + x64  >=1

Lp_prob +=x29 + x30 + x33 + x35 + x36 + x64  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x49 + x64  >=1

Lp_prob +=x32 + x35 + x36 + x49 + x64  >=1

Lp_prob +=x33 + x35 + x36 + x64  >=1

Lp_prob +=x34 + x35 + x64  >=1

Lp_prob +=x35 + x64  >=1

Lp_prob +=x35 + x36 + x64  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x37 + x38 + x49 + x64  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x64  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x39 + x49 + x64  >=1

Lp_prob +=x35 + x36 + x40 + x49 + x56 + x58 + x64  >=1

Lp_prob +=x41 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x47 + x62 + x64  >=1

Lp_prob +=x41 + x48 + x62 + x64  >=1

Lp_prob +=x35 + x36 + x49 + x64  >=1

Lp_prob +=x41 + x42 + x47 + x50 + x62 + x64  >=1

Lp_prob +=x41 + x48 + x51 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55 + x62 + x64  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55 + x62 + x64  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x64  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x57 + x64  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x58 + x64  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x39 + x49 + x59 + x64  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x60 + x64  >=1

Lp_prob +=x61 + x62 + x63 + x64  >=1

Lp_prob +=x62 + x64  >=1

Lp_prob +=x62 + x63 + x64  >=1

Lp_prob +=x62 + x64 + x65  >=1

Lp_prob +=x64 + x66  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x37 + x38 + x49 + x64 + x67  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x64 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x64 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x64 + x70  >=1

Lp_prob +=x64 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x64 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x64 + x66 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x62 + x64 + x65 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x9 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x10 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x62 + x64 + x65 + x66 + x74  >=1

Lp_prob +=x10 + x12 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x64 + x65 + x66  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x15 + x16 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x16 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x15 + x16 + x19 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x15 + x16 + x19 + x20 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x21 + x23 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65 + x70  >=1

Lp_prob +=x22 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x26 + x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x27 + x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x28 + x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x29 + x33 + x36 + x41 + x48 + x62 + x65  >=1

Lp_prob +=x29 + x30 + x33 + x36 + x41 + x48 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x32 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x33 + x36 + x41 + x48 + x62 + x65  >=1

Lp_prob +=x34 + x35 + x62 + x64 + x65  >=1

Lp_prob +=x35 + x62 + x64 + x65  >=1

Lp_prob +=x36 + x41 + x48 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x40 + x41 + x48 + x49 + x51 + x56 + x58 + x62 + x65  >=1

Lp_prob +=x41 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x47 + x62 + x65  >=1

Lp_prob +=x41 + x48 + x62 + x65  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x47 + x50 + x62 + x65  >=1

Lp_prob +=x41 + x48 + x51 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55 + x62 + x65  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55 + x62 + x65  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x62 + x65  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x57 + x62 + x65  >=1

Lp_prob +=x41 + x48 + x49 + x51 + x56 + x58 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x39 + x41 + x48 + x49 + x51 + x59 + x62 + x65  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x60 + x62 + x65  >=1

Lp_prob +=x61 + x62 + x63 + x65  >=1

Lp_prob +=x62 + x65  >=1

Lp_prob +=x62 + x63 + x65  >=1

Lp_prob +=x62 + x64 + x65  >=1

Lp_prob +=x62 + x64 + x65 + x66  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x62 + x65 + x67  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x62 + x65 + x68  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x62 + x64 + x65 + x70  >=1

Lp_prob +=x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x64 + x65 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x64 + x65 + x66 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x66 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x66 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x66  >=1

Lp_prob +=x5 + x6 + x9 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x66  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x66  >=1

Lp_prob +=x9 + x66  >=1

Lp_prob +=x10 + x28 + x66 + x71  >=1

Lp_prob +=x6 + x7 + x8 + x9 + x11 + x66 + x74  >=1

Lp_prob +=x10 + x12 + x28 + x66 + x71  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x66  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x28 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x16 + x28 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x28 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x20 + x28 + x66 + x71  >=1

Lp_prob +=x10 + x12 + x16 + x21 + x22 + x28 + x66 + x69 + x71  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x66 + x71  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x28 + x66 + x70 + x71  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x66 + x71  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x66 + x71  >=1

Lp_prob +=x26 + x27 + x28 + x66 + x71  >=1

Lp_prob +=x27 + x28 + x66 + x71  >=1

Lp_prob +=x28 + x66 + x71  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x66 + x71  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x66 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x32 + x33 + x34 + x66 + x71  >=1

Lp_prob +=x33 + x34 + x66 + x71  >=1

Lp_prob +=x34 + x66 + x71  >=1

Lp_prob +=x35 + x64 + x66  >=1

Lp_prob +=x35 + x36 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x66 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x66 + x71  >=1

Lp_prob +=x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x41 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x43 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x47 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x48 + x62 + x64 + x66  >=1

Lp_prob +=x35 + x36 + x49 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x47 + x50 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x48 + x51 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x54 + x55 + x62 + x64 + x66  >=1

Lp_prob +=x41 + x42 + x43 + x44 + x55 + x62 + x64 + x66  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x64 + x66  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x57 + x64 + x66  >=1

Lp_prob +=x35 + x36 + x49 + x56 + x58 + x64 + x66  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71  >=1

Lp_prob +=x61 + x62 + x63 + x64 + x66  >=1

Lp_prob +=x62 + x64 + x66  >=1

Lp_prob +=x62 + x63 + x64 + x66  >=1

Lp_prob +=x64 + x66  >=1

Lp_prob +=x62 + x64 + x65 + x66  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x66 + x69 + x71  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x66 + x70 + x71  >=1

Lp_prob +=x66 + x71  >=1

Lp_prob +=x6 + x9 + x66 + x72  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x66 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71  >=1

Lp_prob +=x5 + x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71  >=1

Lp_prob +=x7 + x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x11 + x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x12 + x16 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x14 + x15 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x15 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x16 + x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x17 + x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x19 + x21 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x20 + x21 + x23 + x37 + x67  >=1

Lp_prob +=x21 + x23 + x37 + x67  >=1

Lp_prob +=x21 + x22 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x23 + x37 + x67  >=1

Lp_prob +=x24 + x37 + x38 + x67  >=1

Lp_prob +=x25 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x29 + x31 + x32 + x37 + x38 + x67  >=1

Lp_prob +=x30 + x31 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x32 + x33 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x67  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x37 + x38 + x49 + x67  >=1

Lp_prob +=x31 + x32 + x36 + x37 + x38 + x49 + x67  >=1

Lp_prob +=x37 + x67  >=1

Lp_prob +=x37 + x38 + x67  >=1

Lp_prob +=x39 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x40 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x43 + x46 + x49 + x50 + x51 + x52 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x45 + x49 + x50 + x51 + x52 + x53 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x46 + x49 + x50 + x51 + x52 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x47 + x49 + x50 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x48 + x49 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x51 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x53 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x67  >=1

Lp_prob +=x39 + x56 + x58 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x40 + x57 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x39 + x58 + x59 + x60 + x67 + x68  >=1

Lp_prob +=x59 + x60 + x67 + x68  >=1

Lp_prob +=x60 + x67 + x68  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x61 + x63 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x62 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x42 + x47 + x49 + x50 + x51 + x63 + x67  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x37 + x38 + x49 + x64 + x67  >=1

Lp_prob +=x31 + x32 + x37 + x38 + x41 + x48 + x49 + x51 + x62 + x65 + x67  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71  >=1

Lp_prob +=x67 + x68  >=1

Lp_prob +=x21 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x23 + x37 + x67 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x67 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71 + x72  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x67 + x69 + x73  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x67 + x69 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71  >=1

Lp_prob +=x7 + x11 + x13 + x14 + x15 + x22 + x24 + x38 + x68 + x73  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71  >=1

Lp_prob +=x10 + x25 + x26 + x27 + x28 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x11 + x13 + x14 + x15 + x22 + x24 + x38 + x68 + x73  >=1

Lp_prob +=x12 + x16 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x14 + x15 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x15 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x16 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x17 + x20 + x21 + x23 + x37 + x67 + x68  >=1

Lp_prob +=x14 + x15 + x18 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x15 + x19 + x22 + x24 + x38 + x68  >=1

Lp_prob +=x20 + x21 + x23 + x37 + x67 + x68  >=1

Lp_prob +=x21 + x23 + x37 + x67 + x68  >=1

Lp_prob +=x22 + x24 + x38 + x68  >=1

Lp_prob +=x23 + x37 + x67 + x68  >=1

Lp_prob +=x24 + x38 + x68  >=1

Lp_prob +=x25 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x25 + x26 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x25 + x26 + x27 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x31 + x38 + x68  >=1

Lp_prob +=x29 + x31 + x32 + x38 + x68  >=1

Lp_prob +=x30 + x31 + x38 + x68  >=1

Lp_prob +=x31 + x38 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x68  >=1

Lp_prob +=x31 + x32 + x33 + x38 + x68  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x68  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x68  >=1

Lp_prob +=x31 + x32 + x36 + x38 + x49 + x68  >=1

Lp_prob +=x37 + x67 + x68  >=1

Lp_prob +=x38 + x68  >=1

Lp_prob +=x39 + x59 + x60 + x68  >=1

Lp_prob +=x40 + x59 + x60 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x43 + x46 + x49 + x50 + x51 + x52 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x45 + x49 + x50 + x51 + x52 + x53 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x46 + x49 + x50 + x51 + x52 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x47 + x49 + x50 + x51 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x48 + x49 + x51 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x51 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x44 + x45 + x49 + x50 + x51 + x52 + x53 + x55 + x68  >=1

Lp_prob +=x39 + x56 + x58 + x59 + x60 + x68  >=1

Lp_prob +=x40 + x57 + x59 + x60 + x68  >=1

Lp_prob +=x39 + x58 + x59 + x60 + x68  >=1

Lp_prob +=x59 + x60 + x68  >=1

Lp_prob +=x60 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x61 + x63 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x62 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x42 + x47 + x49 + x50 + x51 + x63 + x68  >=1

Lp_prob +=x31 + x32 + x35 + x36 + x38 + x49 + x64 + x68  >=1

Lp_prob +=x31 + x32 + x38 + x41 + x48 + x49 + x51 + x62 + x65 + x68  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71  >=1

Lp_prob +=x67 + x68  >=1

Lp_prob +=x21 + x23 + x37 + x67 + x68 + x69  >=1

Lp_prob +=x23 + x37 + x67 + x68 + x70  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x68 + x71  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x68 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x68 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x22 + x69  >=1

Lp_prob +=x5 + x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x69  >=1

Lp_prob +=x7 + x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x22 + x69  >=1

Lp_prob +=x9 + x10 + x12 + x16 + x22 + x69  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x69  >=1

Lp_prob +=x11 + x18 + x19 + x69 + x73  >=1

Lp_prob +=x12 + x16 + x22 + x69  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x69  >=1

Lp_prob +=x14 + x15 + x22 + x69  >=1

Lp_prob +=x15 + x22 + x69  >=1

Lp_prob +=x16 + x22 + x69  >=1

Lp_prob +=x17 + x18 + x19 + x69  >=1

Lp_prob +=x18 + x19 + x69  >=1

Lp_prob +=x19 + x69  >=1

Lp_prob +=x19 + x20 + x69  >=1

Lp_prob +=x21 + x69  >=1

Lp_prob +=x22 + x69  >=1

Lp_prob +=x21 + x23 + x69  >=1

Lp_prob +=x24 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x69  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x30 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x69 + x70  >=1

Lp_prob +=x21 + x23 + x37 + x69  >=1

Lp_prob +=x24 + x38 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x40 + x59 + x60 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x48 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x51 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x56 + x58 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x40 + x57 + x59 + x60 + x69 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x58 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x59 + x60 + x69 + x70  >=1

Lp_prob +=x24 + x38 + x60 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x64 + x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65 + x69 + x70  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x66 + x69 + x71  >=1

Lp_prob +=x21 + x23 + x37 + x67 + x69  >=1

Lp_prob +=x21 + x23 + x37 + x67 + x68 + x69  >=1

Lp_prob +=x69 + x70  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x69 + x71  >=1

Lp_prob +=x18 + x19 + x69 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x69 + x73  >=1

Lp_prob +=x18 + x19 + x69 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x5 + x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x7 + x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x8 + x13 + x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x9 + x10 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x10 + x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x11 + x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x12 + x16 + x22 + x69 + x70  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x14 + x15 + x22 + x69 + x70  >=1

Lp_prob +=x15 + x22 + x69 + x70  >=1

Lp_prob +=x16 + x22 + x69 + x70  >=1

Lp_prob +=x17 + x18 + x19 + x69 + x70  >=1

Lp_prob +=x18 + x19 + x69 + x70  >=1

Lp_prob +=x19 + x69 + x70  >=1

Lp_prob +=x19 + x20 + x69 + x70  >=1

Lp_prob +=x21 + x23 + x70  >=1

Lp_prob +=x22 + x69 + x70  >=1

Lp_prob +=x23 + x70  >=1

Lp_prob +=x24 + x70  >=1

Lp_prob +=x24 + x25 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x70  >=1

Lp_prob +=x24 + x25 + x30 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x70  >=1

Lp_prob +=x23 + x37 + x70  >=1

Lp_prob +=x24 + x38 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x70  >=1

Lp_prob +=x24 + x38 + x40 + x59 + x60 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x45 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x70  >=1

Lp_prob +=x24 + x25 + x29 + x30 + x33 + x36 + x48 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x51 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x70  >=1

Lp_prob +=x24 + x31 + x32 + x38 + x49 + x50 + x51 + x52 + x53 + x54 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x56 + x58 + x70  >=1

Lp_prob +=x24 + x38 + x40 + x57 + x59 + x60 + x70  >=1

Lp_prob +=x24 + x31 + x38 + x39 + x58 + x70  >=1

Lp_prob +=x24 + x38 + x59 + x60 + x70  >=1

Lp_prob +=x24 + x38 + x60 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x61 + x62 + x63 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x63 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x64 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x34 + x35 + x41 + x62 + x65 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x66 + x70 + x71  >=1

Lp_prob +=x23 + x37 + x67 + x70  >=1

Lp_prob +=x23 + x37 + x67 + x68 + x70  >=1

Lp_prob +=x69 + x70  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x70 + x71  >=1

Lp_prob +=x18 + x19 + x69 + x70 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x18 + x19 + x69 + x70 + x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x3 + x5 + x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x9 + x66 + x71  >=1

Lp_prob +=x5 + x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x66 + x71  >=1

Lp_prob +=x7 + x8 + x10 + x28 + x71 + x74  >=1

Lp_prob +=x8 + x10 + x28 + x71  >=1

Lp_prob +=x9 + x66 + x71  >=1

Lp_prob +=x10 + x28 + x71  >=1

Lp_prob +=x7 + x8 + x10 + x11 + x28 + x71 + x74  >=1

Lp_prob +=x10 + x12 + x28 + x71  >=1

Lp_prob +=x8 + x10 + x13 + x28 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x28 + x71  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x28 + x71  >=1

Lp_prob +=x10 + x12 + x16 + x28 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x17 + x18 + x28 + x71  >=1

Lp_prob +=x10 + x12 + x14 + x18 + x28 + x71  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x28 + x71  >=1

Lp_prob +=x10 + x12 + x15 + x16 + x19 + x20 + x28 + x71  >=1

Lp_prob +=x10 + x12 + x16 + x21 + x22 + x28 + x69 + x71  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x71  >=1

Lp_prob +=x23 + x24 + x25 + x26 + x27 + x28 + x70 + x71  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x71  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x71  >=1

Lp_prob +=x26 + x27 + x28 + x71  >=1

Lp_prob +=x27 + x28 + x71  >=1

Lp_prob +=x28 + x71  >=1

Lp_prob +=x26 + x27 + x28 + x29 + x71  >=1

Lp_prob +=x25 + x26 + x27 + x28 + x30 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x71  >=1

Lp_prob +=x32 + x33 + x34 + x71  >=1

Lp_prob +=x33 + x34 + x71  >=1

Lp_prob +=x34 + x71  >=1

Lp_prob +=x34 + x35 + x71  >=1

Lp_prob +=x34 + x35 + x36 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x40 + x59 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x45 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x46 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x47 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x48 + x71  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x47 + x50 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x48 + x51 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x46 + x52 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x71  >=1

Lp_prob +=x34 + x35 + x41 + x42 + x43 + x44 + x55 + x71  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x56 + x71  >=1

Lp_prob +=x34 + x35 + x36 + x49 + x56 + x57 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x58 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x39 + x59 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x60 + x71  >=1

Lp_prob +=x61 + x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x62 + x64 + x66 + x71  >=1

Lp_prob +=x62 + x63 + x64 + x66 + x71  >=1

Lp_prob +=x64 + x66 + x71  >=1

Lp_prob +=x62 + x64 + x65 + x66 + x71  >=1

Lp_prob +=x66 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x37 + x38 + x67 + x71  >=1

Lp_prob +=x31 + x32 + x33 + x34 + x38 + x68 + x71  >=1

Lp_prob +=x10 + x12 + x16 + x22 + x28 + x69 + x71  >=1

Lp_prob +=x24 + x25 + x26 + x27 + x28 + x70 + x71  >=1

Lp_prob +=x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x8 + x10 + x13 + x28 + x71 + x73  >=1

Lp_prob +=x8 + x10 + x28 + x71 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x72  >=1

Lp_prob +=x2 + x3 + x5 + x72  >=1

Lp_prob +=x3 + x5 + x72  >=1

Lp_prob +=x4 + x6 + x72  >=1

Lp_prob +=x5 + x72  >=1

Lp_prob +=x6 + x72  >=1

Lp_prob +=x5 + x7 + x72  >=1

Lp_prob +=x6 + x8 + x72  >=1

Lp_prob +=x6 + x9 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x72  >=1

Lp_prob +=x5 + x7 + x11 + x72  >=1

Lp_prob +=x6 + x8 + x12 + x13 + x72  >=1

Lp_prob +=x6 + x8 + x13 + x72  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x72  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x72  >=1

Lp_prob +=x6 + x8 + x12 + x13 + x16 + x72  >=1

Lp_prob +=x17 + x18 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x20 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x21 + x69 + x72 + x73 + x74  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x72  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x69 + x72 + x73 + x74  >=1

Lp_prob +=x6 + x8 + x13 + x14 + x15 + x22 + x24 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x25 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x26 + x27 + x28 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x27 + x28 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x28 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x26 + x27 + x28 + x29 + x72  >=1

Lp_prob +=x6 + x9 + x10 + x25 + x26 + x27 + x28 + x30 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x32 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x33 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x34 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x39 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x40 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x45 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x46 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x47 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x48 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x47 + x50 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x48 + x51 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x46 + x52 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x41 + x42 + x43 + x44 + x45 + x53 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x4 + x6 + x54 + x55 + x61 + x72  >=1

Lp_prob +=x4 + x6 + x55 + x61 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x57 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x35 + x36 + x49 + x56 + x58 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x39 + x59 + x66 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x60 + x66 + x71 + x72  >=1

Lp_prob +=x4 + x6 + x61 + x72  >=1

Lp_prob +=x6 + x9 + x62 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x62 + x63 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x64 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x62 + x64 + x65 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x66 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x37 + x38 + x66 + x67 + x71 + x72  >=1

Lp_prob +=x6 + x9 + x31 + x32 + x33 + x34 + x38 + x66 + x68 + x71 + x72  >=1

Lp_prob +=x18 + x19 + x69 + x72 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x69 + x70 + x72 + x73 + x74  >=1

Lp_prob +=x6 + x9 + x66 + x71 + x72  >=1

Lp_prob +=x72 + x73 + x74  >=1

Lp_prob +=x72 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x11 + x73  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x11 + x73  >=1

Lp_prob +=x3 + x5 + x7 + x11 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x73  >=1

Lp_prob +=x5 + x7 + x11 + x73  >=1

Lp_prob +=x6 + x8 + x13 + x73  >=1

Lp_prob +=x7 + x11 + x73  >=1

Lp_prob +=x8 + x13 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x73  >=1

Lp_prob +=x11 + x73  >=1

Lp_prob +=x12 + x13 + x73  >=1

Lp_prob +=x13 + x73  >=1

Lp_prob +=x13 + x14 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x73  >=1

Lp_prob +=x17 + x18 + x73  >=1

Lp_prob +=x18 + x73  >=1

Lp_prob +=x18 + x19 + x73  >=1

Lp_prob +=x18 + x19 + x20 + x73  >=1

Lp_prob +=x18 + x19 + x21 + x69 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x73  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x69 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x26 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x28 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x73  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x69 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x40 + x59 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x46 + x47 + x48 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x47 + x48 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x33 + x36 + x48 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x51 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x29 + x30 + x32 + x49 + x50 + x51 + x52 + x53 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x58 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x56 + x57 + x58 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x58 + x73  >=1

Lp_prob +=x12 + x13 + x16 + x25 + x30 + x31 + x39 + x59 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x60 + x73  >=1

Lp_prob +=x4 + x6 + x8 + x13 + x61 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x64 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x63 + x64 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x64 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x62 + x64 + x65 + x66 + x73  >=1

Lp_prob +=x6 + x8 + x9 + x13 + x66 + x73  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x67 + x69 + x73  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x68 + x73  >=1

Lp_prob +=x18 + x19 + x69 + x73  >=1

Lp_prob +=x18 + x19 + x69 + x70 + x73  >=1

Lp_prob +=x8 + x10 + x13 + x28 + x71 + x73  >=1

Lp_prob +=x72 + x73 + x74  >=1

Lp_prob +=x73 + x74  >=1

Lp_prob +=x1 + x2 + x3 + x5 + x7 + x74  >=1

Lp_prob +=x2 + x3 + x5 + x7 + x74  >=1

Lp_prob +=x3 + x5 + x7 + x74  >=1

Lp_prob +=x4 + x6 + x8 + x74  >=1

Lp_prob +=x5 + x7 + x74  >=1

Lp_prob +=x6 + x8 + x74  >=1

Lp_prob +=x7 + x74  >=1

Lp_prob +=x8 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x74  >=1

Lp_prob +=x8 + x10 + x74  >=1

Lp_prob +=x7 + x11 + x74  >=1

Lp_prob +=x12 + x13 + x73 + x74  >=1

Lp_prob +=x13 + x73 + x74  >=1

Lp_prob +=x13 + x14 + x73 + x74  >=1

Lp_prob +=x13 + x14 + x15 + x73 + x74  >=1

Lp_prob +=x12 + x13 + x16 + x73 + x74  >=1

Lp_prob +=x17 + x18 + x73 + x74  >=1

Lp_prob +=x18 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x20 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x21 + x69 + x73 + x74  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x69 + x73 + x74  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x73 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x74  >=1

Lp_prob +=x8 + x10 + x28 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x33 + x34 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x36 + x74  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x69 + x73 + x74  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x73 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x40 + x59 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x48 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x47 + x50 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x51 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x46 + x52 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x45 + x53 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x54 + x55 + x74  >=1

Lp_prob +=x8 + x10 + x27 + x28 + x34 + x35 + x41 + x42 + x43 + x44 + x55 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x74  >=1

Lp_prob +=x8 + x10 + x26 + x27 + x28 + x29 + x32 + x49 + x56 + x57 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x58 + x74  >=1

Lp_prob +=x8 + x10 + x25 + x26 + x27 + x28 + x30 + x31 + x39 + x59 + x74  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x60 + x73 + x74  >=1

Lp_prob +=x4 + x6 + x8 + x61 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x63 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x64 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x62 + x64 + x65 + x66 + x74  >=1

Lp_prob +=x6 + x8 + x9 + x66 + x74  >=1

Lp_prob +=x18 + x19 + x21 + x23 + x37 + x67 + x69 + x73 + x74  >=1

Lp_prob +=x13 + x14 + x15 + x22 + x24 + x38 + x68 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x69 + x73 + x74  >=1

Lp_prob +=x18 + x19 + x69 + x70 + x73 + x74  >=1

Lp_prob +=x8 + x10 + x28 + x71 + x74  >=1

Lp_prob +=x72 + x74  >=1

Lp_prob +=x73 + x74  >=1



#print(Lp_prob)
status = Lp_prob.solve()#solver
print(p.LpStatus[status]) #the solution status
print(p.value(Lp_prob.objective))
filepoint = open('opt_sol_var_val.txt','a')
filepoint.write	('\tx1	'+	str	(p.value(	x1	)))
filepoint.write	('\tx2	'+	str	(p.value(	x2	)))
filepoint.write	('\tx3	'+	str	(p.value(	x3	)))
filepoint.write	('\tx4	'+	str	(p.value(	x4	)))
filepoint.write	('\tx5	'+	str	(p.value(	x5	)))
filepoint.write	('\tx6	'+	str	(p.value(	x6	)))
filepoint.write	('\tx7	'+	str	(p.value(	x7	)))
filepoint.write	('\tx8	'+	str	(p.value(	x8	)))
filepoint.write	('\tx9	'+	str	(p.value(	x9	)))
filepoint.write	('\tx10	'+	str	(p.value(	x10	)))
filepoint.write	('\tx11	'+	str	(p.value(	x11	)))
filepoint.write	('\tx12	'+	str	(p.value(	x12	)))
filepoint.write	('\tx13	'+	str	(p.value(	x13	)))
filepoint.write	('\tx14	'+	str	(p.value(	x14	)))
filepoint.write	('\tx15	'+	str	(p.value(	x15	)))
filepoint.write	('\tx16	'+	str	(p.value(	x16	)))
filepoint.write	('\tx17	'+	str	(p.value(	x17	)))
filepoint.write	('\tx18	'+	str	(p.value(	x18	)))
filepoint.write	('\tx19	'+	str	(p.value(	x19	)))
filepoint.write	('\tx20	'+	str	(p.value(	x20	)))
filepoint.write	('\tx21	'+	str	(p.value(	x21	)))
filepoint.write	('\tx22	'+	str	(p.value(	x22	)))
filepoint.write	('\tx23	'+	str	(p.value(	x23	)))
filepoint.write	('\tx24	'+	str	(p.value(	x24	)))
filepoint.write	('\tx25	'+	str	(p.value(	x25	)))
filepoint.write	('\tx26	'+	str	(p.value(	x26	)))
filepoint.write	('\tx27	'+	str	(p.value(	x27	)))
filepoint.write	('\tx28	'+	str	(p.value(	x28	)))
filepoint.write	('\tx29	'+	str	(p.value(	x29	)))
filepoint.write	('\tx30	'+	str	(p.value(	x30	)))
filepoint.write	('\tx31	'+	str	(p.value(	x31	)))
filepoint.write	('\tx32	'+	str	(p.value(	x32	)))
filepoint.write	('\tx33	'+	str	(p.value(	x33	)))
filepoint.write	('\tx34	'+	str	(p.value(	x34	)))
filepoint.write	('\tx35	'+	str	(p.value(	x35	)))
filepoint.write	('\tx36	'+	str	(p.value(	x36	)))
filepoint.write	('\tx37	'+	str	(p.value(	x37	)))
filepoint.write	('\tx38	'+	str	(p.value(	x38	)))
filepoint.write	('\tx39	'+	str	(p.value(	x39	)))
filepoint.write	('\tx40	'+	str	(p.value(	x40	)))
filepoint.write	('\tx41	'+	str	(p.value(	x41	)))
filepoint.write	('\tx42	'+	str	(p.value(	x42	)))
filepoint.write	('\tx43	'+	str	(p.value(	x43	)))
filepoint.write	('\tx44	'+	str	(p.value(	x44	)))
filepoint.write	('\tx45	'+	str	(p.value(	x45	)))
filepoint.write	('\tx46	'+	str	(p.value(	x46	)))
filepoint.write	('\tx47	'+	str	(p.value(	x47	)))
filepoint.write	('\tx48	'+	str	(p.value(	x48	)))
filepoint.write	('\tx49	'+	str	(p.value(	x49	)))
filepoint.write	('\tx50	'+	str	(p.value(	x50	)))
filepoint.write	('\tx51	'+	str	(p.value(	x51	)))
filepoint.write	('\tx52	'+	str	(p.value(	x52	)))
filepoint.write	('\tx53	'+	str	(p.value(	x53	)))
filepoint.write	('\tx54	'+	str	(p.value(	x54	)))
filepoint.write	('\tx55	'+	str	(p.value(	x55	)))
filepoint.write	('\tx56	'+	str	(p.value(	x56	)))
filepoint.write	('\tx57	'+	str	(p.value(	x57	)))
filepoint.write	('\tx58	'+	str	(p.value(	x58	)))
filepoint.write	('\tx59	'+	str	(p.value(	x59	)))
filepoint.write	('\tx60	'+	str	(p.value(	x60	)))
filepoint.write	('\tx61	'+	str	(p.value(	x61	)))
filepoint.write	('\tx62	'+	str	(p.value(	x62	)))
filepoint.write	('\tx63	'+	str	(p.value(	x63	)))
filepoint.write	('\tx64	'+	str	(p.value(	x64	)))
filepoint.write	('\tx65	'+	str	(p.value(	x65	)))
filepoint.write	('\tx66	'+	str	(p.value(	x66	)))
filepoint.write	('\tx67	'+	str	(p.value(	x67	)))
filepoint.write	('\tx68	'+	str	(p.value(	x68	)))
filepoint.write	('\tx69	'+	str	(p.value(	x69	)))
filepoint.write	('\tx70	'+	str	(p.value(	x70	)))
filepoint.write	('\tx71	'+	str	(p.value(	x71	)))
filepoint.write	('\tx72	'+	str	(p.value(	x72	)))
filepoint.write	('\tx73	'+	str	(p.value(	x73	)))
filepoint.write	('\tx74	'+	str	(p.value(	x74	)))
filepoint.write	('\tx75	'+	str	(p.value(	x75	)))
filepoint.write	('\tx76	'+	str	(p.value(	x76	)))
filepoint.write	('\tx77	'+	str	(p.value(	x77	)))
filepoint.write	('\tx78	'+	str	(p.value(	x78	)))
filepoint.write	('\tx79	'+	str	(p.value(	x79	)))
filepoint.write	('\tx80	'+	str	(p.value(	x80	)))
filepoint.write	('\tx81	'+	str	(p.value(	x81	)))
filepoint.write	('\tx82	'+	str	(p.value(	x82	)))
filepoint.write	('\tx83	'+	str	(p.value(	x83	)))
filepoint.write	('\tx84	'+	str	(p.value(	x84	)))
filepoint.write	('\tx85	'+	str	(p.value(	x85	)))
filepoint.write	('\tx86	'+	str	(p.value(	x86	)))
filepoint.write	('\tx87	'+	str	(p.value(	x87	)))
filepoint.write	('\tx88	'+	str	(p.value(	x88	)))
filepoint.write	('\tx89	'+	str	(p.value(	x89	)))
filepoint.write	('\tx90	'+	str	(p.value(	x90	)))
filepoint.write	('\tx91	'+	str	(p.value(	x91	)))
filepoint.write	('\tx92	'+	str	(p.value(	x92	)))
filepoint.write	('\tx93	'+	str	(p.value(	x93	)))
filepoint.write	('\tx94	'+	str	(p.value(	x94	)))
filepoint.write	('\tx95	'+	str	(p.value(	x95	)))
filepoint.write	('\tx96	'+	str	(p.value(	x96	)))
filepoint.write	('\tx97	'+	str	(p.value(	x97	)))
filepoint.write	('\tx98	'+	str	(p.value(	x98	)))
filepoint.write	('\tx99	'+	str	(p.value(	x99	)))
filepoint.write	('\tx100	'+	str	(p.value(	x100	)))
filepoint.write	('\tx101	'+	str	(p.value(	x101	)))
filepoint.write	('\tx102	'+	str	(p.value(	x102	)))
filepoint.write	('\tx103	'+	str	(p.value(	x103	)))
filepoint.write	('\tx104	'+	str	(p.value(	x104	)))
filepoint.write	('\tx105	'+	str	(p.value(	x105	)))
filepoint.write	('\tx106	'+	str	(p.value(	x106	)))
filepoint.write	('\tx107	'+	str	(p.value(	x107	)))
filepoint.write	('\tx108	'+	str	(p.value(	x108	)))
filepoint.write	('\tx109	'+	str	(p.value(	x109	)))
filepoint.write	('\tx110	'+	str	(p.value(	x110	)))
filepoint.write	('\tx111	'+	str	(p.value(	x111	)))
filepoint.write	('\tx112	'+	str	(p.value(	x112	)))
filepoint.write	('\tx113	'+	str	(p.value(	x113	)))
filepoint.write	('\tx114	'+	str	(p.value(	x114	)))
filepoint.write	('\tx115	'+	str	(p.value(	x115	)))
filepoint.write	('\tx116	'+	str	(p.value(	x116	)))
filepoint.write	('\tx117	'+	str	(p.value(	x117	)))
filepoint.write	('\tx118	'+	str	(p.value(	x118	)))
filepoint.write	('\tx119	'+	str	(p.value(	x119	)))
filepoint.write	('\tx120	'+	str	(p.value(	x120	)))
filepoint.write	('\tx121	'+	str	(p.value(	x121	)))
filepoint.write	('\tx122	'+	str	(p.value(	x122	)))
filepoint.write	('\tx123	'+	str	(p.value(	x123	)))
filepoint.write	('\tx124	'+	str	(p.value(	x124	)))
filepoint.write	('\tx125	'+	str	(p.value(	x125	)))
filepoint.write	('\tx126	'+	str	(p.value(	x126	)))
filepoint.write	('\tx127	'+	str	(p.value(	x127	)))
filepoint.write	('\tx128	'+	str	(p.value(	x128	)))
filepoint.write	('\tx129	'+	str	(p.value(	x129	)))
filepoint.write	('\tx130	'+	str	(p.value(	x130	)))
filepoint.write	('\tx131	'+	str	(p.value(	x131	)))
filepoint.write	('\tx132	'+	str	(p.value(	x132	)))
filepoint.write	('\tx133	'+	str	(p.value(	x133	)))
filepoint.write	('\tx134	'+	str	(p.value(	x134	)))
filepoint.write	('\tx135	'+	str	(p.value(	x135	)))
filepoint.write	('\tx136	'+	str	(p.value(	x136	)))
filepoint.write	('\tx137	'+	str	(p.value(	x137	)))
filepoint.write	('\tx138	'+	str	(p.value(	x138	)))
filepoint.write	('\tx139	'+	str	(p.value(	x139	)))
filepoint.write	('\tx140	'+	str	(p.value(	x140	)))
filepoint.write	('\tx141	'+	str	(p.value(	x141	)))
filepoint.write	('\tx142	'+	str	(p.value(	x142	)))
filepoint.write	('\tx143	'+	str	(p.value(	x143	)))
filepoint.write	('\tx144	'+	str	(p.value(	x144	)))
filepoint.write	('\tx145	'+	str	(p.value(	x145	)))
filepoint.write	('\tx146	'+	str	(p.value(	x146	)))
filepoint.write	('\tx147	'+	str	(p.value(	x147	)))
filepoint.write	('\tx148	'+	str	(p.value(	x148	)))
filepoint.write	('\tx149	'+	str	(p.value(	x149	)))
filepoint.write	('\tx150	'+	str	(p.value(	x150	)))
filepoint.write	('\tx151	'+	str	(p.value(	x151	)))
filepoint.write	('\tx152	'+	str	(p.value(	x152	)))
filepoint.write	('\tx153	'+	str	(p.value(	x153	)))
filepoint.write	('\tx154	'+	str	(p.value(	x154	)))
filepoint.write	('\tx155	'+	str	(p.value(	x155	)))
filepoint.write	('\tx156	'+	str	(p.value(	x156	)))
filepoint.write	('\tx157	'+	str	(p.value(	x157	)))
filepoint.write	('\tx158	'+	str	(p.value(	x158	)))
filepoint.write	('\tx159	'+	str	(p.value(	x159	)))
filepoint.write	('\tx160	'+	str	(p.value(	x160	)))
filepoint.write	('\tx161	'+	str	(p.value(	x161	)))
filepoint.write	('\tx162	'+	str	(p.value(	x162	)))
filepoint.write	('\tx163	'+	str	(p.value(	x163	)))
filepoint.write	('\tx164	'+	str	(p.value(	x164	)))
filepoint.write	('\tx165	'+	str	(p.value(	x165	)))
filepoint.write	('\tx166	'+	str	(p.value(	x166	)))
filepoint.write	('\tx167	'+	str	(p.value(	x167	)))
filepoint.write	('\tx168	'+	str	(p.value(	x168	)))
filepoint.write	('\tx169	'+	str	(p.value(	x169	)))
filepoint.write	('\tx170	'+	str	(p.value(	x170	)))
filepoint.write	('\tx171	'+	str	(p.value(	x171	)))
filepoint.write	('\tx172	'+	str	(p.value(	x172	)))
filepoint.write	('\tx173	'+	str	(p.value(	x173	)))
filepoint.write	('\tx174	'+	str	(p.value(	x174	)))
filepoint.write	('\tx175	'+	str	(p.value(	x175	)))
filepoint.write	('\tx176	'+	str	(p.value(	x176	)))
filepoint.write	('\tx177	'+	str	(p.value(	x177	)))
filepoint.write	('\tx178	'+	str	(p.value(	x178	)))
filepoint.write	('\tx179	'+	str	(p.value(	x179	)))
filepoint.write	('\tx180	'+	str	(p.value(	x180	)))
filepoint.write	('\tx181	'+	str	(p.value(	x181	)))
filepoint.write	('\tx182	'+	str	(p.value(	x182	)))
filepoint.write	('\tx183	'+	str	(p.value(	x183	)))
filepoint.write	('\tx184	'+	str	(p.value(	x184	)))
filepoint.write	('\tx185	'+	str	(p.value(	x185	)))
filepoint.write	('\tx186	'+	str	(p.value(	x186	)))
filepoint.write	('\tx187	'+	str	(p.value(	x187	)))
filepoint.write	('\tx188	'+	str	(p.value(	x188	)))
filepoint.write	('\tx189	'+	str	(p.value(	x189	)))
filepoint.write	('\tx190	'+	str	(p.value(	x190	)))
filepoint.write	('\tx191	'+	str	(p.value(	x191	)))
filepoint.write	('\tx192	'+	str	(p.value(	x192	)))
filepoint.write	('\tx193	'+	str	(p.value(	x193	)))
filepoint.write	('\tx194	'+	str	(p.value(	x194	)))
filepoint.write	('\tx195	'+	str	(p.value(	x195	)))
filepoint.write	('\tx196	'+	str	(p.value(	x196	)))
filepoint.write	('\tx197	'+	str	(p.value(	x197	)))
filepoint.write	('\tx198	'+	str	(p.value(	x198	)))
filepoint.write	('\tx199	'+	str	(p.value(	x199	)))
filepoint.write	('\tx200	'+	str	(p.value(	x200	)))
filepoint.write	('\tx201	'+	str	(p.value(	x201	)))
filepoint.write	('\tx202	'+	str	(p.value(	x202	)))
filepoint.write	('\tx203	'+	str	(p.value(	x203	)))
filepoint.write	('\tx204	'+	str	(p.value(	x204	)))
filepoint.write	('\tx205	'+	str	(p.value(	x205	)))
filepoint.write	('\tx206	'+	str	(p.value(	x206	)))
filepoint.write	('\tx207	'+	str	(p.value(	x207	)))
filepoint.write	('\tx208	'+	str	(p.value(	x208	)))
filepoint.write	('\tx209	'+	str	(p.value(	x209	)))
filepoint.write	('\tx210	'+	str	(p.value(	x210	)))
filepoint.write	('\tx211	'+	str	(p.value(	x211	)))
filepoint.write	('\tx212	'+	str	(p.value(	x212	)))
filepoint.write	('\tx213	'+	str	(p.value(	x213	)))
filepoint.write	('\tx214	'+	str	(p.value(	x214	)))
filepoint.write	('\tx215	'+	str	(p.value(	x215	)))
filepoint.write	('\tx216	'+	str	(p.value(	x216	)))
filepoint.write	('\tx217	'+	str	(p.value(	x217	)))
filepoint.write	('\tx218	'+	str	(p.value(	x218	)))
filepoint.write	('\tx219	'+	str	(p.value(	x219	)))
filepoint.write	('\tx220	'+	str	(p.value(	x220	)))
filepoint.write	('\tx221	'+	str	(p.value(	x221	)))
filepoint.write	('\tx222	'+	str	(p.value(	x222	)))
filepoint.write	('\tx223	'+	str	(p.value(	x223	)))
filepoint.write	('\tx224	'+	str	(p.value(	x224	)))
filepoint.write	('\tx225	'+	str	(p.value(	x225	)))
filepoint.write	('\tx226	'+	str	(p.value(	x226	)))
filepoint.write	('\tx227	'+	str	(p.value(	x227	)))
filepoint.write	('\tx228	'+	str	(p.value(	x228	)))
filepoint.write	('\tx229	'+	str	(p.value(	x229	)))
filepoint.write	('\tx230	'+	str	(p.value(	x230	)))
filepoint.write	('\tx231	'+	str	(p.value(	x231	)))
filepoint.write	('\tx232	'+	str	(p.value(	x232	)))
filepoint.write	('\tx233	'+	str	(p.value(	x233	)))
filepoint.write	('\tx234	'+	str	(p.value(	x234	)))
filepoint.write	('\tx235	'+	str	(p.value(	x235	)))
filepoint.write	('\tx236	'+	str	(p.value(	x236	)))
filepoint.write	('\tx237	'+	str	(p.value(	x237	)))
filepoint.write	('\tx238	'+	str	(p.value(	x238	)))
filepoint.write	('\tx239	'+	str	(p.value(	x239	)))
filepoint.write	('\tx240	'+	str	(p.value(	x240	)))
filepoint.write	('\tx241	'+	str	(p.value(	x241	)))
filepoint.write	('\tx242	'+	str	(p.value(	x242	)))
filepoint.write	('\tx243	'+	str	(p.value(	x243	)))
filepoint.write	('\tx244	'+	str	(p.value(	x244	)))
filepoint.write	('\tx245	'+	str	(p.value(	x245	)))
filepoint.write	('\tx246	'+	str	(p.value(	x246	)))
filepoint.write	('\tx247	'+	str	(p.value(	x247	)))
filepoint.write	('\tx248	'+	str	(p.value(	x248	)))
filepoint.write	('\tx249	'+	str	(p.value(	x249	)))
filepoint.write	('\tx250	'+	str	(p.value(	x250	)))
filepoint.write	('\tx251	'+	str	(p.value(	x251	)))
filepoint.write	('\tx252	'+	str	(p.value(	x252	)))
filepoint.write	('\tx253	'+	str	(p.value(	x253	)))
filepoint.write	('\tx254	'+	str	(p.value(	x254	)))
filepoint.write	('\tx255	'+	str	(p.value(	x255	)))
filepoint.write	('\tx256	'+	str	(p.value(	x256	)))
filepoint.write	('\tx257	'+	str	(p.value(	x257	)))
filepoint.write	('\tx258	'+	str	(p.value(	x258	)))
filepoint.write	('\tx259	'+	str	(p.value(	x259	)))
filepoint.write	('\tx260	'+	str	(p.value(	x260	)))
filepoint.write	('\tx261	'+	str	(p.value(	x261	)))
filepoint.write	('\tx262	'+	str	(p.value(	x262	)))
filepoint.write	('\tx263	'+	str	(p.value(	x263	)))
filepoint.write	('\tx264	'+	str	(p.value(	x264	)))
filepoint.write	('\tx265	'+	str	(p.value(	x265	)))
filepoint.write	('\tx266	'+	str	(p.value(	x266	)))
filepoint.write	('\tx267	'+	str	(p.value(	x267	)))
filepoint.write	('\tx268	'+	str	(p.value(	x268	)))
filepoint.write	('\tx269	'+	str	(p.value(	x269	)))
filepoint.write	('\tx270	'+	str	(p.value(	x270	)))
filepoint.write	('\tx271	'+	str	(p.value(	x271	)))
filepoint.write	('\tx272	'+	str	(p.value(	x272	)))
filepoint.write	('\tx273	'+	str	(p.value(	x273	)))
filepoint.write	('\tx274	'+	str	(p.value(	x274	)))
filepoint.write	('\tx275	'+	str	(p.value(	x275	)))
filepoint.write	('\tx276	'+	str	(p.value(	x276	)))
filepoint.write	('\tx277	'+	str	(p.value(	x277	)))
filepoint.write	('\tx278	'+	str	(p.value(	x278	)))
filepoint.write	('\tx279	'+	str	(p.value(	x279	)))
filepoint.write	('\tx280	'+	str	(p.value(	x280	)))
filepoint.write	('\tx281	'+	str	(p.value(	x281	)))
filepoint.write	('\tx282	'+	str	(p.value(	x282	)))
filepoint.write	('\tx283	'+	str	(p.value(	x283	)))
filepoint.write	('\tx284	'+	str	(p.value(	x284	)))
filepoint.write	('\tx285	'+	str	(p.value(	x285	)))
filepoint.write	('\tx286	'+	str	(p.value(	x286	)))
filepoint.write	('\tx287	'+	str	(p.value(	x287	)))
filepoint.write	('\tx288	'+	str	(p.value(	x288	)))
filepoint.write	('\tx289	'+	str	(p.value(	x289	)))
filepoint.write	('\tx290	'+	str	(p.value(	x290	)))
filepoint.write	('\tx291	'+	str	(p.value(	x291	)))
filepoint.write	('\tx292	'+	str	(p.value(	x292	)))
filepoint.write	('\tx293	'+	str	(p.value(	x293	)))
filepoint.write	('\tx294	'+	str	(p.value(	x294	)))
filepoint.write	('\tx295	'+	str	(p.value(	x295	)))
filepoint.write	('\tx296	'+	str	(p.value(	x296	)))
filepoint.write	('\tx297	'+	str	(p.value(	x297	)))
filepoint.write	('\tx298	'+	str	(p.value(	x298	)))
filepoint.write	('\tx299	'+	str	(p.value(	x299	)))
filepoint.write	('\tx300	'+	str	(p.value(	x300	)))
filepoint.write	('\tx301	'+	str	(p.value(	x301	)))
filepoint.write	('\tx302	'+	str	(p.value(	x302	)))
filepoint.write	('\tx303	'+	str	(p.value(	x303	)))
filepoint.write	('\tx304	'+	str	(p.value(	x304	)))
filepoint.write	('\tx305	'+	str	(p.value(	x305	)))
filepoint.write	('\tx306	'+	str	(p.value(	x306	)))
filepoint.write	('\tx307	'+	str	(p.value(	x307	)))
filepoint.write	('\tx308	'+	str	(p.value(	x308	)))
filepoint.write	('\tx309	'+	str	(p.value(	x309	)))
filepoint.write	('\tx310	'+	str	(p.value(	x310	)))
filepoint.write	('\tx311	'+	str	(p.value(	x311	)))
filepoint.write	('\tx312	'+	str	(p.value(	x312	)))
filepoint.write	('\tx313	'+	str	(p.value(	x313	)))
filepoint.write	('\tx314	'+	str	(p.value(	x314	)))
filepoint.write	('\tx315	'+	str	(p.value(	x315	)))
filepoint.write	('\tx316	'+	str	(p.value(	x316	)))
filepoint.write	('\tx317	'+	str	(p.value(	x317	)))
filepoint.write	('\tx318	'+	str	(p.value(	x318	)))
filepoint.write	('\tx319	'+	str	(p.value(	x319	)))
filepoint.write	('\tx320	'+	str	(p.value(	x320	)))
filepoint.write	('\tx321	'+	str	(p.value(	x321	)))
filepoint.write	('\tx322	'+	str	(p.value(	x322	)))
filepoint.write	('\tx323	'+	str	(p.value(	x323	)))
filepoint.write	('\tx324	'+	str	(p.value(	x324	)))
filepoint.write	('\tx325	'+	str	(p.value(	x325	)))
filepoint.write	('\tx326	'+	str	(p.value(	x326	)))
filepoint.write	('\tx327	'+	str	(p.value(	x327	)))
filepoint.write	('\tx328	'+	str	(p.value(	x328	)))
filepoint.write	('\tx329	'+	str	(p.value(	x329	)))
filepoint.write	('\tx330	'+	str	(p.value(	x330	)))
filepoint.write	('\tx331	'+	str	(p.value(	x331	)))
filepoint.write	('\tx332	'+	str	(p.value(	x332	)))
filepoint.write	('\tx333	'+	str	(p.value(	x333	)))
filepoint.write	('\tx334	'+	str	(p.value(	x334	)))
filepoint.write	('\tx335	'+	str	(p.value(	x335	)))
filepoint.write	('\tx336	'+	str	(p.value(	x336	)))
filepoint.write	('\tx337	'+	str	(p.value(	x337	)))
filepoint.write	('\tx338	'+	str	(p.value(	x338	)))
filepoint.write	('\tx339	'+	str	(p.value(	x339	)))
filepoint.write	('\tx340	'+	str	(p.value(	x340	)))
filepoint.write	('\tx341	'+	str	(p.value(	x341	)))
filepoint.write	('\tx342	'+	str	(p.value(	x342	)))
filepoint.write	('\tx343	'+	str	(p.value(	x343	)))
filepoint.write	('\tx344	'+	str	(p.value(	x344	)))
filepoint.write	('\tx345	'+	str	(p.value(	x345	)))
filepoint.write	('\tx346	'+	str	(p.value(	x346	)))
filepoint.write	('\tx347	'+	str	(p.value(	x347	)))
filepoint.write	('\tx348	'+	str	(p.value(	x348	)))
filepoint.write	('\tx349	'+	str	(p.value(	x349	)))
filepoint.write	('\tx350	'+	str	(p.value(	x350	)))
filepoint.write	('\tx351	'+	str	(p.value(	x351	)))
filepoint.write	('\tx352	'+	str	(p.value(	x352	)))
filepoint.write	('\tx353	'+	str	(p.value(	x353	)))
filepoint.write	('\tx354	'+	str	(p.value(	x354	)))
filepoint.write	('\tx355	'+	str	(p.value(	x355	)))
filepoint.write	('\tx356	'+	str	(p.value(	x356	)))
filepoint.write	('\tx357	'+	str	(p.value(	x357	)))
filepoint.write	('\tx358	'+	str	(p.value(	x358	)))
filepoint.write	('\tx359	'+	str	(p.value(	x359	)))
filepoint.write	('\tx360	'+	str	(p.value(	x360	)))
filepoint.write	('\tx361	'+	str	(p.value(	x361	)))
filepoint.write	('\tx362	'+	str	(p.value(	x362	)))
filepoint.write	('\tx363	'+	str	(p.value(	x363	)))
filepoint.write	('\tx364	'+	str	(p.value(	x364	)))
filepoint.write	('\tx365	'+	str	(p.value(	x365	)))
filepoint.write	('\tx366	'+	str	(p.value(	x366	)))
filepoint.write	('\tx367	'+	str	(p.value(	x367	)))
filepoint.write	('\tx368	'+	str	(p.value(	x368	)))
filepoint.write	('\tx369	'+	str	(p.value(	x369	)))
filepoint.write	('\tx370	'+	str	(p.value(	x370	)))
filepoint.write	('\tx371	'+	str	(p.value(	x371	)))
filepoint.write	('\tx372	'+	str	(p.value(	x372	)))
filepoint.write	('\tx373	'+	str	(p.value(	x373	)))
filepoint.write	('\tx374	'+	str	(p.value(	x374	)))
filepoint.write	('\tx375	'+	str	(p.value(	x375	)))
filepoint.write	('\tx376	'+	str	(p.value(	x376	)))
filepoint.write	('\tx377	'+	str	(p.value(	x377	)))
filepoint.write	('\tx378	'+	str	(p.value(	x378	)))
filepoint.write	('\tx379	'+	str	(p.value(	x379	)))
filepoint.write	('\tx380	'+	str	(p.value(	x380	)))
filepoint.write	('\tx381	'+	str	(p.value(	x381	)))
filepoint.write	('\tx382	'+	str	(p.value(	x382	)))
filepoint.write	('\tx383	'+	str	(p.value(	x383	)))
filepoint.write	('\tx384	'+	str	(p.value(	x384	)))
filepoint.write	('\tx385	'+	str	(p.value(	x385	)))
filepoint.write	('\tx386	'+	str	(p.value(	x386	)))
filepoint.write	('\tx387	'+	str	(p.value(	x387	)))
filepoint.write	('\tx388	'+	str	(p.value(	x388	)))
filepoint.write	('\tx389	'+	str	(p.value(	x389	)))
filepoint.write	('\tx390	'+	str	(p.value(	x390	)))
filepoint.write	('\tx391	'+	str	(p.value(	x391	)))
filepoint.write	('\tx392	'+	str	(p.value(	x392	)))
filepoint.write	('\tx393	'+	str	(p.value(	x393	)))
filepoint.write	('\tx394	'+	str	(p.value(	x394	)))
filepoint.write	('\tx395	'+	str	(p.value(	x395	)))
filepoint.write	('\tx396	'+	str	(p.value(	x396	)))
filepoint.write	('\tx397	'+	str	(p.value(	x397	)))
filepoint.write	('\tx398	'+	str	(p.value(	x398	)))
filepoint.write	('\tx399	'+	str	(p.value(	x399	)))
filepoint.write	('\tx400	'+	str	(p.value(	x400	)))
filepoint.write	('\tx401	'+	str	(p.value(	x401	)))
filepoint.write	('\tx402	'+	str	(p.value(	x402	)))
filepoint.write	('\tx403	'+	str	(p.value(	x403	)))
filepoint.write	('\tx404	'+	str	(p.value(	x404	)))
filepoint.write	('\tx405	'+	str	(p.value(	x405	)))
filepoint.write	('\tx406	'+	str	(p.value(	x406	)))
filepoint.write	('\tx407	'+	str	(p.value(	x407	)))
filepoint.write	('\tx408	'+	str	(p.value(	x408	)))
filepoint.write	('\tx409	'+	str	(p.value(	x409	)))
filepoint.write	('\tx410	'+	str	(p.value(	x410	)))
filepoint.write	('\tx411	'+	str	(p.value(	x411	)))
filepoint.write	('\tx412	'+	str	(p.value(	x412	)))
filepoint.write	('\tx413	'+	str	(p.value(	x413	)))
filepoint.write	('\tx414	'+	str	(p.value(	x414	)))
filepoint.write	('\tx415	'+	str	(p.value(	x415	)))
filepoint.write	('\tx416	'+	str	(p.value(	x416	)))
filepoint.write	('\tx417	'+	str	(p.value(	x417	)))
filepoint.write	('\tx418	'+	str	(p.value(	x418	)))
filepoint.write	('\tx419	'+	str	(p.value(	x419	)))
filepoint.write	('\tx420	'+	str	(p.value(	x420	)))
filepoint.write	('\tx421	'+	str	(p.value(	x421	)))
filepoint.write	('\tx422	'+	str	(p.value(	x422	)))
filepoint.write	('\tx423	'+	str	(p.value(	x423	)))
filepoint.write	('\tx424	'+	str	(p.value(	x424	)))
filepoint.write	('\tx425	'+	str	(p.value(	x425	)))
filepoint.write	('\tx426	'+	str	(p.value(	x426	)))
filepoint.write	('\tx427	'+	str	(p.value(	x427	)))
filepoint.write	('\tx428	'+	str	(p.value(	x428	)))
filepoint.write	('\tx429	'+	str	(p.value(	x429	)))
filepoint.write	('\tx430	'+	str	(p.value(	x430	)))
filepoint.write	('\tx431	'+	str	(p.value(	x431	)))
filepoint.write	('\tx432	'+	str	(p.value(	x432	)))
filepoint.write	('\tx433	'+	str	(p.value(	x433	)))
filepoint.write	('\tx434	'+	str	(p.value(	x434	)))
filepoint.write	('\tx435	'+	str	(p.value(	x435	)))
filepoint.write	('\tx436	'+	str	(p.value(	x436	)))
filepoint.write	('\tx437	'+	str	(p.value(	x437	)))
filepoint.write	('\tx438	'+	str	(p.value(	x438	)))
filepoint.write	('\tx439	'+	str	(p.value(	x439	)))
filepoint.write	('\tx440	'+	str	(p.value(	x440	)))
filepoint.write	('\tx441	'+	str	(p.value(	x441	)))
filepoint.write	('\tx442	'+	str	(p.value(	x442	)))
filepoint.write	('\tx443	'+	str	(p.value(	x443	)))
filepoint.write	('\tx444	'+	str	(p.value(	x444	)))
filepoint.write	('\tx445	'+	str	(p.value(	x445	)))
filepoint.write	('\tx446	'+	str	(p.value(	x446	)))
filepoint.write	('\tx447	'+	str	(p.value(	x447	)))
filepoint.write	('\tx448	'+	str	(p.value(	x448	)))
filepoint.write	('\tx449	'+	str	(p.value(	x449	)))
filepoint.write	('\tx450	'+	str	(p.value(	x450	)))
filepoint.write	('\tx451	'+	str	(p.value(	x451	)))
filepoint.write	('\tx452	'+	str	(p.value(	x452	)))
filepoint.write	('\tx453	'+	str	(p.value(	x453	)))
filepoint.write	('\tx454	'+	str	(p.value(	x454	)))
filepoint.write	('\tx455	'+	str	(p.value(	x455	)))
filepoint.write	('\tx456	'+	str	(p.value(	x456	)))
filepoint.write	('\tx457	'+	str	(p.value(	x457	)))
filepoint.write	('\tx458	'+	str	(p.value(	x458	)))
filepoint.write	('\tx459	'+	str	(p.value(	x459	)))
filepoint.write	('\tx460	'+	str	(p.value(	x460	)))
filepoint.write	('\tx461	'+	str	(p.value(	x461	)))
filepoint.write	('\tx462	'+	str	(p.value(	x462	)))
filepoint.write	('\tx463	'+	str	(p.value(	x463	)))
filepoint.write	('\tx464	'+	str	(p.value(	x464	)))
filepoint.write	('\tx465	'+	str	(p.value(	x465	)))
filepoint.write	('\tx466	'+	str	(p.value(	x466	)))
filepoint.write	('\tx467	'+	str	(p.value(	x467	)))
filepoint.write	('\tx468	'+	str	(p.value(	x468	)))
filepoint.write	('\tx469	'+	str	(p.value(	x469	)))
filepoint.write	('\tx470	'+	str	(p.value(	x470	)))
filepoint.write	('\tx471	'+	str	(p.value(	x471	)))
filepoint.write	('\tx472	'+	str	(p.value(	x472	)))
filepoint.write	('\tx473	'+	str	(p.value(	x473	)))
filepoint.write	('\tx474	'+	str	(p.value(	x474	)))
filepoint.write	('\tx475	'+	str	(p.value(	x475	)))
filepoint.write	('\tx476	'+	str	(p.value(	x476	)))
filepoint.write	('\tx477	'+	str	(p.value(	x477	)))
filepoint.write	('\tx478	'+	str	(p.value(	x478	)))
filepoint.write	('\tx479	'+	str	(p.value(	x479	)))
filepoint.write	('\tx480	'+	str	(p.value(	x480	)))
filepoint.write	('\tx481	'+	str	(p.value(	x481	)))
filepoint.write	('\tx482	'+	str	(p.value(	x482	)))
filepoint.write	('\tx483	'+	str	(p.value(	x483	)))
filepoint.write	('\tx484	'+	str	(p.value(	x484	)))
filepoint.write	('\tx485	'+	str	(p.value(	x485	)))
filepoint.write	('\tx486	'+	str	(p.value(	x486	)))
filepoint.write	('\tx487	'+	str	(p.value(	x487	)))
filepoint.write	('\tx488	'+	str	(p.value(	x488	)))
filepoint.write	('\tx489	'+	str	(p.value(	x489	)))
filepoint.write	('\tx490	'+	str	(p.value(	x490	)))
filepoint.write	('\tx491	'+	str	(p.value(	x491	)))
filepoint.write	('\tx492	'+	str	(p.value(	x492	)))
filepoint.write	('\tx493	'+	str	(p.value(	x493	)))
filepoint.write	('\tx494	'+	str	(p.value(	x494	)))
filepoint.write	('\tx495	'+	str	(p.value(	x495	)))
filepoint.write	('\tx496	'+	str	(p.value(	x496	)))
filepoint.write	('\tx497	'+	str	(p.value(	x497	)))
filepoint.write	('\tx498	'+	str	(p.value(	x498	)))
filepoint.write	('\tx499	'+	str	(p.value(	x499	)))
filepoint.write	('\tx500	'+	str	(p.value(	x500	)))
filepoint.write	('\tx501	'+	str	(p.value(	x501	)))
filepoint.write	('\tx502	'+	str	(p.value(	x502	)))
filepoint.write	('\tx503	'+	str	(p.value(	x503	)))
filepoint.write	('\tx504	'+	str	(p.value(	x504	)))
filepoint.write	('\tx505	'+	str	(p.value(	x505	)))
filepoint.write	('\tx506	'+	str	(p.value(	x506	)))
filepoint.write	('\tx507	'+	str	(p.value(	x507	)))
filepoint.write	('\tx508	'+	str	(p.value(	x508	)))
filepoint.write	('\tx509	'+	str	(p.value(	x509	)))
filepoint.write	('\tx510	'+	str	(p.value(	x510	)))
filepoint.write	('\tx511	'+	str	(p.value(	x511	)))
filepoint.write	('\tx512	'+	str	(p.value(	x512	)))
filepoint.write	('\tx513	'+	str	(p.value(	x513	)))
filepoint.write	('\tx514	'+	str	(p.value(	x514	)))
filepoint.write	('\tx515	'+	str	(p.value(	x515	)))
filepoint.write	('\tx516	'+	str	(p.value(	x516	)))
filepoint.write	('\tx517	'+	str	(p.value(	x517	)))
filepoint.write	('\tx518	'+	str	(p.value(	x518	)))
filepoint.write	('\tx519	'+	str	(p.value(	x519	)))
filepoint.write	('\tx520	'+	str	(p.value(	x520	)))
filepoint.write	('\tx521	'+	str	(p.value(	x521	)))
filepoint.write	('\tx522	'+	str	(p.value(	x522	)))
filepoint.write	('\tx523	'+	str	(p.value(	x523	)))
filepoint.write	('\tx524	'+	str	(p.value(	x524	)))
filepoint.write	('\tx525	'+	str	(p.value(	x525	)))
filepoint.write	('\tx526	'+	str	(p.value(	x526	)))
filepoint.write	('\tx527	'+	str	(p.value(	x527	)))
filepoint.write	('\tx528	'+	str	(p.value(	x528	)))
filepoint.write	('\tx529	'+	str	(p.value(	x529	)))
filepoint.write	('\tx530	'+	str	(p.value(	x530	)))
filepoint.write	('\tx531	'+	str	(p.value(	x531	)))
filepoint.write	('\tx532	'+	str	(p.value(	x532	)))
filepoint.write	('\tx533	'+	str	(p.value(	x533	)))
filepoint.write	('\tx534	'+	str	(p.value(	x534	)))
filepoint.write	('\tx535	'+	str	(p.value(	x535	)))
filepoint.write	('\tx536	'+	str	(p.value(	x536	)))
filepoint.write	('\tx537	'+	str	(p.value(	x537	)))
filepoint.write	('\tx538	'+	str	(p.value(	x538	)))
filepoint.write	('\tx539	'+	str	(p.value(	x539	)))
filepoint.write	('\tx540	'+	str	(p.value(	x540	)))
filepoint.write	('\tx541	'+	str	(p.value(	x541	)))
filepoint.write	('\tx542	'+	str	(p.value(	x542	)))
filepoint.write	('\tx543	'+	str	(p.value(	x543	)))
filepoint.write	('\tx544	'+	str	(p.value(	x544	)))
filepoint.write	('\tx545	'+	str	(p.value(	x545	)))
filepoint.write	('\tx546	'+	str	(p.value(	x546	)))
filepoint.write	('\tx547	'+	str	(p.value(	x547	)))
filepoint.write	('\tx548	'+	str	(p.value(	x548	)))
filepoint.write	('\tx549	'+	str	(p.value(	x549	)))
filepoint.write	('\tx550	'+	str	(p.value(	x550	)))
filepoint.write	('\tx551	'+	str	(p.value(	x551	)))
filepoint.write	('\tx552	'+	str	(p.value(	x552	)))
filepoint.write	('\tx553	'+	str	(p.value(	x553	)))
filepoint.write	('\tx554	'+	str	(p.value(	x554	)))
filepoint.write	('\tx555	'+	str	(p.value(	x555	)))
filepoint.write	('\tx556	'+	str	(p.value(	x556	)))
filepoint.write	('\tx557	'+	str	(p.value(	x557	)))
filepoint.write	('\tx558	'+	str	(p.value(	x558	)))
filepoint.write	('\tx559	'+	str	(p.value(	x559	)))
filepoint.write	('\tx560	'+	str	(p.value(	x560	)))
filepoint.write	('\tx561	'+	str	(p.value(	x561	)))
filepoint.write	('\tx562	'+	str	(p.value(	x562	)))
filepoint.write	('\tx563	'+	str	(p.value(	x563	)))
filepoint.write	('\tx564	'+	str	(p.value(	x564	)))
filepoint.write	('\tx565	'+	str	(p.value(	x565	)))
filepoint.write	('\tx566	'+	str	(p.value(	x566	)))
filepoint.write	('\tx567	'+	str	(p.value(	x567	)))
filepoint.write	('\tx568	'+	str	(p.value(	x568	)))
filepoint.write	('\tx569	'+	str	(p.value(	x569	)))
filepoint.write	('\tx570	'+	str	(p.value(	x570	)))
filepoint.write	('\tx571	'+	str	(p.value(	x571	)))
filepoint.write	('\tx572	'+	str	(p.value(	x572	)))
filepoint.write	('\tx573	'+	str	(p.value(	x573	)))
filepoint.write	('\tx574	'+	str	(p.value(	x574	)))
filepoint.write	('\tx575	'+	str	(p.value(	x575	)))
filepoint.write	('\tx576	'+	str	(p.value(	x576	)))
filepoint.write	('\tx577	'+	str	(p.value(	x577	)))
filepoint.write	('\tx578	'+	str	(p.value(	x578	)))
filepoint.write	('\tx579	'+	str	(p.value(	x579	)))
filepoint.write	('\tx580	'+	str	(p.value(	x580	)))
filepoint.write	('\tx581	'+	str	(p.value(	x581	)))
filepoint.write	('\tx582	'+	str	(p.value(	x582	)))
filepoint.write	('\tx583	'+	str	(p.value(	x583	)))
filepoint.write	('\tx584	'+	str	(p.value(	x584	)))
filepoint.write	('\tx585	'+	str	(p.value(	x585	)))
filepoint.write	('\tx586	'+	str	(p.value(	x586	)))
filepoint.write	('\tx587	'+	str	(p.value(	x587	)))
filepoint.write	('\tx588	'+	str	(p.value(	x588	)))
filepoint.write	('\tx589	'+	str	(p.value(	x589	)))
filepoint.write	('\tx590	'+	str	(p.value(	x590	)))
filepoint.write	('\tx591	'+	str	(p.value(	x591	)))
filepoint.write	('\tx592	'+	str	(p.value(	x592	)))
filepoint.write	('\tx593	'+	str	(p.value(	x593	)))
filepoint.write	('\tx594	'+	str	(p.value(	x594	)))
filepoint.write	('\tx595	'+	str	(p.value(	x595	)))
filepoint.write	('\tx596	'+	str	(p.value(	x596	)))
filepoint.write	('\tx597	'+	str	(p.value(	x597	)))
filepoint.write	('\tx598	'+	str	(p.value(	x598	)))
filepoint.write	('\tx599	'+	str	(p.value(	x599	)))
filepoint.write	('\tx600	'+	str	(p.value(	x600	)))
filepoint.write	('\tx601	'+	str	(p.value(	x601	)))
filepoint.write	('\tx602	'+	str	(p.value(	x602	)))
filepoint.write	('\tx603	'+	str	(p.value(	x603	)))
filepoint.write	('\tx604	'+	str	(p.value(	x604	)))
filepoint.write	('\tx605	'+	str	(p.value(	x605	)))
filepoint.write	('\tx606	'+	str	(p.value(	x606	)))
filepoint.write	('\tx607	'+	str	(p.value(	x607	)))
filepoint.write	('\tx608	'+	str	(p.value(	x608	)))
filepoint.write	('\tx609	'+	str	(p.value(	x609	)))
filepoint.write	('\tx610	'+	str	(p.value(	x610	)))
filepoint.write	('\tx611	'+	str	(p.value(	x611	)))
filepoint.write	('\tx612	'+	str	(p.value(	x612	)))
filepoint.write	('\tx613	'+	str	(p.value(	x613	)))
filepoint.write	('\tx614	'+	str	(p.value(	x614	)))
filepoint.write	('\tx615	'+	str	(p.value(	x615	)))
filepoint.write	('\tx616	'+	str	(p.value(	x616	)))
filepoint.write	('\tx617	'+	str	(p.value(	x617	)))
filepoint.write	('\tx618	'+	str	(p.value(	x618	)))
filepoint.write	('\tx619	'+	str	(p.value(	x619	)))
filepoint.write	('\tx620	'+	str	(p.value(	x620	)))
filepoint.write	('\tx621	'+	str	(p.value(	x621	)))
filepoint.write	('\tx622	'+	str	(p.value(	x622	)))
filepoint.write	('\tx623	'+	str	(p.value(	x623	)))
filepoint.write	('\tx624	'+	str	(p.value(	x624	)))
filepoint.write	('\tx625	'+	str	(p.value(	x625	)))
filepoint.write	('\tx626	'+	str	(p.value(	x626	)))
filepoint.write	('\tx627	'+	str	(p.value(	x627	)))
filepoint.write	('\tx628	'+	str	(p.value(	x628	)))
filepoint.write	('\tx629	'+	str	(p.value(	x629	)))
filepoint.write	('\tx630	'+	str	(p.value(	x630	)))
filepoint.write	('\tx631	'+	str	(p.value(	x631	)))
filepoint.write	('\tx632	'+	str	(p.value(	x632	)))
filepoint.write	('\tx633	'+	str	(p.value(	x633	)))
filepoint.write	('\tx634	'+	str	(p.value(	x634	)))
filepoint.write	('\tx635	'+	str	(p.value(	x635	)))
filepoint.write	('\tx636	'+	str	(p.value(	x636	)))
filepoint.write	('\tx637	'+	str	(p.value(	x637	)))
filepoint.write	('\tx638	'+	str	(p.value(	x638	)))
filepoint.write	('\tx639	'+	str	(p.value(	x639	)))
filepoint.write	('\tx640	'+	str	(p.value(	x640	)))
filepoint.write	('\tx641	'+	str	(p.value(	x641	)))
filepoint.write	('\tx642	'+	str	(p.value(	x642	)))
filepoint.write	('\tx643	'+	str	(p.value(	x643	)))
filepoint.write	('\tx644	'+	str	(p.value(	x644	)))
filepoint.write	('\tx645	'+	str	(p.value(	x645	)))
filepoint.write	('\tx646	'+	str	(p.value(	x646	)))
filepoint.write	('\tx647	'+	str	(p.value(	x647	)))
filepoint.write	('\tx648	'+	str	(p.value(	x648	)))
filepoint.write	('\tx649	'+	str	(p.value(	x649	)))
filepoint.write	('\tx650	'+	str	(p.value(	x650	)))
filepoint.write	('\tx651	'+	str	(p.value(	x651	)))
filepoint.write	('\tx652	'+	str	(p.value(	x652	)))
filepoint.write	('\tx653	'+	str	(p.value(	x653	)))
filepoint.write	('\tx654	'+	str	(p.value(	x654	)))
filepoint.write	('\tx655	'+	str	(p.value(	x655	)))
filepoint.write	('\tx656	'+	str	(p.value(	x656	)))
filepoint.write	('\tx657	'+	str	(p.value(	x657	)))
filepoint.write	('\tx658	'+	str	(p.value(	x658	)))
filepoint.write	('\tx659	'+	str	(p.value(	x659	)))
filepoint.write	('\tx660	'+	str	(p.value(	x660	)))
filepoint.write	('\tx661	'+	str	(p.value(	x661	)))
filepoint.write	('\tx662	'+	str	(p.value(	x662	)))
filepoint.write	('\tx663	'+	str	(p.value(	x663	)))
filepoint.write	('\tx664	'+	str	(p.value(	x664	)))
filepoint.write	('\tx665	'+	str	(p.value(	x665	)))
filepoint.write	('\tx666	'+	str	(p.value(	x666	)))
filepoint.write	('\tx667	'+	str	(p.value(	x667	)))
filepoint.write	('\tx668	'+	str	(p.value(	x668	)))
filepoint.write	('\tx669	'+	str	(p.value(	x669	)))
filepoint.write	('\tx670	'+	str	(p.value(	x670	)))
filepoint.write	('\tx671	'+	str	(p.value(	x671	)))
filepoint.write	('\tx672	'+	str	(p.value(	x672	)))
filepoint.write	('\tx673	'+	str	(p.value(	x673	)))
filepoint.write	('\tx674	'+	str	(p.value(	x674	)))
filepoint.write	('\tx675	'+	str	(p.value(	x675	)))
filepoint.write	('\tx676	'+	str	(p.value(	x676	)))
filepoint.write	('\tx677	'+	str	(p.value(	x677	)))
filepoint.write	('\tx678	'+	str	(p.value(	x678	)))
filepoint.write	('\tx679	'+	str	(p.value(	x679	)))
filepoint.write	('\tx680	'+	str	(p.value(	x680	)))
filepoint.write	('\tx681	'+	str	(p.value(	x681	)))
filepoint.write	('\tx682	'+	str	(p.value(	x682	)))
filepoint.write	('\tx683	'+	str	(p.value(	x683	)))
filepoint.write	('\tx684	'+	str	(p.value(	x684	)))
filepoint.write	('\tx685	'+	str	(p.value(	x685	)))
filepoint.write	('\tx686	'+	str	(p.value(	x686	)))
filepoint.write	('\tx687	'+	str	(p.value(	x687	)))
filepoint.write	('\tx688	'+	str	(p.value(	x688	)))
filepoint.write	('\tx689	'+	str	(p.value(	x689	)))
filepoint.write	('\tx690	'+	str	(p.value(	x690	)))
filepoint.write	('\tx691	'+	str	(p.value(	x691	)))
filepoint.write	('\tx692	'+	str	(p.value(	x692	)))
filepoint.write	('\tx693	'+	str	(p.value(	x693	)))
filepoint.write	('\tx694	'+	str	(p.value(	x694	)))
filepoint.write	('\tx695	'+	str	(p.value(	x695	)))
filepoint.write	('\tx696	'+	str	(p.value(	x696	)))
filepoint.write	('\tx697	'+	str	(p.value(	x697	)))
filepoint.write	('\tx698	'+	str	(p.value(	x698	)))
filepoint.write	('\tx699	'+	str	(p.value(	x699	)))
filepoint.write	('\tx700	'+	str	(p.value(	x700	)))
filepoint.write	('\tx701	'+	str	(p.value(	x701	)))
filepoint.write	('\tx702	'+	str	(p.value(	x702	)))
filepoint.write	('\tx703	'+	str	(p.value(	x703	)))
filepoint.write	('\tx704	'+	str	(p.value(	x704	)))
filepoint.write	('\tx705	'+	str	(p.value(	x705	)))
filepoint.write	('\tx706	'+	str	(p.value(	x706	)))
filepoint.write	('\tx707	'+	str	(p.value(	x707	)))
filepoint.write	('\tx708	'+	str	(p.value(	x708	)))
filepoint.write	('\tx709	'+	str	(p.value(	x709	)))
filepoint.write	('\tx710	'+	str	(p.value(	x710	)))
filepoint.write	('\tx711	'+	str	(p.value(	x711	)))
filepoint.write	('\tx712	'+	str	(p.value(	x712	)))
filepoint.write	('\tx713	'+	str	(p.value(	x713	)))
filepoint.write	('\tx714	'+	str	(p.value(	x714	)))
filepoint.write	('\tx715	'+	str	(p.value(	x715	)))
filepoint.write	('\tx716	'+	str	(p.value(	x716	)))
filepoint.write	('\tx717	'+	str	(p.value(	x717	)))
filepoint.write	('\tx718	'+	str	(p.value(	x718	)))
filepoint.write	('\tx719	'+	str	(p.value(	x719	)))
filepoint.write	('\tx720	'+	str	(p.value(	x720	)))
filepoint.write	('\tx721	'+	str	(p.value(	x721	)))
filepoint.write	('\tx722	'+	str	(p.value(	x722	)))
filepoint.write	('\tx723	'+	str	(p.value(	x723	)))
filepoint.write	('\tx724	'+	str	(p.value(	x724	)))
filepoint.write	('\tx725	'+	str	(p.value(	x725	)))
filepoint.write	('\tx726	'+	str	(p.value(	x726	)))
filepoint.write	('\tx727	'+	str	(p.value(	x727	)))
filepoint.write	('\tx728	'+	str	(p.value(	x728	)))
filepoint.write	('\tx729	'+	str	(p.value(	x729	)))
filepoint.write	('\tx730	'+	str	(p.value(	x730	)))
filepoint.write	('\tx731	'+	str	(p.value(	x731	)))
filepoint.write	('\tx732	'+	str	(p.value(	x732	)))
filepoint.write	('\tx733	'+	str	(p.value(	x733	)))
filepoint.write	('\tx734	'+	str	(p.value(	x734	)))
filepoint.write	('\tx735	'+	str	(p.value(	x735	)))
filepoint.write	('\tx736	'+	str	(p.value(	x736	)))
filepoint.write	('\tx737	'+	str	(p.value(	x737	)))
filepoint.write	('\tx738	'+	str	(p.value(	x738	)))
filepoint.write	('\tx739	'+	str	(p.value(	x739	)))
filepoint.write	('\tx740	'+	str	(p.value(	x740	)))
filepoint.write	('\tx741	'+	str	(p.value(	x741	)))
filepoint.write	('\tx742	'+	str	(p.value(	x742	)))
filepoint.write	('\tx743	'+	str	(p.value(	x743	)))
filepoint.write	('\tx744	'+	str	(p.value(	x744	)))
filepoint.write	('\tx745	'+	str	(p.value(	x745	)))
filepoint.write	('\tx746	'+	str	(p.value(	x746	)))
filepoint.write	('\tx747	'+	str	(p.value(	x747	)))
filepoint.write	('\tx748	'+	str	(p.value(	x748	)))
filepoint.write	('\tx749	'+	str	(p.value(	x749	)))
filepoint.write	('\tx750	'+	str	(p.value(	x750	)))
filepoint.write	('\tx751	'+	str	(p.value(	x751	)))
filepoint.write	('\tx752	'+	str	(p.value(	x752	)))
filepoint.write	('\tx753	'+	str	(p.value(	x753	)))
filepoint.write	('\tx754	'+	str	(p.value(	x754	)))
filepoint.write	('\tx755	'+	str	(p.value(	x755	)))
filepoint.write	('\tx756	'+	str	(p.value(	x756	)))
filepoint.write	('\tx757	'+	str	(p.value(	x757	)))
filepoint.write	('\tx758	'+	str	(p.value(	x758	)))
filepoint.write	('\tx759	'+	str	(p.value(	x759	)))
filepoint.write	('\tx760	'+	str	(p.value(	x760	)))
filepoint.write	('\tx761	'+	str	(p.value(	x761	)))
filepoint.write	('\tx762	'+	str	(p.value(	x762	)))
filepoint.write	('\tx763	'+	str	(p.value(	x763	)))
filepoint.write	('\tx764	'+	str	(p.value(	x764	)))
filepoint.write	('\tx765	'+	str	(p.value(	x765	)))
filepoint.write	('\tx766	'+	str	(p.value(	x766	)))
filepoint.write	('\tx767	'+	str	(p.value(	x767	)))
filepoint.write	('\tx768	'+	str	(p.value(	x768	)))
filepoint.write	('\tx769	'+	str	(p.value(	x769	)))
filepoint.write	('\tx770	'+	str	(p.value(	x770	)))
filepoint.write	('\tx771	'+	str	(p.value(	x771	)))
filepoint.write	('\tx772	'+	str	(p.value(	x772	)))
filepoint.write	('\tx773	'+	str	(p.value(	x773	)))
filepoint.write	('\tx774	'+	str	(p.value(	x774	)))
filepoint.write	('\tx775	'+	str	(p.value(	x775	)))
filepoint.write	('\tx776	'+	str	(p.value(	x776	)))
filepoint.write	('\tx777	'+	str	(p.value(	x777	)))
filepoint.write	('\tx778	'+	str	(p.value(	x778	)))
filepoint.write	('\tx779	'+	str	(p.value(	x779	)))
filepoint.write	('\tx780	'+	str	(p.value(	x780	)))
filepoint.write	('\tx781	'+	str	(p.value(	x781	)))
filepoint.write	('\tx782	'+	str	(p.value(	x782	)))
filepoint.write	('\tx783	'+	str	(p.value(	x783	)))
filepoint.write	('\tx784	'+	str	(p.value(	x784	)))
filepoint.write	('\tx785	'+	str	(p.value(	x785	)))
filepoint.write	('\tx786	'+	str	(p.value(	x786	)))
filepoint.write	('\tx787	'+	str	(p.value(	x787	)))
filepoint.write	('\tx788	'+	str	(p.value(	x788	)))
filepoint.write	('\tx789	'+	str	(p.value(	x789	)))
filepoint.write	('\tx790	'+	str	(p.value(	x790	)))
filepoint.write	('\tx791	'+	str	(p.value(	x791	)))
filepoint.write	('\tx792	'+	str	(p.value(	x792	)))
filepoint.write	('\tx793	'+	str	(p.value(	x793	)))
filepoint.write	('\tx794	'+	str	(p.value(	x794	)))
filepoint.write	('\tx795	'+	str	(p.value(	x795	)))
filepoint.write	('\tx796	'+	str	(p.value(	x796	)))
filepoint.write	('\tx797	'+	str	(p.value(	x797	)))
filepoint.write	('\tx798	'+	str	(p.value(	x798	)))
filepoint.write	('\tx799	'+	str	(p.value(	x799	)))
filepoint.write	('\tx800	'+	str	(p.value(	x800	)))
filepoint.write	('\tx801	'+	str	(p.value(	x801	)))
filepoint.write	('\tx802	'+	str	(p.value(	x802	)))
filepoint.write	('\tx803	'+	str	(p.value(	x803	)))
filepoint.write	('\tx804	'+	str	(p.value(	x804	)))
filepoint.write	('\tx805	'+	str	(p.value(	x805	)))
filepoint.write	('\tx806	'+	str	(p.value(	x806	)))
filepoint.write	('\tx807	'+	str	(p.value(	x807	)))
filepoint.write	('\tx808	'+	str	(p.value(	x808	)))
filepoint.write	('\tx809	'+	str	(p.value(	x809	)))
filepoint.write	('\tx810	'+	str	(p.value(	x810	)))
filepoint.write	('\tx811	'+	str	(p.value(	x811	)))
filepoint.write	('\tx812	'+	str	(p.value(	x812	)))
filepoint.write	('\tx813	'+	str	(p.value(	x813	)))
filepoint.write	('\tx814	'+	str	(p.value(	x814	)))
filepoint.write	('\tx815	'+	str	(p.value(	x815	)))
filepoint.write	('\tx816	'+	str	(p.value(	x816	)))
filepoint.write	('\tx817	'+	str	(p.value(	x817	)))
filepoint.write	('\tx818	'+	str	(p.value(	x818	)))
filepoint.write	('\tx819	'+	str	(p.value(	x819	)))
filepoint.write	('\tx820	'+	str	(p.value(	x820	)))
filepoint.write	('\tx821	'+	str	(p.value(	x821	)))
filepoint.write	('\tx822	'+	str	(p.value(	x822	)))
filepoint.write	('\tx823	'+	str	(p.value(	x823	)))
filepoint.write	('\tx824	'+	str	(p.value(	x824	)))
filepoint.write	('\tx825	'+	str	(p.value(	x825	)))
filepoint.write	('\tx826	'+	str	(p.value(	x826	)))
filepoint.write	('\tx827	'+	str	(p.value(	x827	)))
filepoint.write	('\tx828	'+	str	(p.value(	x828	)))
filepoint.write	('\tx829	'+	str	(p.value(	x829	)))
filepoint.write	('\tx830	'+	str	(p.value(	x830	)))
filepoint.write	('\tx831	'+	str	(p.value(	x831	)))
filepoint.write	('\tx832	'+	str	(p.value(	x832	)))
filepoint.write	('\tx833	'+	str	(p.value(	x833	)))
filepoint.write	('\tx834	'+	str	(p.value(	x834	)))
filepoint.write	('\tx835	'+	str	(p.value(	x835	)))
filepoint.write	('\tx836	'+	str	(p.value(	x836	)))
filepoint.write	('\tx837	'+	str	(p.value(	x837	)))
filepoint.write	('\tx838	'+	str	(p.value(	x838	)))
filepoint.write	('\tx839	'+	str	(p.value(	x839	)))
filepoint.write	('\tx840	'+	str	(p.value(	x840	)))
filepoint.write	('\tx841	'+	str	(p.value(	x841	)))
filepoint.write	('\tx842	'+	str	(p.value(	x842	)))
filepoint.write	('\tx843	'+	str	(p.value(	x843	)))
filepoint.write	('\tx844	'+	str	(p.value(	x844	)))
filepoint.write	('\tx845	'+	str	(p.value(	x845	)))
filepoint.write	('\tx846	'+	str	(p.value(	x846	)))
filepoint.write	('\tx847	'+	str	(p.value(	x847	)))
filepoint.write	('\tx848	'+	str	(p.value(	x848	)))
filepoint.write	('\tx849	'+	str	(p.value(	x849	)))
filepoint.write	('\tx850	'+	str	(p.value(	x850	)))
filepoint.write	('\tx851	'+	str	(p.value(	x851	)))
filepoint.write	('\tx852	'+	str	(p.value(	x852	)))
filepoint.write	('\tx853	'+	str	(p.value(	x853	)))
filepoint.write	('\tx854	'+	str	(p.value(	x854	)))
filepoint.write	('\tx855	'+	str	(p.value(	x855	)))
filepoint.write	('\tx856	'+	str	(p.value(	x856	)))
filepoint.write	('\tx857	'+	str	(p.value(	x857	)))
filepoint.write	('\tx858	'+	str	(p.value(	x858	)))
filepoint.write	('\tx859	'+	str	(p.value(	x859	)))
filepoint.write	('\tx860	'+	str	(p.value(	x860	)))
filepoint.write	('\tx861	'+	str	(p.value(	x861	)))
filepoint.write	('\tx862	'+	str	(p.value(	x862	)))
filepoint.write	('\tx863	'+	str	(p.value(	x863	)))
filepoint.write	('\tx864	'+	str	(p.value(	x864	)))
filepoint.write	('\tx865	'+	str	(p.value(	x865	)))
filepoint.write	('\tx866	'+	str	(p.value(	x866	)))
filepoint.write	('\tx867	'+	str	(p.value(	x867	)))
filepoint.write	('\tx868	'+	str	(p.value(	x868	)))
filepoint.write	('\tx869	'+	str	(p.value(	x869	)))
filepoint.write	('\tx870	'+	str	(p.value(	x870	)))
filepoint.write	('\tx871	'+	str	(p.value(	x871	)))
filepoint.write	('\tx872	'+	str	(p.value(	x872	)))
filepoint.write	('\tx873	'+	str	(p.value(	x873	)))
filepoint.write	('\tx874	'+	str	(p.value(	x874	)))
filepoint.write	('\tx875	'+	str	(p.value(	x875	)))
filepoint.write	('\tx876	'+	str	(p.value(	x876	)))
filepoint.write	('\tx877	'+	str	(p.value(	x877	)))
filepoint.write	('\tx878	'+	str	(p.value(	x878	)))
filepoint.write	('\tx879	'+	str	(p.value(	x879	)))
filepoint.write	('\tx880	'+	str	(p.value(	x880	)))
filepoint.write	('\tx881	'+	str	(p.value(	x881	)))
filepoint.write	('\tx882	'+	str	(p.value(	x882	)))
filepoint.write	('\tx883	'+	str	(p.value(	x883	)))
filepoint.write	('\tx884	'+	str	(p.value(	x884	)))
filepoint.write	('\tx885	'+	str	(p.value(	x885	)))
filepoint.write	('\tx886	'+	str	(p.value(	x886	)))
filepoint.write	('\tx887	'+	str	(p.value(	x887	)))
filepoint.write	('\tx888	'+	str	(p.value(	x888	)))
filepoint.write	('\tx889	'+	str	(p.value(	x889	)))
filepoint.write	('\tx890	'+	str	(p.value(	x890	)))
filepoint.write	('\tx891	'+	str	(p.value(	x891	)))
filepoint.write	('\tx892	'+	str	(p.value(	x892	)))
filepoint.write	('\tx893	'+	str	(p.value(	x893	)))
filepoint.write	('\tx894	'+	str	(p.value(	x894	)))
filepoint.write	('\tx895	'+	str	(p.value(	x895	)))
filepoint.write	('\tx896	'+	str	(p.value(	x896	)))
filepoint.write	('\tx897	'+	str	(p.value(	x897	)))
filepoint.write	('\tx898	'+	str	(p.value(	x898	)))
filepoint.write	('\tx899	'+	str	(p.value(	x899	)))
filepoint.write	('\tx900	'+	str	(p.value(	x900	)))
filepoint.write	('\tx901	'+	str	(p.value(	x901	)))
filepoint.write	('\tx902	'+	str	(p.value(	x902	)))
filepoint.write	('\tx903	'+	str	(p.value(	x903	)))
filepoint.write	('\tx904	'+	str	(p.value(	x904	)))
filepoint.write	('\tx905	'+	str	(p.value(	x905	)))
filepoint.write	('\tx906	'+	str	(p.value(	x906	)))
filepoint.write	('\tx907	'+	str	(p.value(	x907	)))
filepoint.write	('\tx908	'+	str	(p.value(	x908	)))
filepoint.write	('\tx909	'+	str	(p.value(	x909	)))
filepoint.write	('\tx910	'+	str	(p.value(	x910	)))
filepoint.write	('\tx911	'+	str	(p.value(	x911	)))
filepoint.write	('\tx912	'+	str	(p.value(	x912	)))
filepoint.write	('\tx913	'+	str	(p.value(	x913	)))
filepoint.write	('\tx914	'+	str	(p.value(	x914	)))
filepoint.write	('\tx915	'+	str	(p.value(	x915	)))
filepoint.write	('\tx916	'+	str	(p.value(	x916	)))
filepoint.write	('\tx917	'+	str	(p.value(	x917	)))
filepoint.write	('\tx918	'+	str	(p.value(	x918	)))
filepoint.write	('\tx919	'+	str	(p.value(	x919	)))
filepoint.write	('\tx920	'+	str	(p.value(	x920	)))
filepoint.write	('\tx921	'+	str	(p.value(	x921	)))
filepoint.write	('\tx922	'+	str	(p.value(	x922	)))
filepoint.write	('\tx923	'+	str	(p.value(	x923	)))
filepoint.write	('\tx924	'+	str	(p.value(	x924	)))
filepoint.write	('\tx925	'+	str	(p.value(	x925	)))
filepoint.write	('\tx926	'+	str	(p.value(	x926	)))
filepoint.write	('\tx927	'+	str	(p.value(	x927	)))
filepoint.write	('\tx928	'+	str	(p.value(	x928	)))
filepoint.write	('\tx929	'+	str	(p.value(	x929	)))
filepoint.write	('\tx930	'+	str	(p.value(	x930	)))
filepoint.write	('\tx931	'+	str	(p.value(	x931	)))
filepoint.write	('\tx932	'+	str	(p.value(	x932	)))
filepoint.write	('\tx933	'+	str	(p.value(	x933	)))
filepoint.write	('\tx934	'+	str	(p.value(	x934	)))
filepoint.write	('\tx935	'+	str	(p.value(	x935	)))
filepoint.write	('\tx936	'+	str	(p.value(	x936	)))
filepoint.write	('\tx937	'+	str	(p.value(	x937	)))
filepoint.write	('\tx938	'+	str	(p.value(	x938	)))
filepoint.write	('\tx939	'+	str	(p.value(	x939	)))
filepoint.write	('\tx940	'+	str	(p.value(	x940	)))
filepoint.write	('\tx941	'+	str	(p.value(	x941	)))
filepoint.write	('\tx942	'+	str	(p.value(	x942	)))
filepoint.write	('\tx943	'+	str	(p.value(	x943	)))
filepoint.write	('\tx944	'+	str	(p.value(	x944	)))
filepoint.write	('\tx945	'+	str	(p.value(	x945	)))
filepoint.write	('\tx946	'+	str	(p.value(	x946	)))
filepoint.write	('\tx947	'+	str	(p.value(	x947	)))
filepoint.write	('\tx948	'+	str	(p.value(	x948	)))
filepoint.write	('\tx949	'+	str	(p.value(	x949	)))
filepoint.write	('\tx950	'+	str	(p.value(	x950	)))
filepoint.write	('\tx951	'+	str	(p.value(	x951	)))
filepoint.write	('\tx952	'+	str	(p.value(	x952	)))
filepoint.write	('\tx953	'+	str	(p.value(	x953	)))
filepoint.write	('\tx954	'+	str	(p.value(	x954	)))
filepoint.write	('\tx955	'+	str	(p.value(	x955	)))
filepoint.write	('\tx956	'+	str	(p.value(	x956	)))
filepoint.write	('\tx957	'+	str	(p.value(	x957	)))
filepoint.write	('\tx958	'+	str	(p.value(	x958	)))
filepoint.write	('\tx959	'+	str	(p.value(	x959	)))
filepoint.write	('\tx960	'+	str	(p.value(	x960	)))
filepoint.write	('\tx961	'+	str	(p.value(	x961	)))
filepoint.write	('\tx962	'+	str	(p.value(	x962	)))
filepoint.write	('\tx963	'+	str	(p.value(	x963	)))
filepoint.write	('\tx964	'+	str	(p.value(	x964	)))
filepoint.write	('\tx965	'+	str	(p.value(	x965	)))
filepoint.write	('\tx966	'+	str	(p.value(	x966	)))
filepoint.write	('\tx967	'+	str	(p.value(	x967	)))
filepoint.write	('\tx968	'+	str	(p.value(	x968	)))
filepoint.write	('\tx969	'+	str	(p.value(	x969	)))
filepoint.write	('\tx970	'+	str	(p.value(	x970	)))
filepoint.write	('\tx971	'+	str	(p.value(	x971	)))
filepoint.write	('\tx972	'+	str	(p.value(	x972	)))
filepoint.write	('\tx973	'+	str	(p.value(	x973	)))
filepoint.write	('\tx974	'+	str	(p.value(	x974	)))
filepoint.write	('\tx975	'+	str	(p.value(	x975	)))
filepoint.write	('\tx976	'+	str	(p.value(	x976	)))
filepoint.write	('\tx977	'+	str	(p.value(	x977	)))
filepoint.write	('\tx978	'+	str	(p.value(	x978	)))
filepoint.write	('\tx979	'+	str	(p.value(	x979	)))
filepoint.write	('\tx980	'+	str	(p.value(	x980	)))
filepoint.write	('\tx981	'+	str	(p.value(	x981	)))
filepoint.write	('\tx982	'+	str	(p.value(	x982	)))
filepoint.write	('\tx983	'+	str	(p.value(	x983	)))
filepoint.write	('\tx984	'+	str	(p.value(	x984	)))
filepoint.write	('\tx985	'+	str	(p.value(	x985	)))
filepoint.write	('\tx986	'+	str	(p.value(	x986	)))
filepoint.write	('\tx987	'+	str	(p.value(	x987	)))
filepoint.write	('\tx988	'+	str	(p.value(	x988	)))
filepoint.write	('\tx989	'+	str	(p.value(	x989	)))
filepoint.write	('\tx990	'+	str	(p.value(	x990	)))
filepoint.write	('\tx991	'+	str	(p.value(	x991	)))
filepoint.write	('\tx992	'+	str	(p.value(	x992	)))
filepoint.write	('\tx993	'+	str	(p.value(	x993	)))
filepoint.write	('\tx994	'+	str	(p.value(	x994	)))
filepoint.write	('\tx995	'+	str	(p.value(	x995	)))
filepoint.write	('\tx996	'+	str	(p.value(	x996	)))
filepoint.write	('\tx997	'+	str	(p.value(	x997	)))
filepoint.write	('\tx998	'+	str	(p.value(	x998	)))
filepoint.write	('\tx999	'+	str	(p.value(	x999	)))
filepoint.write	('\tx1000	'+	str	(p.value(	x1000	)))
filepoint.write	('\tx1001	'+	str	(p.value(	x1001	)))
filepoint.write	('\tx1002	'+	str	(p.value(	x1002	)))
filepoint.write	('\tx1003	'+	str	(p.value(	x1003	)))
filepoint.write	('\tx1004	'+	str	(p.value(	x1004	)))
filepoint.write	('\tx1005	'+	str	(p.value(	x1005	)))
filepoint.write	('\tx1006	'+	str	(p.value(	x1006	)))
filepoint.write	('\tx1007	'+	str	(p.value(	x1007	)))
filepoint.write	('\tx1008	'+	str	(p.value(	x1008	)))
filepoint.write	('\tx1009	'+	str	(p.value(	x1009	)))
filepoint.write	('\tx1010	'+	str	(p.value(	x1010	)))
filepoint.write	('\tx1011	'+	str	(p.value(	x1011	)))
filepoint.write	('\tx1012	'+	str	(p.value(	x1012	)))
filepoint.write	('\tx1013	'+	str	(p.value(	x1013	)))
filepoint.write	('\tx1014	'+	str	(p.value(	x1014	)))
filepoint.write	('\tx1015	'+	str	(p.value(	x1015	)))
filepoint.write	('\tx1016	'+	str	(p.value(	x1016	)))
filepoint.write	('\tx1017	'+	str	(p.value(	x1017	)))
filepoint.write	('\tx1018	'+	str	(p.value(	x1018	)))
filepoint.write	('\tx1019	'+	str	(p.value(	x1019	)))
filepoint.write	('\tx1020	'+	str	(p.value(	x1020	)))
filepoint.write	('\tx1021	'+	str	(p.value(	x1021	)))
filepoint.write	('\tx1022	'+	str	(p.value(	x1022	)))
filepoint.write	('\tx1023	'+	str	(p.value(	x1023	)))
filepoint.write	('\tx1024	'+	str	(p.value(	x1024	)))
filepoint.write	('\tx1025	'+	str	(p.value(	x1025	)))
filepoint.write	('\tx1026	'+	str	(p.value(	x1026	)))
filepoint.write	('\tx1027	'+	str	(p.value(	x1027	)))
filepoint.write	('\tx1028	'+	str	(p.value(	x1028	)))
filepoint.write	('\tx1029	'+	str	(p.value(	x1029	)))
filepoint.write	('\tx1030	'+	str	(p.value(	x1030	)))
filepoint.write	('\tx1031	'+	str	(p.value(	x1031	)))
filepoint.write	('\tx1032	'+	str	(p.value(	x1032	)))
filepoint.write	('\tx1033	'+	str	(p.value(	x1033	)))
filepoint.write	('\tx1034	'+	str	(p.value(	x1034	)))
filepoint.write	('\tx1035	'+	str	(p.value(	x1035	)))
filepoint.write	('\tx1036	'+	str	(p.value(	x1036	)))
filepoint.write	('\tx1037	'+	str	(p.value(	x1037	)))
filepoint.write	('\tx1038	'+	str	(p.value(	x1038	)))
filepoint.write	('\tx1039	'+	str	(p.value(	x1039	)))
filepoint.write	('\tx1040	'+	str	(p.value(	x1040	)))
filepoint.write	('\tx1041	'+	str	(p.value(	x1041	)))
filepoint.write	('\tx1042	'+	str	(p.value(	x1042	)))
filepoint.write	('\tx1043	'+	str	(p.value(	x1043	)))
filepoint.write	('\tx1044	'+	str	(p.value(	x1044	)))
filepoint.write	('\tx1045	'+	str	(p.value(	x1045	)))
filepoint.write	('\tx1046	'+	str	(p.value(	x1046	)))
filepoint.write	('\tx1047	'+	str	(p.value(	x1047	)))
filepoint.write	('\tx1048	'+	str	(p.value(	x1048	)))
filepoint.write	('\tx1049	'+	str	(p.value(	x1049	)))
filepoint.write	('\tx1050	'+	str	(p.value(	x1050	)))
filepoint.write	('\tx1051	'+	str	(p.value(	x1051	)))
filepoint.write	('\tx1052	'+	str	(p.value(	x1052	)))
filepoint.write	('\tx1053	'+	str	(p.value(	x1053	)))
filepoint.write	('\tx1054	'+	str	(p.value(	x1054	)))
filepoint.write	('\tx1055	'+	str	(p.value(	x1055	)))
filepoint.write	('\tx1056	'+	str	(p.value(	x1056	)))
filepoint.write	('\tx1057	'+	str	(p.value(	x1057	)))
filepoint.write	('\tx1058	'+	str	(p.value(	x1058	)))
filepoint.write	('\tx1059	'+	str	(p.value(	x1059	)))
filepoint.write	('\tx1060	'+	str	(p.value(	x1060	)))
filepoint.write	('\tx1061	'+	str	(p.value(	x1061	)))
filepoint.write	('\tx1062	'+	str	(p.value(	x1062	)))
filepoint.write	('\tx1063	'+	str	(p.value(	x1063	)))
filepoint.write	('\tx1064	'+	str	(p.value(	x1064	)))
filepoint.write	('\tx1065	'+	str	(p.value(	x1065	)))
filepoint.write	('\tx1066	'+	str	(p.value(	x1066	)))
filepoint.write	('\tx1067	'+	str	(p.value(	x1067	)))
filepoint.write	('\tx1068	'+	str	(p.value(	x1068	)))
filepoint.write	('\tx1069	'+	str	(p.value(	x1069	)))
filepoint.write	('\tx1070	'+	str	(p.value(	x1070	)))
filepoint.write	('\tx1071	'+	str	(p.value(	x1071	)))
filepoint.write	('\tx1072	'+	str	(p.value(	x1072	)))
filepoint.write	('\tx1073	'+	str	(p.value(	x1073	)))
filepoint.write	('\tx1074	'+	str	(p.value(	x1074	)))
filepoint.write	('\tx1075	'+	str	(p.value(	x1075	)))
filepoint.write	('\tx1076	'+	str	(p.value(	x1076	)))
filepoint.write	('\tx1077	'+	str	(p.value(	x1077	)))
filepoint.writelines	('\tx1078	'+	str	(p.value(	x1078	)))
filepoint.writelines	('\tx1079	'+	str	(p.value(	x1079	)))
filepoint.writelines	('\tx1080	'+	str	(p.value(	x1080	)))
filepoint.writelines	('\tx1081	'+	str	(p.value(	x1081	)))
filepoint.writelines	('\tx1082	'+	str	(p.value(	x1082	)))
filepoint.writelines	('\tx1083	'+	str	(p.value(	x1083	)))
filepoint.writelines	('\tx1084	'+	str	(p.value(	x1084	)))
filepoint.writelines	('\tx1085	'+	str	(p.value(	x1085	)))
filepoint.writelines	('\tx1086	'+	str	(p.value(	x1086	)))
filepoint.writelines	('\tx1087	'+	str	(p.value(	x1087	)))
filepoint.writelines	('\tx1088	'+	str	(p.value(	x1088	)))
filepoint.writelines	('\tx1089	'+	str	(p.value(	x1089	)))
filepoint.writelines	('\tx1090	'+	str	(p.value(	x1090	)))
filepoint.writelines	('\tx1091	'+	str	(p.value(	x1091	)))
filepoint.writelines	('\tx1092	'+	str	(p.value(	x1092	)))
filepoint.writelines	('\tx1093	'+	str	(p.value(	x1093	)))
filepoint.writelines	('\tx1094	'+	str	(p.value(	x1094	)))
filepoint.writelines	('\tx1095	'+	str	(p.value(	x1095	)))
filepoint.writelines	('\tx1096	'+	str	(p.value(	x1096	)))
filepoint.writelines	('\tx1097	'+	str	(p.value(	x1097	)))
filepoint.writelines	('\tx1098	'+	str	(p.value(	x1098	)))
filepoint.writelines	('\tx1099	'+	str	(p.value(	x1099	)))
filepoint.writelines	('\tx1100	'+	str	(p.value(	x1100	)))
filepoint.writelines	('\tx1101	'+	str	(p.value(	x1101	)))
filepoint.writelines	('\tx1102	'+	str	(p.value(	x1102	)))
filepoint.writelines	('\tx1103	'+	str	(p.value(	x1103	)))
filepoint.writelines	('\tx1104	'+	str	(p.value(	x1104	)))
filepoint.writelines	('\tx1105	'+	str	(p.value(	x1105	)))
filepoint.writelines	('\tx1106	'+	str	(p.value(	x1106	)))
filepoint.writelines	('\tx1107	'+	str	(p.value(	x1107	)))
filepoint.writelines	('\tx1108	'+	str	(p.value(	x1108	)))
filepoint.writelines	('\tx1109	'+	str	(p.value(	x1109	)))
filepoint.writelines	('\tx1110	'+	str	(p.value(	x1110	)))
filepoint.writelines	('\tx1111	'+	str	(p.value(	x1111	)))
filepoint.writelines	('\tx1112	'+	str	(p.value(	x1112	)))
filepoint.writelines	('\tx1113	'+	str	(p.value(	x1113	)))
filepoint.writelines	('\tx1114	'+	str	(p.value(	x1114	)))
filepoint.writelines	('\tx1115	'+	str	(p.value(	x1115	)))
filepoint.writelines	('\tx1116	'+	str	(p.value(	x1116	)))
filepoint.writelines	('\tx1117	'+	str	(p.value(	x1117	)))
filepoint.writelines	('\tx1118	'+	str	(p.value(	x1118	)))
filepoint.writelines	('\tx1119	'+	str	(p.value(	x1119	)))
filepoint.writelines	('\tx1120	'+	str	(p.value(	x1120	)))
filepoint.writelines	('\tx1121	'+	str	(p.value(	x1121	)))
filepoint.writelines	('\tx1122	'+	str	(p.value(	x1122	)))
filepoint.writelines	('\tx1123	'+	str	(p.value(	x1123	)))
filepoint.writelines	('\tx1124	'+	str	(p.value(	x1124	)))
filepoint.writelines	('\tx1125	'+	str	(p.value(	x1125	)))
filepoint.writelines	('\tx1126	'+	str	(p.value(	x1126	)))
filepoint.writelines	('\tx1127	'+	str	(p.value(	x1127	)))
filepoint.writelines	('\tx1128	'+	str	(p.value(	x1128	)))
filepoint.writelines	('\tx1129	'+	str	(p.value(	x1129	)))
filepoint.writelines	('\tx1130	'+	str	(p.value(	x1130	)))
filepoint.writelines	('\tx1131	'+	str	(p.value(	x1131	)))
filepoint.writelines	('\tx1132	'+	str	(p.value(	x1132	)))
filepoint.writelines	('\tx1133	'+	str	(p.value(	x1133	)))
filepoint.writelines	('\tx1134	'+	str	(p.value(	x1134	)))
filepoint.writelines	('\tx1135	'+	str	(p.value(	x1135	)))
filepoint.writelines	('\tx1136	'+	str	(p.value(	x1136	)))
filepoint.writelines	('\tx1137	'+	str	(p.value(	x1137	)))
filepoint.writelines	('\tx1138	'+	str	(p.value(	x1138	)))
filepoint.writelines	('\tx1139	'+	str	(p.value(	x1139	)))
filepoint.writelines	('\tx1140	'+	str	(p.value(	x1140	)))
filepoint.writelines	('\tx1141	'+	str	(p.value(	x1141	)))
filepoint.writelines	('\tx1142	'+	str	(p.value(	x1142	)))
filepoint.writelines	('\tx1143	'+	str	(p.value(	x1143	)))
filepoint.writelines	('\tx1144	'+	str	(p.value(	x1144	)))
filepoint.writelines	('\tx1145	'+	str	(p.value(	x1145	)))
filepoint.writelines	('\tx1146	'+	str	(p.value(	x1146	)))
filepoint.writelines	('\tx1147	'+	str	(p.value(	x1147	)))
filepoint.writelines	('\tx1148	'+	str	(p.value(	x1148	)))
filepoint.writelines	('\tx1149	'+	str	(p.value(	x1149	)))
filepoint.writelines	('\tx1150	'+	str	(p.value(	x1150	)))
filepoint.writelines	('\tx1151	'+	str	(p.value(	x1151	)))
filepoint.writelines	('\tx1152	'+	str	(p.value(	x1152	)))
filepoint.writelines	('\tx1153	'+	str	(p.value(	x1153	)))
filepoint.writelines	('\tx1154	'+	str	(p.value(	x1154	)))
filepoint.writelines	('\tx1155	'+	str	(p.value(	x1155	)))
filepoint.writelines	('\tx1156	'+	str	(p.value(	x1156	)))
filepoint.writelines	('\tx1157	'+	str	(p.value(	x1157	)))
filepoint.writelines	('\tx1158	'+	str	(p.value(	x1158	)))
filepoint.writelines	('\tx1159	'+	str	(p.value(	x1159	)))
filepoint.writelines	('\tx1160	'+	str	(p.value(	x1160	)))
filepoint.writelines	('\tx1161	'+	str	(p.value(	x1161	)))
filepoint.writelines	('\tx1162	'+	str	(p.value(	x1162	)))
filepoint.writelines	('\tx1163	'+	str	(p.value(	x1163	)))
filepoint.writelines	('\tx1164	'+	str	(p.value(	x1164	)))
filepoint.writelines	('\tx1165	'+	str	(p.value(	x1165	)))
filepoint.writelines	('\tx1166	'+	str	(p.value(	x1166	)))
filepoint.writelines	('\tx1167	'+	str	(p.value(	x1167	)))
filepoint.writelines	('\tx1168	'+	str	(p.value(	x1168	)))
filepoint.writelines	('\tx1169	'+	str	(p.value(	x1169	)))
filepoint.writelines	('\tx1170	'+	str	(p.value(	x1170	)))
filepoint.writelines	('\tx1171	'+	str	(p.value(	x1171	)))
filepoint.writelines	('\tx1172	'+	str	(p.value(	x1172	)))
filepoint.writelines	('\tx1173	'+	str	(p.value(	x1173	)))
filepoint.writelines	('\tx1174	'+	str	(p.value(	x1174	)))
filepoint.writelines	('\tx1175	'+	str	(p.value(	x1175	)))
filepoint.writelines	('\tx1176	'+	str	(p.value(	x1176	)))
filepoint.writelines	('\tx1177	'+	str	(p.value(	x1177	)))
filepoint.writelines	('\tx1178	'+	str	(p.value(	x1178	)))
filepoint.writelines	('\tx1179	'+	str	(p.value(	x1179	)))
filepoint.writelines	('\tx1180	'+	str	(p.value(	x1180	)))
filepoint.writelines	('\tx1181	'+	str	(p.value(	x1181	)))
filepoint.writelines	('\tx1182	'+	str	(p.value(	x1182	)))
filepoint.writelines	('\tx1183	'+	str	(p.value(	x1183	)))
filepoint.writelines	('\tx1184	'+	str	(p.value(	x1184	)))
filepoint.writelines	('\tx1185	'+	str	(p.value(	x1185	)))
filepoint.writelines	('\tx1186	'+	str	(p.value(	x1186	)))
filepoint.writelines	('\tx1187	'+	str	(p.value(	x1187	)))
filepoint.writelines	('\tx1188	'+	str	(p.value(	x1188	)))
filepoint.writelines	('\tx1189	'+	str	(p.value(	x1189	)))
filepoint.writelines	('\tx1190	'+	str	(p.value(	x1190	)))
filepoint.writelines	('\tx1191	'+	str	(p.value(	x1191	)))
filepoint.writelines	('\tx1192	'+	str	(p.value(	x1192	)))
filepoint.writelines	('\tx1193	'+	str	(p.value(	x1193	)))
filepoint.writelines	('\tx1194	'+	str	(p.value(	x1194	)))
filepoint.writelines	('\tx1195	'+	str	(p.value(	x1195	)))
filepoint.writelines	('\tx1196	'+	str	(p.value(	x1196	)))
filepoint.writelines	('\tx1197	'+	str	(p.value(	x1197	)))
filepoint.writelines	('\tx1198	'+	str	(p.value(	x1198	)))
filepoint.writelines	('\tx1199	'+	str	(p.value(	x1199	)))
filepoint.writelines	('\tx1200	'+	str	(p.value(	x1200	)))
filepoint.writelines	('\tx1201	'+	str	(p.value(	x1201	)))
filepoint.writelines	('\tx1202	'+	str	(p.value(	x1202	)))
filepoint.writelines	('\tx1203	'+	str	(p.value(	x1203	)))
filepoint.writelines	('\tx1204	'+	str	(p.value(	x1204	)))
filepoint.writelines	('\tx1205	'+	str	(p.value(	x1205	)))
filepoint.writelines	('\tx1206	'+	str	(p.value(	x1206	)))
filepoint.writelines	('\tx1207	'+	str	(p.value(	x1207	)))
filepoint.writelines	('\tx1208	'+	str	(p.value(	x1208	)))
filepoint.writelines	('\tx1209	'+	str	(p.value(	x1209	)))
filepoint.writelines	('\tx1210	'+	str	(p.value(	x1210	)))
filepoint.writelines	('\tx1211	'+	str	(p.value(	x1211	)))
filepoint.writelines	('\tx1212	'+	str	(p.value(	x1212	)))
filepoint.writelines	('\tx1213	'+	str	(p.value(	x1213	)))
filepoint.writelines	('\tx1214	'+	str	(p.value(	x1214	)))
filepoint.writelines	('\tx1215	'+	str	(p.value(	x1215	)))
filepoint.writelines	('\tx1216	'+	str	(p.value(	x1216	)))
filepoint.writelines	('\tx1217	'+	str	(p.value(	x1217	)))
filepoint.writelines	('\tx1218	'+	str	(p.value(	x1218	)))
filepoint.writelines	('\tx1219	'+	str	(p.value(	x1219	)))
filepoint.writelines	('\tx1220	'+	str	(p.value(	x1220	)))
filepoint.writelines	('\tx1221	'+	str	(p.value(	x1221	)))
filepoint.writelines	('\tx1222	'+	str	(p.value(	x1222	)))
filepoint.writelines	('\tx1223	'+	str	(p.value(	x1223	)))
filepoint.writelines	('\tx1224	'+	str	(p.value(	x1224	)))
filepoint.writelines	('\tx1225	'+	str	(p.value(	x1225	)))
filepoint.writelines	('\tx1226	'+	str	(p.value(	x1226	)))
filepoint.writelines	('\tx1227	'+	str	(p.value(	x1227	)))
filepoint.writelines	('\tx1228	'+	str	(p.value(	x1228	)))
filepoint.writelines	('\tx1229	'+	str	(p.value(	x1229	)))
filepoint.writelines	('\tx1230	'+	str	(p.value(	x1230	)))
filepoint.writelines	('\tx1231	'+	str	(p.value(	x1231	)))
filepoint.writelines	('\tx1232	'+	str	(p.value(	x1232	)))
filepoint.writelines	('\tx1233	'+	str	(p.value(	x1233	)))
filepoint.writelines	('\tx1234	'+	str	(p.value(	x1234	)))
filepoint.writelines	('\tx1235	'+	str	(p.value(	x1235	)))
filepoint.writelines	('\tx1236	'+	str	(p.value(	x1236	)))
filepoint.writelines	('\tx1237	'+	str	(p.value(	x1237	)))
filepoint.writelines	('\tx1238	'+	str	(p.value(	x1238	)))
filepoint.writelines	('\tx1239	'+	str	(p.value(	x1239	)))
filepoint.writelines	('\tx1240	'+	str	(p.value(	x1240	)))
filepoint.writelines	('\tx1241	'+	str	(p.value(	x1241	)))
filepoint.writelines	('\tx1242	'+	str	(p.value(	x1242	)))
filepoint.writelines	('\tx1243	'+	str	(p.value(	x1243	)))
filepoint.writelines	('\tx1244	'+	str	(p.value(	x1244	)))
filepoint.writelines	('\tx1245	'+	str	(p.value(	x1245	)))
filepoint.writelines	('\tx1246	'+	str	(p.value(	x1246	)))
filepoint.writelines	('\tx1247	'+	str	(p.value(	x1247	)))
filepoint.writelines	('\tx1248	'+	str	(p.value(	x1248	)))
filepoint.writelines	('\tx1249	'+	str	(p.value(	x1249	)))
filepoint.writelines	('\tx1250	'+	str	(p.value(	x1250	)))
filepoint.writelines	('\tx1251	'+	str	(p.value(	x1251	)))
filepoint.writelines	('\tx1252	'+	str	(p.value(	x1252	)))
filepoint.writelines	('\tx1253	'+	str	(p.value(	x1253	)))
filepoint.writelines	('\tx1254	'+	str	(p.value(	x1254	)))
filepoint.writelines	('\tx1255	'+	str	(p.value(	x1255	)))
filepoint.writelines	('\tx1256	'+	str	(p.value(	x1256	)))
filepoint.writelines	('\tx1257	'+	str	(p.value(	x1257	)))
filepoint.writelines	('\tx1258	'+	str	(p.value(	x1258	)))
filepoint.writelines	('\tx1259	'+	str	(p.value(	x1259	)))
filepoint.writelines	('\tx1260	'+	str	(p.value(	x1260	)))
filepoint.writelines	('\tx1261	'+	str	(p.value(	x1261	)))
filepoint.writelines	('\tx1262	'+	str	(p.value(	x1262	)))
filepoint.writelines	('\tx1263	'+	str	(p.value(	x1263	)))
filepoint.writelines	('\tx1264	'+	str	(p.value(	x1264	)))
filepoint.writelines	('\tx1265	'+	str	(p.value(	x1265	)))
filepoint.writelines	('\tx1266	'+	str	(p.value(	x1266	)))
filepoint.writelines	('\tx1267	'+	str	(p.value(	x1267	)))
filepoint.writelines	('\tx1268	'+	str	(p.value(	x1268	)))
filepoint.writelines	('\tx1269	'+	str	(p.value(	x1269	)))
filepoint.writelines	('\tx1270	'+	str	(p.value(	x1270	)))
filepoint.writelines	('\tx1271	'+	str	(p.value(	x1271	)))
filepoint.writelines	('\tx1272	'+	str	(p.value(	x1272	)))
filepoint.writelines	('\tx1273	'+	str	(p.value(	x1273	)))
filepoint.writelines	('\tx1274	'+	str	(p.value(	x1274	)))
filepoint.writelines	('\tx1275	'+	str	(p.value(	x1275	)))
filepoint.writelines	('\tx1276	'+	str	(p.value(	x1276	)))
filepoint.writelines	('\tx1277	'+	str	(p.value(	x1277	)))
filepoint.writelines	('\tx1278	'+	str	(p.value(	x1278	)))
filepoint.writelines	('\tx1279	'+	str	(p.value(	x1279	)))
filepoint.writelines	('\tx1280	'+	str	(p.value(	x1280	)))
filepoint.writelines	('\tx1281	'+	str	(p.value(	x1281	)))
filepoint.writelines	('\tx1282	'+	str	(p.value(	x1282	)))
filepoint.writelines	('\tx1283	'+	str	(p.value(	x1283	)))
filepoint.writelines	('\tx1284	'+	str	(p.value(	x1284	)))
filepoint.writelines	('\tx1285	'+	str	(p.value(	x1285	)))
filepoint.writelines	('\tx1286	'+	str	(p.value(	x1286	)))
filepoint.writelines	('\tx1287	'+	str	(p.value(	x1287	)))
filepoint.writelines	('\tx1288	'+	str	(p.value(	x1288	)))
filepoint.writelines	('\tx1289	'+	str	(p.value(	x1289	)))
filepoint.writelines	('\tx1290	'+	str	(p.value(	x1290	)))
filepoint.writelines	('\tx1291	'+	str	(p.value(	x1291	)))
filepoint.writelines	('\tx1292	'+	str	(p.value(	x1292	)))
filepoint.writelines	('\tx1293	'+	str	(p.value(	x1293	)))
filepoint.writelines	('\tx1294	'+	str	(p.value(	x1294	)))
filepoint.writelines	('\tx1295	'+	str	(p.value(	x1295	)))
filepoint.writelines	('\tx1296	'+	str	(p.value(	x1296	)))
filepoint.writelines	('\tx1297	'+	str	(p.value(	x1297	)))
filepoint.writelines	('\tx1298	'+	str	(p.value(	x1298	)))
filepoint.writelines	('\tx1299	'+	str	(p.value(	x1299	)))
filepoint.writelines	('\tx1300	'+	str	(p.value(	x1300	)))
filepoint.writelines	('\tx1301	'+	str	(p.value(	x1301	)))
filepoint.writelines	('\tx1302	'+	str	(p.value(	x1302	)))
filepoint.writelines	('\tx1303	'+	str	(p.value(	x1303	)))
filepoint.writelines	('\tx1304	'+	str	(p.value(	x1304	)))
filepoint.writelines	('\tx1305	'+	str	(p.value(	x1305	)))
filepoint.writelines	('\tx1306	'+	str	(p.value(	x1306	)))
filepoint.writelines	('\tx1307	'+	str	(p.value(	x1307	)))
filepoint.writelines	('\tx1308	'+	str	(p.value(	x1308	)))
filepoint.writelines	('\tx1309	'+	str	(p.value(	x1309	)))
filepoint.writelines	('\tx1310	'+	str	(p.value(	x1310	)))
filepoint.writelines	('\tx1311	'+	str	(p.value(	x1311	)))
filepoint.writelines	('\tx1312	'+	str	(p.value(	x1312	)))
filepoint.writelines	('\tx1313	'+	str	(p.value(	x1313	)))
filepoint.writelines	('\tx1314	'+	str	(p.value(	x1314	)))
filepoint.writelines	('\tx1315	'+	str	(p.value(	x1315	)))
filepoint.writelines	('\tx1316	'+	str	(p.value(	x1316	)))
filepoint.writelines	('\tx1317	'+	str	(p.value(	x1317	)))
filepoint.writelines	('\tx1318	'+	str	(p.value(	x1318	)))
filepoint.writelines	('\tx1319	'+	str	(p.value(	x1319	)))
filepoint.writelines	('\tx1320	'+	str	(p.value(	x1320	)))
filepoint.writelines	('\tx1321	'+	str	(p.value(	x1321	)))
filepoint.writelines	('\tx1322	'+	str	(p.value(	x1322	)))
filepoint.writelines	('\tx1323	'+	str	(p.value(	x1323	)))
filepoint.writelines	('\tx1324	'+	str	(p.value(	x1324	)))
filepoint.writelines	('\tx1325	'+	str	(p.value(	x1325	)))
filepoint.writelines	('\tx1326	'+	str	(p.value(	x1326	)))
filepoint.writelines	('\tx1327	'+	str	(p.value(	x1327	)))
filepoint.writelines	('\tx1328	'+	str	(p.value(	x1328	)))
filepoint.writelines	('\tx1329	'+	str	(p.value(	x1329	)))
filepoint.writelines	('\tx1330	'+	str	(p.value(	x1330	)))
filepoint.writelines	('\tx1331	'+	str	(p.value(	x1331	)))
filepoint.writelines	('\tx1332	'+	str	(p.value(	x1332	)))
filepoint.writelines	('\tx1333	'+	str	(p.value(	x1333	)))
filepoint.writelines	('\tx1334	'+	str	(p.value(	x1334	)))
filepoint.writelines	('\tx1335	'+	str	(p.value(	x1335	)))
filepoint.writelines	('\tx1336	'+	str	(p.value(	x1336	)))
filepoint.writelines	('\tx1337	'+	str	(p.value(	x1337	)))
filepoint.writelines	('\tx1338	'+	str	(p.value(	x1338	)))
filepoint.writelines	('\tx1339	'+	str	(p.value(	x1339	)))
filepoint.writelines	('\tx1340	'+	str	(p.value(	x1340	)))
filepoint.writelines	('\tx1341	'+	str	(p.value(	x1341	)))
filepoint.writelines	('\tx1342	'+	str	(p.value(	x1342	)))
filepoint.writelines	('\tx1343	'+	str	(p.value(	x1343	)))
filepoint.writelines	('\tx1344	'+	str	(p.value(	x1344	)))
filepoint.writelines	('\tx1345	'+	str	(p.value(	x1345	)))
filepoint.writelines	('\tx1346	'+	str	(p.value(	x1346	)))
filepoint.writelines	('\tx1347	'+	str	(p.value(	x1347	)))
filepoint.writelines	('\tx1348	'+	str	(p.value(	x1348	)))
filepoint.writelines	('\tx1349	'+	str	(p.value(	x1349	)))
filepoint.writelines	('\tx1350	'+	str	(p.value(	x1350	)))
filepoint.writelines	('\tx1351	'+	str	(p.value(	x1351	)))
filepoint.writelines	('\tx1352	'+	str	(p.value(	x1352	)))
filepoint.writelines	('\tx1353	'+	str	(p.value(	x1353	)))
filepoint.writelines	('\tx1354	'+	str	(p.value(	x1354	)))
filepoint.writelines	('\tx1355	'+	str	(p.value(	x1355	)))
filepoint.writelines	('\tx1356	'+	str	(p.value(	x1356	)))
filepoint.writelines	('\tx1357	'+	str	(p.value(	x1357	)))
filepoint.writelines	('\tx1358	'+	str	(p.value(	x1358	)))
filepoint.writelines	('\tx1359	'+	str	(p.value(	x1359	)))
filepoint.writelines	('\tx1360	'+	str	(p.value(	x1360	)))
filepoint.writelines	('\tx1361	'+	str	(p.value(	x1361	)))
filepoint.writelines	('\tx1362	'+	str	(p.value(	x1362	)))
filepoint.writelines	('\tx1363	'+	str	(p.value(	x1363	)))
filepoint.writelines	('\tx1364	'+	str	(p.value(	x1364	)))
filepoint.writelines	('\tx1365	'+	str	(p.value(	x1365	)))
filepoint.writelines	('\tx1366	'+	str	(p.value(	x1366	)))
filepoint.writelines	('\tx1367	'+	str	(p.value(	x1367	)))
filepoint.writelines	('\tx1368	'+	str	(p.value(	x1368	)))
filepoint.writelines	('\tx1369	'+	str	(p.value(	x1369	)))
filepoint.writelines	('\tx1370	'+	str	(p.value(	x1370	)))
filepoint.writelines	('\tx1371	'+	str	(p.value(	x1371	)))
filepoint.writelines	('\tx1372	'+	str	(p.value(	x1372	)))
filepoint.writelines	('\tx1373	'+	str	(p.value(	x1373	)))
filepoint.writelines	('\tx1374	'+	str	(p.value(	x1374	)))
filepoint.writelines	('\tx1375	'+	str	(p.value(	x1375	)))
filepoint.writelines	('\tx1376	'+	str	(p.value(	x1376	)))
filepoint.writelines	('\tx1377	'+	str	(p.value(	x1377	)))
filepoint.writelines	('\tx1378	'+	str	(p.value(	x1378	)))
filepoint.writelines	('\tx1379	'+	str	(p.value(	x1379	)))
filepoint.writelines	('\tx1380	'+	str	(p.value(	x1380	)))
filepoint.writelines	('\tx1381	'+	str	(p.value(	x1381	)))
filepoint.writelines	('\tx1382	'+	str	(p.value(	x1382	)))
filepoint.writelines	('\tx1383	'+	str	(p.value(	x1383	)))
filepoint.writelines	('\tx1384	'+	str	(p.value(	x1384	)))
filepoint.writelines	('\tx1385	'+	str	(p.value(	x1385	)))
filepoint.writelines	('\tx1386	'+	str	(p.value(	x1386	)))
filepoint.writelines	('\tx1387	'+	str	(p.value(	x1387	)))
filepoint.writelines	('\tx1388	'+	str	(p.value(	x1388	)))
filepoint.writelines	('\tx1389	'+	str	(p.value(	x1389	)))
filepoint.writelines	('\tx1390	'+	str	(p.value(	x1390	)))
filepoint.writelines	('\tx1391	'+	str	(p.value(	x1391	)))
filepoint.writelines	('\tx1392	'+	str	(p.value(	x1392	)))
filepoint.writelines	('\tx1393	'+	str	(p.value(	x1393	)))
filepoint.writelines	('\tx1394	'+	str	(p.value(	x1394	)))
filepoint.writelines	('\tx1395	'+	str	(p.value(	x1395	)))
filepoint.writelines	('\tx1396	'+	str	(p.value(	x1396	)))
filepoint.writelines	('\tx1397	'+	str	(p.value(	x1397	)))
filepoint.writelines	('\tx1398	'+	str	(p.value(	x1398	)))
filepoint.writelines	('\tx1399	'+	str	(p.value(	x1399	)))
filepoint.writelines	('\tx1400	'+	str	(p.value(	x1400	)))
filepoint.writelines	('\tx1401	'+	str	(p.value(	x1401	)))
filepoint.writelines	('\tx1402	'+	str	(p.value(	x1402	)))
filepoint.writelines	('\tx1403	'+	str	(p.value(	x1403	)))
filepoint.writelines	('\tx1404	'+	str	(p.value(	x1404	)))
filepoint.writelines	('\tx1405	'+	str	(p.value(	x1405	)))
filepoint.writelines	('\tx1406	'+	str	(p.value(	x1406	)))
filepoint.writelines	('\tx1407	'+	str	(p.value(	x1407	)))
filepoint.writelines	('\tx1408	'+	str	(p.value(	x1408	)))
filepoint.writelines	('\tx1409	'+	str	(p.value(	x1409	)))
filepoint.writelines	('\tx1410	'+	str	(p.value(	x1410	)))
filepoint.writelines	('\tx1411	'+	str	(p.value(	x1411	)))
filepoint.writelines	('\tx1412	'+	str	(p.value(	x1412	)))
filepoint.writelines	('\tx1413	'+	str	(p.value(	x1413	)))
filepoint.writelines	('\tx1414	'+	str	(p.value(	x1414	)))
filepoint.writelines	('\tx1415	'+	str	(p.value(	x1415	)))
filepoint.writelines	('\tx1416	'+	str	(p.value(	x1416	)))
filepoint.writelines	('\tx1417	'+	str	(p.value(	x1417	)))
filepoint.writelines	('\tx1418	'+	str	(p.value(	x1418	)))
filepoint.writelines	('\tx1419	'+	str	(p.value(	x1419	)))
filepoint.writelines	('\tx1420	'+	str	(p.value(	x1420	)))
filepoint.writelines	('\tx1421	'+	str	(p.value(	x1421	)))
filepoint.writelines	('\tx1422	'+	str	(p.value(	x1422	)))
filepoint.writelines	('\tx1423	'+	str	(p.value(	x1423	)))
filepoint.writelines	('\tx1424	'+	str	(p.value(	x1424	)))
filepoint.writelines	('\tx1425	'+	str	(p.value(	x1425	)))
filepoint.writelines	('\tx1426	'+	str	(p.value(	x1426	)))
filepoint.writelines	('\tx1427	'+	str	(p.value(	x1427	)))
filepoint.writelines	('\tx1428	'+	str	(p.value(	x1428	)))
filepoint.writelines	('\tx1429	'+	str	(p.value(	x1429	)))
filepoint.writelines	('\tx1430	'+	str	(p.value(	x1430	)))
filepoint.writelines	('\tx1431	'+	str	(p.value(	x1431	)))
filepoint.writelines	('\tx1432	'+	str	(p.value(	x1432	)))
filepoint.writelines	('\tx1433	'+	str	(p.value(	x1433	)))
filepoint.writelines	('\tx1434	'+	str	(p.value(	x1434	)))
filepoint.writelines	('\tx1435	'+	str	(p.value(	x1435	)))
filepoint.writelines	('\tx1436	'+	str	(p.value(	x1436	)))
filepoint.writelines	('\tx1437	'+	str	(p.value(	x1437	)))
filepoint.writelines	('\tx1438	'+	str	(p.value(	x1438	)))
filepoint.writelines	('\tx1439	'+	str	(p.value(	x1439	)))
filepoint.writelines	('\tx1440	'+	str	(p.value(	x1440	)))
filepoint.writelines	('\tx1441	'+	str	(p.value(	x1441	)))
filepoint.writelines	('\tx1442	'+	str	(p.value(	x1442	)))
filepoint.writelines	('\tx1443	'+	str	(p.value(	x1443	)))
filepoint.writelines	('\tx1444	'+	str	(p.value(	x1444	)))
filepoint.writelines	('\tx1445	'+	str	(p.value(	x1445	)))
filepoint.writelines	('\tx1446	'+	str	(p.value(	x1446	)))
filepoint.writelines	('\tx1447	'+	str	(p.value(	x1447	)))
filepoint.writelines	('\tx1448	'+	str	(p.value(	x1448	)))
filepoint.writelines	('\tx1449	'+	str	(p.value(	x1449	)))
filepoint.writelines	('\tx1450	'+	str	(p.value(	x1450	)))
filepoint.writelines	('\tx1451	'+	str	(p.value(	x1451	)))
filepoint.writelines	('\tx1452	'+	str	(p.value(	x1452	)))
filepoint.writelines	('\tx1453	'+	str	(p.value(	x1453	)))
filepoint.writelines	('\tx1454	'+	str	(p.value(	x1454	)))
filepoint.writelines	('\tx1455	'+	str	(p.value(	x1455	)))
filepoint.writelines	('\tx1456	'+	str	(p.value(	x1456	)))
filepoint.writelines	('\tx1457	'+	str	(p.value(	x1457	)))
filepoint.writelines	('\tx1458	'+	str	(p.value(	x1458	)))
filepoint.writelines	('\tx1459	'+	str	(p.value(	x1459	)))
filepoint.writelines	('\tx1460	'+	str	(p.value(	x1460	)))
filepoint.writelines	('\tx1461	'+	str	(p.value(	x1461	)))
filepoint.writelines	('\tx1462	'+	str	(p.value(	x1462	)))
filepoint.writelines	('\tx1463	'+	str	(p.value(	x1463	)))
filepoint.writelines	('\tx1464	'+	str	(p.value(	x1464	)))
filepoint.writelines	('\tx1465	'+	str	(p.value(	x1465	)))
filepoint.writelines	('\tx1466	'+	str	(p.value(	x1466	)))
filepoint.writelines	('\tx1467	'+	str	(p.value(	x1467	)))
filepoint.writelines	('\tx1468	'+	str	(p.value(	x1468	)))
filepoint.writelines	('\tx1469	'+	str	(p.value(	x1469	)))
filepoint.writelines	('\tx1470	'+	str	(p.value(	x1470	)))
filepoint.writelines	('\tx1471	'+	str	(p.value(	x1471	)))
filepoint.writelines	('\tx1472	'+	str	(p.value(	x1472	)))
filepoint.writelines	('\tx1473	'+	str	(p.value(	x1473	)))
filepoint.writelines	('\tx1474	'+	str	(p.value(	x1474	)))
filepoint.writelines	('\tx1475	'+	str	(p.value(	x1475	)))
filepoint.writelines	('\tx1476	'+	str	(p.value(	x1476	)))
filepoint.writelines	('\tx1477	'+	str	(p.value(	x1477	)))
filepoint.writelines	('\tx1478	'+	str	(p.value(	x1478	)))
filepoint.writelines	('\tx1479	'+	str	(p.value(	x1479	)))
filepoint.writelines	('\tx1480	'+	str	(p.value(	x1480	)))
filepoint.writelines	('\tx1481	'+	str	(p.value(	x1481	)))
filepoint.writelines	('\tx1482	'+	str	(p.value(	x1482	)))
filepoint.writelines	('\tx1483	'+	str	(p.value(	x1483	)))
filepoint.writelines	('\tx1484	'+	str	(p.value(	x1484	)))
filepoint.writelines	('\tx1485	'+	str	(p.value(	x1485	)))
filepoint.writelines	('\tx1486	'+	str	(p.value(	x1486	)))
filepoint.writelines	('\tx1487	'+	str	(p.value(	x1487	)))
filepoint.writelines	('\tx1488	'+	str	(p.value(	x1488	)))
filepoint.writelines	('\tx1489	'+	str	(p.value(	x1489	)))
filepoint.writelines	('\tx1490	'+	str	(p.value(	x1490	)))
filepoint.writelines	('\tx1491	'+	str	(p.value(	x1491	)))
filepoint.writelines	('\tx1492	'+	str	(p.value(	x1492	)))
filepoint.writelines	('\tx1493	'+	str	(p.value(	x1493	)))
filepoint.writelines	('\tx1494	'+	str	(p.value(	x1494	)))
filepoint.writelines	('\tx1495	'+	str	(p.value(	x1495	)))
filepoint.writelines	('\tx1496	'+	str	(p.value(	x1496	)))
filepoint.writelines	('\tx1497	'+	str	(p.value(	x1497	)))
filepoint.writelines	('\tx1498	'+	str	(p.value(	x1498	)))
filepoint.writelines	('\tx1499	'+	str	(p.value(	x1499	)))
filepoint.writelines	('\tx1500	'+	str	(p.value(	x1500	)))
filepoint.writelines	('\tx1501	'+	str	(p.value(	x1501	)))
filepoint.writelines	('\tx1502	'+	str	(p.value(	x1502	)))
filepoint.writelines	('\tx1503	'+	str	(p.value(	x1503	)))
filepoint.writelines	('\tx1504	'+	str	(p.value(	x1504	)))
filepoint.writelines	('\tx1505	'+	str	(p.value(	x1505	)))
filepoint.writelines	('\tx1506	'+	str	(p.value(	x1506	)))
filepoint.writelines	('\tx1507	'+	str	(p.value(	x1507	)))
filepoint.writelines	('\tx1508	'+	str	(p.value(	x1508	)))
filepoint.writelines	('\tx1509	'+	str	(p.value(	x1509	)))
filepoint.writelines	('\tx1510	'+	str	(p.value(	x1510	)))
filepoint.writelines	('\tx1511	'+	str	(p.value(	x1511	)))
filepoint.writelines	('\tx1512	'+	str	(p.value(	x1512	)))
filepoint.writelines	('\tx1513	'+	str	(p.value(	x1513	)))
filepoint.writelines	('\tx1514	'+	str	(p.value(	x1514	)))
filepoint.writelines	('\tx1515	'+	str	(p.value(	x1515	)))
filepoint.writelines	('\tx1516	'+	str	(p.value(	x1516	)))
filepoint.writelines	('\tx1517	'+	str	(p.value(	x1517	)))
filepoint.writelines	('\tx1518	'+	str	(p.value(	x1518	)))
filepoint.writelines	('\tx1519	'+	str	(p.value(	x1519	)))
filepoint.writelines	('\tx1520	'+	str	(p.value(	x1520	)))
filepoint.writelines	('\tx1521	'+	str	(p.value(	x1521	)))
filepoint.writelines	('\tx1522	'+	str	(p.value(	x1522	)))
filepoint.writelines	('\tx1523	'+	str	(p.value(	x1523	)))
filepoint.writelines	('\tx1524	'+	str	(p.value(	x1524	)))
filepoint.writelines	('\tx1525	'+	str	(p.value(	x1525	)))
filepoint.writelines	('\tx1526	'+	str	(p.value(	x1526	)))
filepoint.writelines	('\tx1527	'+	str	(p.value(	x1527	)))
filepoint.writelines	('\tx1528	'+	str	(p.value(	x1528	)))
filepoint.writelines	('\tx1529	'+	str	(p.value(	x1529	)))
filepoint.writelines	('\tx1530	'+	str	(p.value(	x1530	)))
filepoint.writelines	('\tx1531	'+	str	(p.value(	x1531	)))
filepoint.writelines	('\tx1532	'+	str	(p.value(	x1532	)))
filepoint.writelines	('\tx1533	'+	str	(p.value(	x1533	)))
filepoint.writelines	('\tx1534	'+	str	(p.value(	x1534	)))
filepoint.writelines	('\tx1535	'+	str	(p.value(	x1535	)))
filepoint.writelines	('\tx1536	'+	str	(p.value(	x1536	)))
filepoint.writelines	('\tx1537	'+	str	(p.value(	x1537	)))
filepoint.writelines	('\tx1538	'+	str	(p.value(	x1538	)))
filepoint.writelines	('\tx1539	'+	str	(p.value(	x1539	)))
filepoint.writelines	('\tx1540	'+	str	(p.value(	x1540	)))
filepoint.writelines	('\tx1541	'+	str	(p.value(	x1541	)))
filepoint.writelines	('\tx1542	'+	str	(p.value(	x1542	)))
filepoint.writelines	('\tx1543	'+	str	(p.value(	x1543	)))
filepoint.writelines	('\tx1544	'+	str	(p.value(	x1544	)))
filepoint.writelines	('\tx1545	'+	str	(p.value(	x1545	)))
filepoint.writelines	('\tx1546	'+	str	(p.value(	x1546	)))
filepoint.writelines	('\tx1547	'+	str	(p.value(	x1547	)))
filepoint.writelines	('\tx1548	'+	str	(p.value(	x1548	)))
filepoint.writelines	('\tx1549	'+	str	(p.value(	x1549	)))
filepoint.writelines	('\tx1550	'+	str	(p.value(	x1550	)))
filepoint.writelines	('\tx1551	'+	str	(p.value(	x1551	)))
filepoint.writelines	('\tx1552	'+	str	(p.value(	x1552	)))
filepoint.writelines	('\tx1553	'+	str	(p.value(	x1553	)))
filepoint.writelines	('\tx1554	'+	str	(p.value(	x1554	)))
filepoint.writelines	('\tx1555	'+	str	(p.value(	x1555	)))
filepoint.writelines	('\tx1556	'+	str	(p.value(	x1556	)))
filepoint.writelines	('\tx1557	'+	str	(p.value(	x1557	)))
filepoint.writelines	('\tx1558	'+	str	(p.value(	x1558	)))
filepoint.writelines	('\tx1559	'+	str	(p.value(	x1559	)))
filepoint.writelines	('\tx1560	'+	str	(p.value(	x1560	)))
filepoint.writelines	('\tx1561	'+	str	(p.value(	x1561	)))
filepoint.writelines	('\tx1562	'+	str	(p.value(	x1562	)))
filepoint.writelines	('\tx1563	'+	str	(p.value(	x1563	)))
filepoint.writelines	('\tx1564	'+	str	(p.value(	x1564	)))
filepoint.writelines	('\tx1565	'+	str	(p.value(	x1565	)))
filepoint.writelines	('\tx1566	'+	str	(p.value(	x1566	)))
filepoint.writelines	('\tx1567	'+	str	(p.value(	x1567	)))
filepoint.writelines	('\tx1568	'+	str	(p.value(	x1568	)))
filepoint.writelines	('\tx1569	'+	str	(p.value(	x1569	)))
filepoint.writelines	('\tx1570	'+	str	(p.value(	x1570	)))
filepoint.writelines	('\tx1571	'+	str	(p.value(	x1571	)))
filepoint.writelines	('\tx1572	'+	str	(p.value(	x1572	)))
filepoint.writelines	('\tx1573	'+	str	(p.value(	x1573	)))
filepoint.writelines	('\tx1574	'+	str	(p.value(	x1574	)))
filepoint.writelines	('\tx1575	'+	str	(p.value(	x1575	)))
filepoint.writelines	('\tx1576	'+	str	(p.value(	x1576	)))
filepoint.writelines	('\tx1577	'+	str	(p.value(	x1577	)))
filepoint.writelines	('\tx1578	'+	str	(p.value(	x1578	)))
filepoint.writelines	('\tx1579	'+	str	(p.value(	x1579	)))
filepoint.writelines	('\tx1580	'+	str	(p.value(	x1580	)))
filepoint.writelines	('\tx1581	'+	str	(p.value(	x1581	)))
filepoint.writelines	('\tx1582	'+	str	(p.value(	x1582	)))
filepoint.writelines	('\tx1583	'+	str	(p.value(	x1583	)))
filepoint.writelines	('\tx1584	'+	str	(p.value(	x1584	)))
filepoint.writelines	('\tx1585	'+	str	(p.value(	x1585	)))
filepoint.writelines	('\tx1586	'+	str	(p.value(	x1586	)))
filepoint.writelines	('\tx1587	'+	str	(p.value(	x1587	)))
filepoint.writelines	('\tx1588	'+	str	(p.value(	x1588	)))
filepoint.writelines	('\tx1589	'+	str	(p.value(	x1589	)))
filepoint.writelines	('\tx1590	'+	str	(p.value(	x1590	)))
filepoint.writelines	('\tx1591	'+	str	(p.value(	x1591	)))
filepoint.writelines	('\tx1592	'+	str	(p.value(	x1592	)))
filepoint.writelines	('\tx1593	'+	str	(p.value(	x1593	)))
filepoint.writelines	('\tx1594	'+	str	(p.value(	x1594	)))
filepoint.writelines	('\tx1595	'+	str	(p.value(	x1595	)))
filepoint.writelines	('\tx1596	'+	str	(p.value(	x1596	)))
filepoint.writelines	('\tx1597	'+	str	(p.value(	x1597	)))
filepoint.writelines	('\tx1598	'+	str	(p.value(	x1598	)))
filepoint.writelines	('\tx1599	'+	str	(p.value(	x1599	)))
filepoint.writelines	('\tx1600	'+	str	(p.value(	x1600	)))
filepoint.writelines	('\tx1601	'+	str	(p.value(	x1601	)))
filepoint.writelines	('\tx1602	'+	str	(p.value(	x1602	)))
filepoint.writelines	('\tx1603	'+	str	(p.value(	x1603	)))
filepoint.writelines	('\tx1604	'+	str	(p.value(	x1604	)))
filepoint.writelines	('\tx1605	'+	str	(p.value(	x1605	)))
filepoint.writelines	('\tx1606	'+	str	(p.value(	x1606	)))
filepoint.writelines	('\tx1607	'+	str	(p.value(	x1607	)))
filepoint.writelines	('\tx1608	'+	str	(p.value(	x1608	)))
filepoint.writelines	('\tx1609	'+	str	(p.value(	x1609	)))
filepoint.writelines	('\tx1610	'+	str	(p.value(	x1610	)))
filepoint.writelines	('\tx1611	'+	str	(p.value(	x1611	)))
filepoint.writelines	('\tx1612	'+	str	(p.value(	x1612	)))
filepoint.writelines	('\tx1613	'+	str	(p.value(	x1613	)))
filepoint.writelines	('\tx1614	'+	str	(p.value(	x1614	)))
filepoint.writelines	('\tx1615	'+	str	(p.value(	x1615	)))
filepoint.writelines	('\tx1616	'+	str	(p.value(	x1616	)))
filepoint.writelines	('\tx1617	'+	str	(p.value(	x1617	)))
filepoint.writelines	('\tx1618	'+	str	(p.value(	x1618	)))
filepoint.writelines	('\tx1619	'+	str	(p.value(	x1619	)))
filepoint.writelines	('\tx1620	'+	str	(p.value(	x1620	)))
filepoint.writelines	('\tx1621	'+	str	(p.value(	x1621	)))
filepoint.writelines	('\tx1622	'+	str	(p.value(	x1622	)))
filepoint.writelines	('\tx1623	'+	str	(p.value(	x1623	)))
filepoint.writelines	('\tx1624	'+	str	(p.value(	x1624	)))
filepoint.writelines	('\tx1625	'+	str	(p.value(	x1625	)))
filepoint.writelines	('\tx1626	'+	str	(p.value(	x1626	)))
filepoint.writelines	('\tx1627	'+	str	(p.value(	x1627	)))
filepoint.writelines	('\tx1628	'+	str	(p.value(	x1628	)))
filepoint.writelines	('\tx1629	'+	str	(p.value(	x1629	)))
filepoint.writelines	('\tx1630	'+	str	(p.value(	x1630	)))
filepoint.writelines	('\tx1631	'+	str	(p.value(	x1631	)))
filepoint.writelines	('\tx1632	'+	str	(p.value(	x1632	)))
filepoint.writelines	('\tx1633	'+	str	(p.value(	x1633	)))
filepoint.writelines	('\tx1634	'+	str	(p.value(	x1634	)))
filepoint.writelines	('\tx1635	'+	str	(p.value(	x1635	)))
filepoint.writelines	('\tx1636	'+	str	(p.value(	x1636	)))
filepoint.writelines	('\tx1637	'+	str	(p.value(	x1637	)))
filepoint.writelines	('\tx1638	'+	str	(p.value(	x1638	)))
filepoint.writelines	('\tx1639	'+	str	(p.value(	x1639	)))
filepoint.writelines	('\tx1640	'+	str	(p.value(	x1640	)))
filepoint.writelines	('\tx1641	'+	str	(p.value(	x1641	)))
filepoint.writelines	('\tx1642	'+	str	(p.value(	x1642	)))
filepoint.writelines	('\tx1643	'+	str	(p.value(	x1643	)))
filepoint.writelines	('\tx1644	'+	str	(p.value(	x1644	)))
filepoint.writelines	('\tx1645	'+	str	(p.value(	x1645	)))
filepoint.writelines	('\tx1646	'+	str	(p.value(	x1646	)))
filepoint.writelines	('\tx1647	'+	str	(p.value(	x1647	)))
filepoint.writelines	('\tx1648	'+	str	(p.value(	x1648	)))
filepoint.writelines	('\tx1649	'+	str	(p.value(	x1649	)))
filepoint.writelines	('\tx1650	'+	str	(p.value(	x1650	)))
filepoint.writelines	('\tx1651	'+	str	(p.value(	x1651	)))
filepoint.writelines	('\tx1652	'+	str	(p.value(	x1652	)))
filepoint.writelines	('\tx1653	'+	str	(p.value(	x1653	)))
filepoint.writelines	('\tx1654	'+	str	(p.value(	x1654	)))
filepoint.writelines	('\tx1655	'+	str	(p.value(	x1655	)))
filepoint.writelines	('\tx1656	'+	str	(p.value(	x1656	)))
filepoint.writelines	('\tx1657	'+	str	(p.value(	x1657	)))
filepoint.writelines	('\tx1658	'+	str	(p.value(	x1658	)))
filepoint.writelines	('\tx1659	'+	str	(p.value(	x1659	)))
filepoint.writelines	('\tx1660	'+	str	(p.value(	x1660	)))
filepoint.writelines	('\tx1661	'+	str	(p.value(	x1661	)))
filepoint.writelines	('\tx1662	'+	str	(p.value(	x1662	)))
filepoint.writelines	('\tx1663	'+	str	(p.value(	x1663	)))
filepoint.writelines	('\tx1664	'+	str	(p.value(	x1664	)))
filepoint.writelines	('\tx1665	'+	str	(p.value(	x1665	)))
filepoint.writelines	('\tx1666	'+	str	(p.value(	x1666	)))
filepoint.writelines	('\tx1667	'+	str	(p.value(	x1667	)))
filepoint.writelines	('\tx1668	'+	str	(p.value(	x1668	)))
filepoint.writelines	('\tx1669	'+	str	(p.value(	x1669	)))
filepoint.writelines	('\tx1670	'+	str	(p.value(	x1670	)))
filepoint.writelines	('\tx1671	'+	str	(p.value(	x1671	)))
filepoint.writelines	('\tx1672	'+	str	(p.value(	x1672	)))
filepoint.writelines	('\tx1673	'+	str	(p.value(	x1673	)))
filepoint.writelines	('\tx1674	'+	str	(p.value(	x1674	)))
filepoint.writelines	('\tx1675	'+	str	(p.value(	x1675	)))
filepoint.writelines	('\tx1676	'+	str	(p.value(	x1676	)))
filepoint.writelines	('\tx1677	'+	str	(p.value(	x1677	)))
filepoint.writelines	('\tx1678	'+	str	(p.value(	x1678	)))
filepoint.writelines	('\tx1679	'+	str	(p.value(	x1679	)))
filepoint.writelines	('\tx1680	'+	str	(p.value(	x1680	)))
filepoint.writelines	('\tx1681	'+	str	(p.value(	x1681	)))
filepoint.writelines	('\tx1682	'+	str	(p.value(	x1682	)))
filepoint.writelines	('\tx1683	'+	str	(p.value(	x1683	)))
filepoint.writelines	('\tx1684	'+	str	(p.value(	x1684	)))
filepoint.writelines	('\tx1685	'+	str	(p.value(	x1685	)))
filepoint.writelines	('\tx1686	'+	str	(p.value(	x1686	)))
filepoint.writelines	('\tx1687	'+	str	(p.value(	x1687	)))
filepoint.writelines	('\tx1688	'+	str	(p.value(	x1688	)))
filepoint.writelines	('\tx1689	'+	str	(p.value(	x1689	)))
filepoint.writelines	('\tx1690	'+	str	(p.value(	x1690	)))
filepoint.writelines	('\tx1691	'+	str	(p.value(	x1691	)))
filepoint.writelines	('\tx1692	'+	str	(p.value(	x1692	)))
filepoint.writelines	('\tx1693	'+	str	(p.value(	x1693	)))
filepoint.writelines	('\tx1694	'+	str	(p.value(	x1694	)))
filepoint.writelines	('\tx1695	'+	str	(p.value(	x1695	)))
filepoint.writelines	('\tx1696	'+	str	(p.value(	x1696	)))
filepoint.writelines	('\tx1697	'+	str	(p.value(	x1697	)))
filepoint.writelines	('\tx1698	'+	str	(p.value(	x1698	)))
filepoint.writelines	('\tx1699	'+	str	(p.value(	x1699	)))
filepoint.writelines	('\tx1700	'+	str	(p.value(	x1700	)))
filepoint.writelines	('\tx1701	'+	str	(p.value(	x1701	)))
filepoint.writelines	('\tx1702	'+	str	(p.value(	x1702	)))
filepoint.writelines	('\tx1703	'+	str	(p.value(	x1703	)))
filepoint.writelines	('\tx1704	'+	str	(p.value(	x1704	)))
filepoint.writelines	('\tx1705	'+	str	(p.value(	x1705	)))
filepoint.writelines	('\tx1706	'+	str	(p.value(	x1706	)))
filepoint.writelines	('\tx1707	'+	str	(p.value(	x1707	)))
filepoint.writelines	('\tx1708	'+	str	(p.value(	x1708	)))
filepoint.writelines	('\tx1709	'+	str	(p.value(	x1709	)))
filepoint.writelines	('\tx1710	'+	str	(p.value(	x1710	)))
filepoint.writelines	('\tx1711	'+	str	(p.value(	x1711	)))
filepoint.writelines	('\tx1712	'+	str	(p.value(	x1712	)))
filepoint.writelines	('\tx1713	'+	str	(p.value(	x1713	)))
filepoint.writelines	('\tx1714	'+	str	(p.value(	x1714	)))
filepoint.writelines	('\tx1715	'+	str	(p.value(	x1715	)))
filepoint.writelines	('\tx1716	'+	str	(p.value(	x1716	)))
filepoint.writelines	('\tx1717	'+	str	(p.value(	x1717	)))
filepoint.writelines	('\tx1718	'+	str	(p.value(	x1718	)))
filepoint.writelines	('\tx1719	'+	str	(p.value(	x1719	)))
filepoint.writelines	('\tx1720	'+	str	(p.value(	x1720	)))
filepoint.writelines	('\tx1721	'+	str	(p.value(	x1721	)))
filepoint.writelines	('\tx1722	'+	str	(p.value(	x1722	)))
filepoint.writelines	('\tx1723	'+	str	(p.value(	x1723	)))
filepoint.writelines	('\tx1724	'+	str	(p.value(	x1724	)))
filepoint.writelines	('\tx1725	'+	str	(p.value(	x1725	)))
filepoint.writelines	('\tx1726	'+	str	(p.value(	x1726	)))
filepoint.writelines	('\tx1727	'+	str	(p.value(	x1727	)))
filepoint.writelines	('\tx1728	'+	str	(p.value(	x1728	)))
filepoint.writelines	('\tx1729	'+	str	(p.value(	x1729	)))
filepoint.writelines	('\tx1730	'+	str	(p.value(	x1730	)))
filepoint.writelines	('\tx1731	'+	str	(p.value(	x1731	)))
filepoint.writelines	('\tx1732	'+	str	(p.value(	x1732	)))
filepoint.writelines	('\tx1733	'+	str	(p.value(	x1733	)))
filepoint.writelines	('\tx1734	'+	str	(p.value(	x1734	)))
filepoint.writelines	('\tx1735	'+	str	(p.value(	x1735	)))
filepoint.writelines	('\tx1736	'+	str	(p.value(	x1736	)))
filepoint.writelines	('\tx1737	'+	str	(p.value(	x1737	)))
filepoint.writelines	('\tx1738	'+	str	(p.value(	x1738	)))
filepoint.writelines	('\tx1739	'+	str	(p.value(	x1739	)))
filepoint.writelines	('\tx1740	'+	str	(p.value(	x1740	)))
filepoint.writelines	('\tx1741	'+	str	(p.value(	x1741	)))
filepoint.writelines	('\tx1742	'+	str	(p.value(	x1742	)))
filepoint.writelines	('\tx1743	'+	str	(p.value(	x1743	)))
filepoint.writelines	('\tx1744	'+	str	(p.value(	x1744	)))
filepoint.writelines	('\tx1745	'+	str	(p.value(	x1745	)))
filepoint.writelines	('\tx1746	'+	str	(p.value(	x1746	)))
filepoint.writelines	('\tx1747	'+	str	(p.value(	x1747	)))
filepoint.writelines	('\tx1748	'+	str	(p.value(	x1748	)))
filepoint.writelines	('\tx1749	'+	str	(p.value(	x1749	)))
filepoint.writelines	('\tx1750	'+	str	(p.value(	x1750	)))
filepoint.writelines	('\tx1751	'+	str	(p.value(	x1751	)))
filepoint.writelines	('\tx1752	'+	str	(p.value(	x1752	)))
filepoint.writelines	('\tx1753	'+	str	(p.value(	x1753	)))
filepoint.writelines	('\tx1754	'+	str	(p.value(	x1754	)))
filepoint.writelines	('\tx1755	'+	str	(p.value(	x1755	)))
filepoint.writelines	('\tx1756	'+	str	(p.value(	x1756	)))
filepoint.writelines	('\tx1757	'+	str	(p.value(	x1757	)))
filepoint.writelines	('\tx1758	'+	str	(p.value(	x1758	)))
filepoint.writelines	('\tx1759	'+	str	(p.value(	x1759	)))
filepoint.writelines	('\tx1760	'+	str	(p.value(	x1760	)))
filepoint.writelines	('\tx1761	'+	str	(p.value(	x1761	)))
filepoint.writelines	('\tx1762	'+	str	(p.value(	x1762	)))
filepoint.writelines	('\tx1763	'+	str	(p.value(	x1763	)))
filepoint.writelines	('\tx1764	'+	str	(p.value(	x1764	)))
filepoint.writelines	('\tx1765	'+	str	(p.value(	x1765	)))
filepoint.writelines	('\tx1766	'+	str	(p.value(	x1766	)))
filepoint.writelines	('\tx1767	'+	str	(p.value(	x1767	)))
filepoint.writelines	('\tx1768	'+	str	(p.value(	x1768	)))
filepoint.writelines	('\tx1769	'+	str	(p.value(	x1769	)))
filepoint.writelines	('\tx1770	'+	str	(p.value(	x1770	)))
filepoint.writelines	('\tx1771	'+	str	(p.value(	x1771	)))
filepoint.writelines	('\tx1772	'+	str	(p.value(	x1772	)))
filepoint.writelines	('\tx1773	'+	str	(p.value(	x1773	)))
filepoint.writelines	('\tx1774	'+	str	(p.value(	x1774	)))
filepoint.writelines	('\tx1775	'+	str	(p.value(	x1775	)))
filepoint.writelines	('\tx1776	'+	str	(p.value(	x1776	)))
filepoint.writelines	('\tx1777	'+	str	(p.value(	x1777	)))
filepoint.writelines	('\tx1778	'+	str	(p.value(	x1778	)))
filepoint.writelines	('\tx1779	'+	str	(p.value(	x1779	)))
filepoint.writelines	('\tx1780	'+	str	(p.value(	x1780	)))
filepoint.writelines	('\tx1781	'+	str	(p.value(	x1781	)))
filepoint.writelines	('\tx1782	'+	str	(p.value(	x1782	)))
filepoint.writelines	('\tx1783	'+	str	(p.value(	x1783	)))
filepoint.writelines	('\tx1784	'+	str	(p.value(	x1784	)))
filepoint.writelines	('\tx1785	'+	str	(p.value(	x1785	)))
filepoint.writelines	('\tx1786	'+	str	(p.value(	x1786	)))
filepoint.writelines	('\tx1787	'+	str	(p.value(	x1787	)))
filepoint.writelines	('\tx1788	'+	str	(p.value(	x1788	)))
filepoint.writelines	('\tx1789	'+	str	(p.value(	x1789	)))
filepoint.writelines	('\tx1790	'+	str	(p.value(	x1790	)))
filepoint.writelines	('\tx1791	'+	str	(p.value(	x1791	)))
filepoint.writelines	('\tx1792	'+	str	(p.value(	x1792	)))
filepoint.writelines	('\tx1793	'+	str	(p.value(	x1793	)))
filepoint.writelines	('\tx1794	'+	str	(p.value(	x1794	)))
filepoint.writelines	('\tx1795	'+	str	(p.value(	x1795	)))
filepoint.writelines	('\tx1796	'+	str	(p.value(	x1796	)))
filepoint.writelines	('\tx1797	'+	str	(p.value(	x1797	)))
filepoint.writelines	('\tx1798	'+	str	(p.value(	x1798	)))
filepoint.writelines	('\tx1799	'+	str	(p.value(	x1799	)))
filepoint.writelines	('\tx1800	'+	str	(p.value(	x1800	)))
filepoint.writelines	('\tx1801	'+	str	(p.value(	x1801	)))
filepoint.writelines	('\tx1802	'+	str	(p.value(	x1802	)))
filepoint.writelines	('\tx1803	'+	str	(p.value(	x1803	)))
filepoint.writelines	('\tx1804	'+	str	(p.value(	x1804	)))
filepoint.writelines	('\tx1805	'+	str	(p.value(	x1805	)))
filepoint.writelines	('\tx1806	'+	str	(p.value(	x1806	)))
filepoint.writelines	('\tx1807	'+	str	(p.value(	x1807	)))
filepoint.writelines	('\tx1808	'+	str	(p.value(	x1808	)))
filepoint.writelines	('\tx1809	'+	str	(p.value(	x1809	)))
filepoint.writelines	('\tx1810	'+	str	(p.value(	x1810	)))
filepoint.writelines	('\tx1811	'+	str	(p.value(	x1811	)))
filepoint.writelines	('\tx1812	'+	str	(p.value(	x1812	)))
filepoint.writelines	('\tx1813	'+	str	(p.value(	x1813	)))
filepoint.writelines	('\tx1814	'+	str	(p.value(	x1814	)))
filepoint.writelines	('\tx1815	'+	str	(p.value(	x1815	)))
filepoint.writelines	('\tx1816	'+	str	(p.value(	x1816	)))
filepoint.writelines	('\tx1817	'+	str	(p.value(	x1817	)))
filepoint.writelines	('\tx1818	'+	str	(p.value(	x1818	)))
filepoint.writelines	('\tx1819	'+	str	(p.value(	x1819	)))
filepoint.writelines	('\tx1820	'+	str	(p.value(	x1820	)))
filepoint.writelines	('\tx1821	'+	str	(p.value(	x1821	)))
filepoint.writelines	('\tx1822	'+	str	(p.value(	x1822	)))
filepoint.writelines	('\tx1823	'+	str	(p.value(	x1823	)))
filepoint.writelines	('\tx1824	'+	str	(p.value(	x1824	)))
filepoint.writelines	('\tx1825	'+	str	(p.value(	x1825	)))
filepoint.writelines	('\tx1826	'+	str	(p.value(	x1826	)))
filepoint.writelines	('\tx1827	'+	str	(p.value(	x1827	)))
filepoint.writelines	('\tx1828	'+	str	(p.value(	x1828	)))
filepoint.writelines	('\tx1829	'+	str	(p.value(	x1829	)))
filepoint.writelines	('\tx1830	'+	str	(p.value(	x1830	)))
filepoint.writelines	('\tx1831	'+	str	(p.value(	x1831	)))
filepoint.writelines	('\tx1832	'+	str	(p.value(	x1832	)))
filepoint.writelines	('\tx1833	'+	str	(p.value(	x1833	)))
filepoint.writelines	('\tx1834	'+	str	(p.value(	x1834	)))
filepoint.writelines	('\tx1835	'+	str	(p.value(	x1835	)))
filepoint.writelines	('\tx1836	'+	str	(p.value(	x1836	)))
filepoint.writelines	('\tx1837	'+	str	(p.value(	x1837	)))
filepoint.writelines	('\tx1838	'+	str	(p.value(	x1838	)))
filepoint.writelines	('\tx1839	'+	str	(p.value(	x1839	)))
filepoint.writelines	('\tx1840	'+	str	(p.value(	x1840	)))
filepoint.writelines	('\tx1841	'+	str	(p.value(	x1841	)))
filepoint.writelines	('\tx1842	'+	str	(p.value(	x1842	)))
filepoint.writelines	('\tx1843	'+	str	(p.value(	x1843	)))
filepoint.writelines	('\tx1844	'+	str	(p.value(	x1844	)))
filepoint.writelines	('\tx1845	'+	str	(p.value(	x1845	)))
filepoint.writelines	('\tx1846	'+	str	(p.value(	x1846	)))
filepoint.writelines	('\tx1847	'+	str	(p.value(	x1847	)))
filepoint.writelines	('\tx1848	'+	str	(p.value(	x1848	)))
filepoint.writelines	('\tx1849	'+	str	(p.value(	x1849	)))
filepoint.writelines	('\tx1850	'+	str	(p.value(	x1850	)))
filepoint.writelines	('\tx1851	'+	str	(p.value(	x1851	)))
filepoint.writelines	('\tx1852	'+	str	(p.value(	x1852	)))
filepoint.writelines	('\tx1853	'+	str	(p.value(	x1853	)))
filepoint.writelines	('\tx1854	'+	str	(p.value(	x1854	)))
filepoint.writelines	('\tx1855	'+	str	(p.value(	x1855	)))
filepoint.writelines	('\tx1856	'+	str	(p.value(	x1856	)))
filepoint.writelines	('\tx1857	'+	str	(p.value(	x1857	)))
filepoint.writelines	('\tx1858	'+	str	(p.value(	x1858	)))
filepoint.writelines	('\tx1859	'+	str	(p.value(	x1859	)))
filepoint.writelines	('\tx1860	'+	str	(p.value(	x1860	)))
filepoint.writelines	('\tx1861	'+	str	(p.value(	x1861	)))
filepoint.writelines	('\tx1862	'+	str	(p.value(	x1862	)))
filepoint.writelines	('\tx1863	'+	str	(p.value(	x1863	)))
filepoint.writelines	('\tx1864	'+	str	(p.value(	x1864	)))
filepoint.writelines	('\tx1865	'+	str	(p.value(	x1865	)))
filepoint.writelines	('\tx1866	'+	str	(p.value(	x1866	)))
filepoint.writelines	('\tx1867	'+	str	(p.value(	x1867	)))
filepoint.writelines	('\tx1868	'+	str	(p.value(	x1868	)))
filepoint.writelines	('\tx1869	'+	str	(p.value(	x1869	)))
filepoint.writelines	('\tx1870	'+	str	(p.value(	x1870	)))
filepoint.writelines	('\tx1871	'+	str	(p.value(	x1871	)))
filepoint.writelines	('\tx1872	'+	str	(p.value(	x1872	)))
filepoint.writelines	('\tx1873	'+	str	(p.value(	x1873	)))
filepoint.writelines	('\tx1874	'+	str	(p.value(	x1874	)))
filepoint.writelines	('\tx1875	'+	str	(p.value(	x1875	)))
filepoint.writelines	('\tx1876	'+	str	(p.value(	x1876	)))
filepoint.writelines	('\tx1877	'+	str	(p.value(	x1877	)))
filepoint.writelines	('\tx1878	'+	str	(p.value(	x1878	)))
filepoint.writelines	('\tx1879	'+	str	(p.value(	x1879	)))
filepoint.writelines	('\tx1880	'+	str	(p.value(	x1880	)))
filepoint.writelines	('\tx1881	'+	str	(p.value(	x1881	)))
filepoint.writelines	('\tx1882	'+	str	(p.value(	x1882	)))
filepoint.writelines	('\tx1883	'+	str	(p.value(	x1883	)))
filepoint.writelines	('\tx1884	'+	str	(p.value(	x1884	)))
filepoint.writelines	('\tx1885	'+	str	(p.value(	x1885	)))
filepoint.writelines	('\tx1886	'+	str	(p.value(	x1886	)))
filepoint.writelines	('\tx1887	'+	str	(p.value(	x1887	)))
filepoint.writelines	('\tx1888	'+	str	(p.value(	x1888	)))
filepoint.writelines	('\tx1889	'+	str	(p.value(	x1889	)))
filepoint.writelines	('\tx1890	'+	str	(p.value(	x1890	)))
filepoint.writelines	('\tx1891	'+	str	(p.value(	x1891	)))
filepoint.writelines	('\tx1892	'+	str	(p.value(	x1892	)))
filepoint.writelines	('\tx1893	'+	str	(p.value(	x1893	)))
filepoint.writelines	('\tx1894	'+	str	(p.value(	x1894	)))
filepoint.writelines	('\tx1895	'+	str	(p.value(	x1895	)))
filepoint.writelines	('\tx1896	'+	str	(p.value(	x1896	)))
filepoint.writelines	('\tx1897	'+	str	(p.value(	x1897	)))
filepoint.writelines	('\tx1898	'+	str	(p.value(	x1898	)))
filepoint.writelines	('\tx1899	'+	str	(p.value(	x1899	)))
filepoint.writelines	('\tx1900	'+	str	(p.value(	x1900	)))
filepoint.writelines	('\tx1901	'+	str	(p.value(	x1901	)))
filepoint.writelines	('\tx1902	'+	str	(p.value(	x1902	)))
filepoint.writelines	('\tx1903	'+	str	(p.value(	x1903	)))
filepoint.writelines	('\tx1904	'+	str	(p.value(	x1904	)))
filepoint.writelines	('\tx1905	'+	str	(p.value(	x1905	)))
filepoint.writelines	('\tx1906	'+	str	(p.value(	x1906	)))
filepoint.writelines	('\tx1907	'+	str	(p.value(	x1907	)))
filepoint.writelines	('\tx1908	'+	str	(p.value(	x1908	)))
filepoint.writelines	('\tx1909	'+	str	(p.value(	x1909	)))
filepoint.writelines	('\tx1910	'+	str	(p.value(	x1910	)))
filepoint.writelines	('\tx1911	'+	str	(p.value(	x1911	)))
filepoint.writelines	('\tx1912	'+	str	(p.value(	x1912	)))
filepoint.writelines	('\tx1913	'+	str	(p.value(	x1913	)))
filepoint.writelines	('\tx1914	'+	str	(p.value(	x1914	)))
filepoint.writelines	('\tx1915	'+	str	(p.value(	x1915	)))
filepoint.writelines	('\tx1916	'+	str	(p.value(	x1916	)))
filepoint.writelines	('\tx1917	'+	str	(p.value(	x1917	)))
filepoint.writelines	('\tx1918	'+	str	(p.value(	x1918	)))
filepoint.writelines	('\tx1919	'+	str	(p.value(	x1919	)))
filepoint.writelines	('\tx1920	'+	str	(p.value(	x1920	)))
filepoint.writelines	('\tx1921	'+	str	(p.value(	x1921	)))
filepoint.writelines	('\tx1922	'+	str	(p.value(	x1922	)))
filepoint.writelines	('\tx1923	'+	str	(p.value(	x1923	)))
filepoint.writelines	('\tx1924	'+	str	(p.value(	x1924	)))
filepoint.writelines	('\tx1925	'+	str	(p.value(	x1925	)))
filepoint.writelines	('\tx1926	'+	str	(p.value(	x1926	)))
filepoint.writelines	('\tx1927	'+	str	(p.value(	x1927	)))
filepoint.writelines	('\tx1928	'+	str	(p.value(	x1928	)))
filepoint.writelines	('\tx1929	'+	str	(p.value(	x1929	)))
filepoint.writelines	('\tx1930	'+	str	(p.value(	x1930	)))
filepoint.writelines	('\tx1931	'+	str	(p.value(	x1931	)))
filepoint.writelines	('\tx1932	'+	str	(p.value(	x1932	)))
filepoint.writelines	('\tx1933	'+	str	(p.value(	x1933	)))
filepoint.writelines	('\tx1934	'+	str	(p.value(	x1934	)))
filepoint.writelines	('\tx1935	'+	str	(p.value(	x1935	)))
filepoint.writelines	('\tx1936	'+	str	(p.value(	x1936	)))
filepoint.writelines	('\tx1937	'+	str	(p.value(	x1937	)))
filepoint.writelines	('\tx1938	'+	str	(p.value(	x1938	)))
filepoint.writelines	('\tx1939	'+	str	(p.value(	x1939	)))
filepoint.writelines	('\tx1940	'+	str	(p.value(	x1940	)))
filepoint.writelines	('\tx1941	'+	str	(p.value(	x1941	)))
filepoint.writelines	('\tx1942	'+	str	(p.value(	x1942	)))
filepoint.writelines	('\tx1943	'+	str	(p.value(	x1943	)))
filepoint.writelines	('\tx1944	'+	str	(p.value(	x1944	)))
filepoint.writelines	('\tx1945	'+	str	(p.value(	x1945	)))
filepoint.writelines	('\tx1946	'+	str	(p.value(	x1946	)))
filepoint.writelines	('\tx1947	'+	str	(p.value(	x1947	)))
filepoint.writelines	('\tx1948	'+	str	(p.value(	x1948	)))
filepoint.writelines	('\tx1949	'+	str	(p.value(	x1949	)))
filepoint.writelines	('\tx1950	'+	str	(p.value(	x1950	)))
filepoint.writelines	('\tx1951	'+	str	(p.value(	x1951	)))
filepoint.writelines	('\tx1952	'+	str	(p.value(	x1952	)))
filepoint.writelines	('\tx1953	'+	str	(p.value(	x1953	)))
filepoint.writelines	('\tx1954	'+	str	(p.value(	x1954	)))
filepoint.writelines	('\tx1955	'+	str	(p.value(	x1955	)))
filepoint.writelines	('\tx1956	'+	str	(p.value(	x1956	)))
filepoint.writelines	('\tx1957	'+	str	(p.value(	x1957	)))
filepoint.writelines	('\tx1958	'+	str	(p.value(	x1958	)))
filepoint.writelines	('\tx1959	'+	str	(p.value(	x1959	)))
filepoint.writelines	('\tx1960	'+	str	(p.value(	x1960	)))
filepoint.writelines	('\tx1961	'+	str	(p.value(	x1961	)))
filepoint.writelines	('\tx1962	'+	str	(p.value(	x1962	)))
filepoint.writelines	('\tx1963	'+	str	(p.value(	x1963	)))
filepoint.writelines	('\tx1964	'+	str	(p.value(	x1964	)))
filepoint.writelines	('\tx1965	'+	str	(p.value(	x1965	)))
filepoint.writelines	('\tx1966	'+	str	(p.value(	x1966	)))
filepoint.writelines	('\tx1967	'+	str	(p.value(	x1967	)))
filepoint.writelines	('\tx1968	'+	str	(p.value(	x1968	)))
filepoint.writelines	('\tx1969	'+	str	(p.value(	x1969	)))
filepoint.writelines	('\tx1970	'+	str	(p.value(	x1970	)))
filepoint.writelines	('\tx1971	'+	str	(p.value(	x1971	)))
filepoint.writelines	('\tx1972	'+	str	(p.value(	x1972	)))
filepoint.writelines	('\tx1973	'+	str	(p.value(	x1973	)))
filepoint.writelines	('\tx1974	'+	str	(p.value(	x1974	)))
filepoint.writelines	('\tx1975	'+	str	(p.value(	x1975	)))
filepoint.writelines	('\tx1976	'+	str	(p.value(	x1976	)))
filepoint.writelines	('\tx1977	'+	str	(p.value(	x1977	)))
filepoint.writelines	('\tx1978	'+	str	(p.value(	x1978	)))
filepoint.writelines	('\tx1979	'+	str	(p.value(	x1979	)))
filepoint.writelines	('\tx1980	'+	str	(p.value(	x1980	)))
filepoint.writelines	('\tx1981	'+	str	(p.value(	x1981	)))
filepoint.writelines	('\tx1982	'+	str	(p.value(	x1982	)))
filepoint.writelines	('\tx1983	'+	str	(p.value(	x1983	)))
filepoint.writelines	('\tx1984	'+	str	(p.value(	x1984	)))
filepoint.writelines	('\tx1985	'+	str	(p.value(	x1985	)))
filepoint.writelines	('\tx1986	'+	str	(p.value(	x1986	)))
filepoint.writelines	('\tx1987	'+	str	(p.value(	x1987	)))
filepoint.writelines	('\tx1988	'+	str	(p.value(	x1988	)))
filepoint.writelines	('\tx1989	'+	str	(p.value(	x1989	)))
filepoint.writelines	('\tx1990	'+	str	(p.value(	x1990	)))
filepoint.writelines	('\tx1991	'+	str	(p.value(	x1991	)))
filepoint.writelines	('\tx1992	'+	str	(p.value(	x1992	)))
filepoint.writelines	('\tx1993	'+	str	(p.value(	x1993	)))
filepoint.writelines	('\tx1994	'+	str	(p.value(	x1994	)))
filepoint.writelines	('\tx1995	'+	str	(p.value(	x1995	)))
filepoint.writelines	('\tx1996	'+	str	(p.value(	x1996	)))
filepoint.writelines	('\tx1997	'+	str	(p.value(	x1997	)))
filepoint.writelines	('\tx1998	'+	str	(p.value(	x1998	)))
filepoint.writelines	('\tx1999	'+	str	(p.value(	x1999	)))
filepoint.writelines	('\tx2000	'+	str	(p.value(	x2000	)))
filepoint.writelines	('\tx2001	'+	str	(p.value(	x2001	)))
filepoint.writelines	('\tx2002	'+	str	(p.value(	x2002	)))
filepoint.writelines	('\tx2003	'+	str	(p.value(	x2003	)))
filepoint.writelines	('\tx2004	'+	str	(p.value(	x2004	)))
filepoint.writelines	('\tx2005	'+	str	(p.value(	x2005	)))
filepoint.writelines	('\tx2006	'+	str	(p.value(	x2006	)))
filepoint.writelines	('\tx2007	'+	str	(p.value(	x2007	)))
filepoint.writelines	('\tx2008	'+	str	(p.value(	x2008	)))
filepoint.writelines	('\tx2009	'+	str	(p.value(	x2009	)))
filepoint.writelines	('\tx2010	'+	str	(p.value(	x2010	)))
filepoint.writelines	('\tx2011	'+	str	(p.value(	x2011	)))
filepoint.writelines	('\tx2012	'+	str	(p.value(	x2012	)))
filepoint.writelines	('\tx2013	'+	str	(p.value(	x2013	)))
filepoint.writelines	('\tx2014	'+	str	(p.value(	x2014	)))
filepoint.writelines	('\tx2015	'+	str	(p.value(	x2015	)))
filepoint.writelines	('\tx2016	'+	str	(p.value(	x2016	)))
filepoint.writelines	('\tx2017	'+	str	(p.value(	x2017	)))
filepoint.writelines	('\tx2018	'+	str	(p.value(	x2018	)))
filepoint.writelines	('\tx2019	'+	str	(p.value(	x2019	)))
filepoint.writelines	('\tx2020	'+	str	(p.value(	x2020	)))
filepoint.writelines	('\tx2021	'+	str	(p.value(	x2021	)))
filepoint.writelines	('\tx2022	'+	str	(p.value(	x2022	)))
filepoint.writelines	('\tx2023	'+	str	(p.value(	x2023	)))
filepoint.writelines	('\tx2024	'+	str	(p.value(	x2024	)))
filepoint.writelines	('\tx2025	'+	str	(p.value(	x2025	)))
filepoint.writelines	('\tx2026	'+	str	(p.value(	x2026	)))
filepoint.writelines	('\tx2027	'+	str	(p.value(	x2027	)))
filepoint.writelines	('\tx2028	'+	str	(p.value(	x2028	)))
filepoint.writelines	('\tx2029	'+	str	(p.value(	x2029	)))
filepoint.writelines	('\tx2030	'+	str	(p.value(	x2030	)))
filepoint.writelines	('\tx2031	'+	str	(p.value(	x2031	)))
filepoint.writelines	('\tx2032	'+	str	(p.value(	x2032	)))
filepoint.writelines	('\tx2033	'+	str	(p.value(	x2033	)))
filepoint.writelines	('\tx2034	'+	str	(p.value(	x2034	)))
filepoint.writelines	('\tx2035	'+	str	(p.value(	x2035	)))
filepoint.writelines	('\tx2036	'+	str	(p.value(	x2036	)))
filepoint.writelines	('\tx2037	'+	str	(p.value(	x2037	)))
filepoint.writelines	('\tx2038	'+	str	(p.value(	x2038	)))
filepoint.writelines	('\tx2039	'+	str	(p.value(	x2039	)))
filepoint.writelines	('\tx2040	'+	str	(p.value(	x2040	)))
filepoint.writelines	('\tx2041	'+	str	(p.value(	x2041	)))
filepoint.writelines	('\tx2042	'+	str	(p.value(	x2042	)))
filepoint.writelines	('\tx2043	'+	str	(p.value(	x2043	)))
filepoint.writelines	('\tx2044	'+	str	(p.value(	x2044	)))
filepoint.writelines	('\tx2045	'+	str	(p.value(	x2045	)))
filepoint.writelines	('\tx2046	'+	str	(p.value(	x2046	)))
filepoint.writelines	('\tx2047	'+	str	(p.value(	x2047	)))
filepoint.writelines	('\tx2048	'+	str	(p.value(	x2048	)))
filepoint.writelines	('\tx2049	'+	str	(p.value(	x2049	)))
filepoint.writelines	('\tx2050	'+	str	(p.value(	x2050	)))
filepoint.writelines	('\tx2051	'+	str	(p.value(	x2051	)))
filepoint.writelines	('\tx2052	'+	str	(p.value(	x2052	)))
filepoint.writelines	('\tx2053	'+	str	(p.value(	x2053	)))
filepoint.writelines	('\tx2054	'+	str	(p.value(	x2054	)))
filepoint.writelines	('\tx2055	'+	str	(p.value(	x2055	)))
filepoint.writelines	('\tx2056	'+	str	(p.value(	x2056	)))
filepoint.writelines	('\tx2057	'+	str	(p.value(	x2057	)))
filepoint.writelines	('\tx2058	'+	str	(p.value(	x2058	)))
filepoint.writelines	('\tx2059	'+	str	(p.value(	x2059	)))
filepoint.writelines	('\tx2060	'+	str	(p.value(	x2060	)))
filepoint.writelines	('\tx2061	'+	str	(p.value(	x2061	)))
filepoint.writelines	('\tx2062	'+	str	(p.value(	x2062	)))
filepoint.writelines	('\tx2063	'+	str	(p.value(	x2063	)))
filepoint.writelines	('\tx2064	'+	str	(p.value(	x2064	)))
filepoint.writelines	('\tx2065	'+	str	(p.value(	x2065	)))
filepoint.writelines	('\tx2066	'+	str	(p.value(	x2066	)))
filepoint.writelines	('\tx2067	'+	str	(p.value(	x2067	)))
filepoint.writelines	('\tx2068	'+	str	(p.value(	x2068	)))
filepoint.writelines	('\tx2069	'+	str	(p.value(	x2069	)))
filepoint.writelines	('\tx2070	'+	str	(p.value(	x2070	)))
filepoint.writelines	('\tx2071	'+	str	(p.value(	x2071	)))
filepoint.writelines	('\tx2072	'+	str	(p.value(	x2072	)))
filepoint.writelines	('\tx2073	'+	str	(p.value(	x2073	)))
filepoint.writelines	('\tx2074	'+	str	(p.value(	x2074	)))
filepoint.writelines	('\tx2075	'+	str	(p.value(	x2075	)))
filepoint.writelines	('\tx2076	'+	str	(p.value(	x2076	)))
filepoint.writelines	('\tx2077	'+	str	(p.value(	x2077	)))
filepoint.writelines	('\tx2078	'+	str	(p.value(	x2078	)))
filepoint.writelines	('\tx2079	'+	str	(p.value(	x2079	)))
filepoint.writelines	('\tx2080	'+	str	(p.value(	x2080	)))
filepoint.writelines	('\tx2081	'+	str	(p.value(	x2081	)))
filepoint.writelines	('\tx2082	'+	str	(p.value(	x2082	)))
filepoint.writelines	('\tx2083	'+	str	(p.value(	x2083	)))
filepoint.writelines	('\tx2084	'+	str	(p.value(	x2084	)))
filepoint.writelines	('\tx2085	'+	str	(p.value(	x2085	)))
filepoint.writelines	('\tx2086	'+	str	(p.value(	x2086	)))
filepoint.writelines	('\tx2087	'+	str	(p.value(	x2087	)))
filepoint.writelines	('\tx2088	'+	str	(p.value(	x2088	)))
filepoint.writelines	('\tx2089	'+	str	(p.value(	x2089	)))
filepoint.writelines	('\tx2090	'+	str	(p.value(	x2090	)))
filepoint.writelines	('\tx2091	'+	str	(p.value(	x2091	)))
filepoint.writelines	('\tx2092	'+	str	(p.value(	x2092	)))
filepoint.writelines	('\tx2093	'+	str	(p.value(	x2093	)))
filepoint.writelines	('\tx2094	'+	str	(p.value(	x2094	)))
filepoint.writelines	('\tx2095	'+	str	(p.value(	x2095	)))
filepoint.writelines	('\tx2096	'+	str	(p.value(	x2096	)))
filepoint.writelines	('\tx2097	'+	str	(p.value(	x2097	)))
filepoint.writelines	('\tx2098	'+	str	(p.value(	x2098	)))
filepoint.writelines	('\tx2099	'+	str	(p.value(	x2099	)))
filepoint.writelines	('\tx2100	'+	str	(p.value(	x2100	)))
filepoint.writelines	('\tx2101	'+	str	(p.value(	x2101	)))
filepoint.writelines	('\tx2102	'+	str	(p.value(	x2102	)))
filepoint.writelines	('\tx2103	'+	str	(p.value(	x2103	)))
filepoint.writelines	('\tx2104	'+	str	(p.value(	x2104	)))
filepoint.writelines	('\tx2105	'+	str	(p.value(	x2105	)))
filepoint.writelines	('\tx2106	'+	str	(p.value(	x2106	)))
filepoint.writelines	('\tx2107	'+	str	(p.value(	x2107	)))
filepoint.writelines	('\tx2108	'+	str	(p.value(	x2108	)))
filepoint.writelines	('\tx2109	'+	str	(p.value(	x2109	)))
filepoint.writelines	('\tx2110	'+	str	(p.value(	x2110	)))
filepoint.writelines	('\tx2111	'+	str	(p.value(	x2111	)))
filepoint.writelines	('\tx2112	'+	str	(p.value(	x2112	)))
filepoint.writelines	('\tx2113	'+	str	(p.value(	x2113	)))
filepoint.writelines	('\tx2114	'+	str	(p.value(	x2114	)))
filepoint.writelines	('\tx2115	'+	str	(p.value(	x2115	)))
filepoint.writelines	('\tx2116	'+	str	(p.value(	x2116	)))
filepoint.writelines	('\tx2117	'+	str	(p.value(	x2117	)))
filepoint.writelines	('\tx2118	'+	str	(p.value(	x2118	)))
filepoint.writelines	('\tx2119	'+	str	(p.value(	x2119	)))
filepoint.writelines	('\tx2120	'+	str	(p.value(	x2120	)))
filepoint.writelines	('\tx2121	'+	str	(p.value(	x2121	)))
filepoint.writelines	('\tx2122	'+	str	(p.value(	x2122	)))
filepoint.writelines	('\tx2123	'+	str	(p.value(	x2123	)))
filepoint.writelines	('\tx2124	'+	str	(p.value(	x2124	)))
filepoint.writelines	('\tx2125	'+	str	(p.value(	x2125	)))
filepoint.writelines	('\tx2126	'+	str	(p.value(	x2126	)))
filepoint.writelines	('\tx2127	'+	str	(p.value(	x2127	)))
filepoint.writelines	('\tx2128	'+	str	(p.value(	x2128	)))
filepoint.writelines	('\tx2129	'+	str	(p.value(	x2129	)))
filepoint.writelines	('\tx2130	'+	str	(p.value(	x2130	)))
filepoint.writelines	('\tx2131	'+	str	(p.value(	x2131	)))
filepoint.writelines	('\tx2132	'+	str	(p.value(	x2132	)))
filepoint.writelines	('\tx2133	'+	str	(p.value(	x2133	)))
filepoint.writelines	('\tx2134	'+	str	(p.value(	x2134	)))
filepoint.writelines	('\tx2135	'+	str	(p.value(	x2135	)))
filepoint.writelines	('\tx2136	'+	str	(p.value(	x2136	)))
filepoint.writelines	('\tx2137	'+	str	(p.value(	x2137	)))
filepoint.writelines	('\tx2138	'+	str	(p.value(	x2138	)))
filepoint.writelines	('\tx2139	'+	str	(p.value(	x2139	)))
filepoint.writelines	('\tx2140	'+	str	(p.value(	x2140	)))
filepoint.writelines	('\tx2141	'+	str	(p.value(	x2141	)))
filepoint.writelines	('\tx2142	'+	str	(p.value(	x2142	)))
filepoint.writelines	('\tx2143	'+	str	(p.value(	x2143	)))
filepoint.writelines	('\tx2144	'+	str	(p.value(	x2144	)))
filepoint.writelines	('\tx2145	'+	str	(p.value(	x2145	)))
filepoint.writelines	('\tx2146	'+	str	(p.value(	x2146	)))
filepoint.writelines	('\tx2147	'+	str	(p.value(	x2147	)))
filepoint.writelines	('\tx2148	'+	str	(p.value(	x2148	)))
filepoint.writelines	('\tx2149	'+	str	(p.value(	x2149	)))
filepoint.writelines	('\tx2150	'+	str	(p.value(	x2150	)))
filepoint.writelines	('\tx2151	'+	str	(p.value(	x2151	)))
filepoint.writelines	('\tx2152	'+	str	(p.value(	x2152	)))
filepoint.writelines	('\tx2153	'+	str	(p.value(	x2153	)))
filepoint.writelines	('\tx2154	'+	str	(p.value(	x2154	)))
filepoint.writelines	('\tx2155	'+	str	(p.value(	x2155	)))
filepoint.writelines	('\tx2156	'+	str	(p.value(	x2156	)))
filepoint.writelines	('\tx2157	'+	str	(p.value(	x2157	)))
filepoint.writelines	('\tx2158	'+	str	(p.value(	x2158	)))
filepoint.writelines	('\tx2159	'+	str	(p.value(	x2159	)))
filepoint.writelines	('\tx2160	'+	str	(p.value(	x2160	)))
filepoint.writelines	('\tx2161	'+	str	(p.value(	x2161	)))
filepoint.writelines	('\tx2162	'+	str	(p.value(	x2162	)))
filepoint.writelines	('\tx2163	'+	str	(p.value(	x2163	)))
filepoint.writelines	('\tx2164	'+	str	(p.value(	x2164	)))
filepoint.writelines	('\tx2165	'+	str	(p.value(	x2165	)))
filepoint.writelines	('\tx2166	'+	str	(p.value(	x2166	)))
filepoint.writelines	('\tx2167	'+	str	(p.value(	x2167	)))
filepoint.writelines	('\tx2168	'+	str	(p.value(	x2168	)))
filepoint.writelines	('\tx2169	'+	str	(p.value(	x2169	)))
filepoint.writelines	('\tx2170	'+	str	(p.value(	x2170	)))
filepoint.writelines	('\tx2171	'+	str	(p.value(	x2171	)))
filepoint.writelines	('\tx2172	'+	str	(p.value(	x2172	)))
filepoint.writelines	('\tx2173	'+	str	(p.value(	x2173	)))
filepoint.writelines	('\tx2174	'+	str	(p.value(	x2174	)))
filepoint.writelines	('\tx2175	'+	str	(p.value(	x2175	)))
filepoint.writelines	('\tx2176	'+	str	(p.value(	x2176	)))
filepoint.writelines	('\tx2177	'+	str	(p.value(	x2177	)))
filepoint.writelines	('\tx2178	'+	str	(p.value(	x2178	)))
filepoint.writelines	('\tx2179	'+	str	(p.value(	x2179	)))
filepoint.writelines	('\tx2180	'+	str	(p.value(	x2180	)))
filepoint.writelines	('\tx2181	'+	str	(p.value(	x2181	)))
filepoint.writelines	('\tx2182	'+	str	(p.value(	x2182	)))
filepoint.writelines	('\tx2183	'+	str	(p.value(	x2183	)))
filepoint.writelines	('\tx2184	'+	str	(p.value(	x2184	)))
filepoint.writelines	('\tx2185	'+	str	(p.value(	x2185	)))
filepoint.writelines	('\tx2186	'+	str	(p.value(	x2186	)))
filepoint.writelines	('\tx2187	'+	str	(p.value(	x2187	)))
filepoint.writelines	('\tx2188	'+	str	(p.value(	x2188	)))
filepoint.writelines	('\tx2189	'+	str	(p.value(	x2189	)))
filepoint.writelines	('\tx2190	'+	str	(p.value(	x2190	)))
filepoint.writelines	('\tx2191	'+	str	(p.value(	x2191	)))
filepoint.writelines	('\tx2192	'+	str	(p.value(	x2192	)))
filepoint.writelines	('\tx2193	'+	str	(p.value(	x2193	)))
filepoint.writelines	('\tx2194	'+	str	(p.value(	x2194	)))
filepoint.writelines	('\tx2195	'+	str	(p.value(	x2195	)))
filepoint.writelines	('\tx2196	'+	str	(p.value(	x2196	)))
filepoint.writelines	('\tx2197	'+	str	(p.value(	x2197	)))
filepoint.writelines	('\tx2198	'+	str	(p.value(	x2198	)))
filepoint.writelines	('\tx2199	'+	str	(p.value(	x2199	)))
filepoint.writelines	('\tx2200	'+	str	(p.value(	x2200	)))
filepoint.writelines	('\tx2201	'+	str	(p.value(	x2201	)))
filepoint.writelines	('\tx2202	'+	str	(p.value(	x2202	)))
filepoint.writelines	('\tx2203	'+	str	(p.value(	x2203	)))
filepoint.writelines	('\tx2204	'+	str	(p.value(	x2204	)))
filepoint.writelines	('\tx2205	'+	str	(p.value(	x2205	)))
filepoint.writelines	('\tx2206	'+	str	(p.value(	x2206	)))
filepoint.writelines	('\tx2207	'+	str	(p.value(	x2207	)))
filepoint.writelines	('\tx2208	'+	str	(p.value(	x2208	)))
filepoint.writelines	('\tx2209	'+	str	(p.value(	x2209	)))
filepoint.writelines	('\tx2210	'+	str	(p.value(	x2210	)))
filepoint.writelines	('\tx2211	'+	str	(p.value(	x2211	)))
filepoint.writelines	('\tx2212	'+	str	(p.value(	x2212	)))
filepoint.writelines	('\tx2213	'+	str	(p.value(	x2213	)))
filepoint.writelines	('\tx2214	'+	str	(p.value(	x2214	)))
filepoint.writelines	('\tx2215	'+	str	(p.value(	x2215	)))
filepoint.writelines	('\tx2216	'+	str	(p.value(	x2216	)))
filepoint.writelines	('\tx2217	'+	str	(p.value(	x2217	)))
filepoint.writelines	('\tx2218	'+	str	(p.value(	x2218	)))
filepoint.writelines	('\tx2219	'+	str	(p.value(	x2219	)))
filepoint.writelines	('\tx2220	'+	str	(p.value(	x2220	)))
filepoint.writelines	('\tx2221	'+	str	(p.value(	x2221	)))
filepoint.writelines	('\tx2222	'+	str	(p.value(	x2222	)))
filepoint.writelines	('\tx2223	'+	str	(p.value(	x2223	)))
filepoint.writelines	('\tx2224	'+	str	(p.value(	x2224	)))
filepoint.writelines	('\tx2225	'+	str	(p.value(	x2225	)))
filepoint.writelines	('\tx2226	'+	str	(p.value(	x2226	)))
filepoint.writelines	('\tx2227	'+	str	(p.value(	x2227	)))
filepoint.writelines	('\tx2228	'+	str	(p.value(	x2228	)))
filepoint.writelines	('\tx2229	'+	str	(p.value(	x2229	)))
filepoint.writelines	('\tx2230	'+	str	(p.value(	x2230	)))
filepoint.writelines	('\tx2231	'+	str	(p.value(	x2231	)))
filepoint.writelines	('\tx2232	'+	str	(p.value(	x2232	)))
filepoint.writelines	('\tx2233	'+	str	(p.value(	x2233	)))
filepoint.writelines	('\tx2234	'+	str	(p.value(	x2234	)))
filepoint.writelines	('\tx2235	'+	str	(p.value(	x2235	)))
filepoint.writelines	('\tx2236	'+	str	(p.value(	x2236	)))
filepoint.writelines	('\tx2237	'+	str	(p.value(	x2237	)))
filepoint.writelines	('\tx2238	'+	str	(p.value(	x2238	)))
filepoint.writelines	('\tx2239	'+	str	(p.value(	x2239	)))
filepoint.writelines	('\tx2240	'+	str	(p.value(	x2240	)))
filepoint.writelines	('\tx2241	'+	str	(p.value(	x2241	)))
filepoint.writelines	('\tx2242	'+	str	(p.value(	x2242	)))
filepoint.writelines	('\tx2243	'+	str	(p.value(	x2243	)))
filepoint.writelines	('\tx2244	'+	str	(p.value(	x2244	)))
filepoint.writelines	('\tx2245	'+	str	(p.value(	x2245	)))
filepoint.writelines	('\tx2246	'+	str	(p.value(	x2246	)))
filepoint.writelines	('\tx2247	'+	str	(p.value(	x2247	)))
filepoint.writelines	('\tx2248	'+	str	(p.value(	x2248	)))
filepoint.writelines	('\tx2249	'+	str	(p.value(	x2249	)))
filepoint.writelines	('\tx2250	'+	str	(p.value(	x2250	)))
filepoint.writelines	('\tx2251	'+	str	(p.value(	x2251	)))
filepoint.writelines	('\tx2252	'+	str	(p.value(	x2252	)))
filepoint.writelines	('\tx2253	'+	str	(p.value(	x2253	)))
filepoint.writelines	('\tx2254	'+	str	(p.value(	x2254	)))
filepoint.writelines	('\tx2255	'+	str	(p.value(	x2255	)))
filepoint.writelines	('\tx2256	'+	str	(p.value(	x2256	)))
filepoint.writelines	('\tx2257	'+	str	(p.value(	x2257	)))
filepoint.writelines	('\tx2258	'+	str	(p.value(	x2258	)))
filepoint.writelines	('\tx2259	'+	str	(p.value(	x2259	)))
filepoint.writelines	('\tx2260	'+	str	(p.value(	x2260	)))
filepoint.writelines	('\tx2261	'+	str	(p.value(	x2261	)))
filepoint.writelines	('\tx2262	'+	str	(p.value(	x2262	)))
filepoint.writelines	('\tx2263	'+	str	(p.value(	x2263	)))
filepoint.writelines	('\tx2264	'+	str	(p.value(	x2264	)))
filepoint.writelines	('\tx2265	'+	str	(p.value(	x2265	)))
filepoint.writelines	('\tx2266	'+	str	(p.value(	x2266	)))
filepoint.writelines	('\tx2267	'+	str	(p.value(	x2267	)))
filepoint.writelines	('\tx2268	'+	str	(p.value(	x2268	)))
filepoint.writelines	('\tx2269	'+	str	(p.value(	x2269	)))
filepoint.writelines	('\tx2270	'+	str	(p.value(	x2270	)))
filepoint.writelines	('\tx2271	'+	str	(p.value(	x2271	)))
filepoint.writelines	('\tx2272	'+	str	(p.value(	x2272	)))
filepoint.writelines	('\tx2273	'+	str	(p.value(	x2273	)))
filepoint.writelines	('\tx2274	'+	str	(p.value(	x2274	)))
filepoint.writelines	('\tx2275	'+	str	(p.value(	x2275	)))
filepoint.writelines	('\tx2276	'+	str	(p.value(	x2276	)))
filepoint.writelines	('\tx2277	'+	str	(p.value(	x2277	)))
filepoint.writelines	('\tx2278	'+	str	(p.value(	x2278	)))
filepoint.writelines	('\tx2279	'+	str	(p.value(	x2279	)))
filepoint.writelines	('\tx2280	'+	str	(p.value(	x2280	)))
filepoint.writelines	('\tx2281	'+	str	(p.value(	x2281	)))
filepoint.writelines	('\tx2282	'+	str	(p.value(	x2282	)))
filepoint.writelines	('\tx2283	'+	str	(p.value(	x2283	)))
filepoint.writelines	('\tx2284	'+	str	(p.value(	x2284	)))
filepoint.writelines	('\tx2285	'+	str	(p.value(	x2285	)))
filepoint.writelines	('\tx2286	'+	str	(p.value(	x2286	)))
filepoint.writelines	('\tx2287	'+	str	(p.value(	x2287	)))
filepoint.writelines	('\tx2288	'+	str	(p.value(	x2288	)))
filepoint.writelines	('\tx2289	'+	str	(p.value(	x2289	)))
filepoint.writelines	('\tx2290	'+	str	(p.value(	x2290	)))
filepoint.writelines	('\tx2291	'+	str	(p.value(	x2291	)))
filepoint.writelines	('\tx2292	'+	str	(p.value(	x2292	)))
filepoint.writelines	('\tx2293	'+	str	(p.value(	x2293	)))
filepoint.writelines	('\tx2294	'+	str	(p.value(	x2294	)))
filepoint.writelines	('\tx2295	'+	str	(p.value(	x2295	)))
filepoint.writelines	('\tx2296	'+	str	(p.value(	x2296	)))
filepoint.writelines	('\tx2297	'+	str	(p.value(	x2297	)))
filepoint.writelines	('\tx2298	'+	str	(p.value(	x2298	)))
filepoint.writelines	('\tx2299	'+	str	(p.value(	x2299	)))
filepoint.writelines	('\tx2300	'+	str	(p.value(	x2300	)))
filepoint.writelines	('\tx2301	'+	str	(p.value(	x2301	)))
filepoint.writelines	('\tx2302	'+	str	(p.value(	x2302	)))
filepoint.writelines	('\tx2303	'+	str	(p.value(	x2303	)))
filepoint.writelines	('\tx2304	'+	str	(p.value(	x2304	)))
filepoint.writelines	('\tx2305	'+	str	(p.value(	x2305	)))
filepoint.writelines	('\tx2306	'+	str	(p.value(	x2306	)))
filepoint.writelines	('\tx2307	'+	str	(p.value(	x2307	)))
filepoint.writelines	('\tx2308	'+	str	(p.value(	x2308	)))
filepoint.writelines	('\tx2309	'+	str	(p.value(	x2309	)))
filepoint.writelines	('\tx2310	'+	str	(p.value(	x2310	)))
filepoint.writelines	('\tx2311	'+	str	(p.value(	x2311	)))
filepoint.writelines	('\tx2312	'+	str	(p.value(	x2312	)))
filepoint.writelines	('\tx2313	'+	str	(p.value(	x2313	)))
filepoint.writelines	('\tx2314	'+	str	(p.value(	x2314	)))
filepoint.writelines	('\tx2315	'+	str	(p.value(	x2315	)))
filepoint.writelines	('\tx2316	'+	str	(p.value(	x2316	)))
filepoint.writelines	('\tx2317	'+	str	(p.value(	x2317	)))
filepoint.writelines	('\tx2318	'+	str	(p.value(	x2318	)))
filepoint.writelines	('\tx2319	'+	str	(p.value(	x2319	)))
filepoint.writelines	('\tx2320	'+	str	(p.value(	x2320	)))
filepoint.writelines	('\tx2321	'+	str	(p.value(	x2321	)))
filepoint.writelines	('\tx2322	'+	str	(p.value(	x2322	)))
filepoint.writelines	('\tx2323	'+	str	(p.value(	x2323	)))
filepoint.writelines	('\tx2324	'+	str	(p.value(	x2324	)))
filepoint.writelines	('\tx2325	'+	str	(p.value(	x2325	)))
filepoint.writelines	('\tx2326	'+	str	(p.value(	x2326	)))
filepoint.writelines	('\tx2327	'+	str	(p.value(	x2327	)))
filepoint.writelines	('\tx2328	'+	str	(p.value(	x2328	)))
filepoint.writelines	('\tx2329	'+	str	(p.value(	x2329	)))
filepoint.writelines	('\tx2330	'+	str	(p.value(	x2330	)))
filepoint.writelines	('\tx2331	'+	str	(p.value(	x2331	)))
filepoint.writelines	('\tx2332	'+	str	(p.value(	x2332	)))
filepoint.writelines	('\tx2333	'+	str	(p.value(	x2333	)))
filepoint.writelines	('\tx2334	'+	str	(p.value(	x2334	)))
filepoint.writelines	('\tx2335	'+	str	(p.value(	x2335	)))
filepoint.writelines	('\tx2336	'+	str	(p.value(	x2336	)))
filepoint.writelines	('\tx2337	'+	str	(p.value(	x2337	)))
filepoint.writelines	('\tx2338	'+	str	(p.value(	x2338	)))
filepoint.writelines	('\tx2339	'+	str	(p.value(	x2339	)))
filepoint.writelines	('\tx2340	'+	str	(p.value(	x2340	)))
filepoint.writelines	('\tx2341	'+	str	(p.value(	x2341	)))
filepoint.writelines	('\tx2342	'+	str	(p.value(	x2342	)))
filepoint.writelines	('\tx2343	'+	str	(p.value(	x2343	)))
filepoint.writelines	('\tx2344	'+	str	(p.value(	x2344	)))
filepoint.writelines	('\tx2345	'+	str	(p.value(	x2345	)))
filepoint.writelines	('\tx2346	'+	str	(p.value(	x2346	)))
filepoint.writelines	('\tx2347	'+	str	(p.value(	x2347	)))
filepoint.writelines	('\tx2348	'+	str	(p.value(	x2348	)))
filepoint.writelines	('\tx2349	'+	str	(p.value(	x2349	)))
filepoint.writelines	('\tx2350	'+	str	(p.value(	x2350	)))
filepoint.writelines	('\tx2351	'+	str	(p.value(	x2351	)))
filepoint.writelines	('\tx2352	'+	str	(p.value(	x2352	)))
filepoint.writelines	('\tx2353	'+	str	(p.value(	x2353	)))
filepoint.writelines	('\tx2354	'+	str	(p.value(	x2354	)))
filepoint.writelines	('\tx2355	'+	str	(p.value(	x2355	)))
filepoint.writelines	('\tx2356	'+	str	(p.value(	x2356	)))
filepoint.writelines	('\tx2357	'+	str	(p.value(	x2357	)))
filepoint.writelines	('\tx2358	'+	str	(p.value(	x2358	)))
filepoint.writelines	('\tx2359	'+	str	(p.value(	x2359	)))
filepoint.writelines	('\tx2360	'+	str	(p.value(	x2360	)))
filepoint.writelines	('\tx2361	'+	str	(p.value(	x2361	)))
filepoint.writelines	('\tx2362	'+	str	(p.value(	x2362	)))
filepoint.writelines	('\tx2363	'+	str	(p.value(	x2363	)))
filepoint.writelines	('\tx2364	'+	str	(p.value(	x2364	)))
filepoint.writelines	('\tx2365	'+	str	(p.value(	x2365	)))
filepoint.writelines	('\tx2366	'+	str	(p.value(	x2366	)))
filepoint.writelines	('\tx2367	'+	str	(p.value(	x2367	)))
filepoint.writelines	('\tx2368	'+	str	(p.value(	x2368	)))
filepoint.writelines	('\tx2369	'+	str	(p.value(	x2369	)))
filepoint.writelines	('\tx2370	'+	str	(p.value(	x2370	)))
filepoint.writelines	('\tx2371	'+	str	(p.value(	x2371	)))
filepoint.writelines	('\tx2372	'+	str	(p.value(	x2372	)))
filepoint.writelines	('\tx2373	'+	str	(p.value(	x2373	)))
filepoint.writelines	('\tx2374	'+	str	(p.value(	x2374	)))
filepoint.writelines	('\tx2375	'+	str	(p.value(	x2375	)))
filepoint.writelines	('\tx2376	'+	str	(p.value(	x2376	)))
filepoint.writelines	('\tx2377	'+	str	(p.value(	x2377	)))
filepoint.writelines	('\tx2378	'+	str	(p.value(	x2378	)))
filepoint.writelines	('\tx2379	'+	str	(p.value(	x2379	)))
filepoint.writelines	('\tx2380	'+	str	(p.value(	x2380	)))
filepoint.writelines	('\tx2381	'+	str	(p.value(	x2381	)))
filepoint.writelines	('\tx2382	'+	str	(p.value(	x2382	)))
filepoint.writelines	('\tx2383	'+	str	(p.value(	x2383	)))
filepoint.writelines	('\tx2384	'+	str	(p.value(	x2384	)))
filepoint.writelines	('\tx2385	'+	str	(p.value(	x2385	)))
filepoint.writelines	('\tx2386	'+	str	(p.value(	x2386	)))
filepoint.writelines	('\tx2387	'+	str	(p.value(	x2387	)))
filepoint.writelines	('\tx2388	'+	str	(p.value(	x2388	)))
filepoint.writelines	('\tx2389	'+	str	(p.value(	x2389	)))
filepoint.writelines	('\tx2390	'+	str	(p.value(	x2390	)))
filepoint.writelines	('\tx2391	'+	str	(p.value(	x2391	)))
filepoint.writelines	('\tx2392	'+	str	(p.value(	x2392	)))
filepoint.writelines	('\tx2393	'+	str	(p.value(	x2393	)))
filepoint.writelines	('\tx2394	'+	str	(p.value(	x2394	)))
filepoint.writelines	('\tx2395	'+	str	(p.value(	x2395	)))
filepoint.writelines	('\tx2396	'+	str	(p.value(	x2396	)))
filepoint.writelines	('\tx2397	'+	str	(p.value(	x2397	)))
filepoint.writelines	('\tx2398	'+	str	(p.value(	x2398	)))
filepoint.writelines	('\tx2399	'+	str	(p.value(	x2399	)))
filepoint.writelines	('\tx2400	'+	str	(p.value(	x2400	)))
filepoint.writelines	('\tx2401	'+	str	(p.value(	x2401	)))
filepoint.writelines	('\tx2402	'+	str	(p.value(	x2402	)))
filepoint.writelines	('\tx2403	'+	str	(p.value(	x2403	)))
filepoint.writelines	('\tx2404	'+	str	(p.value(	x2404	)))
filepoint.writelines	('\tx2405	'+	str	(p.value(	x2405	)))
filepoint.writelines	('\tx2406	'+	str	(p.value(	x2406	)))
filepoint.writelines	('\tx2407	'+	str	(p.value(	x2407	)))
filepoint.writelines	('\tx2408	'+	str	(p.value(	x2408	)))
filepoint.writelines	('\tx2409	'+	str	(p.value(	x2409	)))
filepoint.writelines	('\tx2410	'+	str	(p.value(	x2410	)))
filepoint.writelines	('\tx2411	'+	str	(p.value(	x2411	)))
filepoint.writelines	('\tx2412	'+	str	(p.value(	x2412	)))
filepoint.writelines	('\tx2413	'+	str	(p.value(	x2413	)))
filepoint.writelines	('\tx2414	'+	str	(p.value(	x2414	)))
filepoint.writelines	('\tx2415	'+	str	(p.value(	x2415	)))
filepoint.writelines	('\tx2416	'+	str	(p.value(	x2416	)))
filepoint.writelines	('\tx2417	'+	str	(p.value(	x2417	)))
filepoint.writelines	('\tx2418	'+	str	(p.value(	x2418	)))
filepoint.writelines	('\tx2419	'+	str	(p.value(	x2419	)))
filepoint.writelines	('\tx2420	'+	str	(p.value(	x2420	)))
filepoint.writelines	('\tx2421	'+	str	(p.value(	x2421	)))
filepoint.writelines	('\tx2422	'+	str	(p.value(	x2422	)))
filepoint.writelines	('\tx2423	'+	str	(p.value(	x2423	)))
filepoint.writelines	('\tx2424	'+	str	(p.value(	x2424	)))
filepoint.writelines	('\tx2425	'+	str	(p.value(	x2425	)))
filepoint.writelines	('\tx2426	'+	str	(p.value(	x2426	)))
filepoint.writelines	('\tx2427	'+	str	(p.value(	x2427	)))
filepoint.writelines	('\tx2428	'+	str	(p.value(	x2428	)))
filepoint.writelines	('\tx2429	'+	str	(p.value(	x2429	)))
filepoint.writelines	('\tx2430	'+	str	(p.value(	x2430	)))
filepoint.writelines	('\tx2431	'+	str	(p.value(	x2431	)))
filepoint.writelines	('\tx2432	'+	str	(p.value(	x2432	)))
filepoint.writelines	('\tx2433	'+	str	(p.value(	x2433	)))
filepoint.writelines	('\tx2434	'+	str	(p.value(	x2434	)))
filepoint.writelines	('\tx2435	'+	str	(p.value(	x2435	)))
filepoint.writelines	('\tx2436	'+	str	(p.value(	x2436	)))
filepoint.writelines	('\tx2437	'+	str	(p.value(	x2437	)))
filepoint.writelines	('\tx2438	'+	str	(p.value(	x2438	)))
filepoint.writelines	('\tx2439	'+	str	(p.value(	x2439	)))
filepoint.writelines	('\tx2440	'+	str	(p.value(	x2440	)))
filepoint.writelines	('\tx2441	'+	str	(p.value(	x2441	)))
filepoint.writelines	('\tx2442	'+	str	(p.value(	x2442	)))
filepoint.writelines	('\tx2443	'+	str	(p.value(	x2443	)))
filepoint.writelines	('\tx2444	'+	str	(p.value(	x2444	)))
filepoint.writelines	('\tx2445	'+	str	(p.value(	x2445	)))
filepoint.writelines	('\tx2446	'+	str	(p.value(	x2446	)))
filepoint.writelines	('\tx2447	'+	str	(p.value(	x2447	)))
filepoint.writelines	('\tx2448	'+	str	(p.value(	x2448	)))
filepoint.writelines	('\tx2449	'+	str	(p.value(	x2449	)))
filepoint.writelines	('\tx2450	'+	str	(p.value(	x2450	)))
filepoint.writelines	('\tx2451	'+	str	(p.value(	x2451	)))
filepoint.writelines	('\tx2452	'+	str	(p.value(	x2452	)))
filepoint.writelines	('\tx2453	'+	str	(p.value(	x2453	)))
filepoint.writelines	('\tx2454	'+	str	(p.value(	x2454	)))
filepoint.writelines	('\tx2455	'+	str	(p.value(	x2455	)))
filepoint.writelines	('\tx2456	'+	str	(p.value(	x2456	)))
filepoint.writelines	('\tx2457	'+	str	(p.value(	x2457	)))
filepoint.writelines	('\tx2458	'+	str	(p.value(	x2458	)))
filepoint.writelines	('\tx2459	'+	str	(p.value(	x2459	)))
filepoint.writelines	('\tx2460	'+	str	(p.value(	x2460	)))
filepoint.writelines	('\tx2461	'+	str	(p.value(	x2461	)))
filepoint.writelines	('\tx2462	'+	str	(p.value(	x2462	)))
filepoint.writelines	('\tx2463	'+	str	(p.value(	x2463	)))
filepoint.writelines	('\tx2464	'+	str	(p.value(	x2464	)))
filepoint.writelines	('\tx2465	'+	str	(p.value(	x2465	)))
filepoint.writelines	('\tx2466	'+	str	(p.value(	x2466	)))
filepoint.writelines	('\tx2467	'+	str	(p.value(	x2467	)))
filepoint.writelines	('\tx2468	'+	str	(p.value(	x2468	)))
filepoint.writelines	('\tx2469	'+	str	(p.value(	x2469	)))
filepoint.writelines	('\tx2470	'+	str	(p.value(	x2470	)))
filepoint.writelines	('\tx2471	'+	str	(p.value(	x2471	)))
filepoint.writelines	('\tx2472	'+	str	(p.value(	x2472	)))
filepoint.writelines	('\tx2473	'+	str	(p.value(	x2473	)))
filepoint.writelines	('\tx2474	'+	str	(p.value(	x2474	)))
filepoint.writelines	('\tx2475	'+	str	(p.value(	x2475	)))
filepoint.writelines	('\tx2476	'+	str	(p.value(	x2476	)))
filepoint.writelines	('\tx2477	'+	str	(p.value(	x2477	)))
filepoint.writelines	('\tx2478	'+	str	(p.value(	x2478	)))
filepoint.writelines	('\tx2479	'+	str	(p.value(	x2479	)))
filepoint.writelines	('\tx2480	'+	str	(p.value(	x2480	)))
filepoint.writelines	('\tx2481	'+	str	(p.value(	x2481	)))
filepoint.writelines	('\tx2482	'+	str	(p.value(	x2482	)))
filepoint.writelines	('\tx2483	'+	str	(p.value(	x2483	)))
filepoint.writelines	('\tx2484	'+	str	(p.value(	x2484	)))
filepoint.writelines	('\tx2485	'+	str	(p.value(	x2485	)))
filepoint.writelines	('\tx2486	'+	str	(p.value(	x2486	)))
filepoint.writelines	('\tx2487	'+	str	(p.value(	x2487	)))
filepoint.writelines	('\tx2488	'+	str	(p.value(	x2488	)))
filepoint.writelines	('\tx2489	'+	str	(p.value(	x2489	)))
filepoint.writelines	('\tx2490	'+	str	(p.value(	x2490	)))
filepoint.writelines	('\tx2491	'+	str	(p.value(	x2491	)))
filepoint.writelines	('\tx2492	'+	str	(p.value(	x2492	)))
filepoint.writelines	('\tx2493	'+	str	(p.value(	x2493	)))
filepoint.writelines	('\tx2494	'+	str	(p.value(	x2494	)))
filepoint.writelines	('\tx2495	'+	str	(p.value(	x2495	)))
filepoint.writelines	('\tx2496	'+	str	(p.value(	x2496	)))
filepoint.writelines	('\tx2497	'+	str	(p.value(	x2497	)))
filepoint.writelines	('\tx2498	'+	str	(p.value(	x2498	)))
filepoint.writelines	('\tx2499	'+	str	(p.value(	x2499	)))
filepoint.writelines	('\tx2500	'+	str	(p.value(	x2500	)))
filepoint.writelines	('\tx2501	'+	str	(p.value(	x2501	)))
filepoint.writelines	('\tx2502	'+	str	(p.value(	x2502	)))
filepoint.writelines	('\tx2503	'+	str	(p.value(	x2503	)))
filepoint.writelines	('\tx2504	'+	str	(p.value(	x2504	)))
filepoint.writelines	('\tx2505	'+	str	(p.value(	x2505	)))
filepoint.writelines	('\tx2506	'+	str	(p.value(	x2506	)))
filepoint.writelines	('\tx2507	'+	str	(p.value(	x2507	)))
filepoint.writelines	('\tx2508	'+	str	(p.value(	x2508	)))
filepoint.writelines	('\tx2509	'+	str	(p.value(	x2509	)))
filepoint.writelines	('\tx2510	'+	str	(p.value(	x2510	)))
filepoint.writelines	('\tx2511	'+	str	(p.value(	x2511	)))
filepoint.writelines	('\tx2512	'+	str	(p.value(	x2512	)))
filepoint.writelines	('\tx2513	'+	str	(p.value(	x2513	)))
filepoint.writelines	('\tx2514	'+	str	(p.value(	x2514	)))
filepoint.writelines	('\tx2515	'+	str	(p.value(	x2515	)))
filepoint.writelines	('\tx2516	'+	str	(p.value(	x2516	)))
filepoint.writelines	('\tx2517	'+	str	(p.value(	x2517	)))
filepoint.writelines	('\tx2518	'+	str	(p.value(	x2518	)))
filepoint.writelines	('\tx2519	'+	str	(p.value(	x2519	)))
filepoint.writelines	('\tx2520	'+	str	(p.value(	x2520	)))
filepoint.writelines	('\tx2521	'+	str	(p.value(	x2521	)))
filepoint.writelines	('\tx2522	'+	str	(p.value(	x2522	)))
filepoint.writelines	('\tx2523	'+	str	(p.value(	x2523	)))
filepoint.writelines	('\tx2524	'+	str	(p.value(	x2524	)))
filepoint.writelines	('\tx2525	'+	str	(p.value(	x2525	)))
filepoint.writelines	('\tx2526	'+	str	(p.value(	x2526	)))
filepoint.writelines	('\tx2527	'+	str	(p.value(	x2527	)))
filepoint.writelines	('\tx2528	'+	str	(p.value(	x2528	)))
filepoint.writelines	('\tx2529	'+	str	(p.value(	x2529	)))
filepoint.writelines	('\tx2530	'+	str	(p.value(	x2530	)))
filepoint.writelines	('\tx2531	'+	str	(p.value(	x2531	)))
filepoint.writelines	('\tx2532	'+	str	(p.value(	x2532	)))
filepoint.writelines	('\tx2533	'+	str	(p.value(	x2533	)))
filepoint.writelines	('\tx2534	'+	str	(p.value(	x2534	)))
filepoint.writelines	('\tx2535	'+	str	(p.value(	x2535	)))
filepoint.writelines	('\tx2536	'+	str	(p.value(	x2536	)))
filepoint.writelines	('\tx2537	'+	str	(p.value(	x2537	)))
filepoint.writelines	('\tx2538	'+	str	(p.value(	x2538	)))
filepoint.writelines	('\tx2539	'+	str	(p.value(	x2539	)))
filepoint.writelines	('\tx2540	'+	str	(p.value(	x2540	)))
filepoint.writelines	('\tx2541	'+	str	(p.value(	x2541	)))
filepoint.writelines	('\tx2542	'+	str	(p.value(	x2542	)))
filepoint.writelines	('\tx2543	'+	str	(p.value(	x2543	)))
filepoint.writelines	('\tx2544	'+	str	(p.value(	x2544	)))
filepoint.writelines	('\tx2545	'+	str	(p.value(	x2545	)))
filepoint.writelines	('\tx2546	'+	str	(p.value(	x2546	)))
filepoint.writelines	('\tx2547	'+	str	(p.value(	x2547	)))
filepoint.writelines	('\tx2548	'+	str	(p.value(	x2548	)))
filepoint.writelines	('\tx2549	'+	str	(p.value(	x2549	)))
filepoint.writelines	('\tx2550	'+	str	(p.value(	x2550	)))
filepoint.writelines	('\tx2551	'+	str	(p.value(	x2551	)))
filepoint.writelines	('\tx2552	'+	str	(p.value(	x2552	)))
filepoint.writelines	('\tx2553	'+	str	(p.value(	x2553	)))
filepoint.writelines	('\tx2554	'+	str	(p.value(	x2554	)))
filepoint.writelines	('\tx2555	'+	str	(p.value(	x2555	)))
filepoint.writelines	('\tx2556	'+	str	(p.value(	x2556	)))
filepoint.writelines	('\tx2557	'+	str	(p.value(	x2557	)))
filepoint.writelines	('\tx2558	'+	str	(p.value(	x2558	)))
filepoint.writelines	('\tx2559	'+	str	(p.value(	x2559	)))
filepoint.writelines	('\tx2560	'+	str	(p.value(	x2560	)))
filepoint.writelines	('\tx2561	'+	str	(p.value(	x2561	)))
filepoint.writelines	('\tx2562	'+	str	(p.value(	x2562	)))
filepoint.writelines	('\tx2563	'+	str	(p.value(	x2563	)))
filepoint.writelines	('\tx2564	'+	str	(p.value(	x2564	)))
filepoint.writelines	('\tx2565	'+	str	(p.value(	x2565	)))
filepoint.writelines	('\tx2566	'+	str	(p.value(	x2566	)))
filepoint.writelines	('\tx2567	'+	str	(p.value(	x2567	)))
filepoint.writelines	('\tx2568	'+	str	(p.value(	x2568	)))
filepoint.writelines	('\tx2569	'+	str	(p.value(	x2569	)))
filepoint.writelines	('\tx2570	'+	str	(p.value(	x2570	)))
filepoint.writelines	('\tx2571	'+	str	(p.value(	x2571	)))
filepoint.writelines	('\tx2572	'+	str	(p.value(	x2572	)))
filepoint.writelines	('\tx2573	'+	str	(p.value(	x2573	)))
filepoint.writelines	('\tx2574	'+	str	(p.value(	x2574	)))
filepoint.writelines	('\tx2575	'+	str	(p.value(	x2575	)))
filepoint.writelines	('\tx2576	'+	str	(p.value(	x2576	)))
filepoint.writelines	('\tx2577	'+	str	(p.value(	x2577	)))
filepoint.writelines	('\tx2578	'+	str	(p.value(	x2578	)))
filepoint.writelines	('\tx2579	'+	str	(p.value(	x2579	)))
filepoint.writelines	('\tx2580	'+	str	(p.value(	x2580	)))
filepoint.writelines	('\tx2581	'+	str	(p.value(	x2581	)))
filepoint.writelines	('\tx2582	'+	str	(p.value(	x2582	)))
filepoint.writelines	('\tx2583	'+	str	(p.value(	x2583	)))
filepoint.writelines	('\tx2584	'+	str	(p.value(	x2584	)))
filepoint.writelines	('\tx2585	'+	str	(p.value(	x2585	)))
filepoint.writelines	('\tx2586	'+	str	(p.value(	x2586	)))
filepoint.writelines	('\tx2587	'+	str	(p.value(	x2587	)))
filepoint.writelines	('\tx2588	'+	str	(p.value(	x2588	)))
filepoint.writelines	('\tx2589	'+	str	(p.value(	x2589	)))
filepoint.writelines	('\tx2590	'+	str	(p.value(	x2590	)))
filepoint.writelines	('\tx2591	'+	str	(p.value(	x2591	)))
filepoint.writelines	('\tx2592	'+	str	(p.value(	x2592	)))
filepoint.writelines	('\tx2593	'+	str	(p.value(	x2593	)))
filepoint.writelines	('\tx2594	'+	str	(p.value(	x2594	)))
filepoint.writelines	('\tx2595	'+	str	(p.value(	x2595	)))
filepoint.writelines	('\tx2596	'+	str	(p.value(	x2596	)))
filepoint.writelines	('\tx2597	'+	str	(p.value(	x2597	)))
filepoint.writelines	('\tx2598	'+	str	(p.value(	x2598	)))
filepoint.writelines	('\tx2599	'+	str	(p.value(	x2599	)))
filepoint.writelines	('\tx2600	'+	str	(p.value(	x2600	)))
filepoint.writelines	('\tx2601	'+	str	(p.value(	x2601	)))
filepoint.writelines	('\tx2602	'+	str	(p.value(	x2602	)))
filepoint.writelines	('\tx2603	'+	str	(p.value(	x2603	)))
filepoint.writelines	('\tx2604	'+	str	(p.value(	x2604	)))
filepoint.writelines	('\tx2605	'+	str	(p.value(	x2605	)))
filepoint.writelines	('\tx2606	'+	str	(p.value(	x2606	)))
filepoint.writelines	('\tx2607	'+	str	(p.value(	x2607	)))
filepoint.writelines	('\tx2608	'+	str	(p.value(	x2608	)))
filepoint.writelines	('\tx2609	'+	str	(p.value(	x2609	)))
filepoint.writelines	('\tx2610	'+	str	(p.value(	x2610	)))
filepoint.writelines	('\tx2611	'+	str	(p.value(	x2611	)))
filepoint.writelines	('\tx2612	'+	str	(p.value(	x2612	)))
filepoint.writelines	('\tx2613	'+	str	(p.value(	x2613	)))
filepoint.writelines	('\tx2614	'+	str	(p.value(	x2614	)))
filepoint.writelines	('\tx2615	'+	str	(p.value(	x2615	)))
filepoint.writelines	('\tx2616	'+	str	(p.value(	x2616	)))
filepoint.writelines	('\tx2617	'+	str	(p.value(	x2617	)))
filepoint.writelines	('\tx2618	'+	str	(p.value(	x2618	)))
filepoint.writelines	('\tx2619	'+	str	(p.value(	x2619	)))
filepoint.writelines	('\tx2620	'+	str	(p.value(	x2620	)))
filepoint.writelines	('\tx2621	'+	str	(p.value(	x2621	)))
filepoint.writelines	('\tx2622	'+	str	(p.value(	x2622	)))
filepoint.writelines	('\tx2623	'+	str	(p.value(	x2623	)))
filepoint.writelines	('\tx2624	'+	str	(p.value(	x2624	)))
filepoint.writelines	('\tx2625	'+	str	(p.value(	x2625	)))
filepoint.writelines	('\tx2626	'+	str	(p.value(	x2626	)))
filepoint.writelines	('\tx2627	'+	str	(p.value(	x2627	)))
filepoint.writelines	('\tx2628	'+	str	(p.value(	x2628	)))
filepoint.writelines	('\tx2629	'+	str	(p.value(	x2629	)))
filepoint.writelines	('\tx2630	'+	str	(p.value(	x2630	)))
filepoint.writelines	('\tx2631	'+	str	(p.value(	x2631	)))
filepoint.writelines	('\tx2632	'+	str	(p.value(	x2632	)))
filepoint.writelines	('\tx2633	'+	str	(p.value(	x2633	)))
filepoint.writelines	('\tx2634	'+	str	(p.value(	x2634	)))
filepoint.writelines	('\tx2635	'+	str	(p.value(	x2635	)))
filepoint.writelines	('\tx2636	'+	str	(p.value(	x2636	)))
filepoint.writelines	('\tx2637	'+	str	(p.value(	x2637	)))
filepoint.writelines	('\tx2638	'+	str	(p.value(	x2638	)))
filepoint.writelines	('\tx2639	'+	str	(p.value(	x2639	)))
filepoint.writelines	('\tx2640	'+	str	(p.value(	x2640	)))
filepoint.writelines	('\tx2641	'+	str	(p.value(	x2641	)))
filepoint.writelines	('\tx2642	'+	str	(p.value(	x2642	)))
filepoint.writelines	('\tx2643	'+	str	(p.value(	x2643	)))
filepoint.writelines	('\tx2644	'+	str	(p.value(	x2644	)))
filepoint.writelines	('\tx2645	'+	str	(p.value(	x2645	)))
filepoint.writelines	('\tx2646	'+	str	(p.value(	x2646	)))
filepoint.writelines	('\tx2647	'+	str	(p.value(	x2647	)))
filepoint.writelines	('\tx2648	'+	str	(p.value(	x2648	)))
filepoint.writelines	('\tx2649	'+	str	(p.value(	x2649	)))
filepoint.writelines	('\tx2650	'+	str	(p.value(	x2650	)))
filepoint.writelines	('\tx2651	'+	str	(p.value(	x2651	)))
filepoint.writelines	('\tx2652	'+	str	(p.value(	x2652	)))
filepoint.writelines	('\tx2653	'+	str	(p.value(	x2653	)))
filepoint.writelines	('\tx2654	'+	str	(p.value(	x2654	)))
filepoint.writelines	('\tx2655	'+	str	(p.value(	x2655	)))
filepoint.writelines	('\tx2656	'+	str	(p.value(	x2656	)))
filepoint.writelines	('\tx2657	'+	str	(p.value(	x2657	)))
filepoint.writelines	('\tx2658	'+	str	(p.value(	x2658	)))
filepoint.writelines	('\tx2659	'+	str	(p.value(	x2659	)))
filepoint.writelines	('\tx2660	'+	str	(p.value(	x2660	)))
filepoint.writelines	('\tx2661	'+	str	(p.value(	x2661	)))
filepoint.writelines	('\tx2662	'+	str	(p.value(	x2662	)))
filepoint.writelines	('\tx2663	'+	str	(p.value(	x2663	)))
filepoint.writelines	('\tx2664	'+	str	(p.value(	x2664	)))
filepoint.writelines	('\tx2665	'+	str	(p.value(	x2665	)))
filepoint.writelines	('\tx2666	'+	str	(p.value(	x2666	)))
filepoint.writelines	('\tx2667	'+	str	(p.value(	x2667	)))
filepoint.writelines	('\tx2668	'+	str	(p.value(	x2668	)))
filepoint.writelines	('\tx2669	'+	str	(p.value(	x2669	)))
filepoint.writelines	('\tx2670	'+	str	(p.value(	x2670	)))
filepoint.writelines	('\tx2671	'+	str	(p.value(	x2671	)))
filepoint.writelines	('\tx2672	'+	str	(p.value(	x2672	)))
filepoint.writelines	('\tx2673	'+	str	(p.value(	x2673	)))
filepoint.writelines	('\tx2674	'+	str	(p.value(	x2674	)))
filepoint.writelines	('\tx2675	'+	str	(p.value(	x2675	)))
filepoint.writelines	('\tx2676	'+	str	(p.value(	x2676	)))
filepoint.writelines	('\tx2677	'+	str	(p.value(	x2677	)))
filepoint.writelines	('\tx2678	'+	str	(p.value(	x2678	)))
filepoint.writelines	('\tx2679	'+	str	(p.value(	x2679	)))
filepoint.writelines	('\tx2680	'+	str	(p.value(	x2680	)))
filepoint.writelines	('\tx2681	'+	str	(p.value(	x2681	)))
filepoint.writelines	('\tx2682	'+	str	(p.value(	x2682	)))
filepoint.writelines	('\tx2683	'+	str	(p.value(	x2683	)))
filepoint.writelines	('\tx2684	'+	str	(p.value(	x2684	)))
filepoint.writelines	('\tx2685	'+	str	(p.value(	x2685	)))
filepoint.writelines	('\tx2686	'+	str	(p.value(	x2686	)))
filepoint.writelines	('\tx2687	'+	str	(p.value(	x2687	)))
filepoint.writelines	('\tx2688	'+	str	(p.value(	x2688	)))
filepoint.writelines	('\tx2689	'+	str	(p.value(	x2689	)))
filepoint.writelines	('\tx2690	'+	str	(p.value(	x2690	)))
filepoint.writelines	('\tx2691	'+	str	(p.value(	x2691	)))
filepoint.writelines	('\tx2692	'+	str	(p.value(	x2692	)))
filepoint.writelines	('\tx2693	'+	str	(p.value(	x2693	)))
filepoint.writelines	('\tx2694	'+	str	(p.value(	x2694	)))
filepoint.writelines	('\tx2695	'+	str	(p.value(	x2695	)))
filepoint.writelines	('\tx2696	'+	str	(p.value(	x2696	)))
filepoint.writelines	('\tx2697	'+	str	(p.value(	x2697	)))
filepoint.writelines	('\tx2698	'+	str	(p.value(	x2698	)))
filepoint.writelines	('\tx2699	'+	str	(p.value(	x2699	)))
filepoint.writelines	('\tx2700	'+	str	(p.value(	x2700	)))
filepoint.writelines	('\tx2701	'+	str	(p.value(	x2701	)))
filepoint.writelines	('\tx2702	'+	str	(p.value(	x2702	)))
filepoint.writelines	('\tx2703	'+	str	(p.value(	x2703	)))
filepoint.writelines	('\tx2704	'+	str	(p.value(	x2704	)))
filepoint.writelines	('\tx2705	'+	str	(p.value(	x2705	)))
filepoint.writelines	('\tx2706	'+	str	(p.value(	x2706	)))
filepoint.writelines	('\tx2707	'+	str	(p.value(	x2707	)))
filepoint.writelines	('\tx2708	'+	str	(p.value(	x2708	)))
filepoint.writelines	('\tx2709	'+	str	(p.value(	x2709	)))
filepoint.writelines	('\tx2710	'+	str	(p.value(	x2710	)))
filepoint.writelines	('\tx2711	'+	str	(p.value(	x2711	)))
filepoint.writelines	('\tx2712	'+	str	(p.value(	x2712	)))
filepoint.writelines	('\tx2713	'+	str	(p.value(	x2713	)))
filepoint.writelines	('\tx2714	'+	str	(p.value(	x2714	)))
filepoint.writelines	('\tx2715	'+	str	(p.value(	x2715	)))
filepoint.writelines	('\tx2716	'+	str	(p.value(	x2716	)))
filepoint.writelines	('\tx2717	'+	str	(p.value(	x2717	)))
filepoint.writelines	('\tx2718	'+	str	(p.value(	x2718	)))
filepoint.writelines	('\tx2719	'+	str	(p.value(	x2719	)))
filepoint.writelines	('\tx2720	'+	str	(p.value(	x2720	)))
filepoint.writelines	('\tx2721	'+	str	(p.value(	x2721	)))
filepoint.writelines	('\tx2722	'+	str	(p.value(	x2722	)))
filepoint.writelines	('\tx2723	'+	str	(p.value(	x2723	)))
filepoint.writelines	('\tx2724	'+	str	(p.value(	x2724	)))
filepoint.writelines	('\tx2725	'+	str	(p.value(	x2725	)))
filepoint.writelines	('\tx2726	'+	str	(p.value(	x2726	)))
filepoint.writelines	('\tx2727	'+	str	(p.value(	x2727	)))
filepoint.writelines	('\tx2728	'+	str	(p.value(	x2728	)))
filepoint.writelines	('\tx2729	'+	str	(p.value(	x2729	)))
filepoint.writelines	('\tx2730	'+	str	(p.value(	x2730	)))
filepoint.writelines	('\tx2731	'+	str	(p.value(	x2731	)))
filepoint.writelines	('\tx2732	'+	str	(p.value(	x2732	)))
filepoint.writelines	('\tx2733	'+	str	(p.value(	x2733	)))
filepoint.writelines	('\tx2734	'+	str	(p.value(	x2734	)))
filepoint.writelines	('\tx2735	'+	str	(p.value(	x2735	)))
filepoint.writelines	('\tx2736	'+	str	(p.value(	x2736	)))
filepoint.writelines	('\tx2737	'+	str	(p.value(	x2737	)))
filepoint.writelines	('\tx2738	'+	str	(p.value(	x2738	)))
filepoint.writelines	('\tx2739	'+	str	(p.value(	x2739	)))
filepoint.writelines	('\tx2740	'+	str	(p.value(	x2740	)))
filepoint.writelines	('\tx2741	'+	str	(p.value(	x2741	)))
filepoint.writelines	('\tx2742	'+	str	(p.value(	x2742	)))
filepoint.writelines	('\tx2743	'+	str	(p.value(	x2743	)))
filepoint.writelines	('\tx2744	'+	str	(p.value(	x2744	)))
filepoint.writelines	('\tx2745	'+	str	(p.value(	x2745	)))
filepoint.writelines	('\tx2746	'+	str	(p.value(	x2746	)))
filepoint.writelines	('\tx2747	'+	str	(p.value(	x2747	)))
filepoint.writelines	('\tx2748	'+	str	(p.value(	x2748	)))
filepoint.writelines	('\tx2749	'+	str	(p.value(	x2749	)))
filepoint.writelines	('\tx2750	'+	str	(p.value(	x2750	)))
filepoint.writelines	('\tx2751	'+	str	(p.value(	x2751	)))
filepoint.writelines	('\tx2752	'+	str	(p.value(	x2752	)))
filepoint.writelines	('\tx2753	'+	str	(p.value(	x2753	)))
filepoint.writelines	('\tx2754	'+	str	(p.value(	x2754	)))
filepoint.writelines	('\tx2755	'+	str	(p.value(	x2755	)))
filepoint.writelines	('\tx2756	'+	str	(p.value(	x2756	)))
filepoint.writelines	('\tx2757	'+	str	(p.value(	x2757	)))
filepoint.writelines	('\tx2758	'+	str	(p.value(	x2758	)))
filepoint.writelines	('\tx2759	'+	str	(p.value(	x2759	)))
filepoint.writelines	('\tx2760	'+	str	(p.value(	x2760	)))
filepoint.writelines	('\tx2761	'+	str	(p.value(	x2761	)))
filepoint.writelines	('\tx2762	'+	str	(p.value(	x2762	)))
filepoint.writelines	('\tx2763	'+	str	(p.value(	x2763	)))
filepoint.writelines	('\tx2764	'+	str	(p.value(	x2764	)))
filepoint.writelines	('\tx2765	'+	str	(p.value(	x2765	)))
filepoint.writelines	('\tx2766	'+	str	(p.value(	x2766	)))
filepoint.writelines	('\tx2767	'+	str	(p.value(	x2767	)))
filepoint.writelines	('\tx2768	'+	str	(p.value(	x2768	)))
filepoint.writelines	('\tx2769	'+	str	(p.value(	x2769	)))
filepoint.writelines	('\tx2770	'+	str	(p.value(	x2770	)))
filepoint.writelines	('\tx2771	'+	str	(p.value(	x2771	)))
filepoint.writelines	('\tx2772	'+	str	(p.value(	x2772	)))
filepoint.writelines	('\tx2773	'+	str	(p.value(	x2773	)))
filepoint.writelines	('\tx2774	'+	str	(p.value(	x2774	)))
filepoint.writelines	('\tx2775	'+	str	(p.value(	x2775	)))
filepoint.writelines	('\tx2776	'+	str	(p.value(	x2776	)))
filepoint.writelines	('\tx2777	'+	str	(p.value(	x2777	)))
filepoint.writelines	('\tx2778	'+	str	(p.value(	x2778	)))
filepoint.writelines	('\tx2779	'+	str	(p.value(	x2779	)))
filepoint.writelines	('\tx2780	'+	str	(p.value(	x2780	)))
filepoint.writelines	('\tx2781	'+	str	(p.value(	x2781	)))
filepoint.writelines	('\tx2782	'+	str	(p.value(	x2782	)))
filepoint.writelines	('\tx2783	'+	str	(p.value(	x2783	)))
filepoint.writelines	('\tx2784	'+	str	(p.value(	x2784	)))
filepoint.writelines	('\tx2785	'+	str	(p.value(	x2785	)))
filepoint.writelines	('\tx2786	'+	str	(p.value(	x2786	)))
filepoint.writelines	('\tx2787	'+	str	(p.value(	x2787	)))
filepoint.writelines	('\tx2788	'+	str	(p.value(	x2788	)))
filepoint.writelines	('\tx2789	'+	str	(p.value(	x2789	)))
filepoint.writelines	('\tx2790	'+	str	(p.value(	x2790	)))
filepoint.writelines	('\tx2791	'+	str	(p.value(	x2791	)))
filepoint.writelines	('\tx2792	'+	str	(p.value(	x2792	)))
filepoint.writelines	('\tx2793	'+	str	(p.value(	x2793	)))
filepoint.writelines	('\tx2794	'+	str	(p.value(	x2794	)))
filepoint.writelines	('\tx2795	'+	str	(p.value(	x2795	)))
filepoint.writelines	('\tx2796	'+	str	(p.value(	x2796	)))
filepoint.writelines	('\tx2797	'+	str	(p.value(	x2797	)))
filepoint.writelines	('\tx2798	'+	str	(p.value(	x2798	)))
filepoint.writelines	('\tx2799	'+	str	(p.value(	x2799	)))
filepoint.writelines	('\tx2800	'+	str	(p.value(	x2800	)))
filepoint.writelines	('\tx2801	'+	str	(p.value(	x2801	)))
filepoint.writelines	('\tx2802	'+	str	(p.value(	x2802	)))
filepoint.writelines	('\tx2803	'+	str	(p.value(	x2803	)))
filepoint.writelines	('\tx2804	'+	str	(p.value(	x2804	)))
filepoint.writelines	('\tx2805	'+	str	(p.value(	x2805	)))
filepoint.writelines	('\tx2806	'+	str	(p.value(	x2806	)))
filepoint.writelines	('\tx2807	'+	str	(p.value(	x2807	)))
filepoint.writelines	('\tx2808	'+	str	(p.value(	x2808	)))
filepoint.writelines	('\tx2809	'+	str	(p.value(	x2809	)))
filepoint.writelines	('\tx2810	'+	str	(p.value(	x2810	)))
filepoint.writelines	('\tx2811	'+	str	(p.value(	x2811	)))
filepoint.writelines	('\tx2812	'+	str	(p.value(	x2812	)))
filepoint.writelines	('\tx2813	'+	str	(p.value(	x2813	)))
filepoint.writelines	('\tx2814	'+	str	(p.value(	x2814	)))
filepoint.writelines	('\tx2815	'+	str	(p.value(	x2815	)))
filepoint.writelines	('\tx2816	'+	str	(p.value(	x2816	)))
filepoint.writelines	('\tx2817	'+	str	(p.value(	x2817	)))
filepoint.writelines	('\tx2818	'+	str	(p.value(	x2818	)))
filepoint.writelines	('\tx2819	'+	str	(p.value(	x2819	)))
filepoint.writelines	('\tx2820	'+	str	(p.value(	x2820	)))
filepoint.writelines	('\tx2821	'+	str	(p.value(	x2821	)))
filepoint.writelines	('\tx2822	'+	str	(p.value(	x2822	)))
filepoint.writelines	('\tx2823	'+	str	(p.value(	x2823	)))
filepoint.writelines	('\tx2824	'+	str	(p.value(	x2824	)))
filepoint.writelines	('\tx2825	'+	str	(p.value(	x2825	)))
filepoint.writelines	('\tx2826	'+	str	(p.value(	x2826	)))
filepoint.writelines	('\tx2827	'+	str	(p.value(	x2827	)))
filepoint.writelines	('\tx2828	'+	str	(p.value(	x2828	)))
filepoint.writelines	('\tx2829	'+	str	(p.value(	x2829	)))
filepoint.writelines	('\tx2830	'+	str	(p.value(	x2830	)))
filepoint.writelines	('\tx2831	'+	str	(p.value(	x2831	)))
filepoint.writelines	('\tx2832	'+	str	(p.value(	x2832	)))
filepoint.writelines	('\tx2833	'+	str	(p.value(	x2833	)))
filepoint.writelines	('\tx2834	'+	str	(p.value(	x2834	)))
filepoint.writelines	('\tx2835	'+	str	(p.value(	x2835	)))
filepoint.writelines	('\tx2836	'+	str	(p.value(	x2836	)))
filepoint.writelines	('\tx2837	'+	str	(p.value(	x2837	)))
filepoint.writelines	('\tx2838	'+	str	(p.value(	x2838	)))
filepoint.writelines	('\tx2839	'+	str	(p.value(	x2839	)))
filepoint.writelines	('\tx2840	'+	str	(p.value(	x2840	)))
filepoint.writelines	('\tx2841	'+	str	(p.value(	x2841	)))
filepoint.writelines	('\tx2842	'+	str	(p.value(	x2842	)))
filepoint.writelines	('\tx2843	'+	str	(p.value(	x2843	)))
filepoint.writelines	('\tx2844	'+	str	(p.value(	x2844	)))
filepoint.writelines	('\tx2845	'+	str	(p.value(	x2845	)))
filepoint.writelines	('\tx2846	'+	str	(p.value(	x2846	)))
filepoint.writelines	('\tx2847	'+	str	(p.value(	x2847	)))
filepoint.writelines	('\tx2848	'+	str	(p.value(	x2848	)))
filepoint.writelines	('\tx2849	'+	str	(p.value(	x2849	)))
filepoint.writelines	('\tx2850	'+	str	(p.value(	x2850	)))
filepoint.writelines	('\tx2851	'+	str	(p.value(	x2851	)))
filepoint.writelines	('\tx2852	'+	str	(p.value(	x2852	)))
filepoint.writelines	('\tx2853	'+	str	(p.value(	x2853	)))
filepoint.writelines	('\tx2854	'+	str	(p.value(	x2854	)))
filepoint.writelines	('\tx2855	'+	str	(p.value(	x2855	)))
filepoint.writelines	('\tx2856	'+	str	(p.value(	x2856	)))
filepoint.writelines	('\tx2857	'+	str	(p.value(	x2857	)))
filepoint.writelines	('\tx2858	'+	str	(p.value(	x2858	)))
filepoint.writelines	('\tx2859	'+	str	(p.value(	x2859	)))
filepoint.writelines	('\tx2860	'+	str	(p.value(	x2860	)))
filepoint.writelines	('\tx2861	'+	str	(p.value(	x2861	)))
filepoint.writelines	('\tx2862	'+	str	(p.value(	x2862	)))
filepoint.writelines	('\tx2863	'+	str	(p.value(	x2863	)))
filepoint.writelines	('\tx2864	'+	str	(p.value(	x2864	)))
filepoint.writelines	('\tx2865	'+	str	(p.value(	x2865	)))
filepoint.writelines	('\tx2866	'+	str	(p.value(	x2866	)))
filepoint.writelines	('\tx2867	'+	str	(p.value(	x2867	)))
filepoint.writelines	('\tx2868	'+	str	(p.value(	x2868	)))
filepoint.writelines	('\tx2869	'+	str	(p.value(	x2869	)))
filepoint.writelines	('\tx2870	'+	str	(p.value(	x2870	)))
filepoint.writelines	('\tx2871	'+	str	(p.value(	x2871	)))
filepoint.writelines	('\tx2872	'+	str	(p.value(	x2872	)))
filepoint.writelines	('\tx2873	'+	str	(p.value(	x2873	)))
filepoint.writelines	('\tx2874	'+	str	(p.value(	x2874	)))
filepoint.writelines	('\tx2875	'+	str	(p.value(	x2875	)))
filepoint.writelines	('\tx2876	'+	str	(p.value(	x2876	)))
filepoint.writelines	('\tx2877	'+	str	(p.value(	x2877	)))
filepoint.writelines	('\tx2878	'+	str	(p.value(	x2878	)))
filepoint.writelines	('\tx2879	'+	str	(p.value(	x2879	)))
filepoint.writelines	('\tx2880	'+	str	(p.value(	x2880	)))
filepoint.writelines	('\tx2881	'+	str	(p.value(	x2881	)))
filepoint.writelines	('\tx2882	'+	str	(p.value(	x2882	)))
filepoint.writelines	('\tx2883	'+	str	(p.value(	x2883	)))
filepoint.writelines	('\tx2884	'+	str	(p.value(	x2884	)))
filepoint.writelines	('\tx2885	'+	str	(p.value(	x2885	)))
filepoint.writelines	('\tx2886	'+	str	(p.value(	x2886	)))
filepoint.writelines	('\tx2887	'+	str	(p.value(	x2887	)))
filepoint.writelines	('\tx2888	'+	str	(p.value(	x2888	)))
filepoint.writelines	('\tx2889	'+	str	(p.value(	x2889	)))
filepoint.writelines	('\tx2890	'+	str	(p.value(	x2890	)))
filepoint.writelines	('\tx2891	'+	str	(p.value(	x2891	)))
filepoint.writelines	('\tx2892	'+	str	(p.value(	x2892	)))
filepoint.writelines	('\tx2893	'+	str	(p.value(	x2893	)))
filepoint.writelines	('\tx2894	'+	str	(p.value(	x2894	)))
filepoint.writelines	('\tx2895	'+	str	(p.value(	x2895	)))
filepoint.writelines	('\tx2896	'+	str	(p.value(	x2896	)))
filepoint.writelines	('\tx2897	'+	str	(p.value(	x2897	)))
filepoint.writelines	('\tx2898	'+	str	(p.value(	x2898	)))
filepoint.writelines	('\tx2899	'+	str	(p.value(	x2899	)))
filepoint.writelines	('\tx2900	'+	str	(p.value(	x2900	)))
filepoint.writelines	('\tx2901	'+	str	(p.value(	x2901	)))
filepoint.writelines	('\tx2902	'+	str	(p.value(	x2902	)))
filepoint.writelines	('\tx2903	'+	str	(p.value(	x2903	)))
filepoint.writelines	('\tx2904	'+	str	(p.value(	x2904	)))
filepoint.writelines	('\tx2905	'+	str	(p.value(	x2905	)))
filepoint.writelines	('\tx2906	'+	str	(p.value(	x2906	)))
filepoint.writelines	('\tx2907	'+	str	(p.value(	x2907	)))
filepoint.writelines	('\tx2908	'+	str	(p.value(	x2908	)))
filepoint.writelines	('\tx2909	'+	str	(p.value(	x2909	)))
filepoint.writelines	('\tx2910	'+	str	(p.value(	x2910	)))
filepoint.writelines	('\tx2911	'+	str	(p.value(	x2911	)))
filepoint.writelines	('\tx2912	'+	str	(p.value(	x2912	)))
filepoint.writelines	('\tx2913	'+	str	(p.value(	x2913	)))
filepoint.writelines	('\tx2914	'+	str	(p.value(	x2914	)))
filepoint.writelines	('\tx2915	'+	str	(p.value(	x2915	)))
filepoint.writelines	('\tx2916	'+	str	(p.value(	x2916	)))
filepoint.writelines	('\tx2917	'+	str	(p.value(	x2917	)))
filepoint.writelines	('\tx2918	'+	str	(p.value(	x2918	)))
filepoint.writelines	('\tx2919	'+	str	(p.value(	x2919	)))
filepoint.writelines	('\tx2920	'+	str	(p.value(	x2920	)))
filepoint.writelines	('\tx2921	'+	str	(p.value(	x2921	)))
filepoint.writelines	('\tx2922	'+	str	(p.value(	x2922	)))
filepoint.writelines	('\tx2923	'+	str	(p.value(	x2923	)))
filepoint.writelines	('\tx2924	'+	str	(p.value(	x2924	)))
filepoint.writelines	('\tx2925	'+	str	(p.value(	x2925	)))
filepoint.writelines	('\tx2926	'+	str	(p.value(	x2926	)))
filepoint.writelines	('\tx2927	'+	str	(p.value(	x2927	)))
filepoint.writelines	('\tx2928	'+	str	(p.value(	x2928	)))
filepoint.writelines	('\tx2929	'+	str	(p.value(	x2929	)))
filepoint.writelines	('\tx2930	'+	str	(p.value(	x2930	)))
filepoint.writelines	('\tx2931	'+	str	(p.value(	x2931	)))
filepoint.writelines	('\tx2932	'+	str	(p.value(	x2932	)))
filepoint.writelines	('\tx2933	'+	str	(p.value(	x2933	)))
filepoint.writelines	('\tx2934	'+	str	(p.value(	x2934	)))
filepoint.writelines	('\tx2935	'+	str	(p.value(	x2935	)))
filepoint.writelines	('\tx2936	'+	str	(p.value(	x2936	)))
filepoint.writelines	('\tx2937	'+	str	(p.value(	x2937	)))
filepoint.writelines	('\tx2938	'+	str	(p.value(	x2938	)))
filepoint.writelines	('\tx2939	'+	str	(p.value(	x2939	)))
filepoint.writelines	('\tx2940	'+	str	(p.value(	x2940	)))
filepoint.writelines	('\tx2941	'+	str	(p.value(	x2941	)))
filepoint.writelines	('\tx2942	'+	str	(p.value(	x2942	)))
filepoint.writelines	('\tx2943	'+	str	(p.value(	x2943	)))
filepoint.writelines	('\tx2944	'+	str	(p.value(	x2944	)))
filepoint.writelines	('\tx2945	'+	str	(p.value(	x2945	)))
filepoint.writelines	('\tx2946	'+	str	(p.value(	x2946	)))
filepoint.writelines	('\tx2947	'+	str	(p.value(	x2947	)))
filepoint.writelines	('\tx2948	'+	str	(p.value(	x2948	)))
filepoint.writelines	('\tx2949	'+	str	(p.value(	x2949	)))
filepoint.writelines	('\tx2950	'+	str	(p.value(	x2950	)))
filepoint.writelines	('\tx2951	'+	str	(p.value(	x2951	)))
filepoint.writelines	('\tx2952	'+	str	(p.value(	x2952	)))
filepoint.writelines	('\tx2953	'+	str	(p.value(	x2953	)))
filepoint.writelines	('\tx2954	'+	str	(p.value(	x2954	)))
filepoint.writelines	('\tx2955	'+	str	(p.value(	x2955	)))
filepoint.writelines	('\tx2956	'+	str	(p.value(	x2956	)))
filepoint.writelines	('\tx2957	'+	str	(p.value(	x2957	)))
filepoint.writelines	('\tx2958	'+	str	(p.value(	x2958	)))
filepoint.writelines	('\tx2959	'+	str	(p.value(	x2959	)))
filepoint.writelines	('\tx2960	'+	str	(p.value(	x2960	)))
filepoint.writelines	('\tx2961	'+	str	(p.value(	x2961	)))
filepoint.writelines	('\tx2962	'+	str	(p.value(	x2962	)))
filepoint.writelines	('\tx2963	'+	str	(p.value(	x2963	)))
filepoint.writelines	('\tx2964	'+	str	(p.value(	x2964	)))
filepoint.writelines	('\tx2965	'+	str	(p.value(	x2965	)))
filepoint.writelines	('\tx2966	'+	str	(p.value(	x2966	)))
filepoint.writelines	('\tx2967	'+	str	(p.value(	x2967	)))
filepoint.writelines	('\tx2968	'+	str	(p.value(	x2968	)))
filepoint.writelines	('\tx2969	'+	str	(p.value(	x2969	)))
filepoint.writelines	('\tx2970	'+	str	(p.value(	x2970	)))
filepoint.writelines	('\tx2971	'+	str	(p.value(	x2971	)))
filepoint.writelines	('\tx2972	'+	str	(p.value(	x2972	)))
filepoint.writelines	('\tx2973	'+	str	(p.value(	x2973	)))
filepoint.writelines	('\tx2974	'+	str	(p.value(	x2974	)))
filepoint.writelines	('\tx2975	'+	str	(p.value(	x2975	)))
filepoint.writelines	('\tx2976	'+	str	(p.value(	x2976	)))
filepoint.writelines	('\tx2977	'+	str	(p.value(	x2977	)))
filepoint.writelines	('\tx2978	'+	str	(p.value(	x2978	)))
filepoint.writelines	('\tx2979	'+	str	(p.value(	x2979	)))
filepoint.writelines	('\tx2980	'+	str	(p.value(	x2980	)))
filepoint.writelines	('\tx2981	'+	str	(p.value(	x2981	)))
filepoint.writelines	('\tx2982	'+	str	(p.value(	x2982	)))
filepoint.writelines	('\tx2983	'+	str	(p.value(	x2983	)))
filepoint.writelines	('\tx2984	'+	str	(p.value(	x2984	)))
filepoint.writelines	('\tx2985	'+	str	(p.value(	x2985	)))
filepoint.writelines	('\tx2986	'+	str	(p.value(	x2986	)))
filepoint.writelines	('\tx2987	'+	str	(p.value(	x2987	)))
filepoint.writelines	('\tx2988	'+	str	(p.value(	x2988	)))
filepoint.writelines	('\tx2989	'+	str	(p.value(	x2989	)))
filepoint.writelines	('\tx2990	'+	str	(p.value(	x2990	)))
filepoint.writelines	('\tx2991	'+	str	(p.value(	x2991	)))
filepoint.writelines	('\tx2992	'+	str	(p.value(	x2992	)))
filepoint.writelines	('\tx2993	'+	str	(p.value(	x2993	)))
filepoint.writelines	('\tx2994	'+	str	(p.value(	x2994	)))
filepoint.writelines	('\tx2995	'+	str	(p.value(	x2995	)))
filepoint.writelines	('\tx2996	'+	str	(p.value(	x2996	)))
filepoint.writelines	('\tx2997	'+	str	(p.value(	x2997	)))
filepoint.writelines	('\tx2998	'+	str	(p.value(	x2998	)))
filepoint.writelines	('\tx2999	'+	str	(p.value(	x2999	)))
filepoint.writelines	('\tx3000	'+	str	(p.value(	x3000	)))
filepoint.writelines	('\tx3001	'+	str	(p.value(	x3001	)))
filepoint.writelines	('\tx3002	'+	str	(p.value(	x3002	)))
filepoint.writelines	('\tx3003	'+	str	(p.value(	x3003	)))
filepoint.writelines	('\tx3004	'+	str	(p.value(	x3004	)))
filepoint.writelines	('\tx3005	'+	str	(p.value(	x3005	)))
filepoint.writelines	('\tx3006	'+	str	(p.value(	x3006	)))
filepoint.writelines	('\tx3007	'+	str	(p.value(	x3007	)))
filepoint.writelines	('\tx3008	'+	str	(p.value(	x3008	)))
filepoint.writelines	('\tx3009	'+	str	(p.value(	x3009	)))
filepoint.writelines	('\tx3010	'+	str	(p.value(	x3010	)))
filepoint.writelines	('\tx3011	'+	str	(p.value(	x3011	)))
filepoint.writelines	('\tx3012	'+	str	(p.value(	x3012	)))
filepoint.writelines	('\tx3013	'+	str	(p.value(	x3013	)))
filepoint.writelines	('\tx3014	'+	str	(p.value(	x3014	)))
filepoint.writelines	('\tx3015	'+	str	(p.value(	x3015	)))
filepoint.writelines	('\tx3016	'+	str	(p.value(	x3016	)))
filepoint.writelines	('\tx3017	'+	str	(p.value(	x3017	)))
filepoint.writelines	('\tx3018	'+	str	(p.value(	x3018	)))
filepoint.writelines	('\tx3019	'+	str	(p.value(	x3019	)))
filepoint.writelines	('\tx3020	'+	str	(p.value(	x3020	)))
filepoint.writelines	('\tx3021	'+	str	(p.value(	x3021	)))
filepoint.writelines	('\tx3022	'+	str	(p.value(	x3022	)))
filepoint.writelines	('\tx3023	'+	str	(p.value(	x3023	)))
filepoint.writelines	('\tx3024	'+	str	(p.value(	x3024	)))
filepoint.writelines	('\tx3025	'+	str	(p.value(	x3025	)))
filepoint.writelines	('\tx3026	'+	str	(p.value(	x3026	)))
filepoint.writelines	('\tx3027	'+	str	(p.value(	x3027	)))
filepoint.writelines	('\tx3028	'+	str	(p.value(	x3028	)))
filepoint.writelines	('\tx3029	'+	str	(p.value(	x3029	)))
filepoint.writelines	('\tx3030	'+	str	(p.value(	x3030	)))
filepoint.writelines	('\tx3031	'+	str	(p.value(	x3031	)))
filepoint.writelines	('\tx3032	'+	str	(p.value(	x3032	)))
filepoint.writelines	('\tx3033	'+	str	(p.value(	x3033	)))
filepoint.writelines	('\tx3034	'+	str	(p.value(	x3034	)))
filepoint.writelines	('\tx3035	'+	str	(p.value(	x3035	)))
filepoint.writelines	('\tx3036	'+	str	(p.value(	x3036	)))
filepoint.writelines	('\tx3037	'+	str	(p.value(	x3037	)))
filepoint.writelines	('\tx3038	'+	str	(p.value(	x3038	)))
filepoint.writelines	('\tx3039	'+	str	(p.value(	x3039	)))
filepoint.writelines	('\tx3040	'+	str	(p.value(	x3040	)))
filepoint.writelines	('\tx3041	'+	str	(p.value(	x3041	)))
filepoint.writelines	('\tx3042	'+	str	(p.value(	x3042	)))
filepoint.writelines	('\tx3043	'+	str	(p.value(	x3043	)))
filepoint.writelines	('\tx3044	'+	str	(p.value(	x3044	)))
filepoint.writelines	('\tx3045	'+	str	(p.value(	x3045	)))
filepoint.writelines	('\tx3046	'+	str	(p.value(	x3046	)))
filepoint.writelines	('\tx3047	'+	str	(p.value(	x3047	)))
filepoint.writelines	('\tx3048	'+	str	(p.value(	x3048	)))
filepoint.writelines	('\tx3049	'+	str	(p.value(	x3049	)))
filepoint.writelines	('\tx3050	'+	str	(p.value(	x3050	)))
filepoint.writelines	('\tx3051	'+	str	(p.value(	x3051	)))
filepoint.writelines	('\tx3052	'+	str	(p.value(	x3052	)))
filepoint.writelines	('\tx3053	'+	str	(p.value(	x3053	)))
filepoint.writelines	('\tx3054	'+	str	(p.value(	x3054	)))
filepoint.writelines	('\tx3055	'+	str	(p.value(	x3055	)))
filepoint.writelines	('\tx3056	'+	str	(p.value(	x3056	)))
filepoint.writelines	('\tx3057	'+	str	(p.value(	x3057	)))
filepoint.writelines	('\tx3058	'+	str	(p.value(	x3058	)))
filepoint.writelines	('\tx3059	'+	str	(p.value(	x3059	)))
filepoint.writelines	('\tx3060	'+	str	(p.value(	x3060	)))
filepoint.writelines	('\tx3061	'+	str	(p.value(	x3061	)))
filepoint.writelines	('\tx3062	'+	str	(p.value(	x3062	)))
filepoint.writelines	('\tx3063	'+	str	(p.value(	x3063	)))
filepoint.writelines	('\tx3064	'+	str	(p.value(	x3064	)))
filepoint.writelines	('\tx3065	'+	str	(p.value(	x3065	)))
filepoint.writelines	('\tx3066	'+	str	(p.value(	x3066	)))
filepoint.writelines	('\tx3067	'+	str	(p.value(	x3067	)))
filepoint.writelines	('\tx3068	'+	str	(p.value(	x3068	)))
filepoint.writelines	('\tx3069	'+	str	(p.value(	x3069	)))
filepoint.writelines	('\tx3070	'+	str	(p.value(	x3070	)))
filepoint.writelines	('\tx3071	'+	str	(p.value(	x3071	)))
filepoint.writelines	('\tx3072	'+	str	(p.value(	x3072	)))
filepoint.writelines	('\tx3073	'+	str	(p.value(	x3073	)))
filepoint.writelines	('\tx3074	'+	str	(p.value(	x3074	)))
filepoint.writelines	('\tx3075	'+	str	(p.value(	x3075	)))
filepoint.writelines	('\tx3076	'+	str	(p.value(	x3076	)))
filepoint.writelines	('\tx3077	'+	str	(p.value(	x3077	)))
filepoint.writelines	('\tx3078	'+	str	(p.value(	x3078	)))
filepoint.writelines	('\tx3079	'+	str	(p.value(	x3079	)))
filepoint.writelines	('\tx3080	'+	str	(p.value(	x3080	)))
filepoint.writelines	('\tx3081	'+	str	(p.value(	x3081	)))
filepoint.writelines	('\tx3082	'+	str	(p.value(	x3082	)))
filepoint.writelines	('\tx3083	'+	str	(p.value(	x3083	)))
filepoint.writelines	('\tx3084	'+	str	(p.value(	x3084	)))
filepoint.writelines	('\tx3085	'+	str	(p.value(	x3085	)))
filepoint.writelines	('\tx3086	'+	str	(p.value(	x3086	)))
filepoint.writelines	('\tx3087	'+	str	(p.value(	x3087	)))
filepoint.writelines	('\tx3088	'+	str	(p.value(	x3088	)))
filepoint.writelines	('\tx3089	'+	str	(p.value(	x3089	)))
filepoint.writelines	('\tx3090	'+	str	(p.value(	x3090	)))
filepoint.writelines	('\tx3091	'+	str	(p.value(	x3091	)))
filepoint.writelines	('\tx3092	'+	str	(p.value(	x3092	)))
filepoint.writelines	('\tx3093	'+	str	(p.value(	x3093	)))
filepoint.writelines	('\tx3094	'+	str	(p.value(	x3094	)))
filepoint.writelines	('\tx3095	'+	str	(p.value(	x3095	)))
filepoint.writelines	('\tx3096	'+	str	(p.value(	x3096	)))
filepoint.writelines	('\tx3097	'+	str	(p.value(	x3097	)))
filepoint.writelines	('\tx3098	'+	str	(p.value(	x3098	)))
filepoint.writelines	('\tx3099	'+	str	(p.value(	x3099	)))
filepoint.writelines	('\tx3100	'+	str	(p.value(	x3100	)))
filepoint.writelines	('\tx3101	'+	str	(p.value(	x3101	)))
filepoint.writelines	('\tx3102	'+	str	(p.value(	x3102	)))
filepoint.writelines	('\tx3103	'+	str	(p.value(	x3103	)))
filepoint.writelines	('\tx3104	'+	str	(p.value(	x3104	)))
filepoint.writelines	('\tx3105	'+	str	(p.value(	x3105	)))
filepoint.writelines	('\tx3106	'+	str	(p.value(	x3106	)))
filepoint.writelines	('\tx3107	'+	str	(p.value(	x3107	)))
filepoint.writelines	('\tx3108	'+	str	(p.value(	x3108	)))
filepoint.writelines	('\tx3109	'+	str	(p.value(	x3109	)))
filepoint.writelines	('\tx3110	'+	str	(p.value(	x3110	)))
filepoint.writelines	('\tx3111	'+	str	(p.value(	x3111	)))
filepoint.writelines	('\tx3112	'+	str	(p.value(	x3112	)))
filepoint.writelines	('\tx3113	'+	str	(p.value(	x3113	)))
filepoint.writelines	('\tx3114	'+	str	(p.value(	x3114	)))
filepoint.writelines	('\tx3115	'+	str	(p.value(	x3115	)))
filepoint.writelines	('\tx3116	'+	str	(p.value(	x3116	)))
filepoint.writelines	('\tx3117	'+	str	(p.value(	x3117	)))
filepoint.writelines	('\tx3118	'+	str	(p.value(	x3118	)))
filepoint.writelines	('\tx3119	'+	str	(p.value(	x3119	)))
filepoint.writelines	('\tx3120	'+	str	(p.value(	x3120	)))
filepoint.writelines	('\tx3121	'+	str	(p.value(	x3121	)))
filepoint.writelines	('\tx3122	'+	str	(p.value(	x3122	)))
filepoint.writelines	('\tx3123	'+	str	(p.value(	x3123	)))
filepoint.writelines	('\tx3124	'+	str	(p.value(	x3124	)))
filepoint.writelines	('\tx3125	'+	str	(p.value(	x3125	)))
filepoint.writelines	('\tx3126	'+	str	(p.value(	x3126	)))
filepoint.writelines	('\tx3127	'+	str	(p.value(	x3127	)))
filepoint.writelines	('\tx3128	'+	str	(p.value(	x3128	)))
filepoint.writelines	('\tx3129	'+	str	(p.value(	x3129	)))
filepoint.writelines	('\tx3130	'+	str	(p.value(	x3130	)))
filepoint.writelines	('\tx3131	'+	str	(p.value(	x3131	)))
filepoint.writelines	('\tx3132	'+	str	(p.value(	x3132	)))
filepoint.writelines	('\tx3133	'+	str	(p.value(	x3133	)))
filepoint.writelines	('\tx3134	'+	str	(p.value(	x3134	)))
filepoint.writelines	('\tx3135	'+	str	(p.value(	x3135	)))
filepoint.writelines	('\tx3136	'+	str	(p.value(	x3136	)))
filepoint.writelines	('\tx3137	'+	str	(p.value(	x3137	)))
filepoint.writelines	('\tx3138	'+	str	(p.value(	x3138	)))
filepoint.writelines	('\tx3139	'+	str	(p.value(	x3139	)))
filepoint.writelines	('\tx3140	'+	str	(p.value(	x3140	)))
filepoint.writelines	('\tx3141	'+	str	(p.value(	x3141	)))
filepoint.writelines	('\tx3142	'+	str	(p.value(	x3142	)))
filepoint.writelines	('\tx3143	'+	str	(p.value(	x3143	)))
filepoint.writelines	('\tx3144	'+	str	(p.value(	x3144	)))
filepoint.writelines	('\tx3145	'+	str	(p.value(	x3145	)))
filepoint.writelines	('\tx3146	'+	str	(p.value(	x3146	)))
filepoint.writelines	('\tx3147	'+	str	(p.value(	x3147	)))
filepoint.writelines	('\tx3148	'+	str	(p.value(	x3148	)))
filepoint.writelines	('\tx3149	'+	str	(p.value(	x3149	)))
filepoint.writelines	('\tx3150	'+	str	(p.value(	x3150	)))
filepoint.writelines	('\tx3151	'+	str	(p.value(	x3151	)))
filepoint.writelines	('\tx3152	'+	str	(p.value(	x3152	)))
filepoint.writelines	('\tx3153	'+	str	(p.value(	x3153	)))
filepoint.writelines	('\tx3154	'+	str	(p.value(	x3154	)))
filepoint.writelines	('\tx3155	'+	str	(p.value(	x3155	)))
filepoint.writelines	('\tx3156	'+	str	(p.value(	x3156	)))
filepoint.writelines	('\tx3157	'+	str	(p.value(	x3157	)))
filepoint.writelines	('\tx3158	'+	str	(p.value(	x3158	)))
filepoint.writelines	('\tx3159	'+	str	(p.value(	x3159	)))
filepoint.writelines	('\tx3160	'+	str	(p.value(	x3160	)))
filepoint.writelines	('\tx3161	'+	str	(p.value(	x3161	)))
filepoint.writelines	('\tx3162	'+	str	(p.value(	x3162	)))
filepoint.writelines	('\tx3163	'+	str	(p.value(	x3163	)))
filepoint.writelines	('\tx3164	'+	str	(p.value(	x3164	)))
filepoint.writelines	('\tx3165	'+	str	(p.value(	x3165	)))
filepoint.writelines	('\tx3166	'+	str	(p.value(	x3166	)))
filepoint.writelines	('\tx3167	'+	str	(p.value(	x3167	)))
filepoint.writelines	('\tx3168	'+	str	(p.value(	x3168	)))
filepoint.writelines	('\tx3169	'+	str	(p.value(	x3169	)))
filepoint.writelines	('\tx3170	'+	str	(p.value(	x3170	)))
filepoint.writelines	('\tx3171	'+	str	(p.value(	x3171	)))
filepoint.writelines	('\tx3172	'+	str	(p.value(	x3172	)))
filepoint.writelines	('\tx3173	'+	str	(p.value(	x3173	)))
filepoint.writelines	('\tx3174	'+	str	(p.value(	x3174	)))
filepoint.writelines	('\tx3175	'+	str	(p.value(	x3175	)))
filepoint.writelines	('\tx3176	'+	str	(p.value(	x3176	)))
filepoint.writelines	('\tx3177	'+	str	(p.value(	x3177	)))
filepoint.writelines	('\tx3178	'+	str	(p.value(	x3178	)))
filepoint.writelines	('\tx3179	'+	str	(p.value(	x3179	)))
filepoint.writelines	('\tx3180	'+	str	(p.value(	x3180	)))
filepoint.writelines	('\tx3181	'+	str	(p.value(	x3181	)))
filepoint.writelines	('\tx3182	'+	str	(p.value(	x3182	)))
filepoint.writelines	('\tx3183	'+	str	(p.value(	x3183	)))
filepoint.writelines	('\tx3184	'+	str	(p.value(	x3184	)))
filepoint.writelines	('\tx3185	'+	str	(p.value(	x3185	)))
filepoint.writelines	('\tx3186	'+	str	(p.value(	x3186	)))
filepoint.writelines	('\tx3187	'+	str	(p.value(	x3187	)))
filepoint.writelines	('\tx3188	'+	str	(p.value(	x3188	)))
filepoint.writelines	('\tx3189	'+	str	(p.value(	x3189	)))
filepoint.writelines	('\tx3190	'+	str	(p.value(	x3190	)))
filepoint.writelines	('\tx3191	'+	str	(p.value(	x3191	)))
filepoint.writelines	('\tx3192	'+	str	(p.value(	x3192	)))
filepoint.writelines	('\tx3193	'+	str	(p.value(	x3193	)))
filepoint.writelines	('\tx3194	'+	str	(p.value(	x3194	)))
filepoint.writelines	('\tx3195	'+	str	(p.value(	x3195	)))
filepoint.writelines	('\tx3196	'+	str	(p.value(	x3196	)))
filepoint.writelines	('\tx3197	'+	str	(p.value(	x3197	)))
filepoint.writelines	('\tx3198	'+	str	(p.value(	x3198	)))
filepoint.writelines	('\tx3199	'+	str	(p.value(	x3199	)))
filepoint.writelines	('\tx3200	'+	str	(p.value(	x3200	)))
filepoint.writelines	('\tx3201	'+	str	(p.value(	x3201	)))
filepoint.writelines	('\tx3202	'+	str	(p.value(	x3202	)))
filepoint.writelines	('\tx3203	'+	str	(p.value(	x3203	)))
filepoint.writelines	('\tx3204	'+	str	(p.value(	x3204	)))
filepoint.writelines	('\tx3205	'+	str	(p.value(	x3205	)))
filepoint.writelines	('\tx3206	'+	str	(p.value(	x3206	)))
filepoint.writelines	('\tx3207	'+	str	(p.value(	x3207	)))
filepoint.writelines	('\tx3208	'+	str	(p.value(	x3208	)))
filepoint.writelines	('\tx3209	'+	str	(p.value(	x3209	)))
filepoint.writelines	('\tx3210	'+	str	(p.value(	x3210	)))
filepoint.writelines	('\tx3211	'+	str	(p.value(	x3211	)))
filepoint.writelines	('\tx3212	'+	str	(p.value(	x3212	)))
filepoint.writelines	('\tx3213	'+	str	(p.value(	x3213	)))
filepoint.writelines	('\tx3214	'+	str	(p.value(	x3214	)))
filepoint.writelines	('\tx3215	'+	str	(p.value(	x3215	)))
filepoint.writelines	('\tx3216	'+	str	(p.value(	x3216	)))
filepoint.writelines	('\tx3217	'+	str	(p.value(	x3217	)))
filepoint.writelines	('\tx3218	'+	str	(p.value(	x3218	)))
filepoint.writelines	('\tx3219	'+	str	(p.value(	x3219	)))
filepoint.writelines	('\tx3220	'+	str	(p.value(	x3220	)))
filepoint.writelines	('\tx3221	'+	str	(p.value(	x3221	)))
filepoint.writelines	('\tx3222	'+	str	(p.value(	x3222	)))
filepoint.writelines	('\tx3223	'+	str	(p.value(	x3223	)))
filepoint.writelines	('\tx3224	'+	str	(p.value(	x3224	)))
filepoint.writelines	('\tx3225	'+	str	(p.value(	x3225	)))
filepoint.writelines	('\tx3226	'+	str	(p.value(	x3226	)))
filepoint.writelines	('\tx3227	'+	str	(p.value(	x3227	)))
filepoint.writelines	('\tx3228	'+	str	(p.value(	x3228	)))
filepoint.writelines	('\tx3229	'+	str	(p.value(	x3229	)))
filepoint.writelines	('\tx3230	'+	str	(p.value(	x3230	)))
filepoint.writelines	('\tx3231	'+	str	(p.value(	x3231	)))
filepoint.writelines	('\tx3232	'+	str	(p.value(	x3232	)))
filepoint.writelines	('\tx3233	'+	str	(p.value(	x3233	)))
filepoint.writelines	('\tx3234	'+	str	(p.value(	x3234	)))
filepoint.writelines	('\tx3235	'+	str	(p.value(	x3235	)))
filepoint.writelines	('\tx3236	'+	str	(p.value(	x3236	)))
filepoint.writelines	('\tx3237	'+	str	(p.value(	x3237	)))
filepoint.writelines	('\tx3238	'+	str	(p.value(	x3238	)))
filepoint.writelines	('\tx3239	'+	str	(p.value(	x3239	)))
filepoint.writelines	('\tx3240	'+	str	(p.value(	x3240	)))
filepoint.writelines	('\tx3241	'+	str	(p.value(	x3241	)))
filepoint.writelines	('\tx3242	'+	str	(p.value(	x3242	)))
filepoint.writelines	('\tx3243	'+	str	(p.value(	x3243	)))
filepoint.writelines	('\tx3244	'+	str	(p.value(	x3244	)))
filepoint.writelines	('\tx3245	'+	str	(p.value(	x3245	)))
filepoint.writelines	('\tx3246	'+	str	(p.value(	x3246	)))
filepoint.writelines	('\tx3247	'+	str	(p.value(	x3247	)))
filepoint.writelines	('\tx3248	'+	str	(p.value(	x3248	)))
filepoint.writelines	('\tx3249	'+	str	(p.value(	x3249	)))
filepoint.writelines	('\tx3250	'+	str	(p.value(	x3250	)))
filepoint.writelines	('\tx3251	'+	str	(p.value(	x3251	)))
filepoint.writelines	('\tx3252	'+	str	(p.value(	x3252	)))
filepoint.writelines	('\tx3253	'+	str	(p.value(	x3253	)))
filepoint.writelines	('\tx3254	'+	str	(p.value(	x3254	)))
filepoint.writelines	('\tx3255	'+	str	(p.value(	x3255	)))
filepoint.writelines	('\tx3256	'+	str	(p.value(	x3256	)))
filepoint.writelines	('\tx3257	'+	str	(p.value(	x3257	)))
filepoint.writelines	('\tx3258	'+	str	(p.value(	x3258	)))
filepoint.writelines	('\tx3259	'+	str	(p.value(	x3259	)))
filepoint.writelines	('\tx3260	'+	str	(p.value(	x3260	)))
filepoint.writelines	('\tx3261	'+	str	(p.value(	x3261	)))
filepoint.writelines	('\tx3262	'+	str	(p.value(	x3262	)))
filepoint.writelines	('\tx3263	'+	str	(p.value(	x3263	)))
filepoint.writelines	('\tx3264	'+	str	(p.value(	x3264	)))
filepoint.writelines	('\tx3265	'+	str	(p.value(	x3265	)))
filepoint.writelines	('\tx3266	'+	str	(p.value(	x3266	)))
filepoint.writelines	('\tx3267	'+	str	(p.value(	x3267	)))
filepoint.writelines	('\tx3268	'+	str	(p.value(	x3268	)))
filepoint.writelines	('\tx3269	'+	str	(p.value(	x3269	)))
filepoint.writelines	('\tx3270	'+	str	(p.value(	x3270	)))
filepoint.writelines	('\tx3271	'+	str	(p.value(	x3271	)))
filepoint.writelines	('\tx3272	'+	str	(p.value(	x3272	)))
filepoint.writelines	('\tx3273	'+	str	(p.value(	x3273	)))
filepoint.writelines	('\tx3274	'+	str	(p.value(	x3274	)))
filepoint.writelines	('\tx3275	'+	str	(p.value(	x3275	)))
filepoint.writelines	('\tx3276	'+	str	(p.value(	x3276	)))
filepoint.writelines	('\tx3277	'+	str	(p.value(	x3277	)))
filepoint.writelines	('\tx3278	'+	str	(p.value(	x3278	)))
filepoint.writelines	('\tx3279	'+	str	(p.value(	x3279	)))
filepoint.writelines	('\tx3280	'+	str	(p.value(	x3280	)))
filepoint.writelines	('\tx3281	'+	str	(p.value(	x3281	)))
filepoint.writelines	('\tx3282	'+	str	(p.value(	x3282	)))
filepoint.writelines	('\tx3283	'+	str	(p.value(	x3283	)))
filepoint.writelines	('\tx3284	'+	str	(p.value(	x3284	)))
filepoint.writelines	('\tx3285	'+	str	(p.value(	x3285	)))
filepoint.writelines	('\tx3286	'+	str	(p.value(	x3286	)))
filepoint.writelines	('\tx3287	'+	str	(p.value(	x3287	)))
filepoint.writelines	('\tx3288	'+	str	(p.value(	x3288	)))
filepoint.writelines	('\tx3289	'+	str	(p.value(	x3289	)))
filepoint.writelines	('\tx3290	'+	str	(p.value(	x3290	)))
filepoint.writelines	('\tx3291	'+	str	(p.value(	x3291	)))
filepoint.writelines	('\tx3292	'+	str	(p.value(	x3292	)))
filepoint.writelines	('\tx3293	'+	str	(p.value(	x3293	)))
filepoint.writelines	('\tx3294	'+	str	(p.value(	x3294	)))
filepoint.writelines	('\tx3295	'+	str	(p.value(	x3295	)))
filepoint.writelines	('\tx3296	'+	str	(p.value(	x3296	)))
filepoint.writelines	('\tx3297	'+	str	(p.value(	x3297	)))
filepoint.writelines	('\tx3298	'+	str	(p.value(	x3298	)))
filepoint.writelines	('\tx3299	'+	str	(p.value(	x3299	)))
filepoint.writelines	('\tx3300	'+	str	(p.value(	x3300	)))
filepoint.writelines	('\tx3301	'+	str	(p.value(	x3301	)))
filepoint.writelines	('\tx3302	'+	str	(p.value(	x3302	)))
filepoint.writelines	('\tx3303	'+	str	(p.value(	x3303	)))
filepoint.writelines	('\tx3304	'+	str	(p.value(	x3304	)))
filepoint.writelines	('\tx3305	'+	str	(p.value(	x3305	)))
filepoint.writelines	('\tx3306	'+	str	(p.value(	x3306	)))
filepoint.writelines	('\tx3307	'+	str	(p.value(	x3307	)))
filepoint.writelines	('\tx3308	'+	str	(p.value(	x3308	)))
filepoint.writelines	('\tx3309	'+	str	(p.value(	x3309	)))
filepoint.writelines	('\tx3310	'+	str	(p.value(	x3310	)))
filepoint.writelines	('\tx3311	'+	str	(p.value(	x3311	)))
filepoint.writelines	('\tx3312	'+	str	(p.value(	x3312	)))
filepoint.writelines	('\tx3313	'+	str	(p.value(	x3313	)))
filepoint.writelines	('\tx3314	'+	str	(p.value(	x3314	)))
filepoint.writelines	('\tx3315	'+	str	(p.value(	x3315	)))
filepoint.writelines	('\tx3316	'+	str	(p.value(	x3316	)))
filepoint.writelines	('\tx3317	'+	str	(p.value(	x3317	)))
filepoint.writelines	('\tx3318	'+	str	(p.value(	x3318	)))
filepoint.writelines	('\tx3319	'+	str	(p.value(	x3319	)))
filepoint.writelines	('\tx3320	'+	str	(p.value(	x3320	)))
filepoint.writelines	('\tx3321	'+	str	(p.value(	x3321	)))
filepoint.writelines	('\tx3322	'+	str	(p.value(	x3322	)))
filepoint.writelines	('\tx3323	'+	str	(p.value(	x3323	)))
filepoint.writelines	('\tx3324	'+	str	(p.value(	x3324	)))
filepoint.writelines	('\tx3325	'+	str	(p.value(	x3325	)))
filepoint.writelines	('\tx3326	'+	str	(p.value(	x3326	)))
filepoint.writelines	('\tx3327	'+	str	(p.value(	x3327	)))
filepoint.writelines	('\tx3328	'+	str	(p.value(	x3328	)))
filepoint.writelines	('\tx3329	'+	str	(p.value(	x3329	)))
filepoint.writelines	('\tx3330	'+	str	(p.value(	x3330	)))
filepoint.writelines	('\tx3331	'+	str	(p.value(	x3331	)))
filepoint.writelines	('\tx3332	'+	str	(p.value(	x3332	)))
filepoint.writelines	('\tx3333	'+	str	(p.value(	x3333	)))
filepoint.writelines	('\tx3334	'+	str	(p.value(	x3334	)))
filepoint.writelines	('\tx3335	'+	str	(p.value(	x3335	)))
filepoint.writelines	('\tx3336	'+	str	(p.value(	x3336	)))
filepoint.writelines	('\tx3337	'+	str	(p.value(	x3337	)))
filepoint.writelines	('\tx3338	'+	str	(p.value(	x3338	)))
filepoint.writelines	('\tx3339	'+	str	(p.value(	x3339	)))
filepoint.writelines	('\tx3340	'+	str	(p.value(	x3340	)))
filepoint.writelines	('\tx3341	'+	str	(p.value(	x3341	)))
filepoint.writelines	('\tx3342	'+	str	(p.value(	x3342	)))
filepoint.writelines	('\tx3343	'+	str	(p.value(	x3343	)))
filepoint.writelines	('\tx3344	'+	str	(p.value(	x3344	)))
filepoint.writelines	('\tx3345	'+	str	(p.value(	x3345	)))
filepoint.writelines	('\tx3346	'+	str	(p.value(	x3346	)))
filepoint.writelines	('\tx3347	'+	str	(p.value(	x3347	)))
filepoint.writelines	('\tx3348	'+	str	(p.value(	x3348	)))
filepoint.writelines	('\tx3349	'+	str	(p.value(	x3349	)))
filepoint.writelines	('\tx3350	'+	str	(p.value(	x3350	)))
filepoint.writelines	('\tx3351	'+	str	(p.value(	x3351	)))
filepoint.writelines	('\tx3352	'+	str	(p.value(	x3352	)))
filepoint.writelines	('\tx3353	'+	str	(p.value(	x3353	)))
filepoint.writelines	('\tx3354	'+	str	(p.value(	x3354	)))
filepoint.writelines	('\tx3355	'+	str	(p.value(	x3355	)))
filepoint.writelines	('\tx3356	'+	str	(p.value(	x3356	)))
filepoint.writelines	('\tx3357	'+	str	(p.value(	x3357	)))
filepoint.writelines	('\tx3358	'+	str	(p.value(	x3358	)))
filepoint.writelines	('\tx3359	'+	str	(p.value(	x3359	)))
filepoint.writelines	('\tx3360	'+	str	(p.value(	x3360	)))
filepoint.writelines	('\tx3361	'+	str	(p.value(	x3361	)))
filepoint.writelines	('\tx3362	'+	str	(p.value(	x3362	)))
filepoint.writelines	('\tx3363	'+	str	(p.value(	x3363	)))
filepoint.writelines	('\tx3364	'+	str	(p.value(	x3364	)))
filepoint.writelines	('\tx3365	'+	str	(p.value(	x3365	)))
filepoint.writelines	('\tx3366	'+	str	(p.value(	x3366	)))
filepoint.writelines	('\tx3367	'+	str	(p.value(	x3367	)))
filepoint.writelines	('\tx3368	'+	str	(p.value(	x3368	)))
filepoint.writelines	('\tx3369	'+	str	(p.value(	x3369	)))
filepoint.writelines	('\tx3370	'+	str	(p.value(	x3370	)))
filepoint.writelines	('\tx3371	'+	str	(p.value(	x3371	)))
filepoint.writelines	('\tx3372	'+	str	(p.value(	x3372	)))
filepoint.writelines	('\tx3373	'+	str	(p.value(	x3373	)))
filepoint.writelines	('\tx3374	'+	str	(p.value(	x3374	)))
filepoint.writelines	('\tx3375	'+	str	(p.value(	x3375	)))
filepoint.writelines	('\tx3376	'+	str	(p.value(	x3376	)))
filepoint.writelines	('\tx3377	'+	str	(p.value(	x3377	)))
filepoint.writelines	('\tx3378	'+	str	(p.value(	x3378	)))
filepoint.writelines	('\tx3379	'+	str	(p.value(	x3379	)))
filepoint.writelines	('\tx3380	'+	str	(p.value(	x3380	)))
filepoint.writelines	('\tx3381	'+	str	(p.value(	x3381	)))
filepoint.writelines	('\tx3382	'+	str	(p.value(	x3382	)))
filepoint.writelines	('\tx3383	'+	str	(p.value(	x3383	)))
filepoint.writelines	('\tx3384	'+	str	(p.value(	x3384	)))
filepoint.writelines	('\tx3385	'+	str	(p.value(	x3385	)))
filepoint.writelines	('\tx3386	'+	str	(p.value(	x3386	)))
filepoint.writelines	('\tx3387	'+	str	(p.value(	x3387	)))
filepoint.writelines	('\tx3388	'+	str	(p.value(	x3388	)))
filepoint.writelines	('\tx3389	'+	str	(p.value(	x3389	)))
filepoint.writelines	('\tx3390	'+	str	(p.value(	x3390	)))
filepoint.writelines	('\tx3391	'+	str	(p.value(	x3391	)))
filepoint.writelines	('\tx3392	'+	str	(p.value(	x3392	)))
filepoint.writelines	('\tx3393	'+	str	(p.value(	x3393	)))
filepoint.writelines	('\tx3394	'+	str	(p.value(	x3394	)))
filepoint.writelines	('\tx3395	'+	str	(p.value(	x3395	)))
filepoint.writelines	('\tx3396	'+	str	(p.value(	x3396	)))
filepoint.writelines	('\tx3397	'+	str	(p.value(	x3397	)))
filepoint.writelines	('\tx3398	'+	str	(p.value(	x3398	)))
filepoint.writelines	('\tx3399	'+	str	(p.value(	x3399	)))
filepoint.writelines	('\tx3400	'+	str	(p.value(	x3400	)))
filepoint.writelines	('\tx3401	'+	str	(p.value(	x3401	)))
filepoint.writelines	('\tx3402	'+	str	(p.value(	x3402	)))
filepoint.writelines	('\tx3403	'+	str	(p.value(	x3403	)))
filepoint.writelines	('\tx3404	'+	str	(p.value(	x3404	)))
filepoint.writelines	('\tx3405	'+	str	(p.value(	x3405	)))
filepoint.writelines	('\tx3406	'+	str	(p.value(	x3406	)))
filepoint.writelines	('\tx3407	'+	str	(p.value(	x3407	)))
filepoint.writelines	('\tx3408	'+	str	(p.value(	x3408	)))
filepoint.writelines	('\tx3409	'+	str	(p.value(	x3409	)))
filepoint.writelines	('\tx3410	'+	str	(p.value(	x3410	)))
filepoint.writelines	('\tx3411	'+	str	(p.value(	x3411	)))
filepoint.writelines	('\tx3412	'+	str	(p.value(	x3412	)))
filepoint.writelines	('\tx3413	'+	str	(p.value(	x3413	)))
filepoint.writelines	('\tx3414	'+	str	(p.value(	x3414	)))
filepoint.writelines	('\tx3415	'+	str	(p.value(	x3415	)))
filepoint.writelines	('\tx3416	'+	str	(p.value(	x3416	)))
filepoint.writelines	('\tx3417	'+	str	(p.value(	x3417	)))
filepoint.writelines	('\tx3418	'+	str	(p.value(	x3418	)))
filepoint.writelines	('\tx3419	'+	str	(p.value(	x3419	)))
filepoint.writelines	('\tx3420	'+	str	(p.value(	x3420	)))
filepoint.writelines	('\tx3421	'+	str	(p.value(	x3421	)))
filepoint.writelines	('\tx3422	'+	str	(p.value(	x3422	)))
filepoint.writelines	('\tx3423	'+	str	(p.value(	x3423	)))
filepoint.writelines	('\tx3424	'+	str	(p.value(	x3424	)))
filepoint.writelines	('\tx3425	'+	str	(p.value(	x3425	)))
filepoint.writelines	('\tx3426	'+	str	(p.value(	x3426	)))
filepoint.writelines	('\tx3427	'+	str	(p.value(	x3427	)))
filepoint.writelines	('\tx3428	'+	str	(p.value(	x3428	)))
filepoint.writelines	('\tx3429	'+	str	(p.value(	x3429	)))
filepoint.writelines	('\tx3430	'+	str	(p.value(	x3430	)))
filepoint.writelines	('\tx3431	'+	str	(p.value(	x3431	)))
filepoint.writelines	('\tx3432	'+	str	(p.value(	x3432	)))
filepoint.writelines	('\tx3433	'+	str	(p.value(	x3433	)))
filepoint.writelines	('\tx3434	'+	str	(p.value(	x3434	)))
filepoint.writelines	('\tx3435	'+	str	(p.value(	x3435	)))
filepoint.writelines	('\tx3436	'+	str	(p.value(	x3436	)))
filepoint.writelines	('\tx3437	'+	str	(p.value(	x3437	)))
filepoint.writelines	('\tx3438	'+	str	(p.value(	x3438	)))
filepoint.writelines	('\tx3439	'+	str	(p.value(	x3439	)))
filepoint.writelines	('\tx3440	'+	str	(p.value(	x3440	)))
filepoint.writelines	('\tx3441	'+	str	(p.value(	x3441	)))
filepoint.writelines	('\tx3442	'+	str	(p.value(	x3442	)))
filepoint.writelines	('\tx3443	'+	str	(p.value(	x3443	)))
filepoint.writelines	('\tx3444	'+	str	(p.value(	x3444	)))
filepoint.writelines	('\tx3445	'+	str	(p.value(	x3445	)))
filepoint.writelines	('\tx3446	'+	str	(p.value(	x3446	)))
filepoint.writelines	('\tx3447	'+	str	(p.value(	x3447	)))
filepoint.writelines	('\tx3448	'+	str	(p.value(	x3448	)))
filepoint.writelines	('\tx3449	'+	str	(p.value(	x3449	)))
filepoint.writelines	('\tx3450	'+	str	(p.value(	x3450	)))
filepoint.writelines	('\tx3451	'+	str	(p.value(	x3451	)))
filepoint.writelines	('\tx3452	'+	str	(p.value(	x3452	)))
filepoint.writelines	('\tx3453	'+	str	(p.value(	x3453	)))
filepoint.writelines	('\tx3454	'+	str	(p.value(	x3454	)))
filepoint.writelines	('\tx3455	'+	str	(p.value(	x3455	)))
filepoint.writelines	('\tx3456	'+	str	(p.value(	x3456	)))
filepoint.writelines	('\tx3457	'+	str	(p.value(	x3457	)))
filepoint.writelines	('\tx3458	'+	str	(p.value(	x3458	)))
filepoint.writelines	('\tx3459	'+	str	(p.value(	x3459	)))
filepoint.writelines	('\tx3460	'+	str	(p.value(	x3460	)))
filepoint.writelines	('\tx3461	'+	str	(p.value(	x3461	)))
filepoint.writelines	('\tx3462	'+	str	(p.value(	x3462	)))
filepoint.writelines	('\tx3463	'+	str	(p.value(	x3463	)))
filepoint.writelines	('\tx3464	'+	str	(p.value(	x3464	)))
filepoint.writelines	('\tx3465	'+	str	(p.value(	x3465	)))
filepoint.writelines	('\tx3466	'+	str	(p.value(	x3466	)))
filepoint.writelines	('\tx3467	'+	str	(p.value(	x3467	)))
filepoint.writelines	('\tx3468	'+	str	(p.value(	x3468	)))
filepoint.writelines	('\tx3469	'+	str	(p.value(	x3469	)))
filepoint.writelines	('\tx3470	'+	str	(p.value(	x3470	)))
filepoint.writelines	('\tx3471	'+	str	(p.value(	x3471	)))
filepoint.writelines	('\tx3472	'+	str	(p.value(	x3472	)))
filepoint.writelines	('\tx3473	'+	str	(p.value(	x3473	)))
filepoint.writelines	('\tx3474	'+	str	(p.value(	x3474	)))
filepoint.writelines	('\tx3475	'+	str	(p.value(	x3475	)))
filepoint.writelines	('\tx3476	'+	str	(p.value(	x3476	)))
filepoint.writelines	('\tx3477	'+	str	(p.value(	x3477	)))
filepoint.writelines	('\tx3478	'+	str	(p.value(	x3478	)))
filepoint.writelines	('\tx3479	'+	str	(p.value(	x3479	)))
filepoint.writelines	('\tx3480	'+	str	(p.value(	x3480	)))
filepoint.writelines	('\tx3481	'+	str	(p.value(	x3481	)))
filepoint.writelines	('\tx3482	'+	str	(p.value(	x3482	)))
filepoint.writelines	('\tx3483	'+	str	(p.value(	x3483	)))
filepoint.writelines	('\tx3484	'+	str	(p.value(	x3484	)))
filepoint.writelines	('\tx3485	'+	str	(p.value(	x3485	)))
filepoint.writelines	('\tx3486	'+	str	(p.value(	x3486	)))
filepoint.writelines	('\tx3487	'+	str	(p.value(	x3487	)))
filepoint.writelines	('\tx3488	'+	str	(p.value(	x3488	)))
filepoint.writelines	('\tx3489	'+	str	(p.value(	x3489	)))
filepoint.writelines	('\tx3490	'+	str	(p.value(	x3490	)))
filepoint.writelines	('\tx3491	'+	str	(p.value(	x3491	)))
filepoint.writelines	('\tx3492	'+	str	(p.value(	x3492	)))
filepoint.writelines	('\tx3493	'+	str	(p.value(	x3493	)))
filepoint.writelines	('\tx3494	'+	str	(p.value(	x3494	)))
filepoint.writelines	('\tx3495	'+	str	(p.value(	x3495	)))
filepoint.writelines	('\tx3496	'+	str	(p.value(	x3496	)))
filepoint.writelines	('\tx3497	'+	str	(p.value(	x3497	)))
filepoint.writelines	('\tx3498	'+	str	(p.value(	x3498	)))
filepoint.writelines	('\tx3499	'+	str	(p.value(	x3499	)))
filepoint.writelines	('\tx3500	'+	str	(p.value(	x3500	)))
filepoint.writelines	('\tx3501	'+	str	(p.value(	x3501	)))
filepoint.writelines	('\tx3502	'+	str	(p.value(	x3502	)))
filepoint.writelines	('\tx3503	'+	str	(p.value(	x3503	)))
filepoint.writelines	('\tx3504	'+	str	(p.value(	x3504	)))
filepoint.writelines	('\tx3505	'+	str	(p.value(	x3505	)))
filepoint.writelines	('\tx3506	'+	str	(p.value(	x3506	)))
filepoint.writelines	('\tx3507	'+	str	(p.value(	x3507	)))
filepoint.writelines	('\tx3508	'+	str	(p.value(	x3508	)))
filepoint.writelines	('\tx3509	'+	str	(p.value(	x3509	)))
filepoint.writelines	('\tx3510	'+	str	(p.value(	x3510	)))
filepoint.writelines	('\tx3511	'+	str	(p.value(	x3511	)))
filepoint.writelines	('\tx3512	'+	str	(p.value(	x3512	)))
filepoint.writelines	('\tx3513	'+	str	(p.value(	x3513	)))
filepoint.writelines	('\tx3514	'+	str	(p.value(	x3514	)))
filepoint.writelines	('\tx3515	'+	str	(p.value(	x3515	)))
filepoint.writelines	('\tx3516	'+	str	(p.value(	x3516	)))
filepoint.writelines	('\tx3517	'+	str	(p.value(	x3517	)))
filepoint.writelines	('\tx3518	'+	str	(p.value(	x3518	)))
filepoint.writelines	('\tx3519	'+	str	(p.value(	x3519	)))
filepoint.writelines	('\tx3520	'+	str	(p.value(	x3520	)))
filepoint.writelines	('\tx3521	'+	str	(p.value(	x3521	)))
filepoint.writelines	('\tx3522	'+	str	(p.value(	x3522	)))
filepoint.writelines	('\tx3523	'+	str	(p.value(	x3523	)))
filepoint.writelines	('\tx3524	'+	str	(p.value(	x3524	)))
filepoint.writelines	('\tx3525	'+	str	(p.value(	x3525	)))
filepoint.writelines	('\tx3526	'+	str	(p.value(	x3526	)))
filepoint.writelines	('\tx3527	'+	str	(p.value(	x3527	)))
filepoint.writelines	('\tx3528	'+	str	(p.value(	x3528	)))
filepoint.writelines	('\tx3529	'+	str	(p.value(	x3529	)))
filepoint.writelines	('\tx3530	'+	str	(p.value(	x3530	)))
filepoint.writelines	('\tx3531	'+	str	(p.value(	x3531	)))
filepoint.writelines	('\tx3532	'+	str	(p.value(	x3532	)))
filepoint.writelines	('\tx3533	'+	str	(p.value(	x3533	)))
filepoint.writelines	('\tx3534	'+	str	(p.value(	x3534	)))
filepoint.writelines	('\tx3535	'+	str	(p.value(	x3535	)))
filepoint.writelines	('\tx3536	'+	str	(p.value(	x3536	)))
filepoint.writelines	('\tx3537	'+	str	(p.value(	x3537	)))
filepoint.writelines	('\tx3538	'+	str	(p.value(	x3538	)))
filepoint.writelines	('\tx3539	'+	str	(p.value(	x3539	)))
filepoint.writelines	('\tx3540	'+	str	(p.value(	x3540	)))
filepoint.writelines	('\tx3541	'+	str	(p.value(	x3541	)))
filepoint.writelines	('\tx3542	'+	str	(p.value(	x3542	)))
filepoint.writelines	('\tx3543	'+	str	(p.value(	x3543	)))
filepoint.writelines	('\tx3544	'+	str	(p.value(	x3544	)))
filepoint.writelines	('\tx3545	'+	str	(p.value(	x3545	)))
filepoint.writelines	('\tx3546	'+	str	(p.value(	x3546	)))
filepoint.writelines	('\tx3547	'+	str	(p.value(	x3547	)))
filepoint.writelines	('\tx3548	'+	str	(p.value(	x3548	)))
filepoint.writelines	('\tx3549	'+	str	(p.value(	x3549	)))
filepoint.writelines	('\tx3550	'+	str	(p.value(	x3550	)))
filepoint.writelines	('\tx3551	'+	str	(p.value(	x3551	)))
filepoint.writelines	('\tx3552	'+	str	(p.value(	x3552	)))
filepoint.writelines	('\tx3553	'+	str	(p.value(	x3553	)))
filepoint.writelines	('\tx3554	'+	str	(p.value(	x3554	)))
filepoint.writelines	('\tx3555	'+	str	(p.value(	x3555	)))
filepoint.writelines	('\tx3556	'+	str	(p.value(	x3556	)))
filepoint.writelines	('\tx3557	'+	str	(p.value(	x3557	)))
filepoint.writelines	('\tx3558	'+	str	(p.value(	x3558	)))
filepoint.writelines	('\tx3559	'+	str	(p.value(	x3559	)))
filepoint.writelines	('\tx3560	'+	str	(p.value(	x3560	)))
filepoint.writelines	('\tx3561	'+	str	(p.value(	x3561	)))
filepoint.writelines	('\tx3562	'+	str	(p.value(	x3562	)))
filepoint.writelines	('\tx3563	'+	str	(p.value(	x3563	)))
filepoint.writelines	('\tx3564	'+	str	(p.value(	x3564	)))
filepoint.writelines	('\tx3565	'+	str	(p.value(	x3565	)))
filepoint.writelines	('\tx3566	'+	str	(p.value(	x3566	)))
filepoint.writelines	('\tx3567	'+	str	(p.value(	x3567	)))
filepoint.writelines	('\tx3568	'+	str	(p.value(	x3568	)))
filepoint.writelines	('\tx3569	'+	str	(p.value(	x3569	)))
filepoint.writelines	('\tx3570	'+	str	(p.value(	x3570	)))
filepoint.writelines	('\tx3571	'+	str	(p.value(	x3571	)))
filepoint.writelines	('\tx3572	'+	str	(p.value(	x3572	)))
filepoint.writelines	('\tx3573	'+	str	(p.value(	x3573	)))
filepoint.writelines	('\tx3574	'+	str	(p.value(	x3574	)))
filepoint.writelines	('\tx3575	'+	str	(p.value(	x3575	)))
filepoint.writelines	('\tx3576	'+	str	(p.value(	x3576	)))
filepoint.writelines	('\tx3577	'+	str	(p.value(	x3577	)))
filepoint.writelines	('\tx3578	'+	str	(p.value(	x3578	)))
filepoint.writelines	('\tx3579	'+	str	(p.value(	x3579	)))
filepoint.writelines	('\tx3580	'+	str	(p.value(	x3580	)))
filepoint.writelines	('\tx3581	'+	str	(p.value(	x3581	)))
filepoint.writelines	('\tx3582	'+	str	(p.value(	x3582	)))
filepoint.writelines	('\tx3583	'+	str	(p.value(	x3583	)))
filepoint.writelines	('\tx3584	'+	str	(p.value(	x3584	)))
filepoint.writelines	('\tx3585	'+	str	(p.value(	x3585	)))
filepoint.writelines	('\tx3586	'+	str	(p.value(	x3586	)))
filepoint.writelines	('\tx3587	'+	str	(p.value(	x3587	)))
filepoint.writelines	('\tx3588	'+	str	(p.value(	x3588	)))
filepoint.writelines	('\tx3589	'+	str	(p.value(	x3589	)))
filepoint.writelines	('\tx3590	'+	str	(p.value(	x3590	)))
filepoint.writelines	('\tx3591	'+	str	(p.value(	x3591	)))
filepoint.writelines	('\tx3592	'+	str	(p.value(	x3592	)))
filepoint.writelines	('\tx3593	'+	str	(p.value(	x3593	)))
filepoint.writelines	('\tx3594	'+	str	(p.value(	x3594	)))
filepoint.writelines	('\tx3595	'+	str	(p.value(	x3595	)))
filepoint.writelines	('\tx3596	'+	str	(p.value(	x3596	)))
filepoint.writelines	('\tx3597	'+	str	(p.value(	x3597	)))
filepoint.writelines	('\tx3598	'+	str	(p.value(	x3598	)))
filepoint.writelines	('\tx3599	'+	str	(p.value(	x3599	)))
filepoint.writelines	('\tx3600	'+	str	(p.value(	x3600	)))
filepoint.writelines	('\tx3601	'+	str	(p.value(	x3601	)))
filepoint.writelines	('\tx3602	'+	str	(p.value(	x3602	)))
filepoint.writelines	('\tx3603	'+	str	(p.value(	x3603	)))
filepoint.writelines	('\tx3604	'+	str	(p.value(	x3604	)))
filepoint.writelines	('\tx3605	'+	str	(p.value(	x3605	)))
filepoint.writelines	('\tx3606	'+	str	(p.value(	x3606	)))
filepoint.writelines	('\tx3607	'+	str	(p.value(	x3607	)))
filepoint.writelines	('\tx3608	'+	str	(p.value(	x3608	)))
filepoint.writelines	('\tx3609	'+	str	(p.value(	x3609	)))
filepoint.writelines	('\tx3610	'+	str	(p.value(	x3610	)))
filepoint.writelines	('\tx3611	'+	str	(p.value(	x3611	)))
filepoint.writelines	('\tx3612	'+	str	(p.value(	x3612	)))
filepoint.writelines	('\tx3613	'+	str	(p.value(	x3613	)))
filepoint.writelines	('\tx3614	'+	str	(p.value(	x3614	)))
filepoint.writelines	('\tx3615	'+	str	(p.value(	x3615	)))
filepoint.writelines	('\tx3616	'+	str	(p.value(	x3616	)))
filepoint.writelines	('\tx3617	'+	str	(p.value(	x3617	)))
filepoint.writelines	('\tx3618	'+	str	(p.value(	x3618	)))
filepoint.writelines	('\tx3619	'+	str	(p.value(	x3619	)))
filepoint.writelines	('\tx3620	'+	str	(p.value(	x3620	)))
filepoint.writelines	('\tx3621	'+	str	(p.value(	x3621	)))
filepoint.writelines	('\tx3622	'+	str	(p.value(	x3622	)))
filepoint.writelines	('\tx3623	'+	str	(p.value(	x3623	)))
filepoint.writelines	('\tx3624	'+	str	(p.value(	x3624	)))
filepoint.writelines	('\tx3625	'+	str	(p.value(	x3625	)))
filepoint.writelines	('\tx3626	'+	str	(p.value(	x3626	)))
filepoint.writelines	('\tx3627	'+	str	(p.value(	x3627	)))
filepoint.writelines	('\tx3628	'+	str	(p.value(	x3628	)))
filepoint.writelines	('\tx3629	'+	str	(p.value(	x3629	)))
filepoint.writelines	('\tx3630	'+	str	(p.value(	x3630	)))
filepoint.writelines	('\tx3631	'+	str	(p.value(	x3631	)))
filepoint.writelines	('\tx3632	'+	str	(p.value(	x3632	)))
filepoint.writelines	('\tx3633	'+	str	(p.value(	x3633	)))
filepoint.writelines	('\tx3634	'+	str	(p.value(	x3634	)))
filepoint.writelines	('\tx3635	'+	str	(p.value(	x3635	)))
filepoint.writelines	('\tx3636	'+	str	(p.value(	x3636	)))
filepoint.writelines	('\tx3637	'+	str	(p.value(	x3637	)))
filepoint.writelines	('\tx3638	'+	str	(p.value(	x3638	)))
filepoint.writelines	('\tx3639	'+	str	(p.value(	x3639	)))
filepoint.writelines	('\tx3640	'+	str	(p.value(	x3640	)))
filepoint.writelines	('\tx3641	'+	str	(p.value(	x3641	)))
filepoint.writelines	('\tx3642	'+	str	(p.value(	x3642	)))
filepoint.writelines	('\tx3643	'+	str	(p.value(	x3643	)))
filepoint.writelines	('\tx3644	'+	str	(p.value(	x3644	)))
filepoint.writelines	('\tx3645	'+	str	(p.value(	x3645	)))
filepoint.writelines	('\tx3646	'+	str	(p.value(	x3646	)))
filepoint.writelines	('\tx3647	'+	str	(p.value(	x3647	)))
filepoint.writelines	('\tx3648	'+	str	(p.value(	x3648	)))
filepoint.writelines	('\tx3649	'+	str	(p.value(	x3649	)))
filepoint.writelines	('\tx3650	'+	str	(p.value(	x3650	)))
filepoint.writelines	('\tx3651	'+	str	(p.value(	x3651	)))
filepoint.writelines	('\tx3652	'+	str	(p.value(	x3652	)))
filepoint.writelines	('\tx3653	'+	str	(p.value(	x3653	)))
filepoint.writelines	('\tx3654	'+	str	(p.value(	x3654	)))
filepoint.writelines	('\tx3655	'+	str	(p.value(	x3655	)))
filepoint.writelines	('\tx3656	'+	str	(p.value(	x3656	)))
filepoint.writelines	('\tx3657	'+	str	(p.value(	x3657	)))
filepoint.writelines	('\tx3658	'+	str	(p.value(	x3658	)))
filepoint.writelines	('\tx3659	'+	str	(p.value(	x3659	)))
filepoint.writelines	('\tx3660	'+	str	(p.value(	x3660	)))
filepoint.writelines	('\tx3661	'+	str	(p.value(	x3661	)))
filepoint.writelines	('\tx3662	'+	str	(p.value(	x3662	)))
filepoint.writelines	('\tx3663	'+	str	(p.value(	x3663	)))
filepoint.writelines	('\tx3664	'+	str	(p.value(	x3664	)))
filepoint.writelines	('\tx3665	'+	str	(p.value(	x3665	)))
filepoint.writelines	('\tx3666	'+	str	(p.value(	x3666	)))
filepoint.writelines	('\tx3667	'+	str	(p.value(	x3667	)))
filepoint.writelines	('\tx3668	'+	str	(p.value(	x3668	)))
filepoint.writelines	('\tx3669	'+	str	(p.value(	x3669	)))
filepoint.writelines	('\tx3670	'+	str	(p.value(	x3670	)))
filepoint.writelines	('\tx3671	'+	str	(p.value(	x3671	)))
filepoint.writelines	('\tx3672	'+	str	(p.value(	x3672	)))
filepoint.writelines	('\tx3673	'+	str	(p.value(	x3673	)))
filepoint.writelines	('\tx3674	'+	str	(p.value(	x3674	)))
filepoint.writelines	('\tx3675	'+	str	(p.value(	x3675	)))
filepoint.writelines	('\tx3676	'+	str	(p.value(	x3676	)))
filepoint.writelines	('\tx3677	'+	str	(p.value(	x3677	)))
filepoint.writelines	('\tx3678	'+	str	(p.value(	x3678	)))
filepoint.writelines	('\tx3679	'+	str	(p.value(	x3679	)))
filepoint.writelines	('\tx3680	'+	str	(p.value(	x3680	)))
filepoint.writelines	('\tx3681	'+	str	(p.value(	x3681	)))
filepoint.writelines	('\tx3682	'+	str	(p.value(	x3682	)))
filepoint.writelines	('\tx3683	'+	str	(p.value(	x3683	)))
filepoint.writelines	('\tx3684	'+	str	(p.value(	x3684	)))
filepoint.writelines	('\tx3685	'+	str	(p.value(	x3685	)))
filepoint.writelines	('\tx3686	'+	str	(p.value(	x3686	)))
filepoint.writelines	('\tx3687	'+	str	(p.value(	x3687	)))
filepoint.writelines	('\tx3688	'+	str	(p.value(	x3688	)))
filepoint.writelines	('\tx3689	'+	str	(p.value(	x3689	)))
filepoint.writelines	('\tx3690	'+	str	(p.value(	x3690	)))
filepoint.writelines	('\tx3691	'+	str	(p.value(	x3691	)))
filepoint.writelines	('\tx3692	'+	str	(p.value(	x3692	)))
filepoint.writelines	('\tx3693	'+	str	(p.value(	x3693	)))
filepoint.writelines	('\tx3694	'+	str	(p.value(	x3694	)))
filepoint.writelines	('\tx3695	'+	str	(p.value(	x3695	)))
filepoint.writelines	('\tx3696	'+	str	(p.value(	x3696	)))
filepoint.writelines	('\tx3697	'+	str	(p.value(	x3697	)))
filepoint.writelines	('\tx3698	'+	str	(p.value(	x3698	)))
filepoint.writelines	('\tx3699	'+	str	(p.value(	x3699	)))
filepoint.writelines	('\tx3700	'+	str	(p.value(	x3700	)))
filepoint.writelines	('\tx3701	'+	str	(p.value(	x3701	)))
filepoint.writelines	('\tx3702	'+	str	(p.value(	x3702	)))
filepoint.writelines	('\tx3703	'+	str	(p.value(	x3703	)))
filepoint.writelines	('\tx3704	'+	str	(p.value(	x3704	)))
filepoint.writelines	('\tx3705	'+	str	(p.value(	x3705	)))
filepoint.writelines	('\tx3706	'+	str	(p.value(	x3706	)))
filepoint.writelines	('\tx3707	'+	str	(p.value(	x3707	)))
filepoint.writelines	('\tx3708	'+	str	(p.value(	x3708	)))
filepoint.writelines	('\tx3709	'+	str	(p.value(	x3709	)))
filepoint.writelines	('\tx3710	'+	str	(p.value(	x3710	)))
filepoint.writelines	('\tx3711	'+	str	(p.value(	x3711	)))
filepoint.writelines	('\tx3712	'+	str	(p.value(	x3712	)))
filepoint.writelines	('\tx3713	'+	str	(p.value(	x3713	)))
filepoint.writelines	('\tx3714	'+	str	(p.value(	x3714	)))
filepoint.writelines	('\tx3715	'+	str	(p.value(	x3715	)))
filepoint.writelines	('\tx3716	'+	str	(p.value(	x3716	)))
filepoint.writelines	('\tx3717	'+	str	(p.value(	x3717	)))
filepoint.writelines	('\tx3718	'+	str	(p.value(	x3718	)))
filepoint.writelines	('\tx3719	'+	str	(p.value(	x3719	)))
filepoint.writelines	('\tx3720	'+	str	(p.value(	x3720	)))
filepoint.writelines	('\tx3721	'+	str	(p.value(	x3721	)))
filepoint.writelines	('\tx3722	'+	str	(p.value(	x3722	)))
filepoint.writelines	('\tx3723	'+	str	(p.value(	x3723	)))
filepoint.writelines	('\tx3724	'+	str	(p.value(	x3724	)))
filepoint.writelines	('\tx3725	'+	str	(p.value(	x3725	)))
filepoint.writelines	('\tx3726	'+	str	(p.value(	x3726	)))
filepoint.writelines	('\tx3727	'+	str	(p.value(	x3727	)))
filepoint.writelines	('\tx3728	'+	str	(p.value(	x3728	)))
filepoint.writelines	('\tx3729	'+	str	(p.value(	x3729	)))
filepoint.writelines	('\tx3730	'+	str	(p.value(	x3730	)))
filepoint.writelines	('\tx3731	'+	str	(p.value(	x3731	)))
filepoint.writelines	('\tx3732	'+	str	(p.value(	x3732	)))
filepoint.writelines	('\tx3733	'+	str	(p.value(	x3733	)))
filepoint.writelines	('\tx3734	'+	str	(p.value(	x3734	)))
filepoint.writelines	('\tx3735	'+	str	(p.value(	x3735	)))
filepoint.writelines	('\tx3736	'+	str	(p.value(	x3736	)))
filepoint.writelines	('\tx3737	'+	str	(p.value(	x3737	)))
filepoint.writelines	('\tx3738	'+	str	(p.value(	x3738	)))
filepoint.writelines	('\tx3739	'+	str	(p.value(	x3739	)))
filepoint.writelines	('\tx3740	'+	str	(p.value(	x3740	)))
filepoint.writelines	('\tx3741	'+	str	(p.value(	x3741	)))
filepoint.writelines	('\tx3742	'+	str	(p.value(	x3742	)))
filepoint.writelines	('\tx3743	'+	str	(p.value(	x3743	)))
filepoint.writelines	('\tx3744	'+	str	(p.value(	x3744	)))
filepoint.writelines	('\tx3745	'+	str	(p.value(	x3745	)))
filepoint.writelines	('\tx3746	'+	str	(p.value(	x3746	)))
filepoint.writelines	('\tx3747	'+	str	(p.value(	x3747	)))
filepoint.writelines	('\tx3748	'+	str	(p.value(	x3748	)))
filepoint.writelines	('\tx3749	'+	str	(p.value(	x3749	)))
filepoint.writelines	('\tx3750	'+	str	(p.value(	x3750	)))
filepoint.writelines	('\tx3751	'+	str	(p.value(	x3751	)))
filepoint.writelines	('\tx3752	'+	str	(p.value(	x3752	)))
filepoint.writelines	('\tx3753	'+	str	(p.value(	x3753	)))
filepoint.writelines	('\tx3754	'+	str	(p.value(	x3754	)))
filepoint.writelines	('\tx3755	'+	str	(p.value(	x3755	)))
filepoint.writelines	('\tx3756	'+	str	(p.value(	x3756	)))
filepoint.writelines	('\tx3757	'+	str	(p.value(	x3757	)))
filepoint.writelines	('\tx3758	'+	str	(p.value(	x3758	)))
filepoint.writelines	('\tx3759	'+	str	(p.value(	x3759	)))
filepoint.writelines	('\tx3760	'+	str	(p.value(	x3760	)))
filepoint.writelines	('\tx3761	'+	str	(p.value(	x3761	)))
filepoint.writelines	('\tx3762	'+	str	(p.value(	x3762	)))
filepoint.writelines	('\tx3763	'+	str	(p.value(	x3763	)))
filepoint.writelines	('\tx3764	'+	str	(p.value(	x3764	)))
filepoint.writelines	('\tx3765	'+	str	(p.value(	x3765	)))
filepoint.writelines	('\tx3766	'+	str	(p.value(	x3766	)))
filepoint.writelines	('\tx3767	'+	str	(p.value(	x3767	)))
filepoint.writelines	('\tx3768	'+	str	(p.value(	x3768	)))
filepoint.writelines	('\tx3769	'+	str	(p.value(	x3769	)))
filepoint.writelines	('\tx3770	'+	str	(p.value(	x3770	)))
filepoint.writelines	('\tx3771	'+	str	(p.value(	x3771	)))
filepoint.writelines	('\tx3772	'+	str	(p.value(	x3772	)))
filepoint.writelines	('\tx3773	'+	str	(p.value(	x3773	)))
filepoint.writelines	('\tx3774	'+	str	(p.value(	x3774	)))
filepoint.writelines	('\tx3775	'+	str	(p.value(	x3775	)))
filepoint.writelines	('\tx3776	'+	str	(p.value(	x3776	)))
filepoint.writelines	('\tx3777	'+	str	(p.value(	x3777	)))
filepoint.writelines	('\tx3778	'+	str	(p.value(	x3778	)))
filepoint.writelines	('\tx3779	'+	str	(p.value(	x3779	)))
filepoint.writelines	('\tx3780	'+	str	(p.value(	x3780	)))
filepoint.writelines	('\tx3781	'+	str	(p.value(	x3781	)))
filepoint.writelines	('\tx3782	'+	str	(p.value(	x3782	)))
filepoint.writelines	('\tx3783	'+	str	(p.value(	x3783	)))
filepoint.writelines	('\tx3784	'+	str	(p.value(	x3784	)))
filepoint.writelines	('\tx3785	'+	str	(p.value(	x3785	)))
filepoint.writelines	('\tx3786	'+	str	(p.value(	x3786	)))
filepoint.writelines	('\tx3787	'+	str	(p.value(	x3787	)))
filepoint.writelines	('\tx3788	'+	str	(p.value(	x3788	)))
filepoint.writelines	('\tx3789	'+	str	(p.value(	x3789	)))
filepoint.writelines	('\tx3790	'+	str	(p.value(	x3790	)))
filepoint.writelines	('\tx3791	'+	str	(p.value(	x3791	)))
filepoint.writelines	('\tx3792	'+	str	(p.value(	x3792	)))
filepoint.writelines	('\tx3793	'+	str	(p.value(	x3793	)))
filepoint.writelines	('\tx3794	'+	str	(p.value(	x3794	)))
filepoint.writelines	('\tx3795	'+	str	(p.value(	x3795	)))
filepoint.writelines	('\tx3796	'+	str	(p.value(	x3796	)))
filepoint.writelines	('\tx3797	'+	str	(p.value(	x3797	)))
filepoint.writelines	('\tx3798	'+	str	(p.value(	x3798	)))
filepoint.writelines	('\tx3799	'+	str	(p.value(	x3799	)))
filepoint.writelines	('\tx3800	'+	str	(p.value(	x3800	)))
filepoint.writelines	('\tx3801	'+	str	(p.value(	x3801	)))
filepoint.writelines	('\tx3802	'+	str	(p.value(	x3802	)))
filepoint.writelines	('\tx3803	'+	str	(p.value(	x3803	)))
filepoint.writelines	('\tx3804	'+	str	(p.value(	x3804	)))
filepoint.writelines	('\tx3805	'+	str	(p.value(	x3805	)))
filepoint.writelines	('\tx3806	'+	str	(p.value(	x3806	)))
filepoint.writelines	('\tx3807	'+	str	(p.value(	x3807	)))
filepoint.writelines	('\tx3808	'+	str	(p.value(	x3808	)))
filepoint.writelines	('\tx3809	'+	str	(p.value(	x3809	)))
filepoint.writelines	('\tx3810	'+	str	(p.value(	x3810	)))
filepoint.writelines	('\tx3811	'+	str	(p.value(	x3811	)))
filepoint.writelines	('\tx3812	'+	str	(p.value(	x3812	)))
filepoint.writelines	('\tx3813	'+	str	(p.value(	x3813	)))
filepoint.writelines	('\tx3814	'+	str	(p.value(	x3814	)))
filepoint.writelines	('\tx3815	'+	str	(p.value(	x3815	)))
filepoint.writelines	('\tx3816	'+	str	(p.value(	x3816	)))
filepoint.writelines	('\tx3817	'+	str	(p.value(	x3817	)))
filepoint.writelines	('\tx3818	'+	str	(p.value(	x3818	)))
filepoint.writelines	('\tx3819	'+	str	(p.value(	x3819	)))
filepoint.writelines	('\tx3820	'+	str	(p.value(	x3820	)))
filepoint.writelines	('\tx3821	'+	str	(p.value(	x3821	)))
filepoint.writelines	('\tx3822	'+	str	(p.value(	x3822	)))
filepoint.writelines	('\tx3823	'+	str	(p.value(	x3823	)))
filepoint.writelines	('\tx3824	'+	str	(p.value(	x3824	)))
filepoint.writelines	('\tx3825	'+	str	(p.value(	x3825	)))
filepoint.writelines	('\tx3826	'+	str	(p.value(	x3826	)))
filepoint.writelines	('\tx3827	'+	str	(p.value(	x3827	)))
filepoint.writelines	('\tx3828	'+	str	(p.value(	x3828	)))
filepoint.writelines	('\tx3829	'+	str	(p.value(	x3829	)))
filepoint.writelines	('\tx3830	'+	str	(p.value(	x3830	)))
filepoint.writelines	('\tx3831	'+	str	(p.value(	x3831	)))
filepoint.writelines	('\tx3832	'+	str	(p.value(	x3832	)))
filepoint.writelines	('\tx3833	'+	str	(p.value(	x3833	)))
filepoint.writelines	('\tx3834	'+	str	(p.value(	x3834	)))
filepoint.writelines	('\tx3835	'+	str	(p.value(	x3835	)))
filepoint.writelines	('\tx3836	'+	str	(p.value(	x3836	)))
filepoint.writelines	('\tx3837	'+	str	(p.value(	x3837	)))
filepoint.writelines	('\tx3838	'+	str	(p.value(	x3838	)))
filepoint.writelines	('\tx3839	'+	str	(p.value(	x3839	)))
filepoint.writelines	('\tx3840	'+	str	(p.value(	x3840	)))
filepoint.writelines	('\tx3841	'+	str	(p.value(	x3841	)))
filepoint.writelines	('\tx3842	'+	str	(p.value(	x3842	)))
filepoint.writelines	('\tx3843	'+	str	(p.value(	x3843	)))
filepoint.writelines	('\tx3844	'+	str	(p.value(	x3844	)))
filepoint.writelines	('\tx3845	'+	str	(p.value(	x3845	)))
filepoint.writelines	('\tx3846	'+	str	(p.value(	x3846	)))
filepoint.writelines	('\tx3847	'+	str	(p.value(	x3847	)))
filepoint.writelines	('\tx3848	'+	str	(p.value(	x3848	)))
filepoint.writelines	('\tx3849	'+	str	(p.value(	x3849	)))
filepoint.writelines	('\tx3850	'+	str	(p.value(	x3850	)))
filepoint.writelines	('\tx3851	'+	str	(p.value(	x3851	)))
filepoint.writelines	('\tx3852	'+	str	(p.value(	x3852	)))
filepoint.writelines	('\tx3853	'+	str	(p.value(	x3853	)))
filepoint.writelines	('\tx3854	'+	str	(p.value(	x3854	)))
filepoint.writelines	('\tx3855	'+	str	(p.value(	x3855	)))
filepoint.writelines	('\tx3856	'+	str	(p.value(	x3856	)))
filepoint.writelines	('\tx3857	'+	str	(p.value(	x3857	)))
filepoint.writelines	('\tx3858	'+	str	(p.value(	x3858	)))
filepoint.writelines	('\tx3859	'+	str	(p.value(	x3859	)))
filepoint.writelines	('\tx3860	'+	str	(p.value(	x3860	)))
filepoint.writelines	('\tx3861	'+	str	(p.value(	x3861	)))
filepoint.writelines	('\tx3862	'+	str	(p.value(	x3862	)))
filepoint.writelines	('\tx3863	'+	str	(p.value(	x3863	)))
filepoint.writelines	('\tx3864	'+	str	(p.value(	x3864	)))
filepoint.writelines	('\tx3865	'+	str	(p.value(	x3865	)))
filepoint.writelines	('\tx3866	'+	str	(p.value(	x3866	)))
filepoint.writelines	('\tx3867	'+	str	(p.value(	x3867	)))
filepoint.writelines	('\tx3868	'+	str	(p.value(	x3868	)))
filepoint.writelines	('\tx3869	'+	str	(p.value(	x3869	)))
filepoint.writelines	('\tx3870	'+	str	(p.value(	x3870	)))
filepoint.writelines	('\tx3871	'+	str	(p.value(	x3871	)))
filepoint.writelines	('\tx3872	'+	str	(p.value(	x3872	)))
filepoint.writelines	('\tx3873	'+	str	(p.value(	x3873	)))
filepoint.writelines	('\tx3874	'+	str	(p.value(	x3874	)))
filepoint.writelines	('\tx3875	'+	str	(p.value(	x3875	)))
filepoint.writelines	('\tx3876	'+	str	(p.value(	x3876	)))
filepoint.writelines	('\tx3877	'+	str	(p.value(	x3877	)))
filepoint.writelines	('\tx3878	'+	str	(p.value(	x3878	)))
filepoint.writelines	('\tx3879	'+	str	(p.value(	x3879	)))
filepoint.writelines	('\tx3880	'+	str	(p.value(	x3880	)))
filepoint.writelines	('\tx3881	'+	str	(p.value(	x3881	)))
filepoint.writelines	('\tx3882	'+	str	(p.value(	x3882	)))
filepoint.writelines	('\tx3883	'+	str	(p.value(	x3883	)))
filepoint.writelines	('\tx3884	'+	str	(p.value(	x3884	)))
filepoint.writelines	('\tx3885	'+	str	(p.value(	x3885	)))
filepoint.writelines	('\tx3886	'+	str	(p.value(	x3886	)))
filepoint.writelines	('\tx3887	'+	str	(p.value(	x3887	)))
filepoint.writelines	('\tx3888	'+	str	(p.value(	x3888	)))
filepoint.writelines	('\tx3889	'+	str	(p.value(	x3889	)))
filepoint.writelines	('\tx3890	'+	str	(p.value(	x3890	)))
filepoint.writelines	('\tx3891	'+	str	(p.value(	x3891	)))
filepoint.writelines	('\tx3892	'+	str	(p.value(	x3892	)))
filepoint.writelines	('\tx3893	'+	str	(p.value(	x3893	)))
filepoint.writelines	('\tx3894	'+	str	(p.value(	x3894	)))
filepoint.writelines	('\tx3895	'+	str	(p.value(	x3895	)))
filepoint.writelines	('\tx3896	'+	str	(p.value(	x3896	)))
filepoint.writelines	('\tx3897	'+	str	(p.value(	x3897	)))
filepoint.writelines	('\tx3898	'+	str	(p.value(	x3898	)))
filepoint.writelines	('\tx3899	'+	str	(p.value(	x3899	)))
filepoint.writelines	('\tx3900	'+	str	(p.value(	x3900	)))
filepoint.writelines	('\tx3901	'+	str	(p.value(	x3901	)))
filepoint.writelines	('\tx3902	'+	str	(p.value(	x3902	)))
filepoint.writelines	('\tx3903	'+	str	(p.value(	x3903	)))
filepoint.writelines	('\tx3904	'+	str	(p.value(	x3904	)))
filepoint.writelines	('\tx3905	'+	str	(p.value(	x3905	)))
filepoint.writelines	('\tx3906	'+	str	(p.value(	x3906	)))
filepoint.writelines	('\tx3907	'+	str	(p.value(	x3907	)))
filepoint.writelines	('\tx3908	'+	str	(p.value(	x3908	)))
filepoint.writelines	('\tx3909	'+	str	(p.value(	x3909	)))
filepoint.writelines	('\tx3910	'+	str	(p.value(	x3910	)))
filepoint.writelines	('\tx3911	'+	str	(p.value(	x3911	)))
filepoint.writelines	('\tx3912	'+	str	(p.value(	x3912	)))
filepoint.writelines	('\tx3913	'+	str	(p.value(	x3913	)))
filepoint.writelines	('\tx3914	'+	str	(p.value(	x3914	)))
filepoint.writelines	('\tx3915	'+	str	(p.value(	x3915	)))
filepoint.writelines	('\tx3916	'+	str	(p.value(	x3916	)))
filepoint.writelines	('\tx3917	'+	str	(p.value(	x3917	)))
filepoint.writelines	('\tx3918	'+	str	(p.value(	x3918	)))
filepoint.writelines	('\tx3919	'+	str	(p.value(	x3919	)))
filepoint.writelines	('\tx3920	'+	str	(p.value(	x3920	)))
filepoint.writelines	('\tx3921	'+	str	(p.value(	x3921	)))
filepoint.writelines	('\tx3922	'+	str	(p.value(	x3922	)))
filepoint.writelines	('\tx3923	'+	str	(p.value(	x3923	)))
filepoint.writelines	('\tx3924	'+	str	(p.value(	x3924	)))
filepoint.writelines	('\tx3925	'+	str	(p.value(	x3925	)))
filepoint.writelines	('\tx3926	'+	str	(p.value(	x3926	)))
filepoint.writelines	('\tx3927	'+	str	(p.value(	x3927	)))
filepoint.writelines	('\tx3928	'+	str	(p.value(	x3928	)))
filepoint.writelines	('\tx3929	'+	str	(p.value(	x3929	)))
filepoint.writelines	('\tx3930	'+	str	(p.value(	x3930	)))
filepoint.writelines	('\tx3931	'+	str	(p.value(	x3931	)))
filepoint.writelines	('\tx3932	'+	str	(p.value(	x3932	)))
filepoint.writelines	('\tx3933	'+	str	(p.value(	x3933	)))
filepoint.writelines	('\tx3934	'+	str	(p.value(	x3934	)))
filepoint.writelines	('\tx3935	'+	str	(p.value(	x3935	)))
filepoint.writelines	('\tx3936	'+	str	(p.value(	x3936	)))
filepoint.writelines	('\tx3937	'+	str	(p.value(	x3937	)))
filepoint.writelines	('\tx3938	'+	str	(p.value(	x3938	)))
filepoint.writelines	('\tx3939	'+	str	(p.value(	x3939	)))
filepoint.writelines	('\tx3940	'+	str	(p.value(	x3940	)))
filepoint.writelines	('\tx3941	'+	str	(p.value(	x3941	)))
filepoint.writelines	('\tx3942	'+	str	(p.value(	x3942	)))
filepoint.writelines	('\tx3943	'+	str	(p.value(	x3943	)))
filepoint.writelines	('\tx3944	'+	str	(p.value(	x3944	)))
filepoint.writelines	('\tx3945	'+	str	(p.value(	x3945	)))
filepoint.writelines	('\tx3946	'+	str	(p.value(	x3946	)))
filepoint.writelines	('\tx3947	'+	str	(p.value(	x3947	)))
filepoint.writelines	('\tx3948	'+	str	(p.value(	x3948	)))
filepoint.writelines	('\tx3949	'+	str	(p.value(	x3949	)))
filepoint.writelines	('\tx3950	'+	str	(p.value(	x3950	)))
filepoint.writelines	('\tx3951	'+	str	(p.value(	x3951	)))
filepoint.writelines	('\tx3952	'+	str	(p.value(	x3952	)))
filepoint.writelines	('\tx3953	'+	str	(p.value(	x3953	)))
filepoint.writelines	('\tx3954	'+	str	(p.value(	x3954	)))
filepoint.writelines	('\tx3955	'+	str	(p.value(	x3955	)))
filepoint.writelines	('\tx3956	'+	str	(p.value(	x3956	)))
filepoint.writelines	('\tx3957	'+	str	(p.value(	x3957	)))
filepoint.writelines	('\tx3958	'+	str	(p.value(	x3958	)))
filepoint.writelines	('\tx3959	'+	str	(p.value(	x3959	)))
filepoint.writelines	('\tx3960	'+	str	(p.value(	x3960	)))
filepoint.writelines	('\tx3961	'+	str	(p.value(	x3961	)))
filepoint.writelines	('\tx3962	'+	str	(p.value(	x3962	)))
filepoint.writelines	('\tx3963	'+	str	(p.value(	x3963	)))
filepoint.writelines	('\tx3964	'+	str	(p.value(	x3964	)))
filepoint.writelines	('\tx3965	'+	str	(p.value(	x3965	)))
filepoint.writelines	('\tx3966	'+	str	(p.value(	x3966	)))
filepoint.writelines	('\tx3967	'+	str	(p.value(	x3967	)))
filepoint.writelines	('\tx3968	'+	str	(p.value(	x3968	)))
filepoint.writelines	('\tx3969	'+	str	(p.value(	x3969	)))
filepoint.writelines	('\tx3970	'+	str	(p.value(	x3970	)))
filepoint.writelines	('\tx3971	'+	str	(p.value(	x3971	)))
filepoint.writelines	('\tx3972	'+	str	(p.value(	x3972	)))
filepoint.writelines	('\tx3973	'+	str	(p.value(	x3973	)))
filepoint.writelines	('\tx3974	'+	str	(p.value(	x3974	)))
filepoint.writelines	('\tx3975	'+	str	(p.value(	x3975	)))
filepoint.writelines	('\tx3976	'+	str	(p.value(	x3976	)))
filepoint.writelines	('\tx3977	'+	str	(p.value(	x3977	)))
filepoint.writelines	('\tx3978	'+	str	(p.value(	x3978	)))
filepoint.writelines	('\tx3979	'+	str	(p.value(	x3979	)))
filepoint.writelines	('\tx3980	'+	str	(p.value(	x3980	)))
filepoint.writelines	('\tx3981	'+	str	(p.value(	x3981	)))
filepoint.writelines	('\tx3982	'+	str	(p.value(	x3982	)))
filepoint.writelines	('\tx3983	'+	str	(p.value(	x3983	)))
filepoint.writelines	('\tx3984	'+	str	(p.value(	x3984	)))
filepoint.writelines	('\tx3985	'+	str	(p.value(	x3985	)))
filepoint.writelines	('\tx3986	'+	str	(p.value(	x3986	)))
filepoint.writelines	('\tx3987	'+	str	(p.value(	x3987	)))
filepoint.writelines	('\tx3988	'+	str	(p.value(	x3988	)))
filepoint.writelines	('\tx3989	'+	str	(p.value(	x3989	)))
filepoint.writelines	('\tx3990	'+	str	(p.value(	x3990	)))
filepoint.writelines	('\tx3991	'+	str	(p.value(	x3991	)))
filepoint.writelines	('\tx3992	'+	str	(p.value(	x3992	)))
filepoint.writelines	('\tx3993	'+	str	(p.value(	x3993	)))
filepoint.writelines	('\tx3994	'+	str	(p.value(	x3994	)))
filepoint.writelines	('\tx3995	'+	str	(p.value(	x3995	)))
filepoint.writelines	('\tx3996	'+	str	(p.value(	x3996	)))
filepoint.writelines	('\tx3997	'+	str	(p.value(	x3997	)))
filepoint.writelines	('\tx3998	'+	str	(p.value(	x3998	)))
filepoint.writelines	('\tx3999	'+	str	(p.value(	x3999	)))
filepoint.writelines	('\tx4000	'+	str	(p.value(	x4000	)))
filepoint.writelines	('\tx4001	'+	str	(p.value(	x4001	)))
filepoint.writelines	('\tx4002	'+	str	(p.value(	x4002	)))
filepoint.writelines	('\tx4003	'+	str	(p.value(	x4003	)))
filepoint.writelines	('\tx4004	'+	str	(p.value(	x4004	)))
filepoint.writelines	('\tx4005	'+	str	(p.value(	x4005	)))
filepoint.writelines	('\tx4006	'+	str	(p.value(	x4006	)))
filepoint.writelines	('\tx4007	'+	str	(p.value(	x4007	)))
filepoint.writelines	('\tx4008	'+	str	(p.value(	x4008	)))
filepoint.writelines	('\tx4009	'+	str	(p.value(	x4009	)))
filepoint.writelines	('\tx4010	'+	str	(p.value(	x4010	)))
filepoint.writelines	('\tx4011	'+	str	(p.value(	x4011	)))
filepoint.writelines	('\tx4012	'+	str	(p.value(	x4012	)))
filepoint.writelines	('\tx4013	'+	str	(p.value(	x4013	)))
filepoint.writelines	('\tx4014	'+	str	(p.value(	x4014	)))
filepoint.writelines	('\tx4015	'+	str	(p.value(	x4015	)))
filepoint.writelines	('\tx4016	'+	str	(p.value(	x4016	)))
filepoint.writelines	('\tx4017	'+	str	(p.value(	x4017	)))
filepoint.writelines	('\tx4018	'+	str	(p.value(	x4018	)))
filepoint.writelines	('\tx4019	'+	str	(p.value(	x4019	)))
filepoint.writelines	('\tx4020	'+	str	(p.value(	x4020	)))
filepoint.writelines	('\tx4021	'+	str	(p.value(	x4021	)))
filepoint.writelines	('\tx4022	'+	str	(p.value(	x4022	)))
filepoint.writelines	('\tx4023	'+	str	(p.value(	x4023	)))
filepoint.writelines	('\tx4024	'+	str	(p.value(	x4024	)))
filepoint.writelines	('\tx4025	'+	str	(p.value(	x4025	)))
filepoint.writelines	('\tx4026	'+	str	(p.value(	x4026	)))
filepoint.writelines	('\tx4027	'+	str	(p.value(	x4027	)))
filepoint.writelines	('\tx4028	'+	str	(p.value(	x4028	)))
filepoint.writelines	('\tx4029	'+	str	(p.value(	x4029	)))
filepoint.writelines	('\tx4030	'+	str	(p.value(	x4030	)))
filepoint.writelines	('\tx4031	'+	str	(p.value(	x4031	)))
filepoint.writelines	('\tx4032	'+	str	(p.value(	x4032	)))
filepoint.writelines	('\tx4033	'+	str	(p.value(	x4033	)))
filepoint.writelines	('\tx4034	'+	str	(p.value(	x4034	)))
filepoint.writelines	('\tx4035	'+	str	(p.value(	x4035	)))
filepoint.writelines	('\tx4036	'+	str	(p.value(	x4036	)))
filepoint.writelines	('\tx4037	'+	str	(p.value(	x4037	)))
filepoint.writelines	('\tx4038	'+	str	(p.value(	x4038	)))
filepoint.writelines	('\tx4039	'+	str	(p.value(	x4039	)))
filepoint.writelines	('\tx4040	'+	str	(p.value(	x4040	)))
filepoint.writelines	('\tx4041	'+	str	(p.value(	x4041	)))
filepoint.writelines	('\tx4042	'+	str	(p.value(	x4042	)))
filepoint.writelines	('\tx4043	'+	str	(p.value(	x4043	)))
filepoint.writelines	('\tx4044	'+	str	(p.value(	x4044	)))
filepoint.writelines	('\tx4045	'+	str	(p.value(	x4045	)))
filepoint.writelines	('\tx4046	'+	str	(p.value(	x4046	)))
filepoint.writelines	('\tx4047	'+	str	(p.value(	x4047	)))
filepoint.writelines	('\tx4048	'+	str	(p.value(	x4048	)))
filepoint.writelines	('\tx4049	'+	str	(p.value(	x4049	)))
filepoint.writelines	('\tx4050	'+	str	(p.value(	x4050	)))
filepoint.writelines	('\tx4051	'+	str	(p.value(	x4051	)))
filepoint.writelines	('\tx4052	'+	str	(p.value(	x4052	)))
filepoint.writelines	('\tx4053	'+	str	(p.value(	x4053	)))
filepoint.writelines	('\tx4054	'+	str	(p.value(	x4054	)))
filepoint.writelines	('\tx4055	'+	str	(p.value(	x4055	)))
filepoint.writelines	('\tx4056	'+	str	(p.value(	x4056	)))
filepoint.writelines	('\tx4057	'+	str	(p.value(	x4057	)))
filepoint.writelines	('\tx4058	'+	str	(p.value(	x4058	)))
filepoint.writelines	('\tx4059	'+	str	(p.value(	x4059	)))
filepoint.writelines	('\tx4060	'+	str	(p.value(	x4060	)))
filepoint.writelines	('\tx4061	'+	str	(p.value(	x4061	)))
filepoint.writelines	('\tx4062	'+	str	(p.value(	x4062	)))
filepoint.writelines	('\tx4063	'+	str	(p.value(	x4063	)))
filepoint.writelines	('\tx4064	'+	str	(p.value(	x4064	)))
filepoint.writelines	('\tx4065	'+	str	(p.value(	x4065	)))
filepoint.writelines	('\tx4066	'+	str	(p.value(	x4066	)))
filepoint.writelines	('\tx4067	'+	str	(p.value(	x4067	)))
filepoint.writelines	('\tx4068	'+	str	(p.value(	x4068	)))
filepoint.writelines	('\tx4069	'+	str	(p.value(	x4069	)))
filepoint.writelines	('\tx4070	'+	str	(p.value(	x4070	)))
filepoint.writelines	('\tx4071	'+	str	(p.value(	x4071	)))
filepoint.writelines	('\tx4072	'+	str	(p.value(	x4072	)))
filepoint.writelines	('\tx4073	'+	str	(p.value(	x4073	)))
filepoint.writelines	('\tx4074	'+	str	(p.value(	x4074	)))
filepoint.writelines	('\tx4075	'+	str	(p.value(	x4075	)))
filepoint.writelines	('\tx4076	'+	str	(p.value(	x4076	)))
filepoint.writelines	('\tx4077	'+	str	(p.value(	x4077	)))
filepoint.writelines	('\tx4078	'+	str	(p.value(	x4078	)))
filepoint.writelines	('\tx4079	'+	str	(p.value(	x4079	)))
filepoint.writelines	('\tx4080	'+	str	(p.value(	x4080	)))
filepoint.writelines	('\tx4081	'+	str	(p.value(	x4081	)))
filepoint.writelines	('\tx4082	'+	str	(p.value(	x4082	)))
filepoint.writelines	('\tx4083	'+	str	(p.value(	x4083	)))
filepoint.writelines	('\tx4084	'+	str	(p.value(	x4084	)))
filepoint.writelines	('\tx4085	'+	str	(p.value(	x4085	)))
filepoint.writelines	('\tx4086	'+	str	(p.value(	x4086	)))
filepoint.writelines	('\tx4087	'+	str	(p.value(	x4087	)))
filepoint.writelines	('\tx4088	'+	str	(p.value(	x4088	)))
filepoint.writelines	('\tx4089	'+	str	(p.value(	x4089	)))
filepoint.writelines	('\tx4090	'+	str	(p.value(	x4090	)))
filepoint.writelines	('\tx4091	'+	str	(p.value(	x4091	)))
filepoint.writelines	('\tx4092	'+	str	(p.value(	x4092	)))
filepoint.writelines	('\tx4093	'+	str	(p.value(	x4093	)))
filepoint.writelines	('\tx4094	'+	str	(p.value(	x4094	)))
filepoint.writelines	('\tx4095	'+	str	(p.value(	x4095	)))
filepoint.writelines	('\tx4096	'+	str	(p.value(	x4096	)))
filepoint.writelines	('\tx4097	'+	str	(p.value(	x4097	)))
filepoint.writelines	('\tx4098	'+	str	(p.value(	x4098	)))
filepoint.writelines	('\tx4099	'+	str	(p.value(	x4099	)))
filepoint.writelines	('\tx4100	'+	str	(p.value(	x4100	)))
filepoint.writelines	('\tx4101	'+	str	(p.value(	x4101	)))
filepoint.writelines	('\tx4102	'+	str	(p.value(	x4102	)))
filepoint.writelines	('\tx4103	'+	str	(p.value(	x4103	)))
filepoint.writelines	('\tx4104	'+	str	(p.value(	x4104	)))
filepoint.writelines	('\tx4105	'+	str	(p.value(	x4105	)))
filepoint.writelines	('\tx4106	'+	str	(p.value(	x4106	)))
filepoint.writelines	('\tx4107	'+	str	(p.value(	x4107	)))
filepoint.writelines	('\tx4108	'+	str	(p.value(	x4108	)))
filepoint.writelines	('\tx4109	'+	str	(p.value(	x4109	)))
filepoint.writelines	('\tx4110	'+	str	(p.value(	x4110	)))
filepoint.writelines	('\tx4111	'+	str	(p.value(	x4111	)))
filepoint.writelines	('\tx4112	'+	str	(p.value(	x4112	)))
filepoint.writelines	('\tx4113	'+	str	(p.value(	x4113	)))
filepoint.writelines	('\tx4114	'+	str	(p.value(	x4114	)))
filepoint.writelines	('\tx4115	'+	str	(p.value(	x4115	)))
filepoint.writelines	('\tx4116	'+	str	(p.value(	x4116	)))
filepoint.writelines	('\tx4117	'+	str	(p.value(	x4117	)))
filepoint.writelines	('\tx4118	'+	str	(p.value(	x4118	)))
filepoint.writelines	('\tx4119	'+	str	(p.value(	x4119	)))
filepoint.writelines	('\tx4120	'+	str	(p.value(	x4120	)))
filepoint.writelines	('\tx4121	'+	str	(p.value(	x4121	)))
filepoint.writelines	('\tx4122	'+	str	(p.value(	x4122	)))
filepoint.writelines	('\tx4123	'+	str	(p.value(	x4123	)))
filepoint.writelines	('\tx4124	'+	str	(p.value(	x4124	)))
filepoint.writelines	('\tx4125	'+	str	(p.value(	x4125	)))
filepoint.writelines	('\tx4126	'+	str	(p.value(	x4126	)))
filepoint.writelines	('\tx4127	'+	str	(p.value(	x4127	)))
filepoint.writelines	('\tx4128	'+	str	(p.value(	x4128	)))
filepoint.writelines	('\tx4129	'+	str	(p.value(	x4129	)))
filepoint.writelines	('\tx4130	'+	str	(p.value(	x4130	)))
filepoint.writelines	('\tx4131	'+	str	(p.value(	x4131	)))
filepoint.writelines	('\tx4132	'+	str	(p.value(	x4132	)))
filepoint.writelines	('\tx4133	'+	str	(p.value(	x4133	)))
filepoint.writelines	('\tx4134	'+	str	(p.value(	x4134	)))
filepoint.writelines	('\tx4135	'+	str	(p.value(	x4135	)))
filepoint.writelines	('\tx4136	'+	str	(p.value(	x4136	)))
filepoint.writelines	('\tx4137	'+	str	(p.value(	x4137	)))
filepoint.writelines	('\tx4138	'+	str	(p.value(	x4138	)))
filepoint.writelines	('\tx4139	'+	str	(p.value(	x4139	)))
filepoint.writelines	('\tx4140	'+	str	(p.value(	x4140	)))
filepoint.writelines	('\tx4141	'+	str	(p.value(	x4141	)))
filepoint.writelines	('\tx4142	'+	str	(p.value(	x4142	)))
filepoint.writelines	('\tx4143	'+	str	(p.value(	x4143	)))
filepoint.writelines	('\tx4144	'+	str	(p.value(	x4144	)))
filepoint.writelines	('\tx4145	'+	str	(p.value(	x4145	)))
filepoint.writelines	('\tx4146	'+	str	(p.value(	x4146	)))
filepoint.writelines	('\tx4147	'+	str	(p.value(	x4147	)))
filepoint.writelines	('\tx4148	'+	str	(p.value(	x4148	)))
filepoint.writelines	('\tx4149	'+	str	(p.value(	x4149	)))
filepoint.writelines	('\tx4150	'+	str	(p.value(	x4150	)))
filepoint.writelines	('\tx4151	'+	str	(p.value(	x4151	)))
filepoint.writelines	('\tx4152	'+	str	(p.value(	x4152	)))
filepoint.writelines	('\tx4153	'+	str	(p.value(	x4153	)))
filepoint.writelines	('\tx4154	'+	str	(p.value(	x4154	)))
filepoint.writelines	('\tx4155	'+	str	(p.value(	x4155	)))
filepoint.writelines	('\tx4156	'+	str	(p.value(	x4156	)))
filepoint.writelines	('\tx4157	'+	str	(p.value(	x4157	)))
filepoint.writelines	('\tx4158	'+	str	(p.value(	x4158	)))
filepoint.writelines	('\tx4159	'+	str	(p.value(	x4159	)))
filepoint.writelines	('\tx4160	'+	str	(p.value(	x4160	)))
filepoint.writelines	('\tx4161	'+	str	(p.value(	x4161	)))
filepoint.writelines	('\tx4162	'+	str	(p.value(	x4162	)))
filepoint.writelines	('\tx4163	'+	str	(p.value(	x4163	)))
filepoint.writelines	('\tx4164	'+	str	(p.value(	x4164	)))
filepoint.writelines	('\tx4165	'+	str	(p.value(	x4165	)))
filepoint.writelines	('\tx4166	'+	str	(p.value(	x4166	)))
filepoint.writelines	('\tx4167	'+	str	(p.value(	x4167	)))
filepoint.writelines	('\tx4168	'+	str	(p.value(	x4168	)))
filepoint.writelines	('\tx4169	'+	str	(p.value(	x4169	)))
filepoint.writelines	('\tx4170	'+	str	(p.value(	x4170	)))
filepoint.writelines	('\tx4171	'+	str	(p.value(	x4171	)))
filepoint.writelines	('\tx4172	'+	str	(p.value(	x4172	)))
filepoint.writelines	('\tx4173	'+	str	(p.value(	x4173	)))
filepoint.writelines	('\tx4174	'+	str	(p.value(	x4174	)))
filepoint.writelines	('\tx4175	'+	str	(p.value(	x4175	)))
filepoint.writelines	('\tx4176	'+	str	(p.value(	x4176	)))
filepoint.writelines	('\tx4177	'+	str	(p.value(	x4177	)))
filepoint.writelines	('\tx4178	'+	str	(p.value(	x4178	)))
filepoint.writelines	('\tx4179	'+	str	(p.value(	x4179	)))
filepoint.writelines	('\tx4180	'+	str	(p.value(	x4180	)))
filepoint.writelines	('\tx4181	'+	str	(p.value(	x4181	)))
filepoint.writelines	('\tx4182	'+	str	(p.value(	x4182	)))
filepoint.writelines	('\tx4183	'+	str	(p.value(	x4183	)))
filepoint.writelines	('\tx4184	'+	str	(p.value(	x4184	)))
filepoint.writelines	('\tx4185	'+	str	(p.value(	x4185	)))
filepoint.writelines	('\tx4186	'+	str	(p.value(	x4186	)))
filepoint.writelines	('\tx4187	'+	str	(p.value(	x4187	)))
filepoint.writelines	('\tx4188	'+	str	(p.value(	x4188	)))
filepoint.writelines	('\tx4189	'+	str	(p.value(	x4189	)))
filepoint.writelines	('\tx4190	'+	str	(p.value(	x4190	)))
filepoint.writelines	('\tx4191	'+	str	(p.value(	x4191	)))
filepoint.writelines	('\tx4192	'+	str	(p.value(	x4192	)))
filepoint.writelines	('\tx4193	'+	str	(p.value(	x4193	)))
filepoint.writelines	('\tx4194	'+	str	(p.value(	x4194	)))
filepoint.writelines	('\tx4195	'+	str	(p.value(	x4195	)))
filepoint.writelines	('\tx4196	'+	str	(p.value(	x4196	)))
filepoint.writelines	('\tx4197	'+	str	(p.value(	x4197	)))
filepoint.writelines	('\tx4198	'+	str	(p.value(	x4198	)))
filepoint.writelines	('\tx4199	'+	str	(p.value(	x4199	)))
filepoint.writelines	('\tx4200	'+	str	(p.value(	x4200	)))
filepoint.writelines	('\tx4201	'+	str	(p.value(	x4201	)))
filepoint.writelines	('\tx4202	'+	str	(p.value(	x4202	)))
filepoint.writelines	('\tx4203	'+	str	(p.value(	x4203	)))
filepoint.writelines	('\tx4204	'+	str	(p.value(	x4204	)))
filepoint.writelines	('\tx4205	'+	str	(p.value(	x4205	)))
filepoint.writelines	('\tx4206	'+	str	(p.value(	x4206	)))
filepoint.writelines	('\tx4207	'+	str	(p.value(	x4207	)))
filepoint.writelines	('\tx4208	'+	str	(p.value(	x4208	)))
filepoint.writelines	('\tx4209	'+	str	(p.value(	x4209	)))
filepoint.writelines	('\tx4210	'+	str	(p.value(	x4210	)))
filepoint.writelines	('\tx4211	'+	str	(p.value(	x4211	)))
filepoint.writelines	('\tx4212	'+	str	(p.value(	x4212	)))
filepoint.writelines	('\tx4213	'+	str	(p.value(	x4213	)))
filepoint.writelines	('\tx4214	'+	str	(p.value(	x4214	)))
filepoint.writelines	('\tx4215	'+	str	(p.value(	x4215	)))
filepoint.writelines	('\tx4216	'+	str	(p.value(	x4216	)))
filepoint.writelines	('\tx4217	'+	str	(p.value(	x4217	)))
filepoint.writelines	('\tx4218	'+	str	(p.value(	x4218	)))
filepoint.writelines	('\tx4219	'+	str	(p.value(	x4219	)))
filepoint.writelines	('\tx4220	'+	str	(p.value(	x4220	)))
filepoint.writelines	('\tx4221	'+	str	(p.value(	x4221	)))
filepoint.writelines	('\tx4222	'+	str	(p.value(	x4222	)))
filepoint.writelines	('\tx4223	'+	str	(p.value(	x4223	)))
filepoint.writelines	('\tx4224	'+	str	(p.value(	x4224	)))
filepoint.writelines	('\tx4225	'+	str	(p.value(	x4225	)))
filepoint.writelines	('\tx4226	'+	str	(p.value(	x4226	)))
filepoint.writelines	('\tx4227	'+	str	(p.value(	x4227	)))
filepoint.writelines	('\tx4228	'+	str	(p.value(	x4228	)))
filepoint.writelines	('\tx4229	'+	str	(p.value(	x4229	)))
filepoint.writelines	('\tx4230	'+	str	(p.value(	x4230	)))
filepoint.writelines	('\tx4231	'+	str	(p.value(	x4231	)))
filepoint.writelines	('\tx4232	'+	str	(p.value(	x4232	)))
filepoint.writelines	('\tx4233	'+	str	(p.value(	x4233	)))
filepoint.writelines	('\tx4234	'+	str	(p.value(	x4234	)))
filepoint.writelines	('\tx4235	'+	str	(p.value(	x4235	)))
filepoint.writelines	('\tx4236	'+	str	(p.value(	x4236	)))
filepoint.writelines	('\tx4237	'+	str	(p.value(	x4237	)))
filepoint.writelines	('\tx4238	'+	str	(p.value(	x4238	)))
filepoint.writelines	('\tx4239	'+	str	(p.value(	x4239	)))
filepoint.writelines	('\tx4240	'+	str	(p.value(	x4240	)))
filepoint.writelines	('\tx4241	'+	str	(p.value(	x4241	)))
filepoint.writelines	('\tx4242	'+	str	(p.value(	x4242	)))
filepoint.writelines	('\tx4243	'+	str	(p.value(	x4243	)))
filepoint.writelines	('\tx4244	'+	str	(p.value(	x4244	)))
filepoint.writelines	('\tx4245	'+	str	(p.value(	x4245	)))
filepoint.writelines	('\tx4246	'+	str	(p.value(	x4246	)))
filepoint.writelines	('\tx4247	'+	str	(p.value(	x4247	)))
filepoint.writelines	('\tx4248	'+	str	(p.value(	x4248	)))
filepoint.writelines	('\tx4249	'+	str	(p.value(	x4249	)))
filepoint.writelines	('\tx4250	'+	str	(p.value(	x4250	)))
filepoint.writelines	('\tx4251	'+	str	(p.value(	x4251	)))
filepoint.writelines	('\tx4252	'+	str	(p.value(	x4252	)))
filepoint.writelines	('\tx4253	'+	str	(p.value(	x4253	)))
filepoint.writelines	('\tx4254	'+	str	(p.value(	x4254	)))
filepoint.writelines	('\tx4255	'+	str	(p.value(	x4255	)))
filepoint.writelines	('\tx4256	'+	str	(p.value(	x4256	)))
filepoint.writelines	('\tx4257	'+	str	(p.value(	x4257	)))
filepoint.writelines	('\tx4258	'+	str	(p.value(	x4258	)))
filepoint.writelines	('\tx4259	'+	str	(p.value(	x4259	)))
filepoint.writelines	('\tx4260	'+	str	(p.value(	x4260	)))
filepoint.writelines	('\tx4261	'+	str	(p.value(	x4261	)))
filepoint.writelines	('\tx4262	'+	str	(p.value(	x4262	)))
filepoint.writelines	('\tx4263	'+	str	(p.value(	x4263	)))
filepoint.writelines	('\tx4264	'+	str	(p.value(	x4264	)))
filepoint.writelines	('\tx4265	'+	str	(p.value(	x4265	)))
filepoint.writelines	('\tx4266	'+	str	(p.value(	x4266	)))
filepoint.writelines	('\tx4267	'+	str	(p.value(	x4267	)))
filepoint.writelines	('\tx4268	'+	str	(p.value(	x4268	)))
filepoint.writelines	('\tx4269	'+	str	(p.value(	x4269	)))
filepoint.writelines	('\tx4270	'+	str	(p.value(	x4270	)))
filepoint.writelines	('\tx4271	'+	str	(p.value(	x4271	)))
filepoint.writelines	('\tx4272	'+	str	(p.value(	x4272	)))
filepoint.writelines	('\tx4273	'+	str	(p.value(	x4273	)))
filepoint.writelines	('\tx4274	'+	str	(p.value(	x4274	)))
filepoint.writelines	('\tx4275	'+	str	(p.value(	x4275	)))
filepoint.writelines	('\tx4276	'+	str	(p.value(	x4276	)))
filepoint.writelines	('\tx4277	'+	str	(p.value(	x4277	)))
filepoint.writelines	('\tx4278	'+	str	(p.value(	x4278	)))
filepoint.writelines	('\tx4279	'+	str	(p.value(	x4279	)))
filepoint.writelines	('\tx4280	'+	str	(p.value(	x4280	)))
filepoint.writelines	('\tx4281	'+	str	(p.value(	x4281	)))
filepoint.writelines	('\tx4282	'+	str	(p.value(	x4282	)))
filepoint.writelines	('\tx4283	'+	str	(p.value(	x4283	)))
filepoint.writelines	('\tx4284	'+	str	(p.value(	x4284	)))
filepoint.writelines	('\tx4285	'+	str	(p.value(	x4285	)))
filepoint.writelines	('\tx4286	'+	str	(p.value(	x4286	)))
filepoint.writelines	('\tx4287	'+	str	(p.value(	x4287	)))
filepoint.writelines	('\tx4288	'+	str	(p.value(	x4288	)))
filepoint.writelines	('\tx4289	'+	str	(p.value(	x4289	)))
filepoint.writelines	('\tx4290	'+	str	(p.value(	x4290	)))
filepoint.writelines	('\tx4291	'+	str	(p.value(	x4291	)))
filepoint.writelines	('\tx4292	'+	str	(p.value(	x4292	)))
filepoint.writelines	('\tx4293	'+	str	(p.value(	x4293	)))
filepoint.writelines	('\tx4294	'+	str	(p.value(	x4294	)))
filepoint.writelines	('\tx4295	'+	str	(p.value(	x4295	)))
filepoint.writelines	('\tx4296	'+	str	(p.value(	x4296	)))
filepoint.writelines	('\tx4297	'+	str	(p.value(	x4297	)))
filepoint.writelines	('\tx4298	'+	str	(p.value(	x4298	)))
filepoint.writelines	('\tx4299	'+	str	(p.value(	x4299	)))
filepoint.writelines	('\tx4300	'+	str	(p.value(	x4300	)))
filepoint.writelines	('\tx4301	'+	str	(p.value(	x4301	)))
filepoint.writelines	('\tx4302	'+	str	(p.value(	x4302	)))
filepoint.writelines	('\tx4303	'+	str	(p.value(	x4303	)))
filepoint.writelines	('\tx4304	'+	str	(p.value(	x4304	)))
filepoint.writelines	('\tx4305	'+	str	(p.value(	x4305	)))
filepoint.writelines	('\tx4306	'+	str	(p.value(	x4306	)))
filepoint.writelines	('\tx4307	'+	str	(p.value(	x4307	)))
filepoint.writelines	('\tx4308	'+	str	(p.value(	x4308	)))
filepoint.writelines	('\tx4309	'+	str	(p.value(	x4309	)))
filepoint.writelines	('\tx4310	'+	str	(p.value(	x4310	)))
filepoint.writelines	('\tx4311	'+	str	(p.value(	x4311	)))
filepoint.writelines	('\tx4312	'+	str	(p.value(	x4312	)))
filepoint.writelines	('\tx4313	'+	str	(p.value(	x4313	)))
filepoint.writelines	('\tx4314	'+	str	(p.value(	x4314	)))
filepoint.writelines	('\tx4315	'+	str	(p.value(	x4315	)))
filepoint.writelines	('\tx4316	'+	str	(p.value(	x4316	)))
filepoint.writelines	('\tx4317	'+	str	(p.value(	x4317	)))
filepoint.writelines	('\tx4318	'+	str	(p.value(	x4318	)))
filepoint.writelines	('\tx4319	'+	str	(p.value(	x4319	)))
filepoint.writelines	('\tx4320	'+	str	(p.value(	x4320	)))
filepoint.writelines	('\tx4321	'+	str	(p.value(	x4321	)))
filepoint.writelines	('\tx4322	'+	str	(p.value(	x4322	)))
filepoint.writelines	('\tx4323	'+	str	(p.value(	x4323	)))
filepoint.writelines	('\tx4324	'+	str	(p.value(	x4324	)))
filepoint.writelines	('\tx4325	'+	str	(p.value(	x4325	)))
filepoint.writelines	('\tx4326	'+	str	(p.value(	x4326	)))
filepoint.writelines	('\tx4327	'+	str	(p.value(	x4327	)))
filepoint.writelines	('\tx4328	'+	str	(p.value(	x4328	)))
filepoint.writelines	('\tx4329	'+	str	(p.value(	x4329	)))
filepoint.writelines	('\tx4330	'+	str	(p.value(	x4330	)))
filepoint.writelines	('\tx4331	'+	str	(p.value(	x4331	)))
filepoint.writelines	('\tx4332	'+	str	(p.value(	x4332	)))
filepoint.writelines	('\tx4333	'+	str	(p.value(	x4333	)))
filepoint.writelines	('\tx4334	'+	str	(p.value(	x4334	)))
filepoint.writelines	('\tx4335	'+	str	(p.value(	x4335	)))
filepoint.writelines	('\tx4336	'+	str	(p.value(	x4336	)))
filepoint.writelines	('\tx4337	'+	str	(p.value(	x4337	)))
filepoint.writelines	('\tx4338	'+	str	(p.value(	x4338	)))
filepoint.writelines	('\tx4339	'+	str	(p.value(	x4339	)))
filepoint.writelines	('\tx4340	'+	str	(p.value(	x4340	)))
filepoint.writelines	('\tx4341	'+	str	(p.value(	x4341	)))
filepoint.writelines	('\tx4342	'+	str	(p.value(	x4342	)))
filepoint.writelines	('\tx4343	'+	str	(p.value(	x4343	)))
filepoint.writelines	('\tx4344	'+	str	(p.value(	x4344	)))
filepoint.writelines	('\tx4345	'+	str	(p.value(	x4345	)))
filepoint.writelines	('\tx4346	'+	str	(p.value(	x4346	)))
filepoint.writelines	('\tx4347	'+	str	(p.value(	x4347	)))
filepoint.writelines	('\tx4348	'+	str	(p.value(	x4348	)))
filepoint.writelines	('\tx4349	'+	str	(p.value(	x4349	)))
filepoint.writelines	('\tx4350	'+	str	(p.value(	x4350	)))
filepoint.writelines	('\tx4351	'+	str	(p.value(	x4351	)))
filepoint.writelines	('\tx4352	'+	str	(p.value(	x4352	)))
filepoint.writelines	('\tx4353	'+	str	(p.value(	x4353	)))
filepoint.writelines	('\tx4354	'+	str	(p.value(	x4354	)))
filepoint.writelines	('\tx4355	'+	str	(p.value(	x4355	)))
filepoint.writelines	('\tx4356	'+	str	(p.value(	x4356	)))
filepoint.writelines	('\tx4357	'+	str	(p.value(	x4357	)))
filepoint.writelines	('\tx4358	'+	str	(p.value(	x4358	)))
filepoint.writelines	('\tx4359	'+	str	(p.value(	x4359	)))
filepoint.writelines	('\tx4360	'+	str	(p.value(	x4360	)))
filepoint.writelines	('\tx4361	'+	str	(p.value(	x4361	)))
filepoint.writelines	('\tx4362	'+	str	(p.value(	x4362	)))
filepoint.writelines	('\tx4363	'+	str	(p.value(	x4363	)))
filepoint.writelines	('\tx4364	'+	str	(p.value(	x4364	)))
filepoint.writelines	('\tx4365	'+	str	(p.value(	x4365	)))
filepoint.writelines	('\tx4366	'+	str	(p.value(	x4366	)))
filepoint.writelines	('\tx4367	'+	str	(p.value(	x4367	)))
filepoint.writelines	('\tx4368	'+	str	(p.value(	x4368	)))
filepoint.writelines	('\tx4369	'+	str	(p.value(	x4369	)))
filepoint.writelines	('\tx4370	'+	str	(p.value(	x4370	)))
filepoint.writelines	('\tx4371	'+	str	(p.value(	x4371	)))
filepoint.writelines	('\tx4372	'+	str	(p.value(	x4372	)))
filepoint.writelines	('\tx4373	'+	str	(p.value(	x4373	)))
filepoint.writelines	('\tx4374	'+	str	(p.value(	x4374	)))
filepoint.writelines	('\tx4375	'+	str	(p.value(	x4375	)))
filepoint.writelines	('\tx4376	'+	str	(p.value(	x4376	)))
filepoint.writelines	('\tx4377	'+	str	(p.value(	x4377	)))
filepoint.writelines	('\tx4378	'+	str	(p.value(	x4378	)))
filepoint.writelines	('\tx4379	'+	str	(p.value(	x4379	)))
filepoint.writelines	('\tx4380	'+	str	(p.value(	x4380	)))
filepoint.writelines	('\tx4381	'+	str	(p.value(	x4381	)))
filepoint.writelines	('\tx4382	'+	str	(p.value(	x4382	)))
filepoint.writelines	('\tx4383	'+	str	(p.value(	x4383	)))
filepoint.writelines	('\tx4384	'+	str	(p.value(	x4384	)))
filepoint.writelines	('\tx4385	'+	str	(p.value(	x4385	)))
filepoint.writelines	('\tx4386	'+	str	(p.value(	x4386	)))
filepoint.writelines	('\tx4387	'+	str	(p.value(	x4387	)))
filepoint.writelines	('\tx4388	'+	str	(p.value(	x4388	)))
filepoint.writelines	('\tx4389	'+	str	(p.value(	x4389	)))
filepoint.writelines	('\tx4390	'+	str	(p.value(	x4390	)))
filepoint.writelines	('\tx4391	'+	str	(p.value(	x4391	)))
filepoint.writelines	('\tx4392	'+	str	(p.value(	x4392	)))
filepoint.writelines	('\tx4393	'+	str	(p.value(	x4393	)))
filepoint.writelines	('\tx4394	'+	str	(p.value(	x4394	)))
filepoint.writelines	('\tx4395	'+	str	(p.value(	x4395	)))
filepoint.writelines	('\tx4396	'+	str	(p.value(	x4396	)))
filepoint.writelines	('\tx4397	'+	str	(p.value(	x4397	)))
filepoint.writelines	('\tx4398	'+	str	(p.value(	x4398	)))
filepoint.writelines	('\tx4399	'+	str	(p.value(	x4399	)))
filepoint.writelines	('\tx4400	'+	str	(p.value(	x4400	)))
filepoint.writelines	('\tx4401	'+	str	(p.value(	x4401	)))
filepoint.writelines	('\tx4402	'+	str	(p.value(	x4402	)))
filepoint.writelines	('\tx4403	'+	str	(p.value(	x4403	)))
filepoint.writelines	('\tx4404	'+	str	(p.value(	x4404	)))
filepoint.writelines	('\tx4405	'+	str	(p.value(	x4405	)))
filepoint.writelines	('\tx4406	'+	str	(p.value(	x4406	)))
filepoint.writelines	('\tx4407	'+	str	(p.value(	x4407	)))
filepoint.writelines	('\tx4408	'+	str	(p.value(	x4408	)))
filepoint.writelines	('\tx4409	'+	str	(p.value(	x4409	)))
filepoint.writelines	('\tx4410	'+	str	(p.value(	x4410	)))
filepoint.writelines	('\tx4411	'+	str	(p.value(	x4411	)))
filepoint.writelines	('\tx4412	'+	str	(p.value(	x4412	)))
filepoint.writelines	('\tx4413	'+	str	(p.value(	x4413	)))
filepoint.writelines	('\tx4414	'+	str	(p.value(	x4414	)))
filepoint.writelines	('\tx4415	'+	str	(p.value(	x4415	)))
filepoint.writelines	('\tx4416	'+	str	(p.value(	x4416	)))
filepoint.writelines	('\tx4417	'+	str	(p.value(	x4417	)))
filepoint.writelines	('\tx4418	'+	str	(p.value(	x4418	)))
filepoint.writelines	('\tx4419	'+	str	(p.value(	x4419	)))
filepoint.writelines	('\tx4420	'+	str	(p.value(	x4420	)))
filepoint.writelines	('\tx4421	'+	str	(p.value(	x4421	)))
filepoint.writelines	('\tx4422	'+	str	(p.value(	x4422	)))
filepoint.writelines	('\tx4423	'+	str	(p.value(	x4423	)))
filepoint.writelines	('\tx4424	'+	str	(p.value(	x4424	)))
filepoint.writelines	('\tx4425	'+	str	(p.value(	x4425	)))
filepoint.writelines	('\tx4426	'+	str	(p.value(	x4426	)))
filepoint.writelines	('\tx4427	'+	str	(p.value(	x4427	)))
filepoint.writelines	('\tx4428	'+	str	(p.value(	x4428	)))
filepoint.writelines	('\tx4429	'+	str	(p.value(	x4429	)))
filepoint.writelines	('\tx4430	'+	str	(p.value(	x4430	)))
filepoint.writelines	('\tx4431	'+	str	(p.value(	x4431	)))
filepoint.writelines	('\tx4432	'+	str	(p.value(	x4432	)))
filepoint.writelines	('\tx4433	'+	str	(p.value(	x4433	)))
filepoint.writelines	('\tx4434	'+	str	(p.value(	x4434	)))
filepoint.writelines	('\tx4435	'+	str	(p.value(	x4435	)))
filepoint.writelines	('\tx4436	'+	str	(p.value(	x4436	)))
filepoint.writelines	('\tx4437	'+	str	(p.value(	x4437	)))
filepoint.writelines	('\tx4438	'+	str	(p.value(	x4438	)))
filepoint.writelines	('\tx4439	'+	str	(p.value(	x4439	)))
filepoint.writelines	('\tx4440	'+	str	(p.value(	x4440	)))
filepoint.writelines	('\tx4441	'+	str	(p.value(	x4441	)))
filepoint.writelines	('\tx4442	'+	str	(p.value(	x4442	)))
filepoint.writelines	('\tx4443	'+	str	(p.value(	x4443	)))
filepoint.writelines	('\tx4444	'+	str	(p.value(	x4444	)))
filepoint.writelines	('\tx4445	'+	str	(p.value(	x4445	)))
filepoint.writelines	('\tx4446	'+	str	(p.value(	x4446	)))
filepoint.writelines	('\tx4447	'+	str	(p.value(	x4447	)))
filepoint.writelines	('\tx4448	'+	str	(p.value(	x4448	)))
filepoint.writelines	('\tx4449	'+	str	(p.value(	x4449	)))
filepoint.writelines	('\tx4450	'+	str	(p.value(	x4450	)))
filepoint.writelines	('\tx4451	'+	str	(p.value(	x4451	)))
filepoint.writelines	('\tx4452	'+	str	(p.value(	x4452	)))
filepoint.writelines	('\tx4453	'+	str	(p.value(	x4453	)))
filepoint.writelines	('\tx4454	'+	str	(p.value(	x4454	)))
filepoint.writelines	('\tx4455	'+	str	(p.value(	x4455	)))
filepoint.writelines	('\tx4456	'+	str	(p.value(	x4456	)))
filepoint.writelines	('\tx4457	'+	str	(p.value(	x4457	)))
filepoint.writelines	('\tx4458	'+	str	(p.value(	x4458	)))
filepoint.writelines	('\tx4459	'+	str	(p.value(	x4459	)))
filepoint.writelines	('\tx4460	'+	str	(p.value(	x4460	)))
filepoint.writelines	('\tx4461	'+	str	(p.value(	x4461	)))
filepoint.writelines	('\tx4462	'+	str	(p.value(	x4462	)))
filepoint.writelines	('\tx4463	'+	str	(p.value(	x4463	)))
filepoint.writelines	('\tx4464	'+	str	(p.value(	x4464	)))
filepoint.writelines	('\tx4465	'+	str	(p.value(	x4465	)))
filepoint.writelines	('\tx4466	'+	str	(p.value(	x4466	)))
filepoint.writelines	('\tx4467	'+	str	(p.value(	x4467	)))
filepoint.writelines	('\tx4468	'+	str	(p.value(	x4468	)))
filepoint.writelines	('\tx4469	'+	str	(p.value(	x4469	)))
filepoint.writelines	('\tx4470	'+	str	(p.value(	x4470	)))
filepoint.writelines	('\tx4471	'+	str	(p.value(	x4471	)))
filepoint.writelines	('\tx4472	'+	str	(p.value(	x4472	)))
filepoint.writelines	('\tx4473	'+	str	(p.value(	x4473	)))
filepoint.writelines	('\tx4474	'+	str	(p.value(	x4474	)))
filepoint.writelines	('\tx4475	'+	str	(p.value(	x4475	)))
filepoint.writelines	('\tx4476	'+	str	(p.value(	x4476	)))
filepoint.writelines	('\tx4477	'+	str	(p.value(	x4477	)))
filepoint.writelines	('\tx4478	'+	str	(p.value(	x4478	)))
filepoint.writelines	('\tx4479	'+	str	(p.value(	x4479	)))
filepoint.writelines	('\tx4480	'+	str	(p.value(	x4480	)))
filepoint.writelines	('\tx4481	'+	str	(p.value(	x4481	)))
filepoint.writelines	('\tx4482	'+	str	(p.value(	x4482	)))
filepoint.writelines	('\tx4483	'+	str	(p.value(	x4483	)))
filepoint.writelines	('\tx4484	'+	str	(p.value(	x4484	)))
filepoint.writelines	('\tx4485	'+	str	(p.value(	x4485	)))
filepoint.writelines	('\tx4486	'+	str	(p.value(	x4486	)))
filepoint.writelines	('\tx4487	'+	str	(p.value(	x4487	)))
filepoint.writelines	('\tx4488	'+	str	(p.value(	x4488	)))
filepoint.writelines	('\tx4489	'+	str	(p.value(	x4489	)))
filepoint.writelines	('\tx4490	'+	str	(p.value(	x4490	)))
filepoint.writelines	('\tx4491	'+	str	(p.value(	x4491	)))
filepoint.writelines	('\tx4492	'+	str	(p.value(	x4492	)))
filepoint.writelines	('\tx4493	'+	str	(p.value(	x4493	)))
filepoint.writelines	('\tx4494	'+	str	(p.value(	x4494	)))
filepoint.writelines	('\tx4495	'+	str	(p.value(	x4495	)))
filepoint.writelines	('\tx4496	'+	str	(p.value(	x4496	)))
filepoint.writelines	('\tx4497	'+	str	(p.value(	x4497	)))
filepoint.writelines	('\tx4498	'+	str	(p.value(	x4498	)))
filepoint.writelines	('\tx4499	'+	str	(p.value(	x4499	)))
filepoint.writelines	('\tx4500	'+	str	(p.value(	x4500	)))
filepoint.writelines	('\tx4501	'+	str	(p.value(	x4501	)))
filepoint.writelines	('\tx4502	'+	str	(p.value(	x4502	)))
filepoint.writelines	('\tx4503	'+	str	(p.value(	x4503	)))
filepoint.writelines	('\tx4504	'+	str	(p.value(	x4504	)))
filepoint.writelines	('\tx4505	'+	str	(p.value(	x4505	)))
filepoint.writelines	('\tx4506	'+	str	(p.value(	x4506	)))
filepoint.writelines	('\tx4507	'+	str	(p.value(	x4507	)))
filepoint.writelines	('\tx4508	'+	str	(p.value(	x4508	)))
filepoint.writelines	('\tx4509	'+	str	(p.value(	x4509	)))
filepoint.writelines	('\tx4510	'+	str	(p.value(	x4510	)))
filepoint.writelines	('\tx4511	'+	str	(p.value(	x4511	)))
filepoint.writelines	('\tx4512	'+	str	(p.value(	x4512	)))
filepoint.writelines	('\tx4513	'+	str	(p.value(	x4513	)))
filepoint.writelines	('\tx4514	'+	str	(p.value(	x4514	)))
filepoint.writelines	('\tx4515	'+	str	(p.value(	x4515	)))
filepoint.writelines	('\tx4516	'+	str	(p.value(	x4516	)))
filepoint.writelines	('\tx4517	'+	str	(p.value(	x4517	)))
filepoint.writelines	('\tx4518	'+	str	(p.value(	x4518	)))
filepoint.writelines	('\tx4519	'+	str	(p.value(	x4519	)))
filepoint.writelines	('\tx4520	'+	str	(p.value(	x4520	)))
filepoint.writelines	('\tx4521	'+	str	(p.value(	x4521	)))
filepoint.writelines	('\tx4522	'+	str	(p.value(	x4522	)))
filepoint.writelines	('\tx4523	'+	str	(p.value(	x4523	)))
filepoint.writelines	('\tx4524	'+	str	(p.value(	x4524	)))
filepoint.writelines	('\tx4525	'+	str	(p.value(	x4525	)))
filepoint.writelines	('\tx4526	'+	str	(p.value(	x4526	)))
filepoint.writelines	('\tx4527	'+	str	(p.value(	x4527	)))
filepoint.writelines	('\tx4528	'+	str	(p.value(	x4528	)))
filepoint.writelines	('\tx4529	'+	str	(p.value(	x4529	)))
filepoint.writelines	('\tx4530	'+	str	(p.value(	x4530	)))
filepoint.writelines	('\tx4531	'+	str	(p.value(	x4531	)))
filepoint.writelines	('\tx4532	'+	str	(p.value(	x4532	)))
filepoint.writelines	('\tx4533	'+	str	(p.value(	x4533	)))
filepoint.writelines	('\tx4534	'+	str	(p.value(	x4534	)))
filepoint.writelines	('\tx4535	'+	str	(p.value(	x4535	)))
filepoint.writelines	('\tx4536	'+	str	(p.value(	x4536	)))
filepoint.writelines	('\tx4537	'+	str	(p.value(	x4537	)))
filepoint.writelines	('\tx4538	'+	str	(p.value(	x4538	)))
filepoint.writelines	('\tx4539	'+	str	(p.value(	x4539	)))
filepoint.writelines	('\tx4540	'+	str	(p.value(	x4540	)))
filepoint.writelines	('\tx4541	'+	str	(p.value(	x4541	)))
filepoint.writelines	('\tx4542	'+	str	(p.value(	x4542	)))
filepoint.writelines	('\tx4543	'+	str	(p.value(	x4543	)))
filepoint.writelines	('\tx4544	'+	str	(p.value(	x4544	)))
filepoint.writelines	('\tx4545	'+	str	(p.value(	x4545	)))
filepoint.writelines	('\tx4546	'+	str	(p.value(	x4546	)))
filepoint.writelines	('\tx4547	'+	str	(p.value(	x4547	)))
filepoint.writelines	('\tx4548	'+	str	(p.value(	x4548	)))
filepoint.writelines	('\tx4549	'+	str	(p.value(	x4549	)))
filepoint.writelines	('\tx4550	'+	str	(p.value(	x4550	)))
filepoint.writelines	('\tx4551	'+	str	(p.value(	x4551	)))
filepoint.writelines	('\tx4552	'+	str	(p.value(	x4552	)))
filepoint.writelines	('\tx4553	'+	str	(p.value(	x4553	)))
filepoint.writelines	('\tx4554	'+	str	(p.value(	x4554	)))
filepoint.writelines	('\tx4555	'+	str	(p.value(	x4555	)))
filepoint.writelines	('\tx4556	'+	str	(p.value(	x4556	)))
filepoint.writelines	('\tx4557	'+	str	(p.value(	x4557	)))
filepoint.writelines	('\tx4558	'+	str	(p.value(	x4558	)))
filepoint.writelines	('\tx4559	'+	str	(p.value(	x4559	)))
filepoint.writelines	('\tx4560	'+	str	(p.value(	x4560	)))
filepoint.writelines	('\tx4561	'+	str	(p.value(	x4561	)))
filepoint.writelines	('\tx4562	'+	str	(p.value(	x4562	)))
filepoint.writelines	('\tx4563	'+	str	(p.value(	x4563	)))
filepoint.writelines	('\tx4564	'+	str	(p.value(	x4564	)))
filepoint.writelines	('\tx4565	'+	str	(p.value(	x4565	)))
filepoint.writelines	('\tx4566	'+	str	(p.value(	x4566	)))
filepoint.writelines	('\tx4567	'+	str	(p.value(	x4567	)))
filepoint.writelines	('\tx4568	'+	str	(p.value(	x4568	)))
filepoint.writelines	('\tx4569	'+	str	(p.value(	x4569	)))
filepoint.writelines	('\tx4570	'+	str	(p.value(	x4570	)))
filepoint.writelines	('\tx4571	'+	str	(p.value(	x4571	)))
filepoint.writelines	('\tx4572	'+	str	(p.value(	x4572	)))
filepoint.writelines	('\tx4573	'+	str	(p.value(	x4573	)))
filepoint.writelines	('\tx4574	'+	str	(p.value(	x4574	)))
filepoint.writelines	('\tx4575	'+	str	(p.value(	x4575	)))
filepoint.writelines	('\tx4576	'+	str	(p.value(	x4576	)))
filepoint.writelines	('\tx4577	'+	str	(p.value(	x4577	)))
filepoint.writelines	('\tx4578	'+	str	(p.value(	x4578	)))
filepoint.writelines	('\tx4579	'+	str	(p.value(	x4579	)))
filepoint.writelines	('\tx4580	'+	str	(p.value(	x4580	)))
filepoint.writelines	('\tx4581	'+	str	(p.value(	x4581	)))
filepoint.writelines	('\tx4582	'+	str	(p.value(	x4582	)))
filepoint.writelines	('\tx4583	'+	str	(p.value(	x4583	)))
filepoint.writelines	('\tx4584	'+	str	(p.value(	x4584	)))
filepoint.writelines	('\tx4585	'+	str	(p.value(	x4585	)))
filepoint.writelines	('\tx4586	'+	str	(p.value(	x4586	)))
filepoint.writelines	('\tx4587	'+	str	(p.value(	x4587	)))
filepoint.writelines	('\tx4588	'+	str	(p.value(	x4588	)))
filepoint.writelines	('\tx4589	'+	str	(p.value(	x4589	)))
filepoint.writelines	('\tx4590	'+	str	(p.value(	x4590	)))
filepoint.writelines	('\tx4591	'+	str	(p.value(	x4591	)))
filepoint.writelines	('\tx4592	'+	str	(p.value(	x4592	)))
filepoint.writelines	('\tx4593	'+	str	(p.value(	x4593	)))
filepoint.writelines	('\tx4594	'+	str	(p.value(	x4594	)))
filepoint.writelines	('\tx4595	'+	str	(p.value(	x4595	)))
filepoint.writelines	('\tx4596	'+	str	(p.value(	x4596	)))
filepoint.writelines	('\tx4597	'+	str	(p.value(	x4597	)))
filepoint.writelines	('\tx4598	'+	str	(p.value(	x4598	)))
filepoint.writelines	('\tx4599	'+	str	(p.value(	x4599	)))
filepoint.writelines	('\tx4600	'+	str	(p.value(	x4600	)))
filepoint.writelines	('\tx4601	'+	str	(p.value(	x4601	)))
filepoint.writelines	('\tx4602	'+	str	(p.value(	x4602	)))
filepoint.writelines	('\tx4603	'+	str	(p.value(	x4603	)))
filepoint.writelines	('\tx4604	'+	str	(p.value(	x4604	)))
filepoint.writelines	('\tx4605	'+	str	(p.value(	x4605	)))
filepoint.writelines	('\tx4606	'+	str	(p.value(	x4606	)))
filepoint.writelines	('\tx4607	'+	str	(p.value(	x4607	)))
filepoint.writelines	('\tx4608	'+	str	(p.value(	x4608	)))
filepoint.writelines	('\tx4609	'+	str	(p.value(	x4609	)))
filepoint.writelines	('\tx4610	'+	str	(p.value(	x4610	)))
filepoint.writelines	('\tx4611	'+	str	(p.value(	x4611	)))
filepoint.writelines	('\tx4612	'+	str	(p.value(	x4612	)))
filepoint.writelines	('\tx4613	'+	str	(p.value(	x4613	)))
filepoint.writelines	('\tx4614	'+	str	(p.value(	x4614	)))
filepoint.writelines	('\tx4615	'+	str	(p.value(	x4615	)))
filepoint.writelines	('\tx4616	'+	str	(p.value(	x4616	)))
filepoint.writelines	('\tx4617	'+	str	(p.value(	x4617	)))
filepoint.writelines	('\tx4618	'+	str	(p.value(	x4618	)))
filepoint.writelines	('\tx4619	'+	str	(p.value(	x4619	)))
filepoint.writelines	('\tx4620	'+	str	(p.value(	x4620	)))
filepoint.writelines	('\tx4621	'+	str	(p.value(	x4621	)))
filepoint.writelines	('\tx4622	'+	str	(p.value(	x4622	)))
filepoint.writelines	('\tx4623	'+	str	(p.value(	x4623	)))
filepoint.writelines	('\tx4624	'+	str	(p.value(	x4624	)))
filepoint.writelines	('\tx4625	'+	str	(p.value(	x4625	)))
filepoint.writelines	('\tx4626	'+	str	(p.value(	x4626	)))
filepoint.writelines	('\tx4627	'+	str	(p.value(	x4627	)))
filepoint.writelines	('\tx4628	'+	str	(p.value(	x4628	)))
filepoint.writelines	('\tx4629	'+	str	(p.value(	x4629	)))
filepoint.writelines	('\tx4630	'+	str	(p.value(	x4630	)))
filepoint.writelines	('\tx4631	'+	str	(p.value(	x4631	)))
filepoint.writelines	('\tx4632	'+	str	(p.value(	x4632	)))
filepoint.writelines	('\tx4633	'+	str	(p.value(	x4633	)))
filepoint.writelines	('\tx4634	'+	str	(p.value(	x4634	)))
filepoint.writelines	('\tx4635	'+	str	(p.value(	x4635	)))
filepoint.writelines	('\tx4636	'+	str	(p.value(	x4636	)))
filepoint.writelines	('\tx4637	'+	str	(p.value(	x4637	)))
filepoint.writelines	('\tx4638	'+	str	(p.value(	x4638	)))
filepoint.writelines	('\tx4639	'+	str	(p.value(	x4639	)))
filepoint.writelines	('\tx4640	'+	str	(p.value(	x4640	)))
filepoint.writelines	('\tx4641	'+	str	(p.value(	x4641	)))
filepoint.writelines	('\tx4642	'+	str	(p.value(	x4642	)))
filepoint.writelines	('\tx4643	'+	str	(p.value(	x4643	)))
filepoint.writelines	('\tx4644	'+	str	(p.value(	x4644	)))
filepoint.writelines	('\tx4645	'+	str	(p.value(	x4645	)))
filepoint.writelines	('\tx4646	'+	str	(p.value(	x4646	)))
filepoint.writelines	('\tx4647	'+	str	(p.value(	x4647	)))
filepoint.writelines	('\tx4648	'+	str	(p.value(	x4648	)))
filepoint.writelines	('\tx4649	'+	str	(p.value(	x4649	)))
filepoint.writelines	('\tx4650	'+	str	(p.value(	x4650	)))
filepoint.writelines	('\tx4651	'+	str	(p.value(	x4651	)))
filepoint.writelines	('\tx4652	'+	str	(p.value(	x4652	)))
filepoint.writelines	('\tx4653	'+	str	(p.value(	x4653	)))
filepoint.writelines	('\tx4654	'+	str	(p.value(	x4654	)))
filepoint.writelines	('\tx4655	'+	str	(p.value(	x4655	)))
filepoint.writelines	('\tx4656	'+	str	(p.value(	x4656	)))
filepoint.writelines	('\tx4657	'+	str	(p.value(	x4657	)))
filepoint.writelines	('\tx4658	'+	str	(p.value(	x4658	)))
filepoint.writelines	('\tx4659	'+	str	(p.value(	x4659	)))
filepoint.writelines	('\tx4660	'+	str	(p.value(	x4660	)))
filepoint.writelines	('\tx4661	'+	str	(p.value(	x4661	)))
filepoint.writelines	('\tx4662	'+	str	(p.value(	x4662	)))
filepoint.writelines	('\tx4663	'+	str	(p.value(	x4663	)))
filepoint.writelines	('\tx4664	'+	str	(p.value(	x4664	)))
filepoint.writelines	('\tx4665	'+	str	(p.value(	x4665	)))
filepoint.writelines	('\tx4666	'+	str	(p.value(	x4666	)))
filepoint.writelines	('\tx4667	'+	str	(p.value(	x4667	)))
filepoint.writelines	('\tx4668	'+	str	(p.value(	x4668	)))
filepoint.writelines	('\tx4669	'+	str	(p.value(	x4669	)))
filepoint.writelines	('\tx4670	'+	str	(p.value(	x4670	)))
filepoint.writelines	('\tx4671	'+	str	(p.value(	x4671	)))
filepoint.writelines	('\tx4672	'+	str	(p.value(	x4672	)))
filepoint.writelines	('\tx4673	'+	str	(p.value(	x4673	)))
filepoint.writelines	('\tx4674	'+	str	(p.value(	x4674	)))
filepoint.writelines	('\tx4675	'+	str	(p.value(	x4675	)))
filepoint.writelines	('\tx4676	'+	str	(p.value(	x4676	)))
filepoint.writelines	('\tx4677	'+	str	(p.value(	x4677	)))
filepoint.writelines	('\tx4678	'+	str	(p.value(	x4678	)))
filepoint.writelines	('\tx4679	'+	str	(p.value(	x4679	)))
filepoint.writelines	('\tx4680	'+	str	(p.value(	x4680	)))
filepoint.writelines	('\tx4681	'+	str	(p.value(	x4681	)))
filepoint.writelines	('\tx4682	'+	str	(p.value(	x4682	)))
filepoint.writelines	('\tx4683	'+	str	(p.value(	x4683	)))
filepoint.writelines	('\tx4684	'+	str	(p.value(	x4684	)))
filepoint.writelines	('\tx4685	'+	str	(p.value(	x4685	)))
filepoint.writelines	('\tx4686	'+	str	(p.value(	x4686	)))
filepoint.writelines	('\tx4687	'+	str	(p.value(	x4687	)))
filepoint.writelines	('\tx4688	'+	str	(p.value(	x4688	)))
filepoint.writelines	('\tx4689	'+	str	(p.value(	x4689	)))
filepoint.writelines	('\tx4690	'+	str	(p.value(	x4690	)))
filepoint.writelines	('\tx4691	'+	str	(p.value(	x4691	)))
filepoint.writelines	('\tx4692	'+	str	(p.value(	x4692	)))
filepoint.writelines	('\tx4693	'+	str	(p.value(	x4693	)))
filepoint.writelines	('\tx4694	'+	str	(p.value(	x4694	)))
filepoint.writelines	('\tx4695	'+	str	(p.value(	x4695	)))
filepoint.writelines	('\tx4696	'+	str	(p.value(	x4696	)))
filepoint.writelines	('\tx4697	'+	str	(p.value(	x4697	)))
filepoint.writelines	('\tx4698	'+	str	(p.value(	x4698	)))
filepoint.writelines	('\tx4699	'+	str	(p.value(	x4699	)))
filepoint.writelines	('\tx4700	'+	str	(p.value(	x4700	)))
filepoint.writelines	('\tx4701	'+	str	(p.value(	x4701	)))
filepoint.writelines	('\tx4702	'+	str	(p.value(	x4702	)))
filepoint.writelines	('\tx4703	'+	str	(p.value(	x4703	)))
filepoint.writelines	('\tx4704	'+	str	(p.value(	x4704	)))
filepoint.writelines	('\tx4705	'+	str	(p.value(	x4705	)))
filepoint.writelines	('\tx4706	'+	str	(p.value(	x4706	)))
filepoint.writelines	('\tx4707	'+	str	(p.value(	x4707	)))
filepoint.writelines	('\tx4708	'+	str	(p.value(	x4708	)))
filepoint.writelines	('\tx4709	'+	str	(p.value(	x4709	)))
filepoint.writelines	('\tx4710	'+	str	(p.value(	x4710	)))
filepoint.writelines	('\tx4711	'+	str	(p.value(	x4711	)))
filepoint.writelines	('\tx4712	'+	str	(p.value(	x4712	)))
filepoint.writelines	('\tx4713	'+	str	(p.value(	x4713	)))
filepoint.writelines	('\tx4714	'+	str	(p.value(	x4714	)))
filepoint.writelines	('\tx4715	'+	str	(p.value(	x4715	)))
filepoint.writelines	('\tx4716	'+	str	(p.value(	x4716	)))
filepoint.writelines	('\tx4717	'+	str	(p.value(	x4717	)))
filepoint.writelines	('\tx4718	'+	str	(p.value(	x4718	)))
filepoint.writelines	('\tx4719	'+	str	(p.value(	x4719	)))
filepoint.writelines	('\tx4720	'+	str	(p.value(	x4720	)))
filepoint.writelines	('\tx4721	'+	str	(p.value(	x4721	)))
filepoint.writelines	('\tx4722	'+	str	(p.value(	x4722	)))
filepoint.writelines	('\tx4723	'+	str	(p.value(	x4723	)))
filepoint.writelines	('\tx4724	'+	str	(p.value(	x4724	)))
filepoint.writelines	('\tx4725	'+	str	(p.value(	x4725	)))
filepoint.writelines	('\tx4726	'+	str	(p.value(	x4726	)))
filepoint.writelines	('\tx4727	'+	str	(p.value(	x4727	)))
filepoint.writelines	('\tx4728	'+	str	(p.value(	x4728	)))
filepoint.writelines	('\tx4729	'+	str	(p.value(	x4729	)))
filepoint.writelines	('\tx4730	'+	str	(p.value(	x4730	)))
filepoint.writelines	('\tx4731	'+	str	(p.value(	x4731	)))
filepoint.writelines	('\tx4732	'+	str	(p.value(	x4732	)))
filepoint.writelines	('\tx4733	'+	str	(p.value(	x4733	)))
filepoint.writelines	('\tx4734	'+	str	(p.value(	x4734	)))
filepoint.writelines	('\tx4735	'+	str	(p.value(	x4735	)))
filepoint.writelines	('\tx4736	'+	str	(p.value(	x4736	)))
filepoint.writelines	('\tx4737	'+	str	(p.value(	x4737	)))
filepoint.writelines	('\tx4738	'+	str	(p.value(	x4738	)))
filepoint.writelines	('\tx4739	'+	str	(p.value(	x4739	)))
filepoint.writelines	('\tx4740	'+	str	(p.value(	x4740	)))
filepoint.writelines	('\tx4741	'+	str	(p.value(	x4741	)))
filepoint.writelines	('\tx4742	'+	str	(p.value(	x4742	)))
filepoint.writelines	('\tx4743	'+	str	(p.value(	x4743	)))
filepoint.writelines	('\tx4744	'+	str	(p.value(	x4744	)))
filepoint.writelines	('\tx4745	'+	str	(p.value(	x4745	)))
filepoint.writelines	('\tx4746	'+	str	(p.value(	x4746	)))
filepoint.writelines	('\tx4747	'+	str	(p.value(	x4747	)))
filepoint.writelines	('\tx4748	'+	str	(p.value(	x4748	)))
filepoint.writelines	('\tx4749	'+	str	(p.value(	x4749	)))
filepoint.writelines	('\tx4750	'+	str	(p.value(	x4750	)))
filepoint.writelines	('\tx4751	'+	str	(p.value(	x4751	)))
filepoint.writelines	('\tx4752	'+	str	(p.value(	x4752	)))
filepoint.writelines	('\tx4753	'+	str	(p.value(	x4753	)))
filepoint.writelines	('\tx4754	'+	str	(p.value(	x4754	)))
filepoint.writelines	('\tx4755	'+	str	(p.value(	x4755	)))
filepoint.writelines	('\tx4756	'+	str	(p.value(	x4756	)))
filepoint.writelines	('\tx4757	'+	str	(p.value(	x4757	)))
filepoint.writelines	('\tx4758	'+	str	(p.value(	x4758	)))
filepoint.writelines	('\tx4759	'+	str	(p.value(	x4759	)))
filepoint.writelines	('\tx4760	'+	str	(p.value(	x4760	)))
filepoint.writelines	('\tx4761	'+	str	(p.value(	x4761	)))
filepoint.writelines	('\tx4762	'+	str	(p.value(	x4762	)))
filepoint.writelines	('\tx4763	'+	str	(p.value(	x4763	)))
filepoint.writelines	('\tx4764	'+	str	(p.value(	x4764	)))
filepoint.writelines	('\tx4765	'+	str	(p.value(	x4765	)))
filepoint.writelines	('\tx4766	'+	str	(p.value(	x4766	)))
filepoint.writelines	('\tx4767	'+	str	(p.value(	x4767	)))
filepoint.writelines	('\tx4768	'+	str	(p.value(	x4768	)))
filepoint.writelines	('\tx4769	'+	str	(p.value(	x4769	)))
filepoint.writelines	('\tx4770	'+	str	(p.value(	x4770	)))
filepoint.writelines	('\tx4771	'+	str	(p.value(	x4771	)))
filepoint.writelines	('\tx4772	'+	str	(p.value(	x4772	)))
filepoint.writelines	('\tx4773	'+	str	(p.value(	x4773	)))
filepoint.writelines	('\tx4774	'+	str	(p.value(	x4774	)))
filepoint.writelines	('\tx4775	'+	str	(p.value(	x4775	)))
filepoint.writelines	('\tx4776	'+	str	(p.value(	x4776	)))
filepoint.writelines	('\tx4777	'+	str	(p.value(	x4777	)))
filepoint.writelines	('\tx4778	'+	str	(p.value(	x4778	)))
filepoint.writelines	('\tx4779	'+	str	(p.value(	x4779	)))
filepoint.writelines	('\tx4780	'+	str	(p.value(	x4780	)))
filepoint.writelines	('\tx4781	'+	str	(p.value(	x4781	)))
filepoint.writelines	('\tx4782	'+	str	(p.value(	x4782	)))
filepoint.writelines	('\tx4783	'+	str	(p.value(	x4783	)))
filepoint.writelines	('\tx4784	'+	str	(p.value(	x4784	)))
filepoint.writelines	('\tx4785	'+	str	(p.value(	x4785	)))
filepoint.writelines	('\tx4786	'+	str	(p.value(	x4786	)))
filepoint.writelines	('\tx4787	'+	str	(p.value(	x4787	)))
filepoint.writelines	('\tx4788	'+	str	(p.value(	x4788	)))
filepoint.writelines	('\tx4789	'+	str	(p.value(	x4789	)))
filepoint.writelines	('\tx4790	'+	str	(p.value(	x4790	)))
filepoint.writelines	('\tx4791	'+	str	(p.value(	x4791	)))
filepoint.writelines	('\tx4792	'+	str	(p.value(	x4792	)))
filepoint.writelines	('\tx4793	'+	str	(p.value(	x4793	)))
filepoint.writelines	('\tx4794	'+	str	(p.value(	x4794	)))
filepoint.writelines	('\tx4795	'+	str	(p.value(	x4795	)))
filepoint.writelines	('\tx4796	'+	str	(p.value(	x4796	)))
filepoint.writelines	('\tx4797	'+	str	(p.value(	x4797	)))
filepoint.writelines	('\tx4798	'+	str	(p.value(	x4798	)))
filepoint.writelines	('\tx4799	'+	str	(p.value(	x4799	)))
filepoint.writelines	('\tx4800	'+	str	(p.value(	x4800	)))
filepoint.writelines	('\tx4801	'+	str	(p.value(	x4801	)))
filepoint.writelines	('\tx4802	'+	str	(p.value(	x4802	)))
filepoint.writelines	('\tx4803	'+	str	(p.value(	x4803	)))
filepoint.writelines	('\tx4804	'+	str	(p.value(	x4804	)))
filepoint.writelines	('\tx4805	'+	str	(p.value(	x4805	)))
filepoint.writelines	('\tx4806	'+	str	(p.value(	x4806	)))
filepoint.writelines	('\tx4807	'+	str	(p.value(	x4807	)))
filepoint.writelines	('\tx4808	'+	str	(p.value(	x4808	)))
filepoint.writelines	('\tx4809	'+	str	(p.value(	x4809	)))
filepoint.writelines	('\tx4810	'+	str	(p.value(	x4810	)))
filepoint.writelines	('\tx4811	'+	str	(p.value(	x4811	)))
filepoint.writelines	('\tx4812	'+	str	(p.value(	x4812	)))
filepoint.writelines	('\tx4813	'+	str	(p.value(	x4813	)))
filepoint.writelines	('\tx4814	'+	str	(p.value(	x4814	)))
filepoint.writelines	('\tx4815	'+	str	(p.value(	x4815	)))
filepoint.writelines	('\tx4816	'+	str	(p.value(	x4816	)))
filepoint.writelines	('\tx4817	'+	str	(p.value(	x4817	)))
filepoint.writelines	('\tx4818	'+	str	(p.value(	x4818	)))
filepoint.writelines	('\tx4819	'+	str	(p.value(	x4819	)))
filepoint.writelines	('\tx4820	'+	str	(p.value(	x4820	)))
filepoint.writelines	('\tx4821	'+	str	(p.value(	x4821	)))
filepoint.writelines	('\tx4822	'+	str	(p.value(	x4822	)))
filepoint.writelines	('\tx4823	'+	str	(p.value(	x4823	)))
filepoint.writelines	('\tx4824	'+	str	(p.value(	x4824	)))
filepoint.writelines	('\tx4825	'+	str	(p.value(	x4825	)))
filepoint.writelines	('\tx4826	'+	str	(p.value(	x4826	)))
filepoint.writelines	('\tx4827	'+	str	(p.value(	x4827	)))
filepoint.writelines	('\tx4828	'+	str	(p.value(	x4828	)))
filepoint.writelines	('\tx4829	'+	str	(p.value(	x4829	)))
filepoint.writelines	('\tx4830	'+	str	(p.value(	x4830	)))
filepoint.writelines	('\tx4831	'+	str	(p.value(	x4831	)))
filepoint.writelines	('\tx4832	'+	str	(p.value(	x4832	)))
filepoint.writelines	('\tx4833	'+	str	(p.value(	x4833	)))
filepoint.writelines	('\tx4834	'+	str	(p.value(	x4834	)))
filepoint.writelines	('\tx4835	'+	str	(p.value(	x4835	)))
filepoint.writelines	('\tx4836	'+	str	(p.value(	x4836	)))
filepoint.writelines	('\tx4837	'+	str	(p.value(	x4837	)))
filepoint.writelines	('\tx4838	'+	str	(p.value(	x4838	)))
filepoint.writelines	('\tx4839	'+	str	(p.value(	x4839	)))
filepoint.writelines	('\tx4840	'+	str	(p.value(	x4840	)))
filepoint.writelines	('\tx4841	'+	str	(p.value(	x4841	)))
filepoint.writelines	('\tx4842	'+	str	(p.value(	x4842	)))
filepoint.writelines	('\tx4843	'+	str	(p.value(	x4843	)))
filepoint.writelines	('\tx4844	'+	str	(p.value(	x4844	)))
filepoint.writelines	('\tx4845	'+	str	(p.value(	x4845	)))
filepoint.writelines	('\tx4846	'+	str	(p.value(	x4846	)))
filepoint.writelines	('\tx4847	'+	str	(p.value(	x4847	)))
filepoint.writelines	('\tx4848	'+	str	(p.value(	x4848	)))
filepoint.writelines	('\tx4849	'+	str	(p.value(	x4849	)))
filepoint.writelines	('\tx4850	'+	str	(p.value(	x4850	)))
filepoint.writelines	('\tx4851	'+	str	(p.value(	x4851	)))
filepoint.writelines	('\tx4852	'+	str	(p.value(	x4852	)))
filepoint.writelines	('\tx4853	'+	str	(p.value(	x4853	)))
filepoint.writelines	('\tx4854	'+	str	(p.value(	x4854	)))
filepoint.writelines	('\tx4855	'+	str	(p.value(	x4855	)))
filepoint.writelines	('\tx4856	'+	str	(p.value(	x4856	)))
filepoint.writelines	('\tx4857	'+	str	(p.value(	x4857	)))
filepoint.writelines	('\tx4858	'+	str	(p.value(	x4858	)))
filepoint.writelines	('\tx4859	'+	str	(p.value(	x4859	)))
filepoint.writelines	('\tx4860	'+	str	(p.value(	x4860	)))
filepoint.writelines	('\tx4861	'+	str	(p.value(	x4861	)))
filepoint.writelines	('\tx4862	'+	str	(p.value(	x4862	)))
filepoint.writelines	('\tx4863	'+	str	(p.value(	x4863	)))
filepoint.writelines	('\tx4864	'+	str	(p.value(	x4864	)))
filepoint.writelines	('\tx4865	'+	str	(p.value(	x4865	)))
filepoint.writelines	('\tx4866	'+	str	(p.value(	x4866	)))
filepoint.writelines	('\tx4867	'+	str	(p.value(	x4867	)))
filepoint.writelines	('\tx4868	'+	str	(p.value(	x4868	)))
filepoint.writelines	('\tx4869	'+	str	(p.value(	x4869	)))
filepoint.writelines	('\tx4870	'+	str	(p.value(	x4870	)))
filepoint.writelines	('\tx4871	'+	str	(p.value(	x4871	)))
filepoint.writelines	('\tx4872	'+	str	(p.value(	x4872	)))
filepoint.writelines	('\tx4873	'+	str	(p.value(	x4873	)))
filepoint.writelines	('\tx4874	'+	str	(p.value(	x4874	)))
filepoint.writelines	('\tx4875	'+	str	(p.value(	x4875	)))
filepoint.writelines	('\tx4876	'+	str	(p.value(	x4876	)))
filepoint.writelines	('\tx4877	'+	str	(p.value(	x4877	)))
filepoint.writelines	('\tx4878	'+	str	(p.value(	x4878	)))
filepoint.writelines	('\tx4879	'+	str	(p.value(	x4879	)))
filepoint.writelines	('\tx4880	'+	str	(p.value(	x4880	)))
filepoint.writelines	('\tx4881	'+	str	(p.value(	x4881	)))
filepoint.writelines	('\tx4882	'+	str	(p.value(	x4882	)))
filepoint.writelines	('\tx4883	'+	str	(p.value(	x4883	)))
filepoint.writelines	('\tx4884	'+	str	(p.value(	x4884	)))
filepoint.writelines	('\tx4885	'+	str	(p.value(	x4885	)))
filepoint.writelines	('\tx4886	'+	str	(p.value(	x4886	)))
filepoint.writelines	('\tx4887	'+	str	(p.value(	x4887	)))
filepoint.writelines	('\tx4888	'+	str	(p.value(	x4888	)))
filepoint.writelines	('\tx4889	'+	str	(p.value(	x4889	)))
filepoint.writelines	('\tx4890	'+	str	(p.value(	x4890	)))
filepoint.writelines	('\tx4891	'+	str	(p.value(	x4891	)))
filepoint.writelines	('\tx4892	'+	str	(p.value(	x4892	)))
filepoint.writelines	('\tx4893	'+	str	(p.value(	x4893	)))
filepoint.writelines	('\tx4894	'+	str	(p.value(	x4894	)))
filepoint.writelines	('\tx4895	'+	str	(p.value(	x4895	)))
filepoint.writelines	('\tx4896	'+	str	(p.value(	x4896	)))
filepoint.writelines	('\tx4897	'+	str	(p.value(	x4897	)))
filepoint.writelines	('\tx4898	'+	str	(p.value(	x4898	)))
filepoint.writelines	('\tx4899	'+	str	(p.value(	x4899	)))
filepoint.writelines	('\tx4900	'+	str	(p.value(	x4900	)))
filepoint.writelines	('\tx4901	'+	str	(p.value(	x4901	)))
filepoint.writelines	('\tx4902	'+	str	(p.value(	x4902	)))
filepoint.writelines	('\tx4903	'+	str	(p.value(	x4903	)))
filepoint.writelines	('\tx4904	'+	str	(p.value(	x4904	)))
filepoint.writelines	('\tx4905	'+	str	(p.value(	x4905	)))
filepoint.writelines	('\tx4906	'+	str	(p.value(	x4906	)))
filepoint.writelines	('\tx4907	'+	str	(p.value(	x4907	)))
filepoint.writelines	('\tx4908	'+	str	(p.value(	x4908	)))
filepoint.writelines	('\tx4909	'+	str	(p.value(	x4909	)))
filepoint.writelines	('\tx4910	'+	str	(p.value(	x4910	)))
filepoint.writelines	('\tx4911	'+	str	(p.value(	x4911	)))
filepoint.writelines	('\tx4912	'+	str	(p.value(	x4912	)))
filepoint.writelines	('\tx4913	'+	str	(p.value(	x4913	)))
filepoint.writelines	('\tx4914	'+	str	(p.value(	x4914	)))
filepoint.writelines	('\tx4915	'+	str	(p.value(	x4915	)))
filepoint.writelines	('\tx4916	'+	str	(p.value(	x4916	)))
filepoint.writelines	('\tx4917	'+	str	(p.value(	x4917	)))
filepoint.writelines	('\tx4918	'+	str	(p.value(	x4918	)))
filepoint.writelines	('\tx4919	'+	str	(p.value(	x4919	)))
filepoint.writelines	('\tx4920	'+	str	(p.value(	x4920	)))
filepoint.writelines	('\tx4921	'+	str	(p.value(	x4921	)))
filepoint.writelines	('\tx4922	'+	str	(p.value(	x4922	)))
filepoint.writelines	('\tx4923	'+	str	(p.value(	x4923	)))
filepoint.writelines	('\tx4924	'+	str	(p.value(	x4924	)))
filepoint.writelines	('\tx4925	'+	str	(p.value(	x4925	)))
filepoint.writelines	('\tx4926	'+	str	(p.value(	x4926	)))
filepoint.writelines	('\tx4927	'+	str	(p.value(	x4927	)))
filepoint.writelines	('\tx4928	'+	str	(p.value(	x4928	)))
filepoint.writelines	('\tx4929	'+	str	(p.value(	x4929	)))
filepoint.writelines	('\tx4930	'+	str	(p.value(	x4930	)))
filepoint.writelines	('\tx4931	'+	str	(p.value(	x4931	)))
filepoint.writelines	('\tx4932	'+	str	(p.value(	x4932	)))
filepoint.writelines	('\tx4933	'+	str	(p.value(	x4933	)))
filepoint.writelines	('\tx4934	'+	str	(p.value(	x4934	)))
filepoint.writelines	('\tx4935	'+	str	(p.value(	x4935	)))
filepoint.writelines	('\tx4936	'+	str	(p.value(	x4936	)))
filepoint.writelines	('\tx4937	'+	str	(p.value(	x4937	)))
filepoint.writelines	('\tx4938	'+	str	(p.value(	x4938	)))
filepoint.writelines	('\tx4939	'+	str	(p.value(	x4939	)))
filepoint.writelines	('\tx4940	'+	str	(p.value(	x4940	)))
filepoint.writelines	('\tx4941	'+	str	(p.value(	x4941	)))
filepoint.writelines	('\tx4942	'+	str	(p.value(	x4942	)))
filepoint.writelines	('\tx4943	'+	str	(p.value(	x4943	)))
filepoint.writelines	('\tx4944	'+	str	(p.value(	x4944	)))
filepoint.writelines	('\tx4945	'+	str	(p.value(	x4945	)))
filepoint.writelines	('\tx4946	'+	str	(p.value(	x4946	)))
filepoint.writelines	('\tx4947	'+	str	(p.value(	x4947	)))
filepoint.writelines	('\tx4948	'+	str	(p.value(	x4948	)))
filepoint.writelines	('\tx4949	'+	str	(p.value(	x4949	)))
filepoint.writelines	('\tx4950	'+	str	(p.value(	x4950	)))
filepoint.writelines	('\tx4951	'+	str	(p.value(	x4951	)))
filepoint.writelines	('\tx4952	'+	str	(p.value(	x4952	)))
filepoint.writelines	('\tx4953	'+	str	(p.value(	x4953	)))
filepoint.writelines	('\tx4954	'+	str	(p.value(	x4954	)))
filepoint.writelines	('\tx4955	'+	str	(p.value(	x4955	)))
filepoint.writelines	('\tx4956	'+	str	(p.value(	x4956	)))
filepoint.writelines	('\tx4957	'+	str	(p.value(	x4957	)))
filepoint.writelines	('\tx4958	'+	str	(p.value(	x4958	)))
filepoint.writelines	('\tx4959	'+	str	(p.value(	x4959	)))
filepoint.writelines	('\tx4960	'+	str	(p.value(	x4960	)))
filepoint.writelines	('\tx4961	'+	str	(p.value(	x4961	)))
filepoint.writelines	('\tx4962	'+	str	(p.value(	x4962	)))
filepoint.writelines	('\tx4963	'+	str	(p.value(	x4963	)))
filepoint.writelines	('\tx4964	'+	str	(p.value(	x4964	)))
filepoint.writelines	('\tx4965	'+	str	(p.value(	x4965	)))
filepoint.writelines	('\tx4966	'+	str	(p.value(	x4966	)))
filepoint.writelines	('\tx4967	'+	str	(p.value(	x4967	)))
filepoint.writelines	('\tx4968	'+	str	(p.value(	x4968	)))
filepoint.writelines	('\tx4969	'+	str	(p.value(	x4969	)))
filepoint.writelines	('\tx4970	'+	str	(p.value(	x4970	)))
filepoint.writelines	('\tx4971	'+	str	(p.value(	x4971	)))
filepoint.writelines	('\tx4972	'+	str	(p.value(	x4972	)))
filepoint.writelines	('\tx4973	'+	str	(p.value(	x4973	)))
filepoint.writelines	('\tx4974	'+	str	(p.value(	x4974	)))
filepoint.writelines	('\tx4975	'+	str	(p.value(	x4975	)))
filepoint.writelines	('\tx4976	'+	str	(p.value(	x4976	)))
filepoint.writelines	('\tx4977	'+	str	(p.value(	x4977	)))
filepoint.writelines	('\tx4978	'+	str	(p.value(	x4978	)))
filepoint.writelines	('\tx4979	'+	str	(p.value(	x4979	)))
filepoint.writelines	('\tx4980	'+	str	(p.value(	x4980	)))
filepoint.writelines	('\tx4981	'+	str	(p.value(	x4981	)))
filepoint.writelines	('\tx4982	'+	str	(p.value(	x4982	)))
filepoint.writelines	('\tx4983	'+	str	(p.value(	x4983	)))
filepoint.writelines	('\tx4984	'+	str	(p.value(	x4984	)))
filepoint.writelines	('\tx4985	'+	str	(p.value(	x4985	)))
filepoint.writelines	('\tx4986	'+	str	(p.value(	x4986	)))
filepoint.writelines	('\tx4987	'+	str	(p.value(	x4987	)))
filepoint.writelines	('\tx4988	'+	str	(p.value(	x4988	)))
filepoint.writelines	('\tx4989	'+	str	(p.value(	x4989	)))
filepoint.writelines	('\tx4990	'+	str	(p.value(	x4990	)))
filepoint.writelines	('\tx4991	'+	str	(p.value(	x4991	)))
filepoint.writelines	('\tx4992	'+	str	(p.value(	x4992	)))
filepoint.writelines	('\tx4993	'+	str	(p.value(	x4993	)))
filepoint.writelines	('\tx4994	'+	str	(p.value(	x4994	)))
filepoint.writelines	('\tx4995	'+	str	(p.value(	x4995	)))
filepoint.writelines	('\tx4996	'+	str	(p.value(	x4996	)))
filepoint.writelines	('\tx4997	'+	str	(p.value(	x4997	)))
filepoint.writelines	('\tx4998	'+	str	(p.value(	x4998	)))
filepoint.writelines	('\tx4999	'+	str	(p.value(	x4999	)))
filepoint.writelines	('\tx5000	'+	str	(p.value(	x5000	)))
filepoint.writelines	('\tx5001	'+	str	(p.value(	x5001	)))
filepoint.writelines	('\tx5002	'+	str	(p.value(	x5002	)))
filepoint.writelines	('\tx5003	'+	str	(p.value(	x5003	)))
filepoint.writelines	('\tx5004	'+	str	(p.value(	x5004	)))
filepoint.writelines	('\tx5005	'+	str	(p.value(	x5005	)))
filepoint.writelines	('\tx5006	'+	str	(p.value(	x5006	)))
filepoint.writelines	('\tx5007	'+	str	(p.value(	x5007	)))
filepoint.writelines	('\tx5008	'+	str	(p.value(	x5008	)))
filepoint.writelines	('\tx5009	'+	str	(p.value(	x5009	)))
filepoint.writelines	('\tx5010	'+	str	(p.value(	x5010	)))
filepoint.writelines	('\tx5011	'+	str	(p.value(	x5011	)))
filepoint.writelines	('\tx5012	'+	str	(p.value(	x5012	)))
filepoint.writelines	('\tx5013	'+	str	(p.value(	x5013	)))
filepoint.writelines	('\tx5014	'+	str	(p.value(	x5014	)))
filepoint.writelines	('\tx5015	'+	str	(p.value(	x5015	)))
filepoint.writelines	('\tx5016	'+	str	(p.value(	x5016	)))
filepoint.writelines	('\tx5017	'+	str	(p.value(	x5017	)))
filepoint.writelines	('\tx5018	'+	str	(p.value(	x5018	)))
filepoint.writelines	('\tx5019	'+	str	(p.value(	x5019	)))
filepoint.writelines	('\tx5020	'+	str	(p.value(	x5020	)))
filepoint.writelines	('\tx5021	'+	str	(p.value(	x5021	)))
filepoint.writelines	('\tx5022	'+	str	(p.value(	x5022	)))
filepoint.writelines	('\tx5023	'+	str	(p.value(	x5023	)))
filepoint.writelines	('\tx5024	'+	str	(p.value(	x5024	)))
filepoint.writelines	('\tx5025	'+	str	(p.value(	x5025	)))
filepoint.writelines	('\tx5026	'+	str	(p.value(	x5026	)))
filepoint.writelines	('\tx5027	'+	str	(p.value(	x5027	)))
filepoint.writelines	('\tx5028	'+	str	(p.value(	x5028	)))
filepoint.writelines	('\tx5029	'+	str	(p.value(	x5029	)))
filepoint.writelines	('\tx5030	'+	str	(p.value(	x5030	)))
filepoint.writelines	('\tx5031	'+	str	(p.value(	x5031	)))
filepoint.writelines	('\tx5032	'+	str	(p.value(	x5032	)))
filepoint.writelines	('\tx5033	'+	str	(p.value(	x5033	)))
filepoint.writelines	('\tx5034	'+	str	(p.value(	x5034	)))
filepoint.writelines	('\tx5035	'+	str	(p.value(	x5035	)))
filepoint.writelines	('\tx5036	'+	str	(p.value(	x5036	)))
filepoint.writelines	('\tx5037	'+	str	(p.value(	x5037	)))
filepoint.writelines	('\tx5038	'+	str	(p.value(	x5038	)))
filepoint.writelines	('\tx5039	'+	str	(p.value(	x5039	)))
filepoint.writelines	('\tx5040	'+	str	(p.value(	x5040	)))
filepoint.writelines	('\tx5041	'+	str	(p.value(	x5041	)))
filepoint.writelines	('\tx5042	'+	str	(p.value(	x5042	)))
filepoint.writelines	('\tx5043	'+	str	(p.value(	x5043	)))
filepoint.writelines	('\tx5044	'+	str	(p.value(	x5044	)))
filepoint.writelines	('\tx5045	'+	str	(p.value(	x5045	)))
filepoint.writelines	('\tx5046	'+	str	(p.value(	x5046	)))
filepoint.writelines	('\tx5047	'+	str	(p.value(	x5047	)))
filepoint.writelines	('\tx5048	'+	str	(p.value(	x5048	)))
filepoint.writelines	('\tx5049	'+	str	(p.value(	x5049	)))
filepoint.writelines	('\tx5050	'+	str	(p.value(	x5050	)))
filepoint.writelines	('\tx5051	'+	str	(p.value(	x5051	)))
filepoint.writelines	('\tx5052	'+	str	(p.value(	x5052	)))
filepoint.writelines	('\tx5053	'+	str	(p.value(	x5053	)))
filepoint.writelines	('\tx5054	'+	str	(p.value(	x5054	)))
filepoint.writelines	('\tx5055	'+	str	(p.value(	x5055	)))
filepoint.writelines	('\tx5056	'+	str	(p.value(	x5056	)))
filepoint.writelines	('\tx5057	'+	str	(p.value(	x5057	)))
filepoint.writelines	('\tx5058	'+	str	(p.value(	x5058	)))
filepoint.writelines	('\tx5059	'+	str	(p.value(	x5059	)))
filepoint.writelines	('\tx5060	'+	str	(p.value(	x5060	)))
filepoint.writelines	('\tx5061	'+	str	(p.value(	x5061	)))
filepoint.writelines	('\tx5062	'+	str	(p.value(	x5062	)))
filepoint.writelines	('\tx5063	'+	str	(p.value(	x5063	)))
filepoint.writelines	('\tx5064	'+	str	(p.value(	x5064	)))
filepoint.writelines	('\tx5065	'+	str	(p.value(	x5065	)))
filepoint.writelines	('\tx5066	'+	str	(p.value(	x5066	)))
filepoint.writelines	('\tx5067	'+	str	(p.value(	x5067	)))
filepoint.writelines	('\tx5068	'+	str	(p.value(	x5068	)))
filepoint.writelines	('\tx5069	'+	str	(p.value(	x5069	)))
filepoint.writelines	('\tx5070	'+	str	(p.value(	x5070	)))
filepoint.writelines	('\tx5071	'+	str	(p.value(	x5071	)))
filepoint.writelines	('\tx5072	'+	str	(p.value(	x5072	)))
filepoint.writelines	('\tx5073	'+	str	(p.value(	x5073	)))
filepoint.writelines	('\tx5074	'+	str	(p.value(	x5074	)))
filepoint.writelines	('\tx5075	'+	str	(p.value(	x5075	)))
filepoint.writelines	('\tx5076	'+	str	(p.value(	x5076	)))
filepoint.writelines	('\tx5077	'+	str	(p.value(	x5077	)))
filepoint.writelines	('\tx5078	'+	str	(p.value(	x5078	)))
filepoint.writelines	('\tx5079	'+	str	(p.value(	x5079	)))
filepoint.writelines	('\tx5080	'+	str	(p.value(	x5080	)))
filepoint.writelines	('\tx5081	'+	str	(p.value(	x5081	)))
filepoint.writelines	('\tx5082	'+	str	(p.value(	x5082	)))
filepoint.writelines	('\tx5083	'+	str	(p.value(	x5083	)))
filepoint.writelines	('\tx5084	'+	str	(p.value(	x5084	)))
filepoint.writelines	('\tx5085	'+	str	(p.value(	x5085	)))
filepoint.writelines	('\tx5086	'+	str	(p.value(	x5086	)))
filepoint.writelines	('\tx5087	'+	str	(p.value(	x5087	)))
filepoint.writelines	('\tx5088	'+	str	(p.value(	x5088	)))
filepoint.writelines	('\tx5089	'+	str	(p.value(	x5089	)))
filepoint.writelines	('\tx5090	'+	str	(p.value(	x5090	)))
filepoint.writelines	('\tx5091	'+	str	(p.value(	x5091	)))
filepoint.writelines	('\tx5092	'+	str	(p.value(	x5092	)))
filepoint.writelines	('\tx5093	'+	str	(p.value(	x5093	)))
filepoint.writelines	('\tx5094	'+	str	(p.value(	x5094	)))
filepoint.writelines	('\tx5095	'+	str	(p.value(	x5095	)))
filepoint.writelines	('\tx5096	'+	str	(p.value(	x5096	)))
filepoint.writelines	('\tx5097	'+	str	(p.value(	x5097	)))
filepoint.writelines	('\tx5098	'+	str	(p.value(	x5098	)))
filepoint.writelines	('\tx5099	'+	str	(p.value(	x5099	)))
filepoint.writelines	('\tx5100	'+	str	(p.value(	x5100	)))
filepoint.writelines	('\tx5101	'+	str	(p.value(	x5101	)))
filepoint.writelines	('\tx5102	'+	str	(p.value(	x5102	)))
filepoint.writelines	('\tx5103	'+	str	(p.value(	x5103	)))
filepoint.writelines	('\tx5104	'+	str	(p.value(	x5104	)))
filepoint.writelines	('\tx5105	'+	str	(p.value(	x5105	)))
filepoint.writelines	('\tx5106	'+	str	(p.value(	x5106	)))
filepoint.writelines	('\tx5107	'+	str	(p.value(	x5107	)))
filepoint.writelines	('\tx5108	'+	str	(p.value(	x5108	)))
filepoint.writelines	('\tx5109	'+	str	(p.value(	x5109	)))
filepoint.writelines	('\tx5110	'+	str	(p.value(	x5110	)))
filepoint.writelines	('\tx5111	'+	str	(p.value(	x5111	)))
filepoint.writelines	('\tx5112	'+	str	(p.value(	x5112	)))
filepoint.writelines	('\tx5113	'+	str	(p.value(	x5113	)))
filepoint.writelines	('\tx5114	'+	str	(p.value(	x5114	)))
filepoint.writelines	('\tx5115	'+	str	(p.value(	x5115	)))
filepoint.writelines	('\tx5116	'+	str	(p.value(	x5116	)))
filepoint.writelines	('\tx5117	'+	str	(p.value(	x5117	)))
filepoint.writelines	('\tx5118	'+	str	(p.value(	x5118	)))
filepoint.writelines	('\tx5119	'+	str	(p.value(	x5119	)))
filepoint.writelines	('\tx5120	'+	str	(p.value(	x5120	)))
filepoint.writelines	('\tx5121	'+	str	(p.value(	x5121	)))
filepoint.writelines	('\tx5122	'+	str	(p.value(	x5122	)))
filepoint.writelines	('\tx5123	'+	str	(p.value(	x5123	)))
filepoint.writelines	('\tx5124	'+	str	(p.value(	x5124	)))
filepoint.writelines	('\tx5125	'+	str	(p.value(	x5125	)))
filepoint.writelines	('\tx5126	'+	str	(p.value(	x5126	)))
filepoint.writelines	('\tx5127	'+	str	(p.value(	x5127	)))
filepoint.writelines	('\tx5128	'+	str	(p.value(	x5128	)))
filepoint.writelines	('\tx5129	'+	str	(p.value(	x5129	)))
filepoint.writelines	('\tx5130	'+	str	(p.value(	x5130	)))
filepoint.writelines	('\tx5131	'+	str	(p.value(	x5131	)))
filepoint.writelines	('\tx5132	'+	str	(p.value(	x5132	)))
filepoint.writelines	('\tx5133	'+	str	(p.value(	x5133	)))
filepoint.writelines	('\tx5134	'+	str	(p.value(	x5134	)))
filepoint.writelines	('\tx5135	'+	str	(p.value(	x5135	)))
filepoint.writelines	('\tx5136	'+	str	(p.value(	x5136	)))
filepoint.writelines	('\tx5137	'+	str	(p.value(	x5137	)))
filepoint.writelines	('\tx5138	'+	str	(p.value(	x5138	)))
filepoint.writelines	('\tx5139	'+	str	(p.value(	x5139	)))
filepoint.writelines	('\tx5140	'+	str	(p.value(	x5140	)))
filepoint.writelines	('\tx5141	'+	str	(p.value(	x5141	)))
filepoint.writelines	('\tx5142	'+	str	(p.value(	x5142	)))
filepoint.writelines	('\tx5143	'+	str	(p.value(	x5143	)))
filepoint.writelines	('\tx5144	'+	str	(p.value(	x5144	)))
filepoint.writelines	('\tx5145	'+	str	(p.value(	x5145	)))
filepoint.writelines	('\tx5146	'+	str	(p.value(	x5146	)))
filepoint.writelines	('\tx5147	'+	str	(p.value(	x5147	)))
filepoint.writelines	('\tx5148	'+	str	(p.value(	x5148	)))
filepoint.writelines	('\tx5149	'+	str	(p.value(	x5149	)))
filepoint.writelines	('\tx5150	'+	str	(p.value(	x5150	)))
filepoint.writelines	('\tx5151	'+	str	(p.value(	x5151	)))
filepoint.writelines	('\tx5152	'+	str	(p.value(	x5152	)))
filepoint.writelines	('\tx5153	'+	str	(p.value(	x5153	)))
filepoint.writelines	('\tx5154	'+	str	(p.value(	x5154	)))
filepoint.writelines	('\tx5155	'+	str	(p.value(	x5155	)))
filepoint.writelines	('\tx5156	'+	str	(p.value(	x5156	)))
filepoint.writelines	('\tx5157	'+	str	(p.value(	x5157	)))
filepoint.writelines	('\tx5158	'+	str	(p.value(	x5158	)))
filepoint.writelines	('\tx5159	'+	str	(p.value(	x5159	)))
filepoint.writelines	('\tx5160	'+	str	(p.value(	x5160	)))
filepoint.writelines	('\tx5161	'+	str	(p.value(	x5161	)))
filepoint.writelines	('\tx5162	'+	str	(p.value(	x5162	)))
filepoint.writelines	('\tx5163	'+	str	(p.value(	x5163	)))
filepoint.writelines	('\tx5164	'+	str	(p.value(	x5164	)))
filepoint.writelines	('\tx5165	'+	str	(p.value(	x5165	)))
filepoint.writelines	('\tx5166	'+	str	(p.value(	x5166	)))
filepoint.writelines	('\tx5167	'+	str	(p.value(	x5167	)))
filepoint.writelines	('\tx5168	'+	str	(p.value(	x5168	)))
filepoint.writelines	('\tx5169	'+	str	(p.value(	x5169	)))
filepoint.writelines	('\tx5170	'+	str	(p.value(	x5170	)))
filepoint.writelines	('\tx5171	'+	str	(p.value(	x5171	)))
filepoint.writelines	('\tx5172	'+	str	(p.value(	x5172	)))
filepoint.writelines	('\tx5173	'+	str	(p.value(	x5173	)))
filepoint.writelines	('\tx5174	'+	str	(p.value(	x5174	)))
filepoint.writelines	('\tx5175	'+	str	(p.value(	x5175	)))
filepoint.writelines	('\tx5176	'+	str	(p.value(	x5176	)))
filepoint.writelines	('\tx5177	'+	str	(p.value(	x5177	)))
filepoint.writelines	('\tx5178	'+	str	(p.value(	x5178	)))
filepoint.writelines	('\tx5179	'+	str	(p.value(	x5179	)))
filepoint.writelines	('\tx5180	'+	str	(p.value(	x5180	)))
filepoint.writelines	('\tx5181	'+	str	(p.value(	x5181	)))
filepoint.writelines	('\tx5182	'+	str	(p.value(	x5182	)))
filepoint.writelines	('\tx5183	'+	str	(p.value(	x5183	)))
filepoint.writelines	('\tx5184	'+	str	(p.value(	x5184	)))
filepoint.writelines	('\tx5185	'+	str	(p.value(	x5185	)))
filepoint.writelines	('\tx5186	'+	str	(p.value(	x5186	)))
filepoint.writelines	('\tx5187	'+	str	(p.value(	x5187	)))
filepoint.writelines	('\tx5188	'+	str	(p.value(	x5188	)))
filepoint.writelines	('\tx5189	'+	str	(p.value(	x5189	)))
filepoint.writelines	('\tx5190	'+	str	(p.value(	x5190	)))
filepoint.writelines	('\tx5191	'+	str	(p.value(	x5191	)))
filepoint.writelines	('\tx5192	'+	str	(p.value(	x5192	)))
filepoint.writelines	('\tx5193	'+	str	(p.value(	x5193	)))
filepoint.writelines	('\tx5194	'+	str	(p.value(	x5194	)))
filepoint.writelines	('\tx5195	'+	str	(p.value(	x5195	)))
filepoint.writelines	('\tx5196	'+	str	(p.value(	x5196	)))
filepoint.writelines	('\tx5197	'+	str	(p.value(	x5197	)))
filepoint.writelines	('\tx5198	'+	str	(p.value(	x5198	)))
filepoint.writelines	('\tx5199	'+	str	(p.value(	x5199	)))
filepoint.writelines	('\tx5200	'+	str	(p.value(	x5200	)))
filepoint.writelines	('\tx5201	'+	str	(p.value(	x5201	)))
filepoint.writelines	('\tx5202	'+	str	(p.value(	x5202	)))
filepoint.writelines	('\tx5203	'+	str	(p.value(	x5203	)))
filepoint.writelines	('\tx5204	'+	str	(p.value(	x5204	)))
filepoint.writelines	('\tx5205	'+	str	(p.value(	x5205	)))
filepoint.writelines	('\tx5206	'+	str	(p.value(	x5206	)))
filepoint.writelines	('\tx5207	'+	str	(p.value(	x5207	)))
filepoint.writelines	('\tx5208	'+	str	(p.value(	x5208	)))
filepoint.writelines	('\tx5209	'+	str	(p.value(	x5209	)))
filepoint.writelines	('\tx5210	'+	str	(p.value(	x5210	)))
filepoint.writelines	('\tx5211	'+	str	(p.value(	x5211	)))
filepoint.writelines	('\tx5212	'+	str	(p.value(	x5212	)))
filepoint.writelines	('\tx5213	'+	str	(p.value(	x5213	)))
filepoint.writelines	('\tx5214	'+	str	(p.value(	x5214	)))
filepoint.writelines	('\tx5215	'+	str	(p.value(	x5215	)))
filepoint.writelines	('\tx5216	'+	str	(p.value(	x5216	)))
filepoint.writelines	('\tx5217	'+	str	(p.value(	x5217	)))
filepoint.writelines	('\tx5218	'+	str	(p.value(	x5218	)))
filepoint.writelines	('\tx5219	'+	str	(p.value(	x5219	)))
filepoint.writelines	('\tx5220	'+	str	(p.value(	x5220	)))
filepoint.writelines	('\tx5221	'+	str	(p.value(	x5221	)))
filepoint.writelines	('\tx5222	'+	str	(p.value(	x5222	)))
filepoint.writelines	('\tx5223	'+	str	(p.value(	x5223	)))
filepoint.writelines	('\tx5224	'+	str	(p.value(	x5224	)))
filepoint.writelines	('\tx5225	'+	str	(p.value(	x5225	)))
filepoint.writelines	('\tx5226	'+	str	(p.value(	x5226	)))
filepoint.writelines	('\tx5227	'+	str	(p.value(	x5227	)))
filepoint.writelines	('\tx5228	'+	str	(p.value(	x5228	)))
filepoint.writelines	('\tx5229	'+	str	(p.value(	x5229	)))
filepoint.writelines	('\tx5230	'+	str	(p.value(	x5230	)))
filepoint.writelines	('\tx5231	'+	str	(p.value(	x5231	)))
filepoint.writelines	('\tx5232	'+	str	(p.value(	x5232	)))
filepoint.writelines	('\tx5233	'+	str	(p.value(	x5233	)))
filepoint.writelines	('\tx5234	'+	str	(p.value(	x5234	)))
filepoint.writelines	('\tx5235	'+	str	(p.value(	x5235	)))
filepoint.writelines	('\tx5236	'+	str	(p.value(	x5236	)))
filepoint.writelines	('\tx5237	'+	str	(p.value(	x5237	)))
filepoint.writelines	('\tx5238	'+	str	(p.value(	x5238	)))
filepoint.writelines	('\tx5239	'+	str	(p.value(	x5239	)))
filepoint.writelines	('\tx5240	'+	str	(p.value(	x5240	)))
filepoint.writelines	('\tx5241	'+	str	(p.value(	x5241	)))
filepoint.writelines	('\tx5242	'+	str	(p.value(	x5242	)))
filepoint.writelines	('\tx5243	'+	str	(p.value(	x5243	)))
filepoint.writelines	('\tx5244	'+	str	(p.value(	x5244	)))
filepoint.writelines	('\tx5245	'+	str	(p.value(	x5245	)))
filepoint.writelines	('\tx5246	'+	str	(p.value(	x5246	)))
filepoint.writelines	('\tx5247	'+	str	(p.value(	x5247	)))
filepoint.writelines	('\tx5248	'+	str	(p.value(	x5248	)))
filepoint.writelines	('\tx5249	'+	str	(p.value(	x5249	)))
filepoint.writelines	('\tx5250	'+	str	(p.value(	x5250	)))
filepoint.writelines	('\tx5251	'+	str	(p.value(	x5251	)))
filepoint.writelines	('\tx5252	'+	str	(p.value(	x5252	)))
filepoint.writelines	('\tx5253	'+	str	(p.value(	x5253	)))
filepoint.writelines	('\tx5254	'+	str	(p.value(	x5254	)))
filepoint.writelines	('\tx5255	'+	str	(p.value(	x5255	)))
filepoint.writelines	('\tx5256	'+	str	(p.value(	x5256	)))
filepoint.writelines	('\tx5257	'+	str	(p.value(	x5257	)))
filepoint.writelines	('\tx5258	'+	str	(p.value(	x5258	)))
filepoint.writelines	('\tx5259	'+	str	(p.value(	x5259	)))
filepoint.writelines	('\tx5260	'+	str	(p.value(	x5260	)))
filepoint.writelines	('\tx5261	'+	str	(p.value(	x5261	)))
filepoint.writelines	('\tx5262	'+	str	(p.value(	x5262	)))
filepoint.writelines	('\tx5263	'+	str	(p.value(	x5263	)))
filepoint.writelines	('\tx5264	'+	str	(p.value(	x5264	)))
filepoint.writelines	('\tx5265	'+	str	(p.value(	x5265	)))
filepoint.writelines	('\tx5266	'+	str	(p.value(	x5266	)))
filepoint.writelines	('\tx5267	'+	str	(p.value(	x5267	)))
filepoint.writelines	('\tx5268	'+	str	(p.value(	x5268	)))
filepoint.writelines	('\tx5269	'+	str	(p.value(	x5269	)))
filepoint.writelines	('\tx5270	'+	str	(p.value(	x5270	)))
filepoint.writelines	('\tx5271	'+	str	(p.value(	x5271	)))
filepoint.writelines	('\tx5272	'+	str	(p.value(	x5272	)))
filepoint.writelines	('\tx5273	'+	str	(p.value(	x5273	)))
filepoint.writelines	('\tx5274	'+	str	(p.value(	x5274	)))
filepoint.writelines	('\tx5275	'+	str	(p.value(	x5275	)))
filepoint.writelines	('\tx5276	'+	str	(p.value(	x5276	)))
filepoint.writelines	('\tx5277	'+	str	(p.value(	x5277	)))
filepoint.writelines	('\tx5278	'+	str	(p.value(	x5278	)))
filepoint.writelines	('\tx5279	'+	str	(p.value(	x5279	)))
filepoint.writelines	('\tx5280	'+	str	(p.value(	x5280	)))
filepoint.writelines	('\tx5281	'+	str	(p.value(	x5281	)))
filepoint.writelines	('\tx5282	'+	str	(p.value(	x5282	)))
filepoint.writelines	('\tx5283	'+	str	(p.value(	x5283	)))
filepoint.writelines	('\tx5284	'+	str	(p.value(	x5284	)))
filepoint.writelines	('\tx5285	'+	str	(p.value(	x5285	)))
filepoint.writelines	('\tx5286	'+	str	(p.value(	x5286	)))
filepoint.writelines	('\tx5287	'+	str	(p.value(	x5287	)))
filepoint.writelines	('\tx5288	'+	str	(p.value(	x5288	)))
filepoint.writelines	('\tx5289	'+	str	(p.value(	x5289	)))
filepoint.writelines	('\tx5290	'+	str	(p.value(	x5290	)))
filepoint.writelines	('\tx5291	'+	str	(p.value(	x5291	)))
filepoint.writelines	('\tx5292	'+	str	(p.value(	x5292	)))
filepoint.writelines	('\tx5293	'+	str	(p.value(	x5293	)))
filepoint.writelines	('\tx5294	'+	str	(p.value(	x5294	)))
filepoint.writelines	('\tx5295	'+	str	(p.value(	x5295	)))
filepoint.writelines	('\tx5296	'+	str	(p.value(	x5296	)))
filepoint.writelines	('\tx5297	'+	str	(p.value(	x5297	)))
filepoint.writelines	('\tx5298	'+	str	(p.value(	x5298	)))
filepoint.writelines	('\tx5299	'+	str	(p.value(	x5299	)))
filepoint.writelines	('\tx5300	'+	str	(p.value(	x5300	)))
filepoint.writelines	('\tx5301	'+	str	(p.value(	x5301	)))
filepoint.writelines	('\tx5302	'+	str	(p.value(	x5302	)))
filepoint.writelines	('\tx5303	'+	str	(p.value(	x5303	)))
filepoint.writelines	('\tx5304	'+	str	(p.value(	x5304	)))
filepoint.writelines	('\tx5305	'+	str	(p.value(	x5305	)))
filepoint.writelines	('\tx5306	'+	str	(p.value(	x5306	)))
filepoint.writelines	('\tx5307	'+	str	(p.value(	x5307	)))
filepoint.writelines	('\tx5308	'+	str	(p.value(	x5308	)))
filepoint.writelines	('\tx5309	'+	str	(p.value(	x5309	)))
filepoint.writelines	('\tx5310	'+	str	(p.value(	x5310	)))
filepoint.writelines	('\tx5311	'+	str	(p.value(	x5311	)))
filepoint.writelines	('\tx5312	'+	str	(p.value(	x5312	)))
filepoint.writelines	('\tx5313	'+	str	(p.value(	x5313	)))
filepoint.writelines	('\tx5314	'+	str	(p.value(	x5314	)))
filepoint.writelines	('\tx5315	'+	str	(p.value(	x5315	)))
filepoint.writelines	('\tx5316	'+	str	(p.value(	x5316	)))
filepoint.writelines	('\tx5317	'+	str	(p.value(	x5317	)))
filepoint.writelines	('\tx5318	'+	str	(p.value(	x5318	)))
filepoint.writelines	('\tx5319	'+	str	(p.value(	x5319	)))
filepoint.writelines	('\tx5320	'+	str	(p.value(	x5320	)))
filepoint.writelines	('\tx5321	'+	str	(p.value(	x5321	)))
filepoint.writelines	('\tx5322	'+	str	(p.value(	x5322	)))
filepoint.writelines	('\tx5323	'+	str	(p.value(	x5323	)))
filepoint.writelines	('\tx5324	'+	str	(p.value(	x5324	)))
filepoint.writelines	('\tx5325	'+	str	(p.value(	x5325	)))
filepoint.writelines	('\tx5326	'+	str	(p.value(	x5326	)))
filepoint.writelines	('\tx5327	'+	str	(p.value(	x5327	)))
filepoint.writelines	('\tx5328	'+	str	(p.value(	x5328	)))
filepoint.writelines	('\tx5329	'+	str	(p.value(	x5329	)))
filepoint.writelines	('\tx5330	'+	str	(p.value(	x5330	)))
filepoint.writelines	('\tx5331	'+	str	(p.value(	x5331	)))
filepoint.writelines	('\tx5332	'+	str	(p.value(	x5332	)))
filepoint.writelines	('\tx5333	'+	str	(p.value(	x5333	)))
filepoint.writelines	('\tx5334	'+	str	(p.value(	x5334	)))
filepoint.writelines	('\tx5335	'+	str	(p.value(	x5335	)))
filepoint.writelines	('\tx5336	'+	str	(p.value(	x5336	)))
filepoint.writelines	('\tx5337	'+	str	(p.value(	x5337	)))
filepoint.writelines	('\tx5338	'+	str	(p.value(	x5338	)))
filepoint.writelines	('\tx5339	'+	str	(p.value(	x5339	)))
filepoint.writelines	('\tx5340	'+	str	(p.value(	x5340	)))
filepoint.writelines	('\tx5341	'+	str	(p.value(	x5341	)))
filepoint.writelines	('\tx5342	'+	str	(p.value(	x5342	)))
filepoint.writelines	('\tx5343	'+	str	(p.value(	x5343	)))
filepoint.writelines	('\tx5344	'+	str	(p.value(	x5344	)))
filepoint.writelines	('\tx5345	'+	str	(p.value(	x5345	)))
filepoint.writelines	('\tx5346	'+	str	(p.value(	x5346	)))
filepoint.writelines	('\tx5347	'+	str	(p.value(	x5347	)))
filepoint.writelines	('\tx5348	'+	str	(p.value(	x5348	)))
filepoint.writelines	('\tx5349	'+	str	(p.value(	x5349	)))
filepoint.writelines	('\tx5350	'+	str	(p.value(	x5350	)))
filepoint.writelines	('\tx5351	'+	str	(p.value(	x5351	)))
filepoint.writelines	('\tx5352	'+	str	(p.value(	x5352	)))
filepoint.writelines	('\tx5353	'+	str	(p.value(	x5353	)))
filepoint.writelines	('\tx5354	'+	str	(p.value(	x5354	)))
filepoint.writelines	('\tx5355	'+	str	(p.value(	x5355	)))
filepoint.writelines	('\tx5356	'+	str	(p.value(	x5356	)))
filepoint.writelines	('\tx5357	'+	str	(p.value(	x5357	)))
filepoint.writelines	('\tx5358	'+	str	(p.value(	x5358	)))
filepoint.writelines	('\tx5359	'+	str	(p.value(	x5359	)))
filepoint.writelines	('\tx5360	'+	str	(p.value(	x5360	)))
filepoint.writelines	('\tx5361	'+	str	(p.value(	x5361	)))
filepoint.writelines	('\tx5362	'+	str	(p.value(	x5362	)))
filepoint.writelines	('\tx5363	'+	str	(p.value(	x5363	)))
filepoint.writelines	('\tx5364	'+	str	(p.value(	x5364	)))
filepoint.writelines	('\tx5365	'+	str	(p.value(	x5365	)))
filepoint.writelines	('\tx5366	'+	str	(p.value(	x5366	)))
filepoint.writelines	('\tx5367	'+	str	(p.value(	x5367	)))
filepoint.writelines	('\tx5368	'+	str	(p.value(	x5368	)))
filepoint.writelines	('\tx5369	'+	str	(p.value(	x5369	)))
filepoint.writelines	('\tx5370	'+	str	(p.value(	x5370	)))
filepoint.writelines	('\tx5371	'+	str	(p.value(	x5371	)))
filepoint.writelines	('\tx5372	'+	str	(p.value(	x5372	)))
filepoint.writelines	('\tx5373	'+	str	(p.value(	x5373	)))
filepoint.writelines	('\tx5374	'+	str	(p.value(	x5374	)))
filepoint.writelines	('\tx5375	'+	str	(p.value(	x5375	)))
filepoint.writelines	('\tx5376	'+	str	(p.value(	x5376	)))
filepoint.writelines	('\tx5377	'+	str	(p.value(	x5377	)))
filepoint.writelines	('\tx5378	'+	str	(p.value(	x5378	)))
filepoint.writelines	('\tx5379	'+	str	(p.value(	x5379	)))
filepoint.writelines	('\tx5380	'+	str	(p.value(	x5380	)))
filepoint.writelines	('\tx5381	'+	str	(p.value(	x5381	)))
filepoint.writelines	('\tx5382	'+	str	(p.value(	x5382	)))
filepoint.writelines	('\tx5383	'+	str	(p.value(	x5383	)))
filepoint.writelines	('\tx5384	'+	str	(p.value(	x5384	)))
filepoint.writelines	('\tx5385	'+	str	(p.value(	x5385	)))
filepoint.writelines	('\tx5386	'+	str	(p.value(	x5386	)))
filepoint.writelines	('\tx5387	'+	str	(p.value(	x5387	)))
filepoint.writelines	('\tx5388	'+	str	(p.value(	x5388	)))
filepoint.writelines	('\tx5389	'+	str	(p.value(	x5389	)))
filepoint.writelines	('\tx5390	'+	str	(p.value(	x5390	)))
filepoint.writelines	('\tx5391	'+	str	(p.value(	x5391	)))
filepoint.writelines	('\tx5392	'+	str	(p.value(	x5392	)))
filepoint.writelines	('\tx5393	'+	str	(p.value(	x5393	)))
filepoint.writelines	('\tx5394	'+	str	(p.value(	x5394	)))
filepoint.writelines	('\tx5395	'+	str	(p.value(	x5395	)))
filepoint.writelines	('\tx5396	'+	str	(p.value(	x5396	)))
filepoint.writelines	('\tx5397	'+	str	(p.value(	x5397	)))
filepoint.writelines	('\tx5398	'+	str	(p.value(	x5398	)))
filepoint.writelines	('\tx5399	'+	str	(p.value(	x5399	)))
filepoint.writelines	('\tx5400	'+	str	(p.value(	x5400	)))
filepoint.writelines	('\tx5401	'+	str	(p.value(	x5401	)))
filepoint.writelines	('\tx5402	'+	str	(p.value(	x5402	)))
filepoint.writelines	('\tx5403	'+	str	(p.value(	x5403	)))

