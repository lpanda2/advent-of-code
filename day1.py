input_str = """76663
111378
132647
115688
67473
85562
62955
64052
104961
128687
60344
81158
129984
106462
55967
130004
140810
71523
64891
142922
122783
123918
116246
120842
105578
122950
107512
70051
55347
54348
89301
95258
122323
136781
137756
95658
91017
79626
98414
79296
75226
143850
131334
107028
76591
75492
66400
51904
79262
68956
98957
52481
87955
118871
148734
103699
68681
55118
144120
59403
115012
147742
124218
73580
114949
65346
113104
129059
119068
72339
74984
53095
127452
133786
111439
98153
96312
139641
88907
136831
73574
67871
57641
134505
72116
134503
134387
88598
78687
61020
107234
64801
132668
60204
90001
87833
131148
61488
107938
116072"""

modules = input_str.split('\n')
import math

def fuel(module):
    module = int(module)
    module /= 3
    module = math.floor(module)
    module -= 2
    return module

def fuel_up(module):
    module = int(module)
    module /= 3
    module = math.floor(module)
    module -= 2
    fuel_req = 0
    curr = module
    while curr > 0:
#        print(curr, fuel(curr))
        curr = fuel(curr)
        if curr > 0:
            fuel_req += curr
    return fuel_req + module

print('sum: ', sum([fuel(m) for m in modules]))
print('sum: ', sum([fuel_up(m) for m in modules]))
    
module_fuel = sum([fuel(m) for m in modules])


def int_code_program(code):
    code = code.split(',')
    code = [int(x) for x in code]
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    for chunk in chunks(code, 4):
        if (len(chunk) != 4) or (chunk[0] == 99):
            return ','.join([str(x) for x in code])
        op, a, b, c = chunk
        if op == 1:
            code[c] = code[a] + code[b]
        if op == 2:
            code[c] = code[a] * code[b]
    

def int_code_program_with_gravity_assist(code, noun, verb):
    code = code.split(',')
    code = [int(x) for x in code]

    code[1] = noun
    code[2] = verb
    
    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    for chunk in chunks(code, 4):
        if (len(chunk) != 4) or (chunk[0] == 99):
            return ','.join([str(x) for x in code])
        op, a, b, c = chunk
        if op == 1:
            code[c] = code[a] + code[b]
        if op == 2:
            code[c] = code[a] * code[b]
